# Week 4 — Prompt playground

**Why this week:** the cheapest, fastest, most-overlooked optimization. Most LLM bugs are prompt bugs. Most cost overruns are prompt overruns.

## 📖 Read (~4 hours)
- [ ] **AIE Ch 5** — *Prompt Engineering*. Take notes on her taxonomy.
- [ ] **Anthropic, *Prompt engineering* docs** ([docs.anthropic.com](https://docs.anthropic.com)) — read all 8 sub-pages of the overview
- [ ] **Wei et al., 2022, *Chain-of-Thought Prompting Elicits Reasoning*** ([arxiv 2201.11903](https://arxiv.org/abs/2201.11903)). Sections **1**, **2**, **3**, **6**. Look at Figures 1, 6, 8.
- [ ] **Wang et al., 2022, *Self-Consistency Improves Chain of Thought*** ([arxiv 2203.11171](https://arxiv.org/abs/2203.11171)). Skim — sample multiple CoTs, vote.

Note files: `notes/papers/wei-2022-cot.md`, `notes/books/aie-ch05.md`.

## 🧠 Concepts to internalize
- [ ] The three knobs: prompt content, sampling parameters (temperature, top-p), output format
- [ ] Few-shot > instructions > zero-shot, on hard tasks
- [ ] Chain-of-thought: why "think step by step" works (more compute per token output)
- [ ] Structured outputs: JSON mode, function calling, constrained decoding (Outlines, Instructor)
- [ ] Cost accounting: input × input price + output × output price; cached tokens cost much less
- [ ] Prompt caching (Anthropic, OpenAI) — why a stable prefix matters

## 🛠 Build
1. [ ] CLI in Python: takes a task description + 50 test inputs
2. [ ] Runs the task through 3 models (e.g., Claude Sonnet 4.6, GPT-4o-mini, Llama-3.1-70B via Together)
3. [ ] Each model × 3 strategies: zero-shot, few-shot, CoT
4. [ ] Logs to SQLite: model, strategy, input, output, latency, input/output tokens, cost
5. [ ] Generates a markdown report ranking strategies by quality (judge model) and cost
6. [ ] README: include your report on a real task you care about (e.g., classifying your unread emails)

## ✅ Done when
- [ ] One command produces a reproducible cost-vs-quality table for one real task
- [ ] You can quote, from memory, cost-per-million for Claude Sonnet, GPT-4o-mini, and one open model

## 🎯 Stretch
- [ ] Add prompt caching for Claude. Measure savings on a long-prefix prompt.

---

## What I built

## What I learned

## What I got wrong
