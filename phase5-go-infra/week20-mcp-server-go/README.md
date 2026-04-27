# Week 20 — MCP server (Go)

**Why this week:** shipping the same MCP server in two languages cements the protocol in your head and gives you portfolio breadth.

## 📖 Read (~3 hours)
- [ ] **mark3labs/mcp-go** README and examples (or the official Go SDK if released)
- [ ] Re-read your **week-12 MCP spec notes**
- [ ] **JSON-RPC 2.0 spec** ([jsonrpc.org/specification](https://www.jsonrpc.org/specification))

Note files: `notes/papers/jsonrpc-spec.md`.

## 🧠 Concepts to internalize
- [ ] Same protocol, two transports: stdio (parent process pipes) vs. Streamable HTTP
- [ ] Go's strong typing makes schema-first design natural
- [ ] Single binary deployment: `go build` and ship
- [ ] Resource subscriptions and prompts in addition to tools

## 🛠 Build
1. [ ] Reimplement your week-12 server in Go using `mark3labs/mcp-go`
2. [ ] Match all 3 tools: `search_my_notes`, `journal_append`, `web_fetch`
3. [ ] Add 2 new tools:
   - [ ] `git_log` — returns recent git commits in cwd
   - [ ] `code_search` — ripgrep wrapper with structured output
4. [ ] Add a resource: `desktop_screenshot` returning the latest screenshot path
5. [ ] Connect to Claude Desktop, run the same workflows from week 12
6. [ ] README: side-by-side comparison of TS vs. Go server lines-of-code, binary size, startup time

## ✅ Done when
- [ ] All 5 tools work in Claude Desktop
- [ ] The Go binary is < 10 MB

## 🎯 Stretch
- [ ] Add Streamable HTTP transport. Deploy to Fly.io or Railway. Connect a remote MCP client.

---

## What I built

## What I learned

## What I got wrong
