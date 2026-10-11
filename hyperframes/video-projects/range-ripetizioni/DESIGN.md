# DESIGN — range-ripetizioni

## Style Prompt
Evidence-based fitness explainer in the style of @jeffnippardfitness (see `_reference/creator-library/jeffnippardfitness/style-distilled.md`). Luca talks to camera, full-screen vertical, in front of a light wall. Clean, calm, credible: hard cuts with subtle punch-in zooms to hide jump cuts, plain white captions, and purposeful motion graphics that *prove* each claim (a rep-range scale, a study card with a highlighter, a stacking list of negatives, rep-range cards). Graphics live in the top zone above Luca's head (y 60–500); captions sit under his chin (~y 1480).

## Colors
- `#0a0a0f` — ink (card text, scrims) — from brand-tokens `--brand-bg`
- `#ffffff` — card fill / captions
- `#3b82f6` — brand accent (`--brand-accent`): neutral data, active highlight
- `#22c55e` — semantic GOOD (the recommended 5–10 rep zone)
- `#ef4444` — semantic BAD (12–15+ reps, "sbagliato", negatives)
- `#f5c518` — highlighter yellow (study card, emphasis)

One semantic color per concept, consistent all video: green = good range, red = bad range, yellow = evidence highlight.

## Typography
- Inter (800 for labels/pills, 700 for captions, 600 for body)
- Captions: Inter 700, 58px, white, layered dark text-shadow (no box, no karaoke) — Jeff style
- Numbers: `font-variant-numeric: tabular-nums`

## What NOT to Do
- No flashy shader/whip transitions, no glitch, no neon — this is a calm science explainer
- No graphics over Luca's face (face spans y ≈ 530–1400)
- No karaoke word highlighting or caption pills
- Don't name or fake a specific study title — Luca didn't cite one; the study card is a generic "lo studio" visual
- No more than one SFX per beat; SFX −14 dB or more under voice, music bed ≈ −24 dB
