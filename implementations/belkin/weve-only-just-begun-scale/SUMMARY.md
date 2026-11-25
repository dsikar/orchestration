# We've Only Just Begun (Bars 1–16) — Belkin: Background Scale

## Textbook Passage and Rule

- **Book:** Alan Belkin, *Orchestration* (*Artistic Orchestration*), `reference/textbooks/alan-belkin-artistic-orchestration.pdf`, **PDF page 42** (*Background: movement* — *Scales*).
- **Rule in Belkin's terms:** Scales are one of the four basic types of background movement; a light scale adds vitality and musical direction under a main line while remaining clearly set off in a weaker plane of tone so it stays quieter than the tune and does not cover the foreground.

## Material and Base Score

- **Base score copied:** `implementations/belkin/weve-only-just-begun-repeated-notes/` — **16 bars** in **A major**, **4/4**, **Moderately slow (Ballad) ♩ = 88**, for **Violin 1, Violin 2, Viola, and Cello**.
- **Only Violin 2 in bars 9–10 changes:** Violin 1, Viola (including its repeated notes), Cello, and Violin 2 in bars 1–8 and 11–16 (heterophony in bars 11–12, held `A3` and diminuendo in bars 13–14, tacet elsewhere) are unchanged.

## Background Scales in Violin 2 (Bars 9–10 Only)

In bars 9–10 — sitting quietly underneath Violin 1's melody for a single phrase at **`mp`**, marked **`scale`** at bar 9 — Violin 2 plays two unharmonized eighth-note scales (eight notes per bar):

- **Bar 9 (`Bm7`, rising):** `B3, C#4, D4, E4, F#4, G#4, A4, B4`
- **Bar 10 (`F#m7`, falling):** `F#4, E4, D4, C#4, B3, A3, G#3, F#3` *(Note: `F#3` is entered verbatim per the issue specification, though it lies one semitone below the violin's standard `G3` lowest string.)*

The excerpt still ends mid-phrase on `F#m7` in bar 16.

## Software, Playback, and Checks Performed

- **MuseScore version:** MuseScore Studio `4.7.7` (`MuseSounds` / `Muse Strings`).
- **Playback duration:** `46.71 s` (`46.706875 s` via `ffprobe`; 44.1 kHz stereo, 128 kbps MP3).
- **Audio listening note:** I cannot hear audio output directly, so I did not perform a listen-through. Instead, I verified the MP3 programmatically (`ffprobe` metadata; `ffmpeg volumedetect`: mean `-30.5 dB`, max `-10.9 dB`).
- **Score verification:** Reopened `weve-only-just-begun-scale.mscz` in MuseScore 4.7.7 to export PDF and MP3; programmatically audited all 4 staves × 16 bars against `weve-only-just-begun-repeated-notes.mscz` (100% identical outside Violin 2 bars 9–10); verified chord-symbol playback remains off (`<play>0</play>`, `0.0` max sample diff vs. no-harmony WAV); visually inspected the rendered PDF pages.
