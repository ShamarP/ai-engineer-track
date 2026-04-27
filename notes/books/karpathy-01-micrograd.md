# Karpathy — The spelled-out intro to neural networks and backpropagation: building micrograd

**Source:** https://www.youtube.com/watch?v=VMj-3S1tku0 (~2h25m)
**Watched on:** YYYY-MM-DD
**Why I watched:** Phase 1 / Week 1 — first principles for backprop.

## The question
Why does backprop work, mechanically? What does autograd do under the hood?

## Key claims
- A neural net is just a long mathematical expression. Training is gradient descent on it.
- Reverse-mode autograd = chain rule, applied node-by-node, in reverse topological order.
- Every op records: its output, its inputs (children), and a local backward function. `backward()` calls them in order.
- Three buffers: `data` (forward value), `grad` (accumulated gradient), and per-op `_backward` closure.

## Worked examples I want to remember
- f = a*b + c → ∂f/∂a = b, ∂f/∂b = a, ∂f/∂c = 1
- ReLU's gradient is the indicator function on x > 0
- Why we *accumulate* (`+=`) gradients on `backward()` — a node can be used many times

## My take
*(after the video — what surprised you, what felt obvious, what you still don't fully grok)*

## What I'm doing with it
- Implementing `value.py` from scratch, no peek
- Verifying against PyTorch in `tests/test_against_pytorch.py`
