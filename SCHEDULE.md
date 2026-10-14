# 📅 SCHEDULE — LOCKED

> **This file is the single source of truth for all dates.**
> If any other document disagrees with this file, this file wins.
> Content authority: 📗 [`CURRICULUM_MASTER.md`](CURRICULUM_MASTER.md).

**Status:** 🔒 **LOCKED — 14 October 2026 · FRESH RUN**

---

## The Run in One Line

**Day 1: Monday, 19 October 2026 → Day 84: Sunday, 10 January 2027 — 84 consecutive teaching days, no rest days.**

---

## Key Dates

| Milestone | Date | Day |
|-----------|------|-----|
| **Start** | **Monday, 19 October 2026** | **Day 1** |
| End of Week 4 | Sunday, 15 November 2026 | Day 28 |
| Christmas — teaching day | Friday, 25 December 2026 | Day 68 |
| New Year — teaching day | Friday, 1 January 2027 | Day 75 |
| **End** | **Sunday, 10 January 2027** | **Day 84** |

Every week runs Monday–Sunday. No pauses, no rest days — Christmas and New Year are
teaching days by choice.

---

## Week Overview

| Week | Days | Dates | Theme | Project |
|------|------|-------|-------|---------|
| 01 | 1–7 | Oct 19–25 | Foundations — LLM internals | Model Selection Dashboard (MINI) |
| 02 | 8–14 | Oct 26–Nov 1 | Efficiency — quantization, fine-tuning, serving | Domain Fine-Tune + Quantize (PORTFOLIO) |
| 03 | 15–21 | Nov 2–8 | Retrieval & Agents — RAG, agents, multi-agent | End-to-End Text-to-SQL (CAPSTONE) |
| 04 | 22–28 | Nov 9–15 | Production — LLMOps, versioning, cost, security, multimodal | Production Hardening & Review (PORTFOLIO) |
| 05 | 29–35 | Nov 16–22 | Agents, Harness & Loop Engineering + Agentic Frameworks | AI Research Agent with Tool Calling (PORTFOLIO) |
| 06 | 36–42 | Nov 23–29 | Context Engineering, MCP & Multi-Agent Frameworks | Multi-Agent Business Analyst System (PORTFOLIO) |
| 07 | 43–49 | Nov 30–Dec 6 | Production AI Systems, Evaluation & Observability | Eval & Observability Platform (PORTFOLIO) |
| 08 | 50–56 | Dec 7–13 | AI Application Engineering (FastAPI) & Agentic System Design | End-to-End AI Backend + Agent Runtime (PORTFOLIO) |
| 09 | 57–63 | Dec 14–20 | Machine Learning & Deep Learning Foundations | ML & DL Project Development — 5 projects (PORTFOLIO) |
| 10 | 64–70 | Dec 21–27 | NLP, Multimodal, Reasoning & Red Teaming | NLP & Multimodal Projects + Red Team — 3 projects (PORTFOLIO) |
| 11 | 71–77 | Dec 28–Jan 3 | Cloud Deployment, AI Infrastructure & LLMOps | Deploy a Production-Ready AI Service (PORTFOLIO) |
| 12 | 78–84 | Jan 4–10 | No-Code AI Platforms & Enterprise Capstone | Enterprise Multi-Document RAG Assistant (CAPSTONE) |

**Track 0 (self-study, not teaching days):** Python, Pandas, NumPy, OOP & SQL —
preserved in full in `CURRICULUM_MASTER.md`.

---

## Day-by-Day

Each day: the core topic plus its **⚡ 2026 addition** (Currency Layer u1, verified 11 Oct 2026).

### Week 01 · Foundations — LLM internals — Days 1–7 · Mon 19 Oct – Sun 25 Oct 2026

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 1 | Mon Oct 19 | Tokenization | Tokenizer differences across model families; token-cost tax on non-English text (Tamil vs English) |
| 2 | Tue Oct 20 | Embeddings | Matryoshka (truncatable) embeddings; multi-vector late interaction (ColBERT); multimodal embeddings |
| 3 | Wed Oct 21 | Transformer Architecture | Mixture-of-Experts (total vs active parameters); GQA / MLA attention; long-context mechanics |
| 4 | Thu Oct 22 | Training Lifecycle | The 2026 post-training stack: SFT → preference optimisation (DPO) → RL with verifiable rewards (RLVR / GRPO); how reasoning models are made |
| 5 | Fri Oct 23 | Scaling Laws & Prompt Engineering | Test-time compute scaling; reasoning-effort controls; prompting reasoning models vs classic models |
| 6 | Sat Oct 24 | Structured Output | Constrained decoding and strict JSON-Schema output modes; JSON Schema 2020-12 |
| 7 | Sun Oct 25 | **Week 1 Project** — Model Selection Dashboard | Live 2026 model landscape (frontier vs open-weight, verified from official changelogs on the day); model churn and migration cost; model routing |

### Week 02 · Efficiency — quantization, fine-tuning, serving — Days 8–14 · Mon 26 Oct – Sun 1 Nov 2026

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 8 | Mon Oct 26 | Quantization | FP8 and 4-bit floating-point formats (NVFP4 / MXFP4); KV-cache quantisation |
| 9 | Tue Oct 27 | LoRA & PEFT | QLoRA; serving many LoRA adapters on one base model (multi-LoRA) |
| 10 | Wed Oct 28 | Full Fine-Tuning | RL fine-tuning: RLVR / GRPO, verifier and reward design; open tooling (TRL, verl, OpenRLHF) |
| 11 | Thu Oct 29 | Model Serving | vLLM, SGLang, TensorRT-LLM; prefill/decode disaggregation; llm-d (CNCF Sandbox, Mar 2026) and NVIDIA Dynamo; speculative decoding; prefix caching |
| 12 | Fri Oct 30 | Evaluation | Benchmark saturation and contamination; agentic benchmarks (e.g. SWE-bench Verified); building your own task evals |
| 13 | Sat Oct 31 | Efficiency | Prompt caching, batch APIs, KV-cache reuse, model cascades |
| 14 | Sun Nov 1 | **Week 2 Project** — Text-to-SQL Foundation (running capstone begins) | Project add-on: eval set + cost report per candidate model |

### Week 03 · Retrieval & Agents — RAG, agents, multi-agent — Days 15–21 · Mon 2 Nov – Sun 8 Nov 2026

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 15 | Mon Nov 2 | RAG Foundations | Decision framework: RAG vs long context vs agentic search |
| 16 | Tue Nov 3 | RAG Indexing Pipelines | Contextual chunk enrichment; late chunking; layout-aware document parsing |
| 17 | Wed Nov 4 | RAG Retrieval Deep Dive | Multi-vector retrieval; GraphRAG; query rewriting and routing |
| 18 | Thu Nov 5 | RAG Generation & Prompt Engineering | Grounded citations; agentic RAG (the agent decides when and what to retrieve) |
| 19 | Fri Nov 6 | Agents and Tool Use | Tool calling with reasoning models; computer-use and browser agents |
| 20 | Sat Nov 7 | Multi-Agent Systems | Orchestrator-worker and sub-agent patterns; preview of the A2A protocol |
| 21 | Sun Nov 8 | **Week 3 Capstone** — End-to-End Text-to-SQL | Capstone add-on: tool-call trace review and failure taxonomy |

### Week 04 · Production — LLMOps, versioning, cost, security, multimodal — Days 22–28 · Mon 9 Nov – Sun 15 Nov 2026

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 22 | Mon Nov 9 | Production LLM Operations | OpenTelemetry GenAI semantic conventions (still 'Development' status in 2026); AI gateways |
| 23 | Tue Nov 10 | Prompt and Model Versioning | Prompt registries; model-deprecation and migration playbook for fast model churn |
| 24 | Wed Nov 11 | Cost Optimization at Scale | Prompt caching, batch inference, routing and reasoning-effort budgets as cost levers |
| 25 | Thu Nov 12 | Security and Compliance | OWASP Top 10 for LLM Applications (2025) + OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10, published 9 Dec 2025); indirect prompt injection |
| 26 | Fri Nov 13 | Multi-Modal Systems | Real-time voice agents (speech-to-speech); video understanding |
| 27 | Sat Nov 14 | Fine-Tuning for Production | Distillation from frontier models; synthetic data; fine-tune vs context-engineer decision |
| 28 | Sun Nov 15 | **Week 4 Capstone** — Production Hardening & Review | Review add-on: OWASP LLM + Agentic risk mapping of the capstone |

### Week 05 · Agents, Harness & Loop Engineering + Agentic Frameworks — Days 29–35 · Mon 16 Nov – Sun 22 Nov 2026

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 29 | Mon Nov 16 | Agent Architectures Beyond ReAct | 'Agent = Model + Harness' (Bockeler, Thoughtworks, Apr 2026); long-horizon / deep agents; planning patterns |
| 30 | Tue Nov 17 | **Harness Engineering I — Tool Design** | Agent Skills open standard (SKILL.md, progressive disclosure, agentskills.io); AGENTS.md project instructions |
| 31 | Wed Nov 18 | **Harness Engineering II — Responses, Errors & Environment** | Sandboxing and containment for agents with shell, web and file access; least-privilege tool permissions |
| 32 | Thu Nov 19 | **Loop Engineering I — Termination & Budgets** | Token, time and cost budgets per run; reasoning-effort as a loop control |
| 33 | Fri Nov 20 | **Loop Engineering II — Recovery, Sub-Agents & Human-in-the-Loop Design** | Approval gates and permission modes; interrupt / resume for human review |
| 34 | Sat Nov 21 | **Agentic Frameworks I — LangChain Fundamentals & LangGraph Workflows** | LangGraph durable execution, checkpointing and interrupts |
| 35 | Sun Nov 22 | **Week 5 Project** — AI Research Agent with Tool Calling | Project add-on: trajectory-level eval of the research agent |

### Week 06 · Context Engineering, MCP & Multi-Agent Frameworks — Days 36–42 · Mon 23 Nov – Sun 29 Nov 2026

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 36 | Mon Nov 23 | **Context Engineering I — The Context Budget & Token Management** | Context engineering framework: Write / Select / Compress / Isolate |
| 37 | Tue Nov 24 | **Context Engineering II — Compaction & Progressive Disclosure** | Compaction, memory files and skills as progressive disclosure in practice |
| 38 | Wed Nov 25 | MCP (Model Context Protocol) Fundamentals | MCP spec revision 2026-07-28: stateless core (no initialize handshake, no sessions), server/discover, Multi Round-Trip Requests, Tasks extension, Roots/Sampling/Logging deprecated; MCP governed by the Agentic AI Foundation (Linux Foundation, Dec 2025) |
| 39 | Thu Nov 26 | Building a Production MCP Server | MCP authorisation (OAuth, Client ID Metadata Documents), cacheable list results (ttlMs / cacheScope), OpenTelemetry trace propagation, migrating a 2025-11-25 server |
| 40 | Fri Nov 27 | **Agentic Frameworks II — CrewAI, AG2 / AutoGen / Agno & Multi-Agent Collaboration** | A2A protocol v1.0 (Linux Foundation; Agent Cards, task lifecycle, JSON-RPC + gRPC); MCP vs A2A; vendor agent SDKs (OpenAI Agents SDK, Claude Agent SDK, Google ADK, Microsoft Agent Framework) |
| 41 | Sat Nov 28 | Agent Memory Architectures & Planning Strategies | Long-term memory stores; memory as a tool; memory poisoning risk (OWASP Agentic) |
| 42 | Sun Nov 29 | **Week 6 Project** — Multi-Agent Business Analyst System | Project add-on: expose one agent over A2A and its tools over MCP |

### Week 07 · Production AI Systems, Evaluation & Observability — Days 43–49 · Mon 30 Nov – Sun 6 Dec 2026

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 43 | Mon Nov 30 | **AI System Architecture & Orchestration** | Reference architecture: gateway → guardrails → orchestrator → tools → observability |
| 44 | Tue Dec 1 | LLM-as-a-Judge & Eval Harness Design | Eval-driven development; golden datasets; agent trajectory and tool-use evals |
| 45 | Wed Dec 2 | **Hallucination Detection & Evaluation** | Groundedness and citation checks; uncertainty signals |
| 46 | Thu Dec 3 | **RAG Evaluation — RAGAS & TruLens** | Agentic RAG evaluation (retrieval decisions, not just answers) |
| 47 | Fri Dec 4 | **LangSmith for Debugging & Observability** | Vendor-neutral tracing with OpenTelemetry GenAI conventions alongside LangSmith (Langfuse, Arize Phoenix) |
| 48 | Sat Dec 5 | **AI Safety & Guardrails in Production** | Guardrails mapped to OWASP Agentic risks; runtime policy enforcement |
| 49 | Sun Dec 6 | **Week 7 Project** — Eval & Observability Platform | Project add-on: CI eval gate that blocks a regression |

### Week 08 · AI Application Engineering (FastAPI) & Agentic System Design — Days 50–56 · Mon 7 Dec – Sun 13 Dec 2026

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 50 | Mon Dec 7 | **AI Application Architecture · REST APIs, HTTP Methods & API Integration · JSON, JSON Schema & Structured Data** | Streaming tool-call events; structured outputs at the API boundary |
| 51 | Tue Dec 8 | **FastAPI Fundamentals & API Development · Request Handling, Response Models & Error Handling** | Async FastAPI patterns for long-running LLM calls |
| 52 | Wed Dec 9 | **Authentication, API Keys & Environment Variables · File Uploads, Streaming Responses & Async APIs** | Server-Sent Events streaming; secrets management for model API keys |
| 53 | Thu Dec 10 | **Database Integration (SQLite/PostgreSQL Basics) · AI API Integration (OpenAI, Gemini, Claude)** | Multi-provider abstraction and fallbacks; provider-native MCP connectors |
| 54 | Fri Dec 11 | Agentic System Design — Runtime, State Management & Queueing | Durable execution for long-running agents (workflow engines such as Temporal); resumable state |
| 55 | Sat Dec 12 | Scaling, Backpressure, Failure Isolation & Concurrency | Rate limits, retries with jitter, circuit breakers for model providers |
| 56 | Sun Dec 13 | **Week 8 Project** — End-to-End AI Backend Development using FastAPI + Scalable Agent Runtime | Project add-on: provider failover drill |

### Week 09 · Machine Learning & Deep Learning Foundations — Days 57–63 · Mon 14 Dec – Sun 20 Dec 2026

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 57 | Mon Dec 14 | **ML Fundamentals — Types of ML (Supervised, Unsupervised & Reinforcement) · Features, Labels, Training/Testing Data & Train/Test Split · Classification, Regression & Clustering Algorithms** | Where classical ML still runs FAANG-scale systems (ranking, recommendations, fraud) |
| 58 | Tue Dec 15 | **Model Validation using Cross-Validation · Evaluation Metrics: Accuracy, Precision, Recall, F1-Score & ROC-AUC · Confusion Matrix & Handling Class Imbalance** | Metric choice for imbalanced production data |
| 59 | Wed Dec 16 | **Overfitting, Underfitting & Regularization · Feature Engineering & Data Preprocessing · Feature Scaling, Normalization & Data Preparation · End-to-End ML Workflow using Scikit-learn** | Data leakage and train/serve skew |
| 60 | Thu Dec 17 | **Deep Learning Fundamentals — Neural Networks & Perceptron · Activation Functions, Loss Functions & Optimizers · Forward Propagation, Backward Propagation & Gradient Descent** | From perceptron to transformer: the same gradient-descent engine |
| 61 | Fri Dec 18 | **Epochs, Batch Size, Learning Rate & Hyperparameter Tuning · Batch Normalization, Dropout & Vanishing Gradient Problem** | Mixed-precision training basics (FP16 / BF16) |
| 62 | Sat Dec 19 | **CNNs & Image Classification · Pretrained Models, Transfer Learning & Fine-Tuning · SOTA Models & Modern DL Applications · End-to-End Model Development using TensorFlow/Keras or PyTorch** | Vision Transformers (ViT) and diffusion models in context |
| 63 | Sun Dec 20 | **Week 9 Project** — ML & DL Project Development & Deployment | Project add-on: model card for each project |

### Week 10 · NLP, Multimodal, Reasoning & Red Teaming — Days 64–70 · Mon 21 Dec – Sun 27 Dec 2026

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 64 | Mon Dec 21 | **NLP Foundations — Introduction to NLP & Text Preprocessing · Tokenization, Stop Words, Stemming & Lemmatization** | Why classical preprocessing still matters before LLM pipelines (cost, PII scrubbing) |
| 65 | Tue Dec 22 | **Bag of Words (BoW), Count Vectorizer & TF-IDF · N-Grams, POS Tagging & Named Entity Recognition (NER)** | Classical NER vs LLM extraction: cost and accuracy trade-off |
| 66 | Wed Dec 23 | **Word Embeddings: Word2Vec, GloVe & Vector Embeddings · End-to-End NLP Pipeline using Hugging Face Transformers** | Hugging Face Hub model selection; small open models for on-device and edge |
| 67 | Thu Dec 24 | Vision-Language Models, OCR Pipelines & Document Understanding at Scale | Document AI with vision-language models replacing OCR-only pipelines |
| 68 | Fri Dec 25 | Chart & Diagram Reasoning · Reasoning Models & Test-Time Compute | Reasoning models in production: effort settings, latency/cost trade-offs, when not to use them |
| 69 | Sat Dec 26 | Red Teaming, OWASP LLM Top 10 & Responsible AI Governance | EU AI Act after the Digital Omnibus (Reg. (EU) 2026/1744, in force 27 Jul 2026): Annex III high-risk → 2 Dec 2027, Annex I → 2 Aug 2028, Art. 50 transparency still from Aug 2026; NIST AI RMF; ISO/IEC 42001; OWASP Agentic red-team cases |
| 70 | Sun Dec 27 | **Week 10 Project** — NLP & Multimodal Projects + Red Team Assessment | Project add-on: red-team agent tool misuse, not only prompt injection |

### Week 11 · Cloud Deployment, AI Infrastructure & LLMOps — Days 71–77 · Mon 28 Dec – Sun 3 Jan 2027

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 71 | Mon Dec 28 | **Introduction to AWS, Azure & Google Cloud Platform · Compute Services (EC2, Azure VM, Compute Engine) · Storage Services (S3, Blob Storage, Cloud Storage)** | Managed agent platforms: Amazon Bedrock AgentCore, Microsoft Azure AI Foundry, Google Vertex AI agent tooling |
| 72 | Tue Dec 29 | **Docker Fundamentals & Containerization · Docker for AI Applications** | GPU containers and model-weight caching |
| 73 | Wed Dec 30 | **Deploying FastAPI Applications · Deploying AI Applications on Cloud · Serverless AI Deployments** | Serverless GPU inference; cold-start trade-offs |
| 74 | Thu Dec 31 | **CI/CD Basics for AI Applications · Monitoring & Logging · Cost Optimization & Cloud Best Practices** | Eval gates inside CI/CD; OpenTelemetry-based AI monitoring |
| 75 | Fri Jan 1 | LLMOps — Model Registries, Automated Eval Gates & Inference Optimisation (TensorRT-LLM, ONNX) | Kubernetes-native inference (llm-d, NVIDIA Dynamo) and prefill/decode disaggregation at scale |
| 76 | Sat Jan 2 | Synthetic Data Generation (Self-Instruct, Evol-Instruct) · Feature Stores & Data Lineage · Cost Engineering & Chargeback | Synthetic data for evals and RL environments; verifier quality as the ceiling |
| 77 | Sun Jan 3 | **Week 11 Project** — Deploy a Production-Ready AI Service | Project add-on: cost-per-request dashboard |

### Week 12 · No-Code AI Platforms & Enterprise Capstone — Days 78–84 · Mon 4 Jan – Sun 10 Jan 2027

| Day | Date | Topic | ⚡ 2026 addition |
|-----|------|-------|------------------|
| 78 | Mon Jan 4 | **Introduction to No-Code & Low-Code AI Platforms · Claude Projects & Claude Artifacts · ChatGPT Projects, GPTs & Canvas** | Agent builders inside productivity suites; when no-code agents are enough |
| 79 | Tue Jan 5 | **Microsoft Copilot & Microsoft 365 Copilot · Microsoft Copilot Studio & AI Agents (Basics) · Google Gemini Workspace & Gems** | Enterprise agent governance in Microsoft 365 / Google Workspace |
| 80 | Wed Jan 6 | **AI Workflow Automation using n8n (Introduction) · AI Coding Assistants (GitHub Copilot, Cursor & Windsurf) · Rapid AI Prototyping & Business Use Cases · Choosing Between No-Code, Low-Code & Custom AI Development** | Coding agents as the main developer interface (Claude Code, OpenAI Codex, GitHub Copilot agent mode, Cursor); Agent Skills and AGENTS.md in a real repo |
| 81 | Thu Jan 7 | **Capstone I** — Architecture, ADRs & C4 Diagrams | ADRs for MCP, A2A, model routing and eval-gate choices |
| 82 | Fri Jan 8 | **Capstone II** — Build & Integration | Build with MCP tools, Agent Skills and OpenTelemetry tracing |
| 83 | Sat Jan 9 | **Capstone III** — Evaluation, Security & Deployment | Eval gate + OWASP LLM/Agentic mapping + EU AI Act risk classification |
| 84 | Sun Jan 10 | **Capstone IV** — Enterprise AI Assistant Final Defence | Final defence + State of AI Engineering 2026 → 2027 outlook |

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
  (every date shifted +7 days; no topic changed). Christmas = Day 68, New Year = Day 75.

*Locked 14 October 2026.*
