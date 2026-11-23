# Orchestration

Public repository: https://github.com/dsikar/orchestration

Work through the textbooks in this directory. For each passage put into practice, produce three files:

- a MuseScore score (`.mscz`)
- a PDF of that score
- a short summary of the implementation

An implementation is one claim, example, or technique taken from one book and written out as music. Keep each one short enough to hear the point. The summary names the book and the page, states what the passage says, states what the score does with it, and notes what the playback showed.

Save each implementation in its own folder:

```text
implementations/<book-slug>/<slug>/
├── <slug>.mscz
├── <slug>.pdf
└── SUMMARY.md
```

Use a lowercase hyphenated slug. `<book-slug>` matches the textbook, for example `rimsky-korsakov` or `belkin`.

## Textbooks on disk

| Book | File |
|---|---|
| Alan Belkin, *Orchestration* | `reference/textbooks/alan-belkin-artistic-orchestration.pdf` |
| Nikolay Rimsky-Korsakov, *Principles of Orchestration* (1912) | `reference/textbooks/rimsky-korsakov-principles-of-orchestration-1912.pdf` |
| Cecil Forsyth, *Orchestration* (1914) | `reference/textbooks/forsyth-orchestration-1914.pdf` |
| Adam Carse, *The History of Orchestration* (1925) | `reference/textbooks/carse-the-history-of-orchestration-1925.pdf` |
| Charles-Marie Widor, *The Technique of the Modern Orchestra* (1906) | `downloads/widor-the-technique-of-the-modern-orchestra-1906.pdf` |

Hector Berlioz and Richard Strauss, *Treatise on Instrumentation*, is a copyrighted 1991 ebook. The file stays on the local machine and is not in this public repository.

Belkin is the short book to read through. Rimsky-Korsakov is the book to write from. Forsyth is the instrument reference to check a doubtful part. Widor is the place to look when the others disagree. Carse explains how the orchestra changed. A fuller catalogue of titles, including books not on disk, is below and in `orchestration_titles.json`. Download notes are in `reports/download_report.md`.

`agent-lab/` is a separate exercise lab for mechanical MusicXML edits. New orchestration implementations go under `implementations/`, not there.

## Issues

- [#1](https://github.com/dsikar/orchestration/issues/1) — first book, Belkin. A piano sketch of the first 16 bars of "We've Only Just Begun", from a chord chart. This is the harmonic base for the Belkin exercises, not yet an orchestration of a passage from the book.
- [#2](https://github.com/dsikar/orchestration/issues/2) — Belkin, fat and thin sound. The issue #1 sketch: no invented tune in the intro, vocal melody from bar 5, unison doubling only in bars 11–12.
- [#5](https://github.com/dsikar/orchestration/issues/5) — Belkin, successive balance. The unison score stays thick in bars 11–12; bars 13–14 ease down on a held A instead of dropping straight to one violin.
- [#7](https://github.com/dsikar/orchestration/issues/7) — Belkin, octave doubling. The successive-balance score, with violin 2 an octave above violin 1 in bars 11–12 only.

## Catalogue of titles

Orchestration literature sits at the intersection of craft, history, acoustics, and style. The books below matter because they do more than list instrumental ranges: they show how composers have thought about color, balance, texture, and the expressive use of the orchestra across different periods.

## Foundational Treatises

- **Treatise on Instrumentation**. Hector Berlioz; expanded by Richard Strauss. 1844. One of the foundational orchestration treatises, combining technical discussion with an acute sense of instrumental color and expression. Strauss's expansion helped carry the work into the modern orchestral era.
- **Principles of Orchestration**. Nikolay Rimsky-Korsakov. 1912. A rare orchestration manual written by a composer renowned for orchestral color, still valued for its treatment of resonance, timbre, and orchestral combination. Its many examples from the composer's own scores make it especially practical.
- **The Technique of the Modern Orchestra: A Manual of Practical Instrumentation**. Charles-Marie Widor. 1904. An early twentieth-century supplement to Berlioz that updates practical instrumentation for a later orchestral world. It works well as a bridge between Romantic treatise writing and more modern technical manuals.

## 20th-Century Standards

- **Orchestration**. Walter Piston. 1955. A compact, clear, score-based textbook that became a standard in composition training. It balances technical instrument information with broader issues such as melody, chord spacing, counterpoint, and practical orchestral problem-solving.
- **Orchestration**. Cecil Forsyth. 1914. Famous for its unusually detailed instrument-by-instrument coverage and its preservation of pre-World War I orchestral knowledge. It is also historically valuable because it documents many rare, obsolete, and transitional instruments.
- **The Technique of Orchestration**. Kent Kennan and Donald Grantham. 1952. A long-running classroom standard focused on practical fundamentals, including instrumental writing, scoring, transcription, and preparation of score and parts. Its enduring strength is its concise, direct teaching style.
- **The Study of Orchestration**. Samuel Adler. 1982. One of the most comprehensive modern orchestration texts, pairing instrument study with literature-based examples and a composer's working perspective. Later editions add integrated audio and video resources that make it especially strong for formal study.

## Specialized / Advanced

- **Instrumentation and Orchestration**. Alfred Blatter. 1980. A broad working manual that combines textbook coverage with reference-book usefulness, spanning instruments, score preparation, ensemble scoring, transcription, and arrangement. It is especially good for students who want a practical all-round survey.
- **Orchestration**. Alan Belkin. 2001. A free online resource that approaches orchestration through form, texture, and listening rather than exhaustive cataloging of instruments. It is often most useful as a modern companion to the larger printed textbooks.

## Historically Oriented

- **The History of Orchestration**. Adam Carse. 1925. A classic historical survey of how the orchestra developed from the seventeenth century into the modern period. It is especially useful for understanding changes in instrumental families, balance, color, and orchestral thinking across styles.
- **A History of Music in Western Culture**. Mark Evan Bonds. 2003. Broader than a pure orchestration text, but valuable for situating orchestral writing inside the larger history of repertoire, style, and listening. It is best used as contextual reading alongside more technical manuals.

## Notes on Free / Online Resources

Alan Belkin's *Orchestration* is available free on the author's site, including a PDF version. In addition, public-domain or library-hosted downloadable scans were located for Widor, Rimsky-Korsakov, Forsyth, and Carse during this run; see `reports/download_report.md` for the actual download status and saved filenames.

Generated on 2026-04-23.
