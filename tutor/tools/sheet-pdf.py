"""An exam sheet in Markdown -> one letter page, one side (HTML, PDF and a PNG preview, next to it).

Usage: python3 -I sheet-pdf.py <sheet.md> [--pt 8.5]
Renders the .md as Obsidian does (a line break = a line; a blank line = a small gap), in three
columns, in Obsidian's font. Without --pt, the font is the largest (in steps of 0.1 pt) whose PDF
fits on one page. `<file.svg>` alone on a line inserts the drawing; `<file.png>`, the image.
Then prints the lines that still wrap in their column, to fix the breaks. Used for IFT-2003's
midterm sheet (October 2026); the method: preparing-for-an-exam.md, §3.
"""
import html, json, re, subprocess, sys
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
args = sys.argv[1:]
fixed = float(args.pop(args.index("--pt") + 1)) if "--pt" in args else None
args = [a for a in args if a != "--pt"]
if not args:
    sys.exit(__doc__)
src = Path(args[0]).resolve()
out = src.with_suffix("")


def inline(s):
    s = html.escape(s.rstrip(), quote=False)
    s = s.replace("\\\\", "\x00").replace("\\*", "\x01").replace("\\_", "\x02")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w])_(.+?)_(?![\w])", r"<i>\1</i>", s)
    return s.replace("\x00", "\\").replace("\x01", "*").replace("\x02", "_")


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


lines = src.read_text(encoding="utf-8").split("\n")
body, blk, i = [], [], 0


def flush():
    if blk:
        body.append('<div class="blk">' + "".join(blk) + "</div>")
        blk.clear()


while i < len(lines):
    ln = lines[i]
    if ln.startswith("### "):
        flush()
        body.append(f"<h3>{inline(ln[4:])}</h3>")
    elif not ln.strip():
        flush()
    elif ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-|:]+\|$", lines[i + 1].strip()):
        head = cells(ln)
        rows = []
        i += 2
        while i < len(lines) and lines[i].startswith("|"):
            rows.append(cells(lines[i]))
            i += 1
        t = "<tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr>"
        t += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
        blk.append(f"<table>{t}</table>")
        continue
    elif m := re.fullmatch(r"\s*<([\w\-]+\.svg)>\s*", ln):
        blk.append(f'<div class="fig">{(src.parent / m[1]).read_text(encoding="utf-8")}</div>')
    elif m := re.fullmatch(r"\s*<([\w\-]+\.png)>\s*", ln):
        blk.append(f'<img src="{(src.parent / m[1]).as_uri()}">')
    else:
        tabs = len(ln) - len(ln.lstrip("\t"))
        sub = " sub" if re.fullmatch(r"\*\*[^*]+\*\*", ln) and ln == ln.upper() and not ln.endswith(":**") else ""  # **SUBTITLE**
        blk.append(f'<div class="l{sub}" style="padding-left:{tabs * 1.2}em">{inline(ln.lstrip(chr(9)))}</div>')
    i += 1
flush()

CSS = """
@font-face { font-family: "Symbols"; src: url("file:///System/Library/Fonts/Supplemental/STIXTwoMath.otf"), local("STIX Two Math"); unicode-range: U+2200, U+2203, U+2209, U+21D4; }
@page { size: letter; margin: 0.25in; }
@media screen { .page { width: 8in; } }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing: border-box; }
html, body { margin: 0; background: #fff; color: #000; }
.page { columns: 3; column-gap: 0.12in; column-rule: 0.4pt solid #aaa; column-fill: auto;
  font-family: "Symbols", ui-sans-serif, -apple-system, BlinkMacSystemFont, system-ui, sans-serif; line-height: 1.2;
  letter-spacing: -0.01em; }
b { font-weight: 600; }
h3 { font-size: 1em; font-weight: 600; background: #000; color: #fff; margin: 3pt 0 1.5pt;
  padding: 0.5pt 3pt; break-after: avoid; }
h3:first-child { margin-top: 0; }
.blk { break-inside: avoid; margin-bottom: 3.5pt; }
.l { text-indent: -1em; margin-left: 1em; }
.sub { border-bottom: 0.5pt solid #000; margin-bottom: 1pt; }
.fig { margin: 1pt 0 2pt; }
.fig svg { display: block; }
table { border-collapse: collapse; width: 100%; font-size: 1em; }
th, td { border: 0.4pt solid #777; padding: 0.4pt 1.5pt; vertical-align: top; text-align: left; }
img { width: 100%; display: block; }
"""

# the wraps report: for each line that wraps, its number of lines and how full its last one is
REPORT = """<script>
const rep = [];
for (const el of document.querySelectorAll('.l, h3')) {
  const r = document.createRange(); r.selectNodeContents(el);
  const rows = {};
  for (const q of r.getClientRects()) {
    const k = Math.round(q.top), o = rows[k] || [1e9, -1e9];
    rows[k] = [Math.min(q.left, o[0]), Math.max(q.right, o[1])];
  }
  const ks = Object.keys(rows).map(Number).sort((a, b) => a - b);
  if (ks.length > 1) {
    const w = el.getBoundingClientRect().width, last = rows[ks[ks.length - 1]];
    rep.push([ks.length, Math.round(100 * (last[1] - last[0]) / w), el.textContent]);
  }
}
const pre = document.createElement('pre'); pre.id = 'rep'; pre.textContent = JSON.stringify(rep);
document.body.append(pre);
</script>"""

out_html, out_pdf = out.with_suffix(".html"), Path(f"{out}.pdf")
chrome = [CHROME, "--headless", "--disable-gpu", "--allow-file-access-from-files", "--no-pdf-header-footer"]


def page(pt, script=""):
    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>{html.escape(src.stem)}</title><style>{CSS}</style></head>
<body><div class="page" style="font-size:{pt}pt">{"".join(body)}</div>{script}</body></html>"""


def render(pt):
    out_html.write_text(page(pt), encoding="utf-8")
    subprocess.run(chrome + [f"--print-to-pdf={out_pdf}", out_html.as_uri()], check=True, capture_output=True)
    return len(re.findall(rb"/Type\s*/Page\b", out_pdf.read_bytes()))


if fixed:
    pt, n = fixed, render(fixed)
else:  # a binary search on a 0.1 pt grid
    lo, hi = 50, 110
    while lo < hi:
        mid = (lo + hi + 1) // 2
        lo, hi = (mid, hi) if render(mid / 10) == 1 else (lo, mid - 1)
    pt = lo / 10
    n = render(pt)
subprocess.run(["qlmanage", "-t", "-s", "1700", "-o", str(src.parent), str(out_pdf)], check=True, capture_output=True)
Path(f"{out_pdf}.png").replace(f"{out}-preview.png")
print(f"{pt} pt · {n} page(s)")

tmp = out.with_name(out.name + "-report.html")
tmp.write_text(page(pt, REPORT), encoding="utf-8")
dom = subprocess.run(chrome + ["--window-size=900,900", "--dump-dom", tmp.as_uri()], capture_output=True, text=True).stdout
tmp.unlink()
for nl, fill, txt in json.loads(html.unescape(re.search(r'<pre id="rep">(.*?)</pre>', dom, re.S)[1])):
    print(f"  {nl} lines, the last {fill:3d}% full · {txt[:70]}")
