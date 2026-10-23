# rom-completo — "Basta con le ROM parziali: il lockout va benissimo"

Luca's raw take (1:14.6, Google Drive `191OyvCH-KxaDVWsiQTQ7EWmkqp1p8JSv`, phone selfie 1080×1920 @60 rotated) → 1:10.5.
Brief: **cut only the pauses, leave every word as spoken**; captions, images and slides on top, ≥2 full-screen graphics.

## Cut (`scripts/cut.py assets/raw.mp4 assets/edit.mp4 assets/raw16k.wav`)
Single segment, tight-cut per PREFERENCES: every silence ≤ −37 dB lasting ≥0.10 s shrunk to 60 ms (30 ms lead / 60 ms tail),
18 pieces, −4.2 s. Voice untouched apart from 10 ms fades at each joint. Verified by re-transcribing the cut audio
(`assets/transcript-edit.json`): all 211 words still there; longest remaining pause 0.25 s (at −33 dB).

## Captions (`scripts/captions.py`)
Hand-corrected text aligned onto the whisper words of the cut audio (fixes "ripienzione", "calcolo"→carico, "overed"→overhead).
≤3 words / ≤20 chars, never ending on a function word, plain white (Jeff Nippard style), on the shirt below the beard (y 1505).

## Graphics (`scripts/index.tpl.html` → `scripts/build.py` → `index.html`)
Slides stay in the top third (y 118–468, above the hairline). Colour per concept: blue brand/data, green correct, red myth/less,
yellow measurement.
- Slides: ROM PARZIALI hook · ultimi 2–3 anni + photo (cable fly) + "= più crescita?" · ~~ROM COMPLETO + lockout~~
  "perdi 1 cm di tensione!" / "🙄 per favore…" · "1 secondo dopo… già scendi" + tension curve + "tensione continua" ·
  overhead-extension pictogram (arm travels behind the head, stretch ↑ / forza ↓, "meno forte") · 🤯 + ~~l'angolo perfetto~~ ·
  end: ROM completo ✓ + @luca_bandiera_pt
- Full screen: FACCIAMO CHIAREZZA (ROM completo ✓, ROM articolare ✓, va benissimo) · TENSIONE PERSA IN LOCKOUT < 0,5 %
  (proportional bar with the 0.5 % sliver) · LOCKOUT ARTICOLARE (chest press + squat photos) · DI CONSEGUENZA chain
  (più stretch → meno forza → meno carico → meno tensione)
- Audio: voice at 1.0, library music bed at 0.045, 39 SFX (one per beat, never two within 0.25 s)

Photos (Pexels licence, free to use): chest press 3838926, squat 1552106, cable fly 5327505 —
`https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?w=1400` → `assets/img/{chest-press,squat,cable-fly}.jpg`.
