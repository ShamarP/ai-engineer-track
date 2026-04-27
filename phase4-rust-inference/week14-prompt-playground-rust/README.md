# Week 14 — Rust fundamentals (prompt playground in Rust)

**Why this week:** Rust's borrow checker is famously frustrating for the first 30 hours. Power through. The mental model rewires how you write *all* code, not just Rust.

## 📖 Read (~6 hours, plus ~6 hours of practice)
- [ ] **The Rust Programming Language ("The Book")** — chapters 1–10 ([doc.rust-lang.org/book](https://doc.rust-lang.org/book))
- [ ] **Rustlings** — install and complete through `move_semantics` (skim ahead to `error_handling` if time)
- [ ] **Jon Gjengset, *Crust of Rust: Lifetime Annotations*** (~1h22m on YouTube) — best lifetime explainer that exists

Note files: `notes/books/rust-book-1-10.md`, `notes/books/crust-of-rust-lifetimes.md`.

## 🧠 Concepts to internalize
- [ ] Ownership: every value has one owner; when the owner goes out of scope, drop runs
- [ ] Borrow rules: many `&` *or* one `&mut`, never both, never outliving the owner
- [ ] Lifetimes are descriptive, not prescriptive — you tell the compiler what *is* true
- [ ] `Result<T, E>` and `?` — error handling without exceptions
- [ ] Traits = interfaces; `impl Trait` and generics
- [ ] `String` vs `&str`, `Vec<T>` vs `&[T]` — owned vs. borrowed
- [ ] Cargo workflow: `cargo new`, `cargo run`, `cargo test`, `cargo clippy`

## 🛠 Build
1. [ ] Port your week-4 prompt playground CLI to Rust
2. [ ] Use `reqwest` (HTTP), `serde` (JSON), `clap` (CLI), `rusqlite` (log)
3. [ ] Match the same evaluation reports as the Python version
4. [ ] Run your old eval data through it. Output should match the Python version byte-for-byte (where deterministic).
5. [ ] README: include three things the borrow checker yelled at you about and how you fixed each

## ✅ Done when
- [ ] Compiles, passes `cargo clippy --all-targets -- -D warnings`, and produces the same results as the Python version
- [ ] You can explain why `let x = &mut y; let z = &y;` doesn't compile

## 🎯 Stretch
- [ ] Read the source of the `tokenizers` crate from HuggingFace — pick one method, trace it end-to-end.

---

## What I built

## What I learned

## What I got wrong
