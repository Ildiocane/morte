# upper-pec-activation-every-incline — @jeffnippardfitness

**Source:** https://www.tiktok.com/@jeffnippardfitness/video/7605986132278611221
**Title:** I tested my upper pec activation at every incline (from flat to vertical)
**Duration:** 56.28s
**Aspect:** 9:16
**Resolution:** 720x1280 (30fps)
**Studied:** 2026-10-11
**Engagement (at time of study):** 4.9M views · 278.2K likes · 606 comments (posted 2026-02-12). Highest like rate of the five studied.
**Sample rate:** 113 frames extracted at 2fps; reviewed at 1fps (56 frames) via labeled 3×2 contact sheets.

## Hook (0–2s)
- 0.0s: side view of an adjustable bench in a bright gym. A hand raises the backrest; a **yellow line traces the backrest with a live angle readout "25°"** that ticks up as it moves. Caption "Most people think".
- ~1.0s: backrest at "55°", Jeff peeking in from behind the bench. Caption "a 45° incline".
- ~2.0s: cut to Jeff shirtless with an EMG sensor on his upper chest, smirking. "is the best angle".
- ~3.0s: the upper-pec area is **tinted blue** while he taps it ("for the upper chest").
- Hook formula: **common belief + "I tested it myself"**. A personal experiment; viewers want the result.

## Pacing
- Total scenes: ~20
- Average scene length: ~2.8s
- Shortest / longest: ~1s / ~6s (the chart holds)
- Distribution feel: a strict A/B loop per data point: **lift at angle X (with angle readout) → chart scene where the new bar grows** (6 iterations: 0°, 15°, 25°, 45°, 65°, 90°)
- Pace shift: the chart beats get faster as the pattern becomes familiar; slows at the end for caveats + takeaway

## Captions
- Style: phrase chunks of 1–4 words
- Font feel: white sans, medium, soft shadow
- Active-word treatment: none
- Position: lower-middle in the opening; **top area (~15% down) later in the video**; **no captions at all during the chart scenes**, where the chart carries the information
- Size: medium

## Scene types
1. 0–1.5s — b-roll bench with an animated angle overlay (yellow line + "25°/55°" counter)
2. 2–3s — talking head (shirtless, EMG sensor), muscle region tinted blue
3. 4–5s — lift demo, Smith incline press
4. 6–8s — **split-screen top/bottom**: close-up of sticking on the EMG sensor (green glow ring around it) / laptop showing a live green EMG waveform
5. 9s — bench on a seamless white background (clean product shot)
6. 10–12s — flat bench press with a yellow bench-outline highlight + "0°" label
7. 13–15s — **chart scene**: blurred gym background, white axis, labeled "% MVC (UPPER PEC)", x-axis 0°…90° with **little bench-icon thumbnails** under each label, PiP of Jeff (blue-tinted pec) at the top. The new bar grows in blue with a **count-up %** (48%→59%); old bars turn white.
8. 16–41s — the loop repeats for 15°, 25°, 45°, 65°, 90°; the chart zooms in with a big white arrow on a surprising value ("66%"), x-axis labels turn yellow to group them
9. 42–46s — chart recap: 45° winner bar highlighted, then 15–45° bars all turn blue ("basically the same")
10. 47–49s — demo with a yellow curved line showing back arch
11. 50–52s — talking head caveats + a study title page with the key phrase highlighted ("Acutely Measured Surface EMG Amplitude…")
12. 53–56s — demo + "The real takeaway: pick an angle that you feel working" (no CTA graphic)

## Transitions
- Flavors observed: hard cuts; the chart scene uses a **blurred, darkened version of the same footage** as its background, so live action and chart feel like one space
- Rotation cadence: strict alternation (demo ↔ chart)
- Signature transition: blur-to-chart, then cut back to the sharp lift

## Face treatment
- Mode mix: full-body demos and medium talking head; face appears as a PiP card during charts
- Grading feel: bright, clean, cool-white gym, neutral skin
- Framing: centered; demos shot at a 3/4 angle so the bench angle is readable

## Audio reactivity
- No beat sync; bar growth and % count-up land on the spoken number

## Palette
- `#e8e9eb` dominant: bright white gym
- `#1f1f22` black: equipment, chart scrim
- `#1f5fae` data blue: active bar, muscle tint
- `#f5c518` measurement yellow: angle lines, labels, highlight
- `#ffffff` chart bars and axis
- `#3fe07a` EMG/tech green (sensor glow, waveform)

## Signature move
**Turn himself into the experiment:** a physical test, measured live (EMG), with the result plotted as a bar chart that builds one bar per test and alternates with the footage that produced each bar.

## What to steal (actionable for Hyperframes builds)
- **Live measurement overlay**: SVG line locked to an object + a numeric counter tweening (e.g. angle 0→55°). Reusable for angles, reps, tempo, weight.
- **Progressive bar chart that builds one bar per test**: one bar per test, new bar in the accent color with a % count-up, previous bars fade to white; x-axis with small pictogram icons. Background = blurred + darkened clip of the last scene (CSS `filter: blur(16px) brightness(.5)` over the video wrapper).
- **Chart zoom + arrow** on the surprising data point.
- **Muscle tint**: a semi-transparent colored shape over the target muscle (blue here, red in other videos).
- **Hide captions during data-heavy scenes**, so the graphic does the talking.
- **Caveat beat with a study page** before the takeaway, which builds trust.

## What's creator-specific (don't copy literally)
- The EMG hardware, his own measured numbers, the shirtless lab-test format. Luca can borrow the *experiment* format with his own tests and data.

## Transcript
See `transcript.json` in this folder. Whisper wrote "45 degrees, one" for "45 degrees won". The spoken 15° number ("64%") differs from a mid-animation chart frame (41% while counting up).
