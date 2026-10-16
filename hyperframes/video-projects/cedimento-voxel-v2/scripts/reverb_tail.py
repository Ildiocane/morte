# reverb tail metric: energy 80-250 ms after each word end relative to the word's own level (lower = drier)
import sys, json, soundfile as sf, numpy as np
w = json.load(open(sys.argv[1])); off = float(sys.argv[2])
for f in sys.argv[3:]:
    a, sr = sf.read(f, dtype='float32')
    if a.ndim > 1: a = a.mean(1)
    rms = lambda s, e: 20*np.log10(np.sqrt(np.mean(a[int(s*sr):int(e*sr)]**2))+1e-9)
    r = []
    for i, (s, e, t) in enumerate(w):
        if s < 3.7: continue
        nxt = w[i+1][0] if i+1 < len(w) else e+1
        if nxt - e < 0.3: continue
        s2, e2 = s + off, e + off
        r.append(rms(e2+0.08, e2+0.25) - rms(max(s2, e2-0.25), e2))
    db = [rms(i/100, i/100+0.01) for i in range(int(len(a)/sr*100)-1)]
    print(f.split('/')[-1], 'tail', round(float(np.median(r)),1), 'dB  noise p10', round(float(np.percentile(db,10)),1), 'speech p90', round(float(np.percentile(db,90)),1))
