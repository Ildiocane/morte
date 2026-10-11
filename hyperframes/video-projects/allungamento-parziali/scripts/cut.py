# Build assets/edit.mp4 from Luca's raw take: keep only SEGMENTS (source seconds), shrink internal pauses,
# 12ms audio fades at each cut, 30fps 1080x1920, 1s keyframes, voice loudnorm.
# Every boundary was snapped to a measured silence / energy dip and verified by re-transcribing the clip.
import json, os, subprocess, sys, tempfile
RAW, OUT = sys.argv[1], sys.argv[2]
SEGMENTS = [
    (0.62, 5.86,   "Negli ultimi anni è diventato quasi un dogma: se vuoi crescere devi allenare il muscolo in massimo allungamento."),
    (8.94, 11.42,  "La direzione è interessante, ma va spiegata meglio."),
    (17.98, 25.85, "Allenarsi a lunghezze muscolari elevate significa produrre tensione quando il muscolo si trova relativamente allungato."),
    (57.17, 64.76, "Una meta-analisi pubblicata nel 2026 su 8 studi ha trovato un vantaggio significativo ... per l'ipertrofia complessiva"),
    (75.98, 81.92, "Si parla spesso di crescita longitudinale e aggiunta di sarcomeri in serie come se fosse già dimostrata nell'uomo."),
    (82.40, 83.06, "Non lo è."),
    (99.89, 101.50, "Quindi, praticamente?"),
    (106.07, 110.33, "Scegli esercizi che ti permettono di produrre molta tensione anche nella parte allungata."),
    (110.63, 116.13, "Un leg curl da seduto per i femorali, delle calf raise alla leg press sfruttando realmente la dorsiflessione,"),
    (122.85, 126.40, "ma non devi cercare il massimo stretch possibile a qualsiasi costo."),
    (138.82, 145.20, "Il muscolo non cresce perché viene stirato, cresce perché riesce a produrre e tollerare tensione mentre è allungato."),
    (150.52, 160.25, "Per anni la regola è stata semplice: ripetizione completa buona, ripetizione parziale sbagliata."),
    (162.86, 168.42, "Poi sono arrivate le parziali in allungamento e internet ... è passato all'estremo opposto."),
    (245.70, 249.90, "Quindi la soluzione non è eliminare il ROM completo, è usarlo come base."),
    (268.96, 275.52, "Per esempio, puoi fare dei calf raise completi e, raggiunto il cedimento, aggiungere alcune parziali controllate nella parte bassa."),
    (308.83, 314.76, "Una parziale non è una ripetizione fatta male, è una ripetizione con un ROM deliberatamente scelto."),
    (321.75, 326.86, "Ed è questa intenzionalità che separa una tecnica avanzata da una serie semplicemente eseguita male."),
]
# internal pauses (silencedetect -42dB, d>=0.25) shrunk to KEEP_GAP
PAUSES = [(19.35, 19.83), (141.44, 141.87), (152.16, 152.59), (154.15, 154.53), (156.73, 157.28), (248.38, 248.72), (311.50, 312.02)]
KEEP_GAP = 0.18
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
t, cmap = 0.0, []
for a, b in pieces:
    cmap.append({"src_start": a, "src_end": b, "edit_start": round(t, 3)}); t += b - a
json.dump(cmap, open(OUT.replace(".mp4", ".cutmap.json"), "w"), indent=1)
print(f"{len(pieces)} pieces, expected duration {t:.2f}s")
