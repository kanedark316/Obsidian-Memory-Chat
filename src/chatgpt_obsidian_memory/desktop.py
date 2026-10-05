"""Double-click desktop launcher for Obsidian Memory Chat."""

from __future__ import annotations

import os
import sys
import threading
import time
import webbrowser
from pathlib import Path


def _app_dir() -> Path:
    """Folder containing the .exe (frozen) or the project root (dev)."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    # src/chatgpt_obsidian_memory/desktop.py -> project root
    return Path(__file__).resolve().parents[2]


def _default_vault() -> Path:
    """Prefer the folder that contains this app / ChatGPT-Memory."""
    app_dir = _app_dir()
    # If exe lives in dist/, project root is parent
    for candidate in (app_dir, app_dir.parent):
        if (candidate / "ChatGPT-Memory").is_dir() or (candidate / "pyproject.toml").is_file():
            return candidate
        if (candidate / ".obsidian").is_dir():
            return candidate
    return app_dir


def _ensure_config() -> None:
    from chatgpt_obsidian_memory.config import load_config, save_config

    cfg = load_config()
    vault = _default_vault()
    if cfg.vault_path is None or not Path(cfg.vault_path).exists():
        cfg.vault_path = vault
        save_config(cfg)
        print(f"Vault set to: {cfg.vault_path}")
    else:
        print(f"Vault: {cfg.vault_path}")
    notes = Path(cfg.vault_path) / cfg.notes_subdir
    notes.mkdir(parents=True, exist_ok=True)
    print(f"Notes folder: {notes}")


def _open_browser(url: str, delay: float = 1.2) -> None:
    def _run() -> None:
        time.sleep(delay)
        try:
            webbrowser.open(url)
        except Exception as exc:  # noqa: BLE001
            print(f"Could not open browser automatically: {exc}")
            print(f"Open manually: {url}")

    threading.Thread(target=_run, daemon=True).start()


def main() -> None:
    print("Obsidian Memory Chat")
    print("No ChatGPT API — local capture only.")
    print()
    try:
        _ensure_config()
    except Exception as exc:  # noqa: BLE001
        print(f"Config error: {exc}")
        input("Press Enter to exit...")
        raise SystemExit(1) from exc

    from chatgpt_obsidian_memory.config import load_config
    from chatgpt_obsidian_memory.web.app import create_app
    import uvicorn

    cfg = load_config()
    host = cfg.host or "127.0.0.1"
    port = int(cfg.port or 8765)
    url = f"http://{host}:{port}"
    print(f"Starting UI at {url}")
    print("Leave this window open. Close it to stop the app.")
    print()
    _open_browser(url)

    # Freeze support for Windows multiprocessing / pyinstaller
    if getattr(sys, "frozen", False):
        os.environ.setdefault("PYTHONNOUSERSITE", "1")

    try:
        uvicorn.run(create_app(cfg), host=host, port=port, log_level="info")
    except KeyboardInterrupt:
        print("\nStopped.")
    except Exception as exc:  # noqa: BLE001
        print(f"\nServer failed: {exc}")
        input("Press Enter to exit...")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
