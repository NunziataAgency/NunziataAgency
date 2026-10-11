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
for m in re.finditer(r"^([RBF])(\d+)\. \*\*(.+?)\*\* — ([\d,]+)/10 — (?:📅 (\d\d/\d\d) — )?(.+)$", text, re.M):
    kind, num, head, score, date, rest = m.groups()
    url = re.search(r"\[source\]\((.+?)\)", rest)
    rest = re.sub(r"\s*—?\s*\[source\]\(.+?\)", "", rest).strip(" —")
    items.append({"id": f"{kind}{num}", "kind": kind, "title": head,
                  "score": float(score.replace(",", ".")), "body": rest,
                  "url": url.group(1) if url else "", "date": date or ""})

# Mon numéro : brefs rédigés, questions du jour, notes de rubriques (les plus récents)
def latest(pattern):
    files = sorted(glob.glob(os.path.join(here, "..", pattern)))
    return files[-1] if files else None

brefs = []
bf = latest("brefs/2*.md")
if bf:
    for sec in re.split(r"^## ", open(bf, encoding="utf-8").read(), flags=re.M)[1:]:
        head, _, body = sec.partition("\n")
        lines = [l.replace("Variante : ", "").strip() for l in body.splitlines() if "[Lien](" in l]
        note = " ".join(l.strip() for l in body.splitlines() if l.startswith("Vérif"))
        brefs.append({"head": head.strip(), "ok": "✅" in head, "lines": lines, "note": note})

questions = []
qf = os.path.join(here, "..", "questions", "actu.md")
if os.path.exists(qf):
    for l in open(qf, encoding="utf-8"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) == 6 and c[0].startswith("A-") and "dispo" in c[5]:
            questions.append({"id": c[0], "text": c[1], "format": c[2], "note": c[4]})

docs = []
day = os.path.basename(bf)[:10] if bf else ""
for f in sorted(glob.glob(os.path.join(here, "..", "dossiers", f"{day}*.md"))):
    body = open(f, encoding="utf-8").read()
    t = re.search(r"^# (.+)$", body, re.M)
    docs.append({"title": re.sub(r"\s+—\s+note du.*$", "", t.group(1)) if t else os.path.basename(f), "body": body})

tpl = open(os.path.join(here, "template.html"), encoding="utf-8").read()
out = tpl.replace("__TITLE__", html.escape(title)).replace("__DATA__", json.dumps(items, ensure_ascii=False)).replace("__NUM__", json.dumps({"brefs": brefs, "questions": questions, "docs": docs}, ensure_ascii=False).replace("</", "<\\/"))
open(os.path.join(here, "veille.html"), "w", encoding="utf-8").write(out)
print(f"{len(items)} sujets, {len(brefs)} brefs, {len(questions)} questions, {len(docs)} notes → newsletter/app/veille.html")
