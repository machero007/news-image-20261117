#!/usr/bin/env python3
"""Build the 17 Nov 2026 world-news summary image (1024x1024 PNG).

Editorial poster: date header, 2x2 panels of the day's biggest stories
(each a simple drawn scene + headline), footer ticker of secondary stories.
Deterministic output: same bytes every run.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news.png")

NAVY = (13, 27, 46)
PANEL = (22, 40, 63)
PANEL2 = (18, 34, 54)
WHITE = (245, 245, 240)
GOLD = (212, 175, 55)
MUTE = (170, 185, 200)
RED = (198, 60, 48)
ORANGE = (224, 122, 42)
TEAL = (46, 160, 140)
BLUE = (70, 130, 200)
SKY = (38, 68, 102)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)

# ---------- header ----------
d.text((24, 26), "THE WORLD  •  TUESDAY", font=font(FB, 26), fill=GOLD)
d.text((24, 56), "17 NOVEMBER 2026", font=font(FB, 72), fill=WHITE)
d.text((24, 138), "One day, one image — the news that mattered most.",
       font=font(FR, 26), fill=MUTE)
d.line([(24, 172), (1000, 172)], fill=GOLD, width=3)

# ---------- panels ----------
PX, PY, PW, PH, GAP = 24, 188, 488, 322, 16


def panel(x, y, accent):
    d.rounded_rectangle([x, y, x + PW, y + PH], radius=14, fill=PANEL)
    d.rounded_rectangle([x, y, x + PW, y + 10], radius=5, fill=accent)
    d.rounded_rectangle([x, y + 5, x + PW, y + 10], fill=accent)


def caption(x, y, headline, sub, accent):
    f_h, f_s = font(FB, 29), font(FR, 22)
    lines = wrap(d, headline, f_h, PW - 32)
    cy = y + PH - 118
    for ln in lines[:2]:
        d.text((x + 16, cy), ln, font=f_h, fill=WHITE)
        cy += 34
    d.text((x + 16, y + PH - 44), sub, font=f_s, fill=MUTE)


def burst(cx, cy, r, color):
    import math
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=color)


# Panel 1 — Bahrain drone attack (top-left)
x, y = PX, PY
panel(x, y, RED)
d.rectangle([x, y + 10, x + PW, y + 196], fill=SKY)
d.line([(x, y + 196), (x + PW, y + 196)], fill=(90, 110, 130), width=3)
# ground / base
d.rectangle([x, y + 196, x + PW, y + 206], fill=(60, 70, 60))
d.rectangle([x + 40, y + 150, x + 130, y + 196], fill=(120, 125, 110))  # hangar
d.polygon([(x + 40, y + 150), (x + 85, y + 120), (x + 130, y + 150)], fill=(90, 95, 85))
# radar dish
d.ellipse([x + 330, y + 130, x + 420, y + 196], outline=WHITE, width=4)
d.line([(x + 375, y + 163), (x + 420, y + 110)], fill=WHITE, width=4)
d.line([(x + 375, y + 196), (x + 375, y + 163)], fill=WHITE, width=4)
# drone
dx, dy = x + 210, y + 80
d.ellipse([dx - 34, dy - 10, dx + 34, dy + 10], fill=(30, 30, 30))
d.ellipse([dx - 8, dy - 4, dx + 8, dy + 4], fill=RED)
d.line([(dx - 44, dy - 16), (dx - 20, dy - 8)], fill=WHITE, width=3)
d.line([(dx + 20, dy - 8), (dx + 44, dy - 16)], fill=WHITE, width=3)
d.line([(dx - 44, dy + 16), (dx - 20, dy + 8)], fill=WHITE, width=3)
d.line([(dx + 20, dy + 8), (dx + 44, dy + 16)], fill=WHITE, width=3)
d.text((x + 16, y + 24), "✕ INTERCEPTED", font=font(FB, 24), fill=(255, 120, 100))
caption(x, y, "IRAN DRONES TARGET US BASE IN BAHRAIN",
        "Bahrain air defences stop the attack", RED)

# Panel 2 — Crimea bridge (top-right)
x, y = PX + PW + GAP, PY
panel(x, y, ORANGE)
d.rectangle([x, y + 10, x + PW, y + 196], fill=(52, 74, 96))
d.rectangle([x, y + 160, x + PW, y + 196], fill=(28, 52, 74))  # water
# bridge
d.rectangle([x + 30, y + 60, x + 44, y + 160], fill=(150, 150, 150))
d.rectangle([x + 300, y + 60, x + 314, y + 160], fill=(150, 150, 150))
d.rectangle([x + 20, y + 130, x + PW - 20, y + 142], fill=(190, 190, 190))
d.line([(x + 37, y + 60), (x + 170, y + 130)], fill=(200, 200, 200), width=2)
d.line([(x + 307, y + 60), (x + 180, y + 130)], fill=(200, 200, 200), width=2)
burst(x + 175, y + 105, 46, (255, 200, 60))
burst(x + 175, y + 105, 26, (255, 120, 40))
d.ellipse([x + 200, y + 60, x + 250, y + 95], fill=(120, 120, 120))
d.ellipse([x + 230, y + 45, x + 270, y + 75], fill=(140, 140, 140))
caption(x, y, "UKRAINE HITS CRIMEA BRIDGE",
        "Russia strikes Kyiv bridges in reply", ORANGE)

# Panel 3 — Gaza aid (bottom-left)
x, y = PX, PY + PH + GAP
panel(x, y, TEAL)
d.rectangle([x, y + 10, x + PW, y + 196], fill=(44, 66, 58))
d.rectangle([x, y + 168, x + PW, y + 196], fill=(96, 84, 60))  # ground
# tents
for tx, tc in [(40, (220, 210, 180)), (130, (200, 190, 160))]:
    d.polygon([(x + tx, y + 110), (x + tx + 55, y + 168), (x + tx + 110, y + 168)],
              fill=tc)
    d.polygon([(x + tx, y + 110), (x + tx + 55, y + 168), (x + tx + 110, y + 168)],
              outline=(60, 55, 40), width=2)
# aid truck
d.rectangle([x + 250, y + 95, x + 400, y + 165], fill=(230, 230, 220))
d.rectangle([x + 400, y + 115, x + 445, y + 165], fill=TEAL)
d.rectangle([x + 410, y + 122, x + 438, y + 140], fill=(200, 230, 240))
d.ellipse([x + 275, y + 160, x + 305, y + 190], fill=(25, 25, 25))
d.ellipse([x + 405, y + 160, x + 435, y + 190], fill=(25, 25, 25))
d.text((x + 268, y + 118), "AID", font=font(FB, 34), fill=TEAL)
d.rectangle([x + 250, y + 95, x + 400, y + 165], outline=(180, 180, 170), width=2)
caption(x, y, "GAZA: WEST URGES OPEN CROSSINGS",
        "1.7m displaced as winter closes in", TEAL)

# Panel 4 — Trump-Xi-Putin summit (bottom-right)
x, y = PX + PW + GAP, PY + PH + GAP
panel(x, y, BLUE)
d.rectangle([x, y + 10, x + PW, y + 196], fill=(36, 56, 88))
d.rectangle([x, y + 168, x + PW, y + 196], fill=(52, 44, 34))  # stage floor
# three flags on poles
def flag(fx, kind):
    d.line([(fx, y + 40), (fx, y + 168)], fill=(200, 200, 200), width=4)
    if kind == "us":
        for i in range(7):
            d.rectangle([fx, y + 42 + i * 9, fx + 104, y + 42 + (i + 1) * 9],
                        fill=(178, 34, 52) if i % 2 == 0 else WHITE)
        d.rectangle([fx, y + 42, fx + 46, y + 42 + 36], fill=(30, 60, 120))
        for sx in range(3):
            for sy in range(2):
                d.ellipse([fx + 8 + sx * 14, y + 48 + sy * 14,
                           fx + 14 + sx * 14, y + 54 + sy * 14], fill=WHITE)
    elif kind == "cn":
        d.rectangle([fx, y + 42, fx + 104, y + 105], fill=(222, 41, 16))
        d.ellipse([fx + 10, y + 50, fx + 30, y + 70], fill=(255, 222, 0))
        for sx, sy in [(44, 48), (58, 58), (58, 74), (44, 82)]:
            d.ellipse([fx + sx, y + sy, fx + sx + 8, y + sy + 8], fill=(255, 222, 0))
    else:  # ru
        d.rectangle([fx, y + 42, fx + 104, y + 63], fill=WHITE)
        d.rectangle([fx, y + 63, fx + 104, y + 84], fill=(0, 57, 166))
        d.rectangle([fx, y + 84, fx + 104, y + 105], fill=(213, 0, 0))


flag(x + 40, "us")
flag(x + 192, "cn")
flag(x + 344, "ru")
caption(x, y, "TRUMP · XI · PUTIN TO MEET",
        "Trilateral summit — Shenzhen, 19 Nov", BLUE)

# ---------- footer ticker ----------
d.line([(24, 852), (1000, 852)], fill=GOLD, width=2)
f_f = font(FR, 24)
ticker = ("ALSO:  Quad leaders meet in Manila  •  Japan scrambles jets after "
          "airspace breach  •  COP31 enters decisive phase  •  "
          "Mongolia's president resigns  •  US loses measles-free status")
for i, ln in enumerate(wrap(d, ticker, f_f, 976)):
    d.text((24, 872 + i * 32), ln, font=f_f, fill=MUTE)
d.text((24, 972), "Sources: Reuters / AP / BBC — 17 Nov 2026",
       font=font(FR, 20), fill=(120, 135, 150))

img.save(OUT, "PNG", optimize=True)
print("saved", OUT, os.path.getsize(OUT), "bytes", img.size)
