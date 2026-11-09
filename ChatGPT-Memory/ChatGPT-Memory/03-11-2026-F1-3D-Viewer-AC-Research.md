---
title: F1 3D Viewer - Assetto Corsa Research
saved_at: 2026-11-03
source: opencode-session
tags: [f1, racevision, opencode, assettocorsa, research]
---

# Assetto Corsa - Replay Feasibility Research

Question asked: could we make an Assetto Corsa mod and **inject F1 telemetry to watch a
race replay in AC**? Researched against the current CSP (Custom Shaders Patch) surface.
Verdict: **possible as a live re-enactment - impossible as "replay injection" - and a
big project.**

## Part 1 - mods: three kinds, three answers

| Kind | Feasibility |
| --- | --- |
| CSP Lua script/app ("code mod") | Tractable (days) - custom game modes/HUDs/physics scripts |
| Car mod (KN5 + physics INI + audio) | Months of specialist work; redundant - RSS/VRC-class F1 cars already exist |
| Track mod (we have `mexico_city.blend`) | Big project: KN5 export + collision meshes + `surfaces.ini` + `fast_lane.ai` + `cameras.ini` + LODs |

## Part 2 - feeding telemetry into AC

AC has **no API to author or inject replay files** - replays are recordings the game
makes itself. But CSP added an external control gateway:

- **Custom AI** (memory-mapped files): an external program creates
  `AcTools.CSP.NewBehaviour.CustomAI.CarControls<N>.v0` and writes
  **gas/brake/steer/clutch/gear** (CSP reads at **333 Hz**), even a teleport vector
  (`teleport_to=1` pits / `2` + `teleport_pos`). CSP writes back full car state in
  `Car<N>.v0`. Enable: `extension/config/new_behaviour.ini` -> `CUSTOM_AI ENABLED=1`.
  **Offline sessions only** (not remote cars).
- **CSP Lua**: `ac.CarControlsInput` (control override), per-car physics scripts
  (`script.lua`), "new game modes" - a replay mode could live here.

### Why it degrades to "re-enactment"

1. **No steering channel exists in F1 data** (verified against the raw feed topic set) -
   steering must be *reconstructed* from `Position.z` x/y/z paths via a follower
   controller. Every corner becomes tuning.
2. You feed **inputs into a physics sim, not poses** - errors accumulate; corrections =
   teleports (look like lag).
3. Dependencies: AC + CSP + era-correct car mod + Mexico track mod.

### Two implementable paths

- **A. Physics re-enactment (recommended)**: hybrid - steering follows the recorded
  path, speed target from `CarData.z`, replay gear/DRS events. Smooth; close, not exact.
- **B. Kinematic teleport-follow**: interpolate positions, set poses every tick. Exact
  motion; fights reset/damage/audio systems; brittle.

Plus a prerequisite: **coordinate registration** - fit FOM map space -> AC track metres
with a 2D similarity transform (scale/rotation/translation, least-squares against the
track centreline). Both describe the same physical circuit; converges cleanly.

## Data availability (from the raw F1 feed)

`CarData.z` (~3.7 Hz): speed, rpm, gear, **throttle 0-100, brake 0-100**, DRS.
`Position.z`: x/y/z + status. `TimingData`: gaps/positions. Plus flags/SC/stints/radio -
a full broadcast layer. **The data is not the bottleneck - AC's inability to be posed
kinematically is.**

## Recommendation recorded

Keep the three.js viewer as the replay renderer (it is the correct architecture - see
the f1-race-replay open-source project for prior art). If AC-grade visuals are ever
wanted, scope the **CSP "Replay Mode" app + external bridge** as a long project
(2-car demo on a community Mexico track first). Related: `tobi/ac-tracer` shows the
CSP-Lua telemetry-app ecosystem is mature.
