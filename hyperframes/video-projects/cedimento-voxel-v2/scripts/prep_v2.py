# v2: Luca's own recording drives everything. Novice line = ElevenLabs TTS (only line not in Luca's voice).
import json, soundfile as sf, numpy as np
NOV = (0.35, 0.35 + 1.84); OFF = 0.35 + 1.84 + 0.40 - 3.75          # coach source time -> timeline
w = json.load(open('../../raw-media/v5/w.json'))                     # [start,end,text] in source time
FIX = {'istrutto': 'distrutto', 'cilmento,': 'cedimento,'}
words = [{'text': FIX.get(t, t), 'start': round(s + OFF, 3), 'end': round(e + OFF, 3)} for s, e, t in w if s >= 3.7]
# coach lines = the same 9 beats as v1 (v1 line 4 "Con meno fatica acuta" now stays with the coach, inside line 3)
BEATS = ["Se", "Per", "In", "Attenzione,", "Programma", "Il", "La", "Seguimi"]
lines = [{'who': 'novice', 'text': 'Devi fallire ogni serie?', 'start': NOV[0], 'end': NOV[1]}]
cur = None
for x in words:
    if x['text'] in BEATS and (cur is None or x['text'] != cur['words'][-1]['text']):
        if cur and not (x['text'] == 'Il' and cur['words'][0]['text'] != 'Programma'): pass
    if cur is None or (x['text'] in BEATS and len(cur['words']) > 3):
        cur = {'who': 'coach', 'words': []}; lines.append(cur)
    cur['words'].append(x)
for l in lines[1:]:
    l['text'] = ' '.join(x['text'] for x in l['words']); l['start'] = l['words'][0]['start']; l['end'] = l['words'][-1]['end']
json.dump([{k: v for k, v in l.items()} for l in lines], open('assets/dialogue.json', 'w'), ensure_ascii=False, indent=1)
for l in lines: print(f"{l['start']:6.2f}-{l['end']:6.2f} {l['who']}: {l['text']}")
# captions: chunks of the real words with real timings
KEY = {'distrutto','fatica','efficacia','muscolo','sforzo','adeguato','obbligatorio','8','settimane','due','riserva','simile','cedimento','meno','acuta','attenzione','credibile','5','mascherate','esercizio','recuperi','strumento','qualità','controllabile','seguimi','criterio'}
caps = [{'a': NOV[0], 'b': NOV[1] + 0.2, 'w': ['Devi', 'fallire', 'ogni', 'serie?'], 'hl': [1], 'who': 'novice'}]
for l in lines[1:]:
    cur = []
    for k, x in enumerate(l['words']):
        cur.append(x)
        if x['text'][-1] in ',.;:?' or len(cur) >= 4 or k == len(l['words']) - 1:
            ws = [c['text'] for c in cur]
            hl = [i for i, t in enumerate(ws) if t.strip(',.;:?!').split("'")[-1].lower() in KEY]
            caps.append({'a': cur[0]['start'], 'b': cur[-1]['end'] + 0.12, 'w': ws, 'hl': hl, 'who': 'coach'}); cur = []
for i in range(len(caps) - 1): caps[i]['b'] = min(caps[i]['b'], caps[i + 1]['a'])
json.dump(caps, open('assets/captions.json', 'w'), ensure_ascii=False)
# mouth envelopes per speaker (30fps) from the final dialogue track
a, sr = sf.read('assets/audio/dialogue.wav', dtype='float32')
n = int(len(a) / sr * 30) + 1; env = {'coach': [0] * n, 'novice': [0] * n}
noise = 10 ** (-40 / 20)
for i in range(n):
    s = a[int(i * sr / 30):int((i + 1) * sr / 30)]; r = float(np.sqrt(np.mean(s * s))) if len(s) else 0
    t = i / 30; who = 'novice' if NOV[0] - 0.02 <= t <= NOV[1] + 0.02 else ('coach' if t > NOV[1] + 0.2 else None)
    if who: env[who][i] = round(min(1.0, max(0, r - noise) / (0.05 if who == 'coach' else 0.12)), 2)
json.dump(env, open('assets/mouth.json', 'w'))
# old->new time anchors (v1 line boundaries -> v2 line boundaries) for remapping graphics
v1 = json.load(open('../cedimento-voxel/assets/dialogue.json'))
v1m = [v1[0], v1[1], v1[2], {'start': v1[3]['start'], 'end': v1[4]['end']}] + v1[5:]
anch = [(0, 0)] + [(o['start'], n['start']) for o, n in zip(v1m, lines)] + [(o['end'], n['end']) for o, n in zip(v1m, lines)]
anch = sorted(set(anch)) + [(50.2, len(a) / sr)]
json.dump(anch, open('assets/anchors.json', 'w'))
print('dur', round(len(a) / sr, 2), 'lines', len(lines), 'caps', len(caps))
