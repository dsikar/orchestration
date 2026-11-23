# T06 — Harmonise Violin 1 as a new quartet

**Input:** `agent-lab/scores/excerpts/mozart-k157-i-bb1-16.musicxml`  
**Output:** `output.musicxml`  
**What it tests:** Melody extraction plus invented four-part writing.

## Instruction (paste this)

You are given a MusicXML score: Mozart, String Quartet K.157, movement I, bars 1–16, in C major.

Extract **Violin 1** and treat it as a given melody. Compose **new** Violin 2, Viola, and Cello parts that harmonise it as a string quartet in C major. Do not reuse the original lower parts.

Requirements:

- Violin 1 must match the input note-for-note.
- Three newly composed lower parts, playable on those instruments, original clefs.
- 16 bars, 4/4, C major.
- Cadence in bar 16 should be a clear C-major close (or a half cadence if you are continuing the phrase — say which in a comment only if you must; prefer a close).
- Return a complete, well-formed MusicXML file and nothing else.

## Mechanical checks

| Check | Pass |
| --- | --- |
| File opens in MuseScore | |
| Four parts, 16 measures, C major | |
| Violin 1 identical to input | |
| Lower parts differ from the Mozart original | |
| Ranges plausible for vn2 / viola / cello | |
