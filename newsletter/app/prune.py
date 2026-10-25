"""Retire d'une veille les sujets publiés avant une date (JJ/MM) et renumérote.

Usage : python3 newsletter/app/prune.py <veille.md> JJ/MM
"""
import re, sys

path, limit = sys.argv[1], sys.argv[2]
d0, m0 = map(int, limit.split("/"))
lines = open(path, encoding="utf-8").read().splitlines()
out, n, removed = [], {"R": 0, "B": 0, "F": 0}, 0
for l in lines:
    m = re.match(r"^([RBF])\d+\. (.*)$", l)
    if m:
        d = re.search(r"📅 (\d\d)/(\d\d)", m.group(2))
        if d and (int(d.group(2)), int(d.group(1))) < (m0, d0):
            removed += 1
            continue
        n[m.group(1)] += 1
        out.append(f"{m.group(1)}{n[m.group(1)]}. {m.group(2)}")
    else:
        out.append(l)
keys = {"Rubrique": "R", "Lien en bref": "B", "Fun": "F"}
out = [re.sub(r"\(\d+\)$", f"({n[keys[h.group(1)]]})", l) if (h := re.match(r"^## (Rubrique|Lien en bref|Fun)", l)) else l for l in out]
open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"{removed} sujets retirés, restent {n}")
