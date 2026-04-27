# Phase 5 — Rust ML Internals (Weeks 18–21)

**Goal:** go from "I know Rust" to "I can implement models and inference systems in Rust." Finish with your own working mini inference engine.

This phase doubles down on Rust after the foundations laid in Phase 4. By Week 21 you have a working OSS inference engine — a portfolio piece almost no one else has.

## Weeks
- [Week 18 — Tokenizers in Rust](./week18-tokenizers-rust)
- [Week 19 — Candle deep dive: implement Llama-3](./week19-candle-llama)
- [Week 20 — Build a mini inference engine](./week20-mini-inference-engine)
- [Week 21 — Rust capstone (spec decoding / PR / OSS)](./week21-rust-capstone)

## Anchor reading
- HuggingFace `tokenizers` crate source
- HuggingFace `candle` codebase + candle-book
- vLLM source (`scheduler.py`, `block_manager.py`, `llm_engine.py`)
- Sennrich et al. *BPE*; Kudo & Richardson *SentencePiece*
- Touvron et al. *Llama*; Su et al. *RoPE*
- Dao *FlashAttention-2*
- Leviathan et al. *Speculative Decoding*
- DMLS Ch 7, 8, 10 (light skim — systems-thinking pairing)
