# Shared text geometry for compose.py and layout.py.
from PIL import ImageFont
W, H = 1080, 1920
TEXTS = [("LEG CURL|SEDUTO", "2×5-7"), ("CALF|LEG PRESS", "4×6-8"), ("BACK|EXTENSION", "3×6-8"), ("ABDUCTOR", "2×8-10"), ("CRUNCH|MACHINE", "2×8-10")]
MAXW = [700, 740, 1010, 1010, 1010]
ALIGN = ["r", "l", "c", "c", "c"]          # leg curl: athlete centre-left -> text top right; calf: athlete right -> text left

def font(sz, w="900-italic"): return ImageFont.truetype(f"assets/saira-{w}.ttf", sz)

def name_lines(k, y, d):
    """[(line, x, y, font)] for exercise k starting at y, plus the font size"""
    lines = TEXTS[k][0].split("|"); sz = 300
    while max(d.textlength(l, font=font(sz)) for l in lines) > MAXW[k]: sz -= 6
    out = []
    for l in lines:
        f = font(sz); w = d.textlength(l, font=f)
        out.append((l, {"c": (W - w) / 2, "l": 34, "r": W - 34 - w}[ALIGN[k]], y, f)); y += int(sz * 0.86)
    return out, sz

def sets_box(k, sz, d):
    """sets×reps label: font and box size (w, h)"""
    f = font(int(sz * 0.5)); w = d.textlength(TEXTS[k][1], font=f)
    return f, w, int(w + 68), int(sz * 0.5 * 1.18)
