# progressive-overload — "Che cos'è davvero il Progressive Overload?"

Luca's raw take (4:20, Italian, Google Drive `14HEoV-Wx1rmE00tA15gIcU7Vv1dX7TMt`) → 2:46 clean cut with captions + graphics.

## Audio policy (requested by Luca)
Voice audio is NOT processed: no loudnorm, EQ, compression, music or SFX. Only 10ms fades at each cut (click-free),
one AAC encode at 320 kbps (source is AAC 256k). The final MP4 muxes `assets/edit.mp4`'s audio stream as-is
(`-c:a copy`) over the rendered picture, bypassing the renderer's mixer.

## Rebuild
1. `gdown <id> -O ../../raw-media/v3/raw.mp4`
2. `python3 scripts/cut.py ../../raw-media/v3/raw.mp4 assets/edit.mp4`
3. `python3 scripts/build.py` (index.html from `scripts/index.tpl.html` + `assets/captions-final.json`)
4. `npx hyperframes render --quality standard --output renders/v1.mp4`
5. `ffmpeg -i renders/v1.mp4 -i assets/edit.mp4 -map 0:v -map 1:a -c copy -shortest renders/final.mp4`

## What was cut
- dead air between sentences and long internal pauses (kept 0.2s)
- the first, garbled "ma soltanto pochi… te l'hanno spiegato" (kept the clean retake)
- 3 false starts of "Molti pensano che ci siano tanti parametri…" (kept the 4th, complete take)
- the repeated "aumentare il carico a parità di ripetizioni"
- 8s of silence after "nel corso delle serie"
- 3 of the 4 CTA takes (kept "Se ti è piaciuto il video lascia like, commenta…, iscriviti" + "Ciao!")

## Graphics / colour
Hook title, creators cards, staircase "sovraccarico progressivo", parameter chips (3 struck out → 2 win),
MITO #1/#2/#3 with SBAGLIATO / CONTROPRODUCENTE stamps, TUT counter, rest timer 3:00→1:00, the 2 factors cards +
"BASTA." stamp, tonnage equation + rising bars, strength → cross-section, 5–30 rep range, "a parità di" locks,
"Nuovo muscolo" highlight, CTA. Colour: myths section desaturated + red pulses on each "sbagliato";
white flash and full colour back at "Quindi quali sono questi unici due fattori?"; flash on "Basta!";
warm grade on "nuovo muscolo". Zoom: punch-ins on key words, zoom-out after "Basta!", slow pushes elsewhere.
