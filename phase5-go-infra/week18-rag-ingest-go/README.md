# Week 18 — RAG ingestion in Go

**Why this week:** Go is the easiest of the three languages on this roadmap. You can be productive in a week.

## 📖 Read (~5 hours, plus practice)
- [ ] **DMLS Ch 7** — *Model Deployment and Prediction Service*
- [ ] **A Tour of Go** ([go.dev/tour](https://go.dev/tour)) — work through every section
- [ ] **Effective Go** ([go.dev/doc/effective_go](https://go.dev/doc/effective_go)) — read every word
- [ ] **Dave Cheney, *Practical Go*** ([dave.cheney.net](https://dave.cheney.net)) — best style guide

Note files: `notes/books/dmls-ch07.md`, `notes/books/effective-go.md`.

## 🧠 Concepts to internalize
- [ ] Goroutines: cheap, you can spawn 100k of them; channels for communication
- [ ] "Don't communicate by sharing memory; share memory by communicating" — the Go mantra
- [ ] Interfaces are implicit — types satisfy them by structure, not declaration
- [ ] Error handling: explicit `if err != nil`; no exceptions; wrap with `fmt.Errorf("...: %w", err)`
- [ ] Zero values are useful — design your structs so the zero value is meaningful
- [ ] Single static binary: `go build` produces one file you can scp anywhere

## 🛠 Build
1. [ ] Port your week-6 RAG *ingestion pipeline* to Go (just ingestion; retrieval comes later)
2. [ ] Use `pgx` (Postgres), `goquery` (HTML), `github.com/sashabaranov/go-openai`
3. [ ] Goroutines for parallel chunk embedding (rate-limited to API limits)
4. [ ] Run on the same 100 documents from week 6
5. [ ] Benchmark: time the Python version vs. the Go version
6. [ ] README: report the speedup and explain *where* in the pipeline it came from

## ✅ Done when
- [ ] Go ingestion is at least as fast as Python (it almost certainly will be much faster)
- [ ] You can explain the difference between buffered and unbuffered channels

## 🎯 Stretch
- [ ] Add OpenTelemetry tracing to the ingestion pipeline.

---

## What I built

## What I learned

## What I got wrong
