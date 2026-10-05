from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from chatgpt_obsidian_memory.config import AppConfig
from chatgpt_obsidian_memory.web.app import create_app


def test_paste_and_list_api(tmp_path: Path) -> None:
    cfg = AppConfig(vault_path=tmp_path, notes_subdir="ChatGPT-Memory", port=8765)
    client = TestClient(create_app(cfg))

    health = client.get("/api/health")
    assert health.status_code == 200
    assert health.json()["vault_path"] == str(tmp_path)

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
