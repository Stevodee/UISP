/* ============================================================
   UISP THEME CONFIG
   ============================================================
   The non-CSS half of theming: things that need actual logic
   or content, not just style rules. Loaded before the main
   viewer script; viewer.html reads window.UISP_THEME if present
   and falls back to sane defaults if it's missing entirely —
   this file is optional, not a hard dependency.
   ============================================================ */
window.UISP_THEME = {

  // Optional glyph shown inside a pin, keyed by the object's `type`
  // field. Falls back to the catalog number (01, 02, ...) if the
  // type isn't listed here or no icons block is provided at all.
  icons: {
    "instrument": "◆",
    "document":   "▤",
    "timepiece":  "◷",
    "book":       "▥",
    "lighting":   "✺",
    "botanical":  "❧",
    "face":       "☻",
    "vessel":     "⛵",
    "structure":  "⌂",
    "illustration": "✦"
  },

  // -----------------------------------------------------------
  // NOT YET IMPLEMENTED — reserved for Phase 8 (Immersive Devices).
  // Documented now so the schema doesn't need to change later,
  // per Principle 13 (Extensibility): new capability shouldn't
  // require redefining what already exists.
  //
  // 'screenSpace' (current, only supported mode): pins are DOM
  //   overlays positioned in 2D screen coordinates, sized in px,
  //   always facing the viewer — correct for desktop/phone.
  //
  // 'worldSpace' (reserved): would mean pins/annotations are
  //   positioned as real 3D objects with orientation and depth,
  //   for panorama/VR contexts where "up" and "facing the camera"
  //   aren't fixed. Deliberately not built yet — Pictureality's
  //   own project notes flag this exact tension (pointer/click vs.
  //   controller-ray/gaze input) as needing its own design pass,
  //   not a bolt-on.
  // -----------------------------------------------------------
  layoutMode: "screenSpace"

};
