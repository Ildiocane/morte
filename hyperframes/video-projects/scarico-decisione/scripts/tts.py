# Clone Luca's ElevenLabs voice sample (11.5 s) with Chatterbox Multilingual (MIT, local) and render every script chunk.
# usage: /root/cbx/bin/python scripts/tts.py [chunk_id ...]
import sys, os, time, torch, torchaudio as ta
sys.path.insert(0, os.path.dirname(__file__))
from script import SECTIONS
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
SEED = int(os.environ.get("SEED", 7)); torch.manual_seed(SEED)
REF = "assets/audio/voice-ref.wav"
OUT = "assets/tts"
want = set(sys.argv[1:])
if os.environ.get("THREADS"): torch.set_num_threads(int(os.environ["THREADS"]))
m = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
ALL = [c for _, _, ch in SECTIONS for c in ch]
if os.environ.get("REVERSE"): ALL = ALL[::-1]
for _ in [0]:
    for cid, text in ALL:
        if want and cid not in want: continue
        if os.path.exists(f"{OUT}/{cid}.wav") and not want: continue
        t0 = time.time(); torch.manual_seed(SEED)
        wav = m.generate(text, language_id="it", audio_prompt_path=REF, exaggeration=0.5, cfg_weight=0.5, temperature=0.7)
        ta.save(f"{OUT}/{cid}.wav", wav, m.sr)
        print(cid, round(wav.shape[-1] / m.sr, 2), "s in", round(time.time() - t0, 1), "s", flush=True)
