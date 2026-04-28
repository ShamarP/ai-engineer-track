# Phase 5 — Rust ML Internals (Weeks 18–21)

**Goal:** go from "I know Rust" to "I can implement models and inference systems in Rust." Finish with your own working mini inference engine.

This phase doubles down on Rust after the foundations laid in Phase 4. By Week 21 you have a working OSS inference engine — a portfolio piece almost no one else has.

## Weeks
- [Week 18 — GGUF format + INT8 quantization in Rust](./week18-gguf-quantization)
- [Week 19 — Candle deep dive: implement Phi-3.5-mini or Qwen2.5-1.5B](./week19-candle-llama)
- [Week 20 — Build a mini inference engine](./week20-mini-inference-engine)
- [Week 21 — Rust capstone (spec decoding / PR / OSS)](./week21-rust-capstone)

## Anchor reading
- GGUF specification + llama.cpp `gguf.h/c`
- Dettmers *LLM.int8()*; Lin et al. *AWQ*; Frantar et al. *GPTQ*
- HuggingFace `candle` codebase + candle-book
- vLLM source (`scheduler.py`, `block_manager.py`, `llm_engine.py`)
- Touvron et al. *Llama*; Su et al. *RoPE*; Phi-3 / Qwen2 technical reports
- Dao *FlashAttention-2*
- Leviathan et al. *Speculative Decoding*
- DMLS Ch 7, 8, 10 (light skim — systems-thinking pairing)
