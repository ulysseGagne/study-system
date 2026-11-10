# Starting a study session

How a study session starts, whatever its activity: which course, where it stands, what's waiting, what to do. Follow it as soon as the student wants to study a course (« on étudie IFT-2006 », « salut »), once the welcome is done ([[welcome]]).

## 1. The course and its state

1. **Which course.** From the student's words; otherwise list the course folders in `courses/` (those with a `chapitres/` folder) and ask. One course per session; its folder is « the course folder » in every file of the tutor ([[course-folder-format]]).
2. **Read its `readme.md`**: what the course is and its conventions (notation, units, weights, tools, AI rules), which hold all session.
3. **Its status**, in a few seconds, before saying anything:

   ```bash
   python3 -I tutor/tools/status.py courses/<course>
   ```

   Per chapter: its « Où reprendre », per exercise file the comments and the hard ones, its inbox. Then the course's inbox, the recordings (transcribed, analysed, a transcription running or stopped), the evaluations to come with their plan's « Où reprendre », and the time.

## 2. What's waiting, then what to do

1. **Say first what's waiting**, whatever the student's first message is (even « salut »), one line per item: files in an `inbox/`, recordings not transcribed or not analysed, a stopped transcription, restarted at once ([[lecture-recordings]]). Nothing waiting: say so in one line, and offer to check the course platform for news (new files, forum answers, quiz corrections; the built-in browser, the student logs in).
2. **One new piece of the system, at most.** When a piece in the last section of [[welcome]] has its moment now and `where-to-resume.md` doesn't list it as shown, offer it in one or two lines, then list it there.
3. **An evaluation plan in force** (an evaluation to come whose `readme.md` says to follow it from its « Start of a session »): follow it, after one line on where the day stands against its time boxes. No menu.
4. **Otherwise ask what to do**, in French, in one short message (the multiple-choice tool if there is one: one question for the chapter, one for the activity), with one status line per chapter, e.g. « Ch. 2 Couche physique : enseignement terminé · exercices : 51 faites, 18 difficiles ». Recommend the chapter in progress; with an exam less than a week away, recommend « Réviser pour l'examen » and skip the chapter question. A chapter not set up yet only offers « Ajouter du matériel ». The activities:
   1. **Apprendre la matière**, the first pass on a chapter: [[teaching-a-chapter]].
   2. **Pratiquer les exercices**, once a chapter is taught, or only the hard ones: [[practising-exercises]].
   3. **Réviser pour l'examen**, an exam less than a week away: [[preparing-for-an-exam]].
   4. **Faire un devoir**, a graded assignment, not tied to a chapter: [[working-through-an-assignment]]. A devoir due and not finished always takes a slot.
   5. **Ajouter ou mettre à jour du matériel**, files in an inbox or a recording to process: [[setting-up-new-material]], [[lecture-recordings]].
   6. **Voir ma progression**: §3 below.
   7. **Autre chose**: help directly.

   The tool takes four options at most, « Autre chose » being its free text: offer the four that fit best. If the first message already says what to do (« on continue la matière »), skip the question, or the part already answered.
5. **Read the chosen file in full**, then the chapter's map, and follow the file from its start.

## 3. Progress overview (« Voir ma progression »)

A report in the chat, in French, read-only:

1. **The next exam**: its date, the days left, what it covers.
2. **One line per chapter**, in course order: on the exam or not; taught (sections done of total); exercises (done of total, how many hard); reviewed (notions ✅ of total, if the exam has review files); waiting in its inbox.
3. **What's left before the exam**, most urgent first, five lines at most: chapters on the exam not set up, then not taught, then hard questions not redone since, then chapters taught but never practised.
4. One line on anything stale or uncertain to act on.

Count from the files, never from memory; a missing source shows « — ». Then ask what to do next.

## 4. Rules for every session

1. **Graded work without AI.** When the course's rules forbid AI on an evaluation (its readme says which), and the student starts it: wish them luck and stop. Never answer, check or discuss its questions before it is submitted.
2. **Paths in messages** relative to the working folder (the repo's root, when the session was opened there), so a click opens them; never wrapped in `<…>`, which breaks the link.
3. **Where it runs.** The Code tab of the Claude desktop app, opened in the repo's folder: everything works (the slide viewer in the browser pane, results written in the files). In a plain chat, only practice works: attach the course's `readme.md`, [[practising-exercises]], [[how-i-learn]], and the chapter's map, slide text and exercise files; results come at the end, to paste in by hand.
4. **Saving.** The course folder has no git: write results as you go. The tutor's files and [[how-i-learn]] are in the repo's git: commit your own changes, never push ([[improving-the-system]]).
