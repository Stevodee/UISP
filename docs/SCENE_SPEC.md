# SCENE_SPEC.md

# Scene Specification Version 0.1

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

Scene.search(text)

Scene.find(tag)
```

This API should remain stable regardless of the rendering engine.