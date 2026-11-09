---
title: F1 3D Viewer - Architecture
saved_at: 2026-11-03
source: opencode-session
tags: [f1, viewer, racevision, opencode, architecture]
---

# F1 3D Viewer - Architecture

Part of [[03-11-2026-F1-3D-Viewer-Overview|F1 3D Viewer]].

## Modules (`f1-3d-viewer\*.js`)

| File | Holds |
| --- | --- |
| `main.js` | renderer + post stack (GTAO/bloom), quality tiers, vantage flights, frame loop, `?world=` selection, public API `window.F1Viewer` |
| `real-world.js` | **real Mexico City world**: GLB load + material/shadow pass, spline tables from the racing line, grid start engine, vantage table keyed to the real track |
| `scene.js` | procedural world (code mode): grandstands, crowd, dome, trees, fleet |
| `track.js` | procedural circuit: spline, arc-length, curvature, speed profile, ribbon builder |
| `sim.js` | `RaceEngine` - fixed 1/120 s substeps, slipstream, overtake state machine, RPM/gear; **track-injectable** (default procedural; real world passes its own tables) |
| `telemetry.js` | `TelemetryHub` + `DriverBuffer` (interpolation, dead-reckon), Replay + OpenF1 Live sources |
| `cams.js` | `CameraDirector` - 9 modes + director sequence, dt-normalised springs |
| `hud.js` | camera menu, chips, gap widget, onboard card, source pill |
| `cars.js` | sculpted F1 car factory (lofted body, wings, halo, suspension, lathed tyres) |
| `env.js` | sky/sun/IBL/fog/night presets; shared uniforms `U.uTime/uWind/uNight` |
| `photo.js` | photo pack: CC0 HDRI -> `scene.environment`, PBR maps onto registered surfaces |
| `surface.js` | name -> material registry the photo layer patches |
| `kit.js` | seeded RNG, canvas textures, instancing kit, lathe/sweep |

## Core contracts

**Track API** (both worlds expose the same shape; cameras/telemetry only use this):

```js
track = {
  L,                       // lap length (metres)
  sample(s),               // -> { p: Vector3, tan, nor, cur, v }  (point, tangent, left-normal, signed curvature, speed)
  sDist(a, b),             // wrap-safe signed distance a-b along the lap
  sNear(x, z),             // arc length of nearest spline point
  anchors,                 // landmark arc lengths (start, stadium, esses, ...)
}
```

**World API** (consumed by cameras/HUD/main):

```js
world = {
  group,                   // THREE.Group added to the scene
  engine,                  // RaceEngine
  track, fleet, byCode, codes, centroid, vantage,
  colorOf(code), initialS(code), placeOnTrack(s, v),
  resetTracking(), ringTo(code),
  update(dt, hub, viewer), // -> { states, pair } for cameras/HUD
}
```

## No-jitter design (the signature feature)

- **SIM**: physics at fixed `1/120 s`; every frame renders the *interpolated* state at
  `alpha = acc / FIXED` between `prev`/`cur` snapshots - motion never quantises
- **Cameras**: springs with `k = 1 - e^(-r*dt)` so ramps are refresh-rate-independent
- **LIVE/REPLAY**: feeds arrive ~3-4 Hz; the hub maps source timestamps to the wall clock
  and interpolates between the newest two frames; stalled feed coasts 1.5 s, then freezes
  and flags `LIVE - SIGNAL LOST` after 2.5 s

## Two worlds: `?world=real|code`

- **real (default)**: loads `assets/mexico_scene.glb` + `assets/mexico_racingline.json`;
  on any load failure `main.js` logs and falls back to procedural
- **code**: `?world=code` - the original procedural Mexico-inspired circuit
- Real-world extras: `tvLat: 16 / tvHeight: 9` (trackside cams clear the catch fences),
  grid start (`new RaceEngine(7, track, { grid: true })` - cars 7 m/row behind the line)

## Coordinate conventions (important)

- Car local: **+Z = nose = direction of travel**; viewer yaw = `atan2(tan.x, tan.z)`
  maps local +Z onto the track tangent
- Blender -> glTF (what the exporter does): `(x, y, z)_blender -> (x, z, -y)_three`
- Racing line is recentred so the road plane is `y = 0`; the GLB is shifted by the same
  base offset (`gscene.position.y = -baseY`)
