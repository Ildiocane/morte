# scarico-decisione — "Scarico: decidere, non indovinare" (YouTube 16:9, ~13 min)

Faceless explainer for LB System / NEXUS Private Gym, narrated with Luca's ElevenLabs voice sample (cloned locally).

Pipeline (run from this folder):
1. `scripts/script.py` — full narration, expanded from Luca's minute-by-minute outline (one entry per TTS chunk).
2. `/root/cbx/bin/python scripts/tts.py [ids]` — Chatterbox Multilingual (MIT, local) cloning `assets/audio/voice-ref.wav`; `SEED=n` for retakes.
   `python3 scripts/validate_tts.py` re-transcribes every chunk and flags bad takes.
3. `python3 scripts/assemble.py` — joins chunks with fixed pauses -> `assets/audio/narration.wav`, `assets/timing.json`, word timings `assets/words.json`.
4. `broll/` — voxel 3D b-roll reel (NEXUS gym, squat, bench, row, bar, tired, sleep, eat, stress, physio, LB app);
   render it there, then `python3 scripts/split_broll.py` -> `assets/broll/*.mp4`.
5. `python3 scripts/build.py` — storyboard (`scripts/storyboard.py`) + scenes (`scripts/scenes.py`) + template -> `index.html`.
6. `npx hyperframes render`, then loudnorm -14 LUFS on the final file.

Media, the voice reference and Luca's logos are gitignored.
