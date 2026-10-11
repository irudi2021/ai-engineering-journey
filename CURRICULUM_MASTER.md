# 📗 CURRICULUM MASTER — 12-Week AI Engineering Syllabus

> 🔒 **LOCKED 11 October 2026 — FRESH RUN.**
> **Day 1: Monday 12 October 2026 → Day 84: Sunday 3 January 2027.**
> 84 consecutive teaching days. No rest days — Christmas (Day 75) and New Year (Day 82)
> are teaching days by choice.
>
> This document is the **complete content authority** for all 12 weeks.
> Dates are governed by [`SCHEDULE.md`](SCHEDULE.md).
>
> **Syllabus composition:** an external 4-month (16-week) syllabus was merged into this
> 12-week programme on 2 August 2026 (merge revision m1). **No weeks were added.** Every
> incoming topic and every listed resource is preserved verbatim below.
>
> **2026 Currency Layer (revision u1, 11 October 2026):** every day now carries one
> 2026 addition so the course ends current to the state of AI engineering in October 2026.
> Additive only — no day title, topic or resource from m1 was changed or removed.

---

## 0. 2026 CURRENCY LAYER — What Changed in the Field and Where It Is Taught

Checked on 11 October 2026 against primary sources (listed below). Rules:

1. **Additive.** Each day keeps its m1 topic; the 2026 addition is taught inside it.
2. **Model-agnostic.** No frontier model version is hard-coded — names change monthly.
   Day 7 builds the live model landscape from official provider changelogs on the day.
3. **Verified or excluded.** Anything reported by a single unverified source was left out.

| 2026 shift | Taught on |
|------------|-----------|
| Agent = Model + Harness; harness engineering as a core skill | Days 29–33 |
| Agent Skills open standard (SKILL.md) and AGENTS.md | Days 30, 37, 80 |
| Context engineering: Write / Select / Compress / Isolate | Days 36–37 |
| MCP spec revision 2026-07-28 (stateless core, MRTR, Tasks extension) | Days 38–39 |
| MCP, goose and AGENTS.md under the Agentic AI Foundation (Linux Foundation) | Day 38 |
| A2A protocol v1.0 and MCP-vs-A2A | Days 20, 40, 42 |
| OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10) | Days 25, 41, 48, 69, 83 |
| RL with verifiable rewards (RLVR / GRPO) and reasoning models | Days 4, 5, 10, 68 |
| Prefill/decode disaggregation, llm-d, NVIDIA Dynamo, speculative decoding | Days 11, 75 |
| FP8 / FP4 quantisation formats | Day 8 |
| OpenTelemetry GenAI semantic conventions (Development status) | Days 22, 47, 74 |
| Eval-driven development and trajectory evals | Days 12, 35, 44, 49 |
| EU AI Act after the Digital Omnibus (Reg. (EU) 2026/1744) | Day 69 |
| Coding agents as the primary developer interface | Day 80 |
| Managed agent platforms on AWS, Azure and Google Cloud | Day 71 |

**Sources checked (11 Oct 2026)**

1. MCP specification 2026-07-28 changelog — `modelcontextprotocol.io/specification/2026-07-28/changelog`
2. Agentic AI Foundation formation (Linux Foundation, 9 Dec 2025) — `linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation`
3. A2A protocol one-year milestone (Linux Foundation, 9 Apr 2026) — `linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year`
4. OWASP Top 10 for Agentic Applications 2026 — `genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026`
5. Agent Skills open standard — `agentskills.io`
6. EU Digital Omnibus on AI enters into force (White & Case) — `whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act`
7. OpenTelemetry GenAI semantic conventions status (Aug 2026) — `truefoundry.com/blog/opentelemetry-genai-semantic-conventions`
8. llm-d prefill/decode disaggregation — `llm-d.ai/docs/guides/pd-disaggregation`
9. Harness engineering for coding agent users (B. Bockeler, Apr 2026) — `martinfowler.com`

---

## 1. Merge Evidence — Where the Incoming Syllabus Overlaps Weeks 1–4

Before placing anything, the incoming syllabus was measured term-by-term against the
Weeks 1–4 lesson content (measured 2 August 2026).

| Incoming block | Covered | Total | % | Verdict |
|----------------|---------|-------|---|---------|
| M2W3 Transformers & LLMs | 7 | 8 | 88% | COVERED IN WEEKS 1–4 |
| M1W2 SQL | 6 | 7 | 86% | COVERED IN WEEKS 1–4 |
| M3W3 RAG + Agentic Frameworks | 12 | 16 | 75% | COVERED IN WEEKS 1–4 |
| M4W3 Cloud Infrastructure | 9 | 12 | 75% | COVERED IN WEEKS 1–4 |
| M3W4 Production AI & Evaluation | 8 | 11 | 73% | COVERED IN WEEKS 1–4 |
| M3W2 LLM & Prompt Engineering | 10 | 14 | 71% | COVERED IN WEEKS 1–4 |
| M3W1 Software Engineering / FastAPI | 7 | 12 | 58% | PARTIAL |
| M2W3 Classical NLP | 6 | 12 | 50% | PARTIAL |
| M1W3 ML Fundamentals | 7 | 16 | 44% | PARTIAL |
| M2W1 Deep Learning / CNN | 5 | 13 | 38% | PARTIAL |
| M1W1 Python / Pandas / NumPy / OOP | 2 | 8 | 25% | **NEW** |
| M4W4 No-Code & AI Productivity Tools | 2 | 14 | 14% | **NEW** |

**Conclusion:** roughly **60% of the incoming syllabus is covered by Weeks 1–4**.
The genuine additions are classical ML, deep learning and computer vision, classical NLP,
software-engineering/FastAPI depth, named agentic frameworks, and the entire no-code /
AI-productivity block.

---

## 2. Placement Strategy — Architect's Rationale

Three moves make a 16-week syllabus fit 12 weeks without deleting anything:

**Move 1 — Deduplicate.** Topics taught to production depth in Days 1–28 are not repeated
in Weeks 5–12. They are cross-referenced to the day that teaches them, so nothing is lost
and no time is spent twice.

**Move 2 — Prerequisites become a self-study Foundations Track.** Python, Pandas, NumPy,
OOP and SQL are upstream of Day 1 — the programme assumes working Python and SQL from the
first lesson. They are preserved in full as **Track 0** with all resources, as reference
and revision material, not as teaching days.

**Move 3 — Keep Weeks 5–12 lean where Weeks 1–4 already go deep.**
Security had a full production day on Day 25 (Tier 1–4 control hierarchy, injection,
PII, tenant isolation, audit, supply chain), so Week 10 keeps red teaming and governance
but does not repeat the foundations. The same logic applies to multimodal (Day 26) and
agentic system design (Day 20).

### What was compressed, stated plainly

| Original plan | Now | Justification |
|-----------------------|-----|---------------|
| W8 Agentic System Design — 7 days | 3 days (D54–56) | Day 20 covered orchestration, pools, parallel phases |
| W9 Multimodal — 7 days | 2 days (D67–68) | Day 26 covered VLM architecture, pipelines, tables, staged eval |
| W10 Security — 7 days | 2 days (D69–70) | Day 25 covered the full Tier 1–4 control hierarchy |
| W12 Capstone — 7 days | 4 days (D81–84) | 3 days redirected to the no-code block |

**This is a real trade.** Depth in security, multimodal and system design is reduced to
create room for ML/DL/NLP foundations and the no-code block. The compressed material is
not removed — it layers on top of Days 20, 25 and 26.

---

# TRACK 0 · FOUNDATIONS (Self-Study — Not Teaching Days)

> Preserved verbatim from the incoming syllabus. Reference and revision material.
> No day numbers assigned; these are upstream of Day 1.

## Foundations Week 1 · Python Setup, Core Programming & Pandas Basics

**Topics**
- Python Installation & Environment Setup
- Explore IDEs: VS Code, Jupyter, Colab
- Jupyter Notebook Basics
- Python Basics: Syntax, Variables, Strings, Input/Output
- Loops, Functions, Conditional Statements
- Python Libraries Exploration: Pandas, NumPy, Seaborn, Plotly
- Python Data Structures: Lists, Tuples, Dictionaries, Sets
- DataFrames, Series, Indexing, Selection
- Data Input/Output
- Data Cleaning Techniques
- Handling Missing Data
- Data Visualization with Matplotlib, Seaborn, Plotly
- NumPy Arrays, Broadcasting, Indexing
- OOPS Basics, Classes, Objects, Constructors, Data Input/Output
- Inheritance, Polymorphism, Encapsulation, Abstraction

**Free Resources**
1. Python Tutorial For Beginners (13 Hours) *(AI Coach John's Material)*

**GenAI Support: ChatGPT**

## Foundations Week 2 · Structured Query Language

**Topics**
- Intro to SQL, Basic SQL syntax, data types, primary keys, and constraints
- Creating and Inserting into DB
- DQL and DML Commands and filtering data
- Aggregate Functions and Subqueries
- Group By and Joins, types of joins
- Window Functions and Stored Procedures

**Free Resources**
1. SQL Full Course (4.5 Hours) *(AI Coach John's Material)*

**GenAI Support: ChatGPT**

> **Applied in the programme:** SQL is exercised continuously in the Days 13–27
> Text-to-SQL capstone — joins, aggregates, subqueries, window functions and CTEs all
> appear in generated and validated queries.

---
---

# WEEKS 1–4 · DAYS 1–28 · LLM FOUNDATIONS → PRODUCTION
*12 October – 8 November 2026*

### Day-by-Day

| Day | Date | Topic |
|-----|------|-------|
| 1 | Mon Oct 12 | Tokenization |
| 2 | Tue Oct 13 | Embeddings |
| 3 | Wed Oct 14 | Transformer Architecture |
| 4 | Thu Oct 15 | Training Lifecycle |
| 5 | Fri Oct 16 | Scaling Laws & Prompt Engineering |
| 6 | Sat Oct 17 | Structured Output |
| 7 | Sun Oct 18 | **Week 1 Project** — Model Selection Dashboard |
| 8 | Mon Oct 19 | Quantization |
| 9 | Tue Oct 20 | LoRA & PEFT |
| 10 | Wed Oct 21 | Full Fine-Tuning |
| 11 | Thu Oct 22 | Model Serving |
| 12 | Fri Oct 23 | Evaluation |
| 13 | Sat Oct 24 | Efficiency |
| 14 | Sun Oct 25 | **Week 2 Project** — Text-to-SQL Foundation (running capstone begins) |
| 15 | Mon Oct 26 | RAG Foundations |
| 16 | Tue Oct 27 | RAG Indexing Pipelines |
| 17 | Wed Oct 28 | RAG Retrieval Deep Dive |
| 18 | Thu Oct 29 | RAG Generation & Prompt Engineering |
| 19 | Fri Oct 30 | Agents and Tool Use |
| 20 | Sat Oct 31 | Multi-Agent Systems |
| 21 | Sun Nov 1 | **Week 3 Capstone** — End-to-End Text-to-SQL |
| 22 | Mon Nov 2 | Production LLM Operations |
| 23 | Tue Nov 3 | Prompt and Model Versioning |
| 24 | Wed Nov 4 | Cost Optimization at Scale |
| 25 | Thu Nov 5 | Security and Compliance |
| 26 | Fri Nov 6 | Multi-Modal Systems |
| 27 | Sat Nov 7 | Fine-Tuning for Production |
| 28 | Sun Nov 8 | **Week 4 Capstone** — Production Hardening & Review |

**⚡ 2026 Currency Layer (u1)** — added inside each day, on top of the topic above

| Day | 2026 addition |
|-----|---------------|
| 1 | Tokenizer differences across model families; token-cost tax on non-English text (Tamil vs English) |
| 2 | Matryoshka (truncatable) embeddings; multi-vector late interaction (ColBERT); multimodal embeddings |
| 3 | Mixture-of-Experts (total vs active parameters); GQA / MLA attention; long-context mechanics |
| 4 | The 2026 post-training stack: SFT → preference optimisation (DPO) → RL with verifiable rewards (RLVR / GRPO); how reasoning models are made |
| 5 | Test-time compute scaling; reasoning-effort controls; prompting reasoning models vs classic models |
| 6 | Constrained decoding and strict JSON-Schema output modes; JSON Schema 2020-12 |
| 7 | Live 2026 model landscape (frontier vs open-weight, verified from official changelogs on the day); model churn and migration cost; model routing |
| 8 | FP8 and 4-bit floating-point formats (NVFP4 / MXFP4); KV-cache quantisation |
| 9 | QLoRA; serving many LoRA adapters on one base model (multi-LoRA) |
| 10 | RL fine-tuning: RLVR / GRPO, verifier and reward design; open tooling (TRL, verl, OpenRLHF) |
| 11 | vLLM, SGLang, TensorRT-LLM; prefill/decode disaggregation; llm-d (CNCF Sandbox, Mar 2026) and NVIDIA Dynamo; speculative decoding; prefix caching |
| 12 | Benchmark saturation and contamination; agentic benchmarks (e.g. SWE-bench Verified); building your own task evals |
| 13 | Prompt caching, batch APIs, KV-cache reuse, model cascades |
| 14 | Project add-on: eval set + cost report per candidate model |
| 15 | Decision framework: RAG vs long context vs agentic search |
| 16 | Contextual chunk enrichment; late chunking; layout-aware document parsing |
| 17 | Multi-vector retrieval; GraphRAG; query rewriting and routing |
| 18 | Grounded citations; agentic RAG (the agent decides when and what to retrieve) |
| 19 | Tool calling with reasoning models; computer-use and browser agents |
| 20 | Orchestrator-worker and sub-agent patterns; preview of the A2A protocol |
| 21 | Capstone add-on: tool-call trace review and failure taxonomy |
| 22 | OpenTelemetry GenAI semantic conventions (still 'Development' status in 2026); AI gateways |
| 23 | Prompt registries; model-deprecation and migration playbook for fast model churn |
| 24 | Prompt caching, batch inference, routing and reasoning-effort budgets as cost levers |
| 25 | OWASP Top 10 for LLM Applications (2025) + OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10, published 9 Dec 2025); indirect prompt injection |
| 26 | Real-time voice agents (speech-to-speech); video understanding |
| 27 | Distillation from frontier models; synthetic data; fine-tune vs context-engineer decision |
| 28 | Review add-on: OWASP LLM + Agentic risk mapping of the capstone |

| Week | Days | Theme |
|------|------|-------|
| 1 | 1–7 | Foundations — tokenization, embeddings, transformers, training, scaling laws, structured output, model selection |
| 2 | 8–14 | Efficiency — quantization, LoRA/PEFT, full fine-tuning, serving, evaluation, efficiency, Text-to-SQL foundation |
| 3 | 15–21 | Retrieval & Agents — RAG foundations, indexing, hybrid retrieval, generation, agents, multi-agent, capstone |
| 4 | 22–28 | Production — LLMOps, versioning, cost, security, multimodal, fine-tuning, Week 4 capstone |

### Incoming topics covered in Weeks 1–4

| Incoming topic | Taught on |
|----------------|--------------|
| Tokenization | Day 1 |
| Word Embeddings; Cosine Similarity, Semantic Search & Text Similarity | Day 2 |
| Attention Mechanism, Self-Attention & Encoder-Decoder Architecture; Transformer Architecture & Modern Language Models | Day 3 |
| Large Language Models (LLMs) & Foundation Models | Days 3–4 |
| LLM Fundamentals & Inference Pipeline | Days 4, 11 |
| Prompt Engineering Principles & Prompt Patterns; Zero-Shot, One-Shot & Few-Shot Prompting; Chain-of-Thought | Day 5 |
| Structured Outputs; Output Parsers & Schema Validation | Day 6 |
| Decoding Parameters (Temperature, Top-P, Max Tokens) | Days 5–6 |
| Function Calling & Tool Calling | Days 6, 19 |
| Retrieval-Augmented Generation (RAG); Document Loaders & Chunking Strategies | Days 15–16 |
| Embedding Models & Vector Databases | Days 15–16 |
| Semantic Search & Reranking | Day 17 |
| Agent Memory & Planning Strategies | Days 19–20 |
| Prompt Injection & Prompt Security | Days 18, 25 |
| AI Safety & Guardrails | Days 22, 25 |
| Building Production-Ready LLM Applications | Days 14, 21, 22 |
| Docker for AI Applications *(introduced)* | Day 11 |
| Context Window & Token Management *(cost framing)* | Day 24 |

### Free Resources for blocks covered in Weeks 1–4

**From M3W2 · LLM Engineering & Prompt Engineering**
1. ₹35 LPA LLM Engineer Roadmap 2026 in Tamil (Beginner to Job Ready) *(AI Coach John)*
2. Prompt Engineering Basics to Advanced: One-Shot, Two-Shot, Chain of Prompting — Tamil Full Guide *(AI Coach John)*
3. Prompt Injection Simplified in Tamil *(AI Coach John)*

**GenAI Support: ChatGPT**

**From M3W3 · RAG Systems** *(retrieval half — taught Days 15–18)*
1. 8 RAG Concepts Explained in 26 Minutes: April 2026 *(AI Coach John)*
2. Vector Database (தமிழில்) — The Why? What? How? *(AI Coach John)*
3. 8 (CHUNKING Strategies) Industries Expect You to Know *(AI Coach John)*

**GenAI Support: ChatGPT**

> *The agentic-framework half of M3W3 (LangChain, LangGraph, CrewAI, AG2/AutoGen/Agno,
> Loop Engineering & Human-in-the-Loop) is taught in Weeks 5–6; its resources are
> listed there.*

---
---

# WEEKS 5–12 · DAYS 29–84 · AGENTS → FOUNDATIONS → CLOUD → CAPSTONE
*9 November 2026 – 3 January 2027*

---

## WEEK 5 · AGENTS, HARNESS & LOOP ENGINEERING + AGENTIC FRAMEWORKS
**Days 29–35 · 9–15 November 2026**
**Project:** AI Research Agent with Tool Calling (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 29 | Mon Nov 9 | Agent Architectures Beyond ReAct |
| 30 | Tue Nov 10 | **Harness Engineering I — Tool Design** |
| 31 | Wed Nov 11 | **Harness Engineering II — Responses, Errors & Environment** |
| 32 | Thu Nov 12 | **Loop Engineering I — Termination & Budgets** |
| 33 | Fri Nov 13 | **Loop Engineering II — Recovery, Sub-Agents & Human-in-the-Loop Design** |
| 34 | Sat Nov 14 | **Agentic Frameworks I — LangChain Fundamentals & LangGraph Workflows** |
| 35 | Sun Nov 15 | **Week 5 Project** — AI Research Agent with Tool Calling |

**⚡ 2026 Currency Layer (u1)** — added inside each day, on top of the topic above

| Day | 2026 addition |
|-----|---------------|
| 29 | 'Agent = Model + Harness' (Bockeler, Thoughtworks, Apr 2026); long-horizon / deep agents; planning patterns |
| 30 | Agent Skills open standard (SKILL.md, progressive disclosure, agentskills.io); AGENTS.md project instructions |
| 31 | Sandboxing and containment for agents with shell, web and file access; least-privilege tool permissions |
| 32 | Token, time and cost budgets per run; reasoning-effort as a loop control |
| 33 | Approval gates and permission modes; interrupt / resume for human review |
| 34 | LangGraph durable execution, checkpointing and interrupts |
| 35 | Project add-on: trajectory-level eval of the research agent |

**Incoming topics absorbed:** LangChain Fundamentals · LangGraph Workflows ·
Loop Engineering & Human-in-the-Loop Design · Agent Memory & Planning Strategies *(D33, extended D41)*

**Project (from incoming M4W2):** *(Project 2)* **AI Research Agent with Tool Calling** —
Category: Agentic AI · Industry: Research Automation · YouTube search: *LangGraph AI Research Agent Project*

**Free Resources carried in**
1. Loop Engineering (தமிழ்) *(AI Coach John)*
2. Complete LangGraph Tutorial in Tamil (Free & Open Source) *(AI with Akash)*
3. LangChain for Beginners: Your First AI Agent Explained in Tamil *(AI Coach John)*

---

## WEEK 6 · CONTEXT ENGINEERING, MCP & MULTI-AGENT FRAMEWORKS
**Days 36–42 · 16–22 November 2026**
**Project:** Multi-Agent Business Analyst System (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 36 | Mon Nov 16 | **Context Engineering I — The Context Budget & Token Management** |
| 37 | Tue Nov 17 | **Context Engineering II — Compaction & Progressive Disclosure** |
| 38 | Wed Nov 18 | MCP (Model Context Protocol) Fundamentals |
| 39 | Thu Nov 19 | Building a Production MCP Server |
| 40 | Fri Nov 20 | **Agentic Frameworks II — CrewAI, AG2 / AutoGen / Agno & Multi-Agent Collaboration** |
| 41 | Sat Nov 21 | Agent Memory Architectures & Planning Strategies |
| 42 | Sun Nov 22 | **Week 6 Project** — Multi-Agent Business Analyst System |

**⚡ 2026 Currency Layer (u1)** — added inside each day, on top of the topic above

| Day | 2026 addition |
|-----|---------------|
| 36 | Context engineering framework: Write / Select / Compress / Isolate |
| 37 | Compaction, memory files and skills as progressive disclosure in practice |
| 38 | MCP spec revision 2026-07-28: stateless core (no initialize handshake, no sessions), server/discover, Multi Round-Trip Requests, Tasks extension, Roots/Sampling/Logging deprecated; MCP governed by the Agentic AI Foundation (Linux Foundation, Dec 2025) |
| 39 | MCP authorisation (OAuth, Client ID Metadata Documents), cacheable list results (ttlMs / cacheScope), OpenTelemetry trace propagation, migrating a 2025-11-25 server |
| 40 | A2A protocol v1.0 (Linux Foundation; Agent Cards, task lifecycle, JSON-RPC + gRPC); MCP vs A2A; vendor agent SDKs (OpenAI Agents SDK, Claude Agent SDK, Google ADK, Microsoft Agent Framework) |
| 41 | Long-term memory stores; memory as a tool; memory poisoning risk (OWASP Agentic) |
| 42 | Project add-on: expose one agent over A2A and its tools over MCP |

**Incoming topics absorbed:** Context Window & Token Management · MCP (Model Context
Protocol) · CrewAI & Multi-Agent Collaboration · AG2 / AutoGen / Agno Framework Overview ·
Agent Memory & Planning Strategies

**Project (from incoming M4W2):** *(Project 3)* **Multi-Agent Business Analyst System** —
Category: Multi-Agent AI · Industry: Business Intelligence · YouTube search: *CrewAI Multi Agent Project*

**Free Resources carried in**
1. MCP Crash Course (2 Hours) *(AI Coach John)*
2. Build AI Agents with Crew AI Framework *(AI with Thiru)*
3. Autogen Agentic AI Framework *(Aai Tech)*

---

## WEEK 7 · PRODUCTION AI SYSTEMS, EVALUATION & OBSERVABILITY
**Days 43–49 · 23–29 November 2026**
**Project:** Eval & Observability Platform (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 43 | Mon Nov 23 | **AI System Architecture & Orchestration** |
| 44 | Tue Nov 24 | LLM-as-a-Judge & Eval Harness Design |
| 45 | Wed Nov 25 | **Hallucination Detection & Evaluation** |
| 46 | Thu Nov 26 | **RAG Evaluation — RAGAS & TruLens** |
| 47 | Fri Nov 27 | **LangSmith for Debugging & Observability** |
| 48 | Sat Nov 28 | **AI Safety & Guardrails in Production** |
| 49 | Sun Nov 29 | **Week 7 Project** — Eval & Observability Platform |

**⚡ 2026 Currency Layer (u1)** — added inside each day, on top of the topic above

| Day | 2026 addition |
|-----|---------------|
| 43 | Reference architecture: gateway → guardrails → orchestrator → tools → observability |
| 44 | Eval-driven development; golden datasets; agent trajectory and tool-use evals |
| 45 | Groundedness and citation checks; uncertainty signals |
| 46 | Agentic RAG evaluation (retrieval decisions, not just answers) |
| 47 | Vendor-neutral tracing with OpenTelemetry GenAI conventions alongside LangSmith (Langfuse, Arize Phoenix) |
| 48 | Guardrails mapped to OWASP Agentic risks; runtime policy enforcement |
| 49 | Project add-on: CI eval gate that blocks a regression |

**Incoming topics absorbed:** AI System Architecture & Orchestration · LangSmith for
Debugging & Observability · AI Safety & Guardrails · Hallucination Detection &
Evaluation · RAG Evaluation (RAGAS, TruLens)

---

## WEEK 8 · AI APPLICATION ENGINEERING & AGENTIC SYSTEM DESIGN
**Days 50–56 · 30 November – 6 December 2026**
**Project:** End-to-End AI Backend + Scalable Agent Runtime (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 50 | Mon Nov 30 | **AI Application Architecture · REST APIs, HTTP Methods & API Integration · JSON, JSON Schema & Structured Data** |
| 51 | Tue Dec 1 | **FastAPI Fundamentals & API Development · Request Handling, Response Models & Error Handling** |
| 52 | Wed Dec 2 | **Authentication, API Keys & Environment Variables · File Uploads, Streaming Responses & Async APIs** |
| 53 | Thu Dec 3 | **Database Integration (SQLite/PostgreSQL Basics) · AI API Integration (OpenAI, Gemini, Claude)** |
| 54 | Fri Dec 4 | Agentic System Design — Runtime, State Management & Queueing |
| 55 | Sat Dec 5 | Scaling, Backpressure, Failure Isolation & Concurrency |
| 56 | Sun Dec 6 | **Week 8 Project** — End-to-End AI Backend Development using FastAPI + Scalable Agent Runtime |

**⚡ 2026 Currency Layer (u1)** — added inside each day, on top of the topic above

| Day | 2026 addition |
|-----|---------------|
| 50 | Streaming tool-call events; structured outputs at the API boundary |
| 51 | Async FastAPI patterns for long-running LLM calls |
| 52 | Server-Sent Events streaming; secrets management for model API keys |
| 53 | Multi-provider abstraction and fallbacks; provider-native MCP connectors |
| 54 | Durable execution for long-running agents (workflow engines such as Temporal); resumable state |
| 55 | Rate limits, retries with jitter, circuit breakers for model providers |
| 56 | Project add-on: provider failover drill |

**Incoming topics absorbed — the complete M3W1 block:** Introduction to AI Application
Architecture · REST APIs, HTTP Methods & API Integration · JSON, JSON Schema & Structured
Data · FastAPI Fundamentals & API Development · Authentication, API Keys & Environment
Variables · Request Handling, Response Models & Error Handling · File Uploads, Streaming
Responses & Async APIs · Database Integration (SQLite/PostgreSQL Basics) · AI API
Integration (OpenAI, Gemini, Claude) · End-to-End AI Backend Development using FastAPI

**Free Resources carried in**
1. API — Step by Step — Build, Secure and Deploy | Full Practical Guide *(Applied with AI)*
2. Complete FastAPI Tutorial in Tamil — Build your own RestAPI *(AI with Akash)*

---

## WEEK 9 · MACHINE LEARNING & DEEP LEARNING FOUNDATIONS
**Days 57–63 · 7–13 December 2026**
**Project:** ML & DL Project Development & Deployment (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 57 | Mon Dec 7 | **ML Fundamentals — Types of ML (Supervised, Unsupervised & Reinforcement) · Features, Labels, Training/Testing Data & Train/Test Split · Classification, Regression & Clustering Algorithms** |
| 58 | Tue Dec 8 | **Model Validation using Cross-Validation · Evaluation Metrics: Accuracy, Precision, Recall, F1-Score & ROC-AUC · Confusion Matrix & Handling Class Imbalance** |
| 59 | Wed Dec 9 | **Overfitting, Underfitting & Regularization · Feature Engineering & Data Preprocessing · Feature Scaling, Normalization & Data Preparation · End-to-End ML Workflow using Scikit-learn** |
| 60 | Thu Dec 10 | **Deep Learning Fundamentals — Neural Networks & Perceptron · Activation Functions, Loss Functions & Optimizers · Forward Propagation, Backward Propagation & Gradient Descent** |
| 61 | Fri Dec 11 | **Epochs, Batch Size, Learning Rate & Hyperparameter Tuning · Batch Normalization, Dropout & Vanishing Gradient Problem** |
| 62 | Sat Dec 12 | **CNNs & Image Classification · Pretrained Models, Transfer Learning & Fine-Tuning · SOTA Models & Modern DL Applications · End-to-End Model Development using TensorFlow/Keras or PyTorch** |
| 63 | Sun Dec 13 | **Week 9 Project** — ML & DL Project Development & Deployment |

**⚡ 2026 Currency Layer (u1)** — added inside each day, on top of the topic above

| Day | 2026 addition |
|-----|---------------|
| 57 | Where classical ML still runs FAANG-scale systems (ranking, recommendations, fraud) |
| 58 | Metric choice for imbalanced production data |
| 59 | Data leakage and train/serve skew |
| 60 | From perceptron to transformer: the same gradient-descent engine |
| 61 | Mixed-precision training basics (FP16 / BF16) |
| 62 | Vision Transformers (ViT) and diffusion models in context |
| 63 | Project add-on: model card for each project |

**Incoming topics absorbed — the complete M1W3 and M2W1 blocks.**

### Week 9 Project Set — preserved verbatim

**ML Project Development & Deployment** *(incoming M1W4)*

| Project Title | Category | Industry / Application |
|---------------|----------|------------------------|
| Predictive Maintenance for Industrial Equipment | Regression | Manufacturing / Industry 4.0 |
| Credit Risk Assessment & Loan Default Prediction | Classification | Banking & FinTech |
| Customer Segmentation using K-Means & DBSCAN | Clustering | Retail / E-Commerce / Marketing |

**DL Project Development & Deployment (Image/Video)** *(incoming M2W2)*

| Project Title | Category | Industry / Application |
|---------------|----------|------------------------|
| Brain Tumor Detection & Segmentation using U-Net + CNN | Image Classification / Segmentation | Healthcare / Medical AI |
| Video Anomaly Detection for Smart Surveillance | Video Classification / Anomaly Detection | Smart Cities / Security |

**Free Resources carried in**
1. Machine Learning (தமிழில்) in 25 Minutes: Absolute Beginner Crash Course *(AI Coach John's Material)*
2. Industry-Standard AI, Data Science & Machine Learning Full Course in Tamil for Beginners *(Hire Ready)*
3. AI/ML (தமிழில்): Complete Deep Learning RoadMap Explained in 15 Mins *(AI Coach John's Material)*
4. Deep Learning Series in Tamil *(Adi Explains)*

---

## WEEK 10 · NLP, MULTIMODAL, REASONING & RED TEAMING
**Days 64–70 · 14–20 December 2026**
**Project:** NLP & Multimodal Projects + Red Team Assessment (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 64 | Mon Dec 14 | **NLP Foundations — Introduction to NLP & Text Preprocessing · Tokenization, Stop Words, Stemming & Lemmatization** |
| 65 | Tue Dec 15 | **Bag of Words (BoW), Count Vectorizer & TF-IDF · N-Grams, POS Tagging & Named Entity Recognition (NER)** |
| 66 | Wed Dec 16 | **Word Embeddings: Word2Vec, GloVe & Vector Embeddings · End-to-End NLP Pipeline using Hugging Face Transformers** |
| 67 | Thu Dec 17 | Vision-Language Models, OCR Pipelines & Document Understanding at Scale |
| 68 | Fri Dec 18 | Chart & Diagram Reasoning · Reasoning Models & Test-Time Compute |
| 69 | Sat Dec 19 | Red Teaming, OWASP LLM Top 10 & Responsible AI Governance |
| 70 | Sun Dec 20 | **Week 10 Project** — NLP & Multimodal Projects + Red Team Assessment |

**⚡ 2026 Currency Layer (u1)** — added inside each day, on top of the topic above

| Day | 2026 addition |
|-----|---------------|
| 64 | Why classical preprocessing still matters before LLM pipelines (cost, PII scrubbing) |
| 65 | Classical NER vs LLM extraction: cost and accuracy trade-off |
| 66 | Hugging Face Hub model selection; small open models for on-device and edge |
| 67 | Document AI with vision-language models replacing OCR-only pipelines |
| 68 | Reasoning models in production: effort settings, latency/cost trade-offs, when not to use them |
| 69 | EU AI Act after the Digital Omnibus (Reg. (EU) 2026/1744, in force 27 Jul 2026): Annex III high-risk → 2 Dec 2027, Annex I → 2 Aug 2028, Art. 50 transparency still from Aug 2026; NIST AI RMF; ISO/IEC 42001; OWASP Agentic red-team cases |
| 70 | Project add-on: red-team agent tool misuse, not only prompt injection |

**Incoming topics absorbed — the complete M2W3 classical-NLP block.**
*(Attention, self-attention, encoder-decoder, transformers, LLMs, foundation models,
cosine similarity and semantic search from the same block are taught on Days 2–4.)*

### Week 10 Project Set — preserved verbatim

**NLP Projects & Deployment** *(incoming M2W4)*

| Project Title | Category | Industry / Application |
|---------------|----------|------------------------|
| AI Resume Screening & Candidate Matching System | NLP + Semantic Search | HRTech / Recruitment |
| Legal Document Question Answering using RAG | LLM + RAG | LegalTech / Enterprise AI |
| Intelligent Customer Support Chatbot with Vector Search | Conversational AI + LLM | Customer Support / SaaS |

**Also this week:** Multimodal Document Processor · Red Team Your Own RAG System
(20+ adversarial prompts, guardrails blocking ≥90%, written security assessment with risk
ratings and residual-risk acceptance).

**Free Resources carried in**
1. What is NLP? Beginners to Advanced RoadMap 2025 in Tamil *(AI Coach John's Material)*
2. NLP Playlist *(Chill and Grow)*

---

## WEEK 11 · CLOUD DEPLOYMENT, AI INFRASTRUCTURE & LLMOPS
**Days 71–77 · 21–27 December 2026**
**Project:** Deploy a Production-Ready AI Service (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 71 | Mon Dec 21 | **Introduction to AWS, Azure & Google Cloud Platform · Compute Services (EC2, Azure VM, Compute Engine) · Storage Services (S3, Blob Storage, Cloud Storage)** |
| 72 | Tue Dec 22 | **Docker Fundamentals & Containerization · Docker for AI Applications** |
| 73 | Wed Dec 23 | **Deploying FastAPI Applications · Deploying AI Applications on Cloud · Serverless AI Deployments** |
| 74 | Thu Dec 24 | **CI/CD Basics for AI Applications · Monitoring & Logging · Cost Optimization & Cloud Best Practices** |
| 75 | Fri Dec 25 | LLMOps — Model Registries, Automated Eval Gates & Inference Optimisation (TensorRT-LLM, ONNX) |
| 76 | Sat Dec 26 | Synthetic Data Generation (Self-Instruct, Evol-Instruct) · Feature Stores & Data Lineage · Cost Engineering & Chargeback |
| 77 | Sun Dec 27 | **Week 11 Project** — Deploy a Production-Ready AI Service |

**⚡ 2026 Currency Layer (u1)** — added inside each day, on top of the topic above

| Day | 2026 addition |
|-----|---------------|
| 71 | Managed agent platforms: Amazon Bedrock AgentCore, Microsoft Azure AI Foundry, Google Vertex AI agent tooling |
| 72 | GPU containers and model-weight caching |
| 73 | Serverless GPU inference; cold-start trade-offs |
| 74 | Eval gates inside CI/CD; OpenTelemetry-based AI monitoring |
| 75 | Kubernetes-native inference (llm-d, NVIDIA Dynamo) and prefill/decode disaggregation at scale |
| 76 | Synthetic data for evals and RL environments; verifier quality as the ceiling |
| 77 | Project add-on: cost-per-request dashboard |

**Incoming topics absorbed — the complete M4W3 block plus M3W4's Docker and Cloud Deployment.**

**Free Resources carried in**
1. AWS in Half Hour | Learn EC2 Basics in Tamil *(Tamil Coding / AWS Tamil)*
2. What is Docker? Explained in Tamil | Full Tutorial + Demo *(Arivi by HCL GUVI)*
3. AWS EC2 vs Azure Virtual Machine (தமிழில்) *(K. Mohamed Faizal)*
4. Docker & Containerization in Tamil *(Arivi by HCL GUVI)*
5. AWS for Beginners in Tamil Playlist *(Tamil Coding)*
6. Azure Fundamentals in Tamil *(K. Mohamed Faizal)*
7. Google Cloud Platform (GCP) in Tamil *(Tamil Cloud / Community Resources)*
8. CI/CD Pipeline in Tamil *(DevOps Tamil)*
9. FastAPI Deployment using Docker & Cloud *(English — Recommended if Tamil is unavailable)*
10. Deploying AI Applications on AWS using FastAPI & Docker *(English — Advanced)*
11. Dockers for Beginners *(Simply Byte)*

---

## WEEK 12 · NO-CODE AI PLATFORMS & ENTERPRISE CAPSTONE
**Days 78–84 · 28 December 2026 – 3 January 2027**
**Project:** Enterprise AI Assistant (CAPSTONE)

| Day | Date | Topic |
|-----|------|-------|
| 78 | Mon Dec 28 | **Introduction to No-Code & Low-Code AI Platforms · Claude Projects & Claude Artifacts · ChatGPT Projects, GPTs & Canvas** |
| 79 | Tue Dec 29 | **Microsoft Copilot & Microsoft 365 Copilot · Microsoft Copilot Studio & AI Agents (Basics) · Google Gemini Workspace & Gems** |
| 80 | Wed Dec 30 | **AI Workflow Automation using n8n (Introduction) · AI Coding Assistants (GitHub Copilot, Cursor & Windsurf) · Rapid AI Prototyping & Business Use Cases · Choosing Between No-Code, Low-Code & Custom AI Development** |
| 81 | Thu Dec 31 | **Capstone I** — Architecture, ADRs & C4 Diagrams |
| 82 | Fri Jan 1 | **Capstone II** — Build & Integration |
| 83 | Sat Jan 2 | **Capstone III** — Evaluation, Security & Deployment |
| 84 | Sun Jan 3 | **Capstone IV** — Enterprise AI Assistant Final Defence |

**⚡ 2026 Currency Layer (u1)** — added inside each day, on top of the topic above

| Day | 2026 addition |
|-----|---------------|
| 78 | Agent builders inside productivity suites; when no-code agents are enough |
| 79 | Enterprise agent governance in Microsoft 365 / Google Workspace |
| 80 | Coding agents as the main developer interface (Claude Code, OpenAI Codex, GitHub Copilot agent mode, Cursor); Agent Skills and AGENTS.md in a real repo |
| 81 | ADRs for MCP, A2A, model routing and eval-gate choices |
| 82 | Build with MCP tools, Agent Skills and OpenTelemetry tracing |
| 83 | Eval gate + OWASP LLM/Agentic mapping + EU AI Act risk classification |
| 84 | Final defence + State of AI Engineering 2026 → 2027 outlook |

**Incoming topics absorbed — the complete M4W4 block.**

### Capstone Project — incoming Enterprise Project 1

| Project Title | Category | Industry / Application | YouTube Search |
|---------------|----------|------------------------|----------------|
| *(Project 1)* **Enterprise Multi-Document RAG Assistant** | RAG + LangChain | Enterprise Knowledge Management | Enterprise RAG LangChain LangGraph Project |

### Capstone Required Deliverables

1. **Architecture Decision Records (ADRs)** for every major choice (vector DB, model, framework, cloud)
2. **C4 System Diagrams** — Context, Container, Component, Code
3. **Non-Functional Requirements** — latency SLAs, availability, cost/request, scaling limits
4. **Risk Assessment** — failure modes, guardrail-bypass scenarios, residual risk
5. **Deployment Plan** — blue-green strategy, rollback, monitoring dashboards
6. **Security Report** — red-team results, guardrail coverage, compliance mapping

**Free Resources carried in**
1. Claude Projects & Claude Artifacts (தமிழில்) *(AI Coach John)*
2. Google Gemini Workspace & Gems (தமிழில்) *(AI Coach John)*
3. Microsoft Copilot & Microsoft 365 Copilot (தமிழில்) *(K. Mohamed Faizal)*
4. Microsoft Copilot Studio & AI Agents (Basics) *(English — Microsoft Official)*
5. AI Workflow Automation using n8n (தமிழில்)
6. AI Workflow Automation using n8n (தமிழில்) — Part 2
7. GitHub Copilot (தமிழில்) *(Tamil Tech / Tamil Coding Community)*

---
---

## 3. Complete Placement Index — Every Incoming Block

| Incoming | Title | Placed at |
|----------|-------|-----------|
| **M1W1** | Python Setup, Core Programming & Pandas Basics | **Track 0** (self-study) |
| **M1W2** | Structured Query Language | **Track 0** (self-study); applied Days 13–27 |
| **M1W3** | Machine Learning Fundamentals & Core Concepts | **Days 57–59** |
| **M1W4** | ML Project Development & Deployment | **Day 63** |
| **M2W1** | Deep Learning Fundamentals & Neural Networks | **Days 60–62** |
| **M2W2** | DL Project Development & Deployment (Image/Video) | **Day 63** |
| **M2W3** | NLP & Large Language Models | **Days 64–66** (classical) + Days 1–4 (transformers/LLMs) |
| **M2W4** | NLP Projects & Deployment | **Day 70** |
| **M3W1** | Software Engineering Foundations for AI Applications | **Days 50–53** |
| **M3W2** | LLM Engineering & Prompt Engineering | Days 4–6, 18, 25 + **Day 36** (token mgmt) |
| **M3W3** | RAG Systems & Agentic AI Frameworks | Days 15–20 + **Days 33, 34, 40, 41** (frameworks, loop, HITL) |
| **M3W4** | Production AI Systems, Evaluation & Deployment | **Days 43–48**, 72, 73 |
| **M4W1** | Enterprise AI Project Development — 1 | **Week 12 Capstone** |
| **M4W2** | Enterprise AI Project Development — 2 | **Days 35, 42** |
| **M4W3** | Cloud Deployment & AI Infrastructure | **Days 71–74** |
| **M4W4** | No-Code AI Platforms & AI Productivity Tools | **Days 78–80** |

**Every incoming block is placed. Nothing dropped. No weeks added.**

---

## 4. Project Ladder

| Week | Project | Type |
|------|---------|------|
| 01 | Model Selection Dashboard | MINI |
| 02 | Domain Fine-Tune + Quantize | PORTFOLIO |
| 03 | End-to-End Text-to-SQL | **CAPSTONE** |
| 04 | Production Hardening & Review | PORTFOLIO |
| 05 | AI Research Agent with Tool Calling | PORTFOLIO |
| 06 | Multi-Agent Business Analyst System | PORTFOLIO |
| 07 | Eval & Observability Platform | PORTFOLIO |
| 08 | End-to-End AI Backend + Scalable Agent Runtime | PORTFOLIO |
| 09 | ML & DL Project Development (5 projects) | PORTFOLIO |
| 10 | NLP & Multimodal Projects + Red Team Assessment (3 projects) | PORTFOLIO |
| 11 | Deploy a Production-Ready AI Service | PORTFOLIO |
| 12 | Enterprise Multi-Document RAG Assistant | **CAPSTONE** |

**13 named projects** across the programme.

---

## 5. Daily Protocol

1. **Teach** the day's topic fully in chat — concept-first, plain English, FAANG examples, Architect's Lens, hands-on exercises
2. **Eagle Eye** — two-pass verification; never declare a gap without snip verification, never declare coverage without confirmation
3. **PDF** → `~/Desktop/AI-ML/WeekN_DayNN_TopicName.pdf`
4. **Push** → `week-NN/notes/` on the GitHub repository

**FAANG rule (locked):** examples use only Meta, Apple, Amazon, Netflix, Google, Microsoft.
**GenAI Support:** ChatGPT *(as noted throughout the incoming syllabus)*

---

*Locked 11 October 2026 — fresh run, Day 1 = Mon 12 Oct 2026, Day 84 = Sun 3 Jan 2027.
Content merge revision m1 (2 Aug 2026) + 2026 Currency Layer u1 (11 Oct 2026). Complete content authority for Weeks 1–12.
Dates governed by `SCHEDULE.md`.*
