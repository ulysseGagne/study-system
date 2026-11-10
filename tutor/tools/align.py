#!/usr/bin/env python3
"""Split a video's transcript by slide, for Claude.

Usage, with the venv's python (tools/.venv; numpy):
  <python> -I align.py <recordings folder> <video name> <chapter folder>
  e.g. align.py . s5-1-propositional-logic ../chapters/s5-1-propositional-logic

For videos that show the slide full-frame (4:3, centred). Every 2 s a frame is
shrunk to 64×48 grey and matched to the nearest slide PNG of the chapter (mean
absolute difference); runs shorter than 6 s are merged into their neighbour.
Each Whisper segment (.work/<video>.jsonl) goes to the slide on screen at its
midpoint. Output: by-slide/<video>-by-slide.md, one section per stretch of
slide, with its time range; a frame far from every slide is "other" (an
exercise sheet or a demo on screen).
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

W, H, STEP, MIN_RUN, FAR = 64, 48, 2.0, 6.0, 40.0


def grey(path, crop=None):
    vf = (crop + "," if crop else "") + f"scale={W}:{H},format=gray"
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-vf", vf, "-f", "rawvideo", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)


def hms(s):
    s = int(s)
    return f"{s // 3600}:{s // 60 % 60:02d}:{s % 60:02d}"


def main(rec, stem, chapter):
    rec, chapter = Path(rec).resolve(), Path(chapter).resolve()
    video = rec / "videos" / f"{stem}.mp4"
    slides = sorted((chapter / "slides").glob("[0-9][0-9]-*.png"))
    refs = np.stack([grey(p)[0] for p in slides])
    probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=width,height", "-of", "csv=p=0", str(video)], capture_output=True, text=True).stdout
    vw, vh = map(int, probe.strip().split(",")[:2])
    cw = min(vw, vh * 4 // 3)
    frames = grey(video, f"fps={1 / STEP},crop={cw}:{vh}:{(vw - cw) // 2}:0")
    d = np.abs(frames[:, None] - refs[None]).mean(axis=(2, 3))
    best, dist = d.argmin(1), d.min(1)
    labels = [slides[b].name[:2] if dist[k] < FAR else "other" for k, b in enumerate(best)]
    # runs, then merge the short ones into the previous run
    runs = []
    for k, lab in enumerate(labels):
        if runs and runs[-1][0] == lab:
            runs[-1][2] = (k + 1) * STEP
        else:
            runs.append([lab, k * STEP, (k + 1) * STEP])
    merged = []
    for r in runs:
        if merged and (r[2] - r[1] < MIN_RUN or merged[-1][0] == r[0]):
            merged[-1][2] = r[2]
        else:
            merged.append(r)
    lines = (rec / ".work" / f"{stem}.jsonl").read_text(encoding="utf-8").splitlines()
    segs = [json.loads(line) for line in lines if line.strip()]
    out = [f"---\nvideo: {stem}\nchapter: {chapter.name}\naudience: Claude only\n"
           f"method: align.py (the frame on screen every {STEP:.0f} s, nearest slide); "
           f"Whisper transcript, not proofread\n---\n"]
    for lab, a, b in merged:
        text = " ".join(s["t"].strip() for s in segs if a <= (s["s"] + s["e"]) / 2 < b)
        title = next((p.stem for p in slides if p.name[:2] == lab), lab)
        out.append(f"\n## {title} · {hms(a)}–{hms(b)}\n\n{text}\n")
    (rec / "by-slide").mkdir(exist_ok=True)
    (rec / "by-slide" / f"{stem}-by-slide.md").write_text("".join(out), encoding="utf-8")
    print(stem, " ".join(f"{lab}@{hms(a)}" for lab, a, b in merged))


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    main(*sys.argv[1:4])
