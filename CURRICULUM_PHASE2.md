# Phase 2 Curriculum — Weeks 5–12 · Days 29–84

> ⚠️ **SUPERSEDED (2 Aug 2026) by 📗 [`CURRICULUM_MASTER.md`](CURRICULUM_MASTER.md)**
> after the 4-month syllabus merge. Retained for the coverage-audit rationale in the
> section below, which still explains why harness / loop / context engineering were added.
> **For current Week 5–12 content, use `CURRICULUM_MASTER.md`.**

> 🔒 **LOCKED 2 August 2026.** Dates are governed by [`SCHEDULE.md`](SCHEDULE.md).
> This document governs **content**. Weeks 5 and 6 are specified day-by-day;
> Weeks 7–12 are specified at week level and will be expanded before each week begins.

---

## Why Weeks 5 and 6 Were Rewritten

A coverage audit of the 28-PDF Phase 1 corpus (549 pages) measured five engineering
disciplines against the material actually taught:

| Discipline | Terms matched | Days w/ coverage | Verdict |
|------------|---------------|------------------|---------|
| Evals | 13/14 | 28/28 | ✅ Strong |
| Guardrails | 13/13 | 21/28 | ✅ Strong |
| Loop engineering | 10/13 | 19/28 | 🟡 Mechanics present, discipline unnamed |
| Context engineering | 6/15 | 20/28 | 🟠 Pieces scattered, never assembled |
| Harness engineering | 4/12 | 13/28 | 🔴 Genuine gap |

**Terms absent from all 549 pages:**
- Loop: `termination`, `stopping condition`, `loop engineering`
- Context: `context engineering`, `context budget`, `compaction`, `token budget`,
  `progressive disclosure`, `just-in-time`, `context rot`, `note-taking`, `external memory`
- Harness: `tool design`, `tool namespacing`, `tool response`, `execution environment`,
  `token-efficient`, `tool ergonomics`, `affordance`

Phase 1's spine was *building a system*. These three are disciplines you can only
recognise once you have built one — which makes Phase 2 the correct place for them,
not a correction of Phase 1.

**Resolution:** no extra weeks. Weeks 5 and 6 are re-weighted to name and teach these
disciplines explicitly, folding into the projects already allocated to those weeks.

---

## WEEK 5 · AGENTS, HARNESS & LOOP ENGINEERING
**Days 29–35 · 14–20 September 2026**
**Project:** Tool-Calling Agent (PORTFOLIO)

Builds directly on Day 19 (ReAct, tools, memory) and Day 20 (multi-agent).
**Re-read both before Day 29.**

| Day | Date | Topic |
|-----|------|-------|
| 29 | Mon Sep 14 | **Agent Architectures Beyond ReAct** |
| 30 | Tue Sep 15 | **Harness Engineering I — Tool Design** |
| 31 | Wed Sep 16 | **Harness Engineering II — Responses, Errors & Environment** |
| 32 | Thu Sep 17 | **Loop Engineering I — Termination & Budgets** |
| 33 | Fri Sep 18 | **Loop Engineering II — Recovery & Sub-Agents** |
| 34 | Sat Sep 19 | **Agent Frameworks & Human-in-the-Loop** |
| 35 | Sun Sep 20 | **Week 5 Project** — Tool-Calling Agent |

### Day 29 · Agent Architectures Beyond ReAct
Plan-and-execute, reflection/critic loops, tree search, router-only agents.
When each pattern applies and when it is over-engineering. Cost and latency profile
per architecture. Re-anchoring on the Day 19–20 agent as the baseline to beat.

### Day 30 · Harness Engineering I — Tool Design
The premise: **agent quality is frequently bounded by harness quality, not model quality.**
- Tool granularity — why 4 tools beat 15 or 2; the coherent-operation rule
- Naming and description as model-facing documentation, not developer docs
- Namespacing as tool counts grow; discovery and selection failure modes
- Affordances — designing a tool so the correct call is the obvious one
- Schema design: required vs optional, defaults, enums over free text
- Measuring tool-selection accuracy in isolation from task accuracy

### Day 31 · Harness Engineering II — Responses, Errors & Environment
- Response shape: what comes back, and what share of the context budget it consumes
- Truncation and pagination strategies that do not destroy meaning
- **Error messages written to teach the model to recover**, not to inform a human log
- Idempotency and safe retry semantics at the tool boundary
- The execution environment (sandbox, filesystem, network) as a design surface
- Token-efficient tool results — the harness-side equivalent of Day 24's cost work

### Day 32 · Loop Engineering I — Termination & Budgets
- Stopping conditions: goal-satisfied, budget-exhausted, no-progress, human-required
- **Budgets as a joint constraint** — steps, tokens, wall-clock, and cost together;
  Day 19's `MAX_STEPS` is one axis of four
- Convergence detection vs. thrashing detection (repeating a failing call)
- Partial-result contracts: what a loop returns when it runs out of budget
- Instrumenting loop shape — step histograms, termination-reason distributions

### Day 33 · Loop Engineering II — Recovery & Sub-Agents
- Retry taxonomy: transient / malformed / semantic / unrecoverable — each needs a
  different response
- Escalation ladders (extends Day 24's `EscalatingGenerator` to the loop level)
- When to spawn a sub-agent: context isolation, budget isolation, failure isolation
- What the model sees **between** iterations — observation formatting as a lever
- Loop-level guardrails: cost circuit breakers, runaway detection

### Day 34 · Agent Frameworks & Human-in-the-Loop
Framework landscape and what each abstracts away (and hides). Approval gates,
interruption and resumption, durable agent state across a human pause.
Extends Day 20's Netflix `clarify_question` pattern into a general design.

### Day 35 · Week 5 Project — Tool-Calling Agent (PORTFOLIO)
Build an agent whose **harness and loop are the deliverable**, not the prompt:
measured tool-selection accuracy, an explicit four-axis budget, a termination-reason
distribution, and error messages demonstrated to improve recovery rate.

---

## WEEK 6 · CONTEXT ENGINEERING, MCP & MULTI-AGENT
**Days 36–42 · 21–27 September 2026**
**Project:** MCP Server + Multi-Agent Pipeline (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 36 | Mon Sep 21 | **Context Engineering I — The Context Budget** |
| 37 | Tue Sep 22 | **Context Engineering II — Compaction & Progressive Disclosure** |
| 38 | Wed Sep 23 | **MCP Fundamentals** |
| 39 | Thu Sep 24 | **Building a Production MCP Server** |
| 40 | Fri Sep 25 | **Multi-Agent Communication & Handoffs** |
| 41 | Sat Sep 26 | **Agent Memory Architectures** |
| 42 | Sun Sep 27 | **Week 6 Project** — MCP Server + Multi-Agent Pipeline |

### Day 36 · Context Engineering I — The Context Budget
The discipline Phase 1 used implicitly and never named.
- The context window as a **budget to allocate**, not a limit to avoid
- Allocation across: system rules, tools, retrieved context, history, working notes
- **Context rot** — why a model's effective use of context degrades before the
  window is full, and how to detect it in your own system
- Position effects: what belongs at the start, what belongs nearest the question
- Assembling Phase 1's scattered pieces into one model: Day 18's 3-layer prompt,
  Day 24's prefix ordering, Day 17's compression, Day 26's token costs
- Measuring it: context utilisation vs. context *usefulness*

### Day 37 · Context Engineering II — Compaction & Progressive Disclosure
- **Compaction**: summarising history at checkpoints without losing decisions made
- What must survive compaction (commitments, constraints, failures) vs. what may not
- **Progressive disclosure**: load context when needed rather than pre-loading
- **Just-in-time retrieval** inside an agent loop, not only before it
- **Note-taking / external memory**: the filesystem as unbounded context
- **Sub-agent context isolation** as a context-engineering tool (links Day 33)
- Failure modes: lost-in-the-middle, stale context, contradictory context

### Day 38 · MCP Fundamentals
Protocol model, servers and clients, transports. Resources vs. tools vs. prompts and
why the distinction matters. Capability negotiation. Where MCP fits relative to the
tool schemas from Day 19 and the harness design from Days 30–31.

### Day 39 · Building a Production MCP Server
Expose the Text-to-SQL capstone over MCP. Authentication and authorisation, per-tenant
scoping (carrying Day 25's isolation requirements across the protocol boundary),
error semantics, versioning the server contract (Day 23's discipline applied to MCP).

### Day 40 · Multi-Agent Communication & Handoffs
Deepens Day 20. Handoff protocols and what transfers with them, shared vs. isolated
state, supervisor routing policies, deadlock and livelock in agent graphs,
debugging a multi-agent trace.

### Day 41 · Agent Memory Architectures
Episodic, semantic and procedural memory. Consolidation and forgetting policies.
Cross-session identity and personalisation. Extends Day 19's `AgentLongTermMemory`
into a designed subsystem, with Day 25's erasure requirements built in from the start.

### Day 42 · Week 6 Project — MCP Server + Multi-Agent Pipeline (PORTFOLIO)
Production MCP server fronting a multi-agent pipeline, with an explicit context budget
per agent, a compaction strategy, and a measured comparison of context utilisation
before and after Day 37's techniques.

---

## WEEKS 7–12 · Week-Level Specification

Expanded day-by-day before each week begins.

### WEEK 7 · Evaluation & Production Applications
**Days 43–49 · 28 Sep – 4 Oct 2026** · Eval & Observability Platform (PORTFOLIO)
LLM-as-a-judge (the one eval technique absent from Phase 1), eval harness design,
golden dataset construction, regression gates, tracing and observability tooling,
user feedback loops, production dashboards. Builds on Days 12, 21, 22, 23.

### WEEK 8 · Agentic System Design
**Days 50–56 · 5–11 Oct 2026** · Scalable Agent Runtime (MINI)
Agent runtime architecture, state management, queueing and backpressure, horizontal
scaling, failure isolation, concurrency at agent scale. Builds on Days 20, 22.

### WEEK 9 · Image, Multimodal & Reasoning Models
**Days 57–63 · 12–18 Oct 2026** · Multimodal Document Processor (PORTFOLIO)
Extends Day 26: vision-language architectures, document understanding at scale,
OCR pipelines, chart and diagram reasoning, reasoning models and test-time compute.

### WEEK 10 · AI Security, Red Teaming & Responsible AI
**Days 64–70 · 19–25 Oct 2026** · Red Team Your Own RAG System (PORTFOLIO)
OWASP LLM Top 10, systematic adversarial testing (Garak, PyRIT), guardrail engineering,
injection defences, bias and fairness metrics, model cards, EU AI Act / NIST AI RMF /
ISO 42001. Builds on Day 25. See [`CURRICULUM_EXTENDED.md`](CURRICULUM_EXTENDED.md).

### WEEK 11 · Cloud-Native Deployment, LLMOps & Synthetic Data
**Days 71–77 · 26 Oct – 1 Nov 2026** · Deploy a Production-Ready AI Service (PORTFOLIO)
Cloud deployment, GPU autoscaling, CI/CD with eval gates, model registries, inference
optimisation, synthetic data generation, feature stores and lineage, cost engineering
and chargeback. Builds on Days 11, 22, 23, 24, 27.

### WEEK 12 · Capstone — Enterprise AI Assistant
**Days 78–84 · 2–8 Nov 2026** · Full Capstone (CAPSTONE)
One integrated system: RAG + Agents + Eval + Security + Cloud Deploy, defended with
ADRs, C4 diagrams, NFRs, risk assessment, deployment plan, security report.

---

## Discipline Coverage After This Change

| Discipline | Phase 1 | Phase 2 | Total dedicated days |
|------------|---------|---------|----------------------|
| Evals | D12, D21, D22, D23, D26, D27 | **Week 7 (7 days)** | 13 |
| Guardrails | D22, D25 | **Week 10 (7 days)** | 9 |
| Harness engineering | *(thin — D19 schemas only)* | **D30, D31** | 2 dedicated + W5 project |
| Loop engineering | *(mechanics — D19, D20, D24)* | **D32, D33** | 2 dedicated + W5 project |
| Context engineering | *(scattered — D17, D18, D24, D26)* | **D36, D37** | 2 dedicated + W6 project |

---

*Locked 2 August 2026. Content authority for Phase 2. Dates governed by `SCHEDULE.md`.*
