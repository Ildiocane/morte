# coach-perche — "Quanti coach ti spiegano il perché?" (reel 9:16, 74 s)

Luca's selfie take, **no cuts**, voice untouched (original AAC muxed with `-c:a copy`), no music/SFX.
Added: forehead-height text (y≈470–700), word-by-word captions at chest height (active word on a red box),
vertical voxel b-roll (PDF guide on the phone ×2, slow-tempo squat), 2 full-screen graphics ("ti spiego il perché", "la prima programmazione è una bozza").

1. `assets/face.mp4` = upright video-only copy of the source (rotation applied, 60 fps, no cuts).
2. `assets/words.json` = whisper word timings with 3 fixes (allenamento, quegli, log in PDF).
3. `broll/` renders the vertical b-roll reel → split into `assets/broll/{pdf1,pdf2,squat}.mp4`.
4. `python3 scripts/build.py` → `index.html`; render `--fps 60`; then mux the source audio untouched.
