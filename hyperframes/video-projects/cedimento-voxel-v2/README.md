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
