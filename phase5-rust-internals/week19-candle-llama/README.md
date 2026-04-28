# Week 19 — Candle deep dive: implement a small model

**Why this week:** candle is HuggingFace's pure-Rust ML framework — the most direct path from "I know Rust" to "I can implement models in Rust." A small model (Phi-3.5-mini or Qwen2.5-1.5B) gives you the same low-level lessons (RoPE, GQA, RMSNorm) without 16GB of weights and slow CPU inference.

## 📖 Read (~6 hours)
- [ ] **DMLS Ch 10** — *Infrastructure and Tooling for MLOps* (light skim)
- [ ] **candle-book** ([github.com/huggingface/candle/tree/main/candle-book](https://github.com/huggingface/candle/tree/main/candle-book)) — read fully
- [ ] **`candle-examples/examples/quantized-phi`** OR **`candle-transformers/src/models/qwen2`** — read end-to-end before writing your own
- [ ] **Touvron et al., 2023, *Llama*** ([arxiv 2302.13971](https://arxiv.org/abs/2302.13971)). Sections **2**, **3.1**.
- [ ] **Su et al., 2021, *RoFormer (RoPE)*** ([arxiv 2104.09864](https://arxiv.org/abs/2104.09864)). Sections **1**, **3.4**.
- [ ] Skim **Phi-3 technical report** ([arxiv 2404.14219](https://arxiv.org/abs/2404.14219)) OR **Qwen2 technical report** depending on which you pick

Note files: `notes/papers/touvron-2023-llama.md`, `notes/papers/su-2021-rope.md`, `notes/books/candle-book.md`.

## 🧠 Concepts to internalize
- [ ] Tensor operations in Rust: shapes, dtypes, devices (CPU / Metal)
- [ ] How candle handles autograd vs. PyTorch (lazy evaluation, traced graphs)
- [ ] safetensors: the modern model weight format (vs. pickle's security disaster)
- [ ] RMSNorm vs. LayerNorm — modern models use RMSNorm; why
- [ ] RoPE vs. sinusoidal positional encoding — how rotary works
- [ ] GQA (grouped-query attention) — how it reduces KV cache without quality loss

## 🛠 Build
1. [ ] Pick **Phi-3.5-mini-instruct** (3.8B) or **Qwen2.5-1.5B-Instruct** — load weights from HF safetensors
2. [ ] Implement RMSNorm, RoPE, GQA from primitives (don't black-box the candle example)
3. [ ] Forward pass: token embedding → N × transformer block → final RMSNorm → LM head
4. [ ] Greedy decode + temperature sampling + top-p
5. [ ] Verify: same output as `transformers` (HF Python) for the same prompt with greedy
6. [ ] Benchmark: tokens/sec on CPU vs. Metal. Compare to llama.cpp on the same model.
7. [ ] **Connect to W18**: load the GGUF quantized version of your model using your W18 reader

## ✅ Done when
- [ ] Generates coherent text matching transformers reference on greedy
- [ ] You can explain RoPE on a whiteboard with the rotation matrix
- [ ] Your model runs both fp16 (safetensors) and INT8 (your W18 GGUF reader)

## 🎯 Stretch
- [ ] Add a basic KV cache (sets up Week 20)
- [ ] Or: implement an embedding model (sentence-transformers MiniLM) instead — much smaller, faster, useful for downstream projects.

---

## What I built

## What I learned

## What I got wrong
