# Week 1 — micrograd from scratch

**Why this week:** every LLM concept later in the roadmap (attention, gradients flowing through KV caches, fine-tuning loss curves) rests on backprop. Building it once by hand makes the rest stop being magic.

## 📖 Read (~5 hours)
- [ ] **AIE Ch 1** — *Introduction to Building AI Applications with Foundation Models*. Focus: AI engineering stack diagram, how AI engineering differs from ML engineering, the "three layers" framing.
- [ ] **Karpathy** — [*The spelled-out intro to neural networks and backpropagation: building micrograd*](https://www.youtube.com/watch?v=VMj-3S1tku0) (~2h25m). Code along, don't just watch.
- [ ] **Karpathy** — [*The spelled-out intro to language modeling: building makemore*](https://www.youtube.com/watch?v=PaCmpygFfXo) (~1h57m).

Notes file: [`../../notes/books/aie-ch01.md`](../../notes/books/aie-ch01.md) (create when you start).

## 🧠 Concepts to internalize
- [ ] A computational graph: every scalar op becomes a node; data flows forward, gradients flow backward
- [ ] Chain rule = local derivative × upstream gradient (one line of code per op)
- [ ] `backward()` requires topological order — why?
- [ ] The three buffers: parameters, gradients, optimizer state
- [ ] Why a single-layer linear net cannot solve XOR (motivates depth + nonlinearity)
- [ ] SGD vs. minibatch vs. full-batch — why minibatch usually wins
- [ ] Cross-entropy loss for classification, MSE for regression — when each is correct

## 🛠 Build
1. [ ] Read `karpathy/micrograd/engine.py` *before* writing your own
2. [ ] In this folder, implement a `Value` class with: `__add__`, `__mul__`, `__pow__`, `__neg__`, `relu`, `tanh`, `backward`
3. [ ] Build an `MLP` class on top of it (Neuron → Layer → MLP)
4. [ ] Train your MLP on `sklearn.datasets.make_moons` (200 points). Plot the decision boundary.
5. [ ] Verify: build the same net in PyTorch with the same weights, run forward + backward, confirm gradients match yours to within `1e-6`
6. [ ] Update this README's "What I built" section below

## ✅ Done when
- [ ] PyTorch and your micrograd produce identical gradients on a 3-layer MLP
- [ ] You can draw the computational graph for `((a*b) + c).relu()` on a whiteboard, mark every gradient, and explain each chain-rule application out loud — no notes

## 🎯 Stretch
- [ ] Add `exp`, `log`, `softmax`. Train on Iris.
- [ ] Read `karpathy/nanoGPT` README in prep for Week 2.

---

## What I built
*(fill in when you finish — keep it tight: 3–5 sentences)*

## What I learned
*(2–3 ideas that rewired your thinking)*

## What I got wrong
*(something you had to redo, and why)*
