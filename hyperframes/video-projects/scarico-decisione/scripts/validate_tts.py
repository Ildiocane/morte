# Checks every TTS chunk: speaking rate + whisper transcript vs script text. Prints the chunks to regenerate.
import json, os, re, subprocess, sys, difflib
sys.path.insert(0, os.path.dirname(__file__))
from script import SECTIONS
WHISPER = "/root/.cache/hyperframes/whisper/whisper.cpp/build/bin/whisper-cli"
MODEL = "/root/.cache/hyperframes/whisper/models/ggml-large-v3-turbo-q5_0.bin"
norm = lambda s: [w for w in re.sub(r"[^a-zàèéìòóù0-9' ]", " ", s.lower()).split() if w]
only = set(sys.argv[1:]); bad = []
cache = json.load(open("assets/tts/check.json")) if os.path.exists("assets/tts/check.json") else {}
for sid, _, items in SECTIONS:
    for cid, text in items:
        if only and cid not in only: continue
        p = f"assets/tts/{cid}.wav"
        if not os.path.exists(p): continue
        st = os.path.getmtime(p)
        if cid in cache and cache[cid]["mtime"] == st and not only: r = cache[cid]
        else:
            dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", p, "-ar", "16000", "-ac", "1", "/tmp/chk.wav"], check=True)
            hyp = subprocess.run([WHISPER, "-m", MODEL, "-l", "it", "-nt", "-np", "/tmp/chk.wav"], capture_output=True, text=True).stdout
            sim = difflib.SequenceMatcher(None, norm(text), norm(hyp)).ratio()
            r = cache[cid] = {"mtime": st, "dur": round(dur, 2), "wps": round(len(text.split()) / dur, 2), "sim": round(sim, 3), "hyp": hyp.strip()}
        flag = r["sim"] < 0.9 or r["wps"] < 1.7 or r["wps"] > 3.6
        if flag: bad.append(cid)
        print(f'{cid}  {r["dur"]:6.2f}s  {r["wps"]:.2f} w/s  sim {r["sim"]:.3f}  {"<-- CHECK" if flag else ""}')
        if flag: print("    script:", text, "\n    heard :", r["hyp"])
json.dump(cache, open("assets/tts/check.json", "w"), ensure_ascii=False, indent=0)
print("BAD:", " ".join(bad))
