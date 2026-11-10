#!/usr/bin/env python3
"""Where a course stands, for Claude to read before it says anything to the student.

Usage: python3 -I status.py <course folder> [--today AAAA-MM-JJ]

Per chapter: its title, its progression's « Où reprendre », per exercise file the
questions done (lines holding a `{>>` comment) and the hard ones (`· difficile ·`),
its inbox. Then the course's inbox, the recordings (videos, transcripts, analysed:
the `## ` sections of the signals file), the evaluations to come with their plan's
« Où reprendre » and review progress, and the time. Read-only. The layout it reads:
course-folder-format.md.
"""
import argparse
import datetime
import json
import re
import subprocess
from pathlib import Path

DAYS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre",
          "octobre", "novembre", "décembre"]


def ou_reprendre(md):
    """The non-blank lines between « ## Où reprendre » and the next « ## » heading."""
    out, inside = [], False
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            if inside:
                break
            inside = line[3:].strip().lower().startswith("où reprendre")
            continue
        if inside and line.strip():
            out.append(line.rstrip())
    return out


def waiting(folder):
    files = sorted(p.name for p in folder.iterdir() if not p.name.startswith(".")) if folder.is_dir() else []
    return f"inbox : {len(files)} à traiter ({' '.join(files)})" if files else None


def count_lines(text, needle):
    return sum(needle in line for line in text.splitlines())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("course")
    ap.add_argument("--today")
    a = ap.parse_args()
    course = Path(a.course).expanduser().resolve()
    today = a.today or datetime.date.today().isoformat()

    chapters = course / "chapitres"
    if not chapters.is_dir():
        print("== pas encore de chapitres")
    for ch in sorted(p for p in chapters.iterdir() if p.is_dir()) if chapters.is_dir() else []:
        slides = ch / "diapositives" / "diapositives.json"
        title = json.loads(slides.read_text(encoding="utf-8"))["titre"] if slides.exists() else None
        print(f"== {ch.name}" + (f" — {title}" if title else ""))
        prog = next(iter(sorted((ch / "claude-only").glob("progression-*.md"))), None) if (ch / "claude-only").is_dir() else None
        inbox = waiting(ch / "inbox")
        if not prog:
            print("pas encore mis en place" + (f" · {inbox}" if inbox else ""))
            continue
        for line in ou_reprendre(prog):
            print(line)
        for ex in sorted((ch / "exercices").glob("*.md")):
            text = ex.read_text(encoding="utf-8")
            print(f"{ex.name} : {count_lines(text, '{>>')} faites, {count_lines(text, '· difficile ·')} difficiles")
        if inbox:
            print(inbox)

    inbox = waiting(course / "inbox")
    if inbox:
        print(f"== {inbox} (à la racine du cours)")

    rec = course / "enregistrements"
    if rec.is_dir():
        v = len(list((rec / "videos").glob("*.mp4")))
        t = len(list((rec / "transcriptions").glob("*.md")))
        m = sum(sum(line.startswith("## ") for line in s.read_text(encoding="utf-8").splitlines())
                for s in rec.glob("signaux-*.md"))
        running = subprocess.run(["pgrep", "-f", "transcrire.py"], capture_output=True).returncode == 0
        state = ", transcription en cours" if running else (
            " · transcription arrêtée : la relancer" if t < v else "")
        print(f"== enregistrements : {t} transcrits sur {v} vidéos, {m} analysés{state}")

    for ev in sorted(p for p in (course / "evaluations").glob("*") if p.is_dir()):
        if ev.name[:10] < today:
            continue
        print(f"== évaluation à venir : {ev.name}")
        readme = ev / "readme.md"
        if readme.exists():
            for line in ou_reprendre(readme)[:3]:
                print(line)
        reviews = sorted((ev / "revision").glob("*.md")) if (ev / "revision").is_dir() else []
        if reviews:
            parts = []
            for r in reviews:
                text = r.read_text(encoding="utf-8")
                done = len(re.findall(r"^## .*✅", text, re.M))
                total = len(re.findall(r"^## .*poids", text, re.M))
                parts.append(f"{r.stem} {done}/{total}")
            print("révision, notions faites : " + " · ".join(parts))

    now = datetime.datetime.now()
    print(f"== maintenant : {DAYS[now.weekday()]} {now.day} {MONTHS[now.month - 1]} {now:%H:%M}")


if __name__ == "__main__":
    main()
