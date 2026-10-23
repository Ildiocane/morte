# Build assets/edit.mp4 from Luca's raw take: ONLY pauses are cut, every word stays (Luca: "taglia solo le pause,
# il parlato lascialo così com'è"). Voice is NOT processed: no loudnorm/EQ/compression — only 10ms fades at each cut;
# audio re-encoded once at AAC 320k.
# Tight-cut (Jeff Nippard pacing, PREFERENCES.md): trim to the voice (30ms lead, 60ms tail) and shrink every silence
# >= 0.10 s to 60 ms. 10ms RMS frames on a 16k mono copy of the raw audio; speech = above SIL_DB.
# usage: python scripts/cut.py assets/raw.mp4 assets/edit.mp4 assets/raw16k.wav
import json, os, subprocess, sys, tempfile
import numpy as np, soundfile as sf
RAW, OUT, WAV = sys.argv[1], sys.argv[2], sys.argv[3]
SIL_DB, MIN_SIL, KEEP_GAP, LEAD, TAIL = -37.0, 0.10, 0.06, 0.03, 0.06

a, sr = sf.read(WAV); hop = sr // 100
db = np.array([20 * np.log10(max(np.sqrt(np.mean(a[i * hop:(i + 1) * hop] ** 2)), 1e-9)) for i in range(len(a) // hop)])
loud = np.nonzero(db > SIL_DB)[0]
a2, b2 = max(0, loud[0] / 100 - LEAD), min(len(db) / 100, (loud[-1] + 1) / 100 + TAIL)
pieces, cur, run = [], a2, None
for i in range(int(a2 * 100), int(b2 * 100)):
    quiet = db[i] <= SIL_DB
    if quiet and run is None: run = i
    if not quiet and run is not None:
        if (i - run) / 100 >= MIN_SIL:
            pieces.append((cur, run / 100 + KEEP_GAP / 2)); cur = i / 100 - KEEP_GAP / 2
        run = None
pieces.append((cur, b2))

tmp = tempfile.mkdtemp(prefix="cut-"); parts = []
for i, (s, e) in enumerate(pieces):
    d = e - s; part = os.path.join(tmp, f"p{i:02d}.mkv")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{s:.3f}", "-i", RAW, "-t", f"{d:.3f}",
        "-vf", "fps=30", "-af", f"afade=t=in:d=0.010,afade=t=out:st={d - 0.010:.3f}:d=0.010",
        "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p",
        "-c:a", "pcm_s24le", "-ar", "48000", part], check=True)
    parts.append(part)
lst = os.path.join(tmp, "list.txt")
open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
    "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", "30", "-g", "30", "-keyint_min", "30",
    "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-movflags", "+faststart", OUT], check=True)
t, cmap = 0.0, []
for s, e in pieces:
    cmap.append({"src_start": round(s, 3), "src_end": round(e, 3), "edit_start": round(t, 3)}); t += e - s
json.dump(cmap, open(OUT.replace(".mp4", ".cutmap.json"), "w"), indent=1)
print(f"{len(pieces)} pieces, removed {len(db) / 100 - t:.2f}s, expected duration {t:.2f}s")
