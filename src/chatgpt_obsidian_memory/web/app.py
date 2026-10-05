"""Localhost FastAPI app: paste/drop UI + extension import API."""

from __future__ import annotations

import sys
from importlib import resources
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from chatgpt_obsidian_memory.config import AppConfig, load_config
from chatgpt_obsidian_memory.normalize import (
    ChatTranscript,
    SourceKind,
    normalize_extension_payload,
    normalize_paste,
)
from chatgpt_obsidian_memory.share import ShareImportError, import_share_url
from chatgpt_obsidian_memory.vault import list_notes, write_transcript

def _load_ui_html() -> str:
    """Load index.html from editable install, wheel, PyInstaller bundle, or source tree."""
    candidates: list[Path] = [
        Path(__file__).parent / "static" / "index.html",
    ]

    # PyInstaller onefile extracts datas under sys._MEIPASS
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        candidates.append(
            Path(meipass) / "chatgpt_obsidian_memory" / "web" / "static" / "index.html"
        )
        candidates.append(Path(meipass) / "static" / "index.html")

    try:
        static_pkg = resources.files("chatgpt_obsidian_memory.web.static")
        candidates.append(Path(str(static_pkg.joinpath("index.html"))))
    except (ModuleNotFoundError, TypeError, FileNotFoundError, AttributeError):
        pass

    # Running from repo root without editable install
    for parent in Path(__file__).resolve().parents:
        repo_candidate = (
            parent / "src" / "chatgpt_obsidian_memory" / "web" / "static" / "index.html"
        )
        if repo_candidate not in candidates:
            candidates.append(repo_candidate)
        if (parent / "pyproject.toml").exists():
            break

    for path in candidates:
        try:
            if path.is_file():
                return path.read_text(encoding="utf-8")
        except OSError:
            continue

    searched = "\n".join(f"  - {p}" for p in candidates)
    raise HTTPException(
        status_code=500,
        detail=f"UI missing (index.html not found). Searched:\n{searched}",
    )


class PasteRequest(BaseModel):
    text: str
    title: str | None = None
    tags: list[str] = Field(default_factory=list)
    url: str | None = None


class ExtensionImportRequest(BaseModel):
    title: str | None = None
    url: str | None = None
    tags: list[str] = Field(default_factory=list)
    messages: list[dict[str, Any]] = Field(default_factory=list)
    text: str | None = None
    auto_save: bool | None = None


class ShareRequest(BaseModel):
    url: str
    title: str | None = None
    tags: list[str] = Field(default_factory=list)


def create_app(config: AppConfig | None = None) -> FastAPI:
    app = FastAPI(title="ChatGPT Obsidian Memory", version="0.1.0")
    state_config = config or load_config()

    def get_config() -> AppConfig:
        return state_config

    def merge_tags(extra: list[str]) -> list[str]:
        cfg = get_config()
        seen: list[str] = []
        for tag in [*cfg.default_tags, *extra]:
            if tag and tag not in seen:
                seen.append(tag)
        return seen

    def save(transcript: ChatTranscript) -> dict[str, Any]:
        cfg = get_config()
        try:
            notes_dir = cfg.notes_dir()
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        result = write_transcript(notes_dir, transcript)
        return {
            "ok": True,
            "created": result.created,
            "filename": result.filename,
            "path": str(result.path),
        }

    @app.get("/api/health")
    def health() -> dict[str, Any]:
        cfg = get_config()
        return {
            "ok": True,
            "vault_path": str(cfg.vault_path) if cfg.vault_path else None,
            "notes_subdir": cfg.notes_subdir,
            "auto_save_from_extension": cfg.auto_save_from_extension,
            "host": cfg.host,
            "port": cfg.port,
        }

    @app.get("/api/notes")
    def notes() -> dict[str, Any]:
        cfg = get_config()
        try:
            notes_dir = cfg.notes_dir()
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"notes": list_notes(notes_dir)}

    @app.post("/api/paste")
    def paste(body: PasteRequest) -> dict[str, Any]:
        if not body.text.strip():
            raise HTTPException(status_code=400, detail="text is required")
        transcript = normalize_paste(
            body.text,
            title=body.title,
            tags=merge_tags(body.tags),
            url=body.url,
        )
        return save(transcript)

    @app.post("/api/import")
    def import_from_extension(body: ExtensionImportRequest) -> dict[str, Any]:
        cfg = get_config()
        payload = body.model_dump()
        transcript = normalize_extension_payload(payload)
        transcript.tags = merge_tags(body.tags)
        transcript.source = SourceKind.extension
        auto = cfg.auto_save_from_extension if body.auto_save is None else body.auto_save
        if not auto:
            return {
                "ok": True,
                "saved": False,
                "preview": {
                    "title": transcript.title,
                    "message_count": len(transcript.messages),
                    "stable_key": transcript.stable_key(),
                    "url": transcript.url,
                },
            }
        result = save(transcript)
        result["saved"] = True
        return result

    @app.post("/api/share")
    def import_share(body: ShareRequest) -> dict[str, Any]:
        """Import a public ChatGPT Share link (⋯ → Share chat → Copy link)."""
        try:
            transcript = import_share_url(body.url)
        except ShareImportError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        if body.title and body.title.strip():
            transcript.title = body.title.strip()
        transcript.tags = merge_tags(body.tags)
        transcript.source = SourceKind.share
        result = save(transcript)
        result["saved"] = True
        result["title"] = transcript.title
        result["message_count"] = len(transcript.messages)
        return result

    @app.get("/", response_class=HTMLResponse)
    def index() -> HTMLResponse:
        return HTMLResponse(_load_ui_html())

    return app
