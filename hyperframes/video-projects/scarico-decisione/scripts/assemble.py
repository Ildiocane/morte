# Join the TTS chunks into one narration track with controlled pauses, plus word timings for captions/anchors.
# Per-chunk word timings (relative to the trimmed chunk) are cached in assets/tts/words_rel.json; whisper only runs
# for chunks that are new or were regenerated. TEMPO < 1 slows the clone down to Luca's natural pace (rubberband,
# pitch + formants preserved).
# out: assets/audio/narration.wav, assets/timing.json, assets/words.json
import json, os, re, subprocess, sys, difflib
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.dirname(__file__))
from script import SECTIONS

SR = 48000
TEMPO = 0.9
LEAD, GAP, TAIL = 0.45, 0.42, 3.0
SECTION_GAP = {"s2": 5.2, "default": 1.8}      # s1 -> s2 hosts the brand sting, the others a chapter card
WHISPER = "/root/.cache/hyperframes/whisper/whisper.cpp/build/bin/whisper-cli"
MODEL = "/root/.cache/hyperframes/whisper/models/ggml-large-v3-turbo-q5_0.bin"
REL = "assets/tts/words_rel.json"
norm = lambda w: re.sub(r"[^a-zàèéìòóù0-9']", "", w.lower())

def load(p, af=None):
    cmd = ["ffmpeg", "-loglevel", "error", "-i", p] + (["-af", af] if af else []) + ["-ar", str(SR), "-ac", "1", "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.float32).copy()

def trim(x, thr_db=-46, pad=0.05):
    win = int(0.01 * SR); n = len(x) // win
    rms = np.sqrt(np.mean(x[: n * win].reshape(n, win) ** 2, axis=1) + 1e-12)
    on = np.where(20 * np.log10(rms) > thr_db)[0]
    if not len(on): return x
    a = max(0, on[0] * win - int(pad * SR)); b = min(len(x), (on[-1] + 1) * win + int(pad * SR))
    y = x[a:b].copy(); f = int(0.008 * SR); y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
    return y

def align(text, hw, a, b):
    """script words of one chunk + whisper words [(w, s, e)] -> [(w, s, e)] on the script's own spelling"""
    sw = text.split()
    sm = difflib.SequenceMatcher(None, [norm(w) for w in sw], [norm(w[0]) for w in hw], autojunk=False)
    T = [None] * len(sw)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size): T[blk.a + k] = (hw[blk.b + k][1], hw[blk.b + k][2])
    known = [(i, T[i]) for i in range(len(sw)) if T[i]]
    for i in range(len(sw)):
        if T[i]: continue
        L = max([k for k in known if k[0] < i], default=(-1, (a, a)), key=lambda k: k[0])
        R = min([k for k in known if k[0] > i], default=(len(sw), (b, b)), key=lambda k: k[0])
        f0, f1 = L[1][1], R[1][0]; n = R[0] - L[0]
        T[i] = (f0 + (f1 - f0) * (i - L[0]) / n, f0 + (f1 - f0) * (i - L[0] + 1) / n - 0.02)
    out, last = [], a
    for i, w in enumerate(sw):                                   # keep word starts monotonic
        s0 = min(b - 0.05, max(last, T[i][0])); e0 = min(b, max(T[i][1], s0 + 0.08)); out.append((w, s0, e0)); last = s0 + 0.02
    return out, sm.ratio()

def whisper_words(wav16):
    subprocess.run([WHISPER, "-m", MODEL, "-l", "it", "-sow", "-ml", "1", "-ojf", "-of", wav16[:-4], wav16], capture_output=True, check=True)
    return [(s["text"].strip(), s["offsets"]["from"] / 1000, s["offsets"]["to"] / 1000) for s in json.load(open(wav16[:-4] + ".json"))["transcription"] if s["text"].strip()]

# ---- trimmed chunks (original tempo) + relative word timings ----
rel = json.load(open(REL)) if os.path.exists(REL) else {}
raw = {}
for sid, title, items in SECTIONS:
    for cid, text in items:
        p = f"assets/tts/{cid}.wav"; y = trim(load(p)); raw[cid] = y
        key = f"{os.path.getmtime(p):.0f}|{text}"
        if cid in rel and rel[cid]["key"] == key: continue
        sf.write("/tmp/chunk.wav", y, SR)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/chunk.wav", "-ar", "16000", "-ac", "1", "/tmp/chunk16.wav"], check=True)
        ws, sim = align(text, whisper_words("/tmp/chunk16.wav"), 0.0, len(y) / SR)
        rel[cid] = {"key": key, "w": ws}
        print(f"aligned {cid}  sim {sim:.2f}")
json.dump(rel, open(REL, "w"), ensure_ascii=False)

# ---- assemble at the target tempo ----
out, t = [np.zeros(int(LEAD * SR), np.float32)], LEAD
chunks, sections, words = {}, {}, []
for si, (sid, title, items) in enumerate(SECTIONS):
    if si:
        g = SECTION_GAP.get(sid, SECTION_GAP["default"]) - GAP
        out.append(np.zeros(int(g * SR), np.float32)); t += g
    s0 = t
    for k, (cid, text) in enumerate(items):
        if k: out.append(np.zeros(int(GAP * SR), np.float32)); t += GAP
        sf.write("/tmp/chunk.wav", raw[cid], SR)
        y = load("/tmp/chunk.wav", f"rubberband=tempo={TEMPO}:formant=preserved:pitchq=quality") if TEMPO != 1 else raw[cid]
        chunks[cid] = [round(t, 3), round(t + len(y) / SR, 3)]
        for w, s, e in rel[cid]["w"]: words.append({"w": w, "s": round(t + s / TEMPO, 3), "e": round(t + e / TEMPO, 3), "c": cid})
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
json.dump(words, open("assets/words.json", "w"), ensure_ascii=False)
print("narration", round(t, 2), "s  words", len(words))
