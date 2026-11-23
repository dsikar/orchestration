# We've Only Just Begun (Bars 1–16) — Belkin: Fat vs. Thin Sound & Unison Doubling

## Textbook Passage and Rule

- **Book:** Alan Belkin, *Orchestration* (*Artistic Orchestration*), `reference/textbooks/alan-belkin-artistic-orchestration.pdf`, **PDF pages 34–35** (*Fat vs. thin sound; unison doubling*).
- **Rule in Belkin's terms:** Following Koechlin, Belkin distinguishes *loudness* from *volume* — the "thickness" of a sound (for example, a horn sounds thicker, or "fatter", than a violin at any dynamic level). Fat sound arises in two ways: from a chosen timbre or from unison doubling. Same-instrument unison doubling adds more *volume* than loudness (a qualitative thickening), whereas combining different timbres creates a new colour. Because overuse of unison doubling is the beginner's most common orchestration fault, Belkin's elementary rule of thumb is: **do not double at the unison unless there is a definite need for more volume, or unless that particular colour is exactly what the musical character requires.**

## Material and Sources

- **Harmonic base:** Taken verbatim from the merged piano sketch in `implementations/belkin/weve-only-just-begun-bars-1-16/` — **A major**, **4/4**, **Moderately slow (Ballad) ♩ = 88**, **exactly 16 bars**, no repeats, ending mid-phrase on `F#m7`. All chord symbols are copied unchanged above Violin 1 (including `A` rather than `Amaj7`, and `Bm7/E` for all of bar 12), with chord-symbol playback turned off.
- **Vocal melody (bars 5–16):** Taken from the same Real Book chart cited in the piano sketch's `SUMMARY.md` — [Sheet Music Direct — Hal Leonard *Real Book – Melody, Lyrics & Chords* (ID 480653)](https://www.sheetmusicdirect.com/se/ID_No/480653/Product.aspx), accessed `2026-11-23` (A major, The Carpenters 1970 version) — and checked against [Musicnotes `MN0034721`](https://www.musicnotes.com/sheetmusic/the-carpenters/weve-only-just-begun/MN0034721) (accessed `2026-11-23`) across bars 5–10 to confirm the same version, key, pitches, and rhythms. No chart or lead-sheet file is committed to this repository, and no lyrics are copied.
- **Octave placement of melody:** The Real Book vocal melody in A major spans `E3`–`A4`, whose opening pitches `E3` and `F#3` (bars 5 and 13) lie below the violin's lowest string (`G3`). The melody is therefore placed one octave higher (`E4`–`A5`) in Violin 1 (and Violin 2 in bars 11–12), preserving every pitch class, interval, and rhythm while keeping the line idiomatic for violin and cleanly separated above the viola.

## How the Score Applies Belkin's Rule

Scored for **Violin 1, Violin 2, Viola, and Cello** (no piano, winds, brass, or inherently fat timbres):

- **Bars 1–4 (Intro):** Violin 1 and Violin 2 are **tacet** (no invented melody). Viola and Cello play the harmony at `mp`.
- **Melody entry:** The vocal melody begins in **bar 5** (Verse 1), played by **Violin 1 alone** at `mp` while Violin 2 remains tacet (thin texture, no unison doubling).
- **Bars 11–12 only (the sole unison doubling):** These two bars form the close of the only complete phrase in the 16-bar excerpt, arriving on `Bm7/E`. **Violin 2 doubles Violin 1 at the unison** at `mf`, marked with staff text `unison for volume`. This applies Belkin's first permitted reason for same-instrument doubling — adding volume to mark the arrival of the completed phrase without introducing a new timbre.
- **Bars 13–16 (Verse 2, incomplete):** At bar 13, Violin 2 drops out (tacet again) and the dynamic returns to `mp`. Because bars 13–16 contain only the first four bars of Verse 2 and **stop mid-phrase on `F#m7`** (with no added bars, repeat, or cadence), they remain thin and are **not doubled**.
- **Viola and Cello accompaniment:** Cello plays the exact bass note of each bar from the piano sketch as a sustained whole note (`E2`–`D3`). Viola plays chord tones only from each bar's harmony as playable two-half-note double stops (`E3`–`E4`), matching the sketch's two-half-note rhythm with beats 1 and 3 changes arriving cleanly on beat 1. Every viola and cello pitch lies strictly below Violin 1 (`max(Viola, Cello) < min(Violin 1)` in every bar), so neither instrument ever doubles the melody at the unison.

### Bar-by-Bar Chord Symbols and Texture

| Bar | Section | Chord (beat 1) | Violin 1 | Violin 2 | Viola (2 half notes) | Cello (whole note) | Dynamic |
|---|---|---|---|---|---|---|---|
| 1 | Intro | `A` | tacet | tacet | `E3, C#4` | `A2` | `mp` |
| 2 | Intro | `Dmaj7` | tacet | tacet | `F#3, C#4` | `D3` | `mp` |
| 3 | Intro | `A` | tacet | tacet | `E3, C#4` | `A2` | `mp` |
| 4 | Intro | `Dmaj7` | tacet | tacet | `F#3, C#4` | `D3` | `mp` |
| 5 | Verse 1 | `A` | melody starts | tacet | `E3, C#4` | `A2` | `mp` |
| 6 | Verse 1 | `Dmaj7` | melody | tacet | `F#3, C#4` | `D3` | `mp` |
| 7 | Verse 1 | `C#m7` | melody | tacet | `E3, B3` | `C#3` | `mp` |
| 8 | Verse 1 | `F#m7` | melody | tacet | `E3, A3` | `F#2` | `mp` |
| 9 | Verse 1 | `Bm7` | melody | tacet | `A3, D4` | `B2` | `mp` |
| 10 | Verse 1 | `F#m7` | melody | tacet | `A3, E4` | `F#2` | `mp` |
| 11 | Verse 1 | `Bm7` | melody | **unison** (`unison for volume`) | `A3, D4` | `B2` | `mf` |
| 12 | Verse 1 | `Bm7/E` | melody | **unison** | `B3, D4` | `E2` | `mf` |
| 13 | Verse 2 (incomplete) | `A` | melody | tacet | `E3, C#4` | `A2` | `mp` |
| 14 | Verse 2 (incomplete) | `Dmaj7` | melody | tacet | `F#3, C#4` | `D3` | `mp` |
| 15 | Verse 2 (incomplete) | `C#m7` | melody | tacet | `E3, B3` | `C#3` | `mp` |
| 16 | Verse 2 (incomplete) | `F#m7` | melody (ends mid-phrase) | tacet | `E3, A3` | `F#2` | `mp` |

## Software, Playback, and Checks Performed

- **MuseScore version:** MuseScore Studio `4.7.7` (build `4.7.7.261109195`, revision `b750c43`).
- **Sound library:** MuseScore 4 `MuseSounds` profile (`Muse Strings` — Violin 1, Violin 2, Viola, Cello).
- **Playback duration:** `46.71 s` (`46.706875 s` via `ffprobe` for `weve-only-just-begun-unison-doubling.mp3`, 44.1 kHz stereo, 128 kbps).
- **Audio listening note:** I cannot hear audio output directly, so I did not perform a listen-through. Instead, I checked the exported audio programmatically (`ffprobe` stream/duration metadata, `ffmpeg volumedetect`: mean `-31.3 dB`, max `-11.5 dB`, and per-section WAV RMS showing a clear increase during the unison doubling: bars 1–4 `0.0220`, bars 5–10 `0.0215`, **bars 11–12 `0.0611`**, bars 13–16 `0.0219`).
- **Score verification:**
  - Reopened the saved `weve-only-just-begun-unison-doubling.mscz` in MuseScore 4.7.7 to export both the PDF and MP3, confirming all notation persisted intact.
  - Audited all 4 staves across all 16 bars programmatically against the merged piano sketch: confirmed exactly 16 bars with no repeats, identical chord symbols above Violin 1, Violin 1 & 2 tacet in bars 1–4, Violin 2 in exact pitch-for-pitch unison with Violin 1 in bars 11–12 only and tacet everywhere else, all violin notes `>= G3`, exact cello bass notes, strictly chord-tone viola double stops, and zero melody-accompaniment unison overlap.
  - Verified chord-symbol playback is disabled (`<play>0</play>` on all 16 `<Harmony>` elements) via WAV comparison against an identical score with all `<Harmony>` elements removed (`max_diff = 0.0`).
  - Visually inspected both pages of the rendered PDF to confirm all 16 bars, chord symbols, tacet introduction, `unison for volume` marking in bars 11–12, and clean layout.
