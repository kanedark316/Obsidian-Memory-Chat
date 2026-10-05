"""Local configuration for vault path and server settings."""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

APP_NAME = "chatgpt-obsidian-memory"
DEFAULT_PORT = 8765
DEFAULT_NOTES_SUBDIR = "ChatGPT-Memory"


def default_config_dir() -> Path:
    return Path.home() / ".config" / APP_NAME


def default_config_path() -> Path:
    return default_config_dir() / "config.toml"


class AppConfig(BaseModel):
    vault_path: Path | None = None
    notes_subdir: str = DEFAULT_NOTES_SUBDIR
    host: str = "127.0.0.1"
    port: int = DEFAULT_PORT
    auto_save_from_extension: bool = True
    default_tags: list[str] = Field(default_factory=lambda: ["chatgpt", "memory"])

    def notes_dir(self) -> Path:
        if self.vault_path is None:
            raise ValueError(
                "vault_path is not set. Run: chatgpt-obsidian-memory config set-vault <path>"
            )
        return Path(self.vault_path).expanduser().resolve() / self.notes_subdir


def load_config(path: Path | None = None) -> AppConfig:
    config_path = path or default_config_path()
    if not config_path.exists():
        return AppConfig()
    data = tomllib.loads(config_path.read_text(encoding="utf-8"))
    return AppConfig.model_validate(_normalize_toml(data))


def save_config(config: AppConfig, path: Path | None = None) -> Path:
    config_path = path or default_config_path()
    config_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "vault_path": str(config.vault_path) if config.vault_path else "",
        "notes_subdir": config.notes_subdir,
        "host": config.host,
        "port": config.port,
        "auto_save_from_extension": config.auto_save_from_extension,
        "default_tags": config.default_tags,
    }
    lines = ["# ChatGPT Obsidian Memory — local config (no ChatGPT API)\n"]
    for key, value in payload.items():
        lines.append(f"{key} = {_toml_value(value)}\n")
    config_path.write_text("".join(lines), encoding="utf-8")
    return config_path


def _normalize_toml(data: dict[str, Any]) -> dict[str, Any]:
    out = dict(data)
    vault = out.get("vault_path")
    if vault in ("", None):
        out["vault_path"] = None
    elif isinstance(vault, str):
        out["vault_path"] = Path(vault)
    return out


def _toml_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        inner = ", ".join(_toml_value(v) for v in value)
        return f"[{inner}]"
    escaped = str(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'
