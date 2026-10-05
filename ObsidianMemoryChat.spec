# -*- mode: python ; coding: utf-8 -*-
# Optional PyInstaller spec (scripts/build-windows-exe.ps1 can also build without this).

from PyInstaller.utils.hooks import collect_submodules

hidden = collect_submodules("uvicorn") + [
    "chatgpt_obsidian_memory.web.app",
    "chatgpt_obsidian_memory.share",
]

a = Analysis(
    ["src/chatgpt_obsidian_memory/desktop.py"],
    pathex=[],
    binaries=[],
    datas=[
        (
            "src/chatgpt_obsidian_memory/web/static",
            "chatgpt_obsidian_memory/web/static",
        )
    ],
    hiddenimports=hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="ObsidianMemoryChat",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
