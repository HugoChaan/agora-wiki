# Agora Repository Schema

## Domain
This repository covers the Agora product ecosystem for developers building RTC, RTM/Signaling, Conversational AI, Cloud Recording, token services, and server-side media integrations. It is optimized for AI-assisted integration help, implementation planning, and long-term maintenance of stable product knowledge.

## Core architecture
This repository has three layers:
1. **Skill layer** — `skills/` is the runtime entrypoint for agents
2. **Knowledge layer** — `knowledge/` stores stable reference content loaded by skills
3. **Source layer** — `raw/` stores provenance snapshots; live official docs cover volatile facts

The agent should enter through `skills/`, not by treating the whole repo as a flat wiki.

## Conventions
- File names: lowercase, hyphens, no spaces.
- Every knowledge page starts with YAML frontmatter.
- Use `[[wikilinks]]` or clear relative markdown links for internal navigation.
- Every new knowledge page must be added to `knowledge/index.md`.
- Every material change must be appended to `log.md`.
- Stable knowledge belongs in `knowledge/`; volatile schemas, release notes, and exact API field references belong in `raw/` or should be fetched live from official docs.

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

## Layer responsibilities
### Layer 1 — Skill layer (`skills/`)
Use skills for:
- routing
- intake behavior
- testing guidance
- live-doc escalation policy
- agent runtime entrypoints

### Layer 2 — Knowledge layer (`knowledge/`)
Use knowledge pages for:
- product purpose and boundaries
- product relationships
- integration patterns
- cross-product identity mapping
- security rules and gotchas
- recommended architecture and quickstart routing

### Layer 3 — Source layer (`raw/`) and live docs
Use `raw/` for:
- imported skill reference snapshots
- official docs excerpts
- OpenAPI snapshots
- release-note snapshots
- quickstart README snapshots

Do not rely on `knowledge/` alone for:
- full request/response schemas
- vendor/model config matrices
- release notes and newly added fields
- error code listings

For those, fetch live from Agora docs via `llms.txt`, direct `docs-md` links, or MCP when explicitly requested.

## Content groups
- `knowledge/entities/products/` — product pages and ecosystem entities
- `knowledge/entities/platforms/` — stable platform-specific summaries for RTC/RTM SDK usage on Web, iOS, Android
- `knowledge/concepts/` — durable concepts such as auth, identity, channels, events, media
- `knowledge/patterns/` — recommended implementation patterns and product combinations, including cross-platform lifecycle patterns
- `knowledge/comparisons/` — tradeoff and product comparison pages
- `knowledge/gotchas/` — recurring failure modes and sharp edges, including identity/lifecycle traps across stacks
- `knowledge/queries/` — durable synthesized answers worth keeping
- `skills/` — runtime control layer with separate skill directories and `SKILL.md` entrypoints

## Validation layer
- `tests/` — executable structural/contract tests for repository layout and skill policy
- `docs/tests/` — manual or harness-driven acceptance test definitions, evidence templates, and completion gates

## Anti-drift rules
- `skills/` is the only runtime entrypoint
- `references/` folders inside skills may contain maps, policy docs, and architecture notes only
- long-form product knowledge must live under `knowledge/`, not inside `skills/`
- deleted legacy filenames must not reappear in docs or tests

## Update policy
When new official docs conflict with existing knowledge content:
1. Prefer newer official docs for factual details.
2. Preserve durable guidance if still valid, but mark it with nuance.
3. If a contradiction matters operationally, note both positions and add a follow-up item in `log.md`.
4. If the change affects schemas or fast-moving details, move specifics out of `knowledge/` and point readers to live docs.
