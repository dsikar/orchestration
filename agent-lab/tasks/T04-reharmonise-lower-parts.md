# T04 — Reharmonise the three lower parts

**Input:** `agent-lab/scores/excerpts/mozart-k157-i-bb1-16.musicxml`  
**Output:** `output.musicxml`  
**What it tests:** Harmonisation with a frozen melody.

## Instruction (paste this)

You are given a MusicXML score: Mozart, String Quartet K.157, movement I, bars 1–16, in C major.

Keep **Violin 1 exactly as written** (same pitches, rhythm, articulations).

Rewrite Violin 2, Viola, and Cello as a **different but still tonal** accompaniment for those 16 bars. Stay in C major. Examples of acceptable new textures: closer spacing, a pedal in the cello with suspensions above, or a more chorale-like inner pair. Do not copy the original inner parts.

Requirements:

- Violin 1 must match the input note-for-note.
- The three lower parts must change.
- Four parts, 16 bars, 4/4, original clefs, C major.
- Writing must be playable on violin, viola, and cello (respect ranges; avoid unplayable double stops).
- Return a complete, well-formed MusicXML file and nothing else.

## Mechanical checks

| Check | Pass |
| --- | --- |
| File opens in MuseScore | |
| Four parts, 16 measures, C major, 4/4 | |
| Violin 1 pitches identical to input | |
| Violin 2 / viola / cello are not identical to input | |
| No part written outside a plausible instrument range | |
