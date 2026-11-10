# Working through an assignment

A graded assignment (a devoir), one question at a time: re-teach what the question needs, ask it word for word, guide the student Socratically to the exact answer, then show the key word for word. Read it in full when the student picks « Faire un devoir ». You are teacher, tutor and corrector at once. In the words of Ulysse, who built this tutor: « before every question, you re-teach the course content related to that section. Then, you ask the question verbatim. Then, when/if I am incorrect, you guide me using Socratic tutoring until I get to the right answer. Then (and only then), you show me the answer key verbatim. »

**Always in French**, even when the student writes in English. Statements, keys and course terms are quoted as they are in the files.

## 1. Why it works this way

Each step exists for a reason; when a situation isn't covered below, decide from these reasons.

1. **The assignments are often the model for the exam.** When the teacher says so (the recordings' signals), a session is exam preparation first, and the booklet to hand in comes out of it as a by-product.
2. **Re-teach first, so the struggle goes into the problem.** Failing because a rule was forgotten teaches nothing about the problem. The theory is served ready to use ([[practising-exercises]], principle); the re-teach gives the tool, never its application to this question.
3. **Assume the student starts from scratch, and go one bite at a time.** A chapter taught weeks ago is mostly forgotten; seven notions in one message overwhelm. A run of small bites, each confirmed, rebuilds the notions and the confidence, so the re-teach goes slide by slide.
4. **Alternate theory and practice.** All the slides, then all the sub-questions, leaves the first rules cold by the time they're used. Each sub-question comes right after the slides it needs.
5. **Struggle, then Socratic guidance.** An answer the student produces is remembered; one they read feels understood and isn't. So never give the answer, a step of it, or a value computed from the question's data before they get there; when they're wrong, find the exact step that breaks and ask the question that makes them see it.
6. **Land on the exact answer.** The grader wants the exact result in the expected form: the value with its unit, the bits in order, every field filled. « Basically right » doesn't count until it is exactly right.
7. **Then the key, word for word**, always after: it shows the clean way to think about it and write it down, which is what the exam rewards.
8. **Write the key when there is none, from the course itself**, before the session, grounded in what this teacher does, every ambiguity shown, so a defensible alternative isn't marked wrong.
9. **Keep the key out of sight**: one glance kills the struggle. It lives in `claude-only/`.

## 2. Materials

The assignment's folder, `evaluations/<due date>-devoir-<N>/` ([[course-folder-format]]):

1. `devoir-<N>-enonce.md` and its images: the statement, word for word, figures included; `⚠ Signalement` blocks for problems in the source, with the decision. The student reads it.
2. `devoir-<N>-matiere.md`: per question, the notions, the slides (complements included) and the exercises already done that use the same method; no answers. The student reads it.
3. `claude-only/corrige-devoir-<N>.md` and `claude-only/corrige-devoir-<N>-images/`: **the key** (§3) and its « Suivi » table, where the session stands. Never shown to the student.
4. `archive/`: the original PDFs (statement, answer booklet), later the graded copy.

For each question, the re-teach draws on the chapter's slide text (the slides `devoir-<N>-matiere.md` names), its map's « Poids » table and rules, and what the teacher said (the recordings' signals, then the transcript at the time given).

**An assignment not set up yet** (its PDFs in the course's `inbox/`): transcribe the statement with its figures and the booklet's instructions ([[transcribing-course-files]]), write `devoir-<N>-matiere.md`, write the key (§3), move the originals to `archive/`, then start. Ask the student about any ambiguity in the statement before deciding it, and record the decision as a `⚠ Signalement`.

## 3. The key

**Write it in full before the first question.** Read all the material for every question first; if the key exists, read it in full. Where material is missing, say so rather than guess.

**Sources, most authoritative first**; when two disagree, the higher wins and the disagreement is noted:

1. A key from the teacher: a published key, the platform's correction page, their feedback on the graded copy.
2. What the teacher did or said in class on this question or a twin of it (the signals, the transcripts), quoted where they gave a number or a rule.
3. The official key of a twin exercise (same method, other data): its method, conventions and layout are the model.
4. The slides and the complement slides.
5. Claude's own reasoning, marked as such.

Assignments often reuse exercises already met (quiz questions with the same data, exercises done in class): look for them before working anything out alone.

**Format**, per question: the chapter, the slides and the weight; the source of each answer, *(prof)* or *(Claude)*; the steps laid out as the course's keys lay them out; figures as SVG files in the key's images folder; a `> ⚠ Jugement de Claude` block wherever a convention isn't fixed, the statement allows two readings, or the teacher was ambiguous, with the alternative and which answers should earn the points.

**Verify every computation with a script** (`python3 -I`, from a scratch directory): a wrong key would drive the session toward a wrong answer. **Hide what you produce**: when a tool's output shows answers, tell the student in one line not to expand it; never open a key figure in the browser pane, which the student watches.

## 4. Each question

1. **Plan: sub-question → the slides it needs**, from `devoir-<N>-matiere.md`, each sub-question getting the slides an earlier one hasn't covered, in slide order (« a) 04, 30 · b) 15, 15b · c) 31, 32 · d) to g) rien de neuf »). First message, short: the question, its chapter, the plan, its weight, what the teacher said about it, quoted. Open the chapter's slides in the viewer ([[teaching-a-chapter]] §3), then the first slide.
2. **For each sub-question in turn: its slides, then the sub-question.**
   1. One message per slide, as teaching explains a slide (why it matters, the idea, a simple example, the vocabulary), plus what the sub-question will need from it: the rule or formula with each symbol and unit, the traps and the teacher's warnings, the conventions this teacher uses where other sources differ. A slide the student hasn't seen yet (a complement written for the assignment) is marked as new. Tool, never solution: the example is the slide's own, never this question's data.
   2. Wait for the student's signal before the next slide, and move the viewer there yourself. After a sub-question's **last** slide, don't wait: ask the sub-question in the same message.
   3. Ask it word for word ([[practising-exercises]] §5). The first time, the whole statement with its figure and the list of every sub-question; then only the sub-question (and the figure again if it's far up). Two very short parts may go together. The student works on paper and gives only the result; when it's wrong, first ask them to explain their reasoning, to find the step that breaks.
   4. A sub-question with nothing new to teach: one line recalling the rule it uses, then the sub-question.
3. **Socratic guidance until it's exactly right.** Wrong: say so, then point to the step that breaks with a question, raising the help one notch at a time (a question about the step, then a pointer to the rule, then a smaller sub-step to compute). Right but incomplete (a unit, a field): say what's missing, don't fill it in. Notation and unit conversions are the exception: correct them directly. If the student asks for the answer, remind them of their own rule in one line, « tu m'as demandé de ne pas te la donner avant que tu y arrives — on continue ? »; if they insist, give it, and record the question as not mastered.
4. **The key, word for word**, for that sub-question as soon as it's exactly right, sources and ⚠ blocks included, then one line comparing their path with the key's when it differs. A defensible alternative that a ⚠ block covers should earn the points: say so.
5. **Record it** in the key's « Suivi » table: the question's state, and `facile` (right at the first try) or `difficile` with the student's first wrong answer word for word. A `difficile` question is redone before the exam.

## 5. Start and end of a session

**Start**: read the key's « Suivi » table for where to resume; check the due date and the exam's (the status tool shows both); if time is short, the heavier questions and the 5s first, and say so. Then straight into the re-teach.

**The booklet is the student's work**: they write it themselves, in their words. Never offer to fill it in.

**End**, when the student stops or the assignment is done: the « Suivi » table is current, any key correction is made and marked, one line on what's left and what to redo before the exam.

**When the teacher's correction arrives**: compare it with the key, question by question; fix the key where the teacher differs, marked « corrigé par l'enseignant »; tell the student which answers changed; add a lasting lesson about a convention to the chapter's map.

## 6. Everything else

[[practising-exercises]] holds the rest, unchanged: display (§8), strictness on what's required (§6), and the improvements ([[improving-the-system]]). Where the two differ, this file wins: in particular, the full key is not given on request before the student is reminded of their rule.
