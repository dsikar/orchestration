# T07 — Viola in treble clef

**Input:** `agent-lab/scores/excerpts/mozart-k157-i-bb1-16.musicxml`  
**Output:** `output.musicxml`  
**What it tests:** Clef change without pitch change (alto-clef handling).

## Instruction (paste this)

You are given a MusicXML score: Mozart, String Quartet K.157, movement I, bars 1–16, in C major.

Rewrite the **Viola** part in **treble clef**. Concert pitches must stay exactly the same. Do not change Violin 1, Violin 2, or Cello.

Requirements:

- Viola clef becomes G (treble), line 2.
- Every viola sounding pitch is unchanged (same octave).
- Other three parts identical to the input.
- 16 bars, 4/4, C major.
- Return a complete, well-formed MusicXML file and nothing else.

## Mechanical checks

| Check | Pass |
| --- | --- |
| File opens in MuseScore | |
| Four parts, 16 measures | |
| Viola staff clef is treble | |
| Viola pitches identical to input (watch octave errors — this is the usual fail) | |
| Violin 1, Violin 2, Cello unchanged | |
