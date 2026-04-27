# Week 12 — MCP server (TypeScript)

**Why this week:** MCP is becoming the standard interface for tools, resources, and prompts in 2026. Building one yourself takes the magic out of every agent system you'll see.

## 📖 Read (~4 hours)
- [ ] **Anthropic, *Model Context Protocol* spec** ([modelcontextprotocol.io](https://modelcontextprotocol.io)) — full spec; focus on tools/resources/prompts and JSON-RPC framing
- [ ] **Schick et al., 2023, *Toolformer*** ([arxiv 2302.04761](https://arxiv.org/abs/2302.04761)). Sections **1**, **3**, **4**.
- [ ] **MCP TypeScript SDK quickstart**
- [ ] **Anthropic, *Tool use* docs** ([docs.anthropic.com](https://docs.anthropic.com))

Note files: `notes/papers/schick-2023-toolformer.md`, `notes/papers/mcp-spec.md`.

## 🧠 Concepts to internalize
- [ ] MCP's three primitives: tools (model-invoked), resources (model-readable data), prompts (user-invoked templates)
- [ ] stdio vs. HTTP transport — when to pick each
- [ ] Tool design = API design. The schema is the contract.
- [ ] Function calling under the hood: model emits structured payload; runtime executes; result returns as another message
- [ ] Why MCP exists: every agent + every tool = N×M integrations without a standard

## 🛠 Build
1. [ ] In TypeScript with the official MCP SDK, build a server exposing 3 tools you actually want:
   - [ ] `search_my_notes` — searches your week-5 vector store
   - [ ] `journal_append` — adds an entry to a markdown file
   - [ ] `web_fetch` — fetches and summarizes a URL
2. [ ] Run via stdio
3. [ ] Connect Claude Desktop to your MCP server (edit `claude_desktop_config.json`)
4. [ ] Use it for one real workflow this week (e.g., "search my notes for everything I've written about evals, append a synthesis to today's journal")
5. [ ] Add a `resources/` endpoint exposing recent journal entries
6. [ ] README: document each tool's schema with examples

## ✅ Done when
- [ ] Claude Desktop calls your tools successfully
- [ ] You can explain the JSON-RPC message flow for one tool call, end-to-end

## 🎯 Stretch
- [ ] Add prompt templates — `/draft-pr` that pulls a structured PR description from a git diff resource.

---

## What I built

## What I learned

## What I got wrong
