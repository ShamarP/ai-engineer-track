# Week 18 — Tokenizers in Rust

**Why this week:** tokenization is the most-deployed Rust code in AI — HuggingFace's `tokenizers` crate is called by every transformers user. Re-implementing BPE in Rust cements your fundamentals through real, performance-critical code.

## 📖 Read (~5 hours)
- [ ] **DMLS Ch 7** — *Model Deployment and Prediction Service* (light skim)
- [ ] **HuggingFace `tokenizers` crate source** ([github.com/huggingface/tokenizers](https://github.com/huggingface/tokenizers)) — read `tokenizers/src/tokenizer/mod.rs` and `tokenizers/src/models/bpe/`
- [ ] **Sennrich et al., 2015, *Neural Machine Translation of Rare Words with Subword Units*** ([arxiv 1508.07909](https://arxiv.org/abs/1508.07909)) — the BPE paper, short and foundational
- [ ] **Kudo & Richardson, 2018, *SentencePiece*** ([arxiv 1808.06226](https://arxiv.org/abs/1808.06226))
- [ ] Skim your **GPT-2 tokenizer** notes from Week 2

Note files: `notes/papers/sennrich-2015-bpe.md`, `notes/papers/kudo-2018-sentencepiece.md`, `notes/papers/hf-tokenizers-source.md`.

## 🧠 Concepts to internalize
- [ ] Pre-tokenization (whitespace, punctuation), normalization, BPE merges
- [ ] Why tokenization is one of the largest perf footguns in inference
- [ ] Trie-based fast paths and SIMD opportunities
- [ ] Special tokens, chat templates, byte-level vs. char-level
- [ ] Why HF tokenizers is ~100x faster than Python: ownership + zero-copy

## 🛠 Build
1. [ ] Port your week-2 Python BPE to Rust from scratch
2. [ ] Implement: `Trainer` (learn merges from corpus), `Tokenizer` (encode/decode), special tokens
3. [ ] Train it on TinyShakespeare with a 256-merge vocab
4. [ ] Verify: same vocab as your Python tokenizer when given the same data
5. [ ] Benchmark: encode a 1MB text. Yours vs. Python vs. HF `tokenizers`. Report speeds.
6. [ ] README: explain one Rust-specific decision (zero-copy strings? `Cow<str>`? hashmap choice?)

## ✅ Done when
- [ ] Output matches your Python tokenizer to 100% on a held-out corpus
- [ ] < 10x slower than HF `tokenizers` (HF is hand-tuned with parallelism; getting close is enough)

## 🎯 Stretch
- [ ] Implement a byte-level pre-tokenizer (GPT-2 style) and parallelize encoding with `rayon`.

---

## What I built

## What I learned

## What I got wrong
