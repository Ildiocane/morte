# transcript-raw.json (whisper, edit time) -> transcript.json (spelling fixes) -> captions-final.json (phrase chunks)
import json, sys
w = json.load(open('assets/transcript-raw.json'))
FIX = {"l'espiratorio": 'respiratorio', 'dilatato': 'di lattato', 'ricarico.': 'carico.', 'ricarico': 'carico',
       'cercheremmo': 'cercheremo', 'muscole': 'muscolo', 'centrica,': 'eccentrica,', 'iscrivi.': 'iscriviti.',
       'inscendibile': 'inscindibile', 'Rangi': 'Range'}
out = []
for k, x in enumerate(w):
    t = FIX.get(x['text'], x['text'])
    nxt = w[k + 1]['text'] if k + 1 < len(w) else ''
    if t == 'le' and nxt == 'muscole': t = 'il'
    if t in ('che', 'Che') and nxt.lower().startswith('su') and k + 2 < len(w) and w[k + 2]['text'] == 'quale': t = 'chissà'
    if t.lower() in ('su',) and k > 0 and out and out[-1]['text'] == 'chissà': continue
    out.append({'text': t, 'start': x['start'], 'end': x['end']})
json.dump(out, open('assets/transcript.json', 'w'), ensure_ascii=False, indent=0)
end = float(sys.argv[1])
chunks, cur = [], []
for k, x in enumerate(out):
    cur.append(x); nxt = out[k + 1] if k + 1 < len(out) else None
    gap = (nxt['start'] - x['end']) if nxt else 9
    if x['text'][-1] in '.,?!:' or len(cur) >= 4 or gap > 0.35 or nxt is None:
        chunks.append([cur[0]['start'], 0, ' '.join(c['text'] for c in cur)]); cur = []
for k, c in enumerate(chunks):
    nx = chunks[k + 1][0] if k + 1 < len(chunks) else end
    c[1] = round(min(nx, c[0] + 2.8), 2)
m = []
for c in chunks:
    if m and m[-1][1] - m[-1][0] < 0.35: m[-1] = [m[-1][0], c[1], m[-1][2] + ' ' + c[2]]
    else: m.append(c)
json.dump(m, open('assets/captions-final.json', 'w'), ensure_ascii=False)
print(len(m), 'captions')
