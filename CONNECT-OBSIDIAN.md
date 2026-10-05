# Connect Obsidian + Cursor (Windows)

This folder is set up as:

1. An **Obsidian vault** (`.obsidian/`)
2. A **Cursor workspace** (`.cursor/rules/` + `AGENTS.md`)
3. The save target for **Obsidian Memory Chat** notes (`ChatGPT-Memory/`)

## 0. Easiest: double-click to run

From this folder, double-click:

`Start Obsidian Memory Chat.bat`

That installs dependencies if needed, starts the local app, and opens the browser.

To build a real `.exe` once (then double-click that forever):

```powershell
cd "C:\Users\shash\.cursor-tutor\Obsidian Memory Chat"
powershell -ExecutionPolicy Bypass -File .\scripts\build-windows-exe.ps1
```

Then double-click `ObsidianMemoryChat.exe` (created in this folder and in `dist\`).

## 1. Open this folder in Obsidian

1. Open Obsidian
2. **Open folder as vault**
3. Choose:

```text
C:\Users\shash\.cursor-tutor\Obsidian Memory Chat
```

You should see `ChatGPT-Memory` in the file list (including `Index.md` and any imported chats).

## 2. Point the local app at this vault

In PowerShell:

```powershell
cd "C:\Users\shash\.cursor-tutor\Obsidian Memory Chat"
python -m venv .venv
.\.venv\Scripts\activate
pip install -e ".[dev]"
chatgpt-obsidian-memory config set-vault "C:\Users\shash\.cursor-tutor\Obsidian Memory Chat"
chatgpt-obsidian-memory config show
chatgpt-obsidian-memory serve
```

Open http://127.0.0.1:8765 and import a Share link or paste a chat. New notes appear under `ChatGPT-Memory\`.

## 3. Open the same folder in Cursor

1. Cursor → **File → Open Folder**
2. Select `C:\Users\shash\.cursor-tutor\Obsidian Memory Chat`
3. Agents will follow `.cursor/rules/obsidian-memory.mdc` and `AGENTS.md` and read `ChatGPT-Memory/`

No ChatGPT API is used. Cursor only reads local Markdown files in this vault.
