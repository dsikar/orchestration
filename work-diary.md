# Work Diary

## 2026-09-01

Built an agent MusicXML lab so prompts can be actioned and checked by ear and eye, without hunting for files.

Chose Mozart String Quartet No. 4 in C major, K.157 (OpenScore `sq9199617`, CC0) as the first fixture. Did not scrape MuseScore.com: fetched `.mxl` and `.mscx` from the OpenScore GitHub mirror and converted to uncompressed `.musicxml` with local MuseScore Studio 4.6.5.

Cropped movement I, bars 1–16, as the agent input (`agent-lab/scores/excerpts/mozart-k157-i-bb1-16.musicxml`). Wrote frozen tasks T01–T07 (transpose, key change, reharmonise, piano reduction, new quartet, viola treble clef) and a T08 stub for horns in F.

Settled the operator loop: say `action prompt <path>`. The result always lands in `agent-lab/out/`. `agent-lab/scripts/present-score.sh` exports PDF and audio, opens MuseScore, opens the PDF, and plays the music. Smoke-tested that presenter on the Mozart excerpt; MuseScore, PDF, and playback all came up.

Testing against a real agent is left for tomorrow.

## 2026-04-23

Today I actioned the library-gathering prompt in [prompts/01-gather-library.md](/home/daniel/Documents/music/ELLSO/orchestration/prompts/01-gather-library.md).

I researched the listed orchestration titles and created [orchestration_titles.json](/home/daniel/Documents/music/ELLSO/orchestration/orchestration_titles.json) with structured metadata for each title.

I created [README.md](/home/daniel/Documents/music/ELLSO/orchestration/README.md) summarising the classic orchestration titles by category.

I downloaded and saved the freely accessible titles that were available as PDFs into [downloads](/home/daniel/Documents/music/ELLSO/orchestration/downloads).

I created [reports/download_report.md](/home/daniel/Documents/music/ELLSO/orchestration/reports/download_report.md) to record successful downloads and titles that were not freely downloadable during the automated run.

I checked `~/Downloads` for newer arrivals and found a manually downloaded Berlioz/Strauss ebook file.

I moved that file into the project as [berlioz-strauss-treatise-on-instrumentation-1991.mobi](/home/daniel/Documents/music/ELLSO/orchestration/downloads/berlioz-strauss-treatise-on-instrumentation-1991.mobi) and updated the download report to note that this title was downloaded manually as a `.mobi`.

The todo list must be tackled next.
