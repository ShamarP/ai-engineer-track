# Week 2 — GPT from scratch (tokenizer + transformer)

**Why this week:** tokens are the unit you'll spend the next 23 weeks counting, paying for, debugging, and optimizing. Attention is the mechanism that powers every model you'll touch.

## 📖 Read (~6 hours)
- [ ] **AIE Ch 2** — *Understanding Foundation Models*. Focus: training data, scaling laws, model architectures, post-training.
- [ ] **Vaswani et al., 2017, *Attention Is All You Need*** ([arxiv 1706.03762](https://arxiv.org/abs/1706.03762)). Sections **3.2**, **3.2.2**, **3.5**, **Figures 1–2**. Skip the RNN comparison tables.
- [ ] **Karpathy** — [*Let's build the GPT Tokenizer*](https://www.youtube.com/watch?v=zduSFxRajkE) (~2h13m). Code along.
- [ ] **Karpathy** — [*Let's build GPT: from scratch, in code, spelled out*](https://www.youtube.com/watch?v=kCc8FmEb1nY) (~1h57m). Code along.

Note files: `notes/papers/vaswani-2017-attention.md`, `notes/books/karpathy-03-tokenizer.md`, `notes/books/karpathy-04-gpt.md`.

## 🧠 Concepts to internalize
- [ ] BPE: why merges, why a vocab size, why GPT tokenizers split numbers and whitespace weirdly
- [ ] The tensor shape `(batch, sequence, embedding_dim)` — burn it in
- [ ] Self-attention: query asks "who's relevant to me?", keys answer, values are pulled
- [ ] Why we divide by `sqrt(d_k)` in scaled dot-product attention
- [ ] Multi-head attention as parallel "channels of understanding"
- [ ] Why positional encodings exist — attention is permutation-invariant without them
- [ ] Causal mask: why decoder-only models triangle-mask the attention matrix

## 🛠 Build
1. [ ] Implement BPE tokenizer from scratch on TinyShakespeare (~150 lines, one file)
2. [ ] Implement a transformer block: `LayerNorm → MHSA → residual → LayerNorm → MLP → residual`
3. [ ] Stack 4 blocks into a ~50k-param model
4. [ ] Train on TinyShakespeare for ~10 minutes (CPU okay, free Colab T4 better)
5. [ ] Sample text. Get it to be *recognizably Shakespearean-bad*.
6. [ ] In the README, walk through attention with a worked example for a 3-token sequence

## ✅ Done when
- [ ] You can draw a transformer block from memory, label every tensor's shape, explain each LayerNorm
- [ ] You can answer "why does attention scale O(n²) with sequence length?" without thinking

## 🎯 Stretch
- [ ] Read [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/) (Jay Alammar)
- [ ] Add KV caching to your model

---

## What I built
*(fill in when done)*

## What I learned
*(2–3 ideas)*

## What I got wrong
*(something redone, and why)*
