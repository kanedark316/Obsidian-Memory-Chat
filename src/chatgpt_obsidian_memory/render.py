"""Render ChatTranscript notes as Obsidian Markdown with DD-MM-YYYY-Slug.md names."""

from __future__ import annotations

import re
from datetime import date

from chatgpt_obsidian_memory.normalize import ChatMessage, ChatTranscript, MessageRole

_INVALID_FS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
_MULTISPACE = re.compile(r"\s+")


def title_to_slug(title: str) -> str:
    cleaned = _INVALID_FS.sub("", title)
    cleaned = cleaned.replace("_", " ").replace("-", " ")
    cleaned = _MULTISPACE.sub(" ", cleaned).strip()
    if not cleaned:
        return "Untitled-Chat"
    parts = [p.capitalize() if p else p for p in cleaned.split(" ")]
    slug = "-".join(parts)
    return slug[:80].rstrip("-.")


def note_filename(conversation_date: date, title: str) -> str:
    """Return DD-MM-YYYY-Slug.md"""
    day = conversation_date.strftime("%d-%m-%Y")
    return f"{day}-{title_to_slug(title)}.md"


def render_markdown(transcript: ChatTranscript) -> str:
    tags = transcript.tags or []
    tag_line = "[" + ", ".join(_yaml_str(t) for t in tags) + "]" if tags else "[]"
    url_line = f"url: {_yaml_str(transcript.url)}\n" if transcript.url else ""
    frontmatter = (
        "---\n"
        f"title: {_yaml_str(transcript.title)}\n"
        f"source: {transcript.source.value}\n"
        f"saved_at: {transcript.saved_at.isoformat()}\n"
        f"stable_key: {transcript.stable_key()}\n"
        f"tags: {tag_line}\n"
        f"{url_line}"
        "---\n\n"
    )
    body_parts = [f"# {transcript.title}\n"]
    for message in transcript.messages:
        body_parts.append(_format_message(message))
    return frontmatter + "\n".join(body_parts).rstrip() + "\n"


def _format_message(message: ChatMessage) -> str:
    heading = {
        MessageRole.user: "User",
        MessageRole.assistant: "Assistant",
        MessageRole.system: "System",
        MessageRole.other: "Other",
    }[message.role]
    return f"## {heading}\n\n{message.content.strip()}\n"


def _yaml_str(value: str) -> str:
    if any(ch in value for ch in ":#{}[]&*!|>'\"%@`") or value != value.strip():
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return value
