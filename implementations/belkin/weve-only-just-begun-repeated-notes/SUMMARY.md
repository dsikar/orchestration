# We've Only Just Begun (Bars 1–16) — Belkin: Repeated Notes

## Textbook Passage and Rule

- **Book:** Alan Belkin, *Orchestration* (*Artistic Orchestration*), `reference/textbooks/alan-belkin-artistic-orchestration.pdf`, **PDF pages 41–42** (*Planes of tone*, beginning on p. 39, under *Background: movement* — *Repeated Notes*).
- **Rule in Belkin's terms:** A plane of tone is a line or blended group sharing one rhythmic outline. The foreground must stand out clearly, while background movement — animating and lightening the texture in a secondary plane — must stay in a weaker plane of tone so it does not attract too much attention or cover the melody, keeping to a consistent motive. Repeated notes are one of Belkin's four basic types of orchestral background movement (alongside trills/tremolos, scales, and arpeggiation).

## Material and Base Score

- **Base score copied:** `implementations/belkin/weve-only-just-begun-heterophony/` — **16 bars** in **A major**, **4/4**, **Moderately slow (Ballad) ♩ = 88**, for **Violin 1, Violin 2, Viola, and Cello** (no piano, winds, or brass; no added bars, repeats, or cadence; all 16 chord symbols copied unchanged above Violin 1 with chord-symbol playback turned off).
- **Only the Viola in bars 5–10 and bars 15–16 changes:** Violin 1, Violin 2, and Cello are unchanged across all 16 bars.

## How the Score Applies Repeated Notes

- **Bars 5–10 and bars 15–16 (Viola repeated notes):** Where the heterophony score had two half-note dyads per bar in the Viola at `mp`, each bar now has **four quarter-note dyads** using the **exact same two pitches** already present in that bar, staying at **`mp`** so the background pulse remains weaker than Violin 1's foreground melody. Bar 5 and bar 15 carry the staff text **`repeated notes`**.
  - Bar 5 (`A`): `E3, C#4` (4 × quarter, `repeated notes`)
  - Bar 6 (`Dmaj7`): `F#3, C#4` (4 × quarter)
  - Bar 7 (`C#m7`): `E3, B3` (4 × quarter)
  - Bar 8 (`F#m7`): `E3, A3` (4 × quarter)
  - Bar 9 (`Bm7`): `A3, D4` (4 × quarter)
  - Bar 10 (`F#m7`): `A3, E4` (4 × quarter)
  - Bar 15 (`C#m7`): `E3, B3` (4 × quarter, `mp`, `repeated notes`)
  - Bar 16 (`F#m7`): `E3, A3` (4 × quarter)
- **Bars left held (unchanged from `weve-only-just-begun-heterophony/`):**
  - **Bars 1–4 (Intro):** Both violins are tacet; adding repeated-note movement in the Viola here would turn the accompaniment into the foreground, so the two half-note dyads remain held.
  - **Bars 11–14 (heterophony and successive-balance repair):** These bars carry Violin 2's heterophony (`mf`) in bars 11–12 and the held `A3` diminuendo (`mf` → `mp`) in bars 13–14; leaving the Viola held prevents the repeated-note motive from cluttering or covering those planes.
- **Ending:** The excerpt **still ends mid-phrase on `F#m7`** in bar 16.

## Software, Playback, and Checks Performed

- **MuseScore version:** MuseScore Studio `4.7.7` (build `4.7.7.261109195`, revision `b750c43`).
- **Sound library:** MuseScore 4 `MuseSounds` profile (`Muse Strings` — Violin 1, Violin 2, Viola, Cello).
- **Playback duration:** `46.71 s` (`46.706875 s` via `ffprobe` for `weve-only-just-begun-repeated-notes.mp3`, 44.1 kHz stereo, 128 kbps).
- **Audio listening note:** I cannot hear audio output directly, so I did not perform a listen-through. Instead, I checked the exported MP3 programmatically (`ffprobe` stream/duration metadata; `ffmpeg volumedetect`: mean `-30.8 dB`, max `-10.9 dB`).
- **Score verification:**
  - Reopened the saved `weve-only-just-begun-repeated-notes.mscz` in MuseScore 4.7.7 to export both the PDF and MP3, confirming all notation persisted intact.
  - Programmatically compared all 4 staves × 16 bars against `implementations/belkin/weve-only-just-begun-heterophony/weve-only-just-begun-heterophony.mscz`: confirmed Violin 1, Violin 2, and Cello match 100% identically across all 16 bars; Viola bars 1–4 and 11–14 (including the bar 13–14 diminuendo hairpin) match 100% identically; and Viola bars 5–10 and 15–16 differ only in replacing the two half-note dyads with four quarter-note dyads of the identical pitches plus `repeated notes` staff text at bars 5 and 15.
  - Verified chord-symbol playback remains disabled (`<play>0</play>` on all 16 `<Harmony>` elements; `0.0` max sample diff vs. a no-harmony WAV export).
  - Visually inspected both pages of the rendered PDF to confirm all 16 bars, the quarter-note viola dyads in bars 5–10 and 15–16, the unchanged heterophony in bars 11–12, and the intact bar 13–14 diminuendo hairpins.
