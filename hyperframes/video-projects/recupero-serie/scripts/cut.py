# Build assets/edit.mp4 from Luca's raw take. Voice is NOT processed: no loudnorm/EQ/compression —
# only 10ms fades at each cut to avoid clicks; audio re-encoded once at AAC 320k (source is AAC 256k).
# Every boundary snapped to a measured energy dip and verified by re-transcribing the clip.
import json, os, subprocess, sys, tempfile
RAW, OUT = sys.argv[1], sys.argv[2]
SEGMENTS = [
    (0.0, 6.40,   "Quanto devo recuperare tra le sedute e quanto devo recuperare tra gli esercizi?"),
    (6.40, 16.55, "Sono due cose diverse ma che hanno una cosa in comune ... spirito critico."),
    (16.55, 24.90, "Per sapere quanto devo recuperare tra le sedute mi preoccupo di due fattori: i DOMS e le progressioni."),
    (25.00, 36.10, "Se io ho ancora dei DOMS ... non potrò allenare quel muscolo lì."),
    (39.40, 43.33, "Se invece i DOMS non ci sono ma le prestazioni calano o rimangono in stallo,"),   # skips false start "Se invece le prestazioni,"
    (47.10, 50.50, "allora quell'extra giorno di recupero sarà necessario."),                          # skips "quell'extra giorno di allenamento, di recupero,"
    (50.50, 57.78, "Tra le sedute invece giochiamo con un minimo di recupero di due minuti."),
    (57.78, 65.05, "Questo perché ... se l'intensità è veramente alta."),
    (65.05, 71.40, "Intensità che si traduce in un RIR 0-1 o a cedimento appunto."),
    (72.40, 77.22, "Di conseguenza se vogliamo avere un range più ampio da due minuti minimo fino a un massimo di"),
    (77.92, 79.70, "quattro minuti e mezzo."),                                                           # skips "quattro minuti,"
    (79.70, 95.10, "Ovviamente muscoli più grandi ... parziale extra in allungamento."),
    (95.10, 102.50, "Se ti è stato utile questo video sui recuperi metti un like, seguimi e ci vediamo in un prossimo video."),
]
# Tight-cut (Jeff Nippard pacing): trim every segment to the voice and shrink every silence inside it.
# 10ms RMS frames on a 16k mono copy of the raw audio; speech = above SIL_DB.
WAV = sys.argv[3]
SIL_DB, MIN_SIL, KEEP_GAP, LEAD, TAIL = -37.0, 0.10, 0.06, 0.03, 0.06
import wave, struct, math
_w = wave.open(WAV); _sr = _w.getframerate(); _d = struct.unpack('<%dh' % _w.getnframes(), _w.readframes(_w.getnframes()))
_hop = _sr // 100
def _db(i):
    s = _d[i * _hop:(i + 1) * _hop]
    r = math.sqrt(sum(x * x for x in s) / max(len(s), 1)) or 1
    return 20 * math.log10(r / 32768)
pieces = []
for a, b, _ in SEGMENTS:
    fr = list(range(int(a * 100), int(b * 100)))
    loud = [i for i in fr if _db(i) > SIL_DB]
    a2 = max(a, loud[0] / 100 - LEAD); b2 = min(b, (loud[-1] + 1) / 100 + TAIL)
    cur = a2; run = None
    for i in range(int(a2 * 100), int(b2 * 100)):
        quiet = _db(i) <= SIL_DB
        if quiet and run is None: run = i
        if not quiet and run is not None:
            if (i - run) / 100 >= MIN_SIL:
                pieces.append((cur, run / 100 + KEEP_GAP / 2)); cur = i / 100 - KEEP_GAP / 2
            run = None
    pieces.append((cur, b2))
tmp = tempfile.mkdtemp(prefix="cut-"); parts = []
for i, (a, b) in enumerate(pieces):
    d = b - a; part = os.path.join(tmp, f"p{i:02d}.mkv")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.3f}", "-i", RAW, "-t", f"{d:.3f}",
        "-vf", "fps=30", "-af", f"afade=t=in:d=0.010,afade=t=out:st={d-0.010:.3f}:d=0.010",
        "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p",
        "-c:a", "pcm_s24le", "-ar", "48000", part], check=True)
    parts.append(part)
lst = os.path.join(tmp, "list.txt")
open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
    "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", "30", "-g", "30", "-keyint_min", "30",
    "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-movflags", "+faststart", OUT], check=True)
t, cmap = 0.0, []
for a, b in pieces:
    cmap.append({"src_start": a, "src_end": b, "edit_start": round(t, 3)}); t += b - a
json.dump(cmap, open(OUT.replace(".mp4", ".cutmap.json"), "w"), indent=1)
print(f"{len(pieces)} pieces, expected duration {t:.2f}s")
