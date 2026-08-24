# ROADMAP.md

# Universal Immersive Scene Platform Roadmap

## Phase 1 — Intelligent Images ✅ COMPLETE

Objectives:

- [x] Display a standard image.
- [x] Load scene.json.
- [x] Display hotspots.
- [x] Click hotspots.
- [x] Zoom and pan.
- [x] HTML controls viewer.

Deliverable:

A browser-based intelligent image. **Built and validated** against real photo content
(not just the demo illustration), with `Scene.load/goto/highlight/find/search` implemented
against the spec's API surface, real `fetch()`-based scene loading (not embedded data),
and per-object shareable URLs (`?object=<id>`) per Principle 10.

Also delivered beyond the original objectives: an AI-assisted + manual authoring tool
(`authoring/scene-authoring.html`) combining open-source object/face detection with
click-to-place manual hotspots, per Principle 8 (AI Assists, Humans Decide) — every
AI suggestion requires human review/inclusion before export.

---

## Phase 2 — Deep Zoom ✅ COMPLETE

Objectives:

- [x] Large images.
- [x] Image tiling.
- [x] High-resolution viewing.
- [x] Object persistence.

Deliverable:

Museum-quality zoomable image viewer. **Built and validated** against a real high-resolution
photo. Rendering backed by OpenSeadragon; `tools/make_tiles.py` is the server-side tiling
pipeline (pure Python/Pillow, standard DZI format, no external C library dependency).

Notable architectural outcome: `index.html` (the viewer) handles both flat images and
tiled pyramids through the *same* `Scene.*` API and the same file, with no `media.type`
flag needed — the distinction is resolved automatically from the file OpenSeadragon is
asked to open. This was a real test of Principle 4 (Renderer Independence) under an
actual engine swap (CSS transforms → OpenSeadragon), not just a design assumption.

Two real bugs were found and fixed during validation, not just theorized about:
1. The tile pyramid generator originally stopped early instead of generating down to a
   proper 1×1 base level, which would have caused silent tile 404s at extreme zoom-out.
2. OpenSeadragon does not auto-detect a bare image URL as a plain (non-tiled) source —
   only pyramid descriptors (`.dzi`/`.xml`/IIIF) auto-resolve. Plain images need an
   explicit `{ type: 'image', url }` wrapper. Fixed in one isolated function
   (`resolveTileSource`) rather than special-cased throughout the viewer.

---

## Phase 3 — Panoramas

Objectives:

- 360° images.
- Hotspots.
- Camera movement.
- Scene transitions.

Deliverable:

Interactive panorama scenes.

**Note:** this phase has a real, non-hypothetical predecessor — the Pictureality project
(Three.js + Panolens.js, `config.json`-driven, GitHub-Pages-hosted) already solved panorama
hotspot placement and linking, with hard-won bug fixes on record (X-axis mirroring, raycast
recursion, hover-text cleanup). Phase 3 should treat that as prior art to reconcile with
UISP's `scene.json` format, not a from-scratch problem — see the Pictureality project brief.

---

## Phase 4 — Stereo

Objectives:

- Stereo photographs.
- Stereo panoramas.
- Device detection.

Deliverable:

Optional stereoscopic viewing.

---

## Phase 5 — Multimedia

Objectives:

- Audio.
- Video.
- Narration.
- Documents.
- Maps.
- Timelines.

Deliverable:

Rich multimedia scenes.

**Note:** the viewer's action-button system (`ACTION_HANDLERS` in `index.html`) already
has documented, unimplemented extension points for `playVideo`, `playAudio`, and
`openDocument` — all three already have media types and action names defined in
SCENE_SPEC.md, so this phase should be a small, contained addition (a lightbox/player
UI plus one registry entry each), not a redesign. A photo-gallery concept (multiple
images per object) does **not** yet have a home in SCENE_SPEC.md and needs a deliberate
spec addition before it can be built.

---

## Phase 6 — AI Authoring

Objectives:

- Object detection.
- Automatic annotations.
- Suggested hotspots.
- Metadata generation.
- Scene creation.

Deliverable:

AI-assisted scene authoring.

**Note:** substantially delivered early, during Phase 1 — see `authoring/scene-authoring.html`.
Object detection (YOLOS-tiny / DETR-ResNet-50, swappable) and face detection (BlazeFace,
presence-only, no identity/naming) both run client-side. Remaining Phase 6 scope: upgrading
to open-vocabulary detection (e.g. OWL-ViT) so detection isn't limited to fixed COCO classes —
discussed but not yet built.

---

## Phase 7 — 3D

Objectives:

- glTF models.
- Object interaction.
- Mixed media.

Deliverable:

Hybrid image and 3D scenes.

**Note:** `view3D` already has a reserved (unimplemented) slot in `index.html`'s action
registry, and RESEARCH.md already committed to glTF as the format. Same shape as Phase 5's
video/audio/document additions.

---

## Phase 8 — Immersive Devices

Objectives:

- WebXR.
- VR.
- Mixed Reality.
- Spatial interfaces.

Deliverable:

Fully immersive scene exploration.

**Note:** deliberately not started. `theme-config.js` reserves a `layoutMode` field
(`screenSpace` / `worldSpace`) so this phase won't require redefining the theme schema
when it's tackled, but no VR interaction logic exists yet. Per this document's own
original sequencing and Pictureality's project notes on its admin canvas, VR changes the
entire interaction model (pointer/click vs. controller-ray/gaze) and deserves its own
design pass rather than an incremental bolt-on.

---

## Future

Potential future capabilities include:

- Collaborative editing.
- Live annotations.
- Version control.
- AI tour guides.
- Semantic search.
- Linked scenes.
- Digital twins.
- Educational experiences.
- Museum archives.
- Historical reconstruction.
- Scientific visualization.
- Geographic storytelling.

The architecture should evolve without requiring changes to existing Scene documents.
