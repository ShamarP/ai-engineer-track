# Karpathy — The spelled-out intro to language modeling: building makemore

**Source:** https://www.youtube.com/watch?v=PaCmpygFfXo (~1h57m)
**Watched on:** YYYY-MM-DD
**Why I watched:** Phase 1 / Week 1 — bridge from autograd to language models.

## The question
How does the simplest possible "language model" work? What's the recipe before transformers?

## Key claims
- Bigram model: P(next char | this char). A 27×27 table is your whole model.
- The same problem becomes a 1-layer NN: input one-hot → linear → softmax → cross-entropy on the next char.
- Training = pushing probability mass toward the right next char, away from the wrong ones.
- Negative log-likelihood is the loss; minimizing it = maximizing P(data | model).

## Worked examples I want to remember
- Why softmax + cross-entropy "cancel" elegantly — derivative simplifies to `softmax_output - one_hot_target`
- What "smoothing" means and why a tiny added count fixes infinite loss on unseen bigrams
- The model-counting equivalence: bigram counts ≈ what a 1-layer NN converges to

## My take
*(after the video)*

## What I'm doing with it
- This sets up Week 2: tokenization + transformers. The "input → linear → softmax → loss" recipe scales straight up.
