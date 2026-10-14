#!/usr/bin/env python3
"""Re-date the curriculum files: Day 1 = Mon 19 Oct 2026 -> Day 84 = Sun 10 Jan 2027."""
import re, sys
from datetime import date, timedelta

START = date(2026, 10, 19)
d = lambda n: START + timedelta(days=n - 1)
short = lambda n: f"{d(n):%a} {d(n):%b} {d(n).day}"
repo = sys.argv[1]

def week_hdr(m):
    a, b = int(m.group(1)), int(m.group(2)); x, y = d(a), d(b)
    if x.year != y.year: rng = f"{x.day} {x:%B} {x.year} – {y.day} {y:%B} {y.year}"
    elif x.month == y.month: rng = f"{x.day}–{y.day} {x:%B} {x.year}"
    else: rng = f"{x.day} {x:%B} – {y.day} {y:%B} {y.year}"
    return f"**Days {a}–{b} · {rng}**"

def redate(src):
    src, nh = re.subn(r"\*\*Days (\d+)–(\d+) · [^*]+\*\*", week_hdr, src)
    src, nr = re.subn(r"^\| (\d+) \| (?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) [A-Z][a-z]{2} \d{1,2} \|",
                      lambda m: f"| {m.group(1)} | {short(int(m.group(1)))} |", src, flags=re.M)
    return src, nh, nr

def must(src, old, new):
    assert src.count(old) == 1, f"expected once: {old[:70]!r}"
    return src.replace(old, new)

# ── MASTER ──
p = f"{repo}/CURRICULUM_MASTER.md"; s = open(p).read()
s, nh, nr = redate(s); print(f"MASTER: {nh} week headers, {nr} day rows")
s = must(s, "> 🔒 **LOCKED 11 October 2026 — FRESH RUN.**\n> **Day 1: Monday 12 October 2026 → Day 84: Sunday 3 January 2027.**\n> 84 consecutive teaching days. No rest days — Christmas (Day 75) and New Year (Day 82)",
            "> 🔒 **LOCKED 14 October 2026 — FRESH RUN.**\n> **Day 1: Monday 19 October 2026 → Day 84: Sunday 10 January 2027.**\n> 84 consecutive teaching days. No rest days — Christmas (Day 68) and New Year (Day 75)")
s = must(s, "*12 October – 8 November 2026*", "*19 October – 15 November 2026*")
s = must(s, "*9 November 2026 – 3 January 2027*", "*16 November 2026 – 10 January 2027*")
s = must(s, "*Locked 11 October 2026 — fresh run, Day 1 = Mon 12 Oct 2026, Day 84 = Sun 3 Jan 2027.",
            "*Locked 14 October 2026 — fresh run, Day 1 = Mon 19 Oct 2026, Day 84 = Sun 10 Jan 2027.")
open(p, "w").write(s)

# ── PHASE2 ──
p = f"{repo}/CURRICULUM_PHASE2.md"; s = open(p).read()
s, nh, nr = redate(s); print(f"PHASE2: {nh} week headers, {nr} day rows")
s = must(s, "Dates re-aligned 11 Oct 2026 to the fresh run.", "Dates re-aligned 14 Oct 2026 to the fresh run (Day 1 = Mon 19 Oct 2026).")
open(p, "w").write(s)

# ── EXTENDED ──
p = f"{repo}/CURRICULUM_EXTENDED.md"; s = open(p).read()
s = must(s, "fresh run locked 11 October 2026** (Day 1 = Mon 12 Oct 2026,\n> Day 84 = Sun 3 Jan 2027)",
            "fresh run locked 14 October 2026** (Day 1 = Mon 19 Oct 2026,\n> Day 84 = Sun 10 Jan 2027)")
# reverse order so a replacement never feeds the next one
s = must(s, "*Dec 28, 2026 – Jan 3, 2027*", "*Jan 4 – Jan 10, 2027*")       # Week 12
s = must(s, "*Dec 21 – Dec 27, 2026*", "*Dec 28, 2026 – Jan 3, 2027*")      # Week 11
s = must(s, "*Dec 14 – Dec 20, 2026*", "*Dec 21 – Dec 27, 2026*")           # Week 10
s = must(s, "*Dates updated 11 October 2026 for the fresh run", "*Dates updated 14 October 2026 for the fresh run")
open(p, "w").write(s)
