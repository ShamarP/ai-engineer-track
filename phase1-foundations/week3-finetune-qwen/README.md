# Week 3 — Fine-tune Qwen 0.5B

**Why this week:** a trained transformer isn't ChatGPT. The pipeline that turns one into the other (pretrain → SFT → RLHF) is the recipe behind every modern model. You should know the steps.

## 📖 Read (~5 hours)
- [ ] **DMLS Ch 1–2** — *Overview of ML Systems*, *Introduction to ML Systems Design*. Skim mode — collecting systems-thinking framing.
- [ ] **Brown et al., 2020, *Language Models are Few-Shot Learners*** (GPT-3, [arxiv 2005.14165](https://arxiv.org/abs/2005.14165)). Sections **1**, **2**, **3.1**, **3.4**, **5**. Skim benchmark tables.
- [ ] **Ouyang et al., 2022, *Training language models to follow instructions with human feedback*** (InstructGPT, [arxiv 2203.02155](https://arxiv.org/abs/2203.02155)). Sections **1**, **3**, **4**. Internalize Figure 2 (SFT → RM → PPO).

Note files: `notes/papers/brown-2020-gpt3.md`, `notes/papers/ouyang-2022-instructgpt.md`, `notes/books/dmls-ch01-02.md`.

## 🧠 Concepts to internalize
- [ ] Pretraining vs. SFT vs. RLHF — what data each uses, what objective each optimizes
- [ ] "Emergent abilities" — what scaling buys you, the metric-artifact debate
- [ ] In-context learning: few-shot works because the model was implicitly trained to continue patterns
- [ ] Reward model: a small model trained on human preference data, used as a learned loss function
- [ ] PPO at a conceptual level (you don't need the math, just the role)
- [ ] Why we need RLHF: SFT alone produces models that hallucinate confidently and refuse poorly

## 🛠 Build
1. [ ] Pick a small open model: `Qwen/Qwen2.5-0.5B` (fits on free Colab T4)
2. [ ] Pick a focused task (e.g., "summarize a Hacker News comment in one sentence")
3. [ ] Generate a 200-row dataset (frontier model labels; spot-check 30 by hand)
4. [ ] Fine-tune with HuggingFace `trl`'s `SFTTrainer` (full fine-tune is fine at this size)
5. [ ] Evaluate: base vs. fine-tuned on a held-out 50, scored by Claude or GPT-4o as judge
6. [ ] README: report base vs. tuned win rate. If your tuned model loses, explain why.

## ✅ Done when
- [ ] Tuned model wins ≥60% on your eval set
- [ ] You can sketch the InstructGPT 3-stage pipeline on a whiteboard with the data type at each stage

## 🎯 Stretch
- [ ] Re-do the same task with LoRA instead of full fine-tune. Compare cost and quality.

---

## What I built
*(fill in when done)*

## What I learned

## What I got wrong
