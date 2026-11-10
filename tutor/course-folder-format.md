# Course folder format

The contract between the tutor and a course: what a course folder holds, where, and how its files are written. Read it before setting up material or changing a course folder's layout; the other files of the tutor assume it.

## What a course folder is

1. **The course's data, nothing else.** The material (slides, exercises, recordings), what the tutor knows about it (maps, slide texts, the teacher's signals) and where the student stands (progress, results, exam plans and sheets). What stops mattering once the course is over. What is the student's own lives elsewhere: the method in the tutor, how they learn in [[how-i-learn]].
2. **It never names the tutor's files.** A course folder describes itself (its `readme.md` files) so that another tutor could study it; the tutor never names a course. The tutor's roles may appear in it (« the teacher », « the tutor »), never a prompt, a tool or a path into the tutor.
3. **On this Mac only.** `courses/<code>-<name>/` (`ift-2006-teleinformatique`), out of git (the repo's `.gitignore`), with no git of its own.

## Layout

```text
<course>/
├── readme.md            what the course is, its conventions, what is in the folder
├── chapitres/           one folder per chapter or slide deck, in course order
│   ├── readme.md        the chapters, one line each
│   └── <chapter>/       ch2-couche-physique, s5-1-logique-propositions…
│       ├── readme.md
│       ├── claude-only/ carte-<slug>.md, diapositives-<slug>.md, progression-<slug>.md
│       ├── diapositives/ NN-<description>.png, NNa-complement-<description>.png, diapositives.json, complements-sources/
│       ├── exercices/   <slug>-<what>.md and <slug>-<what>-images/
│       ├── inbox/       new material waiting for setup
│       └── archive/     the originals
├── evaluations/         one folder per evaluation, named by its date
│   └── AAAA-MM-JJ-<what>/   readme.md (its plan, if any), its facts, sheets, review files, claude-only/, archive/
├── enregistrements/     readme.md, signaux-<course>.md, vocabulaire.txt, videos/, transcriptions/, par-diapo/, .work/
├── inbox/               new material not yet sorted into a chapter
└── archive/
```

A course may add what it needs (`brio/`, a teacher's summary sheet, emails), each with its own `readme.md`.

## Names

1. **The house style**: kebab-case, no accents, no version numbers, a name that says what the file is.
2. **Every `.md` name unique in the repo**, so `[[name]]` links work: build them from the chapter's slug (`carte-couche-physique.md`, `couche-physique-questionnaire-brio.md`) or the course (`signaux-teleinformatique.md`). A slug that would collide with another course's gets the course's name added.
3. **Evaluations are dated** by the evaluation (the due date, for an assignment): `2026-10-17-examen-intra/`.
4. **Recordings** keep a name that sorts: the lecture's date (`2026-10-01-jeudi.mp4`) or the course's own numbering (`s5-1-logique-propositions.mp4`); a transcript has the video's name.
5. **A `readme.md` in every folder**, first why the folder exists, then what is in it, one line each. Exceptions: `inbox/`, `archive/`, a figure folder named after its file (`<file>-images/`), `complements-sources/`, and the fixed parts of a chapter, an evaluation or the recordings, which their parent's readme describes.

## The chapter's files

1. **The map**, `claude-only/carte-<slug>.md`, read first by the tutor, and wins over the tutor for that chapter. Its sections: 1. Goal (the evaluations, the learning objectives, where points are lost, the « Poids » table); 2. Materials (paths and counts, the total of official questions, who wrote each key, which exercise file is part A, B, C…, the slides dropped and where they went, the complements, the agenda and photo-only slides, slide errors); 3. Rules (flags, conventions, answer formats, open questions, shared data, debatable keys with their 📼 slide); 4. Sections, one per teaching session; 5. Unlock map: after which slide each question becomes answerable, the last slide it needs; 6. Exercise map: per question, the notions and slides behind its rappel, and its answer format.
2. **The slide text**, `claude-only/diapositives-<slug>.md`: a note on why it exists (a slide read as an image costs about 2,000 tokens, its text about 150), an index (slide · title · questions it feeds), then one section per slide: image link, the text, « Figure : » descriptions, « Ce que dit le prof » with its 📼 time when the course has recordings, « Questions : », « Notes des tuteurs : » (append-only, `- AAAA-MM-JJ · <type> · <note>`).
3. **The progression**, `claude-only/progression-<slug>.md`: « Où reprendre » (read by the status tool), the sections and their state, a session log.
4. **The slides**: one PNG per slide at 150 dpi, `NN-<description>.png`, slide number = PDF page; Claude's complements `NNa-complement-<description>.png`, their HTML in `complements-sources/`. `diapositives.json` lists them in viewer order: `{"titre": …, "diapositives": [{"id": "15a", "file": …, "title": …, "kind": "officielle" | "complement"}]}`. Exercise slides leave the deck; the numbering keeps the gap.
5. **The official questions**, `exercices/`: each file verbatim ([[transcribing-course-files]]), `### Énoncé` then `### Solution` (official) or `### Corrigé (…)` saying whose key it is; figures in `<file>-images/`, statement and solution figures apart; problems in `> ⚠ Signalement` blocks with the decision taken.
6. **`claude-only/`** is never shown to the student, except the student's notes in the slide text.

## Results and notes

1. **A question answered** is recorded where its answer stands: the `**Réponse : …**` line of a `### Corrigé`, or the first line of a `### Solution` (an item's line for a multi-item question), highlighted with a comment after any earlier one:

   ```markdown
   {==**Réponse : A** (10 Gbits/s)==}{>>2026-10-02 · tuteur · difficile · 2 essais · a d'abord répondu « 66.4 » : appliquait Shannon seul<<}
   ```

   Fields: date · who (`enseignant`, `tuteur`, `révision`, `vocal`) · `facile` (right at the first try, without help) or `difficile` · tries · what went wrong, the first answer word for word (« du premier coup » when facile). Never edit or delete a comment; change nothing else in the file. The status tool counts `{>>` and `· difficile ·`.
2. **A note of the student's** goes in the slide text, at the slide concerned: `{==<line>==}{>>AAAA-MM-JJ · note de l'étudiant · <the note>…<<}`; what is Claude's, not the course's, is marked « (Claude) ».

## Weights

Each map's « Poids » table weighs the notions from what the teacher said, with its source (📼 recording and time, or a forum answer):

1. **5**, announced: the teacher said it, or that kind of question, will be evaluated.
2. **4**, important: stressed, a trap warned about, worked in class, or an official question asks it.
3. **3**, normal: taught, no signal either way.
4. **2**, minor: never raised, no question asks it.
5. **1**, light: understand it, don't memorize it (« culture générale », given in the statement).
6. **0**, off the evaluations: the teacher said so.

« jugement de Claude » marks a weight or a decision Claude drew without a clear signal. The course's `readme.md` gives its defaults and the teacher's own signal words.

## Evaluations and recordings

1. **An evaluation's folder** holds what concerns it only: its facts (date, rules, what it covers, what the teacher said about it), its plan in `readme.md` when it has one (why, scope, time boxes, « Où reprendre »), the sheets, the review files, a key in `claude-only/`, the originals in `archive/`.
2. **`enregistrements/`**: `signaux-<course>.md`, the teacher's signals, one `## ` section per recording analysed, each line `[h:mm:ss] · where · kind · what was said`; `vocabulaire.txt`, the terms that prime Whisper; the videos, their raw transcripts and, for slide narrations, the transcripts cut by slide ([[lecture-recordings]]).
