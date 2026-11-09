---
title: F1 3D Viewer - Telemetry Sources
saved_at: 2026-11-03
source: opencode-session
tags: [f1, viewer, racevision, opencode, telemetry, openf1]
---

# F1 3D Viewer - Telemetry Sources

Part of [[03-11-2026-F1-3D-Viewer-Overview|F1 3D Viewer]]. Where the numbers come from.

## The contract

Everything implements one interface: **per driver, a stream of `{ kph, rpm, gear }`
frames ordered in time**. The hub integrates lap distance from speed
(`s += kph/3.6 * dt`) and rides the circuit spline - GPS coordinates are deliberately
**not** used directly (F1's 3D map lives in its own coordinate system; distance
integration is how you map any speed feed onto any circuit faithfully).

## Three interchangeable sources (pill top-right shows which)

| Source | Pill | What it is |
| --- | --- | --- |
| SIM | `SIM TELEMETRY` | Built-in procedural race (`sim.js`): speed profile from track curvature, slipstream, overtakes, RPM/gear from speed |
| REPLAY | `REPLAY TELEMETRY` | Your own data: `F1Viewer.feedTelemetry([...])` rows or CSV text; loops in real time |
| LIVE | `LIVE TELEMETRY` | OpenF1 session polling: `F1Viewer.connectOpenF1(sessionKey)` (~3-4 Hz, no key, CORS-open). Stalls coast 1.5 s then freeze + `SIGNAL LOST` |

Smoothing: the hub keeps the newest frames per driver, maps source timestamps onto the
wall clock, interpolates display poses between the newest two - the 60 fps camera never
sees a 3 Hz step.

## OpenF1 API notes (verified live during this session)

- Base: `https://api.openf1.org/v1` - no key, CORS-open (`access-control-allow-origin`),
  history + live.
- Endpoints used by the live page: `/sessions?year=`, `/drivers?session_key=`,
  `/laps?session_key=`, `/car_data?session_key=&driver_number=&date>=...&date<=...`,
  `/location?session_key=&driver_number=&date...`
- **Gotcha: `/position` is the RANKING feed** (rows only when race position changes -
  returns 404/empty for quiet windows). Track x/y/z coordinates are `/location`
  (`{x, y, z}`; z/x = plan plane, y = elevation). Cost a debugging round.
- **Rate limits are real**: HTTP 429 on bursts. Pace requests (~1.5 s apart), and use
  retry/backoff (the page retries 429s up to 4x with increasing waits; keep under
  ~20 req/min).
- `car_data` row: `{date, driver_number, speed, rpm, n_gear, throttle, brake, drs}` -
  throttle/brake are 0-100.
- `drs` codes: >=10 open, 8 ready/eligible, else off.

### Verified example (used as the page's replay demo)

- Most recent completed session: **2026 Mexico City Race, session 11404** (Nov 1)
- Fastest lap: driver 44 (HAMILTON, Ferrari `ED1131`), lap 50, **1:19.268**
- Window data: 306 car_data rows + 322 location rows; first row gear 7, 10957 rpm,
  throttle 99, speed 275 km/h

## Official F1 livetiming feed (the raw SignalR service)

Investigated because the user's other tool was building a page against it:

- `https://livetiming.formula1.com/signalr/negotiate` returns **HTTP 401** and **no CORS
  headers** - a plain browser page can never consume it directly. Every working project
  (f1-dash, MultiViewer) runs a **server-side proxy**. Any browser-only attempt is
  doomed regardless of decoding fixes.
- The full topic list (canonical broadcast data set, for a future proxy):
  `Heartbeat, SessionInfo, ArchiveStatus, SessionStatus, SessionData, DriverList,
  TimingData, TimingDataF1, TimingAppData, TimingStats, TopThree, LapCount, LapSeries,
  ExtrapolatedClock, TrackStatus, Position.z, CarData.z, WeatherData, WeatherDataSeries,
  RaceControlMessages, TlaRcm, RcmSeries, TeamRadio, AudioStreams, ContentStreams,
  CurrentTyres, TyreStintSeries, PitLaneTimeCollection, ChampionshipPrediction,
  DriverRaceInfo, DriverScore, SPFeed, PitStop, PitStopSeries, DriverTracker,
  OvertakeSeries`
- `*.z` topics = **zlib-deflated base64 JSON**; `CarData.z` carries per-car
  speed/rpm/gear/**throttle 0-100/brake 0-100**/DRS at ~3.7 Hz; `Position.z` carries
  x/y/z + status. No steering channel exists anywhere public - derive it from positions
  if ever needed.

See also: [[03-11-2026-F1-3D-Viewer-LivePage|Live Page]] and
[[03-11-2026-F1-3D-Viewer-AC-Research|Assetto Corsa Research]] (why this data can't be
injected into AC replays directly).
