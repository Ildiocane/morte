# Build assets/edit.mp4 from the raw take: keep only the listed segments (source seconds),
# shorten internal pauses, 12ms audio fades at every cut, 30fps 1080x1920, voice loudnorm.
import json, subprocess, sys
RAW = sys.argv[1]; OUT = sys.argv[2]
# (start, end, label) — boundaries snapped to measured silences / energy dips, each verified by re-transcribing
SEGMENTS = [
    (2.62, 5.45,  "Perché ci hanno mentito sul range di ripetizioni?"),
    (7.40, 13.30, "continuo a sentire quei range ... sempre uguali."),
    (14.20, 15.05, "Non è così."),
    (17.41, 22.90, "lo studio che dice che l'ipertrofia tra 5 e 30 ripetizioni è uguale praticamente,"),
    (24.32, 26.95, "nella sua praticità non ha senso."),
    (28.15, 28.98, "Mi spiego meglio."),
    (29.95, 41.00, "Se tu fai 5-6 colpi, 7 massimo, ... senza compromettere la fatica del sistema nervoso."),
    (54.25, 60.60, "Dalle 12-15 in su ... più stress metabolico,"),
    (65.97, 68.62, "più capacità di recupero del sistema nervoso centrale."),
    (80.05, 83.22, "Ed è per questo che quel range di ripetizione è sbagliato."),
    (86.72, 94.82, "tra un 5 e un 10 colpi ... quindi 5-7, 6-8, 8-10."),
    (112.60, 119.16, "Se ti ho chiarito le idee metti un like ... nel prossimo video."),
]
# internal pauses (from silencedetect -32dB) to shrink to ~0.14s
PAUSES = [(32.11, 32.52), (33.58, 33.84), (37.98, 38.38), (89.36, 89.92), (52.50, 54.30)]
KEEP_GAP = 0.14
pieces = []
for a, b, _ in SEGMENTS:
    cur = a
    for pa, pb in PAUSES:
        if a < pa and pb < b and pb - pa > KEEP_GAP:
            mid = KEEP_GAP / 2
            pieces.append((cur, pa + mid)); cur = pb - mid
    pieces.append((cur, b))
import os, tempfile
tmp = tempfile.mkdtemp(prefix="cut-")
parts = []
for i, (a, b) in enumerate(pieces):
    d = b - a; part = os.path.join(tmp, f"p{i:02d}.mkv")
    # accurate seek (-ss after -i is slow; -ss before -i with re-encode is frame-accurate in modern ffmpeg)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.3f}", "-i", RAW, "-t", f"{d:.3f}",
        "-vf", "fps=30", "-af", f"afade=t=in:d=0.012,afade=t=out:st={d-0.012:.3f}:d=0.012",
        "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p",
        "-c:a", "pcm_s16le", "-ar", "48000", part], check=True)
    parts.append(part)
lst = os.path.join(tmp, "list.txt")
open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
    "-pix_fmt", "yuv420p", "-r", "30", "-g", "30", "-keyint_min", "30", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    "-movflags", "+faststart", OUT], check=True)
n = len(pieces)
# edited-time map: source piece -> edited offset (for reference / captions)
t, cmap = 0.0, []
for a, b in pieces:
    cmap.append({"src_start": a, "src_end": b, "edit_start": round(t, 3)}); t += b - a
json.dump(cmap, open(OUT.replace(".mp4", ".cutmap.json"), "w"), indent=1)
print(f"{n} pieces, expected duration {t:.2f}s")
