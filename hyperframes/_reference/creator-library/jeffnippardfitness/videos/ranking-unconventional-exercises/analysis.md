# ranking-unconventional-exercises — @jeffnippardfitness

**Source:** https://www.tiktok.com/@jeffnippardfitness/video/7607951419785612565
**Title:** Ranking unconventional exercises (one is S-tier!)
**Duration:** 78.21s
**Aspect:** 9:16
**Resolution:** 720x1280 (30fps)
**Studied:** 2026-10-11
**Engagement (at time of study):** 2.4M views · 129.8K likes · 270 comments (posted 2026-02-17)
**Sample rate:** 156 frames extracted at 2fps; reviewed at 1fps (78 frames) via labeled 3×2 contact sheets.

## Hook (0–2s)
- 0.0s: Jeff standing in a bright gym, hands clasped, talking to camera (right half of frame). On the left, a **filled-in S/A/B/C/D/F tier list** with a red-to-green glowing border, already holding exercise thumbnails (the finished result is shown up front). Caption at the TOP: "Rare and unconventional".
- ~1.0s: "exercises tier list!". A row highlight sweeps down the tiers.
- 3–4s: "These are weird, and only one is S-tier!" The S row flashes red. **That's the open loop:** "which one is S-tier?" keeps people watching to the end.
- 5s: hard cut to the first exercise demo.

## Pacing
- Total scenes: ~25
- Average scene length: ~3s
- Shortest / longest: ~1s / ~6s
- Distribution feel: rhythmic loop, repeated 7 times: **name card on demo → 2–3 demo angles while explaining → back to the tier list → verdict**
- Pace: steady; the "But!" twist at 69s restarts the loop for the final S-tier payoff at 75–77s

## Captions
- Style: phrase chunks of 1–5 words
- Font feel: white sans, medium weight, soft shadow
- Active-word treatment: none
- Position: **top of frame** (~8–12% down) in this video, so the bottom stays free for the exercise-name lower-third
- Size: medium
- Plus a second text layer: **exercise name in all caps** ("JEFFERSON CURL"), white bold sans, bottom-center (~85% down), shown for the first 2–3s of each segment

## Scene types
1. 0–4s — talking head + tier-list overlay (left 55% of the frame), final state shown as a teaser
2. 5–8s — exercise demo b-roll + ALL-CAPS name lower-third; **x-ray skeleton overlay** on the shoulder joint to show "strain"
3. 9–17s — Jefferson curl demo; **orange arc line drawn along the spine** to show flexion
4. 18–20s — back view; **anatomical muscle overlay fades in over the real back** (skin → muscle diagram)
5. 21–22s — tier list returns, the exercise thumbnail drops into the matching row (with a PiP of the clip + name)
6. 23–31s — reverse Nordic demo; quads tinted red to show the target muscle; verdict on the tier list
7. 32–40s — Keenan flaps; a **reference TikTok clip inset** (PiP top-right, the original creator's video); lats tinted red; verdict C
8. 41–52s — calf-machine shrug; **glowing brain x-ray on the head + glowing trap connection** for "mind-muscle connection"; verdict A
9. 53–57s — kipping pull-ups; **yellow arc arrows tracing the swing**; verdict F ("Not a fan.")
10. 58–68s — JM press; the **barbell recolored red/pink** while he talks about stabilizing it; verdict A
11. 69–74s — "But!" twist → Smith-machine JM press demo
12. 75–77s — final payoff: the Smith JM press lands in S-tier

## Transitions
- Flavors observed: hard cuts; tier-list rows highlight with a flash of their tier color; PiP thumbnails slide/scale into rows
- Rotation cadence: a predictable cycle (demo → list → demo)
- Signature transition: the **demo clip shrinks into a thumbnail and drops into its tier row**

## Face treatment
- Mode mix: full-body talking head (tier-list segments) and full-frame exercise demos
- Grading feel: bright, clean, cool-neutral white gym; high-key
- Ken Burns: minimal
- Framing: tier-list shots keep him on the right third with the list on the left

## Audio reactivity
- Text pulses on beat: no
- Visual hits land on the spoken verdict ("A-tier.", "C-tier.")

## Palette
- `#e9eaec` dominant: bright white/grey gym
- `#1d1d1f` tier-list fill / clothing
- Tier gradient: `#f0727a` S → `#f4a96b` A → `#f6d36e` B → `#e9ef6f` C → `#c9f07a` D → `#8ef08a` F
- `#f2b632` arc-arrow yellow, `#e0523f` muscle-highlight red

## Signature move
**Interactive tier list as the backbone:** show the finished list up front as a tease, then fill it one exercise at a time, each with a demo and a quick anatomy/physics overlay that justifies the verdict.

## What to steal (actionable for Hyperframes builds)
- **Tier-list overlay component**: 6 colored rows (S–F), glowing gradient border, thumbnails that scale-drop into rows. Build as a reusable composition with a `rows[]` JSON input; each verdict is one GSAP tween synced to the spoken "X-tier".
- **Tease-the-finished-state hook**: show the completed graphic for 2–3s, then wipe it and rebuild.
- **ALL-CAPS name lower-third** for each segment (bottom-center, 2–3s hold).
- **Anatomy overlays**: muscle tint (red glow over the target muscle), skeleton/joint x-ray, brain + nerve glow. Use PNG overlays with a `mix-blend-mode: screen` fade-in.
- **Motion-path arcs** (yellow SVG stroke-draw) to show momentum or range of motion.
- **"But!" twist** near the end to re-hook before the payoff.
- **Captions at the top** whenever the bottom is busy with a lower-third.

## What's creator-specific (don't copy literally)
- His exact exercise picks and verdicts, the "I rock with Keenan" callout to another creator, his gym and outfits.

## Transcript
See `transcript.json` in this folder. Whisper wrote "Stier/Dtier/Ctier/Ftier" for "S-tier…", "Kenan" for "Keenan", "Tipping" for "Kipping", "Not a fame" for "Not a fan", and "lap pulling" for "lat pull-in".
