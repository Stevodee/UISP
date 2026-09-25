# Phase 3 panorama prototype

Confirmed working in a real browser: panorama load, multi-level tile
adapter (thumb/mobile/full zoom-driven LOD), toolbar, shift-click
coordinate copy, and the full marker popup (re-center, copy link, close).

## Known placeholder — fix after Make.com pipeline runs

`scene.json`'s `sources.thumb` and `sources.mobile` are NOT real files
yet — they're the single uploaded original with ImageKit resize params
chained on, faked for testing since the Make.com pipeline hasn't
produced genuine separate tiles yet. Once it has, swap these two URLs
for the real `/panos/960x480/...` and `/panos/1920x960/...` files.
`sources.full` is already the real uploaded original — no change needed
there.

## Not yet built

No panorama-to-panorama linking (ROADMAP.md's "scene transitions" for
Phase 3) — this is a single-panorama prototype with object markers only,
not a tour.
