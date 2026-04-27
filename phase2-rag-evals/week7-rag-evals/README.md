# Week 7 — RAG evals (the highest-leverage skill in this whole roadmap)

**Why this week:** this is the week. Almost every senior practitioner agrees: the people who win at applied LLM work are obsessive about evals. Most engineers skip them. You won't.

## 📖 Read (~5 hours)
- [ ] **AIE Ch 3** — *Evaluation Methodology*
- [ ] **Hamel Husain, *Your AI Product Needs Evals*** ([hamel.dev/blog/posts/evals/](https://hamel.dev/blog/posts/evals/)) — read twice
- [ ] **Hamel Husain, *A Field Guide to Rapidly Improving AI Products*** (hamel.dev follow-up)
- [ ] **Eugene Yan, *LLM-Evaluators: A Comprehensive Study*** ([eugeneyan.com](https://eugeneyan.com))
- [ ] **OpenAI evals repo** README — skim for structure

Note files: `notes/books/aie-ch03.md`, `notes/papers/husain-evals.md`.

## 🧠 Concepts to internalize
- [ ] Three eval levels: unit (per-component), integration (per-feature), e2e (per-user-task)
- [ ] Reference-based vs. reference-free (LLM judge)
- [ ] LLM-as-judge: pairwise > scoring; use a different model than the one being judged
- [ ] Eval-driven development: write the eval *before* changing the prompt
- [ ] Error analysis — read 100 failure traces by hand, no shortcut
- [ ] Cost of evals — budget tokens; you'll run them often
- [ ] Regression suites: never break what worked

## 🛠 Build
1. [ ] Take week-6 RAG. Build three eval suites:
   - [ ] **Retrieval eval**: 50 queries with manually-labeled "should retrieve" doc IDs. Measure recall@5.
   - [ ] **Faithfulness eval**: 30 (question, context, answer) triples. LLM-as-judge: does answer ONLY use context?
   - [ ] **End-to-end eval**: 30 (question, gold-answer) pairs. Pairwise LLM judge vs. baseline.
2. [ ] Each suite is a CLI: `evals run rag-faithfulness`. Output: CSV + markdown summary.
3. [ ] `regression.py` runs all three; fails if any score drops more than 5% from baseline
4. [ ] Commit baseline scores to a `baselines/` folder
5. [ ] Intentionally degrade RAG (top-K 5 → 1). Run regression. Confirm it catches it.
6. [ ] README: include the markdown summary from one full run

## ✅ Done when
- [ ] One command runs all three suites and prints a scorecard
- [ ] You break your RAG, regression catches it, you fix it, regression passes

## 🎯 Stretch
- [ ] Read 30 e2e failure traces. Categorize failure modes. Write up the top 3.

---

## What I built

## What I learned

## What I got wrong
