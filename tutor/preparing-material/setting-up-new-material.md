# Setting up new material

Turning raw course material into a course folder the tutor can teach from: transcribe, crop, export, fill the gaps, write the chapter's map, check every link. Read it in full when an inbox holds files, or when the student brings a new chapter, a quiz correction or a new course. The layout to reach: [[course-folder-format]]; the transcription rules: [[transcribing-course-files]]; recordings: [[lecture-recordings]].

## 0. Before anything

1. **Start from the inboxes.** New material arrives in a chapter's `inbox/`, or the course's for what isn't sorted yet: the student drops it there (a slide deck, an exercise sheet, quiz photos, a key, notes) and asks you to process it. Setting up is done when the inbox is empty: every file transcribed or exported into the chapter's layout, then moved to the chapter's `archive/`. Files outside an inbox are processed already: touch them only to merge new material in (a key that arrives for a quiz already transcribed). List every inbox, say which hold files, and process the one the student names, or ask.
2. **A note in an inbox** (`LISEZ-MOI-…`, `A-FAIRE-…`) is context from the student or an earlier Claude: how the material was split, which questions belong here, which slides to keep. Read it first, follow it, archive it with the rest.
3. **A new chapter** is a new folder in `chapitres/` (sub-parts `chN-M-<slug>/`) with an `inbox/`; the student may create it with the material already inside. **A new course** is a new course folder with its `readme.md` written with the student (what the course is, its platform, its conventions, its AI rules).
4. **Read everything first.** List every file; open each one (PDF text and page images, photos, existing `.md`); note what is a deck, an exercise sheet, a solution sheet, a quiz capture, a note. A `.rtfd` is one file (its `TXT.rtf` and images); read `.rtf` with `textutil -convert txt` (macOS) or `pandoc -f rtf -t markdown` (Linux).
5. **A correction page copied as `.rtf`** marks the right boxes of a *Cases à cocher* only by colour (a green marker before each right choice), which `textutil`, `pandoc` and plain text drop: parse the RTF itself (its `\colortbl`, the `\cfN` colour changes, the choices after a green marker), and check the result against the score.
6. **Tools.** `pdftoppm`, `pdftotext` and `pdfimages` come with poppler: `brew install poppler` when Homebrew is there; otherwise PyMuPDF in `tutor/tools/.venv` (`pip install pymupdf`) renders the pages and reads their text. macOS → Linux (a cloud session): `sips` → ImageMagick `convert` (it reads HEIC); `textutil` → `pandoc`; Chrome → the headless Chromium in `/opt/pw-browsers/`. `pdftoppm`, `pdftotext`, `pdfimages` and `strings` are the same.
7. **The course platform** (Brio at Laval; the course's `readme.md` gives its address): the student logs in to the built-in browser. Read-only: never post, submit, or open an evaluation's attempt, which may start its timer. A week page is a list of items (`.p-element-liste-selectionnable__lien`), each opening a page with an « Activité d'information » (the deck, the video) and an « Activité de mise en pratique » (exercises, solutions). Download what the inbox lacks, with the student's yes.
8. **The pedagogy behind the tutor**: [[why-it-works]]. It explains *why* the tutor works as it does: intuition first, one simple example, the problem before the solution, explain → reformulate → correct, fast feedback, no hint before the first attempt, mastery before moving on, spaced re-asking.
9. **Ask before building.** Clarifying questions, pushback and suggestions come before the first file, each with a recommendation, so « go with your recs » is a valid answer; unless the student said to run without them.
10. **The student studies from this.** So every gap is an action item for them, flagged, never silently skipped or reconstructed: a question with no statement, a part no photo covers, an answer that can't be settled. They can often fix it.
11. **Ambiguities: ask, decide, flag.** When the material is ambiguous or two sources disagree, do all three: ask the student for context; decide the most sensible option and write it, with its reason, in a `> ⚠ Signalement` next to the question (never leave the choice open); the map lists the flag. When the student answers, record the answer in the flag.
12. **Standing rules**: never write from the student's point of view; never invent questions; what Claude creates (keys, complements, examples) is labelled as Claude's, non officiel; course content in French, the tutor's files in English.

## 1. The exercises and quizzes

[[transcribing-course-files]] says how; here, where and what:

1. **Into `exercices/`**, one file per source of official questions, named `<slug>-<what>.md`: `<slug>-exercices-de-revision.md` (a review exercise sheet), `<slug>-questionnaire-brio.md` (the platform's quiz), `<slug>-exercices.md` (the teacher's exercise set), `<slug>-exercices-en-classe.md`… Its figures in `<its name>-images/`. Number the questions as the source does, prefixed by the part's letter when the chapter has several parts (A#3, B16, C#13), or by the teacher's own label (E2 #4).
2. **Statement and solution kept apart.** When the source prints answers inside the statement, move them under the solution and add a `> ⚠ Signalement`. A question with no statement stays « Énoncé : non fourni », flagged, an action item; reconstructed only if the student asks, from the answers that exist, labelled « Énoncé reconstitué par Claude, non officiel », with the reasoning.
3. **Photos of a quiz screen**: convert, read every shot, merge overlapping ones, mark what no photo covers (`[…]`) and ask the student for the missing shot; don't guess how many items are missing.
4. **Check every answer you can**: recompute every number, every truth table, every trace by script; run every program in the course's language (Prolog in `swipl`); flag any disagreement with the key.
5. **The teacher's answers on the forum** about an exercise go under it.
6. **The originals** to the chapter's `archive/`, a quiz's photos in a subfolder.

## 2. The slides

1. **One PNG per slide**, 150 dpi: `pdftoppm -png -r 150 deck.pdf <tmp>/s`. Name each `NN-<description>.png`, from the slide's own text (`pdftotext -layout -f N -l N`), not just its title.
2. **Exercise slides leave the deck**: the deck holds the course content only. A slide whose content is an exercise is not exported: its question must be in an exercise file (match the data, not just the number); what the slide adds (a worked answer, a drawn diagram) goes under that question's solution, as `<file>-images/qNN-solution-diapo-NN-<description>.png`, linked with « (diapo NN du cours) »; a slide that adds nothing is just dropped (the PDF keeps it). The other slides keep their numbers, so slide number = PDF page still holds; the map lists the slides dropped and where each went. A slide mixing course content and an exercise stays, with a ⛔ line in the slide text pointing to the question; a question the slide asks and answers as part of the lesson is course content.
3. **`diapositives.json`**, the slide list in viewer order, complements included ([[course-folder-format]]): the viewer reads it.

## 3. The missing keys

1. **A correction page from the platform is an official key**: transcribe its answers as `### Corrigé (page de correction Brio)` with a `**Réponse : …**` line, say at the top of the file that the key is the platform's, and say so in the map. Where it doesn't settle an answer (a question scored 0 whose right answer it doesn't show), mark it `> ⚠` and make it an action item.
2. **A quiz with no official key**: a `### Corrigé (rédigé par Claude, non officiel)` block under each question (the answer, the computation in a `text` block, the slides it relies on), and one line at the top saying the key is Claude's. Ground it in what was seen in class: the course's formulas, conventions and examples; where the course is silent, the standard result, pointing to a complement slide (§4). Recompute every number by script. Before marking an answer debatable, look for what settles it (a figure on a slide, the course's textbook, an earlier exercise with a key); mark with `> ⚠` only what stays open, with the alternative and the decision, and a 📼 note naming the slide whose recording would settle it.

## 4. Complement slides

Some questions need content the slides don't give; it may be on the exam, so it gets slides, not a footnote.

1. **Gap analysis**: for every question, the notions it needs and the slide that gives each; what has no slide is a gap. Group the gaps by the official slide they extend.
2. **One complement per group**, `NNa-complement-<description>.png`, sorting right after slide NN; **after every notion it uses**: after the **last** official slide whose notions it uses. A group mixing notions from slides far apart is split, one complement per place. Check each against the slides before it: no term a later slide introduces.
3. **The course's look** (its colours, fonts and slide size), clearly marked: a « COMPLÉMENT · non officiel » tag and a footer « Complément rédigé par Claude — hors diapositives officielles · complète la diapo NN ». No university logo.
4. **Content**: the rule or formula, what each symbol means, why it matters, references to the official slides, and a worked example labelled « Exemple (Claude) » with numbers different from the questions', so it teaches without giving an answer away.
5. **Units under every formula**, in small italics: each variable, its meaning and its unit (« λ : longueur d'onde (m) · c : vitesse de la lumière (m/s) »); « sans unité » where none; example values with their units. **One formula per line**, set apart from the text; a derivation one step per line, aligned on `=` or `⇒`; never two formulas, or a formula and its consequence, on one line.
6. **Render** each from HTML in `diapositives/complements-sources/` with headless Chrome (`--headless=new --hide-scrollbars --window-size=<slide size> --screenshot=out.png file:///…`); on Linux, list `Carlito` after Calibri. Look at every render: nothing cut or overflowing.
7. Point the key and the map's exercise map to the complements.

## 5. The slide text

`claude-only/diapositives-<slug>.md` ([[course-folder-format]]). Why it exists, in tokens: a slide read as an image costs about 1,500 to 2,500 tokens, its text about 150, paid again in every session; the transcription is paid once, here. Write that reason at the top of the file. Make it unmistakable that the student doesn't read it: the `claude-only/` folder, `audience: Claude uniquement` in the front matter, a ⛔ banner as the first line. Read every slide with a figure as an image (downscaled, `sips -Z 1000`): the text layer misses figures. Per slide: the image link, the faithful text, « Figure : » descriptions, « Ce que dit le prof » condensed from its recording cut by slide, with its 📼 time ([[lecture-recordings]]), « Questions : » (from the question → slides map, computed by script), « Notes des tuteurs : » (append-only). A slide error or a departure from standard usage: « ⚠ Note Claude », with the decision.

## 6. The map and the progression

1. **The map**, `claude-only/carte-<slug>.md`, with the sections [[course-folder-format]] lists: everything the tutor needs to know about this chapter, and nothing about another. Model it on an existing chapter's map. Its « Poids » table comes from the recordings' signals ([[lecture-recordings]]) and the official questions. The unlock map is computed by script from the question → slides map, every question checked present. A chapter split into parts says why, which part this is, whether it's on the next exam, and what it borrows from the others.
2. **The progression**, `claude-only/progression-<slug>.md`: « Où reprendre : section 1, diapo 01 », the sections, an empty session log.
3. **The readmes**: the chapter's, and its line in `chapitres/readme.md` (slides, complements, questions per part).
4. **A rule for every course goes in the tutor**, never in a copy: say so in the report ([[improving-the-system]]).

## 7. Check

1. Every link in every `.md` resolves (script it: extract `](…)`, test each path from the file's folder).
2. The inbox is empty; every original is in the chapter's `archive/`; nothing was deleted or overwritten without being read first.
3. Every figure has a cropped file, a link and a transcription; no statement image reveals a solution.
4. Every computed answer was recomputed by script; every debatable one carries a ⚠.
5. Every new `.md` name is unique in the repo.

## 8. Report

Short, in the student's language. **Action items first**: everything missing or unsettled that the student could supply or check, each with what exactly is needed and, for an ambiguity, the decision taken meanwhile. Then: what came in and where it went, files created or changed, other flags, decisions taken on the student's behalf, open questions.

## 9. A long setup

A whole course in one night, run while the student sleeps: keep a status file current in the course folder (what's done, in progress, next) so any Claude can resume, and save after each step. Usage is shared with the next day's study: run parallel agents only for what must be ready in the morning (on the night of Oct 18–19, three parallel agents used up the five-hour window in an hour and a half), keep the rest for after the deadline, and schedule a nudge that resumes the work after a usage-limit stop. Delete the status file once the setup is done: it is not a log.
