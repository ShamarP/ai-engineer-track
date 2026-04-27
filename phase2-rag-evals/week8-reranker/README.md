# Week 8 — Reranking + advanced retrieval

**Why this week:** this is where good RAG becomes great RAG. Most production systems use rerankers; few engineers understand why.

## 📖 Read (~4 hours)
- [ ] **AIE Ch 4** — *Evaluate AI Systems*
- [ ] **Khattab & Zaharia, 2020, *ColBERT*** ([arxiv 2004.12832](https://arxiv.org/abs/2004.12832)). Sections **1**, **3**, **Figure 1**.
- [ ] **Asai et al., 2023, *Self-RAG*** ([arxiv 2310.11511](https://arxiv.org/abs/2310.11511)). Sections **1**, **3**, **Figure 1**.
- [ ] **Cohere Rerank docs** — practical view of cross-encoder reranking

Note files: `notes/papers/khattab-2020-colbert.md`, `notes/papers/asai-2023-self-rag.md`.

## 🧠 Concepts to internalize
- [ ] Bi-encoder (your embedding model) vs. cross-encoder (a reranker)
- [ ] Bi-encoders fast but imprecise: query and doc encoded independently
- [ ] Cross-encoders precise but slow: query and doc encoded *together*
- [ ] Two-stage: retrieve top-100 with bi-encoder, rerank to top-5 with cross-encoder
- [ ] Query rewriting: when the user's question doesn't match indexed text style
- [ ] Self-RAG: model decides *whether* to retrieve, then critiques its own output

## 🛠 Build
1. [ ] Add a Cohere or BGE reranker to your week-6 RAG
2. [ ] New pipeline: retrieve top-50 hybrid → rerank to top-5 → generate
3. [ ] Run week-7 eval suite. Record the lift on retrieval recall and faithfulness.
4. [ ] Add query rewriting: small LLM rewrites query into 3 variants, retrieve for each, dedupe, rerank
5. [ ] Re-run evals. Record second lift.
6. [ ] README: report exact numbers ("Reranking +12% recall@5, query rewriting +4% on top of that")

## ✅ Done when
- [ ] You can quote the % improvement reranking bought you on your data
- [ ] You can articulate when reranking *hurts* (small corpus, well-formed queries)

## 🎯 Stretch
- [ ] Read [the BEIR paper](https://arxiv.org/abs/2104.08663) — canonical retrieval benchmark.

---

## What I built

## What I learned

## What I got wrong
