# Generate the dialogue with Kokoro (local TTS): coach = im_nicola, novice = im_nicola pitched up (rubberband).
# Writes assets/audio/lineNN.wav and assets/dialogue.json with per-line timing on the final timeline.
import json, subprocess, sys, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
MODELS = sys.argv[1]
k = Kokoro(MODELS + "/kokoro-v1.0.onnx", MODELS + "/voices-v1.0.bin")
LINES = [
    ("novice", "Devi fallire ogni serie?"),
    ("coach", "Se valuti l'allenamento solo da quanto sei distrutto, rischi di confondere la fatica con l'efficacia."),
    ("coach", "Per costruire muscolo serve uno sforzo adeguato, ma arrivare sempre al punto di non completare un'altra ripetizione non è obbligatorio."),
    ("coach", "In uno studio di otto settimane, allenarsi lasciando una o due ripetizioni in riserva ha prodotto una crescita del quadricipite simile al cedimento."),
    ("novice", "Con meno fatica acuta?"),
    ("coach", "Attenzione: due ripetizioni in riserva devono essere una stima credibile, non cinque ripetizioni mascherate."),
    ("coach", "Programma lo sforzo in base all'esercizio e a come recuperi."),
    ("coach", "Il cedimento può essere uno strumento; usarlo sempre non garantisce di più."),
    ("coach", "La qualità delle ripetizioni deve restare controllabile."),
    ("coach", "Seguimi per allenarti con criterio."),
]
SR = 24000; LEAD = 0.6; GAP_SAME = 0.28; GAP_SWITCH = 0.42
t = LEAD; out = []; prev = None; full = [np.zeros(int(LEAD * SR))]
for i, (who, text) in enumerate(LINES):
    s, sr = k.create(text, voice="im_nicola", speed=1.08 if who == "coach" else 1.14, lang="it")
    s = np.asarray(s, dtype=np.float32)
    # trim TTS leading/trailing silence
    nz = np.where(np.abs(s) > 0.01)[0]; s = s[max(0, nz[0] - 240): nz[-1] + 480]
    f = f"assets/audio/line{i:02d}.wav"; sf.write(f, s, SR)
    if who == "novice":
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", f, "-af", "rubberband=pitch=1.22:formant=preserved", f + ".tmp.wav"], check=True)
        s, _ = sf.read(f + ".tmp.wav", dtype="float32"); subprocess.run(["mv", f + ".tmp.wav", f])
    if prev is not None:
        g = GAP_SAME if prev == who else GAP_SWITCH
        full.append(np.zeros(int(g * SR))); t += g
    out.append({"i": i, "who": who, "text": text, "start": round(t, 3), "end": round(t + len(s) / SR, 3)})
    full.append(s); t += len(s) / SR; prev = who
full.append(np.zeros(int(1.4 * SR)))
sf.write("assets/audio/dialogue.wav", np.concatenate(full), SR)
json.dump(out, open("assets/dialogue.json", "w"), ensure_ascii=False, indent=1)
for o in out: print(f"{o['start']:6.2f}-{o['end']:6.2f} {o['who']:6s} {o['text']}")
print("total", round(t + 1.4, 2))
