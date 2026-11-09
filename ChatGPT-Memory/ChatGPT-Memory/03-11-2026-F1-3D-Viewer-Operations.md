---
title: F1 3D Viewer - Operations
saved_at: 2026-11-03
source: opencode-session
tags: [f1, viewer, opencode, operations, troubleshooting]
---

# F1 3D Viewer - Operations

Part of [[03-11-2026-F1-3D-Viewer-Overview|F1 3D Viewer]]. Run/verify/troubleshoot.

## Serving

```powershell
cd "C:\Users\shash\OneDrive\Documents\Default Project\f1-3d-viewer"
python -m http.server 8000 --bind 127.0.0.1     # keep it running
```

- <http://127.0.0.1:8000/> - 3D viewer (`?world=real` default, `?world=code` procedural,
  `?light=`, `?view=`, `?quality=`, `?photo=0`, `?envI=`, `?record=1`)
- <http://127.0.0.1:8000/f1-live.html> - live/replay telemetry page
- **Server lifecycle**: background servers die whenever the OpenCode app restarts. If
  the browser 404s everything, the server is gone - restart it.
- **Root gotcha**: the server is rooted at `f1-3d-viewer\`. Files in the *Project root*
  (one level up) are NOT served at `/`. Historical confusion source - keep served files
  inside `f1-3d-viewer\`.
- Browser caching: hard-refresh (`Ctrl+Shift+R`) after edits - ES modules cache.

## Blender recipes (5.2)

```powershell
# run a script against a .blend (recommended wrapper; ~40-90 s per launch)
python ".opencode\skills\blender-core\scripts\run_in_blender.py" --blend <file.blend> <script.py>
# standalone headless (for GLB tools etc.)
& 'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe' --factory-startup -b --python-exit-code 1 -P <script.py>
```

## Node verification recipes

```powershell
# syntax-check an ES module (copy to .mjs; --check only parses)
Copy-Item .\main.js "$env:TEMP\chk.mjs"; node --check "$env:TEMP\chk.mjs"

# racing-line maths sanity (tools/chk_raceline.mjs) - prints L, spacing, speed profile
node "f1-3d-viewer\tools\chk_raceline.mjs"

# OpenF1 API mirror (tools/chk_f1live.mjs) - validates the live page's exact calls
node "f1-3d-viewer\tools\chk_f1live.mjs"

# car smoke test (tools/car-smoke-test.mjs): needs node_modules three + cars.js/kit.js
# next to it + the `three/addons/` -> `three/examples/jsm/` specifier remap
```

## Quick health checks (PowerShell)

```powershell
curl.exe -s -o NUL -w "%{http_code}`n" http://127.0.0.1:8000/                  # 200 = viewer up
curl.exe -s -o NUL -w "%{http_code}`n" http://127.0.0.1:8000/f1-live.html      # 200 = page up
Get-NetTCPConnection -LocalPort 8000 -State Listen | Select LocalAddress, OwningProcess
```

## Troubleshooting

| Symptom | Cause / fix |
| --- | --- |
| Everything 404s | Server died with an app restart - restart it |
| A root-level file 404s at `/` | Wrong root (see gotcha above) - move it into `f1-3d-viewer\` |
| Viewer loads but world is procedural | GLB/JSON failed to load - check console; files live in `f1-3d-viewer\assets\` |
| `/f1-live.html` shows stale content | Hard refresh; check the served copy is the one being edited |
| OpenF1 page errors | 429 rate limit (retries built in) or no network; check console |
| Cars backwards / wheels wrong | Re-run `tools/car-smoke-test.mjs` orientation assertions |
| GS label textures broken | Blender UV attribute corruption - see the pipeline note's gotchas |

## Preserved tooling (`f1-3d-viewer\tools\`)

`build_mexico_glb.py` (blend -> GLB converter), `chk_raceline.mjs`, `chk_f1live.mjs`,
`car-smoke-test.mjs`, `review_glb.py` + `review_glb_close.py` (Blender QA renders).
These were rescued from `Temp\opencode` so the pipeline no longer depends on temp state.
