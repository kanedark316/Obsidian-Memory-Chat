---
title: F1 3D Viewer - Car Rebuild
saved_at: 2026-11-03
source: opencode-session
tags: [f1, viewer, racevision, opencode, cars, threejs]
---

# F1 3D Viewer - Car Rebuild

Part of [[03-11-2026-F1-3D-Viewer-Overview|F1 3D Viewer]]. Two jobs: **turn the cars
around**, then **make them look like real F1 cars**. File: `cars.js`.

## Bug 1 - the cars drove backwards (also fixed wheels + steering)

- Root cause: the model was authored **nose at local -Z** (front wing z=-2.30, front
  wheels z=-1.50), but the viewer yaws cars with `atan2(tan.x, tan.z)` which points local
  **+Z** along travel. Every car drove tail-first; wheels spun backwards to match;
  steering looked inverted. Latent since the beginning - the real track made it obvious.
- Fix (baked, not a runtime hack):
  - `bodyGeo.rotateY(Math.PI)` + same for carbon shell; helmet/plate/wheel positions
    mirrored in Z (front wheels now at +1.50)
  - Wheel spin sign: `rotation.x += ds / r` (was `-`)
  - Onboard cams mirrored to the new nose in `cams.js`: tcam `oz -0.28`,
    nose `oz +2.15`, rear `oz -1.15`
- Verified numerically by the smoke test: **rear wing 0.91 m high at the tail, front wing
  0.29 m at the nose** - cars face forward

## Bug 2 - boxes to photoreal (sculpted rebuild)

Full rewrite of `makeCar()` around a reusable **profile-sweep loft**:

- `loft(rings, axis)` - closed rings of `{pos, pts[[a,b]]}`, auto-orients winding by
  testing the first quad against the centreline (no manual normal juggling, ever), caps
  optional. This is the tool to reuse for any future vehicle/asset
- Volumes: monocoque->engine cover (10-pt body rings), mirrored sidepods (undulating,
  inlet faces), shark fin, airbox; floor + diffuser + edge fences
- `wingGeo(span, chord, thick, y0, z0, {lift, curve, attack})` - thin lens profile swept
  across the span with dihedral, tip sweep and angle of attack: 3-element front wing,
  rear wing + DRS flap + beam wing; endplates as 2-ring plate lofts
- Details: halo (torus + pillar strut), **wishbone + pushrod suspension** (12 thin
  cylinders via `strutGeo`), mirrors, T-cam pod, visor, cockpit plate, headrest,
  number roundel on the nose (`alphaTest` so the circle crops cleanly)
- Wheels: **LatheGeometry tyre** with rounded shoulders + rim + accent ring, merged with
  material groups `[tyre, rim, accent]`; shared geometries `WHEEL_F(0.33, 0.30)` /
  `WHEEL_R(0.35, 0.42)` across the fleet
- Materials: clearcoat `MeshPhysicalMaterial` paint + flake normal map; carbon with a
  procedural **2x2 twill weave normal map**; rubber with `DoubleSide`
- Cost: still **8 meshes per car** (paint, accent, carbon, plate, 4 wheels) - fleet draw
  count unchanged
- Public API unchanged: `makeCar(color, accent, num) -> { group, wheels, code,
  roll(s, dt, steer), resetTracking(), dispose() }`

## Verification harness: `tools/car-smoke-test.mjs`

Runs the REAL `cars.js` outside the browser (node + three from npm + a tiny `document`
stub for canvas textures; the CDN specifier `three/addons/` is remapped to
`three/examples/jsm/` for the npm layout). Asserts:

- orientation (tail high / nose low - the regression test for the backwards bug)
- overall dims ~2.06 x 1.04 x 5.29 m; wheels touch y=0
- wheel spin: +0.1 m at r=0.33 -> rotation.x +0.303; fronts steer, rears don't
- all positions finite; 8 cars build; 8 meshes each

Result: **PASS - 8 cars, 8 meshes on car #44**. To re-run: copy `cars.js` + `kit.js`
next to the test, `npm i three@0.169.0`, remap the specifier, `node test.mjs`
(see [[03-11-2026-F1-3D-Viewer-Operations|Operations]] for the exact commands).
