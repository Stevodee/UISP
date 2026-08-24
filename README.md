# UISP — Universal Immersive Scene Platform

An open, browser-first format for describing immersive scenes as portable,
renderer-agnostic data. Content (`scene.json`) is strictly separate from
rendering (`index.html`) — see [`docs/PRINCIPLES.md`](docs/PRINCIPLES.md) and
[`docs/VISION.md`](docs/VISION.md) for the full philosophy.

## Quick start

No build step, no install. Clone this repo (or download it), then from inside it:

```
python3 -m http.server 8000
```

Open `http://localhost:8000/index.html`. A local server is required — opening
the file directly (`file://`) is blocked by browsers for security reasons.

## What's in this repo

```
index.html            The viewer. Reads scene.json, renders it, done.
theme.css              Colors, typography, sizes — the presentation layer.
theme-config.js        Icon-per-object-type mapping + reserved config.
scene.json              Example scene: a detective's desk, 22 objects
                          (AI-detected + hand-placed, human-reviewed).
enhanceddesknoire.png   The example scene's photo.

examples/
  deep-zoom/            The same photo and objects, through the Phase 2
                          tiling pipeline instead of a flat image — same
                          scene.json shape, media.src points at a .dzi
                          tile pyramid instead. Self-contained; has its
                          own copy of index.html/theme.css/theme-config.js.

authoring/
  scene-authoring.html  AI-assisted + manual hotspot authoring tool.
                          Runs entirely client-side (object + face detection).

tools/
  make_tiles.py          Server-side deep-zoom tile pyramid generator.
                          Run this once, offline, on a high-res source image.
                          (This is what generated examples/deep-zoom/.)

docs/
  VISION.md              Why this exists.
  PRINCIPLES.md          The rules that outrank any individual feature.
  ROADMAP.md              Phase-by-phase plan and current status.
  SCENE_SPEC.md            The scene.json schema.
  RESEARCH.md              Why UISP builds on existing standards (IIIF, Web
                            Annotation, glTF, WebXR) instead of reinventing them.
```

## Status

**Phase 1 (Intelligent Images)** and **Phase 2 (Deep Zoom)** are complete —
built and validated against real photo content, not just illustrations.
See [`docs/ROADMAP.md`](docs/ROADMAP.md) for the full phase-by-phase breakdown,
including two real bugs that were found and fixed during validation.

The one viewer (`index.html`) handles both a plain image and a tiled deep-zoom
pyramid through the exact same `Scene.*` API — `scene.json` doesn't need to say
which kind it's dealing with.

## Authoring a scene

1. Open `authoring/scene-authoring.html` locally (no server needed for this one).
2. Drop in a photo. Optionally run AI object/face detection for a first pass —
   everything it finds is a *draft*; nothing is included until you review it.
3. Click directly on the image to add or correct points by hand.
4. Export `scene.json`, drop it next to your photo and `index.html`, done.

Already have a `scene.json` for a photo and want to add more objects to it?
Drop the existing `scene.json` back into the authoring tool's "Continue
Editing" panel along with the same photo — it won't overwrite what's there.

## Using deep zoom on a large image

```
python3 tools/make_tiles.py your-high-res-photo.jpg output-folder 256
```

This generates a full tile pyramid (`output-folder/your-high-res-photo.dzi` +
its tile folder), plus downscaled preview versions and a thumbnail. Point
`scene.json`'s `media[0].src` at the generated `.dzi` file instead of a plain
image, and `index.html` will render it as a real zoomable deep-zoom image —
no other change needed.

## Scene format

See [`docs/SCENE_SPEC.md`](docs/SCENE_SPEC.md) for the full schema. In short:
a scene has a `title`, `description`, one or more `media` entries, and a list
of `objects`, each with a stable `id`, a normalized `location` (`x`/`y` between
0 and 1), and optional `description`/`tags`/`actions`.

## What's deliberately not built yet

- **Video / audio / document playback** from the info box — the format and
  action names already exist in `SCENE_SPEC.md`; the actual player UI doesn't.
- **3D object viewing** (glTF) — same situation.
- **Photo galleries** (multiple images per object) — no schema for this yet;
  needs a deliberate spec decision before it's built.
- **Panoramas / VR** — see `docs/ROADMAP.md` Phases 3 and 8. VR in particular
  is intentionally sequenced last since it changes the whole interaction
  model, not just the visuals.

None of these are accidental gaps — see the `ACTION_HANDLERS` comment block
in `index.html` and the `layoutMode` comment in `theme-config.js` for exactly
what's reserved and why.

## Publishing this to GitHub

If this repo doesn't exist on GitHub yet:

```
git init
git add .
git commit -m "Initial commit: UISP Phase 1 + 2"
git branch -M main
git remote add origin https://github.com/stevodee/uisp.git
git push -u origin main
```

Then, in the repo's Settings → Pages, set the source to the `main` branch,
root folder. The live site will be at `https://<your-username>.github.io/<repo-name>/`.
