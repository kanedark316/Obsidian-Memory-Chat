"""Import public ChatGPT Share links (⋯ → Share chat) without ChatGPT API keys.

Fetches the public https://chatgpt.com/share/... page HTML and extracts the
embedded conversation. This is not the paid ChatGPT/OpenAI API — only the
public share page you create in the ChatGPT UI.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from typing import Any
from urllib.parse import urlparse

import httpx

from chatgpt_obsidian_memory.normalize import (
    ChatMessage,
    ChatTranscript,
    MessageRole,
    SourceKind,
)

SHARE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/118.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/apng,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://chatgpt.com/",
}

_PRIVATE_USE = re.compile(r"[\ue000-\uf8ff]")
_SCRIPT_RE = re.compile(r"<script\b([^>]*)>([\s\S]*?)</script>", re.IGNORECASE)
_ATTR_RE = re.compile(
    r'([^\s=]+)(?:\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s"\'>]+)))?'
)
_SHARE_HOSTS = {"chatgpt.com", "chat.openai.com", "www.chatgpt.com"}


class ShareImportError(Exception):
    """Raised when a share URL cannot be fetched or parsed."""


def is_chatgpt_share_url(url: str) -> bool:
    return get_share_id(url) is not None


def get_share_id(url: str) -> str | None:
    try:
        parsed = urlparse(url.strip())
    except ValueError:
        return None
    host = (parsed.hostname or "").lower()
    if host not in _SHARE_HOSTS:
        return None
    parts = [p for p in parsed.path.split("/") if p]
    if not parts or parts[0] != "share":
        return None
    if parts[1:2] == ["e"] and len(parts) >= 3:
        return parts[2]
    if len(parts) >= 2:
        return parts[1]
    return None


def normalize_share_url(url: str) -> str:
    share_id = get_share_id(url)
    if not share_id:
        raise ShareImportError(
            "Not a ChatGPT share URL. In ChatGPT use ⋯ → Share → Copy link "
            "(https://chatgpt.com/share/...), then paste that link here."
        )
    parsed = urlparse(url.strip())
    host = "chatgpt.com" if "openai" not in (parsed.hostname or "") else "chat.openai.com"
    return f"https://{host}/share/{share_id}"


def fetch_share_html(url: str, *, timeout: float = 45.0) -> str:
    share_url = normalize_share_url(url)
    try:
        response = httpx.get(
            share_url,
            headers=SHARE_HEADERS,
            timeout=timeout,
            follow_redirects=True,
        )
    except httpx.HTTPError as exc:
        raise ShareImportError(f"Could not fetch share page: {exc}") from exc

    if response.status_code == 403:
        raise ShareImportError(
            "Share page returned 403. Open the share link in your browser, "
            "confirm it loads, then try again — or open the share tab and use "
            "the extension / paste the chat text."
        )
    if response.status_code == 404:
        raise ShareImportError("Share link not found (404). Create Share again and copy the new link.")
    if response.status_code >= 400:
        raise ShareImportError(f"Failed to fetch share page (HTTP {response.status_code}).")
    return response.text


def parse_share_html(html: str, *, share_url: str | None = None) -> ChatTranscript:
    data = _extract_share_data(html)
    title = str(data.get("title") or "Shared Chat").strip() or "Shared Chat"
    messages = _messages_from_share_data(data)
    if not messages:
        raise ShareImportError(
            "Could not find messages in the share page. Open the share link in "
            "your browser and use the extension, or paste the chat text."
        )
    update_time = data.get("update_time") or data.get("create_time")
    conversation_date = None
    if isinstance(update_time, (int, float)):
        conversation_date = datetime.fromtimestamp(update_time, tz=timezone.utc).date()

    url = share_url
    if url is None and data.get("conversation_id"):
        url = f"https://chatgpt.com/share/{data['conversation_id']}"

    return ChatTranscript(
        title=title,
        messages=messages,
        source=SourceKind.share,
        url=url,
        conversation_date=conversation_date,
    )


def import_share_url(url: str) -> ChatTranscript:
    share_url = normalize_share_url(url)
    html = fetch_share_html(share_url)
    return parse_share_html(html, share_url=share_url)


def _extract_share_data(html: str) -> dict[str, Any]:
    try:
        return _parse_modern_share_data(html)
    except ShareImportError:
        pass
    return _parse_legacy_share_data(html)


def _parse_legacy_share_data(html: str) -> dict[str, Any]:
    for attrs, text in _extract_scripts(html):
        if attrs.get("id") == "__NEXT_DATA__":
            try:
                payload = json.loads(text)
            except json.JSONDecodeError as exc:
                raise ShareImportError("Legacy share payload is invalid JSON.") from exc
            props = payload.get("props") if isinstance(payload, dict) else None
            page_props = props.get("pageProps") if isinstance(props, dict) else None
            server = page_props.get("serverResponse") if isinstance(page_props, dict) else None
            data = server.get("data") if isinstance(server, dict) else None
            if isinstance(data, dict):
                return data
            raise ShareImportError("Legacy share data not found.")
    raise ShareImportError("Share payload not found in page HTML.")


def _parse_modern_share_data(html: str) -> dict[str, Any]:
    loader = _extract_loader_payload(html)
    if loader is None:
        raise ShareImportError("Modern share payload not found.")
    decoded = _decode_loader(loader)
    loader_data = decoded.get("loaderData")
    if not isinstance(loader_data, dict):
        raise ShareImportError("Modern share loaderData missing.")

    route = loader_data.get("routes/share.$shareId.($action)")
    if not isinstance(route, dict):
        # Some builds use slightly different route keys.
        for key, value in loader_data.items():
            if isinstance(key, str) and "share" in key and isinstance(value, dict):
                route = value
                break
    if not isinstance(route, dict):
        raise ShareImportError("Modern share route data missing.")

    server = route.get("serverResponse")
    data = server.get("data") if isinstance(server, dict) else None
    if not isinstance(data, dict):
        raise ShareImportError("Modern share conversation data missing.")
    return data


def _messages_from_share_data(data: dict[str, Any]) -> list[ChatMessage]:
    mapping = data.get("mapping") if isinstance(data.get("mapping"), dict) else {}
    sequence = data.get("linear_conversation")
    nodes: list[dict[str, Any]] = []

    if isinstance(sequence, list) and sequence:
        for entry in sequence:
            if not isinstance(entry, dict):
                continue
            node_id = entry.get("id")
            mapped = mapping.get(node_id) if isinstance(node_id, str) else None
            node = mapped if isinstance(mapped, dict) else entry
            nodes.append(node)
    elif mapping:
        # Fallback: walk current_node parents like export mapping.
        current = data.get("current_node")
        path: list[dict[str, Any]] = []
        seen: set[str] = set()
        while isinstance(current, str) and current in mapping and current not in seen:
            seen.add(current)
            node = mapping[current]
            if isinstance(node, dict):
                path.append(node)
                current = node.get("parent")
            else:
                break
        nodes = list(reversed(path))

    messages: list[ChatMessage] = []
    for node in nodes:
        message = node.get("message") if isinstance(node, dict) else None
        if not isinstance(message, dict):
            continue
        author = message.get("author") if isinstance(message.get("author"), dict) else {}
        role_raw = str(author.get("role") or "")
        if role_raw == "system":
            continue
        content = message.get("content") if isinstance(message.get("content"), dict) else None
        if not content:
            continue
        text = _flatten_content(content)
        if not text:
            continue
        if role_raw == "user":
            role = MessageRole.user
        elif role_raw in {"assistant", "tool"}:
            role = MessageRole.assistant if role_raw == "assistant" else MessageRole.other
        else:
            role = MessageRole.assistant
        if role == MessageRole.other:
            continue
        messages.append(ChatMessage(role=role, content=text))
    return messages


def _flatten_content(content: dict[str, Any]) -> str:
    content_type = str(content.get("content_type") or "")
    if content_type in {"text", "multimodal_text", ""}:
        parts = content.get("parts")
        chunks: list[str] = []
        if isinstance(parts, list):
            for part in parts:
                if isinstance(part, str):
                    cleaned = _PRIVATE_USE.sub("", part).strip()
                    if cleaned:
                        chunks.append(cleaned)
                elif isinstance(part, dict):
                    text = part.get("text")
                    if isinstance(text, str) and text.strip():
                        chunks.append(_PRIVATE_USE.sub("", text).strip())
        return "\n\n".join(chunks).strip()
    if content_type == "code":
        return str(content.get("text") or "").strip()
    if content_type == "execution_output":
        return str(content.get("text") or content.get("output") or "").strip()
    if isinstance(content.get("parts"), list):
        return "\n\n".join(
            _PRIVATE_USE.sub("", str(p)).strip() for p in content["parts"] if p
        ).strip()
    return ""


def _extract_scripts(html: str) -> list[tuple[dict[str, str], str]]:
    scripts: list[tuple[dict[str, str], str]] = []
    for match in _SCRIPT_RE.finditer(html):
        attrs: dict[str, str] = {}
        for attr in _ATTR_RE.finditer(match.group(1) or ""):
            key = attr.group(1).lower()
            value = attr.group(2) or attr.group(3) or attr.group(4) or ""
            attrs[key] = value
        scripts.append((attrs, match.group(2) or ""))
    return scripts


def _extract_loader_payload(html: str) -> list[Any] | None:
    call = "streamController.enqueue("
    for _attrs, text in _extract_scripts(html):
        if not text or call not in text:
            continue
        start = 0
        while start < len(text):
            anchor = text.find(call, start)
            if anchor < 0:
                break
            argument_start = anchor + len(call)
            call_arg = _find_call_argument(text, argument_start)
            if call_arg is None:
                break
            payload = _parse_enqueued_loader(call_arg[0])
            if payload is not None:
                return payload
            start = call_arg[1]
    return None


def _find_call_argument(text: str, start_index: int) -> tuple[str, int] | None:
    quote: str | None = None
    escaped = False
    depth = 1
    for index in range(start_index, len(text)):
        char = text[index]
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in {'"', "'", "`"}:
            quote = char
            continue
        if char == "(":
            depth += 1
            continue
        if char == ")":
            depth -= 1
            if depth == 0:
                return text[start_index:index].strip(), index + 1
    return None


def _parse_enqueued_loader(argument: str) -> list[Any] | None:
    stripped = argument.strip()
    while stripped.startswith("(") and stripped.endswith(")"):
        stripped = stripped[1:-1].strip()

    chunk: Any = stripped
    if stripped.startswith('"'):
        try:
            chunk = json.loads(stripped)
        except json.JSONDecodeError:
            return None

    if isinstance(chunk, str):
        trimmed = chunk.strip()
        if not trimmed.startswith("["):
            return None
        try:
            parsed = json.loads(trimmed)
        except json.JSONDecodeError:
            return None
        return parsed if isinstance(parsed, list) else None

    if isinstance(chunk, list):
        return chunk

    if stripped.startswith("["):
        try:
            parsed = json.loads(stripped)
        except json.JSONDecodeError:
            return None
        return parsed if isinstance(parsed, list) else None
    return None


def _decode_loader(loader: list[Any]) -> dict[str, Any]:
    cache: dict[int, Any] = {}

    def decode_key(raw_key: str) -> str:
        if re.fullmatch(r"_\d+", raw_key):
            index = int(raw_key[1:])
            candidate = loader[index] if 0 <= index < len(loader) else None
            if isinstance(candidate, str):
                return candidate
        return raw_key

    def resolve(value: Any) -> Any:
        if isinstance(value, int) and not isinstance(value, bool):
            if value in cache:
                return cache[value]
            if value < 0 or value >= len(loader):
                return value
            cache[value] = None
            resolved = resolve(loader[value])
            cache[value] = resolved
            return resolved
        if isinstance(value, list):
            return [resolve(item) for item in value]
        if isinstance(value, dict):
            return {decode_key(str(k)): resolve(v) for k, v in value.items()}
        return value

    decoded: dict[str, Any] = {}
    for index in range(1, max(len(loader) - 1, 0), 2):
        key = loader[index]
        if isinstance(key, str) and key not in decoded:
            decoded[key] = resolve(loader[index + 1])
    return decoded
