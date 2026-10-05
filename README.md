# Obsidian Memory Chat

Local-only tool that saves ChatGPT conversations you choose into an **Obsidian** vault as Markdown notes named `DD-MM-YYYY-Slug.md`, so **Cursor agents** can read and reuse that memory.

**No ChatGPT API keys. No OpenAI Export ZIP.** Capture is either:

1. **Paste / drop** in a localhost UI,  
2. A **Share chat** link (`⋯` → Share → Copy link → paste `https://chatgpt.com/share/...`), or  
3. A **Chromium extension** that reads the open ChatGPT page / share page (DOM only) and POSTs to your local app.

Cursor connects only to your Obsidian vault (files). Share import only fetches the **public share page you create** — it does not log into ChatGPT or use paid APIs.

## Recommended Windows layout

```text
C:\Users\shash\.cursor-tutor\Obsidian Memory Chat\
  (app source — this repo)
  ChatGPT-Memory\          ← imported .md notes (also used as vault subfolder)
```

Point the app at this folder as the vault (notes go into `ChatGPT-Memory\` inside it):

```powershell
cd "C:\Users\shash\.cursor-tutor\Obsidian Memory Chat"
python -m venv .venv
.\.venv\Scripts\activate
pip install -e ".[dev]"
chatgpt-obsidian-memory config set-vault "C:\Users\shash\.cursor-tutor\Obsidian Memory Chat"
chatgpt-obsidian-memory serve
```

Then open http://127.0.0.1:8765

## Requirements

- Python 3.11+
- Obsidian with a local vault folder (this folder can be the vault, or any other vault path)
- Chrome / Edge / Brave / Chromium (for the extension)

## Install (any OS)

```bash
cd "Obsidian Memory Chat"
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

```bash
chatgpt-obsidian-memory config set-vault "/path/to/your/ObsidianVault"
chatgpt-obsidian-memory config show
```

Config is stored at `~/.config/chatgpt-obsidian-memory/config.toml` (on Windows: `%USERPROFILE%\.config\chatgpt-obsidian-memory\config.toml`).

## Run the local app

```bash
chatgpt-obsidian-memory serve
```

Open [http://127.0.0.1:8765](http://127.0.0.1:8765) — paste a chat, drop a `.md` / `.txt` file, or paste a **Share** link, then save.

Notes land in `<vault>/ChatGPT-Memory/` with an `Index.md` map. This repo already includes a `ChatGPT-Memory/` sample from a share import.

### Share chat (⋯ menu)

1. In ChatGPT, open the conversation.
2. Click **⋯** → **Share** → create/copy the public link.
3. Paste `https://chatgpt.com/share/...` into the local UI **Share chat link** box (or CLI below).

CLI alternatives:

```bash
chatgpt-obsidian-memory save --file ./chat.txt --title "My Topic"
chatgpt-obsidian-memory save --text "You: hello\n\nChatGPT: hi" --tag project
chatgpt-obsidian-memory import-share "https://chatgpt.com/share/your-share-id"
chatgpt-obsidian-memory list
```

## Browser extension

1. Keep `chatgpt-obsidian-memory serve` running.
2. In Chrome/Edge: `chrome://extensions` → enable **Developer mode** → **Load unpacked** → select the `extension/` folder in this project.
3. Open a conversation on [chatgpt.com](https://chatgpt.com) (or a `/share/...` page).
4. Click the extension → **Save to Obsidian**.

The extension only scrapes the **visible page** (or imports a share URL) and talks to `http://127.0.0.1:8765`. It does not call OpenAI APIs.

## Note format

Filename example: `05-10-2026-Python-Debugging.md`

```markdown
---
title: Python Debugging
source: paste   # or extension | share
saved_at: 2026-10-05T14:00:00+00:00
stable_key: a1b2c3d4e5f67890
tags: [chatgpt, memory]
url: https://chatgpt.com/share/...
---

# Python Debugging

## User

...

## Assistant

...
```

## Connect Cursor to Obsidian

1. Open `C:\Users\shash\.cursor-tutor\Obsidian Memory Chat` (or your vault) in Cursor.
2. Copy [`templates/cursor-rule.mdc`](templates/cursor-rule.mdc) into `.cursor/rules/`.
3. Optionally paste [`templates/agents-memory.md`](templates/agents-memory.md) into `AGENTS.md`.

## API (localhost)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/health` | Config / health |
| GET | `/api/notes` | List saved notes |
| POST | `/api/paste` | `{ "text", "title?", "tags?" }` |
| POST | `/api/share` | `{ "url": "https://chatgpt.com/share/...", "title?", "tags?" }` |
| POST | `/api/import` | Extension payload |

Server binds to `127.0.0.1` by default.

## Tests

```bash
pip install -e ".[dev]"
pytest
```

## Privacy

- No outbound calls to OpenAI from this app for private chats.
- Share import only fetches the public share page URL you provide.
- Transcripts are written as local Markdown only where you configure `vault_path`.
