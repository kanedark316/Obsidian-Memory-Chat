@echo off
REM Double-click shortcut at project root — runs the real launcher in scripts\
cd /d "%~dp0"
call "%~dp0scripts\Start-Obsidian-Memory-Chat.bat"
