---
title: F1 3D Viewer - Open Threads
saved_at: 2026-11-03
source: opencode-session
tags: [f1, viewer, opencode, todo, roadmap]
---

# F1 3D Viewer - Open Threads

Part of [[03-11-2026-F1-3D-Viewer-Overview|F1 3D Viewer]]. What is still pending
(Nov 3-4, 2026).

## House-rule documentation (pending)

- `assets/MANIFEST.md`: add GLB + racing-line provenance entries (sizes, md5s, Poly
  Haven CC0 lineage, conversion notes) - values all captured in the pipeline note
- `README.md`: document `?world=real|code` and the real-track mode

## Decisions waiting on the user

- **Playwright install (~400 MB)** - would enable the `site-check` skill: real-browser
  screenshots of the viewer at every vantage/light + a truthful check of `f1-live.html`
  rendering (so far it is verified by API mirror + syntax, not by an actual browser).
- **Next demo build**: wire a real session into the 3D viewer itself (FastF1 export ->
  `F1Viewer.feedTelemetry(...)`), i.e. Mexico 2026 race data driving the viewer's
  interpolation pipeline end-to-end.
- **AC bridge spec** (optional long project): 2-car CSP Custom AI demo plan - see
  [[03-11-2026-F1-3D-Viewer-AC-Research|AC Research]].

## Loose ends in the codebase

- `f1-live.html`: `?session=`/`&driver=` pinning is implemented but not yet exercised in
  a real browser; live mode awaits the next on-track session (calendar: races through
  Dec 6, Yas Marina)
- Optional visual polish: test the replay page on a narrow window (grid is responsive but
  unverified on phone)
- Racing line could later be refined from centreline to a true racing line (apex-hugging)
  - current profile is intentionally conservative (97 s lap estimate)

## RaceVision alignment (bigger picture)

This viewer is effectively the working prototype of RaceVision's 3D pillar. Possible
hooks when wanted:

- Feed the viewer from the RaceVision PostgreSQL telemetry store (same `{kph, rpm, gear}`
  frame contract the hub already consumes)
- Convert more circuits from `.cursor-tutor\RaceVision\blender\tracks\` with the same
  pipeline (converter + racing-line extraction are generic)
- OBS/broadcast overlays: the viewer already has `?record=1` scripted tours and a
  frame-capture workflow

## Cleanup notes

- Pipeline scripts now preserved in `f1-3d-viewer\tools\` - the `Temp\opencode` copies
  (incl. diagnostics `inspect_blend.py`, `uv_diag.py` etc.) can be deleted anytime
- Old duplicated `f1-live.html` in the Project root is a stale summary file; the live
  copy is `f1-3d-viewer\f1-live.html`
