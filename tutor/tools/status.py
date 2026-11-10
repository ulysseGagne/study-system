#!/usr/bin/env python3
"""Where a course stands, for Claude to read before it says anything to the student.

Usage: python3 -I status.py <course folder> [--today YYYY-MM-DD]

Per chapter: its title, its progress file's "Where to resume", per exercise file the
questions done (lines holding a `{>>` comment) and the hard ones (`· hard ·`),
its inbox. Then the course's inbox, the recordings (videos, transcripts, analysed:
the `## ` sections of the signals file), the evaluations to come with their plan's
"Where to resume" and review progress, and the time. Read-only. The layout it reads:
course-folder-format.md.
"""
import argparse
import datetime
import json
import re
import subprocess
from pathlib import Path


def where_to_resume(md):
    """The non-blank lines between "## Where to resume" and the next "## " heading."""
    out, inside = [], False
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            if inside:
                break
            inside = line[3:].strip().lower().startswith("where to resume")
            continue
        if inside and line.strip():
            out.append(line.rstrip())
    return out


def waiting(folder):
    files = sorted(p.name for p in folder.iterdir() if not p.name.startswith(".")) if folder.is_dir() else []
    return f"inbox: {len(files)} to process ({' '.join(files)})" if files else None


def count_lines(text, needle):
    return sum(needle in line for line in text.splitlines())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("course")
    ap.add_argument("--today")
    a = ap.parse_args()
    course = Path(a.course).expanduser().resolve()
    today = a.today or datetime.date.today().isoformat()

    chapters = course / "chapters"
    if not chapters.is_dir():
        print("== no chapters yet")
    for ch in sorted(p for p in chapters.iterdir() if p.is_dir()) if chapters.is_dir() else []:
        slides = ch / "slides" / "slides.json"
        title = json.loads(slides.read_text(encoding="utf-8"))["title"] if slides.exists() else None
        print(f"== {ch.name}" + (f" — {title}" if title else ""))
        progress = next(iter(sorted((ch / "claude-only").glob("progress-*.md"))), None) if (ch / "claude-only").is_dir() else None
        inbox = waiting(ch / "inbox")
        if not progress:
            print("not set up yet" + (f" · {inbox}" if inbox else ""))
            continue
        for line in where_to_resume(progress):
            print(line)
        for ex in sorted((ch / "exercises").glob("*.md")):
            text = ex.read_text(encoding="utf-8")
            print(f"{ex.name}: {count_lines(text, '{>>')} done, {count_lines(text, '· hard ·')} hard")
        if inbox:
            print(inbox)

    inbox = waiting(course / "inbox")
    if inbox:
        print(f"== {inbox} (at the course's root)")

    rec = course / "recordings"
    if rec.is_dir():
        v = len(list((rec / "videos").glob("*.mp4")))
        t = len(list((rec / "transcripts").glob("*.md")))
        m = sum(sum(line.startswith("## ") for line in s.read_text(encoding="utf-8").splitlines())
                for s in rec.glob("signals-*.md"))
        running = subprocess.run(["pgrep", "-f", "transcribe.py"], capture_output=True).returncode == 0
        state = ", transcription running" if running else (
            " · transcription stopped: restart it" if t < v else "")
        print(f"== recordings: {t} of {v} videos transcribed, {m} analysed{state}")

    for ev in sorted(p for p in (course / "evaluations").glob("*") if p.is_dir()):
        if ev.name[:10] < today:
            continue
        print(f"== evaluation to come: {ev.name}")
        readme = ev / "readme.md"
        if readme.exists():
            for line in where_to_resume(readme)[:3]:
                print(line)
        reviews = sorted((ev / "review").glob("*.md")) if (ev / "review").is_dir() else []
        if reviews:
            parts = []
            for r in reviews:
                text = r.read_text(encoding="utf-8")
                done = len(re.findall(r"^## .*✅", text, re.M))
                total = len(re.findall(r"^## .*weight", text, re.M))
                parts.append(f"{r.stem} {done}/{total}")
            print("review, notions done: " + " · ".join(parts))

    now = datetime.datetime.now()
    print(f"== now: {now:%A}, {now:%B} {now.day}, {now:%H:%M}")


if __name__ == "__main__":
    main()
