#!/usr/bin/env python3
"""The slide server: the course folders at /, the tutor's pages at /tuteur/.

Usage: python3 -I serve.py [--port 8765] [--courses <repo>/courses]

The viewer of a chapter:
  http://localhost:8765/tuteur/viewer.html?chapitre=<course>/chapitres/<chapter>#<slide>
Listens on 127.0.0.1 only; never serves hidden files (.venv, .work…).
"""
import argparse
import http.server
import posixpath
import socketserver
import urllib.parse
from pathlib import Path

TOOLS = Path(__file__).resolve().parent


def handler(courses):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def translate_path(self, path):
            p = posixpath.normpath(urllib.parse.unquote(urllib.parse.urlsplit(path).path))
            root, rest = (TOOLS, p[len("/tuteur"):]) if p == "/tuteur" or p.startswith("/tuteur/") else (courses, p)
            parts = [x for x in rest.split("/") if x and x not in (".", "..")]
            if any(x.startswith(".") for x in parts):
                return str(TOOLS / "__hidden__")
            return str(root.joinpath(*parts))

        def end_headers(self):
            self.send_header("Cache-Control", "no-store")
            super().end_headers()

        def log_message(self, *args):
            pass

    return Handler


class Server(http.server.ThreadingHTTPServer):
    def server_bind(self):
        # HTTPServer looks up the host's name here, which can hang for seconds: skip it.
        socketserver.TCPServer.server_bind(self)
        self.server_name, self.server_port = "localhost", self.server_address[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--courses", default=str(TOOLS.parents[1] / "courses"))
    a = ap.parse_args()
    courses = Path(a.courses).expanduser().resolve()
    with Server(("127.0.0.1", a.port), handler(courses)) as server:
        print(f"http://localhost:{a.port}/tuteur/viewer.html?chapitre=<course>/chapitres/<chapter> · courses: {courses}",
              flush=True)
        server.serve_forever()


if __name__ == "__main__":
    main()
