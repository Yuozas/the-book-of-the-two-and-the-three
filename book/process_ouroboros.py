# -*- coding: utf-8 -*-
"""
Transform the public-domain 1478 ouroboros (Theodoros Pelecanos, Wikimedia
Commons, PD-Art) into a book plate:
  - radial vignette to transparency, dissolving the manuscript margins/corner
    text into the page so the serpent ring floats on the paper;
  - a gentle, luminance-weighted tone of the parchment toward the page cream,
    so the relic sits on #f4eee2 without a foreign rectangle.
This is a derivative work of a public-domain original.

    python3 book/process_ouroboros.py
"""
import math, pathlib
from PIL import Image, ImageEnhance

HERE = pathlib.Path(__file__).resolve().parent
src = Image.open(HERE / "assets" / "ouroboros.jpg").convert("RGB")
# lift the faded manuscript a touch so the serpent reads with more life
src = ImageEnhance.Color(src).enhance(1.20)
src = ImageEnhance.Contrast(src).enhance(1.12)
w, h = src.size
spx = src.load()

cream = (244, 238, 226)          # the page colour, #f4eee2
cx, cy = w / 2.0, h / 2.0
R_full = 0.455 * w               # fully opaque within (keeps the serpent ring)
R_zero = 0.512 * w               # fully transparent beyond (drops the margin text)

out = Image.new("RGBA", (w, h))
opx = out.load()
for y in range(h):
    for x in range(w):
        r, g, b = spx[x, y]
        # luminance-weighted nudge of light (parchment) pixels toward cream;
        # dark ink and saturated serpent are left almost untouched.
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        t = max(0.0, min(1.0, (lum - 120) / 135.0)) * 0.52
        r = int(r + (cream[0] - r) * t)
        g = int(g + (cream[1] - g) * t)
        b = int(b + (cream[2] - b) * t)
        # radial alpha (smoothstep for a soft edge)
        d = math.hypot(x - cx, y - cy)
        if d <= R_full:
            a = 255
        elif d >= R_zero:
            a = 0
        else:
            u = (d - R_full) / (R_zero - R_full)
            a = int(255 * (1 - (u * u * (3 - 2 * u))))   # smoothstep
        opx[x, y] = (r, g, b, a)

out.save(HERE / "assets" / "ouroboros_plate.png")
print("wrote assets/ouroboros_plate.png", out.size)
