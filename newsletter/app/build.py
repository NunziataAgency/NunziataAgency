"""Génère la page mobile de choix des sujets à partir d'une veille.

Usage : python3 newsletter/app/build.py [newsletter/veille/AAAA-MM-JJ.md]
Sans argument, prend la veille la plus récente. Écrit newsletter/app/veille.html.
"""
import glob, html, json, os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1] if len(sys.argv) > 1 else sorted(glob.glob(os.path.join(here, "..", "veille", "2*.md")))[-1]
text = open(src, encoding="utf-8").read()

title = re.search(r"^# (.+)$", text, re.M).group(1)
items = []
for m in re.finditer(r"^([RB])(\d+)\. \*\*(.+?)\*\* — ([\d,]+)/10 — (.+)$", text, re.M):
    kind, num, head, score, rest = m.groups()
    url = re.search(r"\[source\]\((.+?)\)", rest)
    rest = re.sub(r"\s*—?\s*\[source\]\(.+?\)", "", rest).strip(" —")
    items.append({"id": f"{kind}{num}", "kind": kind, "title": head,
                  "score": float(score.replace(",", ".")), "body": rest,
                  "url": url.group(1) if url else ""})

tpl = open(os.path.join(here, "template.html"), encoding="utf-8").read()
out = tpl.replace("__TITLE__", html.escape(title)).replace("__DATA__", json.dumps(items, ensure_ascii=False))
open(os.path.join(here, "veille.html"), "w", encoding="utf-8").write(out)
print(f"{len(items)} sujets → newsletter/app/veille.html")
