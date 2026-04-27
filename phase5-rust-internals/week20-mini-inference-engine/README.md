# Week 20 — Build a mini inference engine

**Why this week:** KV cache + continuous batching are the two systems ideas that made vLLM possible. Build a toy version yourself in Rust to truly understand vLLM's architecture.

## 📖 Read (~6 hours)
- [ ] **DMLS Ch 8** — *Data Distribution Shifts and Monitoring* (light skim)
- [ ] **vLLM source dive**:
  - [ ] `vllm/core/scheduler.py` — the scheduler
  - [ ] `vllm/core/block_manager.py` — paged KV cache management
  - [ ] `vllm/engine/llm_engine.py` — the request lifecycle
- [ ] **Dao, 2023, *FlashAttention-2*** ([arxiv 2307.08691](https://arxiv.org/abs/2307.08691)). Sections **1**, **3**.
- [ ] **Yu et al., 2022, *Orca*** — origin of continuous batching (skim)
- [ ] Re-read your Week 16 PagedAttention explainer

Note files: `notes/papers/dao-2023-flashattention-2.md`, `notes/papers/vllm-source-trace.md`.

## 🧠 Concepts to internalize
- [ ] Continuous batching: per-step rebatching across in-flight requests
- [ ] Paged KV cache: blocks (typically 16 tokens), block tables, free list management
- [ ] Prefill vs. decode phases — different compute profiles, different scheduling
- [ ] Request lifecycle: queue → scheduler → executor → response stream
- [ ] Why throughput-oriented systems trade per-request latency for total tokens/sec

## 🛠 Build
1. [ ] Rust HTTP server (axum from W15) that loads your candle Llama from W19
2. [ ] Implement paged KV cache: 16-token blocks managed via a free list
3. [ ] Continuous batching scheduler: each step, pull pending requests, batch their decode steps
4. [ ] OpenAI-compatible `/v1/chat/completions` endpoint with SSE streaming
5. [ ] Multi-request stress test: 1, 8, 32 concurrent requests; measure tokens/sec at each
6. [ ] README: architecture diagram, throughput numbers, what surprised you

## ✅ Done when
- [ ] Continuous batching shows ≥3x throughput at concurrency 32 vs. concurrency 1
- [ ] KV cache memory usage flat under sustained load (no leaks; verify with Activity Monitor or htop)

## 🎯 Stretch
- [ ] Add prefix caching for system prompts (huge win when many requests share a prefix).

---

## What I built

## What I learned

## What I got wrong
