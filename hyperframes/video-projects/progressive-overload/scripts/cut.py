# Build assets/edit.mp4 from Luca's raw take. Voice is NOT processed: no loudnorm/EQ/compression —
# only 10ms fades at each cut to avoid clicks; audio re-encoded once at AAC 320k (source is AAC 256k).
# Every boundary snapped to a measured energy dip and verified by re-transcribing the clip.
import json, os, subprocess, sys, tempfile
RAW, OUT = sys.argv[1], sys.argv[2]
SEGMENTS = [
    (0.76, 4.52,    "Ma che cos'è in definitiva il progressive overload?"),
    (4.85, 10.60,   "Tutti parlano di questo progressive overload senza spiegarci realmente che cos'è, facendo confusione."),
    (10.75, 13.21,  "Perché ci sono tanti creator che l'hanno spiegato effettivamente,"),
    (20.20, 24.14,  "ma solo pochi hanno capito veramente che cos'è e l'hanno comunicato correttamente."),  # skips the first, garbled version
    (25.35, 32.30,  "Progressive overload significa qualcosa che riesco a sovraccaricare progressivamente, matematicamente parlando."),
    (32.50, 35.60,  "Sul muscolo in questo caso, perché parliamo di allenamento."),
    (50.45, 58.00,  "Molti pensano che ci siano tanti parametri per un sovraccarico progressivo, quando in realtà sono soltanto due."),  # 4th (clean) take only
    (63.90, 76.20,  "ROM: sbagliato, dovremmo già avere un ROM completo."),
    (76.40, 100.20, "Time under tension: sbagliato."),
    (107.60, 122.40, "Recupero più breve: controproducente (fosfati)."),
    (123.80, 147.10, "Non è progressione: allena l'apparato aerobico, accumula metaboliti."),
    (148.20, 150.60, "Quindi quali sono questi unici due fattori?"),
    (151.20, 153.61, "Aumentare il carico a parità di ripetizioni"),
    (159.31, 162.40, "o aumentare le ripetizioni a parità di carico."),  # skips the repeated first factor
    (165.10, 165.85, "Basta!"),
    (169.40, 187.07, "Questi due fattori ... aumenteranno il tonnellaggio."),
    (195.60, 208.60, "Progressione di forza = aumento trasversale del muscolo. Un processo inscindibile e biologico."),
    (209.00, 213.64, "Se la tua forza aumenta in un range dalle 5 alle 30,"),
    (215.95, 219.70, "avrai una progressione sicura e garantita anche del tuo muscolo."),
    (220.30, 227.00, "Ovviamente a parità di tutti gli altri fattori ..."),
    (227.80, 234.32, "... hai costruito un nuovo muscolo."),
    (243.50, 247.75, "Se ti è piaciuto il video lascia like, commenta cosa vuoi vedere nel prossimo video, iscriviti."),  # cleanest CTA take
    (259.40, 260.17, "Ciao!"),
]
# internal pauses (silencedetect -40dB) shrunk to KEEP_GAP
PAUSES = [(54.20, 54.63), (84.18, 84.48), (114.84, 116.39), (130.52, 131.31), (134.00, 134.63), (135.96, 139.50),
          (172.29, 172.54), (175.59, 176.43), (223.36, 223.82), (232.54, 232.95)]
KEEP_GAP = 0.20
pieces = []
for a, b, _ in SEGMENTS:
    cur = a
    for pa, pb in PAUSES:
        if a < pa and pb < b and pb - pa > KEEP_GAP:
            pieces.append((cur, pa + KEEP_GAP / 2)); cur = pb - KEEP_GAP / 2
    pieces.append((cur, b))
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
