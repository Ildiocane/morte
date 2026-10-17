# Full-screen graphic scenes + pop-ups. Each scene fn returns (html, anims); anims = [(selector, seconds, kind, extra?)].
# T(anchor) -> seconds, TE(anchor) -> end of that word. a/e = scene start/end.
import json

def anim(sel, t, kind, ex=None):
    s, t = json.dumps(sel), f"{t:.3f}"
    K = {
        "up": f'tl.fromTo({s},{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.5,ease:"expo.out"}},{t});',
        "down": f'tl.fromTo({s},{{opacity:0,y:-40}},{{opacity:1,y:0,duration:0.5,ease:"expo.out"}},{t});',
        "fade": f'tl.fromTo({s},{{opacity:0}},{{opacity:1,duration:0.4,ease:"power1.out"}},{t});',
        "pop": f'tl.fromTo({s},{{opacity:0,scale:0.82}},{{opacity:1,scale:1,duration:0.45,ease:"back.out(1.8)"}},{t});',
        "popin": f'tl.fromTo({s},{{opacity:0,y:26,scale:0.96}},{{opacity:1,y:0,scale:1,duration:0.42,ease:"expo.out"}},{t});',
        "left": f'tl.fromTo({s},{{opacity:0,x:-80}},{{opacity:1,x:0,duration:0.55,ease:"expo.out"}},{t});',
        "right": f'tl.fromTo({s},{{opacity:0,x:80}},{{opacity:1,x:0,duration:0.55,ease:"expo.out"}},{t});',
        "grow": f'tl.fromTo({s},{{scaleX:0}},{{scaleX:1,duration:{(ex or {}).get("d", 0.6)},ease:"power3.out",transformOrigin:"0% 50%"}},{t});',
        "growY": f'tl.fromTo({s},{{scaleY:0}},{{scaleY:1,duration:{(ex or {}).get("d", 0.9)},ease:"power2.out",transformOrigin:"50% 100%"}},{t});',
        "mark": f'tl.fromTo({json.dumps(sel + " > i")},{{scaleX:0,skewX:-12}},{{scaleX:1,skewX:-12,duration:0.45,ease:"power3.out"}},{t});',
        "strike": f'tl.fromTo({json.dumps(sel + " > i")},{{scaleX:0}},{{scaleX:1,duration:0.35,ease:"power2.out"}},{t});',
        "stamp": f'tl.fromTo({s},{{opacity:0,scale:1.9,rotation:{(ex or {}).get("r", -5)}}},{{opacity:1,scale:1,rotation:{(ex or {}).get("r", -5)},duration:0.24,ease:"power4.in"}},{t});',
        "dim": f'tl.to({s},{{opacity:{(ex or {}).get("o", 0.28)},duration:0.3}},{t});',
        "undim": f'tl.to({s},{{opacity:1,duration:0.3}},{t});',
        "out": f'tl.to({s},{{opacity:0,duration:0.25}},{t});',
        "draw": f'tl.fromTo({s},{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:{(ex or {}).get("d", 1.0)},ease:"power2.inOut"}},{t});',
        "count": f'tl.fromTo({s},{{textContent:{(ex or {}).get("a", 0)}}},{{textContent:{(ex or {}).get("b", 10)},duration:{(ex or {}).get("d", 0.8)},snap:{{textContent:1}},ease:"power1.out"}},{t});',
        "set": f'tl.set({s},{json.dumps(ex)},{t});',
        "to": f'tl.to({s},{json.dumps(ex)},{t});',
        "pulse": f'tl.fromTo({s},{{scale:1}},{{scale:1.07,duration:0.18,yoyo:true,repeat:1,ease:"power1.inOut"}},{t});',
    }
    return K[kind]

# ---------------- icons (24x24 stroke) ----------------
P = {
    "dumbbell": "M6 6v12M18 6v12M3 9.5v5M21 9.5v5M6 12h12",
    "moon": "M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z",
    "food": "M7 3v8M4.5 3v5a2.5 2.5 0 0 0 5 0V3M7 11v10M17 3c-2 2-2.5 5.5-2 8.5h2V21",
    "bolt": "M13 2L4 14h7l-1 8 9-12h-7z",
    "trend": "M3 17l6-6 4 4 8-8M15 7h6v6",
    "down": "M3 7l6 6 4-4 8 8M15 17h6v-6",
    "wave": "M2 12c2-5 4-5 6 0s4 5 6 0 4-5 6 0",
    "sliders": "M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6",
    "cal": "M3 6h18v15H3zM3 10h18M8 3v5M16 3v5",
    "check": "M4.5 12.5l5 5 10-11",
    "x": "M6 6l12 12M18 6L6 18",
    "med": "M9 3h6v6h6v6h-6v6H9v-6H3V9h6z",
    "phone": "M7 2h10v20H7zM11 18.5h2",
    "pause": "M8 5v14M16 5v14",
    "clock": "M12 7v5l3.5 2",
    "q": "M9 9a3 3 0 1 1 4.2 2.75c-.75.35-1.2 1-1.2 1.8v.45M12 18h.01",
    "user": "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4 21a8 8 0 0 1 16 0",
    "loop": "M4 12a8 8 0 0 1 14-5.3L20 9M20 4v5h-5M20 12a8 8 0 0 1-14 5.3L4 15M4 20v-5h5",
    "arrow": "M4 12h16M14 6l6 6-6 6",
    "note": "M6 3h11a2 2 0 0 1 2 2v16H8a2 2 0 0 1-2-2zM10 8h6M10 12h6M10 16h4",
    "batt": "M2 8h16v8H2zM21 11v2M5 11v2",
    "data": "M4 20V10M10 20V4M16 20v-7M22 20H2",
    "eye": "M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12zM12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z",
    "target": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM12 12h.01",
    "chat": "M4 5h16v11H9l-5 4z",
    "spark": "M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6",
    "pain": "M12 2l2.5 6.5L21 9l-5 4.5L17.5 21 12 17l-5.5 4L8 13.5 3 9l6.5-.5z",
    "rep": "M3 12h3M18 12h3M6 8v8M18 8v8M9 10v4M15 10v4M9 12h6",
}
CIRCLE = {"clock", "target"}
def ic(name, size=56, color="#ffffff", sw=2.3):
    extra = '<circle cx="12" cy="12" r="9"/>' if name == "clock" else ""
    return (f'<span class="ico"><svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{extra}<path d="{P[name]}"/></svg></span>')

def lbmark(h=40, col="#a11d19"):
    w = h / 1.2
    segs = [((50, 0), (100, 58)), ((6, 4), (94, 114)), ((0, 58), (50, 120)), ((94, 4), (6, 114)), ((50, 0), (0, 58)), ((100, 58), (50, 120))]
    lines = "".join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#c2c2c2" stroke-width="22"/><line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{col}" stroke-width="10"/>' for a, b in segs)
    return f'<svg width="{w:.0f}" height="{h}" viewBox="-8 -8 116 136" style="display:block;overflow:visible">{lines}</svg>'

def lbpill(h=58):
    return f'<span class="lbpill">{lbmark(h)}<b style="font-size:{h * 1.05:.0f}px">LB</b></span>'

def boxes(n, on=(), cls="", size=64, gap=12):
    return '<div class="row" style="gap:%dpx">' % gap + "".join(f'<div class="box {"on" if i in on else ""} {cls}" style="width:{size}px;height:{size}px"></div>' for i in range(n)) + "</div>"

def W(inner, cls="", style=""):
    return f'<div class="wrap {cls}" style="{style}">{inner}</div>'

# =====================================================================================
# scenes
# =====================================================================================
def stamp_word(b, T, TE, a, e, word, kick="", sub="", sub_at=None, size=120):
    h = W(f'<div class="kick k">{kick}</div><div style="height:30px"></div><div class="stamp s" style="font-size:{size}px">{word}</div>'
          f'<div style="height:44px"></div><div class="body sb" style="font-size:38px">{sub}</div>', "center")
    an = [(f"#{b} .s", a + 0.1, "stamp")]
    if kick: an.append((f"#{b} .k", a, "fade"))
    if sub: an.append((f"#{b} .sb", T(sub_at) if sub_at else a + 0.8, "up"))
    return h, an

def compare_days(b, T, TE, a, e, right_at, neq_at, noise_at, info_at):
    cal1 = '<div class="row" style="gap:10px">' + "".join(f'<div class="box {"on" if i == 3 else ""}" style="width:54px;height:54px"></div>' for i in range(7)) + "</div>"
    cal2 = '<div class="row" style="gap:10px">' + "".join(f'<div class="box {"on" if i in (0,2,3,5) else ""}" style="width:54px;height:54px"></div>' for i in range(7)) + "</div>"
    noise = '<svg width="420" height="70" viewBox="0 0 420 70"><path d="M0 35 L30 30 L60 42 L90 28 L120 38 L150 33 L180 36 L210 20 L240 37 L270 34 L300 39 L330 31 L360 36 L390 33 L420 35" fill="none" stroke="#a1a1aa" stroke-width="4"/></svg>'
    sig = '<svg width="420" height="70" viewBox="0 0 420 70"><path class="sg" pathLength="1" stroke-dasharray="1" d="M0 12 L80 16 L160 28 L240 40 L320 52 L420 62" fill="none" stroke="#ef4b40" stroke-width="7" stroke-linecap="round"/></svg>'
    h = W(f'''<div class="row" style="justify-content:center;gap:60px;align-items:stretch">
      <div class="card l" style="width:640px"><div class="kick">Una sola</div><div class="h3" style="margin:14px 0 26px">Giornata storta</div>{cal1}
        <div class="nz" style="margin-top:34px"><div class="h4 mut">= rumore</div>{noise}</div></div>
      <div class="neq n" style="align-self:center">≠</div>
      <div class="card acc r" style="width:640px"><div class="kick">Diverse</div><div class="h3" style="margin:14px 0 26px">Sedute difficili di fila</div>{cal2}
        <div class="inf" style="margin-top:34px"><div class="h4 red">= informazione</div>{sig}</div></div></div>''')
    return h, [(f"#{b} .l", a, "left"), (f"#{b} .r", T(right_at), "right"), (f"#{b} .n", T(neq_at), "pop"),
               (f"#{b} .nz", T(noise_at), "up"), (f"#{b} .inf", T(info_at), "up"), (f"#{b} .sg", T(info_at) + 0.2, "draw", {"d": 0.9})]

def crossed(b, T, TE, a, e, title, items):
    rows = "".join(f'<div class="row it{i}" style="gap:30px">{ic(icn, 64, "#a1a1aa")}<span class="strk h2" style="font-size:70px">{txt}<i></i></span></div>' for i, (txt, icn, at, st) in enumerate(items))
    h = W(f'<div class="kick k">{title}</div><div style="height:46px"></div><div class="col" style="gap:46px">{rows}</div>')
    an = [(f"#{b} .k", a, "fade")]
    for i, (txt, icn, at, st) in enumerate(items):
        an += [(f"#{b} .it{i}", T(at), "left"), (f"#{b} .it{i} .strk", T(st), "strike"), (f"#{b} .it{i}", T(st) + 0.35, "dim", {"o": 0.45})]
    return h, an

def steps3(b, T, TE, a, e, title, steps, kick=""):
    cells = []
    for i, (txt, icn, at) in enumerate(steps):
        if i: cells.append(f'<div class="arrow ar{i}">{ic("arrow", 54, "#71717a")}</div>')
        cells.append(f'<div class="card st{i}" style="width:430px;text-align:center;padding:40px 30px"><div style="display:flex;justify-content:center">{ic(icn, 76, "#ef4b40")}</div>'
                     f'<div class="h3" style="margin-top:24px;font-size:42px">{txt}</div></div>')
    h = W(f'<div class="kick k">{kick}</div><div class="h2 t" style="margin:16px 0 60px">{title}</div><div class="row" style="justify-content:center;gap:22px">{"".join(cells)}</div>', "center")
    an = [(f"#{b} .k", a, "fade"), (f"#{b} .t", a + 0.05, "up")]
    for i, (txt, icn, at) in enumerate(steps):
        an.append((f"#{b} .st{i}", T(at), "pop"))
        if i: an.append((f"#{b} .ar{i}", T(at) - 0.1, "fade"))
    return h, an

def sting(b, T, TE, a, e, title, sub):
    title = title.replace(": ", ":<br/>")
    h = f'''<div class="wrap center" style="top:150px">
      <div class="row lg" style="justify-content:center;gap:56px"><img class="nx" src="assets/img/nexus-dark.png" style="width:560px" alt="NEXUS Private Gym"/>
        <span class="xx" style="font:italic 900 70px/1 Saira;color:#71717a">×</span><span class="lbw">{lbpill(92)}</span></div>
      <div class="ln" style="width:900px;height:6px;background:var(--red);margin:60px auto 46px;border-radius:3px"></div>
      <div class="h1 tt" style="font-size:104px">{title}</div><div class="h3 sb mut" style="margin-top:22px;font-weight:600">{sub}</div></div>'''
    return h, [(f"#{b} .nx", a + 0.05, "left"), (f"#{b} .xx", a + 0.35, "pop"), (f"#{b} .lbw", a + 0.5, "right"), (f"#{b} .ln", a + 0.8, "grow", {"d": 0.7}),
               (f"#{b} .tt", a + 1.0, "up"), (f"#{b} .sb", a + 1.4, "up")]

def chapter(b, T, TE, a, e, num, title):
    h = f'''<div class="wrap" style="left:180px">
      <div class="row"><div class="cn" style="font:italic 900 300px/0.8 Saira;color:transparent;-webkit-text-stroke:4px #ef4b40">{num}</div>
      <div class="col" style="gap:18px;margin-left:30px"><div class="kick ck">Capitolo {int(num)}</div><div class="h1 ct" style="font-size:112px;max-width:1150px">{title}</div>
      <div class="cl" style="width:520px;height:8px;background:var(--red);border-radius:4px"></div></div></div></div>'''
    return h, [(f"#{b} .cn", a, "left"), (f"#{b} .ck", a + 0.15, "fade"), (f"#{b} .ct", a + 0.2, "up"), (f"#{b} .cl", a + 0.35, "grow")]

def definition(b, T, TE, a, e, temp_at, rid_at, smett_at):
    h = W(f'''<div class="card acc" style="padding:56px 64px 60px">
      <div class="row" style="gap:24px;align-items:baseline"><div class="h1 w" style="font-size:118px">Scarico</div><div class="body" style="font-style:italic">s.m.</div></div>
      <div class="df" style="font:600 64px/1.25 Inter;margin-top:26px">Una <span class="mark m2">riduzione<i></i></span> <span class="mark m1">temporanea<i></i></span><br/>dello stress allenante.</div>
      <div class="row" style="margin-top:46px;gap:40px">
        <div class="tlb row" style="gap:16px">{ic("cal", 50, "#ef4b40")}<span class="h4">Inizio</span><div style="width:260px;height:6px;background:#ef4b40;border-radius:3px"></div><span class="h4">Fine</span></div>
        <div class="ns row" style="gap:16px">{ic("x", 50, "#ef4b40")}<span class="h4">Non per forza smettere</span></div></div></div>''')
    return h, [(f"#{b} .w", a, "left"), (f"#{b} .df", a + 0.4, "up"), (f"#{b} .m1", T(temp_at), "mark"), (f"#{b} .tlb", T(temp_at) + 0.2, "up"),
               (f"#{b} .m2", T(rid_at), "mark"), (f"#{b} .ns", T(smett_at) - 0.4, "up")]

def three_ways(b, T, TE, a, e, c1, c1b, c2, c2b, c3, neq_at, st_at=None):
    sets_from = boxes(4, on=(0, 1, 2, 3), size=48, gap=10)
    sets_to = '<div class="row" style="gap:10px"><div class="box on" style="width:48px;height:48px"></div><div class="box on" style="width:48px;height:48px"></div><div class="box x1" style="width:48px;height:48px;opacity:0.25"></div><div class="box x2" style="width:48px;height:48px;opacity:0.25"></div></div>'
    rir = '<div class="row" style="gap:8px">' + "".join(f'<div class="box rr{i}" style="width:40px;height:72px;border-radius:8px;{"background:#22c55e;border-color:#4ade80" if i < 1 else ""}"></div>' for i in range(4)) + "</div>"
    h = W(f'''<div class="row" style="justify-content:center;gap:34px;align-items:stretch">
      <div class="card acc w1" style="width:470px"><div class="num">1</div><div class="h3" style="margin:14px 0 30px">Meno serie</div>
        <div class="s4">{sets_from}</div><div class="arrow" style="margin:14px 0 14px 70px;transform:rotate(90deg);width:54px">{ic("arrow", 44, "#71717a")}</div><div class="s2">{sets_to}</div>
        <div class="small" style="margin-top:22px">stessi esercizi · carichi simili</div></div>
      <div class="ne1 neq" style="align-self:center;font-size:80px">≠</div>
      <div class="card acc w2" style="width:470px"><div class="num">2</div><div class="h3" style="margin:14px 0 30px">Serie meno difficili</div>
        <div class="small" style="margin-bottom:12px">ripetizioni in riserva</div>{rir}
        <div class="small" style="margin-top:22px">stesse serie · più lontano dal cedimento</div></div>
      <div class="ne2 neq" style="align-self:center;font-size:80px">≠</div>
      <div class="card acc w3" style="width:470px"><div class="num">3</div><div class="h3" style="margin:14px 0 30px">Stop completo</div>
        <div class="row" style="gap:20px">{ic("pause", 96, "#ef4b40", 3)}<div class="h2" style="font-size:70px">0 kg</div></div>
        <div class="small" style="margin-top:34px">una settimana senza pesi</div></div></div>
      <div style="text-align:center;margin-top:46px"><span class="stamp st" style="font-size:54px">Non intercambiabili</span></div>''')
    an = [(f"#{b} .w1", T(c1), "up"), (f"#{b} .s2", T(c1b) - 0.1, "fade"), (f"#{b} .x1", T(c1b) + 0.25, "to", {"opacity": 0.08, "duration": 0.2}),
          (f"#{b} .w2", T(c2), "up"), (f"#{b} .w3", T(c3), "up"), (f"#{b} .ne1", T(neq_at), "pop"), (f"#{b} .ne2", T(neq_at) + 0.15, "pop")]
    for i in (1, 2, 3): an.append((f"#{b} .rr{i}", T(c2b) + 0.12 * i, "to", {"backgroundColor": "#22c55e", "borderColor": "#4ade80", "duration": 0.2}))
    an.append((f"#{b} .st", T(st_at), "stamp"))
    return h, an

def matrix(b, T, TE, a, e, rows):
    html_rows = ""
    for i, (lab, keep, low, at) in enumerate(rows):
        k = "".join(f'<span class="chip g">{ic("check", 26, "#4ade80", 3)}{x}</span>' for x in keep)
        l = "".join(f'<span class="chip r">{ic(icn, 26, "#ff7068", 3)}{x}</span>' for x, icn in low)
        html_rows += f'<div class="card mr{i}" style="display:grid;grid-template-columns:440px 1fr;align-items:center;padding:28px 36px"><div class="h3" style="font-size:42px">{lab}</div><div class="row" style="gap:16px;flex-wrap:wrap">{k}{l}</div></div>'
    h = W(f'<div class="kick k">Cosa cambia davvero</div><div class="col" style="gap:22px;margin-top:30px">{html_rows}</div>')
    return h, [(f"#{b} .k", a, "fade")] + [(f"#{b} .mr{i}", T(r[3]), "left") for i, r in enumerate(rows)]

def quale(b, T, TE, a, e, q1, q2, big_at):
    h = W(f'''<div class="row" style="justify-content:center;gap:40px">
      <div class="card q1" style="font:italic 700 46px/1.2 Inter;padding:30px 40px">«Lo scarico funziona»</div>
      <div class="card q2" style="font:italic 700 46px/1.2 Inter;padding:30px 40px">«Non serve a niente»</div></div>
      <div class="h1 bg" style="text-align:center;margin-top:70px;font-size:150px">Quale <span class="red">scarico?</span></div>''')
    return h, [(f"#{b} .q1", T(q1), "pop"), (f"#{b} .q2", T(q2), "pop"), (f"#{b} .q1", T(big_at), "dim", {"o": 0.35}), (f"#{b} .q2", T(big_at), "dim", {"o": 0.35}), (f"#{b} .bg", T(big_at), "stamp", {"r": 0})]

def not_transfer(b, T, TE, a, e, l_at, r_at, vv_at):
    h = W(f'''<div class="row" style="justify-content:center;gap:40px">
      <div class="card acc c1" style="width:560px;text-align:center"><div style="display:flex;justify-content:center">{ic("pause", 80, "#ef4b40", 3)}</div><div class="h3" style="margin-top:20px">1 settimana di stop</div></div>
      <div class="col" style="align-items:center;gap:10px"><div class="a1 small" style="font-size:28px">dice poco su</div><div class="a1">{ic("arrow", 70, "#a1a1aa")}</div>
        <div class="a2" style="transform:scaleX(-1)">{ic("arrow", 70, "#a1a1aa")}</div><div class="a2 small" style="font-size:28px">e viceversa</div></div>
      <div class="card acc c2" style="width:560px;text-align:center"><div style="display:flex;justify-content:center">{boxes(4, on=(0,1), size=56)}</div><div class="h3" style="margin-top:26px">Metà delle serie</div></div></div>''')
    return h, [(f"#{b} .c1", T(l_at), "left"), (f"#{b} .a1", T(l_at) + 0.6, "fade"), (f"#{b} .c2", T(r_at), "right"), (f"#{b} .a2", T(vv_at), "fade")]

def study_card(b, T, TE, a, e, chips):
    ch = "".join(f'<span class="chip c{i}">{ic(icn, 30, "#ef4b40")}{t}</span>' for i, (t, icn, at) in enumerate(chips))
    h = W(f'''<div class="card acc pc" style="padding:54px 60px">
      <div class="row" style="justify-content:space-between"><div class="kick">Studio · 2024</div><div class="small">PeerJ</div></div>
      <div style="font:italic 600 44px/1.25 Inter;margin:26px 0 18px;color:#e4e4e7">“Gaining more from doing less? The effects of a one-week deload period during supervised resistance training on muscular adaptations”</div>
      <div class="h4 mut" style="font-style:normal;font-weight:600">Coleman e colleghi, 2024</div>
      <div class="row" style="gap:18px;margin-top:40px;flex-wrap:wrap">{ch}</div></div>''')
    return h, [(f"#{b} .pc", a, "up")] + [(f"#{b} .c{i}", T(at), "pop") for i, (t, icn, at) in enumerate(chips)]

def design(b, T, TE, a, e, rowA_at, rowB_at, gap_at, call_at):
    def row(lbl, cls, stop):
        cells = "".join((f'<div class="wk {cls}{i}" style="width:118px;height:96px;border-radius:14px;{"border:3px dashed #ef4b40;background:repeating-linear-gradient(45deg,rgba(239,75,64,.18) 0 10px,transparent 10px 20px)" if (stop and i == 4) else "background:#e9e9ec"};display:flex;align-items:center;justify-content:center;font:italic 900 34px Saira;color:{"#ef4b40" if (stop and i == 4) else "#0b0b0d"}">{"STOP" if (stop and i == 4) else i + 1}</div>') for i in range(9))
        return f'<div class="row" style="gap:18px"><div class="h4" style="width:260px">{lbl}</div>{cells}</div>'
    h = W(f'''<div class="kick k">9 settimane · allenamento supervisionato</div><div style="height:40px"></div>
      <div class="rA">{row("Continuo", "a", False)}</div><div style="height:30px"></div><div class="rB">{row("Con pausa", "b", True)}</div>
      <div class="row cl" style="gap:20px;margin-top:56px;margin-left:278px"><span class="chip r">≠ meno serie</span><span class="chip r">≠ serie più facili</span><span class="chip w">= sospensione completa</span></div>''')
    an = [(f"#{b} .k", a, "fade"), (f"#{b} .rA .h4", T(rowA_at), "fade"), (f"#{b} .rB .h4", T(rowB_at), "fade")]
    for i in range(9):
        an.append((f"#{b} .a{i}", T(rowA_at) + 0.06 * i, "pop"))
        if i != 4: an.append((f"#{b} .b{i}", T(rowB_at) + 0.06 * i, "pop"))
    an += [(f"#{b} .b4", T(gap_at), "stamp", {"r": 0}), (f"#{b} .cl", T(call_at), "up")]
    return h, an

def result_bars(b, T, TE, a, e, title, kick, bars, verdict, verdict_at, bars_at=None, vcls="w"):
    cols = "".join(f'<div class="col" style="align-items:center;gap:18px;width:300px"><div class="bar br{i}" style="width:200px;height:{hgt}px;background:{c}"></div><div class="h4">{lab}</div></div>' for i, (lab, hgt, c) in enumerate(bars))
    h = W(f'''<div class="row" style="gap:90px;align-items:center">
      <div class="col" style="width:640px;gap:18px"><div class="kick k">{kick}</div><div class="h2 t" style="font-size:76px">{title}</div>
        <div class="vd" style="margin-top:26px"><span class="chip {vcls}" style="font-size:36px;padding:18px 30px">{verdict}</span></div>
        <div class="small nt" style="margin-top:18px">rappresentazione qualitativa dei risultati</div></div>
      <div class="row" style="align-items:flex-end;gap:30px;height:560px;border-bottom:3px solid #3f3f46;padding:0 30px">{cols}</div></div>''')
    t0 = T(bars_at) if bars_at else a + 0.3
    an = [(f"#{b} .k", a, "fade"), (f"#{b} .t", a + 0.05, "up"), (f"#{b} .vd", T(verdict_at), "pop"), (f"#{b} .nt", T(verdict_at) + 0.3, "fade")]
    an += [(f"#{b} .br{i}", t0 + 0.25 * i, "growY") for i in range(len(bars))]
    return h, an

def errore(b, T, TE, a, e, err_at):
    h = W(f'<div class="card q" style="font:italic 700 74px/1.2 Inter;padding:40px 60px;align-self:center">«Ecco, lo scarico non serve.»</div>'
          f'<div style="text-align:center;margin-top:60px"><span class="stamp s" style="font-size:96px">Errore</span></div>', "center")
    return h, [(f"#{b} .q", a, "pop"), (f"#{b} .s", T(err_at), "stamp")]

def says(b, T, TE, a, e, kick, title, items, good=True):
    col, icn = ("#4ade80", "check") if good else ("#ff7068", "x")
    rows = "".join(f'<div class="row it{i}" style="gap:24px;align-items:flex-start"><div style="margin-top:4px">{ic(icn, 50, col, 3)}</div><div style="font:600 44px/1.3 Inter;color:#e4e4e7">{t}</div></div>' for i, (t, at) in enumerate(items))
    h = W(f'<div class="kick k">{kick}</div><div class="h2 t" style="margin:14px 0 44px">{title}</div><div class="col" style="gap:30px">{rows}</div>')
    return h, [(f"#{b} .k", a, "fade"), (f"#{b} .t", a + 0.05, "up")] + [(f"#{b} .it{i}", T(at), "left") for i, (t, at) in enumerate(items)]

def quote(b, T, TE, a, e, text, sub="", sub_at=None, hl=None):
    if hl: text = text.replace(hl, f'<span class="red">{hl}</span>')
    h = W(f'<div style="font:italic 900 220px/0.6 Saira;color:#ef4b40" class="qm">“</div><div class="h2 q" style="font-size:88px;line-height:1.08;max-width:1500px">{text}</div>'
          f'<div class="body sb" style="margin-top:40px">{sub}</div>')
    an = [(f"#{b} .qm", a, "fade"), (f"#{b} .q", a + 0.1, "up")]
    if sub: an.append((f"#{b} .sb", T(sub_at) if sub_at else a + 1, "up"))
    return h, an

def tool(b, T, TE, a, e, rit_at, str_at, first_at):
    cal = '<div style="display:grid;grid-template-columns:repeat(7,46px);gap:8px">' + "".join(f'<div class="box" style="width:46px;height:46px;{"background:#c0241e" if i in (3, 10, 17, 24) else ""}"></div>' for i in range(28)) + "</div>"
    h = W(f'''<div class="row" style="justify-content:center;gap:70px;align-items:stretch">
      <div class="card r1" style="width:640px"><div class="h3"><span class="strk">Rituale a calendario<i></i></span></div><div style="margin-top:30px">{cal}</div><div class="small" style="margin-top:20px">«scarico ogni 4 settimane, a prescindere»</div></div>
      <div class="card acc r2" style="width:640px"><div class="h3">Strumento</div><div class="row" style="margin-top:40px;gap:24px">{ic("sliders", 110, "#ef4b40", 2)}<div class="body" style="color:#e4e4e7">da usare quando serve, per un motivo preciso</div></div></div></div>
      <div class="row fr" style="justify-content:center;margin-top:56px;gap:20px">{ic("q", 54, "#ef4b40")}<div class="h3" style="font-size:44px">Prima: perché le sedute vanno male?</div></div>''')
    return h, [(f"#{b} .r1", T(rit_at), "left"), (f"#{b} .r1 .strk", T(rit_at) + 1.0, "strike"), (f"#{b} .r1", T(str_at) - 0.1, "dim", {"o": 0.4}),
               (f"#{b} .r2", T(str_at), "right"), (f"#{b} .fr", T(first_at), "up")]

CAUSES = [("Condizioni di esecuzione", "sliders"), ("Aumento troppo rapido", "trend"), ("Sonno", "moon"), ("Alimentazione", "food"), ("Stress", "bolt"), ("Variabilità normale", "wave")]
def causes_grid(b, T, TE, a, e, at, focus=None, sub=None):
    tiles = "".join(f'<div class="card tl{i}" style="padding:30px 32px;display:flex;gap:24px;align-items:center"><div class="num" style="font-size:58px;width:50px">{i + 1}</div>{ic(icn, 58, "#ef4b40")}<div class="h3" style="font-size:40px">{t}</div></div>' for i, (t, icn) in enumerate(CAUSES))
    h = W(f'<div class="kick k">Prima di toccare il programma</div><div class="h2" style="margin:14px 0 40px">Possibili spiegazioni</div>'
          f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">{tiles}</div>')
    an = [(f"#{b} .k", a, "fade"), (f"#{b} .h2", a + 0.05, "up")] + [(f"#{b} .tl{i}", T(at) + 0.13 * i, "pop") for i in range(6)]
    return h, an

def technique(b, T, TE, a, e, tech_at, end_at):
    h = W(f'''<div class="kick k">1 · Condizioni di esecuzione</div><div class="h2" style="margin:14px 0 60px">Anche la tecnica conta</div>
      <div class="row" style="gap:36px;justify-content:center">
        <div class="card t1" style="width:520px;text-align:center"><div style="display:flex;justify-content:center">{ic("target", 80, "#ef4b40")}</div><div class="h3" style="margin-top:20px">Esecuzione più pulita e controllata</div></div>
        <div class="t2">{ic("arrow", 70, "#71717a")}</div>
        <div class="card t3" style="width:360px;text-align:center"><div class="h2" style="font-size:76px">Numeri <span class="red">↓</span></div></div>
        <div class="neq t4" style="font-size:90px">≠</div>
        <div class="card t5" style="width:360px;text-align:center"><div class="h2" style="font-size:76px">Forza <span class="red">↓</span></div></div></div>''')
    return h, [(f"#{b} .k", a, "fade"), (f"#{b} .h2", a + 0.05, "up"), (f"#{b} .t1", T(tech_at), "up"), (f"#{b} .t2", T(tech_at) + 0.6, "fade"),
               (f"#{b} .t3", T(tech_at) + 0.9, "pop"), (f"#{b} .t4", T(end_at), "pop"), (f"#{b} .t5", T(end_at) + 0.15, "pop")]

def volume_ramp(b, T, TE, a, e, bars_at, rec_at, fat_at):
    sets = [10, 10, 12, 16, 20, 24]; k = 19          # px per weekly set
    bars = "".join(f'<div class="col" style="align-items:center;gap:14px;width:150px"><div class="bar vb{i}" style="width:120px;height:{s_ * k}px;background:{"#e9e9ec" if s_ <= 15 else "#ef4b40"}"></div>'
                   f'<div class="small" style="font-weight:700">Sett. {i + 1}</div></div>' for i, s_ in enumerate(sets))
    rec_y = 15 * k
    h = f'''<div class="wrap" style="top:90px"><div class="kick k">2 · Lavoro aumentato troppo in fretta</div>
      <div class="row" style="gap:70px;margin-top:30px;align-items:flex-end">
        <div style="position:relative;height:{24 * k + 50}px;display:flex;align-items:flex-end;gap:24px;border-bottom:3px solid #3f3f46;padding:0 20px">{bars}
          <div class="rec" style="position:absolute;left:0;right:0;bottom:{rec_y + 48}px;border-top:6px dashed #4ade80"></div>
          <div class="rect" style="position:absolute;left:10px;bottom:{rec_y + 62}px;font:800 26px Inter;color:#4ade80">capacità di recupero</div></div>
        <div class="col" style="gap:22px;width:520px;margin-bottom:60px"><div class="fatt h3 red" style="font-size:52px">Fatica accumulata</div>
          <div class="body fats">il volume sale più in fretta di quanto riesci a smaltirlo</div></div></div></div>'''
    an = [(f"#{b} .k", a, "fade")] + [(f"#{b} .vb{i}", T(bars_at) + 0.18 * i, "growY", {"d": 0.5}) for i in range(6)]
    an += [(f"#{b} .rec", T(rec_at), "grow"), (f"#{b} .rect", T(rec_at), "fade"), (f"#{b} .fatt", T(fat_at), "pop"), (f"#{b} .fats", T(fat_at) + 0.3, "up")]
    return h, an

def variability(b, T, TE, a, e, line_at, low_at, txt_at):
    ys = [300, 270, 320, 285, 255, 300, 380, 290, 265, 300, 280, 260]
    pts = " ".join(f"{80 + i * 85},{y}" for i, y in enumerate(ys))
    dots = "".join(f'<circle class="dt" cx="{80 + i * 85}" cy="{y}" r="{14 if i == 6 else 9}" fill="{"#ef4b40" if i == 6 else "#e9e9ec"}"/>' for i, y in enumerate(ys))
    h = f'''<div class="wrap" style="top:90px"><div class="kick k">6 · Variabilità normale</div><div class="h2" style="margin:14px 0 10px">Le prestazioni oscillano</div>
      <svg width="1620" height="520" viewBox="0 0 1100 470">
        <line x1="60" y1="292" x2="1060" y2="282" stroke="#4ade80" stroke-width="4" stroke-dasharray="14 10" class="tr"/>
        <polyline class="ln" pathLength="1" stroke-dasharray="1" points="{pts}" fill="none" stroke="#e9e9ec" stroke-width="5" stroke-linejoin="round"/>{dots}
        <g class="lw"><line x1="590" y1="400" x2="590" y2="440" stroke="#ef4b40" stroke-width="3"/><text x="590" y="466" fill="#ef4b40" font-family="Inter" font-weight="800" font-size="30" text-anchor="middle">una seduta peggiore ≠ un problema</text></g>
      </svg></div>'''
    return h, [(f"#{b} .k", a, "fade"), (f"#{b} .h2", a + 0.05, "up"), (f"#{b} .ln", T(line_at), "draw", {"d": 1.6}), (f"#{b} .dt", T(line_at), "fade"),
               (f"#{b} .tr", T(line_at) + 1.2, "fade"), (f"#{b} .lw", T(low_at), "up")]

def checklist(b, T, TE, a, e, title, items, kick=""):
    rows = "".join(f'<div class="row it{i}" style="gap:22px"><div class="cb" style="width:46px;height:46px;border:4px solid #ef4b40;border-radius:10px;flex:none"></div><div style="font:600 42px/1.2 Inter">{t}</div></div>' for i, (t, at) in enumerate(items))
    h = W(f'<div class="kick k">{kick}</div><div class="h2 t" style="margin:14px 0 40px">{title}</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:34px 60px">{rows}</div>')
    return h, [(f"#{b} .k", a, "fade"), (f"#{b} .t", a + 0.05, "up")] + [(f"#{b} .it{i}", T(at), "up") for i, (t, at) in enumerate(items)]

def cause_fix(b, T, TE, a, e, fix_at):
    h = W(f'''<div class="row" style="justify-content:center;gap:40px">
      <div class="card c1" style="width:470px;text-align:center"><div style="display:flex;justify-content:center">{ic("eye", 76, "#ef4b40")}</div><div class="h3" style="margin-top:20px">Causa chiara</div></div>
      <div class="c2">{ic("arrow", 70, "#71717a")}</div>
      <div class="card acc g c3" style="width:470px;text-align:center"><div style="display:flex;justify-content:center">{ic("check", 76, "#4ade80", 3)}</div><div class="h3" style="margin-top:20px">Sistema quella</div></div></div>
      <div style="text-align:center;margin-top:56px" class="c4"><span class="h3 mut"><span class="strk">Scarico automatico<i></i></span></span></div>''', "center")
    return h, [(f"#{b} .c1", a, "pop"), (f"#{b} .c2", a + 0.4, "fade"), (f"#{b} .c3", T(fix_at), "pop"), (f"#{b} .c4", a + 0.6, "fade"), (f"#{b} .c4 .strk", T(fix_at) + 0.4, "strike")]

CASES = [("Caso 1", "Singola seduta negativa", "g", "#4ade80"), ("Caso 2", "Calo ripetuto + recupero difficile", "a", "#f5b31b"), ("Caso 3", "Dolore persistente", "acc", "#ef4b40")]
def cases(b, T, TE, a, e, at, verdicts=None):
    vs = verdicts or [None, None, None]
    cards = "".join(f'<div class="card {cls} cs{i}" style="width:500px;min-height:330px;padding:44px 40px"><div class="kick" style="color:{c}">{k}</div><div class="h3" style="margin-top:20px;font-size:50px">{t}</div>'
                    + (f'<div class="vd{i}" style="margin-top:36px"><span class="chip {["g","a","r"][i]}" style="font-size:30px">{vs[i][0]}</span></div>' if vs[i] else "") + "</div>"
                    for i, (k, t, cls, c) in enumerate(CASES))
    h = W(f'<div class="row" style="justify-content:center;gap:34px;align-items:stretch">{cards}</div>')
    an = [(f"#{b} .cs{i}", (T(at[i]) if isinstance(at, list) else T(at) + 0.18 * i), "up") for i in range(3)]
    if verdicts: an += [(f"#{b} .vd{i}", T(vs[i][1]), "pop") for i in range(3)]
    return h, an

def case1_log(b, T, TE, a, e, today_at, rest_at):
    h = W(f'''<div class="kick" style="color:#4ade80">Caso 1</div><div class="h2" style="margin:12px 0 40px">Singola seduta negativa</div>
      <table class="tb"><tr><th>Giorno</th><th>Esercizio</th><th>Di solito</th><th>Oggi</th></tr>
      <tr class="r1"><td>Lunedì</td><td>Panca piana</td><td>8 rip.</td><td class="td"><span class="red" style="font-size:44px">6 rip.</span></td></tr>
      <tr class="r2"><td>Mercoledì</td><td>Squat</td><td>6 rip.</td><td><span class="green">6 rip. ✓</span></td></tr>
      <tr class="r3"><td>Venerdì</td><td>Rematore</td><td>8 rip.</td><td><span class="green">8 rip. ✓</span></td></tr></table>''')
    return h, [(f"#{b} .r1", a + 0.2, "left"), (f"#{b} .td span", T(today_at), "pop"), (f"#{b} .r2", T(rest_at), "left"), (f"#{b} .r3", T(rest_at) + 0.25, "left")]

def case1_steps(b, T, TE, a, e, s1, s2, s3, noise_at):
    st = [("Annota il dato", "note", s1), ("Cerca una causa evidente", "eye", s2), ("Riprova alla seduta dopo", "loop", s3)]
    cells = "".join(f'<div class="card g st{i}" style="width:470px;padding:36px 34px"><div class="row" style="gap:18px"><div class="num" style="color:#4ade80">{i + 1}</div>{ic(icn, 56, "#4ade80")}</div><div class="h3" style="margin-top:22px;font-size:42px">{t}</div></div>' for i, (t, icn, at) in enumerate(st))
    h = W(f'<div class="kick" style="color:#4ade80">Caso 1 · cosa fare</div><div class="row" style="gap:30px;margin-top:40px">{cells}</div>'
          f'<div class="row nz" style="margin-top:56px;gap:30px;justify-content:center"><span class="h3">Torni ai tuoi numeri?</span><span class="stamp g" style="font-size:64px">Era rumore</span></div>')
    return h, [(f"#{b} .st{i}", T(x[2]), "up") for i, x in enumerate(st)] + [(f"#{b} .nz", T(noise_at) - 0.5, "pop")]

def case2_chart(b, T, TE, a, e, line_at, sig):
    def line(ys, col, cls): return f'<polyline class="{cls}" pathLength="1" stroke-dasharray="1" points="{" ".join(f"{70 + i * 135},{y}" for i, y in enumerate(ys))}" fill="none" stroke="{col}" stroke-width="6" stroke-linejoin="round"/>'
    chart = (f'<svg width="760" height="470" viewBox="0 0 760 470"><line x1="50" y1="420" x2="740" y2="420" stroke="#3f3f46" stroke-width="3"/>'
             + line([120, 115, 150, 185, 220], "#e9e9ec", "l1") + line([180, 190, 215, 250, 290], "#f5b31b", "l2") + line([250, 245, 280, 320, 350], "#ef4b40", "l3")
             + "".join(f'<text x="{70 + i * 135}" y="455" fill="#a1a1aa" font-family="Inter" font-weight="700" font-size="22" text-anchor="middle">{w}</text>' for i, w in enumerate(["sett. 1", "sett. 2", "sett. 3", "sett. 4", "sett. 5"])) + "</svg>")
    chips = "".join(f'<span class="chip a sg{i}" style="font-size:32px">{ic(icn, 32, "#f5b31b")}{t}</span>' for i, (t, icn, at) in enumerate(sig))
    h = W(f'''<div class="kick amber">Caso 2</div><div class="h2" style="margin:12px 0 30px;font-size:72px">Calo ripetuto + recupero difficile</div>
      <div class="row" style="gap:60px;align-items:center"><div class="card ch" style="padding:20px">{chart}</div><div class="col" style="gap:24px;align-items:flex-start">{chips}</div></div>''')
    an = [(f"#{b} .ch", a + 0.1, "up")] + [(f"#{b} .l{i + 1}", T(line_at) + 0.25 * i, "draw", {"d": 1.4}) for i in range(3)]
    an += [(f"#{b} .sg{i}", T(at), "right") for i, (t, icn, at) in enumerate(sig)]
    return h, an

def two_steps(b, T, TE, a, e, kick, kcol, s1, s1_at, s2, s2_at, chips1=()):
    ch = "".join(f'<span class="chip c{i}">{t}</span>' for i, (t, at) in enumerate(chips1))
    h = W(f'''<div class="kick" style="color:{kcol}">{kick}</div>
      <div class="row" style="gap:40px;margin-top:44px;align-items:stretch">
        <div class="card a s1" style="width:720px;padding:44px"><div class="num amber">1</div><div class="h3" style="margin:18px 0 26px">{s1}</div><div class="row" style="gap:14px;flex-wrap:wrap">{ch}</div></div>
        <div class="ar" style="align-self:center">{ic("arrow", 70, "#71717a")}</div>
        <div class="card a s2" style="width:720px;padding:44px"><div class="num amber">2</div><div class="h3" style="margin:18px 0 0">{s2}</div></div></div>''')
    an = [(f"#{b} .s1", T(s1_at), "up"), (f"#{b} .ar", T(s2_at) - 0.3, "fade"), (f"#{b} .s2", T(s2_at), "up")]
    an += [(f"#{b} .c{i}", T(at), "pop") for i, (t, at) in enumerate(chips1)]
    return h, an

def case3_paths(b, T, TE, a, e, mod_at, pro_at):
    h = W(f'''<div class="kick">Caso 3 · dolore persistente</div><div class="h2" style="margin:12px 0 44px">Non solo fatica</div>
      <div class="row" style="gap:40px;align-items:stretch">
        <div class="card p1" style="width:780px;padding:44px"><div class="row" style="gap:20px">{ic("sliders", 60, "#a1a1aa")}<div class="h3">Modifica l'allenamento</div></div>
          <div class="body" style="margin-top:22px">per esempio evitando i movimenti che provocano dolore</div></div>
        <div class="card acc p2" style="width:780px;padding:44px;border-color:rgba(239,75,64,.5)"><div class="row" style="gap:20px">{ic("med", 60, "#ef4b40")}<div class="h3">Fatti valutare</div></div>
          <div class="body" style="margin-top:22px;color:#e4e4e7">da un professionista sanitario: un medico o un fisioterapista</div></div></div>''')
    return h, [(f"#{b} .p1", T(mod_at), "left"), (f"#{b} .p2", T(pro_at), "right"), (f"#{b} .p1", T(pro_at) + 0.3, "dim", {"o": 0.55})]

def loop_back(b, T, TE, a, e, back_at):
    h = W(f'''<div class="row" style="justify-content:center;gap:30px">
      <div class="card c1" style="width:470px;text-align:center"><div class="h3">Meno serie</div><div class="small" style="margin-top:10px">ti senti meglio per una settimana</div></div>
      <div class="a1">{ic("arrow", 60, "#71717a")}</div>
      <div class="card acc c2" style="width:470px;text-align:center"><div class="h3">La causa rimane</div></div>
      <div class="a2">{ic("arrow", 60, "#71717a")}</div>
      <div class="card acc c3" style="width:470px;text-align:center"><div class="row" style="justify-content:center;gap:14px">{ic("loop", 54, "#ef4b40")}<div class="h3">Il problema torna</div></div></div></div>''', "center")
    return h, [(f"#{b} .c1", a + 0.1, "pop"), (f"#{b} .a1", T(back_at) - 0.4, "fade"), (f"#{b} .c2", T(back_at) - 0.3, "pop"), (f"#{b} .a2", T(back_at) + 0.6, "fade"), (f"#{b} .c3", T(back_at) + 0.8, "pop")]

def program(b, T, TE, a, e, rows_at, red_at, rir_at, same_at, title_at):
    rows = [("Squat", "4", "6–8", "1–2", False), ("Panca piana", "4", "6–8", "1–2", True), ("Rematore", "4", "8–10", "1–2", True), ("Complementari", "2–3", "10–12", "1–2", False)]
    trs = "".join(f'<tr class="r{i}"><td style="width:420px">{n}</td><td style="width:200px"><span class="sv{i}">{s}</span>' + (f'<span class="sn{i} red" style="margin-left:18px">→ 2</span>' if cut else "") +
                  f'</td><td style="width:220px">{rp}</td><td style="width:280px"><span class="rv{i}">{rr}</span><span class="rn{i} green" style="margin-left:16px">→ 3–4</span></td></tr>' for i, (n, s, rp, rr, cut) in enumerate(rows))
    h = W(f'''<div class="row" style="justify-content:space-between;align-items:flex-end"><div><div class="kick k">Esempio illustrativo · caso 2</div><div class="h2 tt" style="margin-top:12px;font-size:72px"><span class="t1">Programma attuale</span><span class="t2 red" style="position:absolute;left:0;opacity:0">Settimana di scarico</span></div></div>
      <div class="sm row" style="gap:16px"><span class="chip g">✓ stessi esercizi</span><span class="chip g">✓ carichi simili</span></div></div>
      <table class="tb" style="margin-top:30px"><tr><th>Esercizio</th><th>Serie</th><th>Ripetizioni</th><th>In riserva</th></tr>{trs}</table>''')
    an = [(f"#{b} .k", a, "fade"), (f"#{b} .t1", a + 0.05, "up"), (f"#{b} .sm", T(same_at), "pop")]
    an += [(f"#{b} .r{i}", T(rows_at[i]), "left") for i in range(4)]
    for i in (1, 2): an += [(f"#{b} .sn{i}", T(red_at) + 0.15 * i, "pop"), (f"#{b} .sv{i}", T(red_at) + 0.15 * i, "dim", {"o": 0.4})]
    for i in range(4): an += [(f"#{b} .rn{i}", T(rir_at) + 0.1 * i, "pop"), (f"#{b} .rv{i}", T(rir_at) + 0.1 * i, "dim", {"o": 0.4})]
    an += [(f"#{b} .t1", T(title_at), "out"), (f"#{b} .t2", T(title_at) + 0.05, "to", {"opacity": 1, "duration": 0.4})]
    return h, an

def stop_vs_reduce(b, T, TE, a, e, stop_at, red_at):
    h = W(f'''<div class="row" style="justify-content:center;gap:50px;align-items:stretch">
      <div class="card s1" style="width:700px;padding:44px"><div class="row" style="gap:18px">{ic("pause", 60, "#a1a1aa", 3)}<div class="h3">Stop completo</div></div>
        <div class="col" style="gap:18px;margin-top:30px"><span class="chip">Ipertrofia: nessun vantaggio</span><span class="chip r">Forza: guadagni ridotti</span></div><div class="small" style="margin-top:20px">dallo studio del 2024</div></div>
      <div class="card acc g s2" style="width:700px;padding:44px"><div class="row" style="gap:18px">{ic("down", 60, "#4ade80")}<div class="h3">Ridurre, senza azzerare</div></div>
        <div class="col" style="gap:18px;margin-top:30px"><span class="chip g">✓ Stimolo mantenuto</span><span class="chip g">✓ Fatica più bassa</span></div></div></div>''')
    return h, [(f"#{b} .s1", T(stop_at), "left"), (f"#{b} .s2", T(red_at), "right")]

def big(b, T, TE, a, e, text, kick="", hl=None):
    if hl: text = text.replace(hl, f'<span class="mark mk">{hl}<i></i></span>')
    h = W(f'<div class="kick k">{kick}</div><div class="h1 t" style="margin-top:22px;font-size:118px">{text}</div>', "center")
    an = [(f"#{b} .k", a, "fade"), (f"#{b} .t", a + 0.05, "up")]
    if hl: an.append((f"#{b} .mk", a + 0.7, "mark"))
    return h, an

def sliders(b, T, TE, a, e, p1_at, p2_at, f_at):
    def sl(lbl, cls): return (f'<div class="col" style="gap:16px"><div class="h4">{lbl}</div><div style="position:relative;width:900px;height:14px;border-radius:7px;background:#27272a">'
                             f'<div class="{cls}f" style="position:absolute;left:0;top:0;bottom:0;width:100%;border-radius:7px;background:#ef4b40;transform-origin:0 50%"></div>'
                             f'<div class="{cls}k" style="position:absolute;top:-17px;left:0;width:48px;height:48px;margin-left:-24px;border-radius:50%;background:#fff;box-shadow:0 4px 14px rgba(0,0,0,.5)"></div></div></div>')
    fac = [("Quanto è marcato il calo", "down"), ("Quanto lavoro facevi prima", "data"), ("Cosa succede fuori dalla palestra", "bolt")]
    fs = "".join(f'<span class="chip f{i}" style="font-size:28px">{ic(icn, 30, "#ef4b40")}{t}</span>' for i, (t, icn) in enumerate(fac))
    h = W(f'''<div class="row" style="gap:80px;align-items:center"><div class="col" style="gap:50px">{sl("Quanto ridurre", "q")}{sl("Per quanto tempo", "d")}</div>
      <div class="col" style="gap:14px"><div class="row who" style="gap:14px">{ic("user", 54, "#fff")}<span class="h4 wl">Qualcuno</span></div></div></div>
      <div class="kick fk" style="margin-top:60px">Dipende da</div><div class="row" style="gap:18px;margin-top:20px">{fs}</div>''')
    an = [(f"#{b} .qk", a, "set", {"x": 270}), (f"#{b} .dk", a, "set", {"x": 270}), (f"#{b} .qf", a, "set", {"scaleX": 0.3}), (f"#{b} .df", a, "set", {"scaleX": 0.3}),
          (f"#{b} .qk", T(p1_at), "to", {"x": 180, "duration": 0.6, "ease": "power2.inOut"}), (f"#{b} .qf", T(p1_at), "to", {"scaleX": 0.2, "duration": 0.6, "ease": "power2.inOut"}),
          (f"#{b} .dk", T(p1_at) + 0.2, "to", {"x": 150, "duration": 0.6, "ease": "power2.inOut"}), (f"#{b} .df", T(p1_at) + 0.2, "to", {"scaleX": 0.17, "duration": 0.6, "ease": "power2.inOut"}),
          (f"#{b} .who", T(p1_at), "fade"),
          (f"#{b} .wl", T(p2_at), "set", {"textContent": "Qualcun altro"}), (f"#{b} .who", T(p2_at), "pulse"),
          (f"#{b} .qk", T(p2_at), "to", {"x": 640, "duration": 0.7, "ease": "power2.inOut"}), (f"#{b} .qf", T(p2_at), "to", {"scaleX": 0.71, "duration": 0.7, "ease": "power2.inOut"}),
          (f"#{b} .dk", T(p2_at) + 0.2, "to", {"x": 700, "duration": 0.7, "ease": "power2.inOut"}), (f"#{b} .df", T(p2_at) + 0.2, "to", {"scaleX": 0.78, "duration": 0.7, "ease": "power2.inOut"}),
          (f"#{b} .fk", T(f_at), "fade")]
    an += [(f"#{b} .f{i}", T(f_at) + 0.35 * i + 0.1, "pop") for i in range(3)]
    return h, an

def nomagic(b, T, TE, a, e, p_at, d_at):
    h = W(f'''<div class="row" style="justify-content:center;gap:60px">
      <div class="col n1" style="align-items:center;gap:26px"><div class="h1" style="font-size:150px"><span class="strk">−40%<i></i></span></div><div class="h3 mut">percentuale magica</div></div>
      <div class="col n2" style="align-items:center;gap:26px"><div class="h1" style="font-size:150px"><span class="strk">7 giorni<i></i></span></div><div class="h3 mut">durata standard</div></div></div>''', "center")
    return h, [(f"#{b} .n1", T(p_at), "pop"), (f"#{b} .n1 .strk", T(p_at) + 0.5, "strike"), (f"#{b} .n2", T(d_at), "pop"), (f"#{b} .n2 .strk", T(d_at) + 0.5, "strike")]

MON = [("Qualità delle sedute", "eye", ["Più fresco all'inizio?", "Carichi di nuovo normali?", "Tecnica più stabile?"]),
       ("Prestazioni", "trend", ["Numeri tornati ai livelli di prima?", "O li superano?"]),
       ("Disponibilità", "batt", ["Di nuovo voglia di allenarti?", "Pronto al volume pieno?"])]
def monitors(b, T, TE, a, e, at, qs):
    cards = ""
    for i, (t, icn, q) in enumerate(MON):
        ql = "".join(f'<div class="pl q{i}{j}" style="font:600 30px/1.3 Inter;color:#d4d4d8;margin-top:14px">· {x}</div>' for j, x in enumerate(q))
        cards += f'<div class="card acc m{i}" style="width:500px;min-height:470px;padding:40px 36px"><div class="row" style="gap:18px"><div class="num">{i + 1}</div>{ic(icn, 56, "#ef4b40")}</div><div class="h3" style="margin:22px 0 14px">{t}</div>{ql}</div>'
    h = W(f'<div class="kick k">Cosa osservare dopo</div><div class="row" style="gap:34px;margin-top:36px;align-items:stretch">{cards}</div>')
    an = [(f"#{b} .k", a, "fade")] + [(f"#{b} .m{i}", T(at[i]), "up") for i in range(3)]
    for i, q in enumerate(qs):
        an += [(f"#{b} .q{i}{j}", T(x), "fade") for j, x in enumerate(q)]
    return h, an

def confirm(b, T, TE, a, e, ok_at):
    ups = "".join(f'<div class="card u{i}" style="width:420px;text-align:center;padding:30px"><div class="h4">{t}</div><div style="display:flex;justify-content:center;margin-top:10px">{ic("trend", 70, "#4ade80")}</div></div>' for i, (t, _, _) in enumerate(MON))
    h = W(f'<div class="row" style="justify-content:center;gap:30px">{ups}</div><div class="ok" style="text-align:center;margin-top:60px"><span class="stamp g" style="font-size:74px">Ipotesi confermata</span>'
          f'<div class="body" style="margin-top:30px">c\'era fatica accumulata, e ridurla ha aiutato</div></div>', "center")
    return h, [(f"#{b} .u{i}", a + 0.15 * i, "up") for i in range(3)] + [(f"#{b} .ok", T(ok_at), "pop")]

def reconsider(b, T, TE, a, e, alt_at):
    alts = [("Sonno", "moon", "s7f:sonno"), ("Alimentazione", "food", "s7f:l'alimentazione"), ("Stress", "bolt", "s7f:stress"), ("Altro", "q", "s7f:qualcos")]
    ch = "".join(f'<div class="card al{i}" style="width:330px;text-align:center;padding:30px"><div style="display:flex;justify-content:center">{ic(icn, 64, "#ef4b40")}</div><div class="h3" style="margin-top:14px;font-size:40px">{t}</div></div>' for i, (t, icn, at) in enumerate(alts))
    h = W(f'''<div class="row t" style="gap:26px;justify-content:center">{ic("loop", 80, "#ef4b40")}<div class="h2">Niente cambia? <span class="red">Riconsidera</span></div></div>
      <div class="row" style="justify-content:center;gap:24px;margin-top:60px">{ch}</div>''', "center")
    return h, [(f"#{b} .t", a, "up")] + [(f"#{b} .al{i}", T(at), "pop") for i, (t, icn, at) in enumerate(alts)]

def noid(b, T, TE, a, e, a_at, b_at):
    h = W(f'''<div class="h2 t" style="text-align:center;font-size:72px">Lo scarico <span class="red">non identifica</span> la causa</div>
      <div class="row" style="justify-content:center;gap:50px;margin-top:56px;align-items:stretch">
        <div class="card sa" style="width:700px;padding:40px"><div class="h4 green">Ti senti meglio</div><div class="h3" style="margin:16px 0 22px">Era l'allenamento?</div>
          <div class="row" style="gap:14px"><span class="chip">o hai solo dormito di più?</span></div></div>
        <div class="card acc sb" style="width:700px;padding:40px"><div class="h4 red">Non ti senti meglio</div><div class="h3" style="margin:16px 0 22px">Lo scarico non ti dice perché</div>
          <div class="row" style="gap:14px">{ic("q", 54, "#ef4b40")}</div></div></div>''', "center")
    return h, [(f"#{b} .t", a, "up"), (f"#{b} .sa", T(a_at), "left"), (f"#{b} .sb", T(b_at), "right")]

def loop4(b, T, TE, a, e, nodes):
    lab = [("Dati", "data", "seduta per seduta"), ("Contesto", "eye", "sonno · cibo · stress · lavoro"), ("Decisione", "target", "scelta per un motivo"), ("Verifica", "check", "ha funzionato?")]
    pos = [(560, 40), (1050, 270), (560, 500), (70, 270)]
    nd = "".join(f'<div class="card n{i}" style="position:absolute;left:{x}px;top:{y}px;width:500px;padding:26px 30px;display:flex;gap:20px;align-items:center">{ic(icn, 60, "#ef4b40")}<div><div class="h3" style="font-size:44px">{t}</div><div class="small">{s}</div></div></div>' for i, ((t, icn, s), (x, y)) in enumerate(zip(lab, pos)))
    ring = '<svg width="1620" height="740" style="position:absolute;left:0;top:0"><ellipse class="rg" pathLength="1" stroke-dasharray="1" cx="810" cy="370" rx="560" ry="250" fill="none" stroke="#3f3f46" stroke-width="5"/></svg>'
    h = f'<div class="wrap" style="display:block"><div style="position:relative;width:1620px;height:740px;margin-top:10px">{ring}{nd}</div></div>'
    an = [(f"#{b} .rg", a, "draw", {"d": 1.4})] + [(f"#{b} .n{i}", T(nodes[i]), "pop") for i in range(4)]
    return h, an

def lbsystem(b, T, TE, a, e, f_at):
    feats = [("Programmazione", "sui tuoi dati", "data"), ("App", "registri ogni seduta e vedi l'andamento", "phone"), ("Assistenza diretta", "valutiamo insieme il contesto e decidiamo", "chat")]
    fl = "".join(f'<div class="card acc f{i}" style="width:820px;padding:30px 36px;display:flex;gap:26px;align-items:center">{ic(icn, 62, "#ef4b40")}<div><div class="h3" style="font-size:44px">{t}</div><div class="small" style="font-size:28px;margin-top:6px">{s}</div></div></div>' for i, (t, s, icn) in enumerate(feats))
    h = f'''<div class="wrap" style="left:130px;right:auto;width:900px"><div class="lg">{lbpill(70)}</div><div class="kick" style="margin-top:30px">Il processo LB System</div>
      <div class="col" style="gap:20px;margin-top:26px">{fl}</div></div>
      {phone_app()}'''
    return h, [(f"#{b} .lg", a, "left"), (f"#{b} .phfr", a + 0.2, "up"), (f"#{b} .apl", T(f_at[1]), "draw", {"d": 2.2}), (f"#{b} .apd", T(f_at[1]) + 0.4, "fade")] + \
           [(f"#{b} .f{i}", T(f_at[i]), "left") for i in range(3)] + [(f"#{b} .ar{i}", T(f_at[1]) + 0.8 + 0.25 * i, "left") for i in range(4)] + [(f"#{b} .apb", T(f_at[2]) + 0.3, "pulse")]

def phone_app():
    pts = [8, 8, 9, 8, 6, 6, 7, 8, 9]; X = lambda i: 30 + i * 47; Y = lambda v: 210 - (v - 5) * 34
    poly = " ".join(f"{X(i)},{Y(v)}" for i, v in enumerate(pts))
    dots = "".join(f'<circle cx="{X(i)}" cy="{Y(v)}" r="6" fill="{"#ef4b40" if i in (4, 5) else "#fff"}"/>' for i, v in enumerate(pts))
    rows = [("Lun · Squat", "4 × 6 · 2 in riserva", "#22c55e"), ("Mer · Panca", "2 × 8 · 3 in riserva", "#f5b31b"), ("Ven · Rematore", "2 × 8 · 3 in riserva", "#f5b31b"), ("Sonno medio", "6 h 40'", "#a1a1aa")]
    rl = "".join(f'<div class="ar{i}" style="display:flex;align-items:center;gap:12px;background:#1a1a1f;border-radius:16px;padding:14px 16px;margin-top:10px"><span style="width:12px;height:12px;border-radius:50%;background:{c}"></span>'
                 f'<span style="font:700 17px Inter;color:#fff;flex:1;white-space:nowrap">{a}</span><span style="font:600 14px Inter;color:#a1a1aa;white-space:nowrap">{b}</span></div>' for i, (a, b, c) in enumerate(rows))
    return f'''<div class="phfr" style="position:absolute;left:1240px;top:96px;width:440px;height:880px;border-radius:56px;background:#050506;border:3px solid #3a3a40;box-shadow:0 40px 80px rgba(0,0,0,.6);padding:22px">
      <div style="width:100%;height:100%;border-radius:38px;background:#0f0f12;overflow:hidden;padding:44px 22px 20px">
        <div style="display:flex;align-items:center;justify-content:space-between"><span class="lbpill" style="padding:6px 16px 6px 12px;gap:8px">{lbmark(30)}<b style="font-size:30px">LB</b></span>
          <div style="text-align:right"><div style="font:600 15px Inter;color:#a1a1aa">Ciao Luca</div><div style="font:800 18px Inter">Settimana 6</div></div></div>
        <div style="background:#1a1a1f;border-radius:22px;margin-top:20px;padding:18px 16px 8px">
          <div style="font:800 21px Inter">Andamento panca</div><div style="font:600 14px Inter;color:#a1a1aa">ripetizioni a 80 kg</div>
          <svg width="370" height="240" viewBox="0 0 410 240"><rect x="{X(3.5)}" y="20" width="{X(5.5) - X(3.5)}" height="210" fill="rgba(192,36,30,.18)"/>
            <text x="{X(3.6)}" y="36" fill="#ef4b40" font-family="Inter" font-weight="800" font-size="15">SCARICO</text>
            <polyline class="apl" pathLength="1" stroke-dasharray="1" points="{poly}" fill="none" stroke="#fff" stroke-width="4" stroke-linejoin="round"/><g class="apd">{dots}</g></svg></div>
        {rl}
        <div class="apb" style="margin-top:16px;background:#c0241e;border-radius:999px;text-align:center;font:800 19px Inter;padding:14px">Scrivi al coach</div>
      </div></div>'''

def endcard(b, T, TE, a, e, nexus_at, sub_at):
    h = f'''<div class="wrap center" style="top:100px">
      <div class="lg">{lbpill(110)}</div><div class="h2 t" style="margin-top:40px;font-size:76px">Smetti di indovinare. <span class="red">Inizia a decidere.</span></div>
      <div class="row ln" style="justify-content:center;gap:18px;margin-top:34px"><span class="chip w" style="font-size:34px;padding:18px 32px">Link a LB System nella descrizione ↓</span></div>
      <div class="row nx" style="justify-content:center;gap:30px;margin-top:60px"><span class="h4 mut">Allenati con me da</span><img src="assets/img/nexus-dark.png" style="width:440px" alt="NEXUS Private Gym"/></div>
      <div class="sb" style="margin-top:46px"><span class="sbb" style="display:inline-flex;align-items:center;gap:16px;background:#c0241e;color:#fff;font:800 40px/1 Inter;padding:22px 44px;border-radius:14px">▶ Iscriviti</span></div></div>'''
    return h, [(f"#{b} .lg", a, "pop"), (f"#{b} .t", a + 0.3, "up"), (f"#{b} .ln", a + 0.8, "up"), (f"#{b} .nx", T(nexus_at), "up"), (f"#{b} .sb", T(sub_at), "pop"),
               (f"#{b} .sbb", T(sub_at) + 0.6, "to", {"backgroundColor": "#3f3f46", "duration": 0.25}), (f"#{b} .sbb", T(sub_at) + 0.6, "pulse")]

# ---------------- pop-ups ----------------
def pop_card(pid, T, TE, a, e, title, lines=(), icon=None):
    ls = "".join(f'<div class="pl l{i}"><span class="d"></span><span>{t}</span></div>' for i, (t, at) in enumerate(lines))
    ih = f'<div style="margin-bottom:14px">{ic(icon, 52, "#ef4b40")}</div>' if icon else ""
    return f'<div class="pc">{ih}<div class="pt">{title}</div>{ls}</div>', [(f"#{pid} .l{i}", T(at), "left") for i, (t, at) in enumerate(lines)]

def pop_bubble(pid, T, TE, a, e, text):
    return f'<div class="pc bubble">{text}<i></i><i></i></div>', []
