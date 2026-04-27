# Week 15 — Async Rust inference proxy (axum + SSE)

**Why this week:** every inference server in production handles thousands of concurrent requests. Async Rust is how.

## 📖 Read (~5 hours)
- [ ] **The Rust Book** — chapters 11–16
- [ ] **tokio docs tutorial** (~2 hours of focused work)
- [ ] **axum docs** — quickstart + the streaming example
- [ ] **Alice Ryhl, *Async: What is blocking?*** ([ryhl.io/blog/async-what-is-blocking/](https://ryhl.io/blog/async-what-is-blocking/))

Note files: `notes/books/rust-book-11-16.md`, `notes/papers/ryhl-async-blocking.md`.

## 🧠 Concepts to internalize
- [ ] `async fn` returns a `Future`; nothing runs until you `.await` or hand it to a runtime
- [ ] Tokio is *the* runtime — single-threaded vs. multi-threaded modes
- [ ] `Arc<Mutex<T>>` and `Arc<RwLock<T>>` — bread and butter of async shared state
- [ ] Channels (`mpsc`, `broadcast`) for actor-style designs
- [ ] Why blocking inside async is a footgun (use `spawn_blocking`)
- [ ] Streaming responses: `axum::response::sse::Sse` or write your own `Stream`

## 🛠 Build
1. [ ] `axum` HTTP server exposing `/v1/chat/completions` (OpenAI-compatible)
2. [ ] Proxies to upstream OpenAI, Anthropic, or Together
3. [ ] Streams response back token-by-token via SSE
4. [ ] Per-API-key concurrent request semaphore
5. [ ] Logs every request: route, latency, tokens in/out, status
6. [ ] Stress-test: 100 concurrent requests through your proxy. Compare latency vs. direct API.
7. [ ] README: include a load-test report

## ✅ Done when
- [ ] SSE streaming works end-to-end (`curl --no-buffer` to verify)
- [ ] `tokio-console` shows your proxy handling 100 concurrent connections cleanly

## 🎯 Stretch
- [ ] Add prompt caching — proxy detects identical prefixes, returns cached completions.

---

## What I built

## What I learned

## What I got wrong
