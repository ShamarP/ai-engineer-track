# Week 11 — Persistent memory

**Why this week:** agents without memory are toys. Real agents remember users, preferences, prior sessions, and their own past mistakes.

## 📖 Read (~5 hours)
- [ ] **Park et al., 2023, *Generative Agents*** ([arxiv 2304.03442](https://arxiv.org/abs/2304.03442)). Sections **1**, **3**, **4**. The "memory stream" idea is what to internalize.
- [ ] **Packer et al., 2023, *MemGPT*** ([arxiv 2310.08560](https://arxiv.org/abs/2310.08560)). Sections **1**, **3**.
- [ ] **Pinecone or Weaviate "Long-term memory" guide**

Note files: `notes/papers/park-2023-generative-agents.md`, `notes/papers/packer-2023-memgpt.md`.

## 🧠 Concepts to internalize
- [ ] Memory taxonomy: working (in-context scratchpad), episodic (events with time), semantic (extracted facts), procedural (learned skills)
- [ ] Retrieval-as-memory pattern: store everything, retrieve what's relevant per turn
- [ ] Summarization buffers: when context fills, summarize old turns, replace
- [ ] MemGPT: model has tools to read/write its own memory, OS-style
- [ ] Reflection scoring (Generative Agents): not all memories are equal — score by importance, recency, relevance
- [ ] The fundamental tradeoff: more memory = larger context = higher cost, more attention dilution

## 🛠 Build
1. [ ] Add persistent memory to your week-10 agent
2. [ ] SQLite store with: id, timestamp, content, embedding, importance (0–10, scored by an LLM at insert)
3. [ ] Each turn: retrieve top-5 memories by `importance × recency_decay × cosine_similarity`
4. [ ] After each session: an LLM summarizes the session into 2–3 "what I learned" memories, persisted
5. [ ] Test: 5-turn conversation Monday. Restart Tuesday. Verify the agent remembers a fact you told it Monday.
6. [ ] README: walk through one cross-session example with actual memory rows shown

## ✅ Done when
- [ ] Agent demonstrably remembers user preferences across restarts
- [ ] You can explain the memory-scoring formula and why each term is in it

## 🎯 Stretch
- [ ] Memory consolidation: periodically merge similar memories to prevent bloat.

---

## What I built

## What I learned

## What I got wrong
