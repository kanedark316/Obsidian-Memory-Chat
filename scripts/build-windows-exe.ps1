#Requires -Version 5.1
<#
.SYNOPSIS
  Build ObsidianMemoryChat.exe for Windows (double-click to run).

.DESCRIPTION
  Run this once on your Windows PC from an elevated or normal PowerShell:
    .\scripts\build-windows-exe.ps1

  Output:
    .\dist\ObsidianMemoryChat.exe
#>
$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)

Write-Host "Building Obsidian Memory Chat .exe ..." -ForegroundColor Cyan

if (-not (Test-Path ".venv\Scripts\python.exe")) {
  python -m venv .venv
}
& .\.venv\Scripts\python.exe -m pip install -U pip
& .\.venv\Scripts\python.exe -m pip install -e ".[dev,desktop]"

$static = "src\chatgpt_obsidian_memory\web\static"
if (-not (Test-Path "$static\index.html")) {
  throw "Missing UI file: $static\index.html"
}

& .\.venv\Scripts\pyinstaller.exe `
  --noconfirm `
  --clean `
  --onefile `
  --name "ObsidianMemoryChat" `
  --console `
  --add-data "$static;chatgpt_obsidian_memory\web\static" `
  --hidden-import "chatgpt_obsidian_memory.web.app" `
  --hidden-import "chatgpt_obsidian_memory.share" `
  --hidden-import "uvicorn.logging" `
  --hidden-import "uvicorn.loops" `
  --hidden-import "uvicorn.loops.auto" `
  --hidden-import "uvicorn.protocols" `
  --hidden-import "uvicorn.protocols.http" `
  --hidden-import "uvicorn.protocols.http.auto" `
  --hidden-import "uvicorn.protocols.websockets" `
  --hidden-import "uvicorn.protocols.websockets.auto" `
  --hidden-import "uvicorn.lifespan" `
  --hidden-import "uvicorn.lifespan.on" `
  "src\chatgpt_obsidian_memory\desktop.py"

$exe = Join-Path (Get-Location) "dist\ObsidianMemoryChat.exe"
if (-not (Test-Path $exe)) {
  throw "Build finished but exe not found at $exe"
}

# Convenience copy next to project root for double-click
Copy-Item $exe ".\ObsidianMemoryChat.exe" -Force

Write-Host ""
Write-Host "Done." -ForegroundColor Green
Write-Host "Double-click: $exe"
Write-Host "Also copied to: $(Join-Path (Get-Location) 'ObsidianMemoryChat.exe')"
Write-Host "Notes save under this folder\ChatGPT-Memory\"
Write-Host ""
