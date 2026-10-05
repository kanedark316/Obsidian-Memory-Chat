"""Canonical chat transcript model and normalizers for paste + extension payloads."""

from __future__ import annotations

import hashlib
import re
from datetime import date, datetime, timezone
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator


class MessageRole(str, Enum):
    user = "user"
    assistant = "assistant"
    system = "system"
    other = "other"


class SourceKind(str, Enum):
    paste = "paste"
    extension = "extension"
    share = "share"


class ChatMessage(BaseModel):
    role: MessageRole
    content: str

    @field_validator("content")
    @classmethod
    def strip_content(cls, value: str) -> str:
        return value.strip()


class ChatTranscript(BaseModel):
    title: str
    messages: list[ChatMessage] = Field(default_factory=list)
    source: SourceKind
    url: str | None = None
    tags: list[str] = Field(default_factory=list)
    saved_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    conversation_date: date | None = None

    @field_validator("title")
    @classmethod
    def strip_title(cls, value: str) -> str:
        cleaned = value.strip() or "Untitled Chat"
        return cleaned

    def stable_key(self) -> str:
        if self.url:
            return hashlib.sha256(self.url.encode("utf-8")).hexdigest()[:16]
        first_user = next((m.content for m in self.messages if m.role == MessageRole.user), "")
        seed = f"{self.title}\n{first_user[:500]}"
        return hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16]

    def effective_date(self) -> date:
        if self.conversation_date:
            return self.conversation_date
        return self.saved_at.astimezone().date()


_ROLE_HEADING = re.compile(
    r"^(?:#{1,6}\s*)?(?:you|user|human|me|chatgpt|assistant|gpt|ai)\s*(?:said)?\s*:?\s*$",
    re.IGNORECASE,
)
_INLINE_ROLE = re.compile(
    r"^(you|user|human|me|chatgpt|assistant|gpt|ai)\s*(?:said)?\s*:\s*(.*)$",
    re.IGNORECASE,
)
_CHROME_LINES = re.compile(
    r"^(skip to content|chatgpt can make mistakes|new chat|share|copy|regenerate|"
    r"was this response useful|model:|temporary chat).*$",
    re.IGNORECASE,
)


def normalize_paste(
    text: str,
    *,
    title: str | None = None,
    tags: list[str] | None = None,
    url: str | None = None,
) -> ChatTranscript:
    cleaned = text.replace("\r\n", "\n").strip()
    messages = _parse_roles_from_text(cleaned)
    if not messages:
        messages = [ChatMessage(role=MessageRole.user, content=cleaned)] if cleaned else []

    derived_title = title or _first_line_title(cleaned) or "Untitled Chat"
    return ChatTranscript(
        title=derived_title,
        messages=messages,
        source=SourceKind.paste,
        url=url,
        tags=list(tags or []),
    )


def normalize_extension_payload(payload: dict[str, Any]) -> ChatTranscript:
    title = str(payload.get("title") or "Untitled Chat")
    url = payload.get("url")
    tags = list(payload.get("tags") or [])
    raw_messages = payload.get("messages") or []
    messages: list[ChatMessage] = []
    for item in raw_messages:
        if not isinstance(item, dict):
            continue
        role = _coerce_role(str(item.get("role") or "other"))
        content = str(item.get("content") or "").strip()
        if not content:
            continue
        if role == MessageRole.system:
            continue
        messages.append(ChatMessage(role=role, content=content))

    if not messages and payload.get("text"):
        return normalize_paste(
            str(payload["text"]),
            title=title,
            tags=tags,
            url=url if isinstance(url, str) else None,
        )

    return ChatTranscript(
        title=title,
        messages=messages,
        source=SourceKind.extension,
        url=url if isinstance(url, str) else None,
        tags=tags,
    )


def _parse_roles_from_text(text: str) -> list[ChatMessage]:
    lines = text.split("\n")
    messages: list[ChatMessage] = []
    current_role: MessageRole | None = None
    buffer: list[str] = []

    def flush() -> None:
        nonlocal current_role, buffer
        if current_role is None:
            buffer = []
            return
        body = "\n".join(buffer).strip()
        if body:
            messages.append(ChatMessage(role=current_role, content=body))
        buffer = []

    for raw in lines:
        line = raw.rstrip()
        if _CHROME_LINES.match(line.strip()):
            continue

        heading = _ROLE_HEADING.match(line.strip())
        if heading:
            flush()
            current_role = _coerce_role(heading.group(0))
            continue

        inline = _INLINE_ROLE.match(line.strip())
        if inline:
            flush()
            current_role = _coerce_role(inline.group(1))
            rest = inline.group(2).strip()
            buffer = [rest] if rest else []
            continue

        if current_role is None:
            # Accumulate preamble until first role marker; treat later as user if needed.
            buffer.append(line)
            continue

        buffer.append(line)

    if current_role is None and buffer:
        body = "\n".join(buffer).strip()
        if body:
            messages.append(ChatMessage(role=MessageRole.user, content=body))
    else:
        flush()

    return messages


def _coerce_role(label: str) -> MessageRole:
    key = re.sub(r"[^a-z]", "", label.lower())
    if key in {"you", "user", "human", "me"}:
        return MessageRole.user
    if key in {"chatgpt", "assistant", "gpt", "ai", "chatgptsaid", "assistantsaid"}:
        return MessageRole.assistant
    if key in {"system"}:
        return MessageRole.system
    return MessageRole.other


def _first_line_title(text: str) -> str | None:
    for line in text.split("\n"):
        candidate = line.strip().lstrip("#").strip()
        if candidate and not _ROLE_HEADING.match(candidate) and not _INLINE_ROLE.match(candidate):
            return candidate[:80]
    return None
