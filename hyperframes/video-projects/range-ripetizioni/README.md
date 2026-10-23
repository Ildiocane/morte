# range-ripetizioni — "Perché ci hanno mentito sul range di ripetizioni?"

Luca's raw take (2:00, Italian, Google Drive) → 55.5s Jeff Nippard–style edit.

## Rebuild
1. Download the raw take to `../../raw-media/luca-raw.mp4` (Drive file `1cFygrFhdp5_5BGzxHtNKRrbUx4brUe5e`, e.g. `gdown <id>`).
2. `python3 scripts/cut.py ../../raw-media/luca-raw.mp4 assets/edit.mp4` — cuts silences, the false start, the repeated sentence and side tangents (segment list + rationale inside the script; every boundary verified by re-transcribing the clip).
3. `npx hyperframes render --quality standard --output renders/range-ripetizioni-final.mp4`
4. Loudness for social: `ffmpeg -i in.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.0:LRA=11 -c:a aac -b:a 192k out.mp4`

`index.html` is generated from `scripts/index.tpl.html` + `assets/captions-final.json` (+ SFX list); edit the template, not the output.

## What was cut (source → kept)
- "Perché ti hanno mentito?" false start, "Me lo chiedo ancora ad oggi", "Per quanto mi ricordo precisamente", "beh, ecco"
- the "altri fattori biologici…" and "scarica spinale" tangents, "necessaria per le serie…"
- the repeated "non devi far altro che…" sentence (said twice) and the lateral-raise/shrug aside
- all pauses > 0.14s inside kept sentences
