from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from chatgpt_obsidian_memory.config import AppConfig
from chatgpt_obsidian_memory.web.app import create_app


def test_paste_and_list_api(tmp_path: Path) -> None:
    cfg = AppConfig(vault_path=tmp_path, notes_subdir="ChatGPT-Memory", port=8765)
    client = TestClient(create_app(cfg))

    health = client.get("/api/health")
    assert health.status_code == 200
    body = health.json()
    assert body["vault_path"] == str(tmp_path)
    assert body["wrong_host"] is False
    assert "ChatGPT-Memory" in body["preferred_notes_dir"]

    res = client.post(
        "/api/paste",
        json={
            "title": "API Demo",
            "text": "You: Hello\n\nChatGPT: Hi from tests",
            "tags": ["test"],
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["ok"] is True
    assert body["filename"].endswith("-Api-Demo.md")
    assert "DD-MM-YYYY" not in body["filename"]
    # DD-MM-YYYY pattern: two digits-two digits-four digits
    assert body["filename"][2] == "-" and body["filename"][5] == "-"

    notes = client.get("/api/notes")
    assert notes.status_code == 200
    assert len(notes.json()["notes"]) == 1


def test_cloud_agent_vault_blocks_share_and_paste(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    config_file = tmp_path / "config.toml"
    monkeypatch.setattr(
        "chatgpt_obsidian_memory.config.default_config_path",
        lambda: config_file,
    )

    cloud_vault = Path("/home/ubuntu/Obsidian Memory Chat")
    cfg = AppConfig(vault_path=cloud_vault, notes_subdir="ChatGPT-Memory")
    client = TestClient(create_app(cfg))

    health = client.get("/api/health")
    assert health.status_code == 200
    assert health.json()["wrong_host"] is True

    paste = client.post(
        "/api/paste",
        json={"text": "You: hi\n\nChatGPT: hello", "title": "Blocked"},
    )
    assert paste.status_code == 400
    assert "C:\\Users\\shash\\.cursor-tutor\\Obsidian Memory Chat\\ChatGPT-Memory" in paste.json()[
        "detail"
    ]

    blocked = client.post(
        "/api/config/vault",
        json={"vault_path": "/home/ubuntu/Obsidian Memory Chat"},
    )
    assert blocked.status_code == 400

    ok_vault = tmp_path / "vault"
    ok = client.post("/api/config/vault", json={"vault_path": str(ok_vault)})
    assert ok.status_code == 200
    assert ok.json()["notes_dir"].endswith("ChatGPT-Memory")


def test_import_extension_auto_save(tmp_path: Path) -> None:
    cfg = AppConfig(
        vault_path=tmp_path,
        notes_subdir="ChatGPT-Memory",
        auto_save_from_extension=True,
    )
    client = TestClient(create_app(cfg))
    res = client.post(
        "/api/import",
        json={
            "title": "Ext Demo",
            "url": "https://chatgpt.com/c/api-test",
            "messages": [
                {"role": "user", "content": "Ping"},
                {"role": "assistant", "content": "Pong"},
            ],
        },
    )
    assert res.status_code == 200
    data = res.json()
    assert data["saved"] is True
    assert data["filename"].endswith("-Ext-Demo.md")


def test_ui_served(tmp_path: Path) -> None:
    cfg = AppConfig(vault_path=tmp_path)
    client = TestClient(create_app(cfg))
    page = client.get("/")
    assert page.status_code == 200
    assert "Save to Obsidian" in page.text
