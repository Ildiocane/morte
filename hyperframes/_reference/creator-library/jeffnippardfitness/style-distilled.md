# @jeffnippardfitness — Style Fingerprint

Rolled up across 5 videos. See `videos/*/analysis.md` for per-video detail. Last distilled: 2026-10-11.

## Signature moves (consistent across videos)
- **Hook pattern:** a direct question or a common belief in the first sentence ("Which matters more…", "On a bulk, how fast…", "Most people think 45°…", "If you've been out of the gym…"), with the **visual demonstrating the concept within 1–2s** (color-coded arrow, angle readout, muscle tint, a finished tier list as a tease). No title card, no face-only intro; he's already demonstrating.
- **Caption treatment:** white sans (Inter/SF-like), medium-bold, soft drop shadow, **no stroke, no box, no karaoke highlight**; 1–5-word phrase chunks swapped on speech. Position moves (top / center / lower) to stay out of the way of graphics, and captions are **hidden entirely during data-heavy chart scenes**.
- **Transition rotation:** almost exclusively **hard cuts**. Motion lives *inside* scenes (graphics popping, arrows drawing, bars growing), not in transitions.
- **Face treatment:** fullscreen talking head (medium or full-body) alternating with fullscreen exercise demos; occasional split-screen (A vs B) and PiP face card during charts. Clean, premium gyms/studios; grading neutral-cool with soft contrast.
- **Palette:** neutral base (black/charcoal or bright white gym) + **one semantic color per concept**, kept consistent within a video (yellow vs red, green vs grey-blue, blue = data). Yellow `#f5c518`-ish recurs as the "measurement/highlight" color in all 5.
- **Energy profile:** steady and authoritative, no hype. Pace 2–3s per beat with longer holds while a chart builds; ends on a calm, honest takeaway (often with a caveat), sometimes a sponsor CTA.

## What to steal (ranked by Hyperframes copy-ability)
1. **Semantic color-coded concept pills + matching motion arcs**: small rounded label (bold caps) scale-pops near the subject; an SVG arrow draws along the movement path in the same color. → GSAP `back.out` + `strokeDashoffset`.
2. **Progressive bar chart (one bar per spoken stat)** over a blurred, darkened background clip, with count-up numbers and the newest bar in the accent color. → `data-chart` registry block or custom SVG; blur via a wrapper `filter`.
3. **Study-citation beat**: paper title page slides in, a yellow highlighter swipe (`scaleX` 0→1) marks the key phrase; optional fan-out of many pages = "lots of evidence."
4. **Muscle / object tint overlays**: red = target or "too much", green = correct, blue = measured. Semi-transparent shape with `mix-blend-mode: screen|multiply`, fade in on the keyword.
5. **Persistent structure UI**: chapter tabs (WEEK 1/2/3) or a tier list (S–F) that stays on screen and updates as the video progresses. Viewers always know where they are.
6. **Frosted-glass number pills** (`backdrop-filter: blur`) for quick stats ("↓ 20–50%", "0.7 g/lb", "10 mins of cardio").
7. **Pictogram people grids** that stagger in and split/recolor into study groups.
8. **Live measurement overlays** (angle line + ticking degree counter, height ruler).
9. **Top-third graphics zone**: keep the subject in the lower ~60% so overlays never cover the face.
10. **Re-hook twist near the end** ("But!") before the payoff, and **tease the finished state** in the hook (completed tier list / final chart).

## Don't copy
- His sponsor (MacroFactor) segments and app UI, his studio wall branding ("The Jeff Nippard Muscle"), his catchphrases ("science-based lifter", "I rock with Keenan").
- His exact studies, numbers and verdicts. Luca must cite his own sources and data.
- His specific yellow/red pairing as a brand signature: borrow the *system* (one semantic color per concept) and use Luca's own palette (`assets/brand-tokens.css`).

## Videos studied
- [negative-vs-positive-muscle-growth](videos/negative-vs-positive-muscle-growth/analysis.md): yellow POSITIVE vs red NEGATIVE pills + arc arrows, split-screen, forest-plot chart (41s, 1.4M views)
- [how-fast-to-gain-weight-on-bulk](videos/how-fast-to-gain-weight-on-bulk/analysis.md): seated explainer with in-scene monitor graphics, pictogram groups, highlighter swipes, building bar chart, whiteboard (75s, 5.0M views)
- [ranking-unconventional-exercises](videos/ranking-unconventional-exercises/analysis.md): persistent S–F tier list, anatomy/x-ray overlays, "But!" twist (78s, 2.4M views)
- [upper-pec-activation-every-incline](videos/upper-pec-activation-every-incline/analysis.md): self-experiment with an EMG sensor, angle readouts, progressive bar chart over blurred footage (56s, 4.9M views, best like rate)
- [if-you-lost-muscle-do-this-first](videos/if-you-lost-muscle-do-this-first/analysis.md): WEEK 1/2/3 chapter tabs, frosted-glass stat pills, muscle tint, height ruler (48s, 3.7M views)
