# Transcribing course files

How course files become clean Markdown with their figures cropped: slide decks, exercise and solution sheets, exams with their keys, quiz captures, course-site pages, announcements, the student's own notes. Read it in full before transcribing anything; [[setting-up-new-material]] says where each output goes in the course folder.

## Goal

Clean, complete Markdown in French, used as study material and as the source for Socratic tutoring (a tutor shows a statement, waits for the answer, then reveals the solution). Merge the files that cover the same content, remove all noise, keep all substance, and fold the student's notes in as highlights and comments. The `.md` files and their images replace the originals as study material; the originals are archived, never deleted.

When rules pull in different directions: fidelity first, then completeness, then structure, then concision.

**Everything you can, nothing more.** This may run with file access or in a chat with a few attached files. Do every step your tools and inputs allow; skip the rest, without apology, workaround or question (no file access: deliver the files in your answer, without images, §9; no page images: work from the text layer and flag the figures, §2; no student notes: skip §8). Nothing more: no content of your own (summaries, explanations, answers, checks), no files beyond those defined here, no next steps; the report (§11) is your only commentary. Use only the files provided.

## 1. Each file's role

Decide by content, not by name:

1. **Announcement**: a PDF printed from a mail client (`Subject:`, `Date:`, `From:`, then the teacher's message); its date is the `Date:` line, not the print timestamp.
2. **Page capture**: a `.txt` copied from a course-site page; starts with navigation (`Passer au contenu principal`, the week's title, its page list), then the page's own title; lists its attachments with their sizes in `ko`. A captured « Présentation de la semaine » is week-level, like an announcement.
3. **Slide deck**: title slide, « Plan » slide, one idea per slide, a footer with the course and the slide number.
4. **Exercise sheet, solution sheet**: solutions follow the exercises' numbering; one document may hold both, each question followed by its « Réponse ».
5. **Exam and key**: a practice or past exam and its solutions or grading criteria; treated like exercises and solutions.
6. **Quiz capture**: photos or screenshots of an online quiz, often overlapping.
7. **Student notes**: the student's own class notes, often after a slide number, with screenshots sometimes drawn on.
8. **Earlier output**: a `.md` this method produced (front matter with `sources`): update it, don't rebuild it.
9. **Other**: an assignment statement, a reading, code, an image.

## 2. Read everything, figures included

1. Read all inputs before writing anything.
2. **Read every PDF page as an image**, not only its text layer: figures often carry the data (signals, graphs, trees, tables, constellations, grids, photos of hand-drawn solutions), and the text layer drops or scrambles symbols and tables. Render the pages in a temporary directory outside the course folder (`pdftoppm -png -r 100 in.pdf <tmpdir>/page`), look at every page, zoom in on dense figures. When text and image disagree, the image wins.
3. **Read what a page shows but doesn't print**: hyperlink targets (`strings in.pdf | grep -o '/URI *([^)]*)'`), and formatting that carries meaning (answers in colour under a question, words in bold that the statement refers to).
4. **Quiz captures**: read every photo; merge overlapping shots into one transcription per question; collect each dropdown's options across the shots that show it open, in menu order; note what no shot shows. In an *Association*, every menu choice is used at least once.
5. Without page images, write `> ⚠ Figure non lue : <ce que la figure devait montrer, d'après le texte>` where a figure is missing, and say so in the report.
6. Read page captures to the end: previews ending in `...` usually repeat in full further down.

## 3. Group, merge, name

1. **A topic group** is a page capture plus the attachments it lists. Match each attachment to its page by content first, then declared size, then the folder it sits in. A misfiled file goes with its real topic, named after it, and the report says so; an inconclusive case keeps the folder's grouping, with the doubt reported.
2. **Outputs**: one file per topic page with its deck (page 1's also opens with the week-level items), one per topic's exercise and solution sheets (each exercise followed by its solution), one per other attachment; a standalone document (review exercises, an exam and its key, a quiz) is one file; an exam and its key, one file; a quiz, one file for all its captures. Each file's figures go in `<its name>-images/`. Student notes get no file of their own: they are folded into the others (§8). Names follow [[setting-up-new-material]] in a course folder; elsewhere, `<slug>.md` next to the original.
3. **Slugs**, from the document's title: lowercase ASCII, accents removed, words joined by hyphens, articles and prepositions dropped (le, la, les, l', un, une, de, du, des, d', à, au, aux, en, par, pour, avec, dans, sur, et), four words at most, plus a chapter or session marker when the title alone is generic.

## 4. Keep all substance, drop all noise

These rules apply to the official material; the student's notes follow §8.

**Keep** every definition, explanation, property, criterion, comparison, list, example, algorithm, formula, table, worked example and trace, and every datum a figure shows; every question in full, with data that exists only in a figure, every choice offered and every official solution; a document's header data (course, chapter, session, teacher, kind of work) as a short list; resource links with their label and URL; descriptions, guiding questions, learning objectives, summaries and the deck's own conclusion; lasting logistics (schedule, evaluations with their dates, format, duration, number of questions, points, attempts; deadlines, contacts); the teacher's notes and errata, next to what they concern; activities, one line each, except prompts that pose a course problem, kept in full.

**Drop** site navigation and interface text (`Passer au contenu principal`, page lists, `Dans cette page`, `Cliquer pour afficher le contenu`, `Cet hyperlien s'ouvrira dans un nouvel onglet.`, `Nombre de mots: 0`, `Module suivant`, file sizes, credits, truncated previews; in quiz captures `Sélectionnez une réponse`, browser chrome); document boilerplate (institution lines, logos, footers, page and slide numbers, the « Plan » slide, used instead to shape headings, `(1/2)` suffixes); repeats (slides that build a figure step by step: the most complete version once, the steps as a list only when they show a process; a fact stated in several files: once, in its fullest form); engagement-only content (polls, forum and self-introduction prompts, greetings, signatures).

Two levels of fidelity:

1. **Notes** (pages, slides, emails): rephrasing is allowed (prose to lists, tighter wording) as long as every fact, number, condition and example survives; fix obvious typos.
2. **Verbatim** (statements, choices, solutions, keys): word for word, typos and inconsistencies included (a statement that says « cinq » and lists six). Only the layout may change. Flag what looks wrong (§5); never fix it. A closing « Qu'en déduisez-vous ? » asks for the computation's conclusion: it is part of the question, not a separate one or a gap to flag.

## 5. Fidelity

1. Write in French; keep the English terms the sources use.
2. Use only the provided files: no outside knowledge, examples, explanations or corrections.
3. **Solutions: official content only**, their wording, values and order kept; the format may change (a drawn tree becomes a nested list). Never add steps, checks or answers of your own. No solution in the inputs: `Solution : non fournie.` Answers the student wrote are student notes (§8).
4. **Statement and solution stay apart**: everything that gives the answer away goes under the solution, even when the source interleaves it; say so in a `⚠ Signalement` when you move it.
5. Never change a technical claim, notation or value, even one that looks wrong.
6. Spell out each acronym at its first occurrence in each notes file, not inside verbatim text.
7. **Flag, don't fix**: contradictions between files, notes referring to something absent, unreadable passages, missing parts of a quiz capture, a question without a statement, a solution that visibly doesn't match its question. Put the flag where it applies, `> ⚠ Signalement : …`, and repeat it in the report.
8. No text of your own around the content: no introduction, summary, transition or citation marker.

## 6. Figures: crop, link, transcribe

Every figure is both **cropped and linked** (a reader or a vision-capable tutor sees the original) and **transcribed in text** (a text-only tutor gets every datum). What counts: every image of the source (raster pictures, vector drawings, charts, tables drawn as images, photos, screenshots), except branding and decoration, listed in the report.

1. **Cropping**, with file access: find the images (`pdfimages -list in.pdf`; a page showing a figure absent from the list holds a vector drawing); a raster figure with its text inside, extract it at native resolution (`pdfimages -png -f P -l P`); a vector figure, or one with labels printed over it, render the page at 200 dpi and crop the region (`pdftoppm -png -r 200 -f P -l P -x X -y Y -W W -H H`, or `sips -c`); in quiz photos, crop the figure itself, not the screen. Look at every crop: nothing cut off, nothing of a neighbour caught in it.
2. **One image per figure, split by role**: a statement's figure and a solution's are separate files, so a statement never reveals the answer; a composite figure whose parts are used separately, one file per part.
3. **Names**: `<question or section>-<enonce|solution>-<short description>.png`, zero-padded so files sort in document order (`q02-solution-1-tout-ou-rien.png`); in notes files, `<section or slide>-<short description>.png`.
4. **Link** each image where the figure stood, with a relative path and an alt text saying what it shows: `![Signal NRZ de la suite 1001100111](couche-physique-exercices-de-revision-images/q02-solution-2-nrz.png)`.
5. **Transcribe** right after the link, in the notation that makes its data complete: a table as a table; a graph, one line per node with its outgoing arcs in order and their labels (`- A → C (1), D (2)`), directed or not; a tree, a nested list, one node per line with what the figure attaches to it (`- B (MIN) : 3`), what it highlights in words or bold; a signal, a table with one row per bit or interval; a constellation or plot, the axes then each point; a board or grid, a `text` block plus a list of what it implies; a trace, a table, one row per step; text inside a figure, word for word; a regular structure, a compact exact description; a legend, restated in your notation; an unreadable part, `[illisible]`. Describe only what the figure shows; reading its meaning is the solution's job.

## 7. Markdown format

GitHub-flavoured Markdown: headings, lists, tables, code blocks, blockquotes, image links. No HTML, Mermaid or LaTeX. CriticMarkup only for the student's notes (§8).

**Front matter** at the top of every file:

```yaml
---
cours: <course code and title, as the sources give it>
chapitre: <…>            # or semaine: <N>, whichever the sources give; omit if neither
titre: <title; an exercises file: "<page title> — Exercices">
images: <name>-images/   # omit if no figures
sources:
  - <every original merged in: its path relative to the folder before archiving, or its name in a chat>
---
```

**A page file**: `# <page title>`, then `## Annonce de la semaine` (page 1 only: per announcement, its date, then one bullet per piece of information), the page's own sections in page order, `## Activités` (one line each, naming the exercises file), then the deck's Plan items as `##`, sub-topics as `###`.

**An exercises, exam or review file**: `# <title> — Exercices`, the header data as a short list, then per exercise `## Exercice 1 : <sujet en quelques mots>` (keeping the source's own label: « Question 1 », « Question #1 »), `### Énoncé` (the full statement, sub-questions numbered as in the source, statement figures linked and transcribed), `### Solution` (the official solution, same numbering, solution figures linked and transcribed without repeating the statement's data).

**A quiz file**: `# <quiz title>`, one line on what was transcribed (number of questions, points) and the types used, then per question, separated by `---`: `## Question 1`, `*<type>* · <points if they vary>`, the statement, the choices lettered A., B., … in screen order. Types: *Cases à cocher* (square boxes, several answers), *Choix unique* (round buttons), *Association* (a dropdown per item: a table `| Énoncé | Réponse |` with an empty answer column, then « Choix du menu déroulant : » and the options in menu order), *Réponse courte* (a free field). No answers: the student's own selections on a capture are student notes (§8).

Algorithms and pseudocode in `text` blocks, line structure kept. Formulas in plain Unicode (f(n) = g(n) + h(n), log₂ 4, α ≥ β, ∅); aligned calculations stay aligned, in a `text` block. Bold: key terms where defined, and what the source itself bolds in a statement.

## 8. Student notes

Skip if there are none. Otherwise fold every note into the finished official text; a note is one typed remark, one screenshot, or one mark drawn on a screenshot.

1. **Locate** the passage each note refers to: the slide number the student wrote (it refers to the original deck's PDF page; find where that slide's content landed, and check it matches); else the screenshot's content; else the context (notes follow the lecture's order; wording shared with the official text). A note may belong to any output of the run.
2. **Mark** it with CriticMarkup: a note that repeats official content (copied text, « important ! »), `{==passage==}`; one that adds something (an explanation, an example, a question, an answer, a correction, what a drawing adds), `{==most relevant words==}{>>the note<<}`; one that repeats and adds, `{==passage==}{>>only what it adds<<}`; one that matches no passage, `{>>the note<<}` alone at the start of the most relevant section.
3. **Tight marks**: highlight the words the note repeats, not the whole section.
4. **Screenshots**: only the differences from the official page are additions (handwriting, drawn strokes, added values, crossed-out parts, another version of the slide); ignore capture artifacts (cursor, player controls, webcam, window chrome). A mark that points at something highlights what it points at; one that adds content is described in words in the comment.
5. **Never change the official text**: a correction of the student's goes in a comment. Don't judge or check their notes.
6. **Their words and language**, typos fixed only when obvious; light reorganization when the student would clearly recognize it.
7. **Syntax**: one line per comment (lines joined with « ; »); never nested; never across two blocks; never in code blocks, front matter, headings or image links. CriticMarkup is only for the student's notes; your own flags stay `> ⚠ Signalement : …`.

## 9. Write or deliver

**With file access**: write each `.md` and its images folder where [[setting-up-new-material]] says; move every processed original, the student's notes included, to `archive/`, keeping its relative path; never delete or edit an original, never overwrite a file except to update an earlier output; quote paths (names may hold spaces, `!`, curly apostrophes, accents); temporary renders go in a scratch directory. A folder already processed: process only the files outside `archive/`, merging each into the matching `.md` or creating a new one.

**Without**: one downloadable file per `.md`, or each file's name on its own line, then its full content in a code fence of four backticks tagged `markdown`. No cropping: keep the text transcription of every figure, and replace its link by `> 🖼 Figure : <page and position in the original>`. Never truncate a file; if all won't fit, stop at a file boundary, say which files remain, and continue when asked.

**Files only Claude reads** (a slide-by-slide transcription, read again and again by later sessions) go in `claude-only/`, with `audience: Claude uniquement` in their front matter and a ⛔ banner first, saying the student doesn't read them. Everything else is written for the student.

## 10. Final check

1. Every original appears in the `sources` of at least one output.
2. Every slide's substance, every question with all its choices, and every official solution is present.
3. Every figure (but branding and decoration) has a crop, a link that resolves and a transcription; statement images reveal nothing of the solution; the transcriptions match the crops.
4. Every student note is highlighted or commented; every `{==` closes with `==}`, every `{>>` with `<<}`; no marks where they are forbidden.
5. No noise remains: `Passer au contenu`, `Cet hyperlien`, `Nombre de mots`, `Module suivant`, `Sélectionnez une réponse`, footers, page and slide numbers.
6. Every output is `.md`, in French (the student's notes keep their own words), with front matter.
7. With file access: the originals are in `archive/`; nothing was deleted or overwritten.

## 11. Report

Short, in English: files produced or updated, each with its sources and number of images; originals archived, or to archive by hand; **action items for the student first**, everything missing that they might supply (a question without a statement, a part no capture covers, an unreadable figure), each with what exactly is missing and where; then the flags (misfiled files, missing attachments, contradictions, moved answers, gaps in captures, unread figures and notes, images skipped as branding, judgment calls).

When something here caused friction or turned out wrong, propose the change in the report: [[improving-the-system]].
