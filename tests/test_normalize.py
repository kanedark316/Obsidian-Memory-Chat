from __future__ import annotations

from pathlib import Path

from chatgpt_obsidian_memory.normalize import (
    MessageRole,
    SourceKind,
    normalize_extension_payload,
    normalize_paste,
)

FIXTURES = Path(__file__).parent / "fixtures"


def test_normalize_paste_role_lines() -> None:
    text = (FIXTURES / "sample_paste.txt").read_text(encoding="utf-8")
    transcript = normalize_paste(text, title="Slug Filenames")
    assert transcript.source == SourceKind.paste
    assert transcript.title == "Slug Filenames"
    assert len(transcript.messages) == 2
    assert transcript.messages[0].role == MessageRole.user
    assert "slug filenames" in transcript.messages[0].content.lower()
    assert transcript.messages[1].role == MessageRole.assistant
    assert "DD-MM-YYYY" in transcript.messages[1].content


def test_normalize_paste_markdown_headings() -> None:
    text = "## User\n\nHello\n\n## Assistant\n\nHi there\n"
    transcript = normalize_paste(text)
    assert [m.role for m in transcript.messages] == [MessageRole.user, MessageRole.assistant]
    assert transcript.messages[0].content == "Hello"
    assert transcript.messages[1].content == "Hi there"


def test_normalize_paste_plain_fallback() -> None:
    transcript = normalize_paste("just some notes without roles")
    assert len(transcript.messages) == 1
    assert transcript.messages[0].role == MessageRole.user


def test_normalize_extension_payload() -> None:
    import json

    payload = json.loads((FIXTURES / "extension_payload.json").read_text(encoding="utf-8"))
    transcript = normalize_extension_payload(payload)
    assert transcript.source == SourceKind.extension
    assert transcript.url and transcript.url.startswith("https://chatgpt.com/")
    assert len(transcript.messages) == 2
    assert transcript.stable_key()  # URL-based


def test_stable_key_consistent_for_same_url() -> None:
    a = normalize_extension_payload(
        {
            "title": "A",
            "url": "https://chatgpt.com/c/abc",
            "messages": [{"role": "user", "content": "hi"}],
        }
    )
    b = normalize_extension_payload(
        {
            "title": "B",
            "url": "https://chatgpt.com/c/abc",
            "messages": [{"role": "user", "content": "different"}],
        }
    )
    assert a.stable_key() == b.stable_key()
