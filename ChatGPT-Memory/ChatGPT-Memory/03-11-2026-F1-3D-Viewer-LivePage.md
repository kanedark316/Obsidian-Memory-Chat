---
title: F1 3D Viewer - Live Page (f1-live.html)
saved_at: 2026-11-03
source: opencode-session
tags: [f1, viewer, opencode, live, openf1]
---

# F1 3D Viewer - Live Page

Part of [[03-11-2026-F1-3D-Viewer-Overview|F1 3D Viewer]].

## What it is

`f1-3d-viewer\f1-live.html` - a self-contained telemetry dashboard served next to the 3D
viewer at **<http://127.0.0.1:8000/f1-live.html>**. Built after finding the previous
attempt (SignalR client in the Project root, later overwritten by a summary file) could
never work from a browser - see
[[03-11-2026-F1-3D-Viewer-Telemetry|Telemetry Sources]] for the 401/no-CORS finding.

## Modes (chosen automatically)

- **LIVE** when a session is on track (date window + 45 min grace): polls every 6 s -
  driver table (speed/gear/rpm/throttle/brake/DRS), live track map built from
  `/location` dots, click a row to pin a driver
- **REPLAY** otherwise: finds the most recent completed session, takes its **fastest
  lap**, animates it - big readouts, throttle/brake bars, speed trace canvas, track map
  with the moving car; play/pause + 0.5x/1x/2x/4x; loops
- URL params: `?session=KEY` pins a session, `&driver=NUM` pins a driver

## Engineering details

- Zero dependencies (no pako needed - OpenF1 is plain JSON), vanilla JS + canvas
- **Rate-limit aware**: 429 -> retry with backoff (4 attempts, increasing waits);
  requests paced ~0.5 s apart; live polling at 6 s (~20 req/min)
- Uses `/car_data` (windowed by `date>=`/`date<=`) and `/location` (**not** `/position` -
  that is the ranking feed, see Telemetry note)
- Data cost per replay: ~300 car rows + ~320 location rows for a lap window

## Verification performed

- Inline script extracted + `node --check` passed
- `tools/chk_f1live.mjs` - a node mirror of the page's exact API sequence, run against
  the live service: found Mexico 2026 Race (session 11404), best lap HAM 1:19.268 lap 50,
  fetched and validated both data windows end-to-end (`ALL OK`)

## Related history

- The user's earlier `05-10-2026-Live-F1-Tracking-Data` note already identified OpenF1 as
  the practical tracking API - this page is that idea, realized
- The viewer's built-in LIVE mode (`F1Viewer.connectOpenF1(key)`) and this page now use
  the same provider for a consistent story
