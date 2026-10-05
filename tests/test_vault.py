from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path

from chatgpt_obsidian_memory.normalize import (
    ChatMessage,
    ChatTranscript,
    MessageRole,
    SourceKind,
    normalize_extension_payload,
)
from chatgpt_obsidian_memory.render import note_filename
from chatgpt_obsidian_memory.vault import list_notes, update_index, write_transcript


def _transcript(title: str = "Demo Chat", url: str | None = None) -> ChatTranscript:
    return ChatTranscript(
        title=title,
        messages=[
            ChatMessage(role=MessageRole.user, content="Question one"),
            ChatMessage(role=MessageRole.assistant, content="Answer one"),
        ],
        source=SourceKind.paste if url is None else SourceKind.extension,
        url=url,
        tags=["chatgpt"],
        saved_at=datetime(2026, 10, 5, 12, 0, tzinfo=timezone.utc),
        conversation_date=date(2026, 10, 5),
    )


def test_write_creates_dd_mm_yyyy_slug(tmp_path: Path) -> None:
    notes_dir = tmp_path / "ChatGPT-Memory"
    result = write_transcript(notes_dir, _transcript("Python Debugging"))
    assert result.created is True
    assert result.filename == "05-10-2026-Python-Debugging.md"
    assert result.path.exists()
    assert (notes_dir / "Index.md").exists()
    index = (notes_dir / "Index.md").read_text(encoding="utf-8")
    assert "Python Debugging" in index


def test_write_updates_same_stable_key(tmp_path: Path) -> None:
    notes_dir = tmp_path / "ChatGPT-Memory"
    url = "https://chatgpt.com/c/same-id"
    first = write_transcript(notes_dir, _transcript("First Title", url=url))
    second = write_transcript(notes_dir, _transcript("Second Title", url=url))
    assert first.created is True
    assert second.created is False
    assert second.path == first.path
    assert "Second Title" in second.path.read_text(encoding="utf-8")
    notes = list_notes(notes_dir)
    assert len(notes) == 1


def test_unique_filename_when_different_keys_collide(tmp_path: Path) -> None:
    notes_dir = tmp_path / "ChatGPT-Memory"
    a = write_transcript(notes_dir, _transcript("Same Title"))
    # Force different stable key via different first user message but same title/date
    other = ChatTranscript(
        title="Same Title",
        messages=[ChatMessage(role=MessageRole.user, content="Totally different prompt")],
        source=SourceKind.paste,
        conversation_date=date(2026, 10, 5),
    )
    b = write_transcript(notes_dir, other)
    assert a.created and b.created
    assert a.filename != b.filename
    assert note_filename(date(2026, 10, 5), "Same Title") == a.filename
    assert b.filename.startswith("05-10-2026-Same-Title")


def test_update_index_empty(tmp_path: Path) -> None:
    notes_dir = tmp_path / "ChatGPT-Memory"
    path = update_index(notes_dir)
    assert "No notes yet" in path.read_text(encoding="utf-8")


def test_extension_roundtrip_key(tmp_path: Path) -> None:
    notes_dir = tmp_path / "ChatGPT-Memory"
    payload = {
        "title": "From Extension",
        "url": "https://chatgpt.com/c/xyz",
        "messages": [
            {"role": "user", "content": "Hi"},
            {"role": "assistant", "content": "Hello"},
        ],
    }
    t = normalize_extension_payload(payload)
    t.conversation_date = date(2026, 10, 5)
    result = write_transcript(notes_dir, t)
    assert result.filename == "05-10-2026-From-Extension.md"
