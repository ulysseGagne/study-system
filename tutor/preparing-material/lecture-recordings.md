# Lecture recordings

How the tutor learns what the teacher said: download a recording, transcribe it, cut it by slide, and mine it for the teacher's signals, which become the weights in each chapter's map and the « Ce que dit le prof » of each slide. Read it when a recording waits to be processed, or a transcription has stopped.

## Why

Few students rewatch their lectures, and nobody reads a transcript. But the slides give every notion the same weight, and the teacher doesn't. In class or on video, the teacher says what will be evaluated and how, what to know well, what not to memorize, how they count (conventions, their own solutions), where an exam stops. These cues are scattered across hours of audio. Mined once, they reach every session through the files the tutor already reads: **a signal left in the signals file alone never reaches the student.**

## 1. Download

1. **Into the course's `enregistrements/videos/`**, named so it sorts ([[course-folder-format]]): the lecture's date (`2026-10-13-mardi.mp4`), or the course's own numbering (`s7-1-langage-prolog.mp4`; `sN-0-presentation-semaine.mp4` for a weekly presentation).
2. **From the course platform, in the built-in browser** (the student logs in if asked). Never `curl` a video's address: the file server answers 403 outside the browser's session. Never open a video's address in the browser either: it plays the sound.
   1. **A Zoom recording linked from a Brio page**: take the `ulaval.zoom.us/rec/share/…` link with `javascript_tool` (`find` misses its text) and open it; no passcode was asked so far, and if one is, the student types it, never Claude. There is no download button or Zoom transcript. In the recording's page, fetch the video and save it (it lands in `~/Downloads`; move it into `videos/`):

      ```js
      window.__dl = {got: 0}; (async () => { const r = await fetch(document.querySelector('video').currentSrc, {credentials: 'include'}); const rd = r.body.getReader(), parts = []; for (;;) { const {done, value} = await rd.read(); if (done) break; parts.push(value); window.__dl.got += value.length; } window.__dl.url = URL.createObjectURL(new Blob(parts, {type: 'video/mp4'})); })(); 'started'
      // poll window.__dl.got until window.__dl.url is set, then:
      const a = document.createElement('a'); a.href = window.__dl.url; a.download = '2026-10-13-mardi.mp4'; document.body.appendChild(a); a.click();
      ```

   2. **A file hosted on Brio** (a video, a PDF): a video's address is its poster image's (`…/fichiers/<id>/contenu?jeton=…&format=IMAGE_APERCU_VIDEO&grandeur=360p`) with `format=VIDEO&grandeur=720p`; a PDF's is its link. Since Nov 2026 such an address redirects to a signed `pr.cloudfront.brioeducation.ca` address that refuses the fetch above (CORS). What works (2026-11-09): open one PDF's address in the pane, so the tab sits on the CloudFront origin; from there, load each address in a hidden iframe (`allow="autoplay 'none'"`, its video muted and paused as soon as it appears) and read the iframe's `location.href`: the signed address, valid about an hour, which `curl` downloads straight into the folder. A gallery's third video gets its poster only once shown: click the gallery's next button first. A hidden pane slows timers: run the loop in the background and poll its result.

## 2. Transcribe

`tools/transcrire.py` turns every video of `videos/` without a transcript into `transcriptions/<name>.md`: faster-whisper, model large-v3-turbo (cached in `~/.cache/huggingface`), in French, int8 on the processor, beam 5, silences filtered out, about 2 to 3 times faster than real time on an Apple-silicon Mac (half an hour for an 80-minute lecture). The first time, set up the venv (about 200 MB; the model, 1.6 GB, downloads on the first run): `python3 -m venv tutor/tools/.venv && tutor/tools/.venv/bin/pip install faster-whisper numpy`. The course's `enregistrements/vocabulaire.txt` primes it with the course's terms. It is crash-safe: every segment is saved in `.work/<name>.jsonl` as soon as it's decoded, and a rerun resumes after the last one; a transcript's existence marks its video done. Weekly presentations go last.

Start it detached, so it survives the session and keeps the Mac awake; the same command restarts it after a crash, a reboot or a dead battery:

```bash
cd <repo>/courses/<course>/enregistrements && mkdir -p .work && nohup caffeinate -is nice -n 10 <repo>/tutor/tools/.venv/bin/python -I <repo>/tutor/tools/transcrire.py . >> .work/transcription.log 2>&1 &
```

Progress: `.work/transcription.log`; running or not: `pgrep -f transcrire.py`. The Mac must stay plugged in; a closed lid only pauses it.

**Reliability**: the transcripts are raw Whisper output, never proofread. Fluent text can still be wrong, numbers, names and symbols above all (« 2509 » for the 1509 on screen, « optés » for « octets », « Morgane » for De Morgan), with high confidence; `⟨? … ?⟩` marks a passage Whisper itself doubts. Check any number or « ça » that matters against a frame of the video at that moment:

```bash
ffmpeg -v error -ss <seconds> -i "videos/<name>.mp4" -frames:v 1 -vf scale=1280:-1 .work/frame.jpg
```

## 3. Cut a slide narration by slide

When a video narrates a deck full-screen (one video per deck), `tools/aligner.py` matches a frame every 2 seconds against the deck's slides and puts each transcript segment under the slide on screen: `par-diapo/<name>-par-diapo.md`, one section per stretch of slide with its time range, « autre » when no slide matches (an exercise sheet on screen). About 30 seconds per video:

```bash
cd <repo>/courses/<course>/enregistrements && <repo>/tutor/tools/.venv/bin/python -I <repo>/tutor/tools/aligner.py . <video name> ../chapitres/<chapter>
```

Condensed, it becomes each slide's « Ce que dit le prof » in the slide text, with its 📼 time: how the teacher explains it, their examples, what the slide omits.

## 4. Mine the signals

One recording at a time, as transcripts arrive: first a keyword pass for recall (`grep -n -i` on the words below), then a full read for what keywords miss, and a frame for every number or « ça » that matters. What to look for:

1. **Evaluation content**: « à l'examen », « à l'intra », « on va vous demander », the kinds of questions, « dans l'énoncé on va vous donner… ».
2. **Emphasis**: « important », « retenez », « très important », « attention », « c'est classique », a trap or a common mistake, something said several times, a long time on one slide, an example worked out.
3. **De-emphasis**: « pas besoin de l'apprendre par cœur », « pour votre culture », « on ne vous demandera pas », « on ne va pas vraiment s'en servir », « je passe vite », skipped slides.
4. **Conventions and corrections**: how the teacher counts or computes, where they contradict a slide.
5. **Their solutions to exercises**, compared with the keys in the exercise files: where the teacher solved a question differently, their version is what will be graded.
6. **Logistics**: format, duration, number of questions, allowed material, grading.
7. **Scope**: where an exam stops, what's left for the final.
8. **Open questions**: the debatable keys a recording was expected to settle (each map's 📼 notes).

Out of scope: notions mentioned on no slide and in no official question, since they won't be evaluated; but keep anything that changes the answer to an evaluation-type question (a convention, a correction of a slide, the teacher's method or solution).

## 5. Where the results go

Right after each recording, before the next:

1. **Every signal** in `signaux-<course>.md`, one `## ` section per recording, each line `[h:mm:ss] · where (chapter, slide) · kind · a short quote` ([[course-folder-format]]); a recording without its section isn't analysed yet.
2. **The weights**: each concerned map's « Poids » table, a notion added, raised or lowered with its 📼 source, a « jugement de Claude » settled when the recording clears it up; the same notion in an exam's review files, if any.
3. **What concerns an evaluation** (format, rules, question types, scope): its facts file in `evaluations/`.
4. **A debatable key settled**, or a solution of the teacher's that differs: the question's `⚠ Signalement` (its decision updated) and the map's rules.
5. **A change of scope** (a chapter split differently): only after asking the student.

**Weighting rules**: the scale is in [[course-folder-format]]; each course's `readme.md` gives its defaults and its teacher's signal words. A notion the teacher never raises and no official question asks is less relevant (a grain of salt: teachers improvise). Official questions are a strong signal, often the strongest. When unsure, decide, write the weight with « jugement de Claude » and its source, and don't wait for the student: the tutor brings it up when the student reaches that notion.
