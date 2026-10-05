# Connect this folder as the Obsidian vault (Windows)

$ErrorActionPreference = "Stop"
$Vault = "C:\Users\shash\.cursor-tutor\Obsidian Memory Chat"

if (-not (Test-Path $Vault)) {
  Write-Error "Folder not found: $Vault"
}

Set-Location $Vault

if (-not (Test-Path ".venv")) {
  python -m venv .venv
}

& .\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
chatgpt-obsidian-memory config set-vault $Vault
chatgpt-obsidian-memory config show

Write-Host ""
Write-Host "Vault connected: $Vault"
Write-Host "Notes folder:    $Vault\ChatGPT-Memory"
Write-Host ""
Write-Host "Next:"
Write-Host "  1. Obsidian -> Open folder as vault -> $Vault"
Write-Host "  2. Cursor   -> Open Folder          -> $Vault"
Write-Host "  3. Run: chatgpt-obsidian-memory serve"
Write-Host "  4. Open http://127.0.0.1:8765"
