@echo off
setlocal EnableExtensions
title Obsidian Memory Chat

REM Always use your Windows Obsidian Memory Chat folder as the vault
set "VAULT=C:\Users\shash\.cursor-tutor\Obsidian Memory Chat"
set "NOTES=%VAULT%\ChatGPT-Memory"
set "CHATGPT_OBSIDIAN_VAULT=%VAULT%"

if not exist "%VAULT%" mkdir "%VAULT%"
if not exist "%NOTES%" mkdir "%NOTES%"

REM Prefer remaining in the install folder if this bat lives there;
REM otherwise force cd into the vault so pip install -e finds pyproject.toml
cd /d "%~dp0.."
if not exist "pyproject.toml" (
  cd /d "%VAULT%"
)
if not exist "pyproject.toml" (
  echo Could not find pyproject.toml.
  echo Extract the full zip into:
  echo   %VAULT%
  pause
  exit /b 1
)

echo ============================================
echo   Obsidian Memory Chat
echo ============================================
echo Vault:
echo   %VAULT%
echo Notes (Share imports go here):
echo   %NOTES%
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

echo Forcing vault path to Windows folder...
".venv\Scripts\python.exe" -m chatgpt_obsidian_memory.cli config set-vault "%VAULT%"
if errorlevel 1 (
  echo Failed to set vault path.
  pause
  exit /b 1
)

echo.
echo Starting app...
echo Browser will open at http://127.0.0.1:8765
echo Confirm Vault shows:
echo   %VAULT%
echo Share imports save into:
echo   %NOTES%
echo Leave this window open. Close it to stop.
echo.

".venv\Scripts\python.exe" -m chatgpt_obsidian_memory.desktop
echo.
pause
