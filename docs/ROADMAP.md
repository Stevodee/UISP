# ROADMAP.md

# Universal Immersive Scene Platform Roadmap

## Phase 1 — Intelligent Images

Objectives:

- Display a standard image.
- Load scene.json.
- Display hotspots.
- Click hotspots.
- Zoom and pan.
- HTML controls viewer.

Deliverable:

A browser-based intelligent image.

---

## Phase 2 — Deep Zoom

Objectives:

- Large images.
- Image tiling.
- High-resolution viewing.
- Object persistence.

Deliverable:

Museum-quality zoomable image viewer.

---

## Phase 3 — Panoramas

Objectives:

- 360° images.
- Hotspots.
- Camera movement.
- Scene transitions.

Deliverable:

Interactive panorama scenes.

### Status: in progress

Renderer chosen: Photo Sphere Viewer (see RESEARCH.md Addendum, Section 15,
for the comparison against Panolens.js and A-Frame).

Milestones reached so far:

- `viewer-panorama.html` prototype built and confirmed working in a real
  browser test against a panorama-typed `scene.json`.
- Toolbar and marker-click interaction bugs fixed (overlay z-index, modifier-key
  tracking — see RESEARCH.md Addendum for root causes).
- Multi-resolution tile loading wired in via
  `@photo-sphere-viewer/equirectangular-tiles-adapter`, mapping a three-tier
  hosting scheme (`thumb` 960×480 / `mobile` 1920×960 / `full` 3840×1920) onto
  zoom ranges, with graceful fallback to untiled loading for scenes without
  tiered `sources`.
- `examples/panorama/` (viewer, scene.json, theme.css, theme-config.js —
  mirroring the existing `examples/deep-zoom/` self-contained-folder pattern)
  pushed to `stevodee/uisp`, live at
  `stevodee.github.io/UISP/examples/panorama/viewer-panorama.html`, with
  placeholder thumb/mobile tiers flagged pending a production image pipeline.

Not yet done:

- Production multi-tier image pipeline (Make.com scenario to bake and upload
  `thumb`/`mobile`/`full` tiers) — currently a manual/simulated step.
- Resolving the `wireInteractions()` / `scene.json` loading issue noted in the
  `panorama-proto` debugging notes.

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

---

## Phase 7 — 3D

Objectives:

- glTF models.
- Object interaction.
- Mixed media.

Deliverable:

Hybrid image and 3D scenes.

---

## Phase 8 — Immersive Devices

Objectives:

- WebXR.
- VR.
- Mixed Reality.
- Spatial interfaces.

Deliverable:

Fully immersive scene exploration.

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