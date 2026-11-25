# We've Only Just Begun (Bars 1–16) — Belkin: Contrapuntal Line

## Textbook Passage and Rule

- **Book:** Alan Belkin, *Orchestration* (*Artistic Orchestration*), `reference/textbooks/alan-belkin-artistic-orchestration.pdf`, **PDF page 46** (*Contrapuntal Orchestration*).
- **Rule in Belkin's terms:** A contrapuntal line is an independent second musical line — neither a doubling nor a repetitive background figure. To achieve clear balance between contrapuntal lines, the simplest strategy is assigning them to instruments of the same family (here two violins) while keeping the principal tune clearer through register and rhythmic activity.

## Material and Base Score

- **Base score copied:** `implementations/belkin/weve-only-just-begun-heterophony/` — **16 bars** in **A major**, **4/4**, **Moderately slow (Ballad) ♩ = 88**, for **Violin 1, Violin 2, Viola, and Cello**.
- **Only Violin 2 in bars 5–8 changes:** Violin 1, Viola, and Cello are unchanged across all 16 bars, and Violin 2 keeps its rests in bars 1–4, 9–10, and 15–16, its heterophony in bars 11–12, and its held `A3` (`successive balance`) in bars 13–14.

## Contrapuntal Line in Violin 2 (Bars 5–8 Only)

Where Violin 2 was tacet in bars 5–8, it now plays a slower, independent contrapuntal line at **`mp`**, marked **`counterpoint`** at bar 5. It moves with its own melodic contour and slower harmonic rhythm rather than doubling Violin 1:

- **Bar 5 (`A`):** half `C#4`, half `B3` (`mp`, `counterpoint`)
- **Bar 6 (`Dmaj7`):** half `A3`, half `F#4`
- **Bar 7 (`C#m7`):** whole `B3`
- **Bar 8 (`F#m7`):** half `C#4`, half `A3`

The line does not extend past bar 8, and the excerpt still ends mid-phrase on `F#m7` in bar 16.

## Software, Playback, and Checks Performed

- **MuseScore version:** MuseScore Studio `4.7.7` (`MuseSounds` / `Muse Strings`).
- **Playback duration:** `46.71 s` (`46.706875 s` via `ffprobe`; 44.1 kHz stereo, 128 kbps MP3).
- **Audio listening note:** I cannot hear audio output directly, so I did not perform a listen-through. Instead, I verified the MP3 programmatically (`ffprobe` metadata; `ffmpeg volumedetect`: mean `-30.1 dB`, max `-10.8 dB`).
- **Score verification:** Reopened `weve-only-just-begun-counterpoint.mscz` in MuseScore 4.7.7 to export PDF and MP3; programmatically audited all 4 staves × 16 bars against `weve-only-just-begun-heterophony.mscz` (100% identical outside Violin 2 bars 5–8); verified chord-symbol playback remains off (`<play>0</play>`, `0.0` max sample diff vs. no-harmony WAV); visually inspected the rendered PDF pages.
