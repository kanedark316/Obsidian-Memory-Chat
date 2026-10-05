"""Write and update notes in an Obsidian vault folder."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from chatgpt_obsidian_memory.normalize import ChatTranscript
from chatgpt_obsidian_memory.render import note_filename, render_markdown

_STABLE_KEY_RE = re.compile(r"^stable_key:\s*[\"']?([0-9a-f]+)[\"']?\s*$", re.MULTILINE)
_TITLE_RE = re.compile(r"^title:\s*(.+)\s*$", re.MULTILINE)


@dataclass
class WriteResult:
    path: Path
    created: bool
    filename: str


def write_transcript(notes_dir: Path, transcript: ChatTranscript) -> WriteResult:
    notes_dir.mkdir(parents=True, exist_ok=True)
    key = transcript.stable_key()
    existing = find_note_by_stable_key(notes_dir, key)
    filename = note_filename(transcript.effective_date(), transcript.title)
    target = notes_dir / filename
    markdown = render_markdown(transcript)

    if existing is not None:
        # Keep existing filename when updating the same chat.
        target = existing
        created = False
        target.write_text(markdown, encoding="utf-8")
    else:
        target = _unique_path(target)
        created = True
        target.write_text(markdown, encoding="utf-8")

    update_index(notes_dir)
    return WriteResult(path=target, created=created, filename=target.name)


def find_note_by_stable_key(notes_dir: Path, stable_key: str) -> Path | None:
    if not notes_dir.exists():
        return None
    for path in notes_dir.glob("*.md"):
        if path.name == "Index.md":
            continue
        text = path.read_text(encoding="utf-8")
        match = _STABLE_KEY_RE.search(text)
        if match and match.group(1) == stable_key:
            return path
    return None


def list_notes(notes_dir: Path) -> list[dict[str, str]]:
    if not notes_dir.exists():
        return []
    notes: list[dict[str, str]] = []
    for path in sorted(notes_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True):
        if path.name == "Index.md":
            continue
        text = path.read_text(encoding="utf-8")
        title_match = _TITLE_RE.search(text)
        title = title_match.group(1).strip().strip("\"'") if title_match else path.stem
        key_match = _STABLE_KEY_RE.search(text)
        notes.append(
            {
                "filename": path.name,
                "title": title,
                "stable_key": key_match.group(1) if key_match else "",
                "path": str(path),
            }
        )
    return notes


def update_index(notes_dir: Path) -> Path:
    notes_dir.mkdir(parents=True, exist_ok=True)
    notes = list_notes(notes_dir)
    lines = [
        "---",
        "title: ChatGPT Memory Index",
        "tags: [chatgpt, memory, index]",
        "---",
        "",
        "# ChatGPT Memory Index",
        "",
        "Notes captured locally (paste/extension). No ChatGPT API.",
        "",
    ]
    if not notes:
        lines.append("_No notes yet._")
        lines.append("")
    else:
        for note in notes:
            stem = note["filename"].removesuffix(".md")
            lines.append(f"- [[{stem}|{note['title']}]]")
        lines.append("")
    index_path = notes_dir / "Index.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    return index_path


def _unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    n = 2
    while True:
        candidate = parent / f"{stem}-{n}{suffix}"
        if not candidate.exists():
            return candidate
        n += 1
