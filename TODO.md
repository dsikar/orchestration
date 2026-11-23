# TODO

- Create a GitHub repo for this directory.
- Explore Harmonics and bowing at the bridge for second rehearsal April 30th. Need research on where harmonics occur on violin, viola, cello and double bass, then score accordingly observing which keys would harmonics suit.
- Test the `action prompt` loop with one agent (e.g. Codex).
- Discuss the directory structure in greater detail so it can accommodate the potentially hundreds of scores that will be created.

## Orchestration source maps

- Run `prompts/03-source-map-one-textbook.md` in parallel with one agent assigned to each textbook in `reference/textbooks/`. Save the four citation-ready maps in `research/source-maps/`.
- Organise and run an agent election to select the best source-map output. Give multiple independent agents anonymised maps, ask each to rank them against a shared rubric (citation accuracy, practical usefulness, clarity, coverage, and appropriate qualification), then record the votes, rationale, and winning map in `research/source-maps/election.md`.
- Ask an agent to create a reusable prompt for four agents to build an orchestration dictionary from the textbooks. The prompt must require defined terms, source locators, context/qualifications, and a separation between historic usage and current practical advice.
- Run a follow-up glossary review: give agents the proposed definitions, have them discuss ambiguities and suggest evidence-based edits, then combine the reviewed outputs into one citation-ready text at `research/orchestration-dictionary.md`.
- Plan and conduct a qualitative and quantitative frequency-analysis study of individual instruments, instrument combinations, and orchestral effects. Centre the eventual study on the human perception of orchestration—blend, brightness, roughness, masking, apparent loudness, spatial impression, and emotional/structural function—and use underlying acoustics (spectra, harmonic/inharmonic partials, formants, onset transients, dynamic and register effects) to complement the listening account. Define a reproducible corpus, listening methodology, measurement pipeline, limitations, and a final report structure before analysis begins.
- Once the GitHub repository exists, migrate each actionable to-do item into GitHub Issues; use labels (`research`, `agent-work`, `composition`, `rehearsal`, `infrastructure`, `review`) and milestones (`Library & source maps`, `Orchestration dictionary`, `Perception/physics study`, `First symphony draft`). Keep `TODO.md` as the concise roadmap linking to the issues.
