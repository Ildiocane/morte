# sonno-recupero — "Il sonno non è tempo perso"

Luca's finished take (43.6s, Italian, Dropbox `scroipt-con-forshadowing.mp4`) → same cut, same audio, with overlays.

## Rules for this edit (requested by Luca)
- **No changes to the audio or video track**: no cuts, zooms or colour filters. The final MP4 copies the
  original audio stream (`-c:a copy`) and renders at the source's 60 fps; only overlays are added.
- Two **full-screen overlays** turn two passages into voiceover segments:
  1. 11.2–16.3s "È mentre dormi che recuperi davvero, che produci ormoni, che costruisci adattamento." —
     night scene: moon, stars, hypnogram line drawing, three ✓ benefit cards.
  2. 17.95–23.45s "Netflix, telefono, TikTok fino alle 2. Poi entrate in palestra stanchi…" —
     phone with app screen time and a clock running 23:00→02:00, then a draining battery + falling performance line.

## Overlays (top zone, above the head)
Dieta ✓ / Sonno ✕ 4 ore + PAGLIACCIO stamp · calorie ✓ snack ✓ 03:00 + GENIALE. · Recupero = Cibo + **Sonno** ·
Sonno = "dettaglio" (struck) · Corpo stanco → ~~Costruzione~~ · Dieta ✓ Allenamento ✓ Recupero ✕ + SABOTAGGIO ·
~~Tempo perso~~ → Parte del processo · Fisico serio = Recupero serio · balance Recupero ⇄ Allenamento + **Seriamente.**
Captions: Jeff-style white phrase chunks on the chest (y≈1260), kept on during the voiceover panels.

## Rebuild
1. `curl -L "<dropbox link with dl=1>" -o ../../raw-media/v4/raw.mp4`
2. `ffmpeg -i raw.mp4 -c:v libx264 -crf 12 -g 60 -keyint_min 60 -c:a copy assets/source.mp4` (seek-friendly copy for the renderer)
3. `python3 scripts/build.py && npx hyperframes render --quality standard --fps 60 --output renders/v1.mp4`
4. `ffmpeg -i renders/v1.mp4 -i ../../raw-media/v4/raw.mp4 -map 0:v -map 1:a -c copy -shortest renders/final.mp4`
