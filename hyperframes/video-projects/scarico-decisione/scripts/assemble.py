# Join the TTS chunks into one narration track with controlled pauses, then get word timings.
# out: assets/audio/narration.wav, assets/timing.json, assets/words.json
import json, os, re, subprocess, sys, difflib
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.dirname(__file__))
from script import SECTIONS

SR = 48000
LEAD, GAP, TAIL = 0.45, 0.34, 3.0
SECTION_GAP = {"s2": 5.2, "default": 1.7}      # s1 -> s2 hosts the brand sting, the others a chapter card
WHISPER = "/root/.cache/hyperframes/whisper/whisper.cpp/build/bin/whisper-cli"
MODEL = "/root/.cache/hyperframes/whisper/models/ggml-large-v3-turbo-q5_0.bin"

def load(p):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", p, "-ar", str(SR), "-ac", "1", "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()

def trim(x, thr_db=-46, pad=0.05):
    win = int(0.01 * SR); n = len(x) // win
    rms = np.sqrt(np.mean(x[: n * win].reshape(n, win) ** 2, axis=1) + 1e-12)
    on = np.where(20 * np.log10(rms) > thr_db)[0]
    if not len(on): return x
    a = max(0, on[0] * win - int(pad * SR)); b = min(len(x), (on[-1] + 1) * win + int(pad * SR))
    y = x[a:b].copy(); f = int(0.008 * SR); y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
    return y

out, t = [np.zeros(int(LEAD * SR), np.float32)], LEAD
chunks, sections = {}, {}
for si, (sid, title, items) in enumerate(SECTIONS):
    if si:
        g = SECTION_GAP.get(sid, SECTION_GAP["default"]) - GAP
        out.append(np.zeros(int(g * SR), np.float32)); t += g
    s0 = t
    for k, (cid, text) in enumerate(items):
        if k: out.append(np.zeros(int(GAP * SR), np.float32)); t += GAP
        y = trim(load(f"assets/tts/{cid}.wav"))
        chunks[cid] = [round(t, 3), round(t + len(y) / SR, 3)]
        out.append(y); t += len(y) / SR
    sections[sid] = [round(s0, 3), round(t, 3), title]
out.append(np.zeros(int(TAIL * SR), np.float32)); t += TAIL
x = np.concatenate(out)
sf.write("assets/audio/narration-raw.wav", x, SR)
# light voice polish only: rumble high-pass + gentle presence; loudness is set on the final mix
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "assets/audio/narration-raw.wav", "-af",
                "highpass=f=70,equalizer=f=3200:t=q:w=1.2:g=1.5,acompressor=threshold=-20dB:ratio=2.2:attack=8:release=120:makeup=2",
                "-ar", str(SR), "assets/audio/narration.wav"], check=True)
json.dump({"dur": round(t, 3), "chunks": chunks, "sections": sections}, open("assets/timing.json", "w"), indent=1, ensure_ascii=False)
print("narration", round(t, 2), "s")

# ---- word timings: whisper on the narration, then aligned onto the script's own words ----
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "assets/audio/narration-raw.wav", "-ar", "16000", "-ac", "1", "/tmp/narr16.wav"], check=True)
subprocess.run([WHISPER, "-m", MODEL, "-l", "it", "-sow", "-ml", "1", "-ojf", "-of", "/tmp/narr16", "/tmp/narr16.wav"], capture_output=True, check=True)
segs = json.load(open("/tmp/narr16.json"))["transcription"]
ww = []
for s in segs:
    w = s["text"].strip()
    if w: ww.append((w, s["offsets"]["from"] / 1000, s["offsets"]["to"] / 1000))
norm = lambda w: re.sub(r"[^a-zàèéìòóù0-9']", "", w.lower())
words = []
for sid, title, items in SECTIONS:
    for cid, text in items:
        a, b = chunks[cid]
        hw = [w for w in ww if w[1] >= a - 0.25 and w[1] < b + 0.1]
        sw = text.split()
        sm = difflib.SequenceMatcher(None, [norm(w) for w in sw], [norm(w[0]) for w in hw], autojunk=False)
        dur = b - a
        if sm.ratio() < 0.88 or len(sw) / dur < 1.8 or len(sw) / dur > 3.6:
            print(f"CHECK {cid}: sim {sm.ratio():.2f}  {len(sw) / dur:.2f} w/s\n   script: {text}\n   heard : {' '.join(w[0] for w in hw)}")
        T = [None] * len(sw)
        for blk in sm.get_matching_blocks():
            for k in range(blk.size): T[blk.a + k] = (hw[blk.b + k][1], hw[blk.b + k][2])
        # fill gaps by interpolation between known neighbours (chunk edges as fallback)
        known = [(i, T[i]) for i in range(len(sw)) if T[i]]
        for i in range(len(sw)):
            if T[i]: continue
            L = max([k for k in known if k[0] < i], default=(-1, (a, a)), key=lambda k: k[0])
            R = min([k for k in known if k[0] > i], default=(len(sw), (b, b)), key=lambda k: k[0])
            f0, f1 = L[1][1], R[1][0]; n = R[0] - L[0]
            st = f0 + (f1 - f0) * (i - L[0]) / n; T[i] = (st, f0 + (f1 - f0) * (i - L[0] + 1) / n - 0.02)
        for i, w in enumerate(sw):
            s0, e0 = max(a, T[i][0]), min(b, max(T[i][1], T[i][0] + 0.08))
            words.append({"w": w, "s": round(s0, 3), "e": round(e0, 3), "c": cid})
json.dump(words, open("assets/words.json", "w"), ensure_ascii=False)
print("words", len(words), "matched from", len(ww))
