# Week 17 — Speculative decoding (or vLLM/candle PR)

**Why this week:** shipping a real PR to a real inference project is a credential. Implementing speculative decoding is a credential. Pick one.

## 📖 Read (~4 hours)
- [ ] **Leviathan et al., 2023, *Fast Inference from Transformers via Speculative Decoding*** ([arxiv 2211.17192](https://arxiv.org/abs/2211.17192)). Sections **1**, **2**, **3**. Work through the math in 3.2.
- [ ] **Chen et al., 2023, *Accelerating Large Language Model Decoding with Speculative Sampling*** (DeepMind, [arxiv 2302.01318](https://arxiv.org/abs/2302.01318)) — second perspective
- [ ] Pick your contribution target and read its `CONTRIBUTING.md`:
  - [ ] **vLLM** — Python+CUDA, large project, slow but prestigious
  - [ ] **candle** (HuggingFace) — pure Rust, smaller, friendly maintainers
  - [ ] **mistral.rs** — pure Rust, very active
  - [ ] **llama.cpp** — C++, lots of issues, lots of users

Note files: `notes/papers/leviathan-2023-spec-decoding.md`.

## 🧠 Concepts to internalize
- [ ] Speculative decoding: small "draft" model proposes K tokens; big model verifies in one parallel step; accept the matching prefix
- [ ] Acceptance rate determines speedup — 60% acceptance ≈ 2x speedup
- [ ] Why it works: verification is parallel, generation is sequential. Trade compute for latency.
- [ ] The draft model needs to be cheap *and* well-aligned with the target

## 🛠 Build — pick A or B
- [ ] **A: A real PR.** Browse `good-first-issue` labels on vLLM, candle, mistral.rs, or llama.cpp. Pick one. Fix it. Open the PR. Even a docs fix — the workflow (fork → branch → test → review) is the lesson.
- [ ] **B: Speculative decoding from scratch.** In Rust + `candle`: greedy spec decoding with a small draft (TinyLlama-1.1B) and big target (Llama-3-8B). Measure speedup.

## ✅ Done when
- [ ] (A) PR is open, conversations happening with maintainers
- [ ] (B) Spec decoding is faster than naive autoregressive, with a benchmark in the README

## 🎯 Stretch
- [ ] (Did A): now do B too. (Did B): submit your benchmark write-up to Latent.Space or HN.

---

## What I built

## What I learned

## What I got wrong
