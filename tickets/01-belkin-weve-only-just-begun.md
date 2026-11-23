# Ticket: Harmonic base for Belkin — first 16 bars of "We've Only Just Begun"

The first textbook in this project is **Alan Belkin, *Orchestration***, file `reference/textbooks/alan-belkin-artistic-orchestration.pdf`.

This ticket does not orchestrate a passage from Belkin. It builds the **harmonic base** that the first Belkin exercises will use: a playable MuseScore setting of the **first 16 bars** of **"We've Only Just Begun"**, taken from an online chord chart.

Read `README.md` first. Follow its rule that each implementation is a MuseScore score, a PDF, and a short summary. Save the result under `implementations/belkin/`. Do not put it in `agent-lab/`.

Work in the orchestration directory that contains this ticket (`/home/daniel/Documents/music/ELLSO/orchestration` on Daniel's machine, or the checkout you were given). There is no GitHub remote. Do not create a repository, commit, or push unless you are asked separately.

## 1. Find a chord chart

Choose an online chord chart for **"We've Only Just Begun"** (Paul Williams and Roger Nichols; the well-known recording is by the Carpenters, 1970). The chart must show chord names and where they change, with a key, a time signature, and enough of the form to identify the opening.

Record:

- the exact URL and the access date
- the songwriting credits the page gives
- which recording or version the chart claims to describe, if it says
- the chart's key, metre, tempo, and any capo or transposition
- the author or site of the chart

Prefer one chart that covers the opening continuously. If you must combine a chord chart with a second page to see the bar lines or the form, both pages must describe the same version and key. Document any disagreement.

**First 16 bars** means the first 16 bars of that chart's opening, counted from the start of the song as the chart bars it. Do not choose a later 16-bar slice. Do not repeat a 4-bar loop and call it 16 bars. If the opening includes a pickup, say whether your bar 1 is the pickup or the first full bar, and still deliver 16 notated bars. Name the sections those bars cover (for example intro, verse) and give their chart bar numbers.

The song is still under copyright. Rights in the song are separate from rights in a particular chart. A page that is publicly viewable is not permission to redistribute it. Keep a downloaded chart file only when its terms allow; otherwise keep the link and attribution and do not commit the file. Do not paste the chart's text, lyrics, or tablature into the summary. Do not bypass logins, paywalls, download limits, or bot protection, and do not make purchases. If a source is blocked, choose another accessible chart and say so.

## 2. Write the 16 bars in MuseScore

Create one piano score, grand staff, labelled **Piano**. This is a harmonic sketch, not a transcription of the Carpenters' arrangement and not an orchestration.

- Enter every chord from the chart as a **chord symbol** above the treble staff, aligned to the beat where the chart changes chord.
- Write a simple piano realization that sounds those chords: the bass note in the left hand, and a clear voicing in the right hand. Use one plain, repeatable pattern. In `SUMMARY.md`, identify the voicings and the rhythm as your own editorial realization of the chart.
- Stop chord symbols from playing back on top of the written piano part.
- Include the vocal melody only when the chosen chart, or a second source of the same version and key, actually gives the pitches for these 16 bars. If it does not, do not invent a melody. Say that the score is chords only.
- Set the key, time signature, and tempo from the chart. If the chart uses a capo or a transposed key, write concert pitch and state how you reconciled it.
- Mark sections when the 16 bars cross a boundary such as intro and verse.
- The file contains **16 bars**, no more and no fewer, with no extra repeats that would play a longer span.

Open the saved `.mscz` in MuseScore and check it. Check every chord against the chart. Do not treat an automatic import as already correct.

## 3. Save the implementation

```text
implementations/belkin/weve-only-just-begun-bars-1-16/
├── weve-only-just-begun-bars-1-16.mscz
├── weve-only-just-begun-bars-1-16.pdf
├── weve-only-just-begun-bars-1-16.mp3
└── SUMMARY.md
```

The PDF must show the chord symbols and all 16 bars. Reopen the `.mscz` and confirm that the notation is still there. Export an MP3 so the progression can be heard. If you cannot hear it, say so in the summary and do not describe a listen-through.

`SUMMARY.md` is short. Include:

- Song title, writers, and the version or recording the chart refers to.
- Chart URL, access date, key, metre, tempo, and what bars 1–16 cover.
- A bar-by-bar list of the chord symbols as entered.
- What is editorial (voicing and rhythm) and whether a melody is included.
- MuseScore version, the piano sound used, and the playback duration.
- Confirmation that the score is 16 bars and that each chord was checked against the chart.
- One sentence stating that this score is the harmonic base for the first Belkin exercises, and that no Belkin orchestration technique has been applied yet.

## 4. Done when

- The score opens as a piano sketch of exactly 16 bars, and the chord symbols match the chosen chart.
- The written piano part plays those changes without a second chord-symbol playback.
- The `.mscz`, `.pdf`, `.mp3`, and `SUMMARY.md` are in the folder above.
- The summary gives the source link, the bar mapping, and the checks actually performed.
