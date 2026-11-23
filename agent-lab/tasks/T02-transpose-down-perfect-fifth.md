# T02 — Transpose down a perfect fifth

**Input:** `agent-lab/scores/excerpts/mozart-k157-i-bb1-16.musicxml`  
**Output:** `output.musicxml`  
**What it tests:** A larger transposition (C → F) and bass range.

## Instruction (paste this)

You are given a MusicXML score: Mozart, String Quartet K.157, movement I, bars 1–16, in C major. Four concert-pitch parts: Violin 1, Violin 2, Viola (alto clef), Cello.

Transpose **every part down a perfect fifth**. The result must be in **F major**.

Requirements:

- Move every sounding pitch down seven semitones (a perfect fifth). Preserve octaves relative to that shift.
- Change the key signature to one flat (F major).
- Preserve rhythm, metre (4/4), bar count (16), articulations, slurs, dynamics, and tempo.
- Keep the same four parts and clefs (viola stays in alto clef).
- If the cello would go below its practical written range, use an 8va bassa indication only if unavoidable; prefer a correct pitch at the transposed octave.
- Return a complete, well-formed MusicXML file and nothing else.

## Mechanical checks

| Check | Pass |
| --- | --- |
| File opens in MuseScore | |
| Four parts, 16 measures | |
| Key signature = 1 flat | |
| Every pitch class is −7 semitones vs the input (spot-check bar 1 and bar 16) | |
| Cello not written below C2 without 8vb or a comment | |
| Violin 1 not dumped into viola/cello range by an extra octave error | |
| Output not truncated | |
