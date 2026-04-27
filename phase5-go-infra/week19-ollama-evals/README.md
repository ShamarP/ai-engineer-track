# Week 19 — Ollama-backed eval CLI

**Why this week:** Ollama is the dominant local LLM runtime. Its codebase is a masterclass in writing a usable AI infra product in Go.

## 📖 Read (~5 hours)
- [ ] **DMLS Ch 10** — *Infrastructure and Tooling for MLOps*
- [ ] **The Ollama codebase** ([github.com/ollama/ollama](https://github.com/ollama/ollama)):
  - [ ] `cmd/` — CLI entry points
  - [ ] `server/` — the HTTP server
  - [ ] `llm/` — model loading and inference (CGo bridge to llama.cpp)
  - [ ] `api/` — public API types
  - [ ] Trace one request from `ollama run llama3` to model output
- [ ] **GGUF format spec** ([ggml/docs/gguf.md](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md))

Note files: `notes/books/dmls-ch10.md`, `notes/papers/ollama-codebase-trace.md`.

## 🧠 Concepts to internalize
- [ ] Ollama's model registry: how `ollama pull` works, manifest format, layer reuse (Docker-inspired)
- [ ] The CGo bridge: Go calls into llama.cpp via C ABI
- [ ] The `Modelfile` format: how users compose their own variants
- [ ] Ollama bundles model + system prompt + parameters as one unit
- [ ] Why Ollama uses a *daemon* + CLI architecture

## 🛠 Build
1. [ ] CLI in Go that wraps the Ollama HTTP API
2. [ ] Takes an eval dataset (jsonl: `{"prompt": ..., "expected": ...}`) + a list of local Ollama models
3. [ ] Runs every prompt through every model; scores outputs (LLM-as-judge using a remote frontier model); produces a leaderboard
4. [ ] Streams output to a TUI using `bubbletea`
5. [ ] Saves results to SQLite for re-analysis
6. [ ] README: include a real eval comparison of 3 local models

## ✅ Done when
- [ ] One command runs evals across all your local Ollama models and prints a leaderboard
- [ ] You can describe Ollama's request-flow from CLI to model

## 🎯 Stretch
- [ ] Add quantization-level comparison — same model, different quants, compare quality vs. speed.

---

## What I built

## What I learned

## What I got wrong
