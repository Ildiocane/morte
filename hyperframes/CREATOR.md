<!-- HYPERFRAMES_SETUP_INCOMPLETE -->
<!-- ^ Leave this marker until /setup is complete. It tells Claude to greet a new user
     and run onboarding before any video work. The setup skill removes it when finished. -->

# Creator Profile — Luca Bandiera

Your identity, positioning, and workflow for video work in this workspace. **Read this before every video task** (alongside `PREFERENCES.md`). Use it for on-screen text, niche framing, and workflow assumptions.

> 🚧 **This file is a blank template.** Run `/setup` (or just tell Claude "help me get set up") and it will fill these sections in from a short interview. You can also edit it by hand any time.

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

**Build from scratch with the assistant** (motion graphics, TTS narration, screen recordings assembled together). For reference, the two modes:

- **You record + pre-edit your own speaking video** → it's the source of truth; the assistant builds the visual layer on top and does NOT cut your audio, remove pauses, or change your pacing.
- **You build from scratch with the assistant** → motion graphics, TTS narration, screen-recordings assembled together.

## Brand identity

Clean dark default for now (set during /setup): background `#0a0a0f`, surface `#1a1a23`, accent `#3b82f6`, text `#ffffff`, display font `system-ui, sans-serif`. Source of truth: [`assets/brand-tokens.css`](assets/brand-tokens.css). Will evolve via `/feedback`.

## Inspiration creators

Studied creators live in [`_reference/creator-library/`](_reference/creator-library/). Add more with `/study-creator <url>`.

**Pending (blocked during /setup — TikTok was not reachable from the cloud environment):** study these @jeffnippardfitness videos with `/study-creator`:
- https://www.tiktok.com/@jeffnippardfitness/video/7652093298256923924
- https://www.tiktok.com/@jeffnippardfitness/video/7610877939973934356
- https://www.tiktok.com/@jeffnippardfitness/video/7607951419785612565
- https://www.tiktok.com/@jeffnippardfitness/video/7605986132278611221
- https://www.tiktok.com/@jeffnippardfitness/video/7601564484368370964

## Posting cadence & length defaults

- _Cadence_: _(TBD — set during /setup)_
- _Default length_: 15–45s short-form vertical is a common sweet spot. Adjust per video.
- _Default fps_: 30 (matches TikTok + Instagram defaults).

## Project slug convention

**Topic-only, kebab-case.** Each video gets a new subfolder under `video-projects/<topic-slug>/`. Examples: `ai-agents-intro`, `prompting-101`, `tool-of-the-week`. Keep slugs short and descriptive — scannable at a glance in `ls video-projects/`.

---

*This file is updated as your creator profile evolves. Major changes (new handles, platform shifts, workflow changes) can be edited here directly.*
