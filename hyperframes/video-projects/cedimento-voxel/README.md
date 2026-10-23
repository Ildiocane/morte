# cedimento-voxel — "Devi fallire ogni serie?"

Fully generated 50s vertical video in the blocky/voxel 3D style of the references Luca sent
(Instagram DeguJnIBGZZ, DeMH2VlBtco, DehJ0AdADwl, Deb42oAAR3g): two voxel characters talking in a gym,
shot/reverse-shot cuts, blurred background (depth-of-field feel), white captions with yellow keyword blocks, app-style UI inserts.

## Characters
- **Coach** (Luca): beard, brown hair, broad build, navy tee with **LB SYSTEM** printed on the chest; LB SYSTEM sign on the gym wall.
- **Novizio**: skinny, red cap, grey tank, blue shorts, sweaty and hunched at the start.

## Script (Luca's text, verbatim, split between the two)
Novice: "Devi fallire ogni serie?" … "Con meno fatica acuta?"; every other line is the coach's.

## Audio
Local TTS (Kokoro-82M ONNX, voice `im_nicola`); the novice is the same voice pitched up with rubberband (formants preserved).
These are placeholder synthetic voices — swap `assets/audio/dialogue.wav` for real recordings and re-run the caption/mouth steps.
Music bed at −20 dB, light SFX on UI pops.

## How it's built
- `scripts/tts.py <kokoro-models-dir>` → `assets/audio/lineNN.wav`, `assets/audio/dialogue.wav`, `assets/dialogue.json` (line timings).
- captions (`assets/captions.json`) are chunked per line with keyword highlights; `assets/mouth.json` is the per-frame RMS envelope per speaker (lip-sync).
- `scripts/index.tpl.html`: Three.js r160 (UMD, `assets/three.min.js`). Two WebGL canvases share one camera: `#bg` (gym, CSS-blurred per shot)
  and `#fg` (characters, sharp, transparent). Everything is driven deterministically from the GSAP timeline time.
- `python3 scripts/build.py && npx hyperframes render --quality standard --output renders/v1.mp4`
