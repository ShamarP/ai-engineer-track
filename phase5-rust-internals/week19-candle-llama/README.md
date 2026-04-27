# Week 19 — Candle deep dive: implement Llama-3

**Why this week:** candle is HuggingFace's pure-Rust ML framework — the most direct path from "I know Rust" to "I can implement models in Rust." Implementing a Llama forward pass touches every important transformer concept.

## 📖 Read (~6 hours)
- [ ] **DMLS Ch 10** — *Infrastructure and Tooling for MLOps* (light skim)
- [ ] **candle-book** ([github.com/huggingface/candle/tree/main/candle-book](https://github.com/huggingface/candle/tree/main/candle-book)) — read fully
- [ ] **`candle-examples/examples/llama`** source — read end-to-end before writing your own
- [ ] **Touvron et al., 2023, *Llama: Open and Efficient Foundation Language Models*** ([arxiv 2302.13971](https://arxiv.org/abs/2302.13971)). Sections **2**, **3.1**.
- [ ] **Llama-3 model card / blog post** — focus on architectural choices (RoPE scaling, GQA)
- [ ] **Su et al., 2021, *RoFormer: Enhanced Transformer with Rotary Position Embedding*** ([arxiv 2104.09864](https://arxiv.org/abs/2104.09864)). Sections **1**, **3.4**.

Note files: `notes/papers/touvron-2023-llama.md`, `notes/papers/su-2021-rope.md`, `notes/books/candle-book.md`.

## 🧠 Concepts to internalize
- [ ] Tensor operations in Rust: shapes, dtypes, devices (CPU / Metal / CUDA)
- [ ] How candle handles autograd vs. PyTorch (lazy evaluation, traced graphs)
- [ ] safetensors: the modern model weight format (vs. pickle's security disaster)
- [ ] RMSNorm vs. LayerNorm — Llama uses RMSNorm; why
- [ ] RoPE vs. sinusoidal positional encoding — how rotary works
- [ ] GQA (grouped-query attention) — how Llama-3 reduces KV cache without quality loss

## 🛠 Build
1. [ ] Implement Llama-3-8B forward pass in candle, weights loaded from HF safetensors
2. [ ] Implement RMSNorm, RoPE, GQA from primitives (don't black-box the candle Llama example)
3. [ ] Greedy decode + temperature sampling + top-p
4. [ ] Verify: same output as `transformers` (HF Python) for the same prompt with greedy decoding
5. [ ] Benchmark: tokens/sec on CPU vs. Metal (if Mac) vs. small CUDA box
6. [ ] README: include the verification check and the benchmark table

## ✅ Done when
- [ ] Generates coherent text matching transformers reference on greedy
- [ ] You can explain RoPE on a whiteboard with the rotation matrix

## 🎯 Stretch
- [ ] Add a basic KV cache (sets up Week 20).

---

## What I built

## What I learned

## What I got wrong
