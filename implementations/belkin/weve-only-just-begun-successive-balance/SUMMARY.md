# We've Only Just Begun (Bars 1–16) — Belkin: Successive Balance

## Textbook Passage and Rule

- **Book:** Alan Belkin, *Orchestration* (*Artistic Orchestration*), `reference/textbooks/alan-belkin-artistic-orchestration.pdf`, **PDF page 35** (*Balance: simultaneous and successive*, continuing onto page 36).
- **Rule in Belkin's terms:** Following Koechlin, Belkin distinguishes *simultaneous balance* (which instruments dominate within a single combination) from **successive balance** (the balance between one sound and the sound that follows it). Successive balance becomes a problem mainly when passing straight from very thick sounds to very thin ones: the thin sound can seem disagreeable simply by contrast with the preceding richness, even though heard in another context it would not be disturbing at all.

## Material

- **Base score:** Copied directly from the merged unison-doubling score in `implementations/belkin/weve-only-just-begun-unison-doubling/` — **16 bars** in **A major**, **4/4**, **Moderately slow (Ballad) ♩ = 88**, for **Violin 1, Violin 2, Viola, and Cello** (no piano, winds, or brass; no added bars, repeats, or cadence).
- **Unchanged elements:** All 16 chord symbols above Violin 1 (with chord-symbol playback turned off), the tacet introduction (bars 1–4), Violin 1's vocal melody (bars 5–16), the Viola and Cello harmony across all 16 bars, and the entire **bars 1–12** block — including the `mf` unison doubling in bars 11–12 — are unchanged.

## How the Score Applies Successive Balance

- **Bars 1–10 (Intro and thin Verse 1):** Unchanged from the unison score (`mp`; both violins tacet in bars 1–4; Violin 1 alone on the melody in bars 5–10 with Violin 2 tacet).
- **Bars 11–12 (the thick sound):** Unchanged from the unison score — Violin 2 doubles Violin 1 at the unison at `mf` (marked `unison for volume`) across `Bm7` → `Bm7/E`. Keeping this thick arrival intact establishes the contrast that successive balance must manage.
- **Bars 13–14 (the successive-balance repair):** In the unison score, Violin 2 dropped out abruptly on the downbeat of bar 13 and the dynamic snapped straight back to `mp`, exposing the returning thin melody immediately after the thick `mf` unison. Here, **bars 13–14 cushion that transition so bar 13 does not arrive naked**:
  - **Violin 1** continues the vocal melody unchanged.
  - **Violin 2** stops doubling the melody and sustains a single tied **`A3`** whole note across bars 13 and 14 (`A` is a common tone of bar 12 `Bm7/E`, bar 13 `A`, and bar 14 `Dmaj7`), marked with staff text `successive balance`. Placing the pitch at **`A3`** (rather than `A4`) prevents any unison with Violin 1's `A4` in bar 13, avoids unison with Viola (`E3, C#4` in bar 13; `F#3, C#4` in bar 14) and Cello (`A2`, `D3`), and keeps Violin 1 clearly as the top line while warming the inner harmony on the G string.
  - **Dynamic easing:** Instead of snapping to `mp` on the downbeat of bar 13, all four staves carry a diminuendo hairpin across bars 13–14 from the `mf` of bars 11–12, arriving at `mp` on the downbeat of bar 15.
- **Bars 15–16 (thin again, mid-phrase ending):** At bar 15, Violin 2 is tacet again and Violin 1, Viola, and Cello arrive at `mp`, returning smoothly to the thin single-violin texture of bars 7–8. The excerpt **still ends mid-phrase on `F#m7`** in bar 16.

### Bar-by-Bar Plan

| Bars | Section | Chords (beat 1) | Texture and Dynamics |
|---|---|---|---|
| 1–4 | Intro | `A`, `Dmaj7`, `A`, `Dmaj7` | Violin 1 & 2 tacet; Viola & Cello harmony at `mp` (unchanged) |
| 5–10 | Verse 1 | `A`, `Dmaj7`, `C#m7`, `F#m7`, `Bm7`, `F#m7` | Violin 1 alone on melody, Violin 2 tacet, `mp` — thin (unchanged) |
| 11–12 | Verse 1 (phrase close) | `Bm7`, `Bm7/E` | Violin 1 + Violin 2 unison (`unison for volume`), `mf` — **thick sound** (unchanged) |
| 13–14 | Verse 2 (start) | `A`, `Dmaj7` | Violin 1 melody; Violin 2 holds tied **`A3`** (`successive balance`); diminuendo `mf` → `mp` across all 4 staves |
| 15–16 | Verse 2 (incomplete) | `C#m7`, `F#m7` | Violin 1 alone at `mp`, Violin 2 tacet — **thin again**, ending mid-phrase on `F#m7` |

## Software, Playback, and Checks Performed

- **MuseScore version:** MuseScore Studio `4.7.7` (build `4.7.7.261109195`, revision `b750c43`).
- **Sound library:** MuseScore 4 `MuseSounds` profile (`Muse Strings` — Violin 1, Violin 2, Viola, Cello).
- **Playback duration:** `46.71 s` (`46.706875 s` via `ffprobe` for `weve-only-just-begun-successive-balance.mp3`, 44.1 kHz stereo, 128 kbps).
- **Audio listening note:** I cannot hear audio output directly, so I did not perform a listen-through. Instead, I verified the exported audio programmatically (`ffprobe` metadata, `ffmpeg volumedetect`: mean `-30.8 dB`, max `-11.5 dB`) and measured per-section WAV RMS, confirming a gradual step-down across bars 13–14 instead of an abrupt drop:
  - Bars 1–4 (Intro, `mp`): `0.02203`
  - Bars 5–10 (thin Vln 1 solo, `mp`): `0.02146`
  - Bars 11–12 (thick unison, `mf`): `0.06111`
  - Bar 13 (held `A3`, dim start): `0.04826`
  - Bar 14 (held `A3`, dim end): `0.02627`
  - Bars 15–16 (thin Vln 1 solo again, `mp`): `0.01901`
- **Score verification:**
  - Reopened the saved `weve-only-just-begun-successive-balance.mscz` in MuseScore 4.7.7 to export both the PDF and MP3, confirming all notation persisted intact.
  - Programmatically compared bars 1–12 across all four staves against `implementations/belkin/weve-only-just-begun-unison-doubling/weve-only-just-begun-unison-doubling.mscz`: 100% identical in pitches, rhythms, chord symbols, dynamics, and staff text.
  - Audited bars 13–16: confirmed Violin 1, Viola, and Cello pitches/rhythms unchanged; Violin 2 holds tied `A3` (MIDI 57) in bars 13–14 with staff text `successive balance` and zero unison with any other part; diminuendo hairpins start on bar 13 in all four staves with `mp` arriving on bar 15 in Violin 1, Viola, and Cello; Violin 2 is tacet in bars 15–16.
  - Verified chord-symbol playback remains disabled (`<play>0</play>` on all 16 `<Harmony>` elements; `0.0` max sample diff vs. a no-harmony WAV export).
  - Visually inspected both pages of the rendered PDF to confirm all 16 bars, unchanged unison in bars 11–12, tied `A3` + `successive balance` + diminuendo hairpins in bars 13–14, and thin bars 15–16.
