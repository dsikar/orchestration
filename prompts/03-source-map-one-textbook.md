```
Agent Task: Map One Orchestration Textbook for Citation-Ready Use

You are a careful music-research agent. Survey ONE of the orchestration textbooks
in `reference/textbooks/` and create a source map that lets a composer find the
book's useful advice quickly while writing for orchestra.

## Assignment

The coordinator will specify the PDF filename. Work only on that assigned book;
do not attempt to summarise the other textbooks.

Source directory:
`reference/textbooks/`

Output directory:
`research/source-maps/`

Create one Markdown file named:
`research/source-maps/<book-slug>.md`

Use a short, unambiguous slug based on the author and title, for example
`rimsky-korsakov-principles.md`.

## Purpose

This is a source map, not a book report and not a substitute for reading the
book. Its purpose is to identify where the book is most useful for practical
orchestration questions, particularly:

- string voicing, divisi, desk splitting, and register;
- wind and brass voicing, blend, doubling, balance, and spacing;
- instrumental range, colour, articulation, and idiom;
- texture, orchestral growth, contrast, and transitions.

## Method

1. Inspect the PDF metadata and table of contents first. Record the book's full
   bibliographic details as they appear in the PDF.
2. Map every top-level part or chapter. For each, give its title, its opening
   page, a concise statement of its focus, and its likely value to the composer.
3. Read closely enough to identify the most useful sections for the practical
   topics above. Do not infer advice from chapter titles alone.
4. For every locator, give both the PDF page number and the printed page number
   when one is visible. If the scan has no printed pagination, explicitly say so.
5. Distinguish carefully among:
   - practical guidance the author explicitly gives;
   - historical description or stylistic observation;
   - your own inference. Label inferences as such.
6. Preserve the author's nuance. Orchestration advice depends on register,
   dynamic, articulation, orchestral size, and musical context; do not turn a
   qualified observation into an absolute rule.

## Required Output Structure

# <Author> — <Title>: Source Map

## Bibliographic record

- Author, full title/subtitle, edition or publication year where stated.
- PDF filename.
- Total PDF pages.
- A note explaining how PDF and printed pagination relate, if applicable.

## Book at a glance

In 150–250 words, explain the book's central approach. State whether it is
mainly a practical manual, a historical survey, an aesthetic/compositional
treatise, or a mixture. State its strongest and weakest uses for the current
project: writing a symphony for a real amateur/community orchestra.

## Table-of-contents map

Use a table with these columns:

| Part/chapter | Starts (PDF / printed) | Focus | Practical value | Priority |

Use `high`, `medium`, or `low` for Priority. Include all top-level divisions;
combine only very short, purely administrative items.

## High-value passages by composing question

Organise this section by whichever categories the book genuinely supports:

- Strings
- Woodwinds
- Brass and percussion
- Doubling, voicing, and balance
- Texture, form, and colour
- Score preparation or notation

For each passage, use this exact pattern:

### <Specific composing question>

- **Locator:** Part/chapter/section; PDF p. X; printed p. Y.
- **What the author says:** a concise, faithful paraphrase.
- **Conditions and limits:** the relevant register, dynamic, style, ensemble,
  or exception stated by the author; write `not stated` if none is given.
- **Use in the symphony:** one practical sentence describing when the composer
  should consult or test this advice.

Include only passages you have actually checked. Prefer approximately 8–15
high-value entries over a long list of vague observations.

## Short quotation bank

Include at most five short quotations, each only when exact wording is more
valuable than a paraphrase. Give a full locator for each. Do not reproduce long
passages.

## Recommended first reads

List the 3–5 sections that should be read first before drafting a symphonic
passage, with a one-sentence reason for each.

## Gaps and cautions

Identify material that may be historically dated, incomplete, tied to a
particular national/style tradition, or otherwise needs confirmation with
present-day players, conductor, or an instrument-specific reference.

## Quality Bar

- Never invent a page number, chapter title, quotation, or technical claim.
- Use exact locators that another person can verify in the supplied PDF.
- Keep descriptions specific and concise; avoid generic statements such as
  “discusses orchestration.”
- Do not claim that a historical source is a modern performance-practice rule.
- Do not give medical, legal, copyright, or purchasing advice.
- Finish with a short `## Survey completeness` note explaining what you checked
  closely and any portions that could not be read reliably.
```
