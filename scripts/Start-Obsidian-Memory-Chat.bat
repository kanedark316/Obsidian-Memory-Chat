@echo off
setlocal EnableExtensions
title Obsidian Memory Chat
cd /d "%~dp0.."

echo ============================================
echo   Obsidian Memory Chat
echo ============================================
echo.

where python >nul 2>&1
if errorlevel 1 (
  echo Python was not found on PATH.
  echo Install Python 3.11+ from https://www.python.org/downloads/
  echo and tick "Add python.exe to PATH", then try again.
  pause
  exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
  echo Creating virtual environment...
  python -m venv .venv
  if errorlevel 1 (
    echo Failed to create .venv
    pause
    exit /b 1
  )
)

echo Installing / updating app...
".venv\Scripts\python.exe" -m pip install -e ".[dev]" -q
if errorlevel 1 (
  echo pip install failed.
  pause
  exit /b 1
)

echo Setting vault to this folder...
".venv\Scripts\chatgpt-obsidian-memory.exe" config set-vault "%CD%"
if errorlevel 1 (
  ".venv\Scripts\python.exe" -m chatgpt_obsidian_memory.cli config set-vault "%CD%"
)

echo.
echo Starting app...
echo Browser will open at http://127.0.0.1:8765
echo Leave this window open. Close it to stop.
echo.

".venv\Scripts\python.exe" -m chatgpt_obsidian_memory.desktop
echo.
pause
