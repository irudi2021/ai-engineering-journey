#!/usr/bin/env python3
"""Eagle Eye pass 1 for the syllabus PDF: every master/schedule line and cell present, dates correct.
Usage: eagle_syllabus.py <repo> <pdf>"""
import re, sys
from datetime import date, timedelta
from pypdf import PdfReader
repo, pdf = sys.argv[1], sys.argv[2]
START = date(2026, 10, 19)
txt = "".join(p.extract_text() for p in PdfReader(pdf).pages)
N = lambda s: re.sub(r"[^a-z0-9]", "", s.lower()); T = N(txt)
master = open(f"{repo}/CURRICULUM_MASTER.md").read(); sched = open(f"{repo}/SCHEDULE.md").read()
clean = lambda l: N(re.sub(r"[*`>#|]", " ", re.sub(r"\[`?([^\]`]+)`?\]\([^)]+\)", r"\1", l)))
miss = []
for name, src in [("master", master), ("schedule", sched.split("## Daily Protocol")[0])]:
    for l in src.splitlines():
        if re.fullmatch(r"[\s|:-]*", l): continue
        for c in (l.strip().strip("|").split("|") if l.strip().startswith("|") else [l]):
            k = clean(c)
            if len(k) >= 3 and k not in T: miss.append((name, c.strip()[:100]))
print("PASS 1 — lines/cells missing from PDF:", len(miss)); [print("  ", m) for m in miss[:20]]
bad = [n for n in range(1, 85) for f in (sched, master)
       if not re.search(rf"^\| {n} \| {(START+timedelta(n-1)):%a %b} {(START+timedelta(n-1)).day} \|", f, re.M)]
print("Day rows with wrong date (schedule+master):", bad or "none")
old = [w for w in ["12 October 2026", "3 January 2027", "Mon Oct 12 ", "Day 82"] if w in txt]
print("Old-run date strings in PDF:", old or "none")
print("'oracle' as a word:", bool(re.search(r"\boracle\b", txt, re.I)), "| ■ boxes:", txt.count("■"))
