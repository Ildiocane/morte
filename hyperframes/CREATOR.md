# Creator Profile — Luca Bandiera

Your identity, positioning, and workflow for video work in this workspace. **Read this before every video task** (alongside `PREFERENCES.md`). Use it for on-screen text, niche framing, and workflow assumptions.

## Identity

- **Name on-screen**: Luca Bandiera
- **Instagram**: @luca_bandiera_pt
- **TikTok**: @luca_bandiera_pt
- **YouTube**: @luca_bandiera
- **X / other**: —

When putting handles on-screen (lower-thirds, outros, end-cards), use the platform-appropriate handle.

## Platform priority

**Cross-post all** — TikTok, Instagram Reels, and YouTube Shorts equally. Default: **9:16 vertical, 1080×1920**. Keep text inside platform-safe zones that work across all three UIs.

## Content niche

**Fitness / lifestyle** — health, training, and daily-life content. When planning a new video, assume this niche unless told otherwise.

## On-camera mix

**Both** — a mix of face-cam and faceless videos. Ask per video which mode it is.

- **Face-cam** → use `/short-form-video` face-mode choreography (BOTTOM / FULLSCREEN modes).
- **Faceless** → motion graphics + AI TTS narration (`npx hyperframes tts`) or screen-recordings.

## Workflow — division of labor

**Luca sends raw footage; the assistant does the full edit.** Luca records himself talking to camera (vertical, phone, **in Italian**) and shares the raw file (Google Drive link). The assistant:

- cuts silences, false starts, repeated words, and mistakes (Luca explicitly wants this — his raw take is NOT the source of truth for pacing);
- tightens to the requested length (default hard cap: **60s**);
- adds captions (Italian), Jeff Nippard–style motion graphics, SFX, and light music.

Also open to faceless builds from scratch (motion graphics + TTS) when asked.

**Language:** videos are in **Italian** — transcribe with a multilingual model (`-l it`), never `small.en`. On-screen text and captions in Italian.

## Brand identity

Clean dark default for now (set during /setup): background `#0a0a0f`, surface `#1a1a23`, accent `#3b82f6`, text `#ffffff`, display font `system-ui, sans-serif`. Source of truth: [`assets/brand-tokens.css`](assets/brand-tokens.css). Will evolve via `/feedback`.

## Inspiration creators

See [`_reference/creator-library/INDEX.md`](_reference/creator-library/INDEX.md) for the full list. Add new creators via `/study-creator <url>`.

- **Primary reference:** [@jeffnippardfitness](_reference/creator-library/jeffnippardfitness/style-distilled.md) — 5 videos studied during /setup. Default to this fingerprint for Luca's builds unless told otherwise.

## Posting cadence & length defaults

- _Cadence_: _(TBD — set during /setup)_
- _Default length_: 15–45s short-form vertical is a common sweet spot. Adjust per video.
- _Default fps_: 30 (matches TikTok + Instagram defaults).

## Project slug convention

**Topic-only, kebab-case.** Each video gets a new subfolder under `video-projects/<topic-slug>/`. Examples: `ai-agents-intro`, `prompting-101`, `tool-of-the-week`. Keep slugs short and descriptive — scannable at a glance in `ls video-projects/`.

---

*This file is updated as your creator profile evolves. Major changes (new handles, platform shifts, workflow changes) can be edited here directly.*
