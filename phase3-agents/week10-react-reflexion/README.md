# Week 10 — ReAct + Reflexion

**Why this week:** ReAct is the canonical agent paper; reflection is the canonical "make it work better" technique. Both are still load-bearing in 2026.

## 📖 Read (~4 hours)
- [ ] **Yao et al., 2022, *ReAct*** ([arxiv 2210.03629](https://arxiv.org/abs/2210.03629)). Sections **1**, **2**, **3**, **4**, **5**. Figure 1 is the whole paper in one image.
- [ ] **Shinn et al., 2023, *Reflexion*** ([arxiv 2303.11366](https://arxiv.org/abs/2303.11366)). Sections **1**, **2**, **4**.
- [ ] **Madaan et al., 2023, *Self-Refine*** ([arxiv 2303.17651](https://arxiv.org/abs/2303.17651)). Skim — get the recipe.

Note files: `notes/papers/yao-2022-react.md`, `notes/papers/shinn-2023-reflexion.md`.

## 🧠 Concepts to internalize
- [ ] ReAct = Thought → Action → Observation → repeat. Forces the model to articulate reasoning in-line.
- [ ] Reflexion = ReAct + a critique step that updates "verbal" memory between attempts
- [ ] Self-Refine = generate → critique → revise, all by the same model
- [ ] When reflection helps: tasks with verifiable outcomes (code, math, structured)
- [ ] When it hurts: open-ended tasks where the critique itself is unreliable
- [ ] The "loop budget" problem: more reflection = more cost. Pick a budget.

## 🛠 Build
1. [ ] Add ReAct prompting to your week-9 agent (force `Thought:` → `Action:` → `Observation:` format)
2. [ ] Add a reflection layer: if final result fails self-check, spin up a critique step → re-run with the note in the prompt
3. [ ] Cap retries at 3
4. [ ] Pick a hard task with a clear success criterion (e.g., "write Python that passes these 5 unit tests")
5. [ ] Compare success rate on 20 problems: week-9 baseline vs. ReAct vs. ReAct + reflection
6. [ ] README: report the table. Be honest if reflection didn't help.

## ✅ Done when
- [ ] ReAct + reflection beats the week-9 baseline on your task
- [ ] You can explain why reflection helps for some task types and not others

## 🎯 Stretch
- [ ] Implement evaluator-optimizer (Anthropic): a separate LLM critiques the output, the original regenerates with the critique.

---

## What I built

## What I learned

## What I got wrong
