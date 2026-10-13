# PREFERENCES — Your Video Taste

Your accumulated taste for video work in this workspace. Populated over time via the `/feedback` skill.

**Read this file BEFORE every video task.** Apply the rules as overrides — they win over default skill choices and `MOTION_PHILOSOPHY.md` defaults when there's a conflict. If a section is empty, fall back to skill defaults.

Each bullet should end with a date in parentheses — that traces back to the per-session log under `_reference/feedback-logs/`.

> 🚧 **This file starts empty.** It fills in automatically as you finish videos and run `/feedback` to capture what worked and what didn't. The more you use it, the better the workspace matches your taste without you repeating yourself.

---

## Visual style

_(colors, typography, density, placement — populated by /feedback over time)_

- _no rules captured yet_

## Pacing

- **Jeff Nippard tight-cut, always.** Zero dead air between sentences: trim every kept segment to the voice (≈30ms lead, ≈60ms tail) and shrink every silence/breath inside it to ≈60ms (energy threshold ≈ −37 dB on the raw take, min run 0.10s). After cutting, measure: no gap > 0.25s should remain. (2026-10-13)
- **No retakes, false starts or repeated lines survive.** Transcribe with a disfluency prompt (`--prompt "Ehm, allora, cioè… ripeto."`) so whisper doesn't merge repeated phrases into one, and re-check every joint by transcribing the *edited* audio. Drop fillers like "che questo" / "Sono" at sentence starts when they cut cleanly. (2026-10-13)

## Captions

_(style, color, sync tightness, word-by-word vs. phrase chunks — populated by /feedback over time)_

- _no rules captured yet_

## Transitions

_(preferred / avoid — populated by /feedback over time)_

- _no rules captured yet_

## Audio

- When Luca says "non modificare la qualità audio": no loudnorm/EQ/compression, no music or SFX; only 10ms cut fades, and mux the cut audio into the final MP4 with `-c:a copy`. (2026-10-13)

- _no rules captured yet_

## Brand

_(logo treatment, hashtags, handles, brand-tokens overrides — populated by /feedback over time)_

- _no rules captured yet_

## Avoid

_(anti-patterns to never repeat — populated by /feedback over time)_

- _no rules captured yet_
