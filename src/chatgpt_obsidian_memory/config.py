"""Local configuration for vault path and server settings."""

from __future__ import annotations

import os
import tomllib
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

APP_NAME = "chatgpt-obsidian-memory"
DEFAULT_PORT = 8765
DEFAULT_NOTES_SUBDIR = "ChatGPT-Memory"
# Preferred vault on the user's Windows PC — Share imports must land here
PREFERRED_WINDOWS_VAULT_STR = r"C:\Users\shash\.cursor-tutor\Obsidian Memory Chat"
PREFERRED_WINDOWS_VAULT = Path(PREFERRED_WINDOWS_VAULT_STR)
PREFERRED_NOTES_DIR_STR = rf"{PREFERRED_WINDOWS_VAULT_STR}\{DEFAULT_NOTES_SUBDIR}"

# Cloud Agent / Linux paths that must never receive Share imports
_CLOUD_VAULT_PREFIXES = ("/home/ubuntu", "/workspace")


def preferred_vault_path() -> Path | None:
    """Return the Windows vault path when running on Windows (or if it already exists)."""
    if os.name == "nt":
        return PREFERRED_WINDOWS_VAULT
    if PREFERRED_WINDOWS_VAULT.exists():
        return PREFERRED_WINDOWS_VAULT
    return None


def is_cloud_agent_vault(path: Path | str | None) -> bool:
    """True when vault points at a Cloud Agent Linux folder (not the Windows PC)."""
    if path is None:
        return False
    normalized = str(path).replace("\\", "/")
    return any(normalized.startswith(prefix) for prefix in _CLOUD_VAULT_PREFIXES)


def cloud_vault_blocked_message() -> str:
    return (
        "Share imports must save to "
        f"{PREFERRED_NOTES_DIR_STR}. "
        "This page is using the Cloud Agent vault (/home/ubuntu). "
        "Close it, extract Obsidian-Memory-Chat.zip on your Windows PC into "
        f"{PREFERRED_WINDOWS_VAULT_STR}, "
        "then double-click Start Obsidian Memory Chat.bat and import again."
    )


def assert_vault_allows_writes(config: AppConfig) -> None:
    """Refuse writes into Cloud Agent Linux vaults."""
    if config.vault_path is None:
        raise ValueError(
            "vault_path is not set. On Windows, run Start Obsidian Memory Chat.bat "
            f"(vault: {PREFERRED_WINDOWS_VAULT_STR})."
        )
    if is_cloud_agent_vault(config.vault_path):
        raise ValueError(cloud_vault_blocked_message())


def pin_windows_vault(config: AppConfig) -> AppConfig:
    """On Windows, always pin vault to the preferred Obsidian Memory Chat folder."""
    if os.name != "nt":
        return config
    PREFERRED_WINDOWS_VAULT.mkdir(parents=True, exist_ok=True)
    (PREFERRED_WINDOWS_VAULT / DEFAULT_NOTES_SUBDIR).mkdir(parents=True, exist_ok=True)
    config.vault_path = PREFERRED_WINDOWS_VAULT
    return config



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
