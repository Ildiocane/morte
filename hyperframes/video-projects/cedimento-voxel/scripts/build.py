import json
DUR = "50.2"
dlg = json.load(open('assets/dialogue.json')); caps = json.load(open('assets/captions.json')); mouth = open('assets/mouth.json').read()
SFX = [("whoosh.mp3", 2.38, 0.6, 0.12), ("pop.mp3", 4.68, 0.5, 0.18), ("pop.mp3", 7.28, 0.5, 0.18), ("whoosh.mp3", 8.43, 0.6, 0.12),
       ("pop.mp3", 10.28, 0.5, 0.16), ("pop.mp3", 11.98, 0.5, 0.16), ("click.wav", 15.78, 0.46, 0.2), ("whoosh.mp3", 16.86, 0.6, 0.14),
       ("click.wav", 20.38, 0.46, 0.18), ("pop.mp3", 23.58, 0.5, 0.16), ("whoosh.mp3", 25.78, 0.6, 0.12), ("pop.mp3", 31.58, 0.5, 0.16),
       ("pop.mp3", 32.88, 0.5, 0.16), ("whoosh.mp3", 34.48, 0.6, 0.12), ("pop.mp3", 35.98, 0.5, 0.16), ("slam.mp3", 40.9, 1.1, 0.18),
       ("pop.mp3", 44.78, 0.5, 0.16), ("whoosh.mp3", 46.48, 0.6, 0.14)]
tags = [f'<audio id="sfx{k}" src="assets/sfx/{f}" data-start="{t}" data-duration="{d}" data-track-index="{10+k}" data-volume="{v}"></audio>' for k, (f, t, d, v) in enumerate(SFX)]
s = open('scripts/index.tpl.html').read().replace('__DUR__', DUR).replace('__MOUTH__', mouth).replace('__CAPS__', json.dumps(caps, ensure_ascii=False)) \
    .replace('__DLG__', json.dumps([{'who': d['who'], 'start': d['start'], 'end': d['end']} for d in dlg])).replace('__SFX__', '\n      '.join(tags))
open('index.html', 'w').write(s)
print('ok')
