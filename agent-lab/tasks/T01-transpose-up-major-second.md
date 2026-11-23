# T01 — Transpose up a major second

**Input:** `agent-lab/scores/excerpts/mozart-k157-i-bb1-16.musicxml`  
**Output:** `output.musicxml`  
**What it tests:** Chromatic transposition of a C-major quartet (interval + key signature).

## Instruction (paste this)

You are given a MusicXML score: Mozart, String Quartet K.157, movement I, bars 1–16, in C major. Four concert-pitch parts: Violin 1, Violin 2, Viola (alto clef), Cello.

Transpose **every part up a major second**. The result must be in **D major**.

Requirements:

- Move every sounding pitch up two semitones (a major second). Preserve octaves relative to that shift — do not drop or raise extra octaves.
- Change the key signature to two sharps (D major).
- Preserve rhythm, metre (4/4), bar count (16), articulations, slurs, dynamics, and tempo.
- Keep the same four parts and clefs (viola stays in alto clef).
- Return a complete, well-formed MusicXML file and nothing else.

## Mechanical checks

| Check | Pass |
| --- | --- |
| File opens in MuseScore | |
| Four parts, 16 measures | |
| Key signature = 2 sharps | |
| Time signature still 4/4 | |
| Every pitch class is +2 semitones vs the input (spot-check bar 1 and bar 16, all parts) | |
| Violin 1 tessitura still violin-like (not an octave too high/low) | |
| Cello tessitura still cello-like | |
| Output not truncated mid-measure | |
