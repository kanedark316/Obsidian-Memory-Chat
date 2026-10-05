from __future__ import annotations

from pathlib import Path

import httpx
import pytest
from fastapi.testclient import TestClient

from chatgpt_obsidian_memory.config import AppConfig
from chatgpt_obsidian_memory.normalize import MessageRole, SourceKind
from chatgpt_obsidian_memory.share import (
    ShareImportError,
    get_share_id,
    import_share_url,
    is_chatgpt_share_url,
    parse_share_html,
)
from chatgpt_obsidian_memory.web.app import create_app

FIXTURES = Path(__file__).parent / "fixtures"


def test_share_url_helpers() -> None:
    assert is_chatgpt_share_url("https://chatgpt.com/share/abc-123")
    assert get_share_id("https://chatgpt.com/share/e/abc-123") == "abc-123"
    assert get_share_id("https://chat.openai.com/share/xyz") == "xyz"
    assert get_share_id("https://chatgpt.com/c/private-id") is None


def test_parse_legacy_share_html() -> None:
    html = (FIXTURES / "share_legacy.html").read_text(encoding="utf-8")
    transcript = parse_share_html(html, share_url="https://chatgpt.com/share/demo-share-id")
    assert transcript.source == SourceKind.share
    assert transcript.title == "Shared Demo Chat"
    assert len(transcript.messages) == 2
    assert transcript.messages[0].role == MessageRole.user
    assert "shared chat" in transcript.messages[0].content.lower()
    assert transcript.messages[1].role == MessageRole.assistant
    assert transcript.url == "https://chatgpt.com/share/demo-share-id"


def test_import_share_url_uses_fetch(monkeypatch: pytest.MonkeyPatch) -> None:
    html = (FIXTURES / "share_legacy.html").read_text(encoding="utf-8")

    class FakeResponse:
        status_code = 200
        text = html

    def fake_get(url: str, **kwargs):  # type: ignore[no-untyped-def]
        assert "chatgpt.com/share/demo-share-id" in url
        return FakeResponse()

    monkeypatch.setattr(httpx, "get", fake_get)
    transcript = import_share_url("https://chatgpt.com/share/demo-share-id")
    assert transcript.title == "Shared Demo Chat"
    assert len(transcript.messages) == 2


def test_import_share_rejects_private_conversation_url() -> None:
    with pytest.raises(ShareImportError):
        import_share_url("https://chatgpt.com/c/not-a-share")


def test_api_share_endpoint(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    html = (FIXTURES / "share_legacy.html").read_text(encoding="utf-8")

    class FakeResponse:
        status_code = 200
        text = html

    monkeypatch.setattr(httpx, "get", lambda *a, **k: FakeResponse())
    cfg = AppConfig(vault_path=tmp_path, notes_subdir="ChatGPT-Memory")
    client = TestClient(create_app(cfg))
    res = client.post(
        "/api/share",
        json={"url": "https://chatgpt.com/share/demo-share-id", "tags": ["shared"]},
    )
    assert res.status_code == 200
    body = res.json()
    assert body["ok"] is True
    assert body["saved"] is True
    assert body["message_count"] == 2
    assert "Shared-Demo-Chat" in body["filename"]
