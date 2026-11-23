# T03 — Rewrite in A minor (key change, not transposition)

**Input:** `agent-lab/scores/excerpts/mozart-k157-i-bb1-16.musicxml`  
**Output:** `output.musicxml`  
**What it tests:** Whether the agent can change **key**, not merely slap a new signature on the same pitches, and not merely transpose C major → A minor.

## Instruction (paste this)

You are given a MusicXML score: Mozart, String Quartet K.157, movement I, bars 1–16, in C major.

Rewrite the excerpt so that it is **in A minor**, as a composer would recast the passage — not as a mechanical transposition of every pitch down a minor third, and not as C-major music with an A-minor key signature.

Requirements:

- Key signature must be A minor (no sharps or flats, like C major, but the **tonic is A**).
- Cadences that were on C should now function as cadences on A (or a clearly A-minor equivalent).
- Use A-minor pitch collection and leading tones (G#) where the new key needs them.
- Keep 16 bars, 4/4, four string parts, original clefs, and a similar rhythmic profile.
- Preserve the character of the opening (Allegro quartet texture), not a new piece from scratch.
- Return a complete, well-formed MusicXML file and nothing else.

## Mechanical checks

| Check | Pass |
| --- | --- |
| File opens in MuseScore | |
| Four parts, 16 measures, 4/4 | |
| Key signature has 0 sharps/flats | |
| **Fail if** pitches are identical to the input (signature-only cheat) | |
| **Fail if** every pitch is a literal −3 semitone transpose of the input (that is T01-style transposition, not a key rewrite) | |
| Closing harmony of bar 16 (or last cadence) functions in A minor | |
| G# (or equivalent leading tone) appears where A-minor grammar needs it | |
