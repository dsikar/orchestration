# Where we are

Orchestration directory. Agent MusicXML lab is built. Not yet tested with another agent.

**The score:** Mozart string quartet K.157, movement I, bars 1–16. Lives in `agent-lab/`.

**What you say:** `action prompt agent-lab/tasks/T01-transpose-up-major-second.md`

Then sit. MuseScore opens, the PDF opens, the music plays. Do not look for files.

**Next:** run that once with Codex. After that, talk about folders — `out/` is only the current score, and we will have many.

T08 (horns) is a stub. Skip it. No git repo yet. Harmonics research is a separate, older todo.

**Friday 27 November 2026, 14:00.** Check the last seven Belkin scores of "We've Only Just Begun".

1. Repeated notes — `/home/daniel/Documents/music/ELLSO/orchestration/implementations/belkin/weve-only-just-begun-repeated-notes/weve-only-just-begun-repeated-notes.mscz`
2. Tremolo — `/home/daniel/Documents/music/ELLSO/orchestration/implementations/belkin/weve-only-just-begun-tremolo/weve-only-just-begun-tremolo.mscz`
3. Scale — `/home/daniel/Documents/music/ELLSO/orchestration/implementations/belkin/weve-only-just-begun-scale/weve-only-just-begun-scale.mscz`
4. Arpeggiation — `/home/daniel/Documents/music/ELLSO/orchestration/implementations/belkin/weve-only-just-begun-arpeggiation/weve-only-just-begun-arpeggiation.mscz`
5. Counterpoint — `/home/daniel/Documents/music/ELLSO/orchestration/implementations/belkin/weve-only-just-begun-counterpoint/weve-only-just-begun-counterpoint.mscz`
6. Soft tutti — `/home/daniel/Documents/music/ELLSO/orchestration/implementations/belkin/weve-only-just-begun-tutti/weve-only-just-begun-tutti.mscz`
7. Accompaniment — `/home/daniel/Documents/music/ELLSO/orchestration/implementations/belkin/weve-only-just-begun-accompaniment/weve-only-just-begun-accompaniment.mscz`

**Finding melody and harmonisation candidates.** Do this before the next Belkin scores. Find passages that already have both a melody and a harmonisation. Do not invent either.

A candidate needs:

- A melody that can be read from a named source.
- A harmonisation that can be checked against that source, or against a named chord chart.
- A length that can be scored as it stands. The exercises so far are 16 bars, and they stop where the source stops.
- A joint in the phrase where a doubling can end and another line can take over. The first technique below needs that joint.
- No lyric and no chart committed to the repo. Name the source only, as issue #1 did for "We've Only Just Begun" (Hal Leonard Real Book, Sheet Music Direct 480653; Musicnotes MN0034721).

"We've Only Just Begun", bars 1–16, stays the current base until a candidate is chosen.

**Next steps in Belkin.** Alan Belkin, *Artistic Orchestration*, `/home/daniel/Documents/music/ELLSO/orchestration/reference/textbooks/alan-belkin-artistic-orchestration.pdf`. These are the unused techniques that still fit a short excerpt, in book order.

1. Doubling which becomes counterpoint (PDF p. 38). A part starts by doubling, then at a real joint becomes its own line. On the current excerpt that joint is bar 13: violin 2 would keep the heterophony in bars 11–12, then leave it for a slower independent line through bars 13–16. The line has to be a found melody. The excerpt still ends on F#m7. Bars 1–12 stay as they are.
2. Piecemeal doubling (same page). One part moves from doubling one existing line to doubling another, and does not add a new melody. The heterophony score already has the lines for this.
3. Partial doubling does not need its own score. Bars 11–14 already double a highlight and then settle on a held note.

After accompaniment, the book is a checklist (p. 58), a conclusion, and two appendices. Those are not further scores. The later accompaniment ideas, dialogue, loud alternation with the soloist, and doubling a singer, do not fit this ballad or a 16-bar stop.

Sustained against dry sound (p. 33) is the earlier section that can still be a score on a short excerpt. The other basic notions on pages 19–32 need a longer span.
