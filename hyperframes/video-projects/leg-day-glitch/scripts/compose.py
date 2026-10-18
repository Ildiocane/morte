# Leg-day glitch edit — frame compositor (numpy/PIL).
#  · original audio dropped; music = the reference TikTok sound looped on beats (scripts/music.py) + shutter SFX
#  · each sequence opens with a 3-shot photo burst (freeze + flash + shutter + frozen "clone" cut-outs, like the reference)
#  · then the exercise text glitches in, huge, BEHIND the athlete (RVM alpha matte = green-screen effect), and stays;
#    a faint outline of the hidden letters shows through him, the sets×reps label sits on a spot he never crosses
#  · extra glitch hits on music bars and on every cut; light cinematic grade, vignette and grain
# usage: /root/cbx/bin/python scripts/compose.py [--preview t1,t2,...]
import sys, subprocess, json, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
SRC, ALPHA = "assets/src.mp4", "assets/alpha.mkv"
CUTS = [0.0, 12.0667, 20.6, 30.7333, 40.6333]
DUR = 50.1333
NF = int(round(DUR * FPS))
sys.path.insert(0, "scripts")
from geom import TEXTS, name_lines, sets_box
LAYOUT = json.load(open("assets/layout.json"))     # name heights + sets-label spots, picked from the matte by scripts/layout.py
SNAPS = [0.0, 0.2, 0.4]          # photo burst offsets from each sequence start
FREEZE = 4                        # frames each snap holds
TEXT_IN = 0.62                    # text glitch-in offset
BEATS = json.load(open("assets/beats.json"))

# ---------- text layers (RGBA float, full frame) ----------
def text_layer(k):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    lines, sz = name_lines(k, LAYOUT["name_y"][k], d)
    for l, x, y, f in lines: d.text((x, y), l, font=f, fill=(255, 255, 255, 240))
    solid = np.asarray(img).astype(np.float32) / 255
    # sets × reps: white on a red block, on a spot the athlete (almost) never crosses
    st = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d3 = ImageDraw.Draw(st); fs, w, bw, bh = sets_box(k, sz, d3)
    bx, by = LAYOUT["sets"][k]
    d3.rounded_rectangle((bx, by, bx + bw, by + bh), radius=18, fill=(225, 36, 30, 235))
    d3.text((bx + 34, by + int(sz * 0.5 * 0.02)), TEXTS[k][1], font=fs, fill=(255, 255, 255, 255))
    sets_l = np.asarray(st).astype(np.float32) / 255
    # outline-only copy: "snapshot" echoes, and the faint x-ray outline drawn over the athlete
    ol = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d2 = ImageDraw.Draw(ol)
    for l, x, y, f in lines: d2.text((x, y), l, font=f, fill=(0, 0, 0, 0), stroke_width=4, stroke_fill=(255, 255, 255, 200))
    return solid, np.asarray(ol).astype(np.float32) / 255, sets_l

TL = [text_layer(k) for k in range(5)]

# ---------- helpers ----------
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
r2 = ((xx - W / 2) / (W / 2)) ** 2 * 0.8 + ((yy - H / 2) / (H / 2)) ** 2
VIG = (1 - 0.42 * np.clip(r2, 0, 1.6) ** 1.3)[..., None].clip(0.35, 1)

def grade(f):
    l = f.mean(axis=2, keepdims=True)
    f = f + (1 - l) ** 2 * np.array([-0.035, 0.012, 0.03], np.float32)        # teal shadows
    f = f + l ** 2 * np.array([0.02, 0.008, -0.015], np.float32)              # warm highlights
    f = (f - 0.5) * 1.1 + 0.5
    l = f.mean(axis=2, keepdims=True); f = l + (f - l) * 0.86
    return f * VIG

def shift(a, dx, dy=0): return np.roll(np.roll(a, dx, axis=1), dy, axis=0)

def slices(a, rng, n, amp):
    out = a.copy()
    for _ in range(n):
        y0 = int(rng.integers(0, H - 40)); h = int(rng.integers(12, 120)); dx = int(rng.integers(-amp, amp + 1))
        out[y0:y0 + h] = np.roll(a[y0:y0 + h], dx, axis=1)
    return out

def glitch_frame(f, rng, amt):
    """full-frame RGB split + band displacement"""
    dx = int(6 + 22 * amt)
    g = f.copy(); g[..., 0] = shift(f[..., 0], dx); g[..., 2] = shift(f[..., 2], -dx)
    g = slices(g, rng, int(3 + 8 * amt), int(30 + 90 * amt))
    lines = (np.sin(yy[..., None] * 0.9) * 0.5 + 0.5) * 0.06 * amt
    return np.clip(g - lines, 0, 1)

def put_text(bg, solid, rng, state):
    """composite the text layer with optional glitch (RGB-split alpha per channel, sliced, flicker)"""
    a = solid[..., 3:4] * state["opacity"]
    col = solid[..., :3]
    if state["glitch"] > 0:
        g = state["glitch"]; dx = int(4 + 40 * g)
        aR, aB = shift(a, dx), shift(a, -dx)
        cR, cB = shift(col, dx), shift(col, -dx)
        A = np.concatenate([aR, a, aB], axis=2); C = np.concatenate([cR[..., 0:1], col[..., 1:2], cB[..., 2:3]], axis=2)
        both = slices(np.concatenate([C, A], axis=2), rng, int(2 + 10 * g), int(20 + 140 * g))
        C, A = both[..., :3], both[..., 3:]
    else:
        A, C = np.repeat(a, 3, axis=2), col
    mix = C * state.get("solid", 0.82) + bg * (1 - state.get("solid", 0.82))   # let the image breathe through the letters
    return bg * (1 - A) + mix * A

# ---------- timeline ----------
def seq_of(t):
    k = 0
    for i, c in enumerate(CUTS):
        if t >= c - 1e-6: k = i
    return k
bars = [b for i, b in enumerate(BEATS) if i % 4 == 0]

def plan(fi):
    t = fi / FPS; k = seq_of(t); s = CUTS[k]; e = CUTS[k + 1] if k + 1 < len(CUTS) else DUR; u = t - s
    P = {"k": k, "u": u, "freeze": None, "flash": 0.0, "clones": [], "text": None, "fglitch": 0.0}
    for j, off in enumerate(SNAPS):
        f0 = int(round((s + off) * FPS))
        if f0 <= fi < f0 + FREEZE: P["freeze"] = f0
        fl = (0.8, 0.4, 0.12) if j == 0 else (0.16, 0.06, 0.0)              # one real flash per burst (stays under 3 flashes/s)
        if f0 <= fi < f0 + 3: P["flash"] = fl[fi - f0]
        if fi >= f0 + FREEZE and u < 1.05: P["clones"].append(f0)          # frozen cut-outs stay on screen
    if k > 0 and -0.001 <= u < 3 / FPS: P["fglitch"] = 1.0 - u * FPS / 3      # glitch on the cut itself
    if u >= TEXT_IN and t < e - 0.12:
        g = 0.0; op = 1.0; v = u - TEXT_IN
        if v < 0.45:                                                         # glitch-in with flicker
            g = 1.0 - v / 0.45; op = [0.0, 1.0, 0.3, 1.0, 0.6, 1.0, 1.0, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0][min(13, int(v * FPS))]
        for b in bars:                                                       # micro-glitch on every bar
            if 0 <= t - b < 2.5 / FPS and v > 0.6: g = max(g, 0.45)
        if e - t < 0.3: g = max(g, (0.3 - (e - t)) / 0.3); op = 1.0 if int(t * FPS) % 2 else 0.6
        P["text"] = {"opacity": op, "glitch": g, "echo": max(0.0, 1 - v / 0.55)}
    for b in bars[::2]:                                                      # light full-frame hit every 2 bars
        if 0 <= t - b < 2 / FPS and u > 1.2: P["fglitch"] = max(P["fglitch"], 0.35)
    return P

from scipy import ndimage
def clean_alpha(al):
    """keep only the athlete: drop matte blobs much smaller than the largest connected region (e.g. a wall lamp)"""
    a = al[..., 0]; lab, n = ndimage.label(a > 96)
    if n <= 1: return al
    sizes = ndimage.sum(np.ones_like(a), lab, range(1, n + 1)); keep = np.zeros(n + 1, bool); keep[1:] = sizes >= sizes.max() * 0.15
    m = ndimage.binary_dilation(keep[lab], iterations=6)
    return (a * m)[..., None].astype(np.uint8)

# ---------- I/O ----------
def reader(path, ch):
    p = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", path, "-f", "rawvideo", "-pix_fmt", "rgb24" if ch == 3 else "gray", "-"], stdout=subprocess.PIPE)
    n = W * H * ch
    while True:
        b = p.stdout.read(n)
        if len(b) < n: return
        yield np.frombuffer(b, np.uint8).reshape(H, W, ch)

def run(out_path, only=None):
    wr = None if only else subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                                             "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out_path], stdin=subprocess.PIPE)
    store = {}
    want = set()
    for k, s in enumerate(CUTS):
        for off in SNAPS: want.add(int(round((s + off) * FPS)))
    for fi, (fr, al) in enumerate(zip(reader(SRC, 3), reader(ALPHA, 1))):
        if fi >= NF: break
        al = clean_alpha(al)
        if fi in want: store[fi] = (grade(fr.astype(np.float32) / 255), al[..., 0].astype(np.float32) / 255)
        if only is not None and fi not in only: continue
        P = plan(fi); rng = np.random.default_rng(fi * 7919 + 13)
        if P["freeze"] is not None:
            img, a = store[P["freeze"]]; img = img.copy()
            zoom = 1.035                                                     # tiny punch on each snap
            ys, xs = int(H * (zoom - 1) / 2), int(W * (zoom - 1) / 2)
            img = np.asarray(Image.fromarray((img.clip(0, 1) * 255).astype(np.uint8)).crop((xs, ys, W - xs, H - ys)).resize((W, H), Image.BILINEAR)).astype(np.float32) / 255
        else:
            img = grade(fr.astype(np.float32) / 255); a = al[..., 0].astype(np.float32) / 255
        a3 = a[..., None]
        bg = img
        for c in P["clones"]:                                               # frozen cut-outs from earlier snaps
            ci, ca = store[c]; ca3 = ca[..., None]; bg = bg * (1 - ca3) + ci * ca3
        if P["text"]:
            solid, ol, sets_l = TL[P["k"]]
            bg2 = put_text(bg, solid, rng, P["text"])
            if P["text"]["echo"] > 0:                                        # snapshot echoes of the text (outline copies)
                for j, dy in enumerate((-70, 70, -140)):
                    ea = shift(ol[..., 3:4], 0, dy) * P["text"]["echo"] * (0.8 - 0.2 * j)
                    bg2 = bg2 * (1 - ea) + ea
            sst = dict(P["text"]); sst["solid"] = 1.0; sst["opacity"] = P["text"]["opacity"] * (1.0 if P["text"]["echo"] < 0.75 else 0.0)
            bg = put_text(bg2, sets_l, rng, sst) if sst["opacity"] > 0 else bg2
        out = bg * (1 - a3) + img * a3 if (P["text"] or P["clones"]) else bg   # athlete back on top (= behind-the-subject text)
        if P["text"] and P["text"]["glitch"] < 0.5:                         # faint outline of the hidden letters over the athlete
            ga = ol[..., 3:4] * a3 * (0.34 * P["text"]["opacity"]); out = out * (1 - ga) + ga
        if P["fglitch"] > 0: out = glitch_frame(out, rng, P["fglitch"])
        if P["flash"] > 0: out = out * (1 - P["flash"]) + P["flash"]
        if P["freeze"] is not None:                                         # thin photo frame during a snap
            bw = 14; out[:bw] = out[-bw:] = 1; out[:, :bw] = out[:, -bw:] = 1
        out = out + rng.normal(0, 0.012, (H, W, 1)).astype(np.float32)        # grain
        o8 = (out.clip(0, 1) * 255).astype(np.uint8)
        if only is not None: Image.fromarray(o8).save(f"{out_path}/f{fi:05d}.jpg", quality=90)
        else: wr.stdin.write(o8.tobytes())
        if fi % 150 == 0: print("frame", fi, flush=True)
    if wr: wr.stdin.close(); wr.wait()

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--preview":
        import os; os.makedirs(sys.argv[3], exist_ok=True)
        run(sys.argv[3], only={int(round(float(x) * FPS)) for x in sys.argv[2].split(",")})
    else:
        run("renders/video.mp4")
