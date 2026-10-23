# carico-conta — "Il carico è l'unica cosa che ti deve interessare (o quasi)"

Luca's take (1:00.5, Google Drive `1vHIpK1rfAmhXGiy9j4aAMpDss4TB4464`, phone selfie stored 1920×1080 rotated 90°).
Brief: **no cuts, the video stays as it is**; pop-ups + subtitles in the LB System / NEXUS brand colours; two dynamic
full-screen slides with images, B-roll and effects.

## Source (`assets/face.mp4`)
`ffmpeg -i assets/raw.mp4 -map 0:v -map 0:a -c:v libx264 -crf 14 -pix_fmt yuv420p -r 30 -g 30 -c:a copy assets/face.mp4`:
rotation baked in, 29.99 fps VFR → 30 fps CFR (one duplicated frame, nothing removed), audio stream copied bit-for-bit
(same md5 as the raw take).

## Captions (`scripts/captions.py`)
Hand-corrected text ("o quasi l'unica roba", "senza montagne di massa muscolare", "prima diventi forte e poi c'è il
muscolo") aligned onto the whisper words; ≤3 words, never ending on a function word; Saira italic, keywords in NEXUS red.

## Brand
NEXUS Private Gym (white/black, red X, heavy italic, slanted speed bars) + LB System mark (grey outline, red core,
drawn as an SVG symbol in `scripts/build.py`). Palette: ink #0b0b0d, white #f4f4f5, NEXUS red #a8171a, LB red #c0241e,
accent #ef4b40, grey #c2c2c2. Font: Saira (OFL) in `assets/fonts/`. Logos in `assets/img/nexus-*.png` (not committed).

## Graphics (`scripts/index.tpl.html` → `scripts/build.py` → `index.html`)
Pop-ups in the top third (y 110–470): IL CARICO / l'unica cosa che conta *o quasi · checklist tecnica / stesso ROM /
recupero · "Ok? Non vuoi sentire altro." + PUOI ESSERE FORTE anche senza montagne di massa · 1 · FORZA → 2 · MUSCOLO ·
3 rules → E CRESCERAI. BASTA. · + CARICO, SEMPRE + 4–10 rep range bar.
Full screen (NEXUS slanted-bar wipe in/out, flash, glitch slices, speed lines, red glow):
1. 14.05–20.15 — B-roll plate close-up → squat; IL CARICO DEVE AUMENTARE, CARICO ↑ → FORZA ↑ → IPERTROFIA ↑ + physique
   photo, rising red line + LINEARE.
2. 45.55–53.45 — B-roll loading a plate; AUMENTA SEMPRE, +1 kg → +1,5 kg, microplates (1,25 / 1 / 0,5) sliding on the
   sleeve, MICROCARICHI, impercettibili… → …ma IMPORTANTI.
Audio: original voice, library music bed at 0.04, 40 SFX (never two within 0.25 s).

Stock (Pexels licence, free to use): videos 5837709 (plate, 1.5–4.2 s), 5319755 (squat, 7–11.2 s), 5320015
(loading, 4.6–12.6 s) via `https://www.pexels.com/download/video/<id>/`; photo 896061 → `assets/img/physique.jpg`.
B-roll grade: `crop` to 9:16, `eq=saturation=0.3:contrast=1.08:brightness=0.02:gamma=1.18`, 1080×1920 @30.
