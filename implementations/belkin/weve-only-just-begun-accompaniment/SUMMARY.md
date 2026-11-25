# We've Only Just Begun (Bars 1–16) — Belkin: Wind Accompaniment for Solo Violin

## Textbook Passage and Rule

- **Book:** Alan Belkin, *Orchestration* (*Artistic Orchestration*), `reference/textbooks/alan-belkin-artistic-orchestration.pdf`, **PDF pages 51–53** (*Orchestral Accompaniment*).
- **Rule in Belkin's terms:** When accompanying a soloist, the main problem is supporting the solo without drowning it out or reducing the accompaniment to a feeble, unbroken murmur. Belkin brings out the soloist through contrast of timbre (here solo string against two woodwinds) and rhythm (making the solo line the only moving melodic voice), while aerating the accompaniment with rests and staccato bass notes.

## Material and Ensemble

- **Solo Violin (`mf`):** Alone against two woodwinds — no second violin, viola, cello, or tutti. Copied directly from Violin 1 of `implementations/belkin/weve-only-just-begun-heterophony/` (tacet bars 1–4, vocal melody bars 5–16), with the 16 chord symbols above the solo staff (`<play>0</play>`), in **A major**, **4/4**, **Moderately slow (Ballad) ♩ = 88**, ending mid-phrase on `F#m7`.
- **Accompaniment (two winds at `mp`, never doubling the solo line):**
  - **Clarinet in B-flat (`mp`, written up a major 2nd in B major, 5 sharps):** Two half notes per bar (beat 1 and beat 3, leaving beats 2 and 4 unfilled) across bars 1–16.
  - **Bassoon (C, `mp`):** One **staccato quarter note on beat 1**, followed by a quarter rest and half rest (three beats of rest), across bars 1–16.

### Sounding Pitches by Bar

| Bar | Chord | Clarinet in Bb (sounding, beat 1 & beat 3) | Clarinet written | Bassoon (sounding, staccato beat 1) |
|---|---|---|---|---|
| 1 | `A` | `C#4` | `D#4` | `A2` |
| 2 | `Dmaj7` | `F#4` | `G#4` | `D3` |
| 3 | `A` | `C#4` | `D#4` | `A2` |
| 4 | `Dmaj7` | `F#4` | `G#4` | `D3` |
| 5 | `A` | `C#4` | `D#4` | `A2` |
| 6 | `Dmaj7` | `F#4` | `G#4` | `D3` |
| 7 | `C#m7` | `E4` | `F#4` | `C#3` |
| 8 | `F#m7` | `A4` | `B4` | `F#2` |
| 9 | `Bm7` | `D4` | `E4` | `B2` |
| 10 | `F#m7` | `E4` | `F#4` | `F#2` |
| 11 | `Bm7` | `D4` | `E4` | `B2` |
| 12 | `Bm7/E` | `D4` | `E4` | `E2` |
| 13 | `A` | `C#4` | `D#4` | `A2` |
| 14 | `Dmaj7` | `F#4` | `G#4` | `D3` |
| 15 | `C#m7` | `B3` | `C#4` | `C#3` |
| 16 | `F#m7` | `A3` | `B3` | `F#2` |

## Software, Playback, and Checks Performed

- **MuseScore version:** MuseScore Studio `4.7.7` (`MuseSounds` — `Muse Strings` Solo Violin, `Muse Woodwinds` Clarinet in B-flat and Bassoon).
- **Playback duration:** `46.71 s` (`46.706875 s` via `ffprobe`; 44.1 kHz stereo, 128 kbps MP3).
- **Audio listening note:** I cannot hear audio output directly, so I did not perform a listen-through. Instead, I checked the MP3 programmatically (`ffprobe` metadata; `ffmpeg volumedetect`: mean `-35.7 dB`, max `-18.6 dB`).
- **Transposition & score verification:** Reopened `weve-only-just-begun-accompaniment.mscz` in MuseScore 4.7.7 to export PDF and MP3; programmatically confirmed every bar's Clarinet in B-flat internal concert MIDI `<pitch>` matches the exact sounding table above (while displaying transposed up a major 2nd in B major on the score); confirmed every Bassoon bar has a staccato quarter note on beat 1 matching the exact cello bass line followed by three beats of rest; verified chord-symbol playback remains off (`<play>0</play>`, `0.0` max sample diff vs. no-harmony WAV); visually inspected both rendered PDF pages.
