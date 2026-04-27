# Week 9 — Agent foundations (no framework)

**Why this week:** Anthropic's "Building Effective Agents" is the most influential piece in the agent space because it pushes back against framework bloat. Internalize their patterns first; complexity comes later.

## 📖 Read (~4 hours)
- [ ] **AIE Ch 6** — agent sections (the half you skipped in Week 6)
- [ ] **Anthropic, *Building Effective Agents*** ([anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents), Dec 2024). Read every word, **twice**.
- [ ] **Lilian Weng, *LLM Powered Autonomous Agents*** ([lilianweng.github.io](https://lilianweng.github.io/posts/2023-06-23-agent/)). Read planning + memory + tool-use sections in depth.

Note files: `notes/papers/anthropic-building-effective-agents.md`, `notes/papers/weng-2023-agents.md`.

## 🧠 Concepts to internalize
- [ ] Workflow vs. agent: workflows have predetermined paths; agents choose their own
- [ ] Start with the simplest pattern that works: prompt → augmented LLM → workflow → agent. Don't skip steps.
- [ ] Five core patterns: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer
- [ ] Agents = LLM + tool use + loop + termination condition
- [ ] The terminating condition is the hardest part — most agent failures are runaway loops

## 🛠 Build
1. [ ] **No framework**. Hand-roll the loop.
2. [ ] Define 3 tools: `search_web` (Tavily/SerpAPI), `read_file`, `execute_python` (sandboxed via `e2b`)
3. [ ] Loop: while not done → ask LLM for next action → parse tool call → execute → append result → repeat. Hard cap at 10 iterations.
4. [ ] Pick a real multi-step task: "find me 5 recent papers on KV cache compression, summarize each, save to a markdown file"
5. [ ] Run it. Watch it succeed (or fail). Log every step.
6. [ ] README: include the trace of one full run with commentary

## ✅ Done when
- [ ] Your agent solves the multi-step task end-to-end without a framework
- [ ] You can recite Anthropic's five patterns and give a one-sentence example of each

## 🎯 Stretch
- [ ] Implement the orchestrator-workers pattern: one agent spawns sub-agents for parallel sub-tasks.

---

## What I built

## What I learned

## What I got wrong
