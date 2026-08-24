# PRINCIPLES.md

# Universal Immersive Scene Platform (UISP)

## Guiding Principles

This document defines the fundamental principles of the Universal Immersive Scene Platform (UISP). These principles are intended to remain stable over the lifetime of the project and should guide all architectural, technical, and design decisions.

If a proposed feature conflicts with these principles, the principles take precedence.

---

# 1. Browser First

UISP is a web platform.

Every scene should function in a standard web browser without requiring proprietary software, plugins, or dedicated applications.

Advanced hardware should enhance the experience, not define it.

---

# 2. Progressive Enhancement

Every scene should provide the best possible experience for the user's device.

Examples:

- Basic browser → image, text, hotspots
- Mobile device → touch, motion sensors
- Desktop → advanced graphics
- VR headset → immersive viewing
- Future devices → automatic enhancement

No device should be excluded simply because it lacks advanced capabilities.

---

# 3. Open Standards Before Custom Standards

Whenever an established open standard already solves a problem, UISP should use it rather than invent a new solution.

Examples include:

- HTML
- CSS
- JavaScript
- JSON
- W3C Web Annotation
- glTF
- IIIF
- WebXR
- SVG

Custom specifications should exist only where no suitable standard is available.

---

# 4. Renderer Independence

Scenes should never depend on a specific rendering engine.

Whether a scene is displayed using Panolens.js, Three.js, A-Frame, Babylon.js, or a future engine should not affect the scene itself.

The renderer is an implementation detail.

The scene is the product.

---

# 5. Content Over Technology

The purpose of UISP is to communicate information, stories, education, history, science, art, and experiences.

Technology exists only to support the content.

Features should be added because they improve understanding, not because they demonstrate technical capability.

---

# 6. Every Object Has Identity

Every meaningful object within a scene should possess a stable, unique identifier.

An object's identity should remain consistent regardless of whether it appears in:

- a photograph
- a panorama
- a video
- a 3D model
- a historical reconstruction

Identity is independent of representation.

---

# 7. Scenes Are Data

A scene is a structured description of an experience.

It should remain portable, editable, searchable, and understandable by both humans and software.

Scene descriptions should never be locked inside proprietary binary formats.

---

# 8. AI Assists, Humans Decide

Artificial intelligence should accelerate scene creation by suggesting:

- objects
- annotations
- metadata
- tours
- descriptions

Final editorial control belongs to the creator.

AI is an assistant, not the author.

---

# 9. Accessibility Is Fundamental

Immersive experiences should be available to the widest possible audience.

Where practical, scenes should support:

- captions
- transcripts
- screen readers
- keyboard navigation
- high contrast
- scalable interfaces
- alternative descriptions

Accessibility is part of the design process, not an afterthought.

---

# 10. Every Scene Has a URL

Every scene should be directly shareable.

Every object within a scene should also be individually addressable whenever practical.

Users should be able to reference:

- an entire scene
- a specific object
- a viewpoint
- a tour
- a moment in time

using standard web links.

---

# 11. Modularity

Every subsystem should be replaceable.

Media formats, renderers, AI engines, storage systems, and user interfaces should evolve independently without requiring redesign of the overall architecture.

---

# 12. Longevity

Scenes should remain usable for decades.

The platform should prioritize:

- readable formats
- documented specifications
- backwards compatibility
- migration paths
- stable identifiers

Historical preservation is a design objective.

---

# 13. Extensibility

New media types should be incorporated without changing existing scene definitions.

The architecture should anticipate future technologies rather than limiting them.

---

# 14. Human-Centered Navigation

Navigation should feel natural.

Users should explore visual information intuitively through:

- movement
- zoom
- focus
- context
- storytelling

The interface should disappear behind the experience.

---

# 15. One Scene, Many Experiences

The same scene should support multiple modes of exploration.

Examples include:

- casual browsing
- guided tours
- education
- accessibility mode
- research
- virtual reality
- mobile viewing

Different experiences should be derived from the same underlying scene data.

---

# 16. Simplicity Before Complexity

Every feature should justify its existence.

Whenever two approaches provide similar value, the simpler solution should be preferred.

Complexity should emerge only when necessary.

---

# 17. Community and Interoperability

UISP should encourage collaboration and interoperability.

The platform should make it easy for creators, educators, museums, researchers, developers, and organizations to exchange content without unnecessary barriers.

---

# Mission Statement

The Universal Immersive Scene Platform exists to create an open, extensible, browser-based standard for immersive visual experiences that remain accessible, portable, and meaningful across technologies, devices, and generations.

The platform values openness over lock-in, standards over reinvention, content over technology, and people over software.