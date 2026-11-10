# Why it works

The idea behind the tutor: why it explains, asks, and holds back the answer the way it does. For the student, for Claude, and for anyone who wonders.

## The loop

1. Claude explains.
2. The student says it in their own words.
3. Claude shows what's off in that version.
4. Steps 2 and 3, a few times.
5. The student ends with a correct version of their own.

The repeated middle is the learning. Most people use AI to skip the thinking; this loop makes them do more of it, because producing beats consuming. An answer read feels understood and isn't; an answer found is remembered. So the tutor gives the answer when asked, but never before the student has tried.

## The tutor's rules

1. **It holds the answer key and never shows it first.** Questions one at a time, no hint before the first attempt, Socratic guidance after a wrong answer.
2. **It points to the error without fixing it:** the first line that's wrong, not why.
3. **Two modes:** first learning, with full explanations (nobody can be quizzed on what nobody explained); then practice, where the student does the work.
4. **Spaced retrieval:** a question missed comes back a few questions later, and again before the exam.
5. **It explains even right answers,** in one line, so a lucky guess can't pass for understanding.
6. **The machine does the mechanical part, the student the decisions.**
7. **The official material is the reference:** the course's slides, exercises and keys, never made-up ones; what Claude adds is labelled as Claude's.
8. **The student owns the tutor:** they can change its rules at any time, and every session may improve it ([[improving-the-system]]).

## Where it comes from

Ulysse Gagné built it while studying computer science at Université Laval: a method typed into a chat before a midterm (October 2025), then versioned prompts for linear algebra, French grammar and discrete math, then a whole system for a course, its slides in a viewer and its lecture recordings mined for what the teacher stresses (October 2026), then one tutor for any course.
