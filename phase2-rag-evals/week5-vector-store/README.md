# Week 5 — Vector store + embeddings

**Why this week:** every RAG, every memory system, every semantic-search tool you'll build runs on embeddings. Get the geometry, the indexing, and the gotchas in your hands.

## 📖 Read (~4 hours)
- [ ] **Reimers & Gurevych, 2019, *Sentence-BERT*** ([arxiv 1908.10084](https://arxiv.org/abs/1908.10084)). Sections **1**, **3**, **4 (STS only)**.
- [ ] **OpenAI text-embedding-3 docs** + note that **Anthropic** has no native embeddings
- [ ] **pgvector README** + the `<->` (L2), `<#>` (inner product), `<=>` (cosine) operators
- [ ] **Pinecone or Weaviate "Vector DB 101"** — pick one, read their HNSW explainer
- [ ] **Malkov & Yashunin, 2018, *HNSW*** ([arxiv 1603.09320](https://arxiv.org/abs/1603.09320)) — figures 1, 2 are enough

Note files: `notes/papers/reimers-2019-sbert.md`, `notes/papers/malkov-2018-hnsw.md`.

## 🧠 Concepts to internalize
- [ ] Embedding = fixed-length vector; close (cosine) for semantically similar inputs
- [ ] Why cosine, not Euclidean: magnitude carries no semantic signal in most embedding models
- [ ] ANN vs. exact: at scale you trade recall for speed
- [ ] HNSW intuition: small-world graphs, layered, log-time search
- [ ] Embedding model quality varies wildly — you must evaluate on *your* data
- [ ] Chunking strategy *changes* what embeddings represent (next week)

## 🛠 Build
1. [ ] Stand up Postgres + `pgvector` locally (Docker fine)
2. [ ] Pick 10k of your own documents (Pocket, Readwise, your notes folder, Slack export)
3. [ ] Embed with `text-embedding-3-small` (cheap), store in pgvector with HNSW index
4. [ ] CLI: `search "query"` returns top-5 with distance scores
5. [ ] Pick 30 queries you can hand-judge. Score top-1 relevance. Compute hit rate.
6. [ ] README: report your hit rate + three failure modes you observed

## ✅ Done when
- [ ] Sub-100ms similarity search over 10k docs from your laptop
- [ ] You can explain HNSW to someone in 60 seconds without the paper

## 🎯 Stretch
- [ ] Re-embed with `text-embedding-3-large`. Worth the 6.5x cost? Find out.

---

## What I built

## What I learned

## What I got wrong
