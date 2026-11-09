---
title: F1 3D Viewer - Mexico Track Pipeline
saved_at: 2026-11-03
source: opencode-session
tags: [f1, viewer, racevision, opencode, blender, pipeline]
---

# F1 3D Viewer - Mexico Track Pipeline

Part of [[03-11-2026-F1-3D-Viewer-Overview|F1 3D Viewer]]. How `mexico_city.blend`
became the viewer's real world: `mexico_scene.glb` + `mexico_racingline.json`.

## Source scene

- `Default Project\f1-3d-viewer\assets\mexico_city.blend` (3,170,177 B,
  md5 `B082408CFE1A0C57A5A9BE37B6F89BB4`) - user-supplied RaceVision-style Mexico City GP
  scene: `RV_Track`, stadium, pit complex, Tecpro, catch fences, 44 masts, city, 20 grid
  empties, labels
- Inspection (headless Blender 5.2): 245 objects, ~229k verts; no linked libraries, no
  embedded scripts - clean
- Textures: 12 external JPEGs (diffuse/normal/roughness x 4 sets) - all **Poly Haven CC0**:
  `asphalt_02`, `concrete_floor`, `gravel_ground_01`, `metal_plate`

## Conversion (`tools/build_mexico_glb.py`)

Runs **in memory only** - the `.blend` is never saved/modified. Steps:

1. Record anchors: `Car_Template` position, `RV_StartFinish` mesh centroid
2. Texture fallback remap (never triggered - all files present)
3. **Box-project UVs** for every image-material mesh (see gotchas): per-face dominant
   world normal picks the projection axis; UVs in metres; un-mirror flips on backfaces;
   metre scales asphalt 4 / concrete 5 / gravel 3 / metal 3; colour-only meshes ship
   textureless (**no UV layer at all** - empty layers break the exporter)
4. Extract the **racing line** (below) *before* deleting anything
5. `Mesh.validate()` pass; drop the pathological label mesh; drop 125 non-mesh objects
   (cameras, lights, empties)
6. Export: `bpy.ops.export_scene.gltf(format=GLB, image_format='AUTO', yup=True,
   no cameras/animations/draco)`

### Results

- `assets/mexico_scene.glb` - 27,767,132 B, md5 `7A2FC41628173772131EF2834A04E634`
  (textures embedded: 12 JPEGs; 275,132 tris across 119 meshes / 43 materials)
- `assets/mexico_racingline.json` - 25,467 B, md5 `7AB15246694B1F0CBA61BB67444999FC`

## Racing line extraction (the core trick)

`RV_Track` is a closed quad ribbon (~2 m faces, 2153 faces). The script:

1. Builds face adjacency (edges shared by exactly 2 faces - validates clean loop)
2. Walks the cycle; per-face centre = ribbon centreline
3. Decimates every ~4th face -> **1077 points**, gentle 1-2-1 smoothing x2
4. Rotates the cycle so index 0 = point nearest the start/finish **paint**, and flips the
   direction so a few metres after the line head **+X** (matches the 20 grid empties)
5. Converts Blender->glTF coords: `(x, z, -y)` -> JSON `[[x, y, z], ...]`

### Verified numbers (via `tools/chk_raceline.mjs`)

| Metric | Value |
| --- | --- |
| Length | 4,289.4 m (real Autodromo lap ~4.3 km) |
| Points / spacing | 1077 @ mean 3.98 m (uniform - extraction is faithful) |
| Speed profile vMax | 317 km/h at s=119 (main straight) |
| vMin | 57 km/h at s=3696 (slowest corner) |
| Estimated lap | 97 s (centreline + conservative grip; fine for the demo) |

## Blender 5.2 gotchas (hard-won, reusable)

- `mesh.uv_layers.new()` returns **None** when a broken `UVMap` shares the attribute
  namespace with an orphaned `.pn.UVMap` marker (CORNER/BOOLEAN). Fix: purge CORNER
  FLOAT2 + `.pn.*` attributes at the **attribute** level first
- An **empty** UV layer (`len(uv.data) == 0` vs loops 6904) crashes the glTF exporter
  (`foreach_get sequence length mismatch given 6904, needed 0`)
- Textures fed through **non-UV coordinates** cannot export; meshes need real UVs
  (hence the box projection)
- One label mesh (`RV_Label_MEXICO CITY.002`) had internal corruption the exporter could
  not handle (`IndexError: index 1424 out of bounds`, validate() did not flag) - dropped;
  two identical billboards remain in the scene
- Workflow note: run scripts inside Blender via
  `.opencode\skills\blender-core\scripts\run_in_blender.py --blend <file> <script.py>`

## Visual QA (`tools/review_glb.py`, `tools/review_glb_close.py`)

Runs inside Blender: imports the GLB, renders geometry contact sheets (skill
`blender-asset-qa`) + Workbench TEXTURE passes + **EEVEE lit renders**. Outputs in
`Temp\opencode\mexico_review\` (close-ups of start line, stadium, pit; EEVEE shots show
textured layout, kerbs, catch fences - all correct). EEVEE engine id in 5.2:
`BLENDER_EEVEE`.

## Re-run recipe

```powershell
$blender = 'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe'
python ".opencode\skills\blender-core\scripts\run_in_blender.py" `
  --blend "f1-3d-viewer\assets\mexico_city.blend" `
  "f1-3d-viewer\tools\build_mexico_glb.py"          # ~1 min; rewrites GLB + JSON
& $blender --factory-startup -b --python-exit-code 1 -P "f1-3d-viewer\tools\review_glb.py"   # QA sheets
```
