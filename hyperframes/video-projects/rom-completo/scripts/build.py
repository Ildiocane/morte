# Builds index.html from scripts/index.tpl.html + assets/captions.json (scripts/captions.py) + the SFX cue list.
# All times are edited-time seconds (assets/edit.mp4).
import json, subprocess
caps = json.load(open("assets/captions.json"))
DUR = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", "assets/edit.mp4"], capture_output=True, text=True).stdout.strip()
LEN = {"whoosh.mp3": 0.57, "swipe.mp3": 1.05, "pop.mp3": 0.72, "click.wav": 0.45, "slam.mp3": 1.22, "sparkle.mp3": 2.03}
VOL = {"whoosh.mp3": 0.18, "swipe.mp3": 0.12, "pop.mp3": 0.14, "click.wav": 0.16, "slam.mp3": 0.15, "sparkle.mp3": 0.14}
SFX = [("pop.mp3", 0.98), ("slam.mp3", 4.87), ("pop.mp3", 7.2), ("swipe.mp3", 9.75), ("slam.mp3", 14.12),
       ("pop.mp3", 17.14), ("click.wav", 19.21), ("slam.mp3", 20.26), ("pop.mp3", 22.29),
       ("whoosh.mp3", 23.0), ("slam.mp3", 23.63), ("click.wav", 24.99), ("click.wav", 26.05), ("slam.mp3", 27.15),
       ("whoosh.mp3", 27.93), ("click.wav", 28.74), ("pop.mp3", 30.62), ("slam.mp3", 31.77), ("click.wav", 33.35), ("sparkle.mp3", 34.2),
       ("whoosh.mp3", 36.3), ("swipe.mp3", 38.46), ("swipe.mp3", 39.31),
       ("pop.mp3", 41.5), ("slam.mp3", 44.84), ("pop.mp3", 46.8), ("swipe.mp3", 50.1), ("click.wav", 52.63), ("slam.mp3", 56.12),
       ("whoosh.mp3", 56.98), ("click.wav", 57.5), ("click.wav", 58.03), ("click.wav", 60.28), ("slam.mp3", 61.67),
       ("slam.mp3", 64.57), ("pop.mp3", 66.95), ("click.wav", 67.38), ("pop.mp3", 68.74), ("sparkle.mp3", 69.4)]
for (_, a), (_, b) in zip(SFX, SFX[1:]): assert b - a >= 0.25, (a, b)        # one SFX per beat, no double hits
tags = [f'<audio id="sfx{k}" src="assets/sfx/{f}" data-start="{t}" data-duration="{min(LEN[f], float(DUR) - t):.2f}" data-track-index="{10 + k}" data-volume="{VOL[f]}"></audio>'
        for k, (f, t) in enumerate(SFX)]
tags.append(f'<audio id="music" src="assets/music.mp3" data-start="0" data-duration="{DUR}" data-track-index="2" data-volume="0.045"></audio>')
s = open("scripts/index.tpl.html").read().replace("__DUR__", DUR).replace("__CAPS__", json.dumps(caps, ensure_ascii=False)).replace("__SFX__", "\n      ".join(tags))
open("index.html", "w").write(s); print(len(caps), "captions,", len(SFX), "sfx, dur", DUR)
