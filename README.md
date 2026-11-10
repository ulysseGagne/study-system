# Study system

A Socratic tutor for your own courses, in Claude Code. It teaches your course's slides one at a time, then has you do the official exercises, and never gives you the answer before you've tried: you find it yourself, so you remember it. Tell it what bugs you, and it rewrites its own instructions.

Built by [Ulysse Gagné](https://ulyssegagne.com) to study at Université Laval; it works with any course that has slides and exercises.

## Start

You need a Mac, the Claude app and a paid Claude plan. In the app, open the Code tab, choose a folder, and paste:

```
Clone https://github.com/ulysseGagne/study-system into this folder, then read study-system/CLAUDE.md and follow it. It's my first time: guide me one step at a time.
```

Your Claude takes it from there. Setting up a course uses a good part of your Claude usage; studying uses much less.

## What's in here

- `CLAUDE.md`: where your Claude starts.
- `tutor/`: the method, one file per job, and its tools; why it works: `tutor/why-it-works.md`.
- `how-i-learn.md`: how you like to learn; your tutor fills it in as you go.
- `where-to-resume.md`: what's in progress.
- `courses/`: your courses, made as you add them, kept on your Mac (it's in `.gitignore`).
