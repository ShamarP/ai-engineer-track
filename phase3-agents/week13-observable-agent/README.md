# Week 13 — Observable agent (tracing + evals)

**Why this week:** you cannot debug an agent you cannot see. Tracing is the difference between "it worked once" and "it works."

## 📖 Read (~4 hours)
- [ ] **AIE Ch 10** — *AI Engineering Architecture and User Feedback*
- [ ] **Eugene Yan, *Patterns for Building LLM-based Systems & Products*** ([eugeneyan.com](https://eugeneyan.com)) — read patterns on Evaluation, Guardrails, Defensive UX, Observability
- [ ] Pick one and read its docs end-to-end: **LangSmith**, **Braintrust**, or **Arize Phoenix** (Phoenix is open-source if you want self-hosted)
- [ ] **OpenTelemetry GenAI semantic conventions** ([opentelemetry.io](https://opentelemetry.io))

Note files: `notes/books/aie-ch10.md`, `notes/papers/yan-llm-patterns.md`.

## 🧠 Concepts to internalize
- [ ] A trace = a tree of spans; each span is one LLM call, one tool call, or one logical step
- [ ] Capture: inputs, outputs, prompts, tokens, latency, model, temperature, errors
- [ ] Replay: rerun a trace with a different prompt or model — most valuable debugging primitive
- [ ] Datasets = traces you've labeled. Evals run against datasets. Production ↔ evals are a closed loop.
- [ ] Online vs. offline evals — when each fires
- [ ] Guardrails: input validation (PII, injection), output validation (refusal, hallucination)

## 🛠 Build
1. [ ] Wire your week-12 agent to your chosen tracing tool. Every LLM call, every tool call traced.
2. [ ] Run 50 real interactions. Save the traces.
3. [ ] Pick 5 failure traces. For each: read the trace → hypothesize cause → replay with a fix → verify.
4. [ ] Convert the 5 traces into an eval dataset
5. [ ] Add a regression run that uses this dataset against your agent
6. [ ] README: include the 5 case studies — failure → diagnosis → fix → regression-locked

## ✅ Done when
- [ ] You can show a trace of a real failure, walk through it span-by-span, explain what broke
- [ ] The 5 failures are now eval cases that fail-loudly if reintroduced

## 🎯 Stretch
- [ ] Add a guardrail layer — input PII filter, output refusal classifier. Trace it.

---

## What I built

## What I learned

## What I got wrong
