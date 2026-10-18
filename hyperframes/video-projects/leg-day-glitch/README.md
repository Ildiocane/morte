# leg-day-glitch

Vertical 1080×1920 gym edit (5 exercises). Built without the HTML pipeline: a numpy/PIL frame compositor, because the
text has to sit *behind* the athlete (matte from RobustVideoMatting).

Pipeline (run from this folder, Python env with torch/numpy/PIL/scipy/soundfile):

1. `assets/src.mp4`: source clip (not committed). Its own audio track is discarded.
2. `scripts/matte.py` → `assets/alpha.mkv` (RVM mobilenetv3 TorchScript, CPU, downsample 0.25)
3. `scripts/music.py` → `assets/music.wav`: the reference TikTok sound (`assets/song-snippet.wav`, ~11.8 s) looped on
   beat boundaries to 50.13 s (`assets/beats.json`)
4. `PYTHONPATH=scripts python scripts/layout.py` → `assets/layout.json`: per exercise, the name height where the athlete
   covers ~8 % of the letters (behind him, still readable) and a sets-label spot he never crosses
5. `scripts/compose.py` → `renders/video.mp4` (`--preview 3.0,13.5 outdir` writes single JPG frames)
6. `scripts/mix.py` + loudnorm −14 LUFS (TP −1.5) → `renders/mix.wav`, then mux

Per sequence: 3-shot photo burst (freeze, flash, shutter SFX, frozen cut-out clones), then the exercise name glitches in
huge behind the athlete (a faint outline of the hidden letters shows through him), with sets×reps on a red block. Extra glitch hits on music bars and cuts.

Fonts: Saira (OFL, Google Fonts) 900 italic / 800 italic / 900 → `assets/saira-*.ttf` (not committed).
