"""Ajoute les infos d'un fichier brut (veille/brut/*.md) à la veille du jour.

Usage : python3 newsletter/app/merge_brut.py <veille.md> <brut.md> [--en-tete]
Lignes brutes acceptées : « [R|B|F] JJ/MM | Titre | Fait | URL ou aucun | Newsletter » (crochets facultatifs).
--en-tete : les nouvelles infos passent avant les anciennes (renumérotation). Sinon, ajout à la suite.
"""
import re, sys

veille, brut = sys.argv[1], sys.argv[2]
head = "--en-tete" in sys.argv
text = open(veille, encoding="utf-8").read()
lines = text.splitlines()

old = {"R": [], "B": [], "F": []}
for l in lines:
    m = re.match(r"^([RBF])\d+\. (.*)$", l)
    if m:
        old[m.group(1)].append(m.group(2))

seen = {re.sub(r"\W+", " ", re.match(r"\*\*(.+?)\*\*", r).group(1).lower()) for v in old.values() for r in v}
new = {"R": [], "B": [], "F": []}
for l in open(brut, encoding="utf-8"):
    m = re.match(r"^\[?([RBF])\]?\s*\|?\s*(\d\d/\d\d)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(\S+|aucun)\s*\|\s*(.+)$", l.strip())
    if not m:
        continue
    k, d, t, fait, url, src = m.groups()
    key = re.sub(r"\W+", " ", t.lower())
    if key in seen:
        continue
    seen.add(key)
    score = {"R": 7.5, "B": 7, "F": 7}[k] + (1 if ";" in src else 0)
    s = str(score).replace(".", ",").replace(",0", "")
    line = f"**🆕 {t}** — {s}/10 — 📅 {d} — {fait} — {src}"
    if url.startswith("http"):
        line += f" — [source]({url})"
    new[k].append(line)

for k in "RBF":
    new[k].sort(key=lambda x: -float(re.search(r"— ([\d,]+)/10", x).group(1).replace(",", ".")))
    old[k] = new[k] + old[k] if head else old[k] + new[k]

titles = {"R": "Rubrique — sujets longs", "B": "Lien en bref — infos croustillantes", "F": "Fun & actionnable"}
out, skip = [], False
for l in lines:
    m = re.match(r"^## (Rubrique|Lien en bref|Fun)", l)
    if m:
        k = {"Rubrique": "R", "Lien en bref": "B", "Fun": "F"}[m.group(1)]
        out.append(f"## {titles[k]} ({len(old[k])})")
        out += [f"{k}{i+1}. {r}" for i, r in enumerate(old[k])]
        skip = True
        continue
    if skip and re.match(r"^[RBF]\d+\. ", l):
        continue
    skip = False if l.startswith("## ") else skip
    out.append(l)
open(veille, "w", encoding="utf-8").write("\n".join(out) + "\n")
print({k: len(v) for k, v in new.items()}, "ajoutés")
