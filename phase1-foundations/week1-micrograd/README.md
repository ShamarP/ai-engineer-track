# Week 1 — micrograd from scratch

**Why this week:** every LLM concept later in the roadmap (attention, gradients flowing through KV caches, fine-tuning loss curves) rests on backprop. Building it once by hand makes the rest stop being magic.

## 📖 Read (~4 hours)
- [x] ~~**AIE Ch 1** — already read prior to roadmap start~~
- [ ] **Karpathy** — [*The spelled-out intro to neural networks and backpropagation: building micrograd*](https://www.youtube.com/watch?v=VMj-3S1tku0) (~2h25m). Code along, don't just watch.
- [ ] **Karpathy** — [*The spelled-out intro to language modeling: building makemore*](https://www.youtube.com/watch?v=PaCmpygFfXo) (~1h57m).

Note files: drop your video notes in [`../../notes/books/karpathy-01-micrograd.md`](../../notes/books/karpathy-01-micrograd.md) and [`../../notes/books/karpathy-02-makemore.md`](../../notes/books/karpathy-02-makemore.md) — templates are pre-staged.

## 🧠 Concepts to internalize
- [ ] A computational graph: every scalar op becomes a node; data flows forward, gradients flow backward
- [ ] Chain rule = local derivative × upstream gradient (one line of code per op)
- [ ] `backward()` requires topological order — why?
- [ ] The three buffers: parameters, gradients, optimizer state
- [ ] Why a single-layer linear net cannot solve XOR (motivates depth + nonlinearity)
- [ ] SGD vs. minibatch vs. full-batch — why minibatch usually wins
- [ ] Cross-entropy loss for classification, MSE for regression — when each is correct

## 🛠 Build

Project is scaffolded — see [Setup](#setup) below to install deps. Files in this folder:

- `value.py` — empty stub for the `Value` class (you implement)
- `nn.py` — empty stub for `Neuron`, `Layer`, `MLP`
- `train_moons.py` — empty stub for the training loop
- `tests/test_against_pytorch.py` — verification scaffold for the PyTorch parity check

Steps:
1. [ ] Read `karpathy/micrograd/engine.py` *before* writing your own
2. [ ] Implement `value.py` with: `__add__`, `__mul__`, `__pow__`, `__neg__`, `relu`, `tanh`, `backward`
3. [ ] Implement `nn.py` (Neuron → Layer → MLP)
4. [ ] Implement `train_moons.py` — train your MLP on `sklearn.datasets.make_moons` (200 points), plot decision boundary
5. [ ] Fill in `tests/test_against_pytorch.py` — build same net in PyTorch with the same weights, confirm gradients match yours to within `1e-6`
6. [ ] Run `pytest` — should pass
7. [ ] Update the "What I built" section below

## ✅ Done when
- [ ] PyTorch and your micrograd produce identical gradients on a 3-layer MLP
- [ ] You can draw the computational graph for `((a*b) + c).relu()` on a whiteboard, mark every gradient, and explain each chain-rule application out loud — no notes

## 🎯 Stretch
- [ ] Add `exp`, `log`, `softmax`. Train on Iris.
- [ ] Read `karpathy/nanoGPT` README in prep for Week 2.

## Setup

```bash
cd phase1-foundations/week1-micrograd
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
pytest             # confirm scaffold runs (will fail until you implement)
```

If you don't have `uv`: `pip install uv` first, or substitute `python -m venv .venv && pip install -e ".[dev]"`.

---

## What I built
*(fill in when you finish — keep it tight: 3–5 sentences)*

## What I learned
*(2–3 ideas that rewired your thinking)*

## What I got wrong
*(something you had to redo, and why)*
