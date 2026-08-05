# 📅 SCHEDULE — LOCKED

> **This file is the single source of truth for all dates.**
> If any other document disagrees with this file, this file wins.

**Status:** 🔒 **LOCKED** — updated 2 August 2026 (revision 2)
**Change:** Series pauses after Day 28 (2 Aug 2026); resumes at Week 5 on **14 Sep 2026**.

> **Revision history**
> - r1 (31 Jul 2026): pause after Day 28, resume 31 Aug 2026
> - **r2 (2 Aug 2026): resume moved +14 days to 14 Sep 2026** ← current

---

## The Change in One Line

**Days 1–28 run to Sunday 2 August 2026 → 6-week pause → Week 5 resumes Monday 14 September 2026.**

---

## Key Dates

| Milestone | Date | Day |
|-----------|------|-----|
| Series start | Monday, 6 July 2026 | Day 1 |
| **Phase 1 ends** | **Sunday, 2 August 2026** | **Day 28** |
| ⏸️ Pause begins | Monday, 3 August 2026 | — |
| ⏸️ Pause ends | Sunday, 13 September 2026 | — |
| **Phase 2 resumes** | **Monday, 14 September 2026** | **Day 29 · Week 5** |
| Series end | Sunday, 8 November 2026 | Day 84 |

**Pause duration:** exactly 42 days (6 full weeks), Mon 3 Aug → Sun 13 Sep 2026.
**Total elapsed:** 6 Jul → 8 Nov 2026 (18 calendar weeks, 12 teaching weeks).

Day 28 falls exactly on the Week 4 boundary (28 = 4 × 7), so the pause lands on a clean
week break with no split week on either side. Every week in both phases runs Monday–Sunday.

---

## PHASE 1 — Weeks 1–4 · Days 1–28
*6 July – 2 August 2026* — ✅ **COMPLETE**

| Week | Days | Dates | Theme | Status |
|------|------|-------|-------|--------|
| 01 | 1–7 | Jul 6–12 | Foundations — LLM internals | ✅ Complete |
| 02 | 8–14 | Jul 13–19 | Efficiency — quantization, fine-tuning, serving | ✅ Complete |
| 03 | 15–21 | Jul 20–26 | Retrieval & Agents — RAG, agents, capstone | ✅ Complete |
| 04 | 22–28 | Jul 27–Aug 2 | Production — LLMOps, cost, security, multi-modal | ✅ Complete |

**Verified:** 28 PDFs · 549 pages · 371 Eagle Eye terms · 0 gaps · 0 FAANG-rule violations.

### Phase 1 Day-by-Day

| Day | Date | Topic |
|-----|------|-------|
| 1 | Mon Jul 6 | Tokenization |
| 2 | Tue Jul 7 | Embeddings |
| 3 | Wed Jul 8 | Transformer Architecture |
| 4 | Thu Jul 9 | Training Lifecycle |
| 5 | Fri Jul 10 | Scaling Laws & Prompt Engineering |
| 6 | Sat Jul 11 | Structured Output |
| 7 | Sun Jul 12 | Model Selection Dashboard |
| 8 | Mon Jul 13 | Quantization |
| 9 | Tue Jul 14 | LoRA & PEFT |
| 10 | Wed Jul 15 | Full Fine-Tuning |
| 11 | Thu Jul 16 | Model Serving |
| 12 | Fri Jul 17 | Evaluation |
| 13 | Sat Jul 18 | Efficiency |
| 14 | Sun Jul 19 | Week 2 Project |
| 15 | Mon Jul 20 | RAG Foundations |
| 16 | Tue Jul 21 | RAG Indexing Pipelines |
| 17 | Wed Jul 22 | RAG Retrieval Deep Dive |
| 18 | Thu Jul 23 | RAG Generation & Prompt Engineering |
| 19 | Fri Jul 24 | Agents and Tool Use |
| 20 | Sat Jul 25 | Multi-Agent Systems |
| 21 | Sun Jul 26 | **Week 3 Capstone** — End-to-End Text-to-SQL |
| 22 | Mon Jul 27 | Production LLM Operations |
| 23 | Tue Jul 28 | Prompt and Model Versioning |
| 24 | Wed Jul 29 | Cost Optimization at Scale |
| 25 | Thu Jul 30 | Security and Compliance |
| 26 | Fri Jul 31 | Multi-Modal Systems |
| 27 | Sat Aug 1 | Fine-Tuning for Production |
| 28 | **Sun Aug 2** | **Week 4 Capstone & Phase 1 Close** |

---

## ⏸️ PAUSE — 3 August – 13 September 2026

No teaching days. 42 days (6 weeks).

**On resume, re-anchor before Day 29:**
- The running capstone is the Text-to-SQL system built across Days 13–27
- Final measured state: **82.8% execution accuracy · p95 3,740 ms · $0.002694/query**
- **Accuracy budget: 0.8pp remaining** — this is the binding constraint on the system
- Full handoff is in **Day 28 §5 (RESUME BRIEF)** — read that first

**First three actions on resume (from Day 28):**
1. Buy accuracy headroom — two prompt fixes worth ~3pp (Day 21 failure triage)
2. Deploy Tier 1 security — `llm_query_role` + RLS, 20 minutes (Day 28 §2)
3. Wire the two CI gates — golden set (Day 23) + IsolationTestSuite (Day 25)

---

## PHASE 2 — Weeks 5–12 · Days 29–84
*14 September – 8 November 2026*

| Week | Days | Dates | Theme | Project |
|------|------|-------|-------|---------|
| 05 | 29–35 | **Sep 14–20** | Agents & Tool Calling | Tool-Calling Agent (PORTFOLIO) |
| 06 | 36–42 | Sep 21–27 | MCP, Context Engineering & Multi-Agent | MCP Server + Multi-Agent Pipeline (PORTFOLIO) |
| 07 | 43–49 | Sep 28–Oct 4 | Evaluation & Production Applications | Eval & Observability Platform (PORTFOLIO) |
| 08 | 50–56 | Oct 5–11 | Agentic System Design | Scalable Agent Runtime (MINI) |
| 09 | 57–63 | Oct 12–18 | Multimodal & Reasoning Models | Multimodal Document Processor (PORTFOLIO) |
| 10 | 64–70 | Oct 19–25 | AI Security, Red Teaming & Responsible AI | Red Team Your Own RAG System (PORTFOLIO) |
| 11 | 71–77 | Oct 26–Nov 1 | Cloud-Native Deployment, LLMOps & Synthetic Data | Deploy Production AI Service (PORTFOLIO) |
| 12 | 78–84 | Nov 2–8 | **Capstone** — Enterprise AI Assistant | Full Capstone (CAPSTONE) |

---

## Date Shift History

Weeks 1–4 have never moved. Weeks 5–12 have shifted **+42 days total** from the original plan.

| Week | Original | r1 (+28d) | **r2 (+42d) — CURRENT** |
|------|----------|-----------|-------------------------|
| 05 | Aug 3–9 | Aug 31–Sep 6 | **Sep 14–20** |
| 06 | Aug 10–16 | Sep 7–13 | **Sep 21–27** |
| 07 | Aug 17–23 | Sep 14–20 | **Sep 28–Oct 4** |
| 08 | Aug 24–30 | Sep 21–27 | **Oct 5–11** |
| 09 | Aug 31–Sep 6 | Sep 28–Oct 4 | **Oct 12–18** |
| 10 | Sep 7–13 | Oct 5–11 | **Oct 19–25** |
| 11 | Sep 14–20 | Oct 12–18 | **Oct 26–Nov 1** |
| 12 | Sep 21–27 | Oct 19–25 | **Nov 2–8** |
| **End** | Sep 27 | Oct 25 | **Nov 8, 2026** |

---

## Daily Protocol (unchanged across the pause)

Every teaching day runs all four steps:

1. **Teach** the day's topic fully in chat — concept-first, plain English, FAANG examples,
   Architect's Lens, hands-on exercises
2. **Eagle Eye** — two-pass verification (keyword scan + snip confirmation on every flag);
   never declare a gap without snip verification, never declare coverage without confirmation
3. **PDF** → `~/Desktop/AI-ML/WeekN_DayNN_TopicName.pdf`
4. **Push** → `week-NN/notes/` on `git@github.com:irudi2021/ai-engineering-journey.git`

**FAANG rule (locked):** examples use only Meta, Apple, Amazon, Netflix, Google, Microsoft.
**Eagle Eye standard (locked):** "Don't hallucinate and don't miss anything."

**Trigger to resume:** say `Day 29 Week 5 Start` on or after 14 September 2026.

---

*Locked 2 August 2026 (r2). Supersedes all prior date tables in this repository.*
