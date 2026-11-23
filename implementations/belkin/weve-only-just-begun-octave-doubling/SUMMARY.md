# We've Only Just Begun (Bars 1–16) — Belkin: Octave Doubling

## Textbook Passage and Rule

- **Book:** Alan Belkin, *Orchestration* (*Artistic Orchestration*), `reference/textbooks/alan-belkin-artistic-orchestration.pdf`, **PDF page 37** (*Musical lines vs. instrumental parts* — *Doubling at intervals other than the unison*).
- **Rule in Belkin's terms:** Too frequent literal (unison) doubling leads to heaviness and a rather gray sound. **Doubling at the octave allows for greater transparency of color, and fills the musical space in more interesting and varied ways** instead of thickening a single pitch.

## Material and Comparison Context

- **Base score copied:** `implementations/belkin/weve-only-just-begun-successive-balance/` — **16 bars** in **A major**, **4/4**, **Moderately slow (Ballad) ♩ = 88**, for **Violin 1, Violin 2, Viola, and Cello** (no piano, winds, or brass; no added bars, repeats, or cadence; all 16 chord symbols copied unchanged above Violin 1 with chord-symbol playback off).
- **Direct comparison to earlier scores:**
  - `implementations/belkin/weve-only-just-begun-unison-doubling/` (issue #2) introduced a **unison** doubling in Violin 2 at bars 11–12 (`unison for volume`).
  - `implementations/belkin/weve-only-just-begun-successive-balance/` (issue #5) kept that unison in bars 11–12 and added the successive-balance repair in bars 13–14 (Violin 2 held `A3` + diminuendo from `mf` to `mp` at bar 15).
  - This score keeps everything from `weve-only-just-begun-successive-balance/` identical **except Violin 2 in bars 11–12**, replacing the unison with an **octave doubling** so the two doubling types can be compared directly in the same musical context.

## How the Score Applies Octave Doubling

- **Bars 1–10:** Unchanged from the successive-balance score (bars 1–4 tacet in both violins with Viola and Cello harmony at `mp`; bars 5–10 Violin 1 alone on the vocal melody at `mp`, Violin 2 tacet).
- **Bars 11–12 only (octave doubling, not a unison):** Violin 2 plays the exact same line and rhythm as Violin 1 **one octave higher**, at **`mf`**, with staff text changed from `unison for volume` to **`octave doubling`**. No other doubling is added anywhere in the score, and Violin 2 remains tacet in bars 1–10 and bars 15–16.
  - **Bar 11 (`Bm7`):**
    - Violin 1: `C#5` (dotted quarter), `D5` (eighth), `B4` (half, tied to bar 12)
    - Violin 2 (+1 octave): `C#6` (dotted quarter), `D6` (eighth), `B5` (half, tied to bar 12)
  - **Bar 12 (`Bm7/E`):**
    - Violin 1: `B4` (dotted quarter, tied from bar 11), `E5` (eighth), `F#5` (quarter), `A5` (eighth), `F#5` (eighth)
    - Violin 2 (+1 octave): `B5` (dotted quarter, tied from bar 11), `E6` (eighth), `F#6` (quarter), `A6` (eighth), `F#6` (eighth)
- **Bars 13–16 (unchanged):** Identical to `implementations/belkin/weve-only-just-begun-successive-balance/`. In bars 13–14, Violin 2 drops intentionally from the higher octave down to the held common-tone **`A3`** (marked `successive balance`) while all four staves diminuendo from `mf` to arrive at `mp` on beat 1 of bar 15. In bars 15–16, Violin 2 is tacet and Violin 1 returns alone at `mp`. The excerpt **still ends mid-phrase on `F#m7`** in bar 16.
- **Violin 1, Viola, and Cello:** Unchanged across all 16 bars; Viola and Cello remain on their sustained chord harmony and do not double the melody at the unison or at the octave.

## Software, Playback, and Checks Performed

- **MuseScore version:** MuseScore Studio `4.7.7` (build `4.7.7.261109195`, revision `b750c43`).
- **Sound library:** MuseScore 4 `MuseSounds` profile (`Muse Strings` — Violin 1, Violin 2, Viola, Cello).
- **Playback duration:** `46.71 s` (`46.706875 s` via `ffprobe` for `weve-only-just-begun-octave-doubling.mp3`, 44.1 kHz stereo, 128 kbps).
- **Audio listening note:** I cannot hear audio output directly, so I did not perform a listen-through. Instead, I checked the exported audio programmatically (`ffprobe` metadata, `ffmpeg volumedetect`: mean `-30.7 dB`, max `-11.3 dB`) and measured per-section WAV RMS:
  - Bars 1–4 (Intro, `mp`): `0.02203`
  - Bars 5–10 (Vln 1 solo, `mp`): `0.02146`
  - Bars 11–12 (Vln 1 + Vln 2 octave doubling, `mf`): `0.06143`
  - Bar 13 (held `A3`, dim start): `0.04825`
  - Bar 14 (held `A3`, dim end): `0.02627`
  - Bars 15–16 (Vln 1 solo, `mp`): `0.01901`
- **Score verification:**
  - Reopened the saved `weve-only-just-begun-octave-doubling.mscz` in MuseScore 4.7.7 to export both the PDF and MP3, confirming all notation persisted intact.
  - Programmatically compared all 4 staves × 16 bars against `implementations/belkin/weve-only-just-begun-successive-balance/weve-only-just-begun-successive-balance.mscz`: confirmed bars 1–10 and 13–16 match 100% identically across all four staves, Violin 1, Viola, and Cello match 100% identically across all 16 bars, and bars 11–12 differ only in Violin 2's pitches (+12 semitones above Violin 1) and staff text (`octave doubling`).
  - Verified chord-symbol playback remains disabled (`<play>0</play>` on all 16 `<Harmony>` elements; `0.0` max sample diff vs. a no-harmony WAV export).
  - Visually inspected both pages of the rendered PDF to confirm all 16 bars, the octave doubling in bars 11–12, the held `A3` and diminuendo in bars 13–14, and the thin mid-phrase ending in bars 15–16.
