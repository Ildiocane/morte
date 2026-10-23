# Build assets/edit.mp4 from Luca's raw take. Voice is NOT processed: no loudnorm/EQ/compression —
# only 10ms fades at each cut to avoid clicks; audio re-encoded once at AAC 320k (source is AAC 256k).
# Every boundary snapped to a measured energy dip and verified by re-transcribing the clip.
import json, os, subprocess, sys, tempfile
RAW, OUT = sys.argv[1], sys.argv[2]
SEGMENTS = [
    (0.76, 4.52,    "Ma che cos'è in definitiva il progressive overload?"),
    (4.85, 10.60,   "Tutti parlano di questo progressive overload senza spiegarci realmente che cos'è, facendo confusione."),
    (10.75, 13.21,  "Perché ci sono tanti creator che l'hanno spiegato effettivamente,"),
    (20.20, 24.14,  "ma solo pochi hanno capito veramente che cos'è e l'hanno comunicato correttamente."),  # skips the garbled first version
    (25.35, 32.30,  "Progressive overload significa qualcosa che riesco a sovraccaricare progressivamente, matematicamente parlando,"),
    (32.50, 35.60,  "sul muscolo in questo caso, perché parliamo di allenamento."),
    (50.45, 58.00,  "Molti pensano che ci siano tanti parametri ... soltanto due i valori che ci interessano."),  # 4th (clean) take only
    (63.90, 76.20,  "ROM: sbagliato, dovremmo già avere un ROM completo."),
    (76.40, 81.75,  "Altri parlano di time under tension, quindi tenere sotto tensione il muscolo per più tempo,"),
    (84.33, 100.20, "ma anche qui sbagliato ... nessuno stimolo reale al muscolo."),  # skips the first, abandoned "ma anche qui sbagliato perché se noi teniamo…"
    (107.60, 110.95, "Altri parlano invece di diminuire il recupero tra le serie."),
    (111.36, 122.40, "Oltre ad essere controproduttivo ... nelle prossime serie,"),  # drops filler "che questo"
    (123.80, 147.10, "non stiamo anche qui dando una progressione continua ... in maniera diretta."),
    (148.20, 150.60, "Quindi quali sono questi unici due fattori?"),
    (151.62, 153.61, "Aumentare il carico a parità di ripetizioni"),  # drops "Sono"
    (159.31, 162.40, "o aumentare le ripetizioni a parità di carico."),  # skips the repeated first factor
    (165.10, 165.85, "Basta!"),
    (169.40, 187.07, "Questi due fattori ... aumenteranno il tonnellaggio ... nel corso delle serie."),
    (195.60, 208.60, "Facendo così ... È un processo inscindibile e biologico."),
    (209.00, 213.64, "Se la tua forza aumenta in un range dalle 5 alle 30,"),
    (215.95, 219.70, "avrai una progressione sicura e garantita anche del tuo muscolo."),
    (220.30, 227.00, "Ovviamente a parità di tutti gli altri fattori ..."),
    (227.80, 234.32, "... hai costruito un nuovo muscolo."),
    (243.50, 247.75, "Se ti è piaciuto il video lascia like, commenta cosa vuoi vedere nel prossimo video, iscriviti."),  # cleanest CTA take
    (259.40, 260.17, "Ciao!"),
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
