# cedimento-voxel-v2 — "Devi fallire ogni serie?" con la voce di Luca

Same voxel world as `../cedimento-voxel`, rebuilt around Luca's own recording (`allenarti_criteri.m4a`, 48.2s).

## Audio
- **Coach (LB SYSTEM)** = Luca's recording from 3.75s to the end, untouched: decoded to 24-bit WAV, no cuts inside, no EQ/normalisation.
- **Novizio** = only "Devi fallire ogni serie?", replacing Luca's first 3.6s. Generated with ElevenLabs TTS
  (voice "Alfio Narra – Light Youthful Energy", eleven_v4, take 2 of 2), loudness-matched to Luca (−23 LUFS).
  A voice-changer pass on Luca's own take wasn't possible: the session cannot upload local files to ElevenLabs.
- "con meno fatica acuta" stays with the coach (ElevenLabs refused a second generation: free tier disabled).
- Final mix (`scripts/mix.py`): dialogue sample-exact + music −21 dB + SFX, `amix normalize=0`, AAC 320k.

## Build
`python3 scripts/prep_v2.py` (lines, captions, lip-sync envelope, v1→v2 time anchors) → `python3 scripts/build.py`
→ `npx hyperframes render --quality standard -o renders/v1.mp4` → `python3 scripts/mix.py renders/v1.mp4 renders/final.mp4`.
Shots and graphics keep their v1 authoring times; `T()` remaps them onto Luca's real line timings via `assets/anchors.json`.

## v2 audio (Luca: "musica molto bassa, voce più alta, niente rumore di fondo")
- Coach voice cleaned: `highpass=75, anlmdn (s=0.0015), afftdn nr=10, gentle compressor 2.5:1, +2.5 dB presence @3.5 kHz`
  → `assets/audio/coach-clean.wav` (room noise −37 → −50 dBFS; a gate variant was rejected because it ate consonants).
- Dialogue normalised to −14 LUFS (TP −1.2) → `dialogue-clean.wav`; music bed at −43 LUFS (~29 dB under the voice); SFX −4.4 dB.
- Video stream reused from `renders/v1.mp4` (`python3 scripts/mix.py renders/v1.mp4 renders/final-v2.mp4`).
