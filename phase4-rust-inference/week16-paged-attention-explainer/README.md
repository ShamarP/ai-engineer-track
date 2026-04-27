# Week 16 — PagedAttention explainer (writing week)

**Why this week:** PagedAttention is the most important systems paper in the LLM era. Reading it carefully — and understanding *why* it's so good — is what separates AI engineers from "people who use OpenAI."

## 📖 Read (~6 hours, this week is reading-heavy)
- [ ] **AIE Ch 9** — *Inference Optimization*
- [ ] **Dao et al., 2022, *FlashAttention*** ([arxiv 2205.14135](https://arxiv.org/abs/2205.14135)). Sections **1**, **3**, **3.1**, **3.2**, **Figure 1**.
- [ ] **Kwon et al., 2023, *PagedAttention / vLLM*** ([arxiv 2309.06180](https://arxiv.org/abs/2309.06180)). Read every word. Sketch Figures 1, 4, 5, 6.
- [ ] **vLLM blog post** — original release post on the vLLM GitHub
- [ ] Skim **Yu et al., 2022, *Orca*** — origin of continuous batching

Note files: `notes/papers/dao-2022-flashattention.md`, `notes/papers/kwon-2023-paged-attention.md`.

## 🧠 Concepts to internalize
- [ ] KV cache: every token's key and value vectors, cached so you don't recompute on each new token
- [ ] KV cache memory grows with sequence length × batch size — it eats your GPU
- [ ] The "paged" idea: borrow virtual memory paging from OS-land, apply to KV cache
- [ ] Continuous vs. static batching: dynamic, per-request, much higher throughput
- [ ] Prefill vs. decode: prefill is parallel and compute-bound; decode is sequential and memory-bound
- [ ] FlashAttention: tile attention to keep activations in SRAM not HBM

## 🛠 Build
1. [ ] Read the vLLM paper twice
2. [ ] Read `vllm/core/block_manager.py` and `vllm/worker/cache_engine.py` (vLLM source)
3. [ ] Write a 1500–2000 word blog post: *PagedAttention, explained for engineers who haven't read the paper*. Include:
   - [ ] The KV cache memory problem with one diagram
   - [ ] The OS analogy
   - [ ] How block tables work, with a worked example
   - [ ] What it cost the authors (CUDA kernel work)
   - [ ] The throughput numbers, with citations
4. [ ] Publish it (your blog, dev.to, Substack)
5. [ ] README links to the post + includes your hand-drawn diagrams

## ✅ Done when
- [ ] The post is public
- [ ] You can explain PagedAttention to a senior engineer in 5 minutes, no slides, and answer "why not just use a bigger GPU?"

## 🎯 Stretch
- [ ] Read FlashAttention-2; write a one-page diff to the post.

---

## What I built

## What I learned

## What I got wrong
