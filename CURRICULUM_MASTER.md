# 📗 CURRICULUM MASTER — Merged 12-Week Syllabus

> 🔒 **LOCKED 2 August 2026 (merge revision m1).**
> This document is the **complete content authority** for all 12 weeks.
> Dates are governed by [`SCHEDULE.md`](SCHEDULE.md).
>
> **Merge:** an incoming 4-month (16-week) syllabus has been absorbed into the existing
> 12-week programme. **No weeks were added.** Every incoming topic and every listed
> resource is preserved verbatim below.

---

## 1. Merge Evidence — What Was Already Taught

Before placing anything, the incoming syllabus was measured term-by-term against the
28-PDF Phase 1 corpus (549 pages, Days 1–28).

| Incoming block | Covered | Total | % | Verdict |
|----------------|---------|-------|---|---------|
| M2W3 Transformers & LLMs | 7 | 8 | 88% | ALREADY TAUGHT |
| M1W2 SQL | 6 | 7 | 86% | ALREADY TAUGHT |
| M3W3 RAG + Agentic Frameworks | 12 | 16 | 75% | ALREADY TAUGHT |
| M4W3 Cloud Infrastructure | 9 | 12 | 75% | ALREADY TAUGHT |
| M3W4 Production AI & Evaluation | 8 | 11 | 73% | ALREADY TAUGHT |
| M3W2 LLM & Prompt Engineering | 10 | 14 | 71% | ALREADY TAUGHT |
| M3W1 Software Engineering / FastAPI | 7 | 12 | 58% | PARTIAL |
| M2W3 Classical NLP | 6 | 12 | 50% | PARTIAL |
| M1W3 ML Fundamentals | 7 | 16 | 44% | PARTIAL |
| M2W1 Deep Learning / CNN | 5 | 13 | 38% | PARTIAL |
| M1W1 Python / Pandas / NumPy / OOP | 2 | 8 | 25% | **NEW** |
| M4W4 No-Code & AI Productivity Tools | 2 | 14 | 14% | **NEW** |

**Conclusion:** roughly **60% of the incoming syllabus is already delivered** in Days 1–28.
The genuine additions are classical ML, deep learning and computer vision, classical NLP,
software-engineering/FastAPI depth, named agentic frameworks, and the entire no-code /
AI-productivity block.

---

## 2. Placement Strategy — Architect's Rationale

Three moves make a 16-week syllabus fit 12 weeks without deleting anything:

**Move 1 — Deduplicate against delivered work.** Topics already taught to production depth
in Days 1–28 are not re-taught. They are cross-referenced to the day that covered them, so
nothing is lost and no time is spent twice.

**Move 2 — Prerequisites become a self-study Foundations Track.** Python, Pandas, NumPy,
OOP and SQL are upstream of everything already built. A student 28 days into advanced LLM
engineering — with a working multi-tenant Text-to-SQL system — has demonstrably cleared
them. They are preserved in full as **Track 0** with all resources, as reference and
revision material, not as teaching days.

**Move 3 — Compress the deferred Phase 2 weeks where Phase 1 already went deep.**
Security had a full production day on Day 25 (Tier 1–4 control hierarchy, injection,
PII, tenant isolation, audit, supply chain), so Week 10 keeps red teaming and governance
but does not repeat the foundations. The same logic applies to multimodal (Day 26) and
agentic system design (Day 20).

### What was compressed, stated plainly

| Original Phase 2 plan | Now | Justification |
|-----------------------|-----|---------------|
| W8 Agentic System Design — 7 days | 3 days (D54–56) | Day 20 covered orchestration, pools, parallel phases |
| W9 Multimodal — 7 days | 2 days (D67–68) | Day 26 covered VLM architecture, pipelines, tables, staged eval |
| W10 Security — 7 days | 2 days (D69–70) | Day 25 covered the full Tier 1–4 control hierarchy |
| W12 Capstone — 7 days | 4 days (D81–84) | 3 days redirected to the no-code block |

**This is a real trade.** Depth in security, multimodal and system design is reduced to
create room for ML/DL/NLP foundations and the no-code block. The compressed material is
not removed — it is layered on top of days already delivered.

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

> **Already applied in the programme:** SQL is exercised continuously in the Days 13–27
> Text-to-SQL capstone — joins, aggregates, subqueries, window functions and CTEs all
> appear in generated and validated queries.

---
---

# PHASE 1 · WEEKS 1–4 · DAYS 1–28 — ✅ COMPLETE
*6 July – 2 August 2026 · 28 PDFs · 549 pages · 371 Eagle Eye terms · 0 gaps*

Unchanged by this merge. Full day-by-day is in [`SCHEDULE.md`](SCHEDULE.md).

| Week | Days | Theme |
|------|------|-------|
| 1 | 1–7 | Foundations — tokenization, embeddings, transformers, training, scaling laws, structured output, model selection |
| 2 | 8–14 | Efficiency — quantization, LoRA/PEFT, full fine-tuning, serving, evaluation, efficiency, Text-to-SQL foundation |
| 3 | 15–21 | Retrieval & Agents — RAG foundations, indexing, hybrid retrieval, generation, agents, multi-agent, capstone |
| 4 | 22–28 | Production — LLMOps, versioning, cost, security, multimodal, fine-tuning, Phase 1 close |

### Incoming topics already delivered here

| Incoming topic | Delivered on |
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

### Free Resources for blocks already delivered in Phase 1

**From M3W2 · LLM Engineering & Prompt Engineering**
1. ₹35 LPA LLM Engineer Roadmap 2026 in Tamil (Beginner to Job Ready) *(AI Coach John)*
2. Prompt Engineering Basics to Advanced: One-Shot, Two-Shot, Chain of Prompting — Tamil Full Guide *(AI Coach John)*
3. Prompt Injection Simplified in Tamil *(AI Coach John)*

**GenAI Support: ChatGPT**

**From M3W3 · RAG Systems** *(retrieval half — delivered Days 15–18)*
1. 8 RAG Concepts Explained in 26 Minutes: April 2026 *(AI Coach John)*
2. Vector Database (தமிழில்) — The Why? What? How? *(AI Coach John)*
3. 8 (CHUNKING Strategies) Industries Expect You to Know *(AI Coach John)*

**GenAI Support: ChatGPT**

> *The agentic-framework half of M3W3 (LangChain, LangGraph, CrewAI, AG2/AutoGen/Agno,
> Loop Engineering & Human-in-the-Loop) is delivered in Weeks 5–6; its resources are
> listed there.*

---
---

# PHASE 2 · WEEKS 5–12 · DAYS 29–84
*14 September – 8 November 2026*

---

## WEEK 5 · AGENTS, HARNESS & LOOP ENGINEERING + AGENTIC FRAMEWORKS
**Days 29–35 · 14–20 September 2026**
**Project:** AI Research Agent with Tool Calling (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 29 | Mon Sep 14 | Agent Architectures Beyond ReAct |
| 30 | Tue Sep 15 | **Harness Engineering I — Tool Design** |
| 31 | Wed Sep 16 | **Harness Engineering II — Responses, Errors & Environment** |
| 32 | Thu Sep 17 | **Loop Engineering I — Termination & Budgets** |
| 33 | Fri Sep 18 | **Loop Engineering II — Recovery, Sub-Agents & Human-in-the-Loop Design** |
| 34 | Sat Sep 19 | **Agentic Frameworks I — LangChain Fundamentals & LangGraph Workflows** |
| 35 | Sun Sep 20 | **Week 5 Project** — AI Research Agent with Tool Calling |

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
**Days 36–42 · 21–27 September 2026**
**Project:** Multi-Agent Business Analyst System (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 36 | Mon Sep 21 | **Context Engineering I — The Context Budget & Token Management** |
| 37 | Tue Sep 22 | **Context Engineering II — Compaction & Progressive Disclosure** |
| 38 | Wed Sep 23 | MCP (Model Context Protocol) Fundamentals |
| 39 | Thu Sep 24 | Building a Production MCP Server |
| 40 | Fri Sep 25 | **Agentic Frameworks II — CrewAI, AG2 / AutoGen / Agno & Multi-Agent Collaboration** |
| 41 | Sat Sep 26 | Agent Memory Architectures & Planning Strategies |
| 42 | Sun Sep 27 | **Week 6 Project** — Multi-Agent Business Analyst System |

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
**Days 43–49 · 28 September – 4 October 2026**
**Project:** Eval & Observability Platform (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 43 | Mon Sep 28 | **AI System Architecture & Orchestration** |
| 44 | Tue Sep 29 | LLM-as-a-Judge & Eval Harness Design |
| 45 | Wed Sep 30 | **Hallucination Detection & Evaluation** |
| 46 | Thu Oct 1 | **RAG Evaluation — RAGAS & TruLens** |
| 47 | Fri Oct 2 | **LangSmith for Debugging & Observability** |
| 48 | Sat Oct 3 | **AI Safety & Guardrails in Production** |
| 49 | Sun Oct 4 | **Week 7 Project** — Eval & Observability Platform |

**Incoming topics absorbed:** AI System Architecture & Orchestration · LangSmith for
Debugging & Observability · AI Safety & Guardrails · Hallucination Detection &
Evaluation · RAG Evaluation (RAGAS, TruLens)

---

## WEEK 8 · AI APPLICATION ENGINEERING & AGENTIC SYSTEM DESIGN
**Days 50–56 · 5–11 October 2026**
**Project:** End-to-End AI Backend + Scalable Agent Runtime (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 50 | Mon Oct 5 | **AI Application Architecture · REST APIs, HTTP Methods & API Integration · JSON, JSON Schema & Structured Data** |
| 51 | Tue Oct 6 | **FastAPI Fundamentals & API Development · Request Handling, Response Models & Error Handling** |
| 52 | Wed Oct 7 | **Authentication, API Keys & Environment Variables · File Uploads, Streaming Responses & Async APIs** |
| 53 | Thu Oct 8 | **Database Integration (SQLite/PostgreSQL Basics) · AI API Integration (OpenAI, Gemini, Claude)** |
| 54 | Fri Oct 9 | Agentic System Design — Runtime, State Management & Queueing |
| 55 | Sat Oct 10 | Scaling, Backpressure, Failure Isolation & Concurrency |
| 56 | Sun Oct 11 | **Week 8 Project** — End-to-End AI Backend Development using FastAPI + Scalable Agent Runtime |

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
**Days 57–63 · 12–18 October 2026**
**Project:** ML & DL Project Development & Deployment (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 57 | Mon Oct 12 | **ML Fundamentals — Types of ML (Supervised, Unsupervised & Reinforcement) · Features, Labels, Training/Testing Data & Train/Test Split · Classification, Regression & Clustering Algorithms** |
| 58 | Tue Oct 13 | **Model Validation using Cross-Validation · Evaluation Metrics: Accuracy, Precision, Recall, F1-Score & ROC-AUC · Confusion Matrix & Handling Class Imbalance** |
| 59 | Wed Oct 14 | **Overfitting, Underfitting & Regularization · Feature Engineering & Data Preprocessing · Feature Scaling, Normalization & Data Preparation · End-to-End ML Workflow using Scikit-learn** |
| 60 | Thu Oct 15 | **Deep Learning Fundamentals — Neural Networks & Perceptron · Activation Functions, Loss Functions & Optimizers · Forward Propagation, Backward Propagation & Gradient Descent** |
| 61 | Fri Oct 16 | **Epochs, Batch Size, Learning Rate & Hyperparameter Tuning · Batch Normalization, Dropout & Vanishing Gradient Problem** |
| 62 | Sat Oct 17 | **CNNs & Image Classification · Pretrained Models, Transfer Learning & Fine-Tuning · SOTA Models & Modern DL Applications · End-to-End Model Development using TensorFlow/Keras or PyTorch** |
| 63 | Sun Oct 18 | **Week 9 Project** — ML & DL Project Development & Deployment |

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
**Days 64–70 · 19–25 October 2026**
**Project:** NLP & Multimodal Projects + Red Team Assessment (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 64 | Mon Oct 19 | **NLP Foundations — Introduction to NLP & Text Preprocessing · Tokenization, Stop Words, Stemming & Lemmatization** |
| 65 | Tue Oct 20 | **Bag of Words (BoW), Count Vectorizer & TF-IDF · N-Grams, POS Tagging & Named Entity Recognition (NER)** |
| 66 | Wed Oct 21 | **Word Embeddings: Word2Vec, GloVe & Vector Embeddings · End-to-End NLP Pipeline using Hugging Face Transformers** |
| 67 | Thu Oct 22 | Vision-Language Models, OCR Pipelines & Document Understanding at Scale |
| 68 | Fri Oct 23 | Chart & Diagram Reasoning · Reasoning Models & Test-Time Compute |
| 69 | Sat Oct 24 | Red Teaming, OWASP LLM Top 10 & Responsible AI Governance |
| 70 | Sun Oct 25 | **Week 10 Project** — NLP & Multimodal Projects + Red Team Assessment |

**Incoming topics absorbed — the complete M2W3 classical-NLP block.**
*(Attention, self-attention, encoder-decoder, transformers, LLMs, foundation models,
cosine similarity and semantic search from the same block were delivered on Days 2–4.)*

### Week 10 Project Set — preserved verbatim

**NLP Projects & Deployment** *(incoming M2W4)*

| Project Title | Category | Industry / Application |
|---------------|----------|------------------------|
| AI Resume Screening & Candidate Matching System | NLP + Semantic Search | HRTech / Recruitment |
| Legal Document Question Answering using RAG | LLM + RAG | LegalTech / Enterprise AI |
| Intelligent Customer Support Chatbot with Vector Search | Conversational AI + LLM | Customer Support / SaaS |

**Also delivered this week:** Multimodal Document Processor · Red Team Your Own RAG System
(20+ adversarial prompts, guardrails blocking ≥90%, written security assessment with risk
ratings and residual-risk acceptance).

**Free Resources carried in**
1. What is NLP? Beginners to Advanced RoadMap 2025 in Tamil *(AI Coach John's Material)*
2. NLP Playlist *(Chill and Grow)*

---

## WEEK 11 · CLOUD DEPLOYMENT, AI INFRASTRUCTURE & LLMOPS
**Days 71–77 · 26 October – 1 November 2026**
**Project:** Deploy a Production-Ready AI Service (PORTFOLIO)

| Day | Date | Topic |
|-----|------|-------|
| 71 | Mon Oct 26 | **Introduction to AWS, Azure & Google Cloud Platform · Compute Services (EC2, Azure VM, Compute Engine) · Storage Services (S3, Blob Storage, Cloud Storage)** |
| 72 | Tue Oct 27 | **Docker Fundamentals & Containerization · Docker for AI Applications** |
| 73 | Wed Oct 28 | **Deploying FastAPI Applications · Deploying AI Applications on Cloud · Serverless AI Deployments** |
| 74 | Thu Oct 29 | **CI/CD Basics for AI Applications · Monitoring & Logging · Cost Optimization & Cloud Best Practices** |
| 75 | Fri Oct 30 | LLMOps — Model Registries, Automated Eval Gates & Inference Optimisation (TensorRT-LLM, ONNX) |
| 76 | Sat Oct 31 | Synthetic Data Generation (Self-Instruct, Evol-Instruct) · Feature Stores & Data Lineage · Cost Engineering & Chargeback |
| 77 | Sun Nov 1 | **Week 11 Project** — Deploy a Production-Ready AI Service |

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
**Days 78–84 · 2–8 November 2026**
**Project:** Enterprise AI Assistant (CAPSTONE)

| Day | Date | Topic |
|-----|------|-------|
| 78 | Mon Nov 2 | **Introduction to No-Code & Low-Code AI Platforms · Claude Projects & Claude Artifacts · ChatGPT Projects, GPTs & Canvas** |
| 79 | Tue Nov 3 | **Microsoft Copilot & Microsoft 365 Copilot · Microsoft Copilot Studio & AI Agents (Basics) · Google Gemini Workspace & Gems** |
| 80 | Wed Nov 4 | **AI Workflow Automation using n8n (Introduction) · AI Coding Assistants (GitHub Copilot, Cursor & Windsurf) · Rapid AI Prototyping & Business Use Cases · Choosing Between No-Code, Low-Code & Custom AI Development** |
| 81 | Thu Nov 5 | **Capstone I** — Architecture, ADRs & C4 Diagrams |
| 82 | Fri Nov 6 | **Capstone II** — Build & Integration |
| 83 | Sat Nov 7 | **Capstone III** — Evaluation, Security & Deployment |
| 84 | Sun Nov 8 | **Capstone IV** — Enterprise AI Assistant Final Defence |

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

## 4. Project Ladder — Merged

| Week | Project | Type |
|------|---------|------|
| 01 | Model Selection Dashboard | MINI ✅ |
| 02 | Domain Fine-Tune + Quantize | PORTFOLIO ✅ |
| 03 | End-to-End Text-to-SQL | **CAPSTONE** ✅ |
| 04 | Production Hardening | PORTFOLIO ✅ |
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

## 5. Daily Protocol (unchanged)

1. **Teach** the day's topic fully in chat — concept-first, plain English, FAANG examples, Architect's Lens, hands-on exercises
2. **Eagle Eye** — two-pass verification; never declare a gap without snip verification, never declare coverage without confirmation
3. **PDF** → `~/Desktop/AI-ML/WeekN_DayNN_TopicName.pdf`
4. **Push** → `week-NN/notes/` on the GitHub repository

**FAANG rule (locked):** examples use only Meta, Apple, Amazon, Netflix, Google, Microsoft.
**GenAI Support:** ChatGPT *(as noted throughout the incoming syllabus)*

---

*Locked 2 August 2026 (merge revision m1). Complete content authority for Weeks 1–12.
Dates governed by `SCHEDULE.md`. Supersedes `CURRICULUM_PHASE2.md` for Weeks 5–12.*
