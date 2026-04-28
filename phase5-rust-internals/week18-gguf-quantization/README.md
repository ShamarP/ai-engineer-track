# Week 18 — GGUF format + INT8 quantization in Rust

**Why this week:** every production inference system uses quantization. GGUF is the binary model format that powers llama.cpp / Ollama / LM Studio. Implementing both forces you to read binary formats, understand fixed-point math, and reason about memory layout — all real low-level skills you don't get from agent-building.

## 📖 Read (~5 hours)
- [ ] **DMLS Ch 7** — *Model Deployment and Prediction Service* (light skim)
- [ ] **GGUF format specification** ([github.com/ggerganov/ggml/blob/master/docs/gguf.md](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)) — read fully
- [ ] **llama.cpp `gguf.h` and `gguf.c`** — the canonical reader/writer
- [ ] **Dettmers et al., 2022, *LLM.int8()*** ([arxiv 2208.07339](https://arxiv.org/abs/2208.07339)). Sections **1**, **3**, **4**.
- [ ] **Lin et al., 2023, *AWQ: Activation-aware Weight Quantization*** ([arxiv 2306.00978](https://arxiv.org/abs/2306.00978)). Sections **1**, **3**, **4**.
- [ ] Skim **Frantar et al., 2022, *GPTQ*** ([arxiv 2210.17323](https://arxiv.org/abs/2210.17323))

Note files: `notes/papers/gguf-spec.md`, `notes/papers/dettmers-2022-llm-int8.md`, `notes/papers/lin-2023-awq.md`.

## 🧠 Concepts to internalize
- [ ] Binary model format anatomy: header, metadata KVs, tensor info, aligned tensor data
- [ ] INT8 quantization: per-channel vs. per-tensor scale; symmetric vs. asymmetric
- [ ] INT4 quantization: group sizes, packing two 4-bit values into one byte
- [ ] The quantize → dequantize → operate cycle in inference
- [ ] Outliers: why naive INT8 destroys quality (LLM.int8 mixed-precision insight)
- [ ] AWQ vs. GPTQ vs. naive RTN: tradeoffs in calibration cost and quality
- [ ] Why quantization-aware training beats post-training quant at low bit-widths

## 🛠 Build
1. [ ] Implement a GGUF reader in Rust: parse header, metadata, tensor info, mmap the weights
2. [ ] Load a real GGUF file (e.g., Phi-3.5-mini Q8_0 from HuggingFace) and print metadata
3. [ ] Implement INT8 symmetric quantization for `f32 → i8`: compute scale, quantize, dequantize
4. [ ] Quantize a small candle model end-to-end (e.g., a sentence-embedding model) and measure quality loss vs. fp32 baseline
5. [ ] Bonus: implement INT4 group quantization (group-size 32 or 64) and compare
6. [ ] README: include quality/size table — fp32 vs. INT8 vs. INT4

## ✅ Done when
- [ ] You can load any GGUF model and print every tensor's name, shape, and quantization type
- [ ] Your INT8 quantization preserves ≥95% of fp32 quality on a downstream task you choose

## 🎯 Stretch
- [ ] Implement AWQ from the paper. Calibrate on a small dataset.

---

## What I built

## What I learned

## What I got wrong
