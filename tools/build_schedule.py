#!/usr/bin/env python3
"""Build SCHEDULE.md and README.md from CURRICULUM_MASTER.md (titles + 2026 layer). Usage: build_schedule.py <repo>"""
import re, sys
from datetime import date, timedelta

repo = sys.argv[1]
master = open(f"{repo}/CURRICULUM_MASTER.md").read()
START = date(2026, 10, 19)

rows = {}
for m in re.finditer(r"^\| (\d+) \| ((?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) [A-Z][a-z]{2} \d{1,2}) \| (.+?) \|$", master, re.M):
    rows.setdefault(int(m.group(1)), (m.group(2), m.group(3)))
assert sorted(rows) == list(range(1, 85)), f"missing days: {set(range(1,85)) - set(rows)}"
for n, (dt, _) in rows.items():
    x = START + timedelta(days=n - 1)
    assert dt == f"{x:%a} {x:%b} {x.day}", f"day {n} date mismatch: {dt}"

# 2026 Currency Layer: the "| Day | 2026 addition |" tables in the master
LAYER = {}
for blk in re.findall(r"\| Day \| 2026 addition \|\n\|-+\|-+\|\n((?:\|.*\|\n?)+)", master):
    for m in re.finditer(r"^\| (\d+) \| (.+) \|$", blk, re.M):
        LAYER[int(m.group(1))] = m.group(2)
assert sorted(LAYER) == list(range(1, 85)), f"layer missing: {set(range(1,85)) - set(LAYER)}"

WEEKS = [
 ("Foundations — LLM internals", "Model Selection Dashboard (MINI)"),
 ("Efficiency — quantization, fine-tuning, serving", "Domain Fine-Tune + Quantize (PORTFOLIO)"),
 ("Retrieval & Agents — RAG, agents, multi-agent", "End-to-End Text-to-SQL (CAPSTONE)"),
 ("Production — LLMOps, versioning, cost, security, multimodal", "Production Hardening & Review (PORTFOLIO)"),
 ("Agents, Harness & Loop Engineering + Agentic Frameworks", "AI Research Agent with Tool Calling (PORTFOLIO)"),
 ("Context Engineering, MCP & Multi-Agent Frameworks", "Multi-Agent Business Analyst System (PORTFOLIO)"),
 ("Production AI Systems, Evaluation & Observability", "Eval & Observability Platform (PORTFOLIO)"),
 ("AI Application Engineering (FastAPI) & Agentic System Design", "End-to-End AI Backend + Agent Runtime (PORTFOLIO)"),
 ("Machine Learning & Deep Learning Foundations", "ML & DL Project Development — 5 projects (PORTFOLIO)"),
 ("NLP, Multimodal, Reasoning & Red Teaming", "NLP & Multimodal Projects + Red Team — 3 projects (PORTFOLIO)"),
 ("Cloud Deployment, AI Infrastructure & LLMOps", "Deploy a Production-Ready AI Service (PORTFOLIO)"),
 ("No-Code AI Platforms & Enterprise Capstone", "Enterprise Multi-Document RAG Assistant (CAPSTONE)"),
]
D = lambda n: START + timedelta(days=n - 1)
def long(n): x = D(n); return f"{x:%A}, {x.day} {x:%B} {x.year}"
XMAS, NY = (date(2026, 12, 25) - START).days + 1, (date(2027, 1, 1) - START).days + 1

def wk_range(w):
    a = START + timedelta(days=7 * w); b = a + timedelta(days=6)
    if a.month == b.month: return f"{a:%b} {a.day}–{b.day}"
    return f"{a:%b} {a.day}–{b:%b} {b.day}"

week_tbl = "\n".join(f"| {w+1:02d} | {7*w+1}–{7*w+7} | {wk_range(w)} | {t} | {p} |" for w, (t, p) in enumerate(WEEKS))
day_sections = []
for w, (t, _) in enumerate(WEEKS):
    a = START + timedelta(days=7 * w); b = a + timedelta(days=6)
    hdr = f"### Week {w+1:02d} · {t} — Days {7*w+1}–{7*w+7} · {a:%a} {a.day} {a:%b} – {b:%a} {b.day} {b:%b} {b.year}"
    body = "\n".join(f"| {n} | {rows[n][0]} | {rows[n][1]} | {LAYER[n]} |" for n in range(7*w+1, 7*w+8))
    day_sections.append(f"{hdr}\n\n| Day | Date | Topic | ⚡ 2026 addition |\n|-----|------|-------|------------------|\n{body}")

schedule = f"""# 📅 SCHEDULE — LOCKED

> **This file is the single source of truth for all dates.**
> If any other document disagrees with this file, this file wins.
> Content authority: 📗 [`CURRICULUM_MASTER.md`](CURRICULUM_MASTER.md).

**Status:** 🔒 **LOCKED — 14 October 2026 · FRESH RUN**

---

## The Run in One Line

**Day 1: {long(1)} → Day 84: {long(84)} — 84 consecutive teaching days, no rest days.**

---

## Key Dates

| Milestone | Date | Day |
|-----------|------|-----|
| **Start** | **{long(1)}** | **Day 1** |
| End of Week 4 | {long(28)} | Day 28 |
| Christmas — teaching day | {long(XMAS)} | Day {XMAS} |
| New Year — teaching day | {long(NY)} | Day {NY} |
| **End** | **{long(84)}** | **Day 84** |

Every week runs Monday–Sunday. No pauses, no rest days — Christmas and New Year are
teaching days by choice.

---

## Week Overview

| Week | Days | Dates | Theme | Project |
|------|------|-------|-------|---------|
{week_tbl}

**Track 0 (self-study, not teaching days):** Python, Pandas, NumPy, OOP & SQL —
preserved in full in `CURRICULUM_MASTER.md`.

---

## Day-by-Day

Each day: the core topic plus its **⚡ 2026 addition** (Currency Layer u1, verified 11 Oct 2026).

{chr(10).join(s + chr(10) for s in day_sections)}
---

## Daily Protocol

Every teaching day runs all four steps:

1. **Teach** the day's topic fully in chat — concept-first, plain English, FAANG examples,
   Architect's Lens, hands-on exercises
2. **Eagle Eye** — two-pass verification (keyword scan + snip confirmation on every flag);
   never declare a gap without snip verification, never declare coverage without confirmation
3. **PDF** → `~/Desktop/AI-ML/WeekN_DayNN_TopicName.pdf`
4. **Push** → `week-NN/notes/` on `git@github.com:irudi2021/ai-engineering-journey.git`

**FAANG rule (locked):** examples use only Meta, Apple, Amazon, Netflix, Google, Microsoft.
**Eagle Eye standard (locked):** "Don't hallucinate and don't miss anything."

**Daily trigger:** `Day N Week M Start`

---

## History

- **6 Jul – 2 Aug 2026:** a first run covered Days 1–28, then paused. Its lesson PDFs were
  removed on 11 Oct 2026 for a clean restart; they remain recoverable from git history
  (last present at commit `7f258ab`).
- **2 Aug 2026:** content merge revision m1 — a 4-month external syllabus absorbed into
  the 12 weeks (133/133 topics, 53/53 resources preserved).
- **11 Oct 2026:** fresh run locked — Day 1 = 12 Oct 2026, Day 84 = 3 Jan 2027.
- **11 Oct 2026:** 2026 Currency Layer u1 — one verified 2026 addition per day (MCP 2026-07-28,
  A2A v1.0, Agent Skills, OWASP Agentic Top 10, RLVR, disaggregated serving, EU AI Act Omnibus).
  Additive only; no m1 topic changed.
- **14 Oct 2026:** start moved one week later — Day 1 = Mon 19 Oct 2026, Day 84 = Sun 10 Jan 2027
  (every date shifted +7 days; no topic changed). Christmas = Day {XMAS}, New Year = Day {NY}.

*Locked 14 October 2026.*
"""
open(f"{repo}/SCHEDULE.md", "w").write(schedule)

readme_weeks = "\n".join(f"| {w+1:02d} | {t} | {p} | {wk_range(w)} |" for w, (t, p) in enumerate(WEEKS))
readme = f"""# AI Engineering Journey

A 12-week hands-on curriculum — From LLM Foundations to Production-Grade AI Systems.

**Topics:** Python & SQL Foundations · Machine Learning · Deep Learning & CNNs · Computer Vision · NLP · LLMs · Fine-Tuning · RAG · Agents · LangChain · LangGraph · CrewAI · AutoGen · MCP · Evals · RAGAS · LangSmith · Guardrails · Harness Engineering · Loop Engineering · Context Engineering · FastAPI · System Design · Multimodal · Security & Red Teaming · Cloud & LLMOps · No-Code AI Platforms

**Start:** {long(1)} · **End:** {long(84)} · **84 days, no rest days**

**Current to October 2026:** every day carries a verified 2026 addition — MCP spec 2026-07-28 · A2A v1.0 · Agent Skills · harness & context engineering · OWASP Top 10 for Agentic Applications · RLVR/GRPO · disaggregated inference · OpenTelemetry GenAI · EU AI Act Digital Omnibus.

> 📅 **[`SCHEDULE.md`](SCHEDULE.md)** — authoritative source for all dates, full day-by-day
> 📗 **[`CURRICULUM_MASTER.md`](CURRICULUM_MASTER.md)** — complete content authority for Weeks 1–12
> 📄 **[`AI_Engineering_Complete_Syllabus_Weeks1-12.pdf`](AI_Engineering_Complete_Syllabus_Weeks1-12.pdf)** — full syllabus PDF

---

## Curriculum Overview

| Week | Theme | Project | Dates |
|------|-------|---------|-------|
{readme_weeks}

**Track 0 (self-study):** Python, Pandas, NumPy, OOP & SQL.

---

## Weekly Structure

Each week folder contains:
- `notes/` — daily lesson PDFs
- `project/` — weekly hands-on project code
- `notebooks/` — Jupyter notebooks for experiments

`tools/` holds the generators for the schedule, syllabus PDF and verification.

---

## Progress

**Day 0 of 84.** Fresh run starts {long(1)}. Day 1 (Tokenization) notes are already in `week-01/notes/`.

---

## Setup

```bash
cd /Users/thaya/AI-Engineering
source .venv/bin/activate
```

---

*Instructor: Pro AI Principal Architect*
"""
open(f"{repo}/README.md", "w").write(readme)
print(f"✓ SCHEDULE.md — 12 week rows, {len(rows)} day rows + {len(LAYER)} layer entries, dates verified; Christmas=Day {XMAS}, New Year=Day {NY}")
print("✓ README.md")
