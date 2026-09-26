# SCENE_SPEC.md

# Scene Specification Version 0.3

**Changes from 0.2:** added a Video coordinate system entry, a `goto`
Object Action, a `returnable` link flag, and `Scene.back()` — together
these support a resumable detour: pausing a video at a stop point to
explore another scene (e.g. a panorama), then returning to the video where
it left off. No existing fields changed; this is additive.

**Changes from 0.1:** added the Media References section below — Scene
media entries may now indirect through a descriptor document rather than
embedding delivery details inline. No existing fields changed; this is
additive.

## Purpose

A Scene describes an immersive experience.

It does not define how the experience is rendered.

---

## Scene Structure

```
Scene

├── Metadata
├── Media
├── Objects
├── Tours
├── Audio
├── Documents
├── Links
└── Settings
```

---

## Required Fields

```
title
description
media
objects
```

---

## Media Types

Supported media should include:

- image
- panorama
- video
- 360_video
- stereo_image
- stereo_panorama
- model
- document
- audio

Additional media types may be added in future versions.

---

## Media References

A Scene's `media` field describes *what* is present. It should never encode
*how that media is delivered* — resolution tiers, tile grids, encoding
ladders, LOD variants, and similar delivery mechanics belong outside the
Scene entirely.

This split exists so the representation backing a piece of media can be
regenerated, re-tiered, or swapped for a different delivery strategy
without editing Scene content, and so a pipeline rerun can safely
regenerate delivery data without risk to hand-authored Scene fields (title,
objects, tours, links). It is Principle #6 (Every Object Has Identity —
identity independent of representation) applied one level up, to the media
reference itself, and it keeps Scene data aligned with Principle #4
(Renderer Independence): a descriptor's internal shape is free to be
renderer- or pipeline-specific without that specificity leaking into Scene
content.

### Two valid forms

For simple, lightweight media with no reasonable case for substitution
(Principle #16, Simplicity Before Complexity — indirection should earn its
keep), `media` may be a plain reference:

```json
"media": "photo.jpg"
```

For media where the delivery representation may need to evolve
independently of the Scene — this is expected to be the common case for
panorama, video, 360_video, and model, and optional for image — `media` is
an object pointing at a separate descriptor document:

```json
"media": {
  "type": "panorama",
  "descriptor": "descriptors/gibson-house-foyer.json"
}
```

### The descriptor contract

- **Path stability.** A descriptor's path must stay stable across
  regeneration — same address, swapped contents. A viewer or another Scene
  should never need to change because the pipeline that regenerates a
  descriptor ran again.
- **Ownership.** A descriptor is owned entirely by whatever pipeline
  produces that media type. SCENE_SPEC does not define descriptor payload
  schemas — those are implementation detail per Principle #4, and will
  differ meaningfully by media type. Illustrative shapes, not
  specifications:

  - *panorama* — a tile pyramid: base low-resolution image, one or more
    resolution levels each with their own tile grid, mapped to zoom ranges.
  - *video / 360_video* — an encoding ladder: a manifest (e.g. HLS/DASH) or
    a set of quality renditions.
  - *model* — LOD variants: e.g. a high-poly desktop asset alongside a
    decimated or compressed mobile/headset variant.

- **Lazy loading.** A viewer should be able to load a Scene's structure
  (objects, tours, titles) without resolving every descriptor in it, and
  fetch a given media item's descriptor only once that item is actually
  needed. Descriptor indirection should make Scenes lighter to load, not
  heavier.

---

## Objects

Each object requires:

- id
- label
- type
- location

Optional:

- description
- media
- tags
- links
- actions

---

## Coordinate Systems

The specification supports multiple coordinate systems.

### Image

```
x
y
```

Normalized values (0–1).

---

### Panorama

```
yaw
pitch
```

---

### Video

```
t
```

Seconds from the start of playback. Identifies a stop point on a video or
360_video's timeline — the video-equivalent of a panorama's yaw/pitch or an
image's x/y.

Optional, for 360_video specifically:

```
yaw
pitch
```

A 360 video still has a full sphere of view at any given timestamp, so a
stop point may also specify which direction the viewer should be facing
when playback pauses there.

---

### 3D

```
x
y
z
```

---

## Object Actions

Objects may support:

- zoom
- highlight
- playAudio
- playVideo
- openDocument
- openURL
- startTour
- showAnnotation
- goto

`goto` navigates to another object or Scene, identified via the object's
`links`. A link may carry an optional `returnable: true` flag, signaling
that the current view/playback state (e.g. a video's timestamp and
play/pause state) should be preserved and restorable — see `Scene.back()`
below. Without `returnable`, a `goto` is a one-way transition and no state
is preserved.

---

## Scene API

Every viewer should expose a common API.

```
Scene.load()

Scene.goto(id)

Scene.highlight(id)

Scene.play(id)

Scene.open(id)

Scene.startTour(id)

Scene.back()

Scene.search(text)

Scene.find(tag)
```

This API should remain stable regardless of the rendering engine.

`Scene.back()` returns to the state before the most recent `returnable`
`goto` — restoring the previous object/Scene and, where applicable, its
paused playback position. Non-returnable transitions do not push onto this
history, so `back()` only ever unwinds detours that were explicitly marked
resumable.