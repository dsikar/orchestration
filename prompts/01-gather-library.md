```
Agent Task: Gather Orchestration Titles & Create README

You are a research and file-organization agent. Your task is to gather information about classic orchestration titles and organize the results into a structured output.

## Instructions

### 1. Search & Gather Book Information
For each title in the list below, search the web to retrieve the following fields where available:
- Full title and subtitle
- Author(s)
- Publication year (and revised editions)
- Publisher
- ISBN (preferably the most recent edition)
- A 1–2 sentence description of the book's significance
- A purchase or reference URL (e.g. Amazon, Google Books, or publisher page)

### 2. Titles to Research
Search for the following books:

**Foundational Treatises**
- Treatise on Instrumentation – Berlioz (expanded by Strauss)
- Principles of Orchestration – Rimsky-Korsakov
- The Technique of the Modern Orchestra – Widor

**20th-Century Standards**
- Orchestration – Walter Piston
- Orchestration – Cecil Forsyth
- The Technique of Orchestration – Kent Kennan & Donald Grantham
- The Study of Orchestration – Samuel Adler

**Specialized / Advanced**
- Instrumentation and Orchestration – Alfred Blatter
- Orchestration – Alan Belkin (online resource)

**Historically Oriented**
- The History of Orchestration – Adam Carse
- A History of Music in Western Culture – Mark Evan Bonds

### 3. Output Files

**File 1 — orchestration_titles.json**
Produce a JSON file with an array of objects, one per book, using this schema:
{
  "title": "",
  "subtitle": "",
  "authors": [],
  "year": "",
  "editions": [],
  "publisher": "",
  "isbn": "",
  "description": "",
  "url": ""
}

**File 2 — README.md**
Produce a well-formatted Markdown file that includes:
- A top-level heading: # Classic Titles on Orchestration
- A short introductory paragraph explaining the importance of orchestration literature
- One section per category (Foundational Treatises, 20th-Century Standards, etc.)
- Each book listed with: title (bold), author, year, and its 1–2 sentence description
- A closing section with notes on free/online resources (e.g. Alan Belkin's free text)
- A footer with the date the file was generated

### 4. Constraints & Notes
- Prefer authoritative sources (publisher sites, WorldCat, Google Books, Open Library)
- If an ISBN or URL cannot be found, use null for that field — do not invent data
- If a book has multiple well-known editions, list up to 3 in the editions array
- Save both files to the working output directory when complete
```
