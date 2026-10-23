# allungamento-parziali — "Allenamento in allungamento e parziali"

Luca's raw take (5:28, Italian, Google Drive `12pKRS4Fi10CmqUjrPVCOdm7nBY5m88t_`) → 86.6s Jeff Nippard–style edit.

## Rebuild
1. Download the raw take to `../../raw-media/v2/raw.mp4` (`gdown <id>`).
2. `python3 scripts/cut.py ../../raw-media/v2/raw.mp4 assets/edit.mp4` — 17 kept sentences (list + text in the script); every boundary verified by re-transcribing the clip.
3. `python3 scripts/build.py` → generates `index.html` from `scripts/index.tpl.html` + `assets/captions-final.json` + SFX list.
4. `npx hyperframes render --quality standard --output renders/final.mp4`, then loudnorm to −14 LUFS for social.

## Editorial choices
- Kept: hook (dogma), definition, 2026 meta-analysis, sarcomere myth + "Non lo è", practical exercises, "not max stretch at any cost", key line (tension, not stretch), full vs partial ROM story, "full ROM as base", calf-raise example, closing definition of a partial.
- Cut for length/repetition: restarted takes ("Allenarsi a lunghezze…", "La letteratura scientifica…" ×3), the "non è stretching con un peso" aside, the fascicle-length review detail, the "5 centimetri" line, the 16-study / upper-body / 2025-study section, the three-situations list, "studi recenti hanno investigato…", and the repeated "Una ripetizione parziale non è…".
- Zoom plan: slow push-ins on argument build-ups, hard punch-in (1.32×) on "Non lo è.", fast zoom-out on "estremo opposto", reset-wide on chapter changes.
- Color: desaturated/cool grade during the myth section, white flash back to normal at "Quindi, praticamente?", red tint on the "massimo stretch" warning, warmer grade on "tensione".
