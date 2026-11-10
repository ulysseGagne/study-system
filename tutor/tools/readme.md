# Tools

The tutor's scripts and pages, run on a course folder given as an argument; none names a course. Python scripts run with `python3 -I`; those that need faster-whisper or numpy, with the venv beside them.

1. `status.py`: where a course stands (chapters, exercises done and hard, inboxes, recordings, evaluations and dates to come): [[starting-a-session]].
2. `serve.py`: the slide server, the course folders at `/` and these pages at `/tuteur/`, on 127.0.0.1:8765 (the repo's `.claude/launch.json` starts it as `diapositives`).
3. `viewer.html`: the slide viewer of every chapter, `/tuteur/viewer.html?chapitre=<course>/chapitres/<chapter>#<slide>`: [[teaching-a-chapter]].
4. `transcrire.py`: transcribes a course's recordings with Whisper: [[lecture-recordings]].
5. `aligner.py`: cuts a slide narration's transcript by slide: [[lecture-recordings]].
6. `feuille-pdf.py`: lays an exam sheet out on one page, the largest font that fits: [[preparing-for-an-exam]].
7. `feuille-de-notes.html`: lays a note sheet out on letter pages in the browser, `?md=<path of the sheet>`: [[preparing-for-an-exam]].
8. `.venv/`: the Python packages the tools need, made the first time one is needed and out of git: `python3 -m venv tutor/tools/.venv && tutor/tools/.venv/bin/pip install faster-whisper numpy` for the recordings, `pymupdf` for PDFs on a Mac without poppler. The Whisper model is cached in `~/.cache/huggingface`.
