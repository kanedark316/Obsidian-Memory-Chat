"""CLI for ChatGPT Obsidian Memory."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
import uvicorn
from rich.console import Console
from rich.table import Table

from chatgpt_obsidian_memory.config import (
    AppConfig,
    default_config_path,
    load_config,
    save_config,
)
from chatgpt_obsidian_memory.normalize import normalize_paste
from chatgpt_obsidian_memory.share import ShareImportError, import_share_url
from chatgpt_obsidian_memory.vault import list_notes, write_transcript
from chatgpt_obsidian_memory.web.app import create_app

app = typer.Typer(
    name="chatgpt-obsidian-memory",
    help="Capture ChatGPT chats into Obsidian locally (no ChatGPT API).",
    no_args_is_help=True,
)
config_app = typer.Typer(help="Manage local configuration.")
app.add_typer(config_app, name="config")
console = Console()


@config_app.command("show")
def config_show() -> None:
    cfg = load_config()
    console.print(f"Config file: {default_config_path()}")
    console.print(f"vault_path: {cfg.vault_path or '(not set)'}")
    console.print(f"notes_subdir: {cfg.notes_subdir}")
    console.print(f"host: {cfg.host}")
    console.print(f"port: {cfg.port}")
    console.print(f"auto_save_from_extension: {cfg.auto_save_from_extension}")
    console.print(f"default_tags: {cfg.default_tags}")


@config_app.command("set-vault")
def config_set_vault(path: Path = typer.Argument(..., exists=True, file_okay=False)) -> None:
    cfg = load_config()
    cfg.vault_path = path.expanduser().resolve()
    saved = save_config(cfg)
    console.print(f"Vault set to {cfg.vault_path}")
    console.print(f"Wrote {saved}")


@config_app.command("set")
def config_set(
    key: str = typer.Argument(...),
    value: str = typer.Argument(...),
) -> None:
    cfg = load_config()
    allowed = {
        "notes_subdir",
        "host",
        "port",
        "auto_save_from_extension",
        "default_tags",
        "vault_path",
    }
    if key not in allowed:
        raise typer.BadParameter(f"Unknown key {key}. Allowed: {', '.join(sorted(allowed))}")
    if key == "port":
        cfg.port = int(value)
    elif key == "auto_save_from_extension":
        cfg.auto_save_from_extension = value.lower() in {"1", "true", "yes", "on"}
    elif key == "default_tags":
        cfg.default_tags = [t.strip() for t in value.split(",") if t.strip()]
    elif key == "vault_path":
        cfg.vault_path = Path(value).expanduser().resolve()
    elif key == "notes_subdir":
        cfg.notes_subdir = value
    elif key == "host":
        cfg.host = value
    saved = save_config(cfg)
    console.print(f"Updated {key}. Wrote {saved}")


@app.command("serve")
def serve(
    host: Optional[str] = typer.Option(None, help="Bind host (default from config: 127.0.0.1)"),
    port: Optional[int] = typer.Option(None, help="Bind port (default from config: 8765)"),
) -> None:
    """Start the localhost UI + import API for the browser extension."""
    import os

    from chatgpt_obsidian_memory.config import (
        PREFERRED_NOTES_DIR_STR,
        PREFERRED_WINDOWS_VAULT_STR,
        is_cloud_agent_vault,
        pin_windows_vault,
    )

    if os.name != "nt" and os.environ.get("CHATGPT_OBSIDIAN_DEV") != "1":
        console.print("[red]Refusing to serve outside Windows.[/red]")
        console.print(f"Share imports must go to: {PREFERRED_NOTES_DIR_STR}")
        console.print(
            f"On your PC extract into {PREFERRED_WINDOWS_VAULT_STR} "
            "and double-click Start Obsidian Memory Chat.bat"
        )
        console.print("Cloud Agent /home/ubuntu cannot write to C:\\")
        raise typer.Exit(code=1)

    cfg = pin_windows_vault(load_config())
    if is_cloud_agent_vault(cfg.vault_path) and os.environ.get("CHATGPT_OBSIDIAN_DEV") != "1":
        console.print("[red]Refusing to serve with Cloud Agent vault.[/red]")
        console.print(f"Share imports must go to: {PREFERRED_NOTES_DIR_STR}")
        raise typer.Exit(code=1)

    bind_host = host or cfg.host
    bind_port = port or cfg.port
    if bind_host not in {"127.0.0.1", "localhost", "::1"}:
        console.print(
            "[yellow]Warning:[/yellow] binding outside localhost exposes the import API on your network."
        )
    console.print(f"Serving on http://{bind_host}:{bind_port}")
    if cfg.vault_path:
        console.print(f"Vault: {cfg.vault_path} / {cfg.notes_subdir}")
    else:
        console.print("[yellow]vault_path not set[/yellow] — run config set-vault first.")
    uvicorn.run(create_app(cfg), host=bind_host, port=bind_port, log_level="info")


@app.command("save")
def save_cmd(
    file: Optional[Path] = typer.Option(None, "--file", "-f", exists=True, dir_okay=False),
    text: Optional[str] = typer.Option(None, "--text", "-t"),
    title: Optional[str] = typer.Option(None, "--title"),
    tag: Optional[list[str]] = typer.Option(None, "--tag"),
) -> None:
    """Save pasted text or a file into the Obsidian vault."""
    if bool(file) == bool(text):
        raise typer.BadParameter("Provide exactly one of --file or --text")
    raw = file.read_text(encoding="utf-8") if file else (text or "")
    cfg = load_config()
    tags = list(dict.fromkeys([*(cfg.default_tags), *(tag or [])]))
    transcript = normalize_paste(raw, title=title, tags=tags)
    result = write_transcript(cfg.notes_dir(), transcript)
    action = "Created" if result.created else "Updated"
    console.print(f"{action} {result.path}")


@app.command("list")
def list_cmd() -> None:
    """List notes already in the vault memory folder."""
    cfg = load_config()
    notes = list_notes(cfg.notes_dir())
    if not notes:
        console.print("No notes yet.")
        return
    table = Table("Title", "Filename")
    for note in notes:
        table.add_row(note["title"], note["filename"])
    console.print(table)


@app.command("import-share")
def import_share_cmd(
    url: str = typer.Argument(..., help="Public https://chatgpt.com/share/... link"),
    title: Optional[str] = typer.Option(None, "--title"),
    tag: Optional[list[str]] = typer.Option(None, "--tag"),
) -> None:
    """Import a chat from ChatGPT's Share link (⋯ → Share → Copy link)."""
    cfg = load_config()
    try:
        transcript = import_share_url(url)
    except ShareImportError as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(code=1) from exc
    if title:
        transcript.title = title
    transcript.tags = list(dict.fromkeys([*(cfg.default_tags), *(tag or [])]))
    result = write_transcript(cfg.notes_dir(), transcript)
    action = "Created" if result.created else "Updated"
    console.print(f"{action} {result.path} ({len(transcript.messages)} messages)")


if __name__ == "__main__":
    app()
