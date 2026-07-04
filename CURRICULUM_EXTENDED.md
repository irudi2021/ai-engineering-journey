# Extended Curriculum — Week 10 & Week 11

Added to the original 10-week syllabus to cover AI Security and Cloud-Native LLMOps
before the Capstone (moved to Week 12).

---

## WEEK 10 · AI Security, Red Teaming & Responsible AI
*Sep 7 – Sep 13*

### Goal
Learn how to attack and defend LLM-powered systems. Build production-grade guardrails.
Understand governance, compliance, and responsible AI frameworks.

### Topics Covered

| Module | Content |
|--------|---------|
| **AI Threat Landscape** | OWASP LLM Top 10 deep-dive: prompt injection, jailbreaks, data exfiltration, insecure output handling, excessive agency, model theft, supply chain attacks |
| **Red Teaming LLMs** | Systematic adversarial testing: crafting attack prompts (direct injection, indirect injection, role-play, token smuggling), automated red-teaming frameworks (Garak, PyRIT), measuring attack success rates |
| **Input/Output Guardrails Engineering** | Building production guardrails: toxicity classification (Perspective API, Detoxify), PII detection (Presidio), topic filtering, hallucination detection as middleware |
| **Prompt Injection Defenses** | Defensive patterns: instruction hierarchy, delimiters, output constraints, canary tokens, prompt sandboxing, system prompt isolation |
| **Responsible AI & Governance** | Bias detection, fairness metrics, model cards, explainability techniques (SHAP, attention visualization), regulatory landscape (EU AI Act, NIST AI RMF, ISO 42001) |
| **AI Audit & Compliance** | Logging and audit trails for AI decisions, data retention policies, right-to-explanation, A/B testing for bias regression, immutable audit logs |

### Architect's Lens · Security as Architecture

Security is not a feature — it's a property of the system. Design:

- **Zero-trust AI architecture**: every LLM call authenticated, every tool call authorized, every output scanned
- **Defense in depth**: input filtering → retrieval filtering → generation constraints → output scanning → audit logging
- **Incident response**: automated kill switches, rollback procedures, breach notification pipelines, forensic replay capability

### Hands-On Project — Red Team Your Own RAG System (PORTFOLIO)

- Take your Week 4 RAG service and write 20+ adversarial prompts (direct injection, indirect injection, role-play attacks, multi-turn attacks)
- Build input/output guardrails that block ≥90% of attacks
- Document a security assessment report with risk ratings, mitigations, and residual risk acceptance

**Portfolio headline:** *"Red-teamed a production RAG system; engineered guardrails blocking 90%+ of adversarial attacks."*

**Tags:** `red-teaming` `guardrails` `owasp-llm` `responsible-ai` `pii-detection` `audit-logging`

---

## WEEK 11 · Cloud-Native AI Deployment, LLMOps & Synthetic Data Engineering
*Sep 14 – Sep 20*

### Goal
Deploy AI systems to production at scale. Build CI/CD pipelines for AI. Generate and manage
synthetic training and evaluation data. Enforce cost governance.

### Topics Covered

| Module | Content |
|--------|---------|
| **Cloud-Native AI Deployment** | Deploying models on AWS (SageMaker, Bedrock, EKS), GCP (Vertex AI, GKE), Azure (OpenAI Service, Container Apps); serverless vs. containerized inference; GPU node pools on Kubernetes with autoscaling |
| **LLMOps Pipelines** | CI/CD for AI: automated testing, prompt versioning (PromptLayer, LangSmith, Weights & Biases), model registries (MLflow, Hugging Face Hub), drift detection, automated rollback on eval regression |
| **Inference Optimization** | TensorRT-LLM, ONNX Runtime, model distillation, speculative decoding, continuous batching; building and enforcing latency SLAs |
| **Synthetic Data Generation** | Generating training/evaluation data with LLMs: Self-Instruct, Alpaca-style data generation, Evol-Instruct, quality filtering (deduplication, toxicity scoring), diversity scoring, human verification workflows |
| **Feature Stores & Data Lineage** | Embedding stores as features (Feast, Tecton), versioning datasets (DVC), tracking lineage from raw data → embeddings → model outputs → user-facing decisions |
| **Cost Engineering & Chargeback** | Per-team/token billing, spot instance usage, semantic caching strategies (Redis, GPTCache), budget alerts, chargeback models for multi-tenant AI |

### Architect's Lens · Production Readiness Checklist

Before any AI system goes live, validate:

- [ ] Latency SLA met under load test (p50, p95, p99)
- [ ] Cost per request within budget with 2× traffic headroom
- [ ] Eval gate passes with no regression vs. previous version
- [ ] Security scan (red team) clean — no critical or high findings
- [ ] Observability dashboards live (traces, metrics, logs)
- [ ] Runbook and rollback plan documented and tested
- [ ] Model card and data lineage documented
- [ ] Disaster recovery: RTO < 1 hour, RPO < 15 minutes

### Hands-On Project — Deploy a Production-Ready AI Service (PORTFOLIO)

- Containerize your Week 5 agent or Week 4 RAG system with Docker
- Deploy to a managed Kubernetes cluster (EKS/GKE) or serverless platform
- Set up CI/CD: automated eval on PR, canary deployment, automatic rollback on regression
- Generate a 500-example synthetic golden dataset for your domain, human-verify 10%, benchmark eval quality vs. real data
- Build a live cost dashboard: track tokens/query, latency p95, $/1K requests, with alerting

**Portfolio headline:** *"Deployed a production AI service on Kubernetes with CI/CD eval gates, synthetic data pipeline, and a live cost dashboard."*

**Tags:** `llmops` `kubernetes` `cicd` `synthetic-data` `cost-engineering` `inference-optimization`

---

## WEEK 12 · Capstone Project — Enterprise AI Assistant
*Sep 21 – Sep 27*

One integrated system wiring RAG + Agents + Eval + Security + Cloud Deploy,
defended with ADRs, C4 diagrams, NFRs, and a risk & cost analysis.

### Required Deliverables (Architect's Lens)

1. **Architecture Decision Records (ADRs)** for every major choice (vector DB, model, framework, cloud)
2. **C4 System Diagrams** — Context, Container, Component, Code
3. **Non-Functional Requirements** — latency SLAs, availability, cost/request, scaling limits
4. **Risk Assessment** — failure modes, guardrail-bypass scenarios, residual risk
5. **Deployment Plan** — blue-green strategy, rollback, monitoring dashboards
6. **Security Report** — red-team results, guardrail coverage, compliance mapping

### Suggested Capstone Themes

- **Enterprise Knowledge Assistant** — multi-tenant RAG with ACLs, API gateway, LLM-as-a-Judge eval pipeline
- **Agentic Process Orchestrator** — multi-agent system using MCP to interface with business systems, supervisor routing, memory
- **AI-Powered Code Review Agent** — analyzes code with a fine-tuned model, safety guardrails, audit logging
- **Multimodal Document Processor** — invoices/contracts: OCR, entity extraction, validation agents, archival

**Portfolio headline:** *"Designed & deployed an enterprise AI assistant, presented as a full architecture proposal."*

---

*Extended by student on July 4, 2026 — Weeks 10 & 11 added, Capstone moved to Week 12.*
