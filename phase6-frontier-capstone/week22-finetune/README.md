# Week 22 — Fine-tuning mastery (QLoRA + DPO + light distillation)

**Why this week:** fine-tuning is what separates "prompt user" from "model practitioner." A focused week covers QLoRA (parameter-efficient SFT), DPO (preference alignment without a reward model), and a small distillation finisher. One sharp week beats two diluted ones.

## 📖 Read (~5 hours)
- [ ] **AIE Ch 7** — *Finetuning*; **Ch 8** — *Dataset Engineering*
- [ ] **Hu et al., 2021, *LoRA*** ([arxiv 2106.09685](https://arxiv.org/abs/2106.09685)). Sections **1**, **3**, **4**.
- [ ] **Dettmers et al., 2023, *QLoRA*** ([arxiv 2305.14314](https://arxiv.org/abs/2305.14314)). Sections **1**, **3**, **4**.
- [ ] **Rafailov et al., 2023, *DPO*** ([arxiv 2305.18290](https://arxiv.org/abs/2305.18290)). Sections **1**, **3**, **4**.
- [ ] **Hsieh et al., 2023, *Distilling Step-by-Step!*** ([arxiv 2305.02301](https://arxiv.org/abs/2305.02301)). Sections **1**, **3**.
- [ ] **HuggingFace `trl` and `peft` docs** — the libraries you'll use

Note files: `notes/papers/hu-2021-lora.md`, `notes/papers/dettmers-2023-qlora.md`, `notes/papers/rafailov-2023-dpo.md`, `notes/papers/hsieh-2023-distilling-step-by-step.md`.

## 🧠 Concepts to internalize
- [ ] LoRA: freeze the base, train low-rank adapters; tiny disk footprint vs. full fine-tune
- [ ] QLoRA: load base in 4-bit, train LoRA in fp16 — fine-tune 70B on a single 80GB GPU
- [ ] DPO: fine-tune directly on preference pairs without a separate reward model. Replacing PPO in 2024+.
- [ ] Dataset construction is 80% of success. Spend your time here.
- [ ] When to fine-tune vs. prompt: tone/style, narrow domain, latency-sensitive, ≥1k high-quality examples
- [ ] When *not* to: knowledge updates (use RAG), most one-off tasks (prompt is faster)
- [ ] Distillation as fine-tuning's cousin: traces from a frontier model become training data for a small one

## 🛠 Build
1. [ ] Identify a task from your W4 prompt playground where the best prompt still loses ≥30% of the time
2. [ ] Build 1k-example SFT set + 200-example eval set (frontier model labels; hand-fix 20%)
3. [ ] **QLoRA SFT** on `Llama-3.1-8B-Instruct` via Modal/RunPod/Lambda (~$3–10 in GPU time)
4. [ ] **DPO** on top of SFT: generate 200 preference pairs by hand-judging your SFT outputs vs. the prompt baseline; train DPO for 1 epoch
5. [ ] **Light distillation finisher**: take 500 traces from your best agent (W13) using a frontier model; SFT a 3B model on them; report the cost/quality delta
6. [ ] README: win-rate table for prompt baseline vs. SFT vs. SFT+DPO; cost-per-1k-queries comparison for the 3B distilled model

## ✅ Done when
- [ ] SFT+DPO 8B beats prompt-only frontier model on your task by ≥10 pts
- [ ] You can explain LoRA vs. QLoRA vs. full fine-tune and when each is correct
- [ ] You can articulate why DPO replaced PPO in most modern alignment

## 🎯 Stretch
- [ ] Deploy the fine-tuned model on Modal or Replicate
- [ ] Wire it into your week-15 Rust proxy as another backend

## GPU budget
- QLoRA SFT: ~1–2 hours on an A100 (80GB) — about $3–8 on Modal/Lambda
- DPO: ~1 hour additional
- Distillation: ~30 min on a smaller GPU (A10/A6000)
- **Total: $5–15 for the whole week**

---

## What I built

## What I learned

## What I got wrong
