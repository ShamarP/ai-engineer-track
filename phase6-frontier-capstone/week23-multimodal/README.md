# Week 23 — Multimodal: voice + vision-language

**Why this week:** vision is in every product; voice agents are exploding. Both are easier than you think when you go through candle (which you already know from W19). One week of focused multimodal coverage gets you from "haven't touched it" to "can ship multimodal features."

## 📖 Read (~5 hours)
- [ ] **Radford et al., 2022, *Whisper: Robust Speech Recognition*** ([arxiv 2212.04356](https://arxiv.org/abs/2212.04356)). Sections **1**, **2**, **3.1**, **6**.
- [ ] **Radford et al., 2021, *CLIP*** ([arxiv 2103.00020](https://arxiv.org/abs/2103.00020)). Sections **1**, **2**, **5**.
- [ ] **Liu et al., 2023, *LLaVA: Visual Instruction Tuning*** ([arxiv 2304.08485](https://arxiv.org/abs/2304.08485)). Sections **1**, **3**, **5**.
- [ ] Skim **Phi-3.5-vision** model card OR **Qwen2-VL** technical report
- [ ] **OpenAI Realtime API docs** — production-grade voice-agent UX
- [ ] **`candle-examples/whisper`** and **`candle-examples/llava`** source

Note files: `notes/papers/radford-2022-whisper.md`, `notes/papers/radford-2021-clip.md`, `notes/papers/liu-2023-llava.md`.

## 🧠 Concepts to internalize
- [ ] Whisper architecture: log-mel spectrograms → encoder-decoder transformer; multilingual + timestamps
- [ ] CLIP: dual-encoder contrastive training; why it generalizes to zero-shot classification
- [ ] Vision-language models: vision encoder (often CLIP or SigLIP) + projection layer + LLM
- [ ] Streaming audio: VAD (voice activity detection), partial transcripts, end-of-speech detection
- [ ] Image preprocessing: resize, normalize, patch tokenization for ViT
- [ ] Why multimodal evaluation is harder: subjective on outputs, no clean ground truth

## 🛠 Build
1. [ ] **Audio path**: run Whisper-small via candle (your W19 knowledge applies). Build a CLI that takes a `.wav` or `.mp3` and produces a transcript with timestamps.
2. [ ] **Vision path**: run **Phi-3.5-vision** or **Qwen2-VL-2B** via candle. CLI: "given image X, answer question Y" with citations to image regions if the model supports it.
3. [ ] **Compose**: build a small "voice memo to structured note" tool — record audio → Whisper → small LLM extracts (date, action items, summary) → save as markdown. Or: "screenshot to markdown notes" via the vision model.
4. [ ] README: include 3 example runs (audio, image, composed); note where each model fails

## ✅ Done when
- [ ] Whisper transcribes a 1-minute audio clip you record on your phone
- [ ] The vision model correctly answers questions about 5 of your own screenshots
- [ ] The composed tool ships an actually-useful artifact for *you*

## 🎯 Stretch
- [ ] Build a real-time voice agent using OpenAI Realtime API + your W13 traced agent core. Voice in → reasoning → voice out.

---

## What I built

## What I learned

## What I got wrong
