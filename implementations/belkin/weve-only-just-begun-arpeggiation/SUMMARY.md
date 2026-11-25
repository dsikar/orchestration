# We've Only Just Begun (Bars 1–16) — Belkin: Arpeggiation

## Textbook Passage and Rule

- **Book:** Alan Belkin, *Orchestration* (*Artistic Orchestration*), `reference/textbooks/alan-belkin-artistic-orchestration.pdf`, **PDF page 42** (*Background: movement* — *Arpeggiation*, citing Brahms's Symphony No. 3, 3rd movement, beginning, as a rocking string accompaniment).
- **Rule in Belkin's terms:** Arpeggiation animates a secondary background plane using chord tones already in the harmony. Kept quiet and consistent in a weaker plane of tone, the rocking figure adds gentle motion without competing as a second foreground tune.

## Material and Base Score

- **Base score copied:** `implementations/belkin/weve-only-just-begun-repeated-notes/` — **16 bars** in **A major**, **4/4**, **Moderately slow (Ballad) ♩ = 88**, for **Violin 1, Violin 2, Viola, and Cello**.
- **Only the Viola in bars 5–10 and bars 15–16 changes:** Violin 1, Violin 2, and Cello are unchanged across all 16 bars, and Viola bars 1–4 and 11–14 remain held half-note dyads.

## Viola Rocking Arpeggiation (Bars 5–10 and 15–16)

In bars 5–10 and 15–16, the Viola's four quarter-note dyads from the repeated-notes score are replaced by **eight eighth notes** rocking strictly between the same two chord tones already in each bar (`low, high, low, high, low, high, low, high`), staying at **`mp`** with `repeated notes` replaced by **`arpeggiation`** at bar 5 and bar 15:

- **Bar 5 (`A`):** `E3, C#4` (×4, `arpeggiation`)
- **Bar 6 (`Dmaj7`):** `F#3, C#4` (×4)
- **Bar 7 (`C#m7`):** `E3, B3` (×4)
- **Bar 8 (`F#m7`):** `E3, A3` (×4)
- **Bar 9 (`Bm7`):** `A3, D4` (×4)
- **Bar 10 (`F#m7`):** `A3, E4` (×4)
- **Bar 15 (`C#m7`):** `E3, B3` (×4, `mp`, `arpeggiation`)
- **Bar 16 (`F#m7`):** `E3, A3` (×4; excerpt still ends mid-phrase on `F#m7`)

## Software, Playback, and Checks Performed

- **MuseScore version:** MuseScore Studio `4.7.7` (`MuseSounds` / `Muse Strings`).
- **Playback duration:** `46.71 s` (`46.706875 s` via `ffprobe`; 44.1 kHz stereo, 128 kbps MP3).
- **Audio listening note:** I cannot hear audio output directly, so I did not perform a listen-through. Instead, I verified the MP3 programmatically (`ffprobe` metadata; `ffmpeg volumedetect`: mean `-30.8 dB`, max `-10.9 dB`).
- **Score verification:** Reopened `weve-only-just-begun-arpeggiation.mscz` in MuseScore 4.7.7 to export PDF and MP3; programmatically audited all 4 staves × 16 bars against `weve-only-just-begun-repeated-notes.mscz` (100% identical outside Viola bars 5–10 and 15–16, including intact bar 13–14 diminuendo hairpins); verified chord-symbol playback remains off (`<play>0</play>`, `0.0` max sample diff vs. no-harmony WAV); visually inspected both rendered PDF pages.
