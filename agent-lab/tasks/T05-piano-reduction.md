# T05 — Piano reduction

**Input:** `agent-lab/scores/excerpts/mozart-k157-i-bb1-16.musicxml`  
**Output:** `output.musicxml`  
**What it tests:** Collapsing four staves to a grand staff without losing the essential harmony.

## Instruction (paste this)

You are given a MusicXML score: Mozart, String Quartet K.157, movement I, bars 1–16, in C major.

Reduce it to a **piano grand staff** (treble + bass).

Requirements:

- Exactly two staves, one piano part.
- 16 bars, 4/4, C major.
- Keep the Violin 1 melody clearly in the right hand where it sits naturally.
- Keep the essential harmony and bass line; inner-voice omissions are allowed if the harmony remains clear.
- Stay in a playable piano range (no ten-note clusters, no impossible stretches as the default texture).
- Return a complete, well-formed MusicXML file and nothing else.

## Mechanical checks

| Check | Pass |
| --- | --- |
| File opens in MuseScore | |
| One piano part, two staves (G and F clefs) | |
| 16 measures, 4/4, C major | |
| Melody of bar 1 is recognisable | |
| Bass of bar 1 is recognisable (not empty, not the violin line) | |
