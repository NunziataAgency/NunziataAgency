#!/usr/bin/env python3
"""Retire les sujets en double (même type, même titre) d'une veille, en gardant le premier.
Usage : python3 newsletter/app/dedup.py <veille.md>  (puis prune.py pour renuméroter)"""
import re, sys
p = sys.argv[1]; t = open(p, encoding="utf-8").read().split("\n")
seen, out, n = set(), [], 0
for l in t:
    m = re.match(r"([RBF])\d+\. \*\*(?:🆕 |🍿 )?([^*]+)\*\*", l)
    if m:
        key = (m.group(1), re.sub(r"\W+", " ", m.group(2).lower()).strip())
        if key in seen:
            n += 1; continue
        seen.add(key)
    out.append(l)
open(p, "w", encoding="utf-8").write("\n".join(out)); print(f"{n} doublons retirés")
