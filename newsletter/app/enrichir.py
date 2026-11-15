#!/usr/bin/env python3
"""Remplace le champ « détails » de sujets de la veille par un résumé enrichi.

Usage : python3 newsletter/app/enrichir.py <veille.md> <enrich.md> [<enrich2.md> …]
Chaque fichier enrich contient des lignes « R12 | résumé enrichi ».
"""
import re
import sys

veille, sources = sys.argv[1], sys.argv[2:]
resume = {}
for src in sources:
    for line in open(src, encoding="utf-8"):
        m = re.match(r"^\s*([RBF]\d+)\s*\|\s*(.+?)\s*$", line)
        if m:
            resume[m.group(1)] = m.group(2).replace(" — ", ", ")

lines = open(veille, encoding="utf-8").read().split("\n")
n = 0
for i, l in enumerate(lines):
    m = re.match(r"^([RBF]\d+)\. ", l)
    if not m or m.group(1) not in resume:
        continue
    parts = l.split(" — ")
    if len(parts) < 4:
        continue
    tail = parts[-2:] if parts[-1].startswith("[source]") else parts[-1:]
    lines[i] = " — ".join(parts[:3] + [resume[m.group(1)]] + tail)
    n += 1
open(veille, "w", encoding="utf-8").write("\n".join(lines))
print(f"{n} sujets enrichis")
