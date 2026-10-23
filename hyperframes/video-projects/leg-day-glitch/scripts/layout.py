# Picks, per exercise, where the big name and the sets×reps label sit, from the athlete matte (assets/alpha.mkv):
#  · name: the height (glyphs below SAFE_TOP, clear of the platform top bar) where the athlete covers ~8 % of the letters on average,
#    so the text reads clearly yet visibly sits BEHIND him; big occlusion spikes (90th pct > 20 %) are penalised
#  · sets label: the spot right above/below the name (flush left / centre / flush right) the athlete crosses least
# writes assets/layout.json
import json, subprocess, numpy as np
from PIL import Image, ImageDraw
from geom import W, H, TEXTS, ALIGN, name_lines, sets_box
CUTS = [0.0, 12.0667, 20.6, 30.7333, 40.6333]; DUR = 50.1333; TEXT_IN = 0.62; S = 4
SAFE_TOP = 200                                   # keep clear of the TikTok / Reels top bar
p = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", "assets/alpha.mkv", "-vf", f"scale={W // S}:{H // S}", "-f", "rawvideo", "-pix_fmt", "gray", "-"], stdout=subprocess.PIPE)
fr = []
while len(b := p.stdout.read(W // S * H // S)) == W // S * H // S: fr.append(np.frombuffer(b, np.uint8).reshape(H // S, W // S))
fr = np.array(fr, np.float32) / 255
ends = CUTS[1:] + [DUR]

def occ(seq, m, y4):
    o = (seq[:, y4:y4 + m.shape[0], :] * m).sum((1, 2)) / m.sum()
    return o.mean(), np.percentile(o, 90)

out = {"name_y": [], "sets": []}
for k in range(5):
    seq = fr[int((CUTS[k] + TEXT_IN) * 30):int(ends[k] * 30):2]
    img = Image.new("L", (W, H), 0); d = ImageDraw.Draw(img)
    lines, sz = name_lines(k, 0, d)
    for l, x, y, f in lines: d.text((x, y), l, font=f, fill=255)
    m = np.asarray(img.resize((W // S, H // S))).astype(np.float32) / 255
    rows = np.nonzero(m.sum(1))[0]; top, bot = rows.min(), rows.max() + 1; m = m[top:bot]
    cols = np.nonzero(m.sum(0))[0]; nl, nr = cols.min() * S, (cols.max() + 1) * S       # name's left / right edge
    _, _, bw, bh = sets_box(k, sz, d)
    def label(ny):
        """best sets-label spot for a name at ny: (score, x, y, tag, mean occlusion)"""
        gtop, gbot = ny + top * S, ny + bot * S                              # glyph extent of the name block
        cands = []
        for where, by in (("below", gbot + 26), ("above", gtop - 26 - bh)):
            if by < SAFE_TOP or by + bh > 1500: continue
            for xa, bx in (("c", (W - bw) // 2), ("l", nl + 6), ("r", nr - 6 - bw)):     # flush with the name's edge
                if ALIGN[k] != "c" and xa != ALIGN[k]: continue
                o = seq[:, by // S:(by + bh) // S, bx // S:(bx + bw) // S].mean((1, 2))
                cands.append((o.mean() + 0.5 * np.percentile(o, 90), bx, by, where + "-" + xa, o.mean()))
        return min(cands)
    best = None
    for y in range(100, 901, 10):                                            # name + label chosen together
        if y + top * S < SAFE_TOP: continue
        mo, p9 = occ(seq, m, (y // S) + top); lb = label(y)
        sc = abs(mo - 0.08) + 0.5 * max(0.0, p9 - 0.2) + lb[0]
        if best is None or sc < best[0]: best = (sc, y, mo, p9, lb)
    _, ny, mo, p9, (_, bx, by, tag, bo) = best
    out["name_y"].append(ny); out["sets"].append([int(bx), int(by)])
    print(f"{TEXTS[k][0]:16s} y={ny:4d} occl mean {mo:.2f} p90 {p9:.2f} | sets {tag} at ({bx},{by}) occl {bo:.3f}")
json.dump(out, open("assets/layout.json", "w"))
