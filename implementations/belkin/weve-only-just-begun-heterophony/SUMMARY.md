# We've Only Just Begun (Bars 1–16) — Belkin: Heterophony

## Textbook Passage and Rule

- **Book:** Alan Belkin, *Orchestration* (*Artistic Orchestration*), `reference/textbooks/alan-belkin-artistic-orchestration.pdf`, **PDF page 38** (*Musical lines vs. instrumental parts* — *Heterophony*).
- **Rule in Belkin's terms:** Rather than literal doubling, a doubled part can be an ornamental or simplified variation on the same basic contour. This keeps the overall musical design clear while allowing individuality and avoiding a mechanical duplicate.

## Material and Base Score

- **Base score copied:** `implementations/belkin/weve-only-just-begun-octave-doubling/` — **16 bars** in **A major**, **4/4**, **Moderately slow (Ballad) ♩ = 88**, for **Violin 1, Violin 2, Viola, and Cello** (no piano, winds, or brass; no added bars, repeats, or cadence; all 16 chord symbols copied unchanged above Violin 1 with chord-symbol playback turned off).
- **Only bars 11–12 in Violin 2 change:** Bars 1–10 and 13–16 match `weve-only-just-begun-octave-doubling/` identically across all four staves, and Violin 1, Viola, and Cello are unchanged in all 16 bars.

## How the Score Applies Heterophony (Bars 11–12)

In `weve-only-just-begun-octave-doubling/`, Violin 2 copied Violin 1 literally one octave higher in bars 11–12 (`mf`, marked `octave doubling`). Here, Violin 2 replaces that literal copy with a simplified version of the same contour, still one octave above Violin 1 and still at **`mf`**, with staff text changed to **`heterophony`**:

- **Bar 11 (`Bm7`):**
  - **Violin 1:** dotted quarter `C#5`, eighth `D5`, half `B4` (tied to bar 12).
  - **Violin 2 (simplified octave contour):** half `C#6`, half `B5` (tied to bar 12).
  - **Omitted note:** the eighth-note **`D`** (`D6`) between `C#` and `B` drops out, leaving the essential falling step `C#6 → B5`.
- **Bar 12 (`Bm7/E`):**
  - **Violin 1:** dotted quarter `B4` (tied from bar 11), eighth `E5`, quarter `F#5`, eighth `A5`, eighth `F#5`.
  - **Violin 2 (simplified octave contour):** quarter `B5` (tied from bar 11), quarter `E6`, half `F#6`.
  - **Omitted notes:** the **`A–F#` (`A6–F#6`) turn** at the end of the bar drops out (and `E6` enters cleanly on beat 2 as a quarter note), preserving the rising contour `B5 → E6 → F#6` without adding other pitches or contrary motion.

### Bars 1–10 and 13–16 (Unchanged)

- **Bars 1–10:** Unchanged from the octave-doubling score (bars 1–4 tacet in both violins with Viola and Cello at `mp`; bars 5–10 Violin 1 alone on the melody at `mp`, Violin 2 tacet).
- **Bars 13–16:** Unchanged from `implementations/belkin/weve-only-just-begun-octave-doubling/` (and `weve-only-just-begun-successive-balance/`). In bars 13–14, Violin 2 drops intentionally from `F#6` down to the held common-tone **`A3`** (`successive balance`) while all four staves diminuendo from `mf` to arrive at `mp` on beat 1 of bar 15. In bars 15–16, Violin 2 is tacet and Violin 1 returns alone at `mp`. The excerpt **still ends mid-phrase on `F#m7`** in bar 16.

## Software, Playback, and Checks Performed

- **MuseScore version:** MuseScore Studio `4.7.7` (build `4.7.7.261109195`, revision `b750c43`).
- **Sound library:** MuseScore 4 `MuseSounds` profile (`Muse Strings` — Violin 1, Violin 2, Viola, Cello).
- **Playback duration:** `46.71 s` (`46.706875 s` via `ffprobe` for `weve-only-just-begun-heterophony.mp3`, 44.1 kHz stereo, 128 kbps).
- **Audio listening note:** I cannot hear audio output directly, so I did not perform a listen-through. Instead, I checked the exported audio programmatically (`ffprobe` metadata, `ffmpeg volumedetect`: mean `-30.8 dB`, max `-10.8 dB`) and measured per-section WAV RMS:
  - Bars 1–4 (Intro, `mp`): `0.02203`
  - Bars 5–10 (Vln 1 solo, `mp`): `0.02146`
  - Bars 11–12 (Vln 1 + Vln 2 heterophony, `mf`): `0.06103`
  - Bar 13 (held `A3`, dim start): `0.04824`
  - Bar 14 (held `A3`, dim end): `0.02627`
  - Bars 15–16 (Vln 1 solo, `mp`): `0.01901`
- **Score verification:**
  - Reopened the saved `weve-only-just-begun-heterophony.mscz` in MuseScore 4.7.7 to export both the PDF and MP3, confirming all notation persisted intact.
  - Programmatically compared all 4 staves × 16 bars against `implementations/belkin/weve-only-just-begun-octave-doubling/weve-only-just-begun-octave-doubling.mscz`: confirmed bars 1–10 and 13–16 match 100% identically across all four staves, Violin 1, Viola, and Cello match 100% identically across all 16 bars, and bars 11–12 differ only in Violin 2's simplified pitches/rhythms (`half C#6, half B5 | quarter B5, quarter E6, half F#6`, tied across `B5`, `mf`) and staff text (`heterophony`).
  - Verified chord-symbol playback remains disabled (`<play>0</play>` on all 16 `<Harmony>` elements; `0.0` max sample diff vs. a no-harmony WAV export).
  - Visually inspected both pages of the rendered PDF to confirm all 16 bars, the simplified octave line (`heterophony`) in bars 11–12, the held `A3` (`successive balance`) and diminuendo in bars 13–14, and the thin mid-phrase ending in bars 15–16.
