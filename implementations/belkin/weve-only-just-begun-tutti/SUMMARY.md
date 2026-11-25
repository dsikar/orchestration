# We've Only Just Begun (Bars 1–16) — Belkin: Soft Tutti

## Textbook Passage and Rule

- **Book:** Alan Belkin, *Orchestration* (*Artistic Orchestration*), `reference/textbooks/alan-belkin-artistic-orchestration.pdf`, **PDF pages 47–49** (*The tutti*).
- **Rule in Belkin's terms:** A tutti uses at least three orchestral families (here woodwinds, brass, and strings; no percussion). A soft tutti can be especially effective in a ballad context. Belkin's first and primary method for organizing a tutti is to make each family harmonically coherent while keeping part-writing independent from family to family, avoiding the heavy, gray sound of literal line-for-line doubling across families.

## Material and Ensemble

- **String quartet base copied verbatim:** `implementations/belkin/weve-only-just-begun-heterophony/` — all four string parts (Violin 1, Violin 2, Viola, Cello) remain unchanged across all 16 bars in **A major**, **4/4**, **Moderately slow (Ballad) ♩ = 88**, with chord symbols at the top of the score (`<play>0</play>`).
- **Added families (all at `mp`, never louder than Violin 1):** Flute, Clarinet in B-flat, Bassoon, and Horn in F. The string parts were **not** recopied literally into the winds or brass: each family contributes an independent textural role.

## Sounding Pitches of Added Wind and Brass Parts

- **Flute (C, `mp`):** Tacet in bars 1–10 and 13–16. In **bars 11–12 only**, doubles Violin 1 one octave higher in the same rhythm:
  - Bar 11 (`Bm7`): dotted quarter `C#6`, eighth `D6`, half `B5` (tied)
  - Bar 12 (`Bm7/E`): dotted quarter `B5` (tied), eighth `E6`, quarter `F#6`, eighth `A6`, eighth `F#6`
- **Clarinet in B-flat (`mp`, written up a major 2nd in B major, 5 sharps):** Tacet bars 1–4; whole notes bars 5–16:
  - Bars 5–12 sounding: `C#4, F#4, E4, A4, A4, E4, D4, D4` (written `D#4, G#4, F#4, B4, B4, F#4, E4, E4`)
  - Bars 13–16 sounding: `C#4, F#4, B3, A3` (written `D#4, G#4, C#4, B3`)
- **Bassoon (C, `mp`):** Tacet bars 1–4 and 13–14; whole notes matching Cello sounding pitches in bars 5–12 (`A2, D3, C#3, F#2, B2, F#2, B2, E2`) and bars 15–16 (`C#3, F#2`).
- **Horn in F (`mp`, written up a perfect 5th in E major, 4 sharps):** Tacet bars 1–4 and 13–16; whole notes bars 5–12:
  - Bars 5–12 sounding: `C#4, F#4, E4, A4, D4, A4, D4, D4` (written `G#4, C#5, B4, E5, A4, E5, A4, A4`)

The excerpt still ends mid-phrase on `F#m7` in bar 16.

## Software, Playback, and Checks Performed

- **MuseScore version:** MuseScore Studio `4.7.7` (`MuseSounds` — `Muse Woodwinds`, `Muse Brass`, `Muse Strings`).
- **Playback duration:** `46.71 s` (`46.706875 s` via `ffprobe`; 44.1 kHz stereo, 128 kbps MP3).
- **Audio listening note:** I cannot hear audio output directly, so I did not perform a listen-through. Instead, I checked the MP3 programmatically (`ffprobe` metadata; `ffmpeg volumedetect`: mean `-29.7 dB`, max `-11.2 dB`).
- **Transposition & score verification:** Reopened `weve-only-just-begun-tutti.mscz` in MuseScore 4.7.7 to export PDF and MP3; programmatically verified the internal concert MIDI `<pitch>` values of **Clarinet in B-flat** (bars 5–16) and **Horn in F** (bars 5–12) match every required sounding pitch above while displaying correctly transposed in B major and E major in the score; verified Flute, Bassoon, and all four string parts; verified chord-symbol playback remains off (`<play>0</play>`, `0.0` max sample diff vs. no-harmony WAV); visually inspected all four rendered PDF pages.
