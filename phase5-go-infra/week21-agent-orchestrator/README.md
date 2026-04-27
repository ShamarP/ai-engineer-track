# Week 21 — Multi-agent orchestrator

**Why this week:** the capstone of the Go phase. A long-running orchestration service is the kind of thing actual companies pay for.

## 📖 Read (~4 hours)
- [ ] **DMLS Ch 8** — *Data Distribution Shifts and Monitoring*
- [ ] **Wu et al., 2023, *AutoGen*** ([arxiv 2308.08155](https://arxiv.org/abs/2308.08155)). Sections **1**, **3**, **4**.
- [ ] **Hong et al., 2023, *MetaGPT*** ([arxiv 2308.00352](https://arxiv.org/abs/2308.00352)). Sections **1**, **3**, **5**.
- [ ] **Anthropic, *Building Effective Agents*** — re-read the orchestrator-workers section

Note files: `notes/papers/wu-2023-autogen.md`, `notes/papers/hong-2023-metagpt.md`.

## 🧠 Concepts to internalize
- [ ] Multi-agent systems: roles, conversation, termination
- [ ] When *not* to use multiple agents: most of the time
- [ ] Queue-based orchestration: durable, observable, retryable
- [ ] Idempotency: tool calls must be safe to retry
- [ ] Backpressure: how do you protect upstream APIs from your agent army?
- [ ] Chaos testing: random tool failures, model timeouts, network drops

## 🛠 Build
1. [ ] Go service: HTTP API receives a "task" (high-level goal in JSON)
2. [ ] Service spawns a manager agent + N worker agents (configurable)
3. [ ] Manager decomposes the task, dispatches subtasks to workers via Redis (or NATS) queue
4. [ ] Workers execute, return results; manager synthesizes
5. [ ] Each agent's calls traced (OpenTelemetry → local Jaeger)
6. [ ] Chaos test middleware: inject 20% tool-call failures and 10% LLM timeouts. Service must survive.
7. [ ] README: include a Mermaid architecture diagram and the chaos test results

## ✅ Done when
- [ ] Service handles 10 concurrent tasks; chaos test runs to completion with zero crashes
- [ ] You can sketch the architecture on a whiteboard from memory

## 🎯 Stretch
- [ ] Add a web UI (Templ + HTMX in Go) showing live agent traces.

---

## What I built

## What I learned

## What I got wrong
