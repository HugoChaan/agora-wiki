---
title: Agora Live-Doc Fetch Policy
created: 2026-04-16
updated: 2026-04-16
type: concept
status: draft
tags: [live-docs, architecture, routing, rest-api, sdk]
sources: [raw/skills/doc-fetching.md]
---

# Agora Live-Doc Fetch Policy

Not all Agora knowledge should be frozen into a wiki.

## Level 1 — Stable bundled knowledge
Use stable knowledge pages for:
- product boundaries,
- integration patterns,
- identity rules,
- token and security guidance,
- common gotchas,
- high-signal architecture advice.

## Level 2 — Live docs
When stable pages are not enough, fetch live docs. This is especially important for:
- full request/response schemas,
- vendor-specific configs,
- model lists,
- language-specific quickstarts,
- error codes,
- release notes,
- newly added fields and parameters.

## Source strategy
Preferred sequence:
1. Try stable wiki knowledge first.
2. If the question needs volatile details, use Agora docs discovery such as `llms.txt`.
3. If needed, fetch direct `docs-md` pages.
4. Use MCP only when explicitly requested or when the runtime is configured for it.

## Why this matters
A wiki is good at compounding stable understanding. It is bad at pretending volatile API truth is static.

## Related pages
- [[agora-product-landscape]]
- [[agora-conversational-ai]]
- [[agora-rtc]]
- [[agora-common-integration-gotchas]]
