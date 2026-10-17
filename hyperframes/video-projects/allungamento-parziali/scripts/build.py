# Generate index.html from scripts/index.tpl.html + captions + SFX list.
import json
caps = json.load(open('assets/captions-final.json'))
merged = []
for c in caps:  # merge the too-short "Quindi," chunk into "praticamente?"
    if c[2] == 'praticamente?' and merged and merged[-1][2] == 'Quindi,':
        merged[-1] = [merged[-1][0], c[1], 'Quindi, praticamente?']; continue
    merged.append(c)
DUR = "86.57"
SFX = [("whoosh.mp3",0.22,0.6,0.2),("click.wav",1.73,0.46,0.28),("swipe.mp3",3.3,1.0,0.18),("pop.mp3",5.68,0.5,0.2),
  ("pop.mp3",6.53,0.5,0.2),("whoosh.mp3",7.68,0.6,0.2),("zap.mp3",12.03,0.9,0.14),("pop.mp3",14.38,0.5,0.2),
  ("paper-flip.mp3",15.25,1.4,0.3),("pop.mp3",18.93,0.5,0.2),("swipe.mp3",22.86,1.0,0.18),("click.wav",25.43,0.46,0.22),
  ("click.wav",25.73,0.46,0.18),("click.wav",26.03,0.46,0.18),("slam.mp3",28.82,1.1,0.3),("whoosh.mp3",29.46,0.6,0.22),
  ("pop.mp3",33.08,0.5,0.2),("click.wav",35.4,0.46,0.24),("click.wav",37.33,0.46,0.24),("error.mp3",40.85,1.2,0.12),
  ("swipe.mp3",42.28,0.8,0.18),("hard-cut.mp3",46.1,0.2,0.3),("sparkle.mp3",48.8,1.6,0.18),("whoosh.mp3",50.5,0.6,0.22),
  ("pop.mp3",53.48,0.5,0.2),("hard-cut.mp3",56.8,0.2,0.28),("swipe.mp3",60.05,1.0,0.2),("whoosh.mp3",63.38,0.6,0.25),
  ("click.wav",66.73,0.46,0.24),("pop.mp3",68.28,0.5,0.2),("hard-cut.mp3",71.75,0.2,0.3),("pop.mp3",73.68,0.5,0.18),
  ("slam.mp3",77.2,1.1,0.24),("pop.mp3",79.43,0.5,0.2),("sparkle.mp3",81.55,1.6,0.2),("pop.mp3",82.98,0.5,0.2),
  ("hard-cut.mp3",85.03,0.2,0.26)]
tags = [f'<audio id="sfx{k}" src="assets/sfx/{f}" data-start="{t}" data-duration="{d}" data-track-index="{10+k}" data-volume="{v}"></audio>'
        for k, (f, t, d, v) in enumerate(SFX)]
s = open('scripts/index.tpl.html').read()
s = s.replace('__DUR__', DUR).replace('__CAPS__', json.dumps(merged, ensure_ascii=False)).replace('__SFX__', '\n      '.join(tags))
open('index.html', 'w').write(s)
print(len(merged), 'captions,', len(SFX), 'sfx')
