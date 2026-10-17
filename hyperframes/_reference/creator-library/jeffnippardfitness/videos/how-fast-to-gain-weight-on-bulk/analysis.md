# how-fast-to-gain-weight-on-bulk — @jeffnippardfitness

**Source:** https://www.tiktok.com/@jeffnippardfitness/video/7610877939973934356
**Title:** How fast should you gain weight on a bulk? (Beginner to advanced)
**Duration:** 75.09s
**Aspect:** 9:16
**Resolution:** 720x1280 (29.97fps)
**Studied:** 2026-10-11
**Engagement (at time of study):** 5.0M views · 151.1K likes · 1,457 comments (posted 2026-02-25)
**Sample rate:** 150 frames extracted at 2fps; reviewed at 1fps (75 frames) via labeled 3×2 contact sheets.

## Hook (0–2s)
- 0.0s: Jeff seated on a stool in his office/studio (shelves, desk, monitor), wide-ish shot, talking to camera. The desk monitor beside him shows a lean shredded physique photo. Caption "On a bulk,".
- ~1.0s: the monitor image swaps to an overweight "dirty bulk" photo. Caption "you gain weight?".
- ~2.0s: the monitor now shows a simple "WEIGHT GAIN →" stacked bar chart (green MUSCLE block, yellow FAT block).
- Spoken hook: "On a bulk, how fast should you gain weight?" A direct question to the audience, with visual contrast (lean vs fat) **inside a physical prop on set** (the screen), not as an overlay.

## Pacing
- Total scenes: ~12 (shot-level), but graphics change every 1–3s
- Average scene length: ~6s per camera setup, ~2s per graphic beat
- Shortest / longest: ~1s (monitor swaps) / ~14s (whiteboard sequence 47–68s)
- Distribution feel: long camera holds, kept fresh by graphics constantly building on top
- Shift: info-dense overlays in the first half → slower, more personal whiteboard section → product CTA

## Captions
- Style: phrase chunks of 1–4 words, swapped in sync with speech
- Font feel: white sans, medium-bold, soft shadow, no box
- Active-word treatment: none
- Position: center-frame (about chest height, ~55% down) in seated shots; a little lower in standing shots
- Size relative to frame: medium

## Scene types
1. 0–7s — talking head (seated, wide) + **in-scene monitor graphic** cycling lean photo → fat photo → MUSCLE/FAT stacked bar → "UNREALIZED GAINS" ghost block
2. 8s — talking head + study abstract page overlaid top-center, label pill "TRAINED LIFTERS"
3. 9–11s — talking head + **pictogram people icons** (rows of white human figures) under "TRAINED LIFTERS" + "8 WEEKS" pill
4. 12–20s — pictograms split into two groups, green = SLOW BULK 🥗, blue-grey = FAST BULK 🍔, with "1%/month" / "3%/month" labels popping above
5. 21–25s — study "Conclusions" text with **yellow highlighter swipes** on key phrases, final phrase zoomed big ("increased their skinfold thicknesses more")
6. 26–27s — back to the monitor: a gauge/speedometer graphic Beginner → Intermediate → Advanced with a pointer
7. 28–46s — new angle (frontal, branded wall), "NEW LIFTERS" pill + study page → pictogram grid → "Normal Diet + 2010 kcal" / "4 DAYS/WEEK" tags → **bar chart that grows bar by bar** (Body Mass grey, Fat-Free green, Fat yellow-tiny)
8. 47–60s — whiteboard scene: handwritten "NEW LIFTERS 0.5–1%", **yellow highlighter boxes added digitally** to each line as he speaks
9. 61–68s — he erases the board and hand-writes "AFTER 6 MONTHS 1%/month" (real-world motion; close-up insert of the marker)
10. 69–75s — sponsor CTA: phone mockup of the app UI on the left, him leaning on a machine on the right

## Transitions
- Flavors observed: hard cuts between camera angles; overlays pop/scale in and out
- Rotation cadence: angle changes every ~10–20s, graphics every 1–3s
- Signature transition: graphics change *inside* the scene (monitor, whiteboard) instead of cutting away

## Face treatment
- Mode mix: fullscreen talking head (seated wide, frontal medium, standing at the whiteboard), graphics layered on the upper third
- Grading feel: neutral/warm interior, soft contrast, clean premium office
- Ken Burns: slight push-ins
- Framing: the upper ~40% is kept empty for graphics; the subject sits in the lower 60%

## Audio reactivity
- Text pulses on beat: no
- Background reactivity: no
- Every graphic beat lands on the spoken number or keyword ("1%", "3%", "8 weeks", "six and a half pounds")

## Palette
- `#2b2d30` dominant: dark charcoal set
- `#f4f4f4` overlay cards: white paper / chart backgrounds
- `#4f6b4f` "good" green: muscle, slow bulk, fat-free mass
- `#e5b23a` highlight yellow: fat, highlighter swipes
- `#7f8a99` neutral blue-grey: fast-bulk group

## Signature move
**Data storytelling on top of a talking head:** each claim gets a quick visual (pictograms → groups → % labels → bar chart building one bar per spoken stat), always in the top third so his face stays visible.

## What to steal (actionable for Hyperframes builds)
- **Pictogram group visual**: a grid of person icons that stagger in, then split/recolor into groups (Slow vs Fast). GSAP `stagger` + recolor; good for "N people in the study".
- **Highlighter swipe on text**: yellow rect scaling on `scaleX` from 0→1 behind a phrase, then that phrase zooms out of the paragraph. Works for quotes, study conclusions, rules.
- **Bar chart that builds one bar per spoken stat**, synced to transcript timestamps (`data-chart` registry block or a custom SVG).
- **Top-third overlay zone**: keep the subject in the bottom 60% and float label pills + graphics above.
- **Small label pills** ("NEW LIFTERS", "8 WEEKS") as section headers, white fill with black text and a second grey pill stacked under it.
- **Phone mockup CTA** for any app/product mention (`app-showcase` block).

## What's creator-specific (don't copy literally)
- The MacroFactor sponsor segment and app UI, "The Jeff Nippard Muscle" wall branding, his studio set.
- Cited studies (Helms et al., Rozenek). Luca should cite his own sources.

## Transcript
See `transcript.json` in this folder. Whisper wrote "Rosenic" for "Rozenek" (the on-screen caption spells it correctly) and "macro factor" for "MacroFactor".
