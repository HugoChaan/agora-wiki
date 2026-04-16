# Agora Wiki Schema

## Domain
This wiki covers the Agora product ecosystem for developers building RTC, RTM/Signaling, Conversational AI, Cloud Recording, token services, and server-side media integrations. It is optimized for AI-assisted integration help, implementation planning, and long-term maintenance of stable product knowledge.

## Conventions
- File names: lowercase, hyphens, no spaces.
- Every wiki page starts with YAML frontmatter.
- Use `[[wikilinks]]` for internal links.
- Every page should link to at least 2 related pages where practical.
- When updating a page, always bump the `updated` date.
- Every new page must be added to `index.md`.
- Every material change must be appended to `log.md`.
- Stable knowledge belongs in wiki pages; volatile schemas, release notes, and exact API field references belong in `raw/` or should be fetched live from official docs.

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | pattern | gotcha
status: draft | stable
tags: [from taxonomy below]
sources: [raw/skills/...]
---
```

## Tag Taxonomy
### Products
- product-rtc
- product-rtm
- product-convoai
- product-cloud-recording
- product-token-service
- product-server-gateway

### Platforms
- platform-web
- platform-react
- platform-nextjs
- platform-ios
- platform-android
- platform-python
- platform-go
- platform-nodejs
- platform-server
- platform-linux

### Topics
- auth
- identity
- channels
- events
- media
- routing
- architecture
- quickstart
- sdk
- rest-api
- testing
- security
- gotcha
- live-docs

## Page Thresholds
- Create a page when a concept or product is central to Agora integration work.
- Add to an existing page when the information refines a known concept.
- Do not create pages for single-field API trivia that belongs in official docs.
- Split pages when they exceed ~200 lines.
- Keep exact request/response schemas in `raw/` or retrieve them from official docs at answer time.

## Agora Knowledge Layers
### Layer 1 — Stable wiki knowledge
Use wiki pages for:
- Product purpose and boundaries
- Product relationships
- Integration patterns
- Cross-product identity mapping
- Security rules and gotchas
- Recommended architecture and quickstart routing

### Layer 2 — Raw sources
Use `raw/` for:
- Imported skill reference snapshots
- Official docs excerpts
- OpenAPI snapshots
- Release-note snapshots
- Quickstart README snapshots

### Layer 3 — Live docs
Do not rely on the wiki alone for:
- Full request/response schemas
- Vendor/model config matrices
- Release notes and newly added fields
- Error code listings

For those, fetch live from Agora docs via `llms.txt`, direct `docs-md` links, or MCP when explicitly requested.

## Content Groups
- `entities/products/` — product pages and ecosystem entities
- `entities/platforms/` — stable platform-specific summaries for RTC/RTM SDK usage on Web, iOS, Android
- `concepts/` — durable concepts such as auth, identity, channels, events, media
- `patterns/` — recommended implementation patterns and product combinations, including cross-platform lifecycle patterns
- `comparisons/` — tradeoff and product comparison pages
- `gotchas/` — recurring failure modes and sharp edges, including identity/lifecycle traps across stacks
- `queries/` — durable synthesized answers worth keeping
- `skills/` — standard skill bundle with separate skill directories and `SKILL.md` entrypoints for orchestration and routing

## Validation Layer
- `tests/` — executable structural/contract tests for repository layout and skill policy.
- `docs/tests/` — manual or harness-driven acceptance test definitions, evidence templates, and completion gates.

## Update Policy
When new official docs conflict with existing wiki content:
1. Prefer newer official docs for factual details.
2. Preserve durable guidance if still valid, but mark it with nuance.
3. If a contradiction matters operationally, note both positions and add a follow-up item in `log.md`.
4. If the change affects schemas or fast-moving details, move specifics out of the wiki and point readers to live docs.
