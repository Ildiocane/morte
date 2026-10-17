# coach-perche: no cuts, voice untouched (muxed later with -c:a copy), no music/SFX.
# Layers: face video (full length) · forehead-height text · b-roll inserts · 2 full-screen graphics · word captions.
import json, re, html as H

W = json.load(open("assets/words.json"))
DUR = 74.316
def t(word, n=1, after=0.0):
    """start time of the n-th occurrence of `word` (prefix match) after `after` seconds"""
    k = 0
    for w in W:
        if w["s"] >= after - 1e-6 and re.sub(r"[^\wàèéìòù']", "", w["w"].lower()).startswith(word):
            k += 1
            if k == n: return w["s"]
    raise SystemExit(f"word not found: {word} after {after}")

def mark(s): return re.sub(r"\[(.+?)\]", r'<span class="hl">\1</span>', s)
body, js = [], []
tr = [10]
def track(): tr[0] += 1; return tr[0]

# ---------------- forehead-height text (y ≈ 470–700) ----------------
# (start, end, lines[(text, at)]) ; [word] = red highlight box
FH = [   # only three moments on the face, all in the band above the head
    (t("quanti") - 0.15, 8.25, [("Quanti coach", t("quanti") - 0.15), ("ti spiegano il [perché?]", t("spiegarti"))]),
    (t("perché", 1, 55) - 0.05, 58.75, [("Il perché di", t("perché", 1, 55) - 0.05), ("[ogni stimolo]", t("stimolo") - 0.2)]),
    (t("quindi", 1, 65) + 0.1, t("allora", 1, 72) - 0.05, [("Il tuo coach", t("coach", 1, 65)), ("[non ti spiega?]", t("spiegando") - 0.2)]),
]
for i, (a, e, lines) in enumerate(FH):
    lh = "".join(f'<div class="fl l{j}">{mark(H.escape(x).replace("[", "[").replace("]", "]"))}</div>' for j, (x, at) in enumerate(lines))
    body.append(f'<div class="fh clip" id="fh{i}" data-start="{a:.3f}" data-duration="{e - a:.3f}" data-track-index="{track()}">{lh}</div>')
    for j, (x, at) in enumerate(lines):
        js.append(f'tl.fromTo("#fh{i} .l{j}",{{opacity:0,y:34,scale:0.94}},{{opacity:1,y:0,scale:1,duration:0.32,ease:"back.out(2)"}},{max(a, at):.3f});')
    js.append(f'tl.fromTo("#fh{i} .hl",{{backgroundSize:"0% 100%"}},{{backgroundSize:"100% 100%",duration:0.3,ease:"power2.out"}},{max(a, lines[-1][1]) + 0.15:.3f});')
    js.append(f'tl.to("#fh{i}",{{opacity:0,duration:0.15}},{e - 0.15:.3f});')

# closing stamp, same band above the head
a = t("allora", 1, 72) - 0.05
body.append(f'<div class="fh clip" id="end" data-start="{a:.3f}" data-duration="{DUR - a:.3f}" data-track-index="{track()}"><div class="fl e1"><span class="stamp big">cambia coach</span></div></div>')
js.append(f'tl.fromTo("#end .stamp",{{opacity:0,scale:2.2,rotation:-4}},{{opacity:1,scale:1,rotation:-4,duration:0.22,ease:"power4.in"}},{t("cambi", 1, 72) - 0.1:.3f});')

# ---------------- b-roll inserts (full screen, face video keeps running underneath) ----------------
BR = [("pdf1", 0, t("io", 1, 14.5) - 0.02, t("quali", 1, 19)), ("squat", 0.3, t("quali", 1, 19), t("perché", 1, 24)), ("pdf2", 0, t("ed", 1, 58.5) - 0.05, t("quindi", 1, 65))]
LEN = {"pdf1": 5, "pdf2": 7, "squat": 6}
for k, (name, off, a, e) in enumerate(BR):
    d = min(e - a, LEN[name] - off - 0.03)
    body.append(f'<div class="bw" id="bw{k}"><video id="vb{k}" src="assets/broll/{name}.mp4" muted playsinline data-start="{a:.3f}" data-duration="{d:.3f}" data-media-start="{off}" data-track-index="{track()}"></video></div>')
    js.append(f'tl.fromTo("#bw{k}",{{scale:1.0}},{{scale:1.07,duration:{d:.3f},ease:"none"}},{a:.3f});')
    assert d > e - a - 0.05, f"b-roll {name} too short"
# text on the b-roll, same forehead band
BT = [(t("io", 1, 14.5), t("quali", 1, 19) - 0.05, [("Guide in [PDF]", t("guide"))]),
      (t("quali", 1, 19), t("perché", 1, 24) - 0.05, [("[Progressioni]", t("progressioni"))]),
      (t("ed", 1, 58.5), t("quindi", 1, 65) - 0.05, [("Da leggere con [calma]", t("con", 1, 60.5) - 0.3)])]
for i, (a, e, lines) in enumerate(BT):
    lh = "".join(f'<div class="fl l{j}">{mark(H.escape(x))}</div>' for j, (x, at) in enumerate(lines))
    body.append(f'<div class="fh clip onb" id="bt{i}" data-start="{a:.3f}" data-duration="{e - a:.3f}" data-track-index="{track()}">{lh}</div>')
    for j, (x, at) in enumerate(lines):
        js.append(f'tl.fromTo("#bt{i} .l{j}",{{opacity:0,y:34,scale:0.94}},{{opacity:1,y:0,scale:1,duration:0.32,ease:"back.out(2)"}},{max(a, at):.3f});')
    js.append(f'tl.fromTo("#bt{i} .hl",{{backgroundSize:"0% 100%"}},{{backgroundSize:"100% 100%",duration:0.3,ease:"power2.out"}},{max(a, lines[0][1]) + 0.15:.3f});')

# ---------------- full-screen graphics ----------------
# FS1: "perché" list
a, e = t("perché", 1, 24) - 0.02, t("quindi", 1, 28) - 0.02
items = [("Punti di tensione", t("punti")), ("ROM", t("rom")), ("Time under tension", t("time")), ("Di tutto", t("di", 1, 27.5))]
li = "".join(f'<div class="why w{i}"><span class="wq">Perché</span><span class="wt">{x}</span></div>' for i, (x, at) in enumerate(items))
body.append(f'<div class="fs clip" id="fs1" data-start="{a:.3f}" data-duration="{e - a:.3f}" data-track-index="{track()}"><div class="grid"></div><div class="fsin" style="top:330px"><div class="kick">Nelle mie guide</div><div class="big">Ti spiego<br/><span class="red">il perché</span></div><div class="wlist">{li}</div></div></div>')
js.append(f'tl.fromTo("#fs1 .kick",{{opacity:0}},{{opacity:1,duration:0.3}},{a:.3f});tl.fromTo("#fs1 .big",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.45,ease:"expo.out"}},{a + 0.05:.3f});')
for i, (x, at) in enumerate(items):
    js.append(f'tl.fromTo("#fs1 .w{i}",{{opacity:0,x:-80}},{{opacity:1,x:0,duration:0.35,ease:"expo.out"}},{at - 0.05:.3f});')
js.append(f'tl.fromTo("#fs1 .w3",{{scale:1.25}},{{scale:1,duration:0.25,ease:"power4.in"}},{items[3][1] - 0.05:.3f});')

# FS2: the first program is a draft
a, e = t("una", 1, 37) - 0.03, t("ma", 1, 44) - 0.02
lines_svg = "".join(f'<path class="sk s{i}" pathLength="1" stroke-dasharray="1" d="M70 {150 + i * 62} q60 -14 120 0 t120 0 t120 0 t{80 + (i * 37) % 90} 0" fill="none" stroke="#3f3f46" stroke-width="7" stroke-linecap="round"/>' for i in range(6))
body.append(f'''<div class="fs clip" id="fs2" data-start="{a:.3f}" data-duration="{e - a:.3f}" data-track-index="{track()}"><div class="grid"></div>
  <div class="fsin" style="top:250px"><div class="kick">La prima programmazione</div><div class="big">È una <span class="red">bozza</span></div>
  <div class="paper"><div class="ptag">v1 · bozza</div><svg width="640" height="560" viewBox="0 0 640 560">{lines_svg}
    <path class="q1" pathLength="1" stroke-dasharray="1" d="M470 470 c40 -50 110 -30 100 20 c-10 50 -90 50 -110 10" fill="none" stroke="#ef4b40" stroke-width="7" stroke-linecap="round"/></svg>
    <div class="sticky">da verificare</div></div>
  <div class="sub s1">serve a capire</div><div class="sub s2"><span class="red">le tue esigenze</span></div></div></div>''')
js.append(f'tl.fromTo("#fs2 .kick",{{opacity:0}},{{opacity:1,duration:0.3}},{a:.3f});tl.fromTo("#fs2 .big",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.45,ease:"expo.out"}},{a + 0.05:.3f});')
js.append(f'tl.fromTo("#fs2 .paper",{{opacity:0,y:80,rotation:-8}},{{opacity:1,y:0,rotation:-3,duration:0.6,ease:"expo.out"}},{a + 0.3:.3f});')
for i in range(6): js.append(f'tl.fromTo("#fs2 .s{i}",{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:0.5,ease:"power1.inOut"}},{a + 0.7 + i * 0.35:.3f});')
js.append(f'tl.fromTo("#fs2 .q1",{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:0.6}},{t("capire") - 0.2:.3f});tl.fromTo("#fs2 .sticky",{{opacity:0,scale:0.6,rotation:12}},{{opacity:1,scale:1,rotation:8,duration:0.35,ease:"back.out(2)"}},{t("stimi"):.3f});')
js.append(f'tl.fromTo("#fs2 .s1",{{opacity:0,y:20}},{{opacity:1,y:0,duration:0.35}},{t("capire"):.3f});tl.fromTo("#fs2 .s2",{{opacity:0,y:20}},{{opacity:1,y:0,duration:0.35}},{t("esigenze"):.3f});')

# ---------------- gentle punch-ins on the face (no cuts) ----------------
Z = [(0, 1.0), (t("perché", 1, 5) - 0.1, 1.04), (8.4, 1.0), (t("stimolo") - 0.1, 1.04), (t("quindi", 1, 65), 1.0), (t("cambi", 1, 72) - 0.1, 1.05)]
for tt, sc in Z: js.append(f'tl.to("#facew",{{scale:{sc},duration:0.35,ease:"power2.out"}},{tt:.3f});')

# ---------------- captions: 1–3 words, active word on a red box ----------------
caps, cur = [], []
for w in W:
    if cur and (w["s"] - cur[-1]["e"] > 0.45 or len(" ".join(x["w"] for x in cur + [w])) > 17): caps.append(cur); cur = []
    cur.append(w)
    if re.search(r"[.,?!:;]$", w["w"]) or len(cur) >= 3: caps.append(cur); cur = []
if cur: caps.append(cur)
cap_html = []
for i, g in enumerate(caps):
    a = g[0]["s"]; e = g[-1]["e"] + 0.2
    if i + 1 < len(caps): e = min(max(e, caps[i + 1][0]["s"] - 0.01) if caps[i + 1][0]["s"] - g[-1]["e"] < 0.5 else e, caps[i + 1][0]["s"] - 0.01)
    e = max(e, a + 0.25)
    spans = "".join(f'<span class="cw" id="c{i}w{k}">{H.escape(re.sub(r"[.,;:]$", "", x["w"]).upper())}</span> ' for k, x in enumerate(g))
    cap_html.append(f'<div class="cap" id="c{i}">{spans}</div>')
    js.append(f'tl.set("#c{i}",{{opacity:1}},{a:.3f});tl.set("#c{i}",{{opacity:0}},{e:.3f});')
    for k, x in enumerate(g):
        js.append(f'tl.set("#c{i}w{k}",{{backgroundColor:"rgba(224,48,42,1)"}},{x["s"]:.3f});' + (f'tl.set("#c{i}w{k}",{{backgroundColor:"rgba(224,48,42,0)"}},{g[k + 1]["s"]:.3f});' if k + 1 < len(g) else ""))

from pathlib import Path
import sys; sys.path.insert(0, "../scarico-decisione/scripts"); from scenes import lbmark
tpl = Path("scripts/index.tpl.html").read_text()
out = (tpl.replace("__DUR__", f"{DUR:.3f}").replace("__BODY__", "\n      ".join(body)).replace("__CAPS__", "\n        ".join(cap_html))
          .replace("__JS__", "\n      ".join(js)).replace("__LBMARK__", lbmark(30)))
Path("index.html").write_text(out)
print("ok", len(caps), "captions,", len(FH), "forehead texts,", len(BR), "b-roll,", "2 full-screen")
