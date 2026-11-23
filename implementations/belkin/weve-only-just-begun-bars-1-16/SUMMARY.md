# We've Only Just Begun (Bars 1–16) — Harmonic Base

## Source and Attribution

- **Song:** "We've Only Just Begun"
- **Songwriting credits (primary chart):** Roger Nichols / Paul Williams (`Copyright © 1970 Irving Music, Inc. Copyright Renewed`)
- **Songwriting credits (tempo cross-reference):** Words by Paul Williams, Music by Roger Nichols (`© 1970 Irving Music, Inc. (BMI)`)
- **Version / recording described:** The Carpenters (1970 recording, original key of A major)
- **Primary chord chart:** [Sheet Music Direct — Hal Leonard *Real Book – Melody, Lyrics & Chords* (ID 480653)](https://www.sheetmusicdirect.com/se/ID_No/480653/Product.aspx), author/publisher Hal Leonard on Sheet Music Direct, accessed `2026-11-23` (publicly viewable page-1 preview covers the entire opening continuously; no chart file is committed to this repository).
- **Tempo cross-reference (same version and key):** [Musicnotes — The Carpenters Piano/Vocal/Guitar (SKU MN0034721)](https://www.musicnotes.com/sheetmusic/the-carpenters/weve-only-just-begun/MN0034721), Universal Music Publishing Group on Musicnotes, accessed `2026-11-23`.
- **Blocked sources skipped:** `e-chords.com`, `cifraclub.com.br`, `chordwiki.org`, and `chordify.net` returned HTTP 403 Forbidden during lookup and were not used.

## Musical Parameters and Disagreements

- **Key:** A major (concert pitch, three sharps; no capo or transposition).
- **Metre:** 4/4, with no pickup (bar 1 is the first full measure).
- **Tempo:** `Moderately slow (Ballad) ♩ = 88`. The primary Real Book chart prints only `(BALLAD)` with no numeric metronome mark; `♩ = 88` (`Moderately slow`) is taken from Musicnotes `MN0034721`, which describes the same Carpenters 1970 version in A major, 4/4.
- **Disagreements / notational reconciliations:**
  - The Real Book chart uses jazz minus-sign shorthand for minor sevenths (`C#-7`, `F#-7`, `B-7`, `B-7/E`). In MuseScore these are entered in standard chord notation as `C#m7`, `F#m7`, `Bm7`, and `Bm7/E`.
  - Musicnotes `MN0034721` omits a printed chord symbol above bar 1 (while writing an A-major piano vamp and printing `A` at bar 3), whereas the Real Book explicitly prints `A` at bar 1. Across bars 1–10 (where the `MN0034721` page-1 preview ends), the harmony agrees bar for bar; bars 11–12 (`Bm7`, `Bm7/E`) and the Verse 2 repeat come directly from the Real Book chart.

## Form and Bar-by-Bar Chord Mapping (Bars 1–16)

In the Real Book chart, bars 1–4 are the instrumental Intro and bars 5–12 are enclosed in repeat barlines (taking the 1st ending at bar 12 and returning to bar 5 for Verse 2). To deliver exactly 16 notated bars with no extra repeats, the opening is written out linearly:

- **Intro:** score bars 1–4 (chart bars 1–4)
- **Verse 1:** score bars 5–12 (chart bars 5–12, first pass through repeat, 1st ending)
- **Verse 2:** score bars 13–16 (chart bars 5–8 repeated linearly, second pass)

| Score bar | Section | Chart bar | Beat 1 chord symbol | Real Book shorthand |
|---|---|---|---|---|
| 1 | Intro | 1 | `A` | `A` |
| 2 | Intro | 2 | `Dmaj7` | `Dmaj7` |
| 3 | Intro | 3 | `A` | `A` |
| 4 | Intro | 4 | `Dmaj7` | `Dmaj7` |
| 5 | Verse 1 | 5 | `A` | `A` |
| 6 | Verse 1 | 6 | `Dmaj7` | `Dmaj7` |
| 7 | Verse 1 | 7 | `C#m7` | `C#-7` |
| 8 | Verse 1 | 8 | `F#m7` | `F#-7` |
| 9 | Verse 1 | 9 | `Bm7` | `B-7` |
| 10 | Verse 1 | 10 | `F#m7` | `F#-7` |
| 11 | Verse 1 | 11 | `Bm7` | `B-7` |
| 12 | Verse 1 | 12 (1st ending) | `Bm7/E` | `B-7/E` |
| 13 | Verse 2 | 5 (2nd pass) | `A` | `A` |
| 14 | Verse 2 | 6 (2nd pass) | `Dmaj7` | `Dmaj7` |
| 15 | Verse 2 | 7 (2nd pass) | `C#m7` | `C#-7` |
| 16 | Verse 2 | 8 (2nd pass) | `F#m7` | `F#-7` |

## Editorial Realization and Melody

- **Editorial piano realization:** Both the chord voicings and the rhythm are my own editorial realization of the chart. Across all 16 bars, a single plain, repeatable pattern is used at dynamic `mp`: a whole-note bass note on beat 1 in the left hand (`E2`–`D3`) and two half-note block chords on beats 1 and 3 in the right hand (`E4`–`E5`), voiced with smooth voice-leading and complete chord tones (including all four pitches of `Bm7` above `E2` in bar 12's `Bm7/E`).
- **Melody:** **Chords only** — no vocal melody is included. Although the Real Book source prints a lead melody and lyrics, both are intentionally omitted here so the score remains a clean harmonic sketch.

## Software, Sound, and Verification Checks

- **MuseScore version:** MuseScore Studio `4.7.7` (build `4.7.7.261109195`, revision `b750c43`).
- **Piano sound:** MuseScore 4 `MuseSounds` active sound profile (`Muse Keys` — `Piano` installed locally; FluidSynth GM program `0` Acoustic Grand Piano as channel fallback).
- **Playback duration:** `46.71 s` (`46.706875 s` reported by `ffprobe` for `weve-only-just-begun-bars-1-16.mp3`, 44.1 kHz stereo, 128 kbps; 64 beats at `♩ = 88` = `43.64 s` plus a ~`3.1 s` piano decay tail).
- **Audio listening note:** I cannot hear audio playback directly, so I did not perform a listen-through. Instead, I checked the exported MP3 programmatically (`ffprobe` duration/stream metadata and `ffmpeg volumedetect`: mean `-35.0 dB`, max `-13.7 dB`).
- **Score and chord-playback checks performed:**
  - Reopened the saved `weve-only-just-begun-bars-1-16.mscz` in MuseScore 4.7.7 to export both the PDF and the MP3, confirming all notation persisted intact.
  - Verified programmatically and by visual inspection of the rendered PDF that the score has **exactly 16 bars** (no repeats), shows the `Piano` grand staff, key of A major, 4/4 time, `Moderately slow (Ballad) ♩ = 88`, section marks (`Intro`, `Verse 1`, `Verse 2`), and all 16 chord symbols aligned to beat 1.
  - Checked every bar's chord symbol and written LH/RH pitches against the Real Book chart.
  - Disabled chord-symbol playback by setting `<play>0</play>` on all 16 `<Harmony>` elements (preserved across MuseScore 4.7.7 round-trip save) and verified by WAV comparison against a copy with all `<Harmony>` elements removed (`max sample diff = 0.0`, `RMS diff = 0.0`), confirming the written piano part plays without a second chord-symbol playback layer.

This score is the harmonic base for the first Belkin exercises, and no Belkin orchestration technique has been applied yet.
