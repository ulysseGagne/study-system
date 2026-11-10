# Improving the system

How the tutor changes during use. Ulysse built it to study, one remark at a time; this copy is the student's now: they use it, Claude maintains it, and every session may improve it. Their feedback is welcome, and it is how the tutor gets better. Read it whenever a rule causes friction, the student corrects one, or a change is approved.

## The loop

1. **Notice.** Something in a file causes friction, is missing, or turns out wrong: the student corrects a rule, asks for the same thing twice, a rule doesn't fit a case, a tool fails.
2. **Suggest it in one line**, at a natural break (between slides, after a key, never in the middle of an explanation or a question): « 💡 Prompt : <change> — <why> ».
3. **Apply it as soon as the student agrees**, or asks for a change themselves: edit the right file at once, in place, at the right section, in as few words as the rule needs, with no date or request tag. Don't hold it for the end of the session, and don't make a new version of the file.
4. **Never silently**: say in one line what changed and where.

Without file access (a plain chat), collect the changes, present them with their reasons at the end, and wait for approval.

## Where a rule goes

Said once, as high as it applies, so an improvement made on one course reaches the others:

1. **A rule for every course**: the tutor's file it belongs to ([[starting-a-session]], [[teaching-a-chapter]], [[practising-exercises]], [[preparing-for-an-exam]], [[working-through-an-assignment]], [[setting-up-new-material]], [[transcribing-course-files]], [[lecture-recordings]]).
2. **How a course folder is laid out or written**: [[course-folder-format]].
3. **A fact about how the student learns**, true in any course: [[how-i-learn]].
4. **A rule for one course** (its teacher's conventions, its notation, its tools): that course's `readme.md`.
5. **A rule for one chapter** (a slide, a question, a convention): the chapter's map.
6. **A rule for one evaluation**: its plan, the `readme.md` of its folder.

A course folder never names the tutor's files; the tutor never names a course, except as an example.

## Keeping it good

1. **Every session gets its context from the files**: nothing important lives only in a chat.
2. **No bloat**: every line is read again and again, and tokens cost money and time. Rewrite in place; move out what is no longer true.
3. **No duplication**: each fact in one place, linked from elsewhere.
4. **Navigable**: plain folders and `.md` files the student can browse, in Finder or in Obsidian.
5. **Saving**: the tutor's files and [[how-i-learn]] are in the repo's git: after a change, commit your own files, and never push (the repo came from Ulysse's GitHub; this copy is the student's). A course folder has no git: write its results as you go.
