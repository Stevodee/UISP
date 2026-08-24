# RESEARCH.md

# Universal Immersive Scene Platform

## Existing Standards and Technologies

### Purpose

UISP should not create new standards where established, interoperable standards already solve the problem.

This document examines existing technologies that overlap with the UISP vision and identifies:

1. What each technology does well.
2. Its limitations relative to UISP.
3. What UISP should reuse.
4. What gap, if any, UISP should address.

The research should be treated as a living document and updated as the project develops.

---

# 1. HTML

## What it provides

HTML is the fundamental delivery and linking system of the Web.

It provides:

- Documents
- Hyperlinks
- Images
- Video
- Audio
- Embedded content
- Forms
- Semantic structure
- Accessibility mechanisms

HTML links are fundamentally resource relationships, allowing a document to link to external resources or locations within the document.

## Advantages

- Universal web foundation
- Extremely broad browser support
- Native hyperlink model
- Native multimedia
- Accessible
- Well documented
- Long-term stability
- Naturally URL based

## Limitations

HTML does not provide a standard representation for:

- Spatial objects inside an image
- Panorama coordinates
- 3D scene relationships
- Object-aware camera navigation
- Immersive tours
- Relationships between equivalent objects in different media representations

## UISP Decision

**Use HTML as the primary delivery environment.**

UISP should complement HTML rather than attempt to replace it.

HTML links should be capable of controlling a UISP viewer.

---

# 2. W3C Web Annotation

## What it provides

The Web Annotation Data Model defines a structured model for associating information with web resources.

It supports annotations on:

- Images
- Documents
- Web pages
- Audio
- Video
- Specific regions
- Temporal segments

It supports selectors including spatial and textual selectors.

The specification is a W3C Recommendation and was specifically designed for annotations that can be shared and reused across platforms.

## Advantages

- W3C Recommendation
- Open standard
- JSON-LD representation
- Designed for interoperability
- Supports spatial regions
- Supports timed media
- Supports arbitrary annotation bodies
- Can reference external resources
- Highly relevant to UISP's hotspot concept

## Limitations

Web Annotation describes relationships and annotations but does not define:

- A complete immersive scene
- Panorama camera navigation
- VR presentation
- Guided tours
- Rendering engines
- Media capability negotiation
- A universal scene container

## UISP Decision

**Adopt Web Annotation wherever appropriate.**

UISP should avoid creating a proprietary annotation model when Web Annotation can represent the requirement.

UISP may add a higher-level scene model that references Web Annotations.

---

# 3. IIIF

## What it provides

IIIF is particularly important to UISP.

The IIIF Image API defines standardized requests for images including:

- Region
- Size
- Rotation
- Quality
- Format

This makes it particularly suitable for very large images and deep zoom.

The IIIF Presentation API defines Manifests and Canvases for presenting compound digital objects. Canvases can be independently addressable and can use Web Annotations to associate content with them.

## Advantages

- Mature open ecosystem
- Strong cultural heritage adoption
- Designed for interoperability
- Excellent deep-zoom architecture
- URL-addressable image regions
- JSON-LD
- Annotation integration
- Can represent sequences and compound objects
- Works with static files as well as dynamic services

## Limitations

IIIF is primarily an image and digital-object interoperability framework.

It does not attempt to provide a universal:

- Panorama format
- Stereo format
- 3D world format
- VR experience
- Immersive tour scripting system
- General-purpose interaction model

## UISP Decision

**Build on IIIF rather than compete with it.**

IIIF should be a major component of UISP's image layer.

For high-resolution images, UISP should preferentially support IIIF.

UISP should investigate whether a UISP Scene can reference an IIIF Manifest directly.

---

# 4. glTF

## What it provides

glTF is an open, runtime-neutral standard for efficient delivery of 3D assets.

It supports:

- Geometry
- Materials
- Textures
- Animation
- Scene hierarchies
- Extensibility

The current specification is glTF 2.0.

## Advantages

- Open standard
- Designed for efficient runtime delivery
- Strong WebGL/WebGPU ecosystem
- Well suited to browsers
- Extensible
- Compact compared with many production formats
- Strong support in modern 3D tools

## Limitations

glTF is primarily an asset delivery format.

It is not a complete publishing system for:

- HTML documents
- Image annotations
- Guided tours
- Cultural metadata
- Web hyperlinks
- General multimedia relationships
- Browser capability negotiation

## UISP Decision

**Reference glTF rather than replace it.**

3D objects inside UISP should normally be represented by glTF assets.

UISP should describe the object's identity, relationships, metadata, and interaction while glTF provides its 3D representation.

---

# 5. OpenUSD

## What it provides

OpenUSD is a powerful scene-description and composition system developed for complex 3D production workflows.

It supports:

- Hierarchical scenes
- Composition
- References
- Layering
- Geometry
- Materials
- Animation
- Large collaborative workflows
- Extensible schemas

It is particularly strong in film, VFX, animation, simulation, and complex 3D production.

## Advantages

- Extremely powerful scene description
- Rich composition system
- Strong hierarchy and relationships
- Extensible
- Designed for large-scale collaborative workflows
- Increasing ecosystem adoption
- Potentially valuable for complex future UISP scenes

## Limitations

OpenUSD is substantially more complex than the lightweight browser-first system envisioned by UISP.

It is primarily designed around professional 3D content creation and production rather than:

- Lightweight web delivery
- Simple 2D images
- HTML embedding
- Browser-native hyperlinks
- Simple annotation workflows
- Small portable scenes

## UISP Decision

**Do not make OpenUSD the core UISP format.**

Investigate OpenUSD as a supported external scene representation.

UISP should be capable of referencing or importing OpenUSD-derived assets without requiring browsers to implement OpenUSD.

---

# 6. WebXR

## What it provides

WebXR provides browser APIs for accessing VR and AR hardware, including:

- Head-mounted displays
- Sensors
- Controllers
- XR sessions
- Spatial tracking

WebXR is currently a W3C Candidate Recommendation Draft.

## Advantages

- Open Web standard
- Browser based
- Designed specifically for XR
- Supports VR and AR
- Provides standardized browser/device interaction

## Limitations

WebXR does not define:

- A scene file format
- A multimedia package
- Image annotations
- Metadata
- Tours
- Publishing
- Object identity
- General scene storage

Browser support is also not universal, which is significant for UISP.

## UISP Decision

**Treat WebXR as progressive enhancement.**

UISP must function without WebXR.

When WebXR is available, it should provide a richer presentation mode for the same underlying Scene.

---

# 7. GeoJSON

## What it provides

GeoJSON is an IETF-standard JSON format for geographic features and their spatial extents.

It supports:

- Points
- Lines
- Polygons
- Multi-geometries
- Properties
- Geographic coordinates

## Advantages

- Open Internet standard
- JSON based
- Simple
- Widely supported
- Useful for geographic objects
- Appropriate for maps and location metadata

## Limitations

GeoJSON assumes geographic coordinates.

It does not describe:

- Image coordinates
- Panorama coordinates
- 3D object coordinates
- Media relationships
- Tours
- Multimedia behavior

## UISP Decision

**Support GeoJSON as an optional geographic representation.**

Do not use GeoJSON as the universal coordinate model.

---

# 8. IPTC / XMP Metadata

## What it provides

IPTC Photo Metadata and XMP provide established mechanisms for describing photographic resources.

Metadata can include:

- Creator
- Copyright
- Location
- Dates
- People
- Products
- Artwork
- Rights
- Identifiers
- AI-related information

IPTC's current specification also includes properties concerning AI systems and prompts.

## Advantages

- Mature photography ecosystem
- Widely used
- Strong rights-management capabilities
- Useful for provenance
- Can be embedded or stored externally
- Relevant to AI-generated and AI-assisted media

## Limitations

Metadata systems do not provide:

- Interactive hotspots
- Scene navigation
- Spatial interactions
- Tours
- Rendering
- Multimedia relationships

## UISP Decision

**Reuse IPTC/XMP for media metadata where appropriate.**

UISP should not attempt to replace established photographic metadata systems.

---

# 9. HTML Media APIs

HTML already provides widely supported mechanisms for:

- Audio
- Video
- Playback
- Seeking
- Captions
- Controls

These capabilities are broadly available across browsers.

## UISP Decision

Use native HTML media capabilities whenever possible.

UISP should attach media to scene objects rather than inventing a new media playback system.

---

# 10. Web Components

Web Components provide browser technologies for creating reusable custom elements.

This presents an interesting potential delivery mechanism.

A future UISP implementation could expose something conceptually similar to:

```html
<immersive-scene src="scene.json"></immersive-scene>
```

## Advantages

- Native Web platform technology
- Reusable
- Encapsulated
- Easy to embed
- Does not require a new browser feature

## Limitations

Web Components are an implementation mechanism, not a scene-data standard.

## UISP Decision

Investigate Web Components for the reference viewer and embedding system.

Do not make Web Components part of the underlying scene specification.

---

# 11. Overall Findings

The research demonstrates that UISP should not attempt to create replacements for existing standards.

Instead, UISP should operate as an orchestration layer.

Conceptually:

```text
                         UISP SCENE
                              |
        +---------------------+---------------------+
        |                     |                     |
     Metadata             Annotations            Media
        |                     |                     |
    IPTC/XMP             W3C Web Annotation       HTML
                                                   IIIF
                                                   glTF
                                                   Video
                                                   Audio
                                                   Images
                              |
                         Experience
                              |
                 Tours / Navigation / Actions
                              |
                           Renderer
                              |
               +--------------+--------------+
               |              |              |
             2D/HTML       Panorama        WebXR
```

The purpose of UISP is therefore not to replace these technologies.

It is to define how they can be combined into a coherent, addressable, browser-based visual experience.

---

# 12. The Potential UISP Gap

The research identifies a potential gap between existing standards.

Existing technologies independently solve important parts of the problem:

- HTML provides documents and links.
- IIIF provides interoperable image delivery and presentation.
- Web Annotation provides annotations and spatial relationships.
- IPTC/XMP provides photographic metadata.
- GeoJSON provides geographic structures.
- glTF provides efficient 3D asset delivery.
- OpenUSD provides sophisticated 3D scene composition.
- WebXR provides immersive device access.

What is not provided by any single one of these systems is a lightweight, browser-first **experience layer** that can associate these representations with stable object identities, navigation actions, tours, and progressive presentation modes.

This is the area UISP should investigate.

---

# 13. Critical Architectural Principle

UISP should be a **thin orchestration layer**, not a replacement for the Web.

The specification should contain only information necessary to connect and describe the experience.

Whenever possible:

```text
UISP
  |
  +-- references IIIF
  +-- references Web Annotation
  +-- references IPTC/XMP
  +-- references GeoJSON
  +-- references glTF
  +-- references HTML
  +-- optionally activates WebXR
```

rather than:

```text
UISP
  |
  +-- replaces everything
```

This approach reduces duplication, increases interoperability, and makes adoption more realistic.

---

# 14. Research Conclusion

The existing standards make the UISP concept more feasible, not less.

The project should not claim to have invented a universal replacement for existing media standards.

Instead, its potential contribution is to define an open, lightweight way of connecting existing standards into a unified visual experience.

The central research question is therefore no longer:

"Can we invent a universal immersive media format?"

It is:

"Can we define an interoperable scene and experience layer that allows existing visual-media standards to behave as one addressable, navigable, browser-based document?"

That is the question the prototype should attempt to answer.