# Builds index.html from: assets/timing.json + assets/words.json (narration timing) and the storyboard in storyboard.py.
# All animation times are resolved here (word anchors -> seconds); the page just plays a GSAP timeline.
import json, os, re, sys, html as H
sys.path.insert(0, os.path.dirname(__file__))
TIM = json.load(open("assets/timing.json")); WORDS = json.load(open("assets/words.json"))
CH, SEC, DUR = TIM["chunks"], TIM["sections"], TIM["dur"]
norm = lambda w: re.sub(r"[^a-zàèéìòóù0-9']", "", w.lower())

def T(a):
    """anchor -> seconds. 's2d' chunk start, 's2d$' chunk end, 's2d:word' / 's2d:word#2' word start, optional '+0.3' / '-0.2'."""
    if isinstance(a, (int, float)): return float(a)
    off = 0.0
    m = re.match(r"^(.*?)([+-]\d+(?:\.\d+)?)$", a)
    if m and ":" not in m.group(2): a, off = m.group(1), float(m.group(2))
    if a.endswith("$"): return CH[a[:-1]][1] + off
    if ":" not in a: return (CH[a][0] if a in CH else SEC[a][0]) + off
    cid, key = a.split(":", 1); n = 1
    if "#" in key: key, n = key.split("#"); n = int(n)
    hits = [w for w in WORDS if w["c"] == cid and (norm(w["w"]) == norm(key[1:]) if key.startswith("=") else norm(w["w"]).startswith(norm(key)))]
    if len(hits) < n: raise SystemExit(f"anchor not found: {a}")
    return hits[n - 1]["s"] + off

def TE(a):
    """end time of the word an anchor points at"""
    cid, key = a.split(":", 1); n = 1
    if "#" in key: key, n = key.split("#"); n = int(n)
    hits = [w for w in WORDS if w["c"] == cid and norm(w["w"]).startswith(norm(key))]
    return hits[n - 1]["e"]

from storyboard import BEATS, POPS, BROLL_LEN, SFX_EXTRA, CHAPTERS
import scenes as SC

body, anims, sfx = [], [], []
track = [10]
def tr():
    track[0] += 1; return track[0]

# ---------- beats: each lasts until the next one starts ----------
starts = [T(b["at"]) for b in BEATS]
for i, b in enumerate(BEATS):
    a = starts[i]; e = starts[i + 1] if i + 1 < len(BEATS) else DUR
    if e - a < 0.3: raise SystemExit(f"beat too short at {b['at']}: {e - a:.2f}s")
    bid = f"b{i}"
    if "broll" in b:
        clips = b["broll"] if isinstance(b["broll"], list) else [b["broll"]]
        t0 = a; k = 0
        while t0 < e - 0.05:
            name = clips[min(k, len(clips) - 1)]; off = b.get("off", 0) if k == 0 else 0
            d = min(e - t0, BROLL_LEN[name] - off - 0.04)
            if d < 0.3: raise SystemExit(f"b-roll {name} too short at {b['at']}")
            wid = f"{bid}w{k}"
            body.append(f'<div class="bw" id="{wid}"><video id="v{wid}" src="assets/broll/{name}.mp4" muted playsinline data-start="{t0:.3f}" data-duration="{d:.3f}" '
                        f'data-media-start="{off:.3f}" data-track-index="{tr()}"></video></div>')
            z0, z1 = b.get("zoom", (1.03, 1.12)); ox = b.get("origin", "50% 50%")
            if b.get("flip"): body[-1] = body[-1].replace('class="bw"', 'class="bw flip"')
            anims.append(f'tl.fromTo("#{wid}",{{scale:{z0}}},{{scale:{z1},duration:{d:.3f},ease:"none",transformOrigin:"{ox}"}},{t0:.3f});')
            t0 += d; k += 1
            if t0 < e - 0.05 and k >= len(clips): raise SystemExit(f"b-roll beat at {b['at']} needs {e - t0:.2f}s more footage")
    else:
        fn = getattr(SC, b["scene"])
        h, an = fn(bid, T, TE, a, e, **b.get("p", {}))
        body.append(f'<div class="fs clip" id="{bid}" data-start="{a:.3f}" data-duration="{e - a:.3f}" data-track-index="{tr()}">{h}</div>')
        for sel, t, kind, *ex in an:
            anims.append(SC.anim(sel, t, kind, ex[0] if ex else None))
        if b.get("sfx"): sfx.append((b["sfx"], a - 0.12))

# ---------- pop-ups over b-roll ----------
for j, p in enumerate(POPS):
    a = T(p["at"]); e = T(p["to"]) if "to" in p else a + p.get("d", 3.5)
    pid = f"p{j}"
    h, an = getattr(SC, "pop_" + p.get("kind", "card"))(pid, T, TE, a, e, **p.get("p", {}))
    body.append(f'<div class="pop clip {p.get("pos", "right")}" id="{pid}" data-start="{a:.3f}" data-duration="{e - a:.3f}" data-track-index="{tr()}">{h}</div>')
    anims.append(SC.anim(f"#{pid} .pc", a, "popin"))
    anims.append(f'tl.to("#{pid} .pc",{{opacity:0,y:-14,duration:0.22,ease:"power2.in"}},{e - 0.24:.3f});')
    for sel, t, kind, *ex in an: anims.append(SC.anim(sel, t, kind, ex[0] if ex else None))
    if p.get("sfx", "pop"): sfx.append((p.get("sfx", "pop"), a - 0.03))

# ---------- chapter HUD + progress ----------
chap_js, chap_html = [], []
for k, (sid, label) in enumerate(CHAPTERS):
    a = SEC[sid][0] + (0.0 if sid != "s2" else 0.0); e = SEC[CHAPTERS[k + 1][0]][0] - 1.75 if k + 1 < len(CHAPTERS) else DUR - 2.5
    chap_html.append(f'<div class="chap" id="chap{k}"><span class="lbm">{SC.lbmark(24)}<b>LB</b></span><span class="chapnum">{k + 1:02d}</span><span class="chaptxt">{H.escape(label)}</span></div>')
    chap_js.append(f'tl.fromTo("#chap{k}",{{opacity:0,x:-30}},{{opacity:1,x:0,duration:0.4,ease:"expo.out"}},{a:.3f});tl.to("#chap{k}",{{opacity:0,duration:0.25}},{e - 0.3:.3f});')
segs = "".join(f'<i style="flex:{SEC[s][1] - SEC[s][0]:.2f}"><b id="pg{k}"></b></i>' for k, (s, _) in enumerate(CHAPTERS))
prog_js = "".join(f'tl.fromTo("#pg{k}",{{scaleX:0}},{{scaleX:1,duration:{SEC[s][1] - SEC[s][0]:.3f},ease:"none"}},{SEC[s][0]:.3f});' for k, (s, _) in enumerate(CHAPTERS))

# ---------- captions ----------
caps, cur = [], []
def flush():
    if cur: caps.append(list(cur)); cur.clear()
for k, w in enumerate(WORDS):
    if cur and (w["c"] != cur[-1]["c"] or w["s"] - cur[-1]["e"] > 0.5): flush()
    cur.append(w)
    txt = " ".join(x["w"] for x in cur)
    end_p = re.search(r"[.?!:;]$", w["w"]); comma = w["w"].endswith(",")
    if end_p or len(txt) > 40 or (comma and len(cur) >= 3) or len(cur) >= 8: flush()
flush()
cap_html, cap_js = [], []
for i, g in enumerate(caps):
    a = g[0]["s"]; e = g[-1]["e"] + 0.25
    if i + 1 < len(caps): e = min(max(e, caps[i + 1][0]["s"] - 0.02) if caps[i + 1][0]["s"] - g[-1]["e"] < 0.6 else e, caps[i + 1][0]["s"] - 0.02)
    txt = " ".join(x["w"] for x in g).rstrip(",;:")
    cap_html.append(f'<div class="cap" id="c{i}">{H.escape(txt)}</div>')
    cap_js.append(f'tl.set("#c{i}",{{opacity:1}},{a:.3f});tl.set("#c{i}",{{opacity:0}},{e:.3f});')

# ---------- audio ----------
sfx += SFX_EXTRA(T)
VOL = {"whoosh": 0.10, "pop": 0.12, "click": 0.14, "slam": 0.12, "swipe": 0.09, "sparkle": 0.10, "bass-drop": 0.16, "riser": 0.09, "paper-flip": 0.12, "zap": 0.08, "error": 0.06}
LEN = {"whoosh": 0.57, "pop": 0.72, "click": 0.46, "slam": 1.22, "swipe": 1.06, "sparkle": 2.04, "bass-drop": 1.1, "riser": 4.03, "paper-flip": 2.61, "zap": 0.92, "error": 2.55}
EXT = {"click": "wav"}
sfx.sort(key=lambda x: x[1]); kept, last = [], -9
for n, t in sfx:                                   # never two SFX within 0.9 s
    if t - last >= 0.9 and t > 0: kept.append((n, t)); last = t
aud = [f'<audio id="vo" src="assets/audio/narration.wav" data-start="0" data-duration="{DUR:.3f}" data-track-index="1" data-volume="1"></audio>',
       f'<audio id="mu" src="assets/audio/music-long.mp3" data-start="0" data-duration="{DUR:.3f}" data-track-index="2" data-volume="0.055" data-fade-in="1.5" data-fade-out="3"></audio>']
for k, (n, t) in enumerate(kept):
    aud.append(f'<audio id="sfx{k}" src="assets/sfx/{n}.{EXT.get(n, "mp3")}" data-start="{t:.3f}" data-duration="{LEN[n]}" data-track-index="{tr()}" data-volume="{VOL[n]}"></audio>')

tpl = open("scripts/index.tpl.html").read()
out = (tpl.replace("__DUR__", f"{DUR:.3f}").replace("__BODY__", "\n      ".join(body)).replace("__AUDIO__", "\n      ".join(aud))
       .replace("__SEGS__", segs).replace("__CAPS__", "\n        ".join(cap_html))
       .replace("__ANIMS__", "\n      ".join(anims)).replace("__CHAP__", "\n      ".join(chap_js)).replace("__PROG__", prog_js).replace("__CAPJS__", "\n      ".join(cap_js)).replace("__CHAPS__", "".join(chap_html)))
open("index.html", "w").write(out)
print(f"ok  dur {DUR:.1f}s  beats {len(BEATS)}  pops {len(POPS)}  captions {len(caps)}  sfx {len(kept)}")
