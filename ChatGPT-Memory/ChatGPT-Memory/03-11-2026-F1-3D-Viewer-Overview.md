---
title: F1 3D Viewer - Overview
saved_at: 2026-11-03
source: opencode-session
tags: [f1, viewer, racevision, opencode, overview]
---

# F1 3D Viewer - Overview

A **browser-native 3D broadcast viewer** for the real Mexico City GP circuit, built in
three.js. This is a working prototype of the 3D-rendering + live-tracking pillar of
[[05-10-2026-Racevision-F1-Project|RaceVision]] - real converted track, real telemetry
plumbing, broadcast cameras, HUD.

## Quick start

```powershell
cd "C:\Users\shash\OneDrive\Documents\Default Project\f1-3d-viewer"
python -m http.server 8000 --bind 127.0.0.1
```

- **Viewer:** <http://127.0.0.1:8000/> (real Mexico City world by default)
- **Live telemetry page:** <http://127.0.0.1:8000/f1-live.html> (OpenF1: live when a
  session is on track, otherwise replays the most recent completed session's fastest lap)
- Hard-refresh (`Ctrl+Shift+R`) after code changes - browsers cache ES modules

## What it does

- Real circuit: `mexico_city.blend` converted to `mexico_scene.glb` (26.5 MB, textures
  embedded) + racing line extracted from `RV_Track` (4.2894 km, 1077 pts)
- 8 cars race the real 4.3 km lap on a physically-derived speed profile (grid start,
  slipstream, overtakes), sculpted modern-F1 car models
- 9 camera modes: free / director / helicopter / TV trackside / chase / battle / t-cam /
  nose / rear - all with dt-normalised springs, zero jitter
- HUD: camera menu, driver chips, battle gap widget, onboard card, source pill
- Telemetry hub with three interchangeable sources (SIM / REPLAY / LIVE OpenF1)
- Photo pack (CC0 HDRIs + PBR) and night mode; quality tiers that auto-drop

## Data flow

```
telemetry source (SIM engine | replay frames | OpenF1 live)
   -> TelemetryHub: interpolate/dead-reckon to 60 fps
   -> lap distance s -> circuit spline (sample/sDist)
   -> world.update(): place cars, wheels, glow ring
   -> CameraDirector + Hud render the broadcast
```

## Key artifacts

| Artifact | Path (under `Default Project\f1-3d-viewer\`) | Size | md5 |
| --- | --- | --- | --- |
| Source scene | `assets/mexico_city.blend` (pristine, never modified) | 3,170,177 | `B082408CFE1A0C57A5A9BE37B6F89BB4` |
| Converted world | `assets/mexico_scene.glb` | 27,767,132 | `7A2FC41628173772131EF2834A04E634` |
| Racing line | `assets/mexico_racingline.json` | 25,467 | `7AB15246694B1F0CBA61BB67444999FC` |
| Pipeline tools | `tools/` (converter, QA renders, test harnesses) | - | - |

## Note map

- [[03-11-2026-F1-3D-Viewer-Architecture|Architecture]] - modules, contracts, no-jitter design
- [[03-11-2026-F1-3D-Viewer-Mexico-Track-Pipeline|Mexico Track Pipeline]] - blend -> GLB + racing line
- [[03-11-2026-F1-3D-Viewer-Car-Rebuild|Car Rebuild]] - orientation fix + photoreal cars
- [[03-11-2026-F1-3D-Viewer-Telemetry|Telemetry Sources]] - SIM/REPLAY/LIVE, OpenF1 findings
- [[03-11-2026-F1-3D-Viewer-LivePage|Live Page]] - f1-live.html
- [[03-11-2026-F1-3D-Viewer-AC-Research|Assetto Corsa Research]] - modding feasibility answer
- [[03-11-2026-F1-3D-Viewer-Operations|Operations]] - serving, testing, troubleshooting
- [[03-11-2026-F1-3D-Viewer-Open-Threads|Open Threads]] - what is still pending
