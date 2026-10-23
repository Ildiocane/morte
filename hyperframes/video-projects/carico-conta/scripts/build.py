# Builds index.html from scripts/index.tpl.html + assets/captions.json (scripts/captions.py) + the SFX cue list.
# The take is used as is (no cuts): every time below is a time in assets/face.mp4.
import json, subprocess
caps = json.load(open("assets/captions.json"))
DUR = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", "assets/face.mp4"], capture_output=True, text=True).stdout.strip()

# LB System mark (same geometry as the YouTube build): grey outline + NEXUS red core
SEG = [((50, 0), (100, 58)), ((6, 4), (94, 114)), ((0, 58), (50, 120)), ((94, 4), (6, 114)), ((50, 0), (0, 58)), ((100, 58), (50, 120))]
LB = "".join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#c2c2c2" stroke-width="22" stroke-linecap="round"/>'
             f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#a8171a" stroke-width="10" stroke-linecap="round"/>' for a, b in SEG)

# caption words shown in NEXUS red
KEYS = ["CARICO", "FORZA", "IPERTROFIA", "LINEARE", "FORTE", "MUSCOLO", "MUSCOLARE", "ROM", "MICROCARICHI", "CHILO", "IMPORTANTI",
        "4 AI 10", "RECUPERA", "RECUPERI", "BASTA", "TECNICA", "CRESCERAI"]

LEN = {"whoosh.mp3": 0.57, "swipe.mp3": 1.05, "pop.mp3": 0.72, "click.wav": 0.45, "slam.mp3": 1.22, "sparkle.mp3": 2.03, "glitch.mp3": 1.2}
VOL = {"whoosh.mp3": 0.18, "swipe.mp3": 0.12, "pop.mp3": 0.14, "click.wav": 0.16, "slam.mp3": 0.15, "sparkle.mp3": 0.13, "glitch.mp3": 0.12}
SFX = [("swipe.mp3", 0.3), ("slam.mp3", 2.35), ("pop.mp3", 3.0), ("pop.mp3", 6.65),
       ("swipe.mp3", 8.8), ("click.wav", 9.89), ("click.wav", 11.33), ("click.wav", 12.88),
       ("whoosh.mp3", 13.8), ("glitch.mp3", 14.07), ("pop.mp3", 14.6), ("glitch.mp3", 16.62), ("slam.mp3", 18.58), ("swipe.mp3", 18.86), ("slam.mp3", 19.51), ("whoosh.mp3", 19.9),
       ("pop.mp3", 20.24), ("slam.mp3", 25.71), ("swipe.mp3", 26.33),
       ("swipe.mp3", 29.66), ("slam.mp3", 33.54), ("pop.mp3", 34.95), ("slam.mp3", 35.63),
       ("click.wav", 36.94), ("click.wav", 39.24), ("click.wav", 40.88), ("slam.mp3", 44.14), ("slam.mp3", 45.08),
       ("whoosh.mp3", 45.33), ("glitch.mp3", 45.6), ("swipe.mp3", 45.9), ("slam.mp3", 47.55), ("slam.mp3", 48.71), ("click.wav", 49.7), ("click.wav", 50.14),
       ("glitch.mp3", 52.6), ("whoosh.mp3", 53.2),
       ("swipe.mp3", 55.65), ("pop.mp3", 57.45), ("slam.mp3", 59.35)]
for (_, a), (_, b) in zip(SFX, SFX[1:]): assert b - a >= 0.25, (a, b)        # one SFX per beat, no double hits
tags = [f'<audio id="sfx{k}" src="assets/sfx/{f}" data-start="{t}" data-duration="{min(LEN[f], float(DUR) - t):.2f}" data-track-index="{10 + k}" data-volume="{VOL[f]}"></audio>'
        for k, (f, t) in enumerate(SFX)]
tags.append(f'<audio id="music" src="assets/music.mp3" data-start="0" data-duration="{DUR}" data-track-index="2" data-volume="0.04"></audio>')
s = (open("scripts/index.tpl.html").read().replace("__DUR__", DUR).replace("__CAPS__", json.dumps(caps, ensure_ascii=False))
     .replace("__SFX__", "\n      ".join(tags)).replace("__LBMARK__", LB).replace("__KEYS__", json.dumps(KEYS)))
open("index.html", "w").write(s); print(len(caps), "captions,", len(SFX), "sfx, dur", DUR)
