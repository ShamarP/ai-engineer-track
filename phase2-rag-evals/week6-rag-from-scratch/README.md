# Week 6 — RAG from scratch (no framework)

**Why this week:** most "RAG" in the wild is a one-line LangChain call that nobody understands. Build it without a framework once and you'll debug the framework versions ten times faster.

## 📖 Read (~5 hours)
- [ ] **AIE Ch 6** — *RAG and Agents*, RAG sections only this week
- [ ] **Lewis et al., 2020, *Retrieval-Augmented Generation*** ([arxiv 2005.11401](https://arxiv.org/abs/2005.11401)). Sections **1**, **2**, **3**.
- [ ] **Gao et al., 2022, *HyDE*** ([arxiv 2212.10496](https://arxiv.org/abs/2212.10496)). 8 pages, read all of it.
- [ ] **Microsoft Azure RAG patterns** OR **OpenAI cookbook RAG patterns** — pick one
- [ ] **Anthropic, *Contextual Retrieval*** (Sept 2024 blog post)

Note files: `notes/papers/lewis-2020-rag.md`, `notes/papers/gao-2022-hyde.md`, `notes/books/aie-ch06-rag.md`.

## 🧠 Concepts to internalize
- [ ] RAG pipeline: ingest → chunk → embed → index → retrieve → rerank → generate
- [ ] Chunking strategies: fixed-size, recursive, semantic, document-structure-aware
- [ ] Retrieval ≠ reading: top-K matters; precision vs. recall
- [ ] Hybrid search: BM25 + dense vector usually beats either alone
- [ ] HyDE: generate a hypothetical answer, embed *that*, retrieve
- [ ] Contextual retrieval: prepend chunk-level context to each chunk before embedding
- [ ] Citations are non-negotiable — hallucination is the fail mode you must close

## 🛠 Build
1. [ ] **No framework**. Just `requests`/`anthropic`/`openai`, `psycopg`, your week-5 vector store
2. [ ] Ingest 100 long-form documents (your blog, papers you've read, etc.)
3. [ ] Three chunking strategies: 500-token fixed, 200-token-with-overlap, paragraph-level
4. [ ] Hybrid search: pgvector cosine + Postgres FTS, blended with reciprocal rank fusion
5. [ ] HyDE as an optional flag
6. [ ] `chat` CLI that answers questions with inline citations like `[doc:5, chunk:3]`
7. [ ] README: 5 example Q&A interactions with your assessment of correctness

## ✅ Done when
- [ ] Citations appear and are correct (you click through to verify)
- [ ] You can articulate the chunking-strategy tradeoff for your corpus

## 🎯 Stretch
- [ ] Implement contextual retrieval. Measure the lift.

---

## What I built

## What I learned

## What I got wrong
