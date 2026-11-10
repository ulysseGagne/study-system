#!/usr/bin/env python3
"""Transcribe a course's recordings, for Claude: videos/ into transcriptions/.

Usage, with the venv's python (tools/.venv):
  <python> -I transcrire.py <enregistrements folder>           every video without a transcript (order
                                                               below), then rescans, so videos added
                                                               during the run are picked up
  <python> -I transcrire.py <enregistrements folder> FILE...   these videos, in this order

A transcript has its video's name. Order: by name (dated videos: oldest first;
`sN-K-…`: by week, then by number), the weekly presentations (`sN-0-…`) last,
since they mostly repeat the rest. The folder's vocabulaire.txt, if any, primes
Whisper with the course's terms.

Crash-safe: each segment is appended to .work/<video>.jsonl as soon as it is
decoded, and a rerun resumes after the last saved one. transcriptions/<video>.md
is written once the whole video is done; its existence marks the video done.
"""
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
from faster_whisper import WhisperModel

MODEL = "large-v3-turbo"
SR = 16000
# A paragraph of the transcript closes after this many seconds, or at a pause this long.
PARAGRAPH_S, PAUSE_S = 45, 8


def order(video):
    m = re.match(r"s(\d+)-(\d+)", video.stem)
    week, n = (int(m[1]), int(m[2])) if m else (0, 1)
    return (n == 0, week, n, video.stem)


def hms(s):
    s = int(s)
    return f"{s // 3600}:{s // 60 % 60:02d}:{s % 60:02d}"


def load_audio(video):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video), "-vn", "-f", "s16le",
                          "-ac", "1", "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0


def saved_segments(jsonl):
    """The segments already saved; drops a last line cut short by a crash."""
    if not jsonl.exists():
        return []
    segs, lines = [], jsonl.read_text(encoding="utf-8").splitlines()
    for line in lines:
        try:
            segs.append(json.loads(line))
        except json.JSONDecodeError:
            break
    if len(segs) < len(lines):
        jsonl.write_text("".join(json.dumps(s, ensure_ascii=False) + "\n" for s in segs), encoding="utf-8")
    return segs


def render(video, segs, duration):
    """Paragraphs headed by their position in the video; ⟨? ?⟩ marks text Whisper itself doubts."""
    paras, cur, start, prev_end = [], [], 0.0, 0.0
    for s in segs:
        if cur and (s["s"] - start >= PARAGRAPH_S or s["s"] - prev_end >= PAUSE_S):
            paras.append(f"[{hms(start)}] " + " ".join(cur))
            cur = []
        if not cur:
            start = s["s"]
        text = s["t"].strip()
        cur.append(f"⟨?{text}?⟩" if s["lp"] < -1.0 or s["cr"] > 2.4 else text)
        prev_end = s["e"]
    if cur:
        paras.append(f"[{hms(start)}] " + " ".join(cur))
    head = (f"---\nvidéo: \"{video.name}\"\ndurée: \"{hms(duration)}\"\n"
            f"transcription: Whisper {MODEL}, automatique, non relue\naudience: Claude uniquement\n---\n\n")
    return head + "\n\n".join(paras) + "\n"


def transcribe(model, video, transcripts, work, prompt):
    out, jsonl = transcripts / f"{video.stem}.md", work / f"{video.stem}.jsonl"
    if out.exists():
        print(f"{video.name}: already transcribed", flush=True)
        return
    audio = load_audio(video)
    duration = len(audio) / SR
    segs = saved_segments(jsonl)
    offset = segs[-1]["e"] if segs else 0.0
    print(f"{video.name}: {'resuming at ' + hms(offset) if segs else 'starting'}, length {hms(duration)}", flush=True)
    if duration - offset > 1:
        t0, last_log = time.time(), offset
        # The prompt primes the first window only (condition_on_previous_text is off,
        # to avoid repetition loops over long recordings).
        pieces, _ = model.transcribe(audio[int(offset * SR):], language="fr", beam_size=5,
                                     vad_filter=True, condition_on_previous_text=False,
                                     initial_prompt=prompt or None)
        with jsonl.open("a", encoding="utf-8") as f:
            for p in pieces:
                s = {"s": round(p.start + offset, 2), "e": round(p.end + offset, 2), "t": p.text,
                     "lp": round(p.avg_logprob, 3), "cr": round(p.compression_ratio, 2),
                     "ns": round(p.no_speech_prob, 3)}
                f.write(json.dumps(s, ensure_ascii=False) + "\n")
                f.flush()
                os.fsync(f.fileno())
                segs.append(s)
                if s["e"] - last_log >= 300:
                    speed = (s["e"] - offset) / (time.time() - t0)
                    print(f"  {hms(s['e'])} / {hms(duration)} ({speed:.1f}x)", flush=True)
                    last_log = s["e"]
    out.write_text(render(video, segs, duration), encoding="utf-8")
    print(f"{video.name}: done -> transcriptions/{out.name}", flush=True)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    rec = Path(sys.argv[1]).resolve()
    videos_dir, transcripts, work = rec / "videos", rec / "transcriptions", rec / ".work"
    transcripts.mkdir(exist_ok=True)
    work.mkdir(exist_ok=True)
    vocab = rec / "vocabulaire.txt"
    prompt = vocab.read_text(encoding="utf-8").strip() if vocab.exists() else ""

    def pending():
        return sorted((v for v in videos_dir.glob("*.mp4") if not (transcripts / f"{v.stem}.md").exists()), key=order)

    explicit = [Path(a).resolve() for a in sys.argv[2:]]
    videos = explicit or pending()
    if not videos:
        print("nothing to transcribe", flush=True)
        return
    try:
        model = WhisperModel(MODEL, device="cpu", compute_type="int8", cpu_threads=8, local_files_only=True)
    except Exception:
        model = WhisperModel(MODEL, device="cpu", compute_type="int8", cpu_threads=8)
    while videos:
        transcribe(model, videos[0], transcripts, work, prompt)
        videos = videos[1:] if explicit else pending()
    print("all done", flush=True)


if __name__ == "__main__":
    main()
