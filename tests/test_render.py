from __future__ import annotations

from datetime import date, datetime, timezone

from chatgpt_obsidian_memory.normalize import (
    ChatMessage,
    ChatTranscript,
    MessageRole,
    SourceKind,
)
from chatgpt_obsidian_memory.render import note_filename, render_markdown, title_to_slug


def test_filename_dd_mm_yyyy_slug() -> None:
    name = note_filename(date(2026, 10, 5), "python debugging tips")
    assert name == "05-10-2026-Python-Debugging-Tips.md"


def test_title_to_slug_strips_invalid() -> None:
    assert title_to_slug('Weird: Title/Name?') == "Weird-Titlename"


def test_render_markdown_frontmatter_and_turns() -> None:
    transcript = ChatTranscript(
        title="Demo",
        messages=[
            ChatMessage(role=MessageRole.user, content="Hello"),
            ChatMessage(role=MessageRole.assistant, content="World"),
        ],
        source=SourceKind.paste,
        tags=["chatgpt", "memory"],
        saved_at=datetime(2026, 10, 5, 12, 0, tzinfo=timezone.utc),
    )
    md = render_markdown(transcript)
    assert md.startswith("---\n")
    assert "title: Demo" in md
    assert "source: paste" in md
    assert "## User" in md
    assert "Hello" in md
    assert "## Assistant" in md
    assert "World" in md
