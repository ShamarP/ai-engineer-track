# AI Engineer Track

A 24-week, public-by-default journey from competent engineer to top-tier **AI engineer** working on applied ML, agents, Rust-based inference, and Go-based AI infrastructure.

This repo is the artifact of that work. Every week ships a project; every project lives in its own folder; every folder has a README explaining what it is and what I learned.

> **Status:** Week 1 (Phase 1 — Foundations)

## About

I'm Shamar. I'm going all-in on AI engineering. I want to be one of the best — not "knows the buzzwords," but "can read a paper on Tuesday and ship the idea on Friday." This repo is how I get there in public.

The plan is structured around **two anchor texts** — Chip Huyen's *AI Engineering* and *Designing Machine Learning Systems* — plus ~25 specific papers, Karpathy's neural net series, and the canonical infra projects (vLLM, Ollama, MCP).

## Progress

### Phase 1 — Foundations (Weeks 1–4)
- [ ] [Week 1 — micrograd from scratch](./phase1-foundations/week1-micrograd)
- [ ] [Week 2 — GPT from scratch](./phase1-foundations/week2-gpt-from-scratch)
- [ ] [Week 3 — Fine-tune Qwen 0.5B](./phase1-foundations/week3-finetune-qwen)
- [ ] [Week 4 — Prompt playground](./phase1-foundations/week4-prompt-playground)

### Phase 2 — RAG + Evals (Weeks 5–8)
- [ ] [Week 5 — Vector store + embeddings](./phase2-rag-evals/week5-vector-store)
- [ ] [Week 6 — RAG from scratch (no framework)](./phase2-rag-evals/week6-rag-from-scratch)
- [ ] [Week 7 — RAG evals (the most important week)](./phase2-rag-evals/week7-rag-evals)
- [ ] [Week 8 — Reranking + advanced retrieval](./phase2-rag-evals/week8-reranker)

### Phase 3 — Agents (Weeks 9–13)
- [ ] [Week 9 — Agent foundations (no framework)](./phase3-agents/week9-agent-no-framework)
- [ ] [Week 10 — ReAct + Reflexion](./phase3-agents/week10-react-reflexion)
- [ ] [Week 11 — Persistent memory](./phase3-agents/week11-memory)
- [ ] [Week 12 — MCP server (TypeScript)](./phase3-agents/week12-mcp-server-ts)
- [ ] [Week 13 — Observable agent (tracing + evals)](./phase3-agents/week13-observable-agent)

### Phase 4 — Rust + Inference (Weeks 14–17)
- [ ] [Week 14 — Rust fundamentals (prompt playground in Rust)](./phase4-rust-inference/week14-prompt-playground-rust)
- [ ] [Week 15 — Async Rust inference proxy (axum + SSE)](./phase4-rust-inference/week15-inference-proxy)
- [ ] [Week 16 — PagedAttention explainer](./phase4-rust-inference/week16-paged-attention-explainer)
- [ ] [Week 17 — Speculative decoding (or vLLM/candle PR)](./phase4-rust-inference/week17-spec-decoding)

### Phase 5 — Go + AI Infrastructure (Weeks 18–21)
- [ ] [Week 18 — RAG ingestion in Go](./phase5-go-infra/week18-rag-ingest-go)
- [ ] [Week 19 — Ollama-backed eval CLI](./phase5-go-infra/week19-ollama-evals)
- [ ] [Week 20 — MCP server (Go)](./phase5-go-infra/week20-mcp-server-go)
- [ ] [Week 21 — Multi-agent orchestrator](./phase5-go-infra/week21-agent-orchestrator)

### Phase 6 — Frontier + Capstone (Weeks 22–24)
- [ ] [Week 22 — QLoRA fine-tune](./phase6-frontier-capstone/week22-qlora-task)
- [ ] [Week 23 — Distillation + cost engineering](./phase6-frontier-capstone/week23-distill)
- [ ] [Week 24 — Capstone](./phase6-frontier-capstone/week24-capstone)

See [PROGRESS.md](./PROGRESS.md) for weekly write-ups.

## How to navigate

- **Each week** has its own folder with a README laying out the plan: what to read, what concepts to internalize, what to build, and how I'll know it's done.
- **`notes/papers/`** — running notes on every paper I read.
- **`notes/books/`** — chapter notes on the two anchor books.
- **`PROGRESS.md`** — weekly retrospectives. What worked, what didn't, what I learned.

## Languages

| Language   | Used in           | Purpose                                                    |
|------------|-------------------|------------------------------------------------------------|
| Python     | Phases 1–3, 6     | Model layer: prompting, RAG, agents, fine-tuning           |
| TypeScript | Phase 3, capstone | Agent product surfaces, MCP servers                        |
| Rust       | Phase 4           | Inference internals, async serving, performance hot paths  |
| Go         | Phase 5           | AI infrastructure, orchestration, MCP servers              |

## License

MIT for code unless otherwise noted in a subfolder. Notes and write-ups are CC BY 4.0.
