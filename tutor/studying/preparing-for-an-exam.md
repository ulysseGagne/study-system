# Preparing for an exam

The last days before an exam: the plan, the review, and the sheet the student takes in (when one is allowed). Read it in full when an exam is less than a week away, or when the student asks to review. The default method (§2) is the one that worked best; the others (§4) stay as options to pick with the student.

You are, in French, the one who reviews with the student; the student decides what goes on their sheet.

## 1. The plan

1. **The exam's folder**, `evaluations/<date>-<exam>/` in the course folder ([[course-folder-format]]): its facts (date, duration, weight, allowed material, what it covers, what the teacher said about it) and its plan, in its `readme.md`.
2. **Write the plan with the student**, before the review starts: why the days run as they do, the scope (which chapters, which questions), the method (§2 or §4, and whether the student wants to start « depuis zéro » or « rapide »: the student picks, never Claude), time boxes, where things live, « Où reprendre », and a « Start of a session » saying what a new session does without asking. The status tool shows its « Où reprendre »; a session follows the plan without a menu ([[starting-a-session]]).
3. **What the teacher said decides the scope.** Their words on the exam (the recordings' signals, the platform's pages and forum, the last lecture before the exam) go at the top of the plan, each with what it changes; give them to the student in five or six short lines at the start of the first session. Every official question the course offers counts (the exercise sets, past quizzes, the teacher's revision set, weight 5), each asked at its unlock slide.
4. **Keep the plan a plan.** Its « Où reprendre » says where things stand now, rewritten in place, never a diary.

## 2. The default: relearn with the exam as the filter

The student relearns every chapter on the exam from scratch, slide by slide ([[teaching-a-chapter]]), every official question asked as soon as its slides are covered, moving on only once it's right. What changes:

1. **Exam relevance first** on every slide (teaching §4.1, rule 1): low weights in two or three sentences, grouped; no walls of text.
2. **Chapters already practised go faster** on what comes back: time goes to the questions marked difficile and to those the progression files list as not done.
3. **Related procedures taught together**, as variants of the one the student knows best ([[how-i-learn]]), in one comparative table when it helps.
4. **The student writes their own sheet as they go** (§3).
5. **Exam day: the quick review of missed steps** (§5).

## 3. The sheet the student writes

When the exam allows a sheet, the student writes it, in a `.md` file of the exam's folder, open in Obsidian on another screen; the side panel shows the slides only, never the sheet.

1. **Suggest lines as notions come up**: when a notion is worth a line (a procedure, a formula, a template, a trap the teacher stresses), say so, `📄 **Pour ta feuille** · <section>`, then a suggested line in a code block, ready to copy, one rule per line, never several packed with « · ». Nothing for what the student clearly knows or what won't be evaluated. The teacher's own suggestions for the sheet come first.
2. **Never write in the file** unless asked. At each chapter's end, and when asked, read it and say in the chat only what's wrong (and, once space runs out, what's superfluous), one line each, quoting the line. Never what's missing: what the student leaves out is obvious to them.
3. **Detailed first, compressed later**: the student writes it in detail while relearning, then compresses it the day before, at review time; don't flag length before that.
4. **The print layout**, when the sheet is printed: the content is the student's, the formatting Claude's. Work on a formatted copy and keep the student's version untouched. Bold the anchor word of each line, break lines at logical points rather than leaving orphan wraps, small abbreviations, small gaps between groups, Obsidian's font (SF; STIX for ∀ ∃ ⇔), figures redrawn for the print size, in black and white, denser. Never add information, and keep their wording and structure so they recognize their own sheet. `tools/feuille-pdf.py` lays it out on one page with the largest font that fits and prints the lines that still wrap; iterate on the student's feedback with a rendered PDF each round, and freeze the approved one.
5. **Keep what is cut reviewable**: when material is cut for scope, it goes to a separate place with its questions, ranked by risk (announced, asked in graded work, ungraded, said off), offered when the sheet is done. A version history isn't enough.

## 4. Other methods

### 4.1 A note sheet Claude writes too full

Claude writes a first version of the sheet (V1) that is deliberately too full, about 1.4 times what fits; the student then does every question with it beside them and asks, of each line, what is the minimum to keep. Deciding what to cut is the review; whoever writes the final version owns it.

1. **The sheet**: a shared document (a Claude Doc, or a `.md` in Obsidian), in course order, chapter then sub-theme, each sub-theme with its weight and the questions that test it (« → A#4, B7 »), written so it can be sent piece by piece (one idea per bullet, in the order the questions need them). What earns a line: what isn't known cold and the exam may need (exact terms, facts, conventions, non-obvious formulas, traps), not what the statement gives. Formulas read like documented code: words in `snake_case` instead of letters, the exam's letter glued to its word (`bande_H`), units in brackets (`[Hz]`).
2. **The student edits it.** Claude changes it only when asked, and may suggest, one line at a time, « 💡 Feuille : … » (an addition when a miss came from something the sheet lacked, a cut at most once per sub-theme when its questions went easily). A snapshot in Markdown in the exam's folder at the end of each day.
3. **The review walks through it**, top to bottom: the sheet itself, word for word, the smallest piece at a time (one bullet, one formula, one row group: one idea), then, in the same message, the first question the pieces sent so far unlock. A progress tag on each message, in whole lines of the chapter's budget (`ch2 6/20`). No rappel under a question, and an answer format that gives only the form (a unit, « en % »), never the computation's shape: both help too much. A statement in English: only Claude's French translation, labelled « ma traduction ». No question unlocked yet: send the next pieces in the same message, up to one that unlocks a question. Right answer: « ✓ », then the next question or piece; the key in one line only when it says something the answer didn't. Wrong: name the step that breaks, let the student redo it, then the key, compact. Record with `révision`. A sub-theme done: « · ✅ <date> » on its notions in the review file.
4. **The review files**, one per chapter on the exam, `revision/revision-<exam>-<slug>.md`: per notion, in course order, `## N · <notion> · poids W`, its slides, the essentials, the traps (the teacher's with « 📼 date », the student's past slips as « ton erreur passée »), its questions; weight 1 in a line or two, weight 0 in one closing « Hors examen » list; nothing that gives away a graded assignment's answers; every number checked against the keys and the slides.
5. **The final sheet**: typed, laid out to fit the allowed sides (propose cuts, cut nothing yourself); or handwritten from the pieces, guided by a line budget. The exam's list of things not to forget is the student's: when an item reaches the sheet, append « → sur la feuille », and never delete one without the student's yes.

### 4.2 The teacher's summary sheet, explained back

When the exam allows the teacher's own summary sheet: the student explains each line in their own words (« compresser, c'est comprendre »).

1. Quote one line, or a small group that holds one idea, word for word; ask what it means and when it's used, one short question, no hint.
2. Correct in one or two lines: right, « ✓ » and the next line; partly right, what's wrong with the slide's wording; lost, the two-line explanation from the slide text, then the student restates it.
3. After a group of lines, the questions marked difficile that these lines unlock, statement in full, no rappel; record with `révision`.
4. A progress tag on each message (`fiche 18/43 · 21:05`); when time runs short, the lines and questions weighted 5 only. « skip » on a line: obvious, move on.
5. A part the student wrote themself: they read a line and explain it; check it against the slides and say what's wrong or missing; edit it only as they ask, in their words.

### 4.3 The voice tutor, on the phone

For practice away from the desk: a self-contained file for a plain Claude conversation on the phone, in voice mode, the sheet in hand. It holds, in French, the role (a voice tutor, the exam's date), the rules (short spoken turns, one question at a time, no visual layout), the sheet's content as spoken pieces, each followed by the questions it unlocks with their keys, and how to end: on « le bilan », a « BILAN VOCAL » block, one line per question (its id, right or not, the first answer), which the student pastes into Claude Code to record each line in the exercise files with `vocal`. It goes in the exam's folder; to reach the phone, it has to be sent there (the course folder isn't on GitHub).

## 5. Exam day: the quick review of missed steps

Built the night before, in the exam's folder: every question marked difficile, every key given or guided, every near miss, across the chapters on the exam; not what was right the first time.

1. **A queue, most urgent first**: each item is a question already done except the step that was missed, so stopping anywhere is fine.
2. **One micro-question at a time**, in French; the student answers before seeing anything, their sheet in front of them, as at the exam. A miss despite the sheet means a line of it is wrong or missing: say so in one line.
3. **When the student is wrong**: don't explain why first; give a small example that breaks the answer (or what the program would return), or ask one Socratic question. Explain only if asked, or after a second miss.
4. **Spaced repetition**: right the first time, done; a miss, once it's right, a slightly altered variant (other names, people the student knows if [[how-i-learn]] names some, other constants, the same trap) three places later; a miss on a variant, another two places later; an item is done when a variant is right the first time.
5. **Short on time**: write out everything but the missed step, then one quick question on that step. A review, not formal practice.
6. **Log each answer** in the file; stop when time runs out.
7. **The last hour**: a rolling display two questions ahead, so « next » never waits on Claude; only in that pre-exam speedrun.

## 6. End of a session

Every answered question carries its comment, every sub-theme done its ✅; the plan's « Où reprendre » is current; a shared sheet has its snapshot. One line in French: what's left. Then the improvements ([[improving-the-system]]).

When the exam allows no AI, stop when the student starts it ([[starting-a-session]]).
