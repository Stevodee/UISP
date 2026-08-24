"""
Server-side deep zoom pipeline for UISP Phase 2.

Takes one high-resolution source image and produces:
  1. A Deep Zoom (DZI) tile pyramid — the standard OpenSeadragon format,
     conceptually equivalent to the IIIF Image API's region/size model
     (RESEARCH.md's recommendation), without requiring a IIIF server.
  2. A handful of flat downscaled versions (for progressive-enhancement
     fallbacks, previews, or non-JS contexts).
  3. A thumbnail.

This is meant to run once, offline/server-side, when a new high-res
image is added — not something a visitor's browser ever does.

Usage: python3 make_tiles.py <source_image> <output_dir> [tile_size]
"""
import sys, os, math
from PIL import Image

Image.MAX_IMAGE_PIXELS = None  # we trust our own local source images

def make_dzi(src_path, out_dir, tile_size=256, overlap=1, fmt="jpg", quality=85):
    base = os.path.splitext(os.path.basename(src_path))[0]
    img = Image.open(src_path).convert("RGB")
    W, H = img.size
    max_level = math.ceil(math.log2(max(W, H)))
    tiles_dir = os.path.join(out_dir, f"{base}_files")
    os.makedirs(tiles_dir, exist_ok=True)

    level_count = 0
    for level in range(max_level, -1, -1):
        scale = 2 ** (level - max_level)
        lw, lh = max(1, round(W * scale)), max(1, round(H * scale))
        level_img = img.resize((lw, lh), Image.LANCZOS) if (lw, lh) != (W, H) else img
        level_dir = os.path.join(tiles_dir, str(level))
        os.makedirs(level_dir, exist_ok=True)

        cols = math.ceil(lw / tile_size)
        rows = math.ceil(lh / tile_size)
        for row in range(rows):
            for col in range(cols):
                x0 = max(0, col*tile_size - overlap)
                y0 = max(0, row*tile_size - overlap)
                x1 = min(lw, (col+1)*tile_size + overlap)
                y1 = min(lh, (row+1)*tile_size + overlap)
                tile = level_img.crop((x0, y0, x1, y1))
                tile.save(os.path.join(level_dir, f"{col}_{row}.{fmt}"), quality=quality)
        level_count += 1
        if lw <= 1 and lh <= 1:
            break  # reached the 1x1 base level

    dzi_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Image TileSize="{tile_size}" Overlap="{overlap}" Format="{fmt}"
       xmlns="http://schemas.microsoft.com/deepzoom/2008">
  <Size Width="{W}" Height="{H}"/>
</Image>"""
    with open(os.path.join(out_dir, f"{base}.dzi"), "w") as f:
        f.write(dzi_xml)

    return W, H, max_level, base

def make_previews_and_thumb(src_path, out_dir):
    base = os.path.splitext(os.path.basename(src_path))[0]
    img = Image.open(src_path).convert("RGB")
    W, H = img.size
    previews_dir = os.path.join(out_dir, "previews")
    os.makedirs(previews_dir, exist_ok=True)
    sizes = [4000, 2000, 1000, 500]
    for target_w in sizes:
        if target_w >= W:
            continue
        h = round(H * (target_w / W))
        img.resize((target_w, h), Image.LANCZOS).save(
            os.path.join(previews_dir, f"{base}-{target_w}.jpg"), quality=85)
    thumb = img.copy()
    thumb.thumbnail((320, 320), Image.LANCZOS)
    thumb.save(os.path.join(out_dir, f"{base}-thumbnail.jpg"), quality=85)

def dir_size_mb(path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    return total / (1024*1024)

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "chart.jpg"
    out = sys.argv[2] if len(sys.argv) > 2 else "output"
    tile_size = int(sys.argv[3]) if len(sys.argv) > 3 else 256

    os.makedirs(out, exist_ok=True)
    W, H, levels, base = make_dzi(src, out, tile_size=tile_size)
    make_previews_and_thumb(src, out)

    tile_count = sum(len(files) for _, _, files in os.walk(os.path.join(out, f"{base}_files")))
    print(f"Source: {W}x{H}px")
    print(f"Output: {base}.dzi, {base}_files/")
    print(f"Levels: {levels}, tile size: {tile_size}px")
    print(f"Tiles generated: {tile_count}")
    print(f"Total output size: {dir_size_mb(out):.1f} MB")
