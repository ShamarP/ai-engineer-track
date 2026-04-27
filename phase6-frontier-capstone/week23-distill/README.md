# Week 23 — Distillation + cost engineering

**Why this week:** knowing how to make a system *cheaper without making it worse* is one of the most valuable engineering skills there is.

## 📖 Read (~4 hours)
- [ ] **DMLS Ch 9** — *Continual Learning and Test in Production*; **Ch 11** — *The Human Side of Machine Learning*
- [ ] **Hsieh et al., 2023, *Distilling Step-by-Step!*** ([arxiv 2305.02301](https://arxiv.org/abs/2305.02301)). Sections **1**, **3**, **4**.
- [ ] **Hinton, Vinyals, Dean, 2015, *Distilling the Knowledge in a Neural Network*** ([arxiv 1503.02531](https://arxiv.org/abs/1503.02531)) — the original; short and worth reading
- [ ] **Anthropic, *Prompt caching* docs**
- [ ] **OpenAI, *Batch API* docs**

Note files: `notes/papers/hsieh-2023-distilling-step-by-step.md`, `notes/papers/hinton-2015-distillation.md`.

## 🧠 Concepts to internalize
- [ ] Distillation: train a small "student" to mimic a big "teacher"
- [ ] Knowledge transfer happens through soft labels (logits) or rationale steps
- [ ] The cost-quality-latency triangle: pick two
- [ ] Caching levers: prompt caching, semantic caching, response caching
- [ ] Routing: cheap model for easy queries, expensive for hard — needs a classifier
- [ ] Batch APIs: 50% discount for async, perfect for evals and bulk processing

## 🛠 Build
1. [ ] Take your best agent from Phase 3
2. [ ] Run 5,000 real queries through it with a frontier model (Claude Sonnet 4.6 or GPT-4o); log every input + output + reasoning trace
3. [ ] Use those traces as training data
4. [ ] QLoRA fine-tune `Qwen2.5-3B-Instruct` on the traces (rationale + answer)
5. [ ] Plot: cost-per-1k-queries × latency × quality (held-out eval) for: frontier model, fine-tuned 3B, base 3B
6. [ ] README: include the 3-axis chart and a recommendation: "for *this* workload, model X is the right call because…"

## ✅ Done when
- [ ] 3B model is within 10% of frontier-model quality on your eval and ≥5x cheaper
- [ ] You can quote per-token cost for 3 production-grade hosting options for your distilled model

## 🎯 Stretch
- [ ] Implement semantic caching — cache responses keyed by a query embedding, hit on cosine distance. Measure cache hit rate and savings.

---

## What I built

## What I learned

## What I got wrong
