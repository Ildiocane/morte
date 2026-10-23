# negative-vs-positive-muscle-growth — @jeffnippardfitness

**Source:** https://www.tiktok.com/@jeffnippardfitness/video/7652093298256923924
**Title:** Negative vs positive: what's more important for muscle growth?
**Duration:** 41.52s
**Aspect:** 9:16
**Resolution:** 720x1280 (30fps)
**Studied:** 2026-10-11
**Engagement (at time of study):** 1.4M views · 91.3K likes · 538 comments (posted 2026-06-16)
**Sample rate:** 83 frames extracted at 2fps; reviewed at 1fps (42 frames) via labeled 3×2 contact sheets.

## Hook (0–2s)
- 0.0s: wide shot, Jeff doing alternating dumbbell curls in a dark, premium gym (black walls, white LED strip lights on the ceiling). Caption "Which matters more" in white sans, lower-middle.
- ~1.0s: hard cut to a tight side-profile curl. A tiny yellow pill label "POSITIVE" pops in and scales up, and a yellow curved arrow starts drawing from the dumbbell.
- ~2.0s: the "POSITIVE" pill is full size, and the yellow arc arrow traces the full curl path upward. Caption "weight up,".
- Spoken hook: "Which matters more for muscle growth: the positive, where you lift the weight up, or the negative…" The question is the hook, and the visuals *demonstrate* the two terms immediately.

## Pacing
- Total scenes: ~14
- Average scene length: ~3.0s
- Shortest / longest scene: ~1.0 / ~6.0
- Distribution feel: medium. Fast cuts in the hook (1s), then 3–6s holds whenever a graphic is building.
- Pace slows for the data reveal (bar chart 26–34s) and ends on a calm talking-head conclusion (35–41s).

## Captions
- Style: phrase chunks of 1–4 words, swapped in sync with speech (no karaoke highlight)
- Font feel: clean white sans (SF/Inter-like), medium-bold, with a subtle drop shadow and no stroke or pill
- Active-word treatment: none; the whole chunk appears at once
- Position: center-lower (~70% down the frame), consistent throughout
- Size relative to frame: medium

## Scene types
1. 0–1s — b-roll demo, wide curl + caption (hook)
2. 1–2.5s — side-profile curl + yellow "POSITIVE" pill + yellow arc arrow (annotated demo)
3. 3–4.5s — same angle, red "NEGATIVE" pill + red arc arrow downward (annotated demo)
4. 5s — wide, Jeff standing (b-roll transition beat)
5. 6–8s — curl close-up, red downward arrow + red muscle-highlight overlay on the biceps ("lengthening")
6. 9–13s — wide curl, dumbbells recolored solid green on "control the negative" (color-recolor trick)
7. 14s — talking-head face-cam, medium close-up ("But…")
8. 15–17s — talking head + floating paper thumbnails with big red "?" marks behind the head (question beat)
9. 18–21s — talking head + the real meta-analysis title page with a yellow highlighter on the title, then a grid of study pages fanning out; callout "(682 subjects included in the meta-analysis)"
10. 22–30s — **split-screen top/bottom**: top = POSITIVE (yellow pill), bottom = NEGATIVE (red pill), dark "UPPER BODY" label in the middle; full-frame yellow / red color flashes on each side; a yellow/red forest-plot style bar chart animates in
11. 31–34s — leg extension b-roll, "LOWER BODY" label, the same bar chart now centered at ~0 (tie)
12. 35–41s — talking head, full body, gestures to camera, conclusion (outro, no CTA graphic)

## Transitions
- Flavors observed: hard cuts throughout; brief full-frame color washes (yellow/red tint flash) when each split-screen half is called out
- Rotation cadence: almost always a hard cut; the movement comes from on-screen graphics, not transitions
- Signature transition: none. Cuts are invisible, and the graphics do the work.

## Face treatment
- Mode mix: fullscreen talking head (medium close-up and full-body) alternating with fullscreen exercise b-roll; split-screen b-roll in the data section
- Grading feel: cool, desaturated, contrasty; crushed blacks; clean white practical lights
- Ken Burns: subtle slow push-ins on talking head
- Framing: centered, shot from slightly below; he's often partially out of frame (dynamic)

## Audio reactivity
- Text pulses on beat: no
- Background reactivity: no
- Color flashes land exactly on the spoken words "positive" and "negative"

## Palette
- `#111214` dominant: gym black/charcoal
- `#e9e9ea` neutral: concrete/white light strips
- `#e8b230` accent A: "positive" yellow
- `#b5202b` accent B: "negative" red
- `#3cc84a` occasional highlight: green recolor ("do this")

## Signature move
**Science explained on top of real lifting footage:** two opposing concepts each get a color (yellow vs red pill + arc arrow), and those colors carry through to split-screens and charts so viewers *see* the result before he says it.

## What to steal (actionable for Hyperframes builds)
- **Color-coded concept pills**: small rounded-rect label (bold caps, 2-color fill) that scale-pops in at ~0.2s, placed near the subject. Map to a reusable `concept-pill` component with GSAP `back.out` scale.
- **Hand-drawn arc arrows tracing the movement path**: SVG path + `strokeDashoffset` draw-on over 0.6–0.8s, colored to match the pill.
- **Split-screen A/B comparison with a center label** ("UPPER BODY") and a full-frame tint flash on whichever side is speaking.
- **Study-citation stack**: paper title page with a highlighter swipe across the title, then a fan-out grid of pages = "lots of evidence". Use the `color-recolor` + stagger patterns in MOTION_PHILOSOPHY.md.
- **Simple two-color result chart** (yellow vs red bars with a tick axis) for one stat per video.
- **Object recolor** (dumbbells turn green) to flag "this is the right way".

## What's creator-specific (don't copy literally)
- His physique/gym set, the "science-based lifter" phrase, citing specific meta-analyses. Luca should use his own studies and wording.
- The exact yellow/red pairing is fine to borrow as a *pattern*, but pick Luca's own two concept colors for brand ownership.

## Transcript
See `transcript.json` in this folder.
