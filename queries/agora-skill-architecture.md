---
title: Agora Skill Architecture
created: 2026-04-16
updated: 2026-04-16
type: query
status: draft
tags: [routing, architecture, testing, live-docs]
sources: [raw/skills/agora-intake.md, raw/skills/doc-fetching.md]
---

# Agora Skill Architecture

## Decision
The next-generation Agora skills should be **wiki-first but not wiki-only**.

- The wiki owns stable product knowledge, concepts, patterns, and gotchas.
- Skills own routing, guardrails, testing requirements, and live-doc escalation policy.
- Fast-changing facts stay out of the stable wiki and must be fetched live.

## Repository choice
The new skills should live in **this same `agora-wiki` repository**, under `skills/`.

Why:
- knowledge pages and skill routing rules evolve together;
- relative wiki links stay stable;
- one repo reduces version drift between wiki content and skill instructions;
- testing the new skill layer becomes easier because fixtures and docs live together.

Use a separate repo only if you later need a distribution-specific packaging layer for multiple runtimes.

## Recommended layout
```text
agora-wiki/
├── entities/
├── concepts/
├── patterns/
├── gotchas/
├── queries/
├── raw/
└── skills/
    ├── SKILL.md                     # root router skill
    ├── intake/SKILL.md              # vague request classifier
    ├── testing-guidance/SKILL.md    # testing guardrails
    ├── products/
    │   ├── rtc.md
    │   ├── rtm.md
    │   ├── conversational-ai.md
    │   ├── cloud-recording.md
    │   ├── server.md
    │   └── server-gateway.md
    └── shared/
        ├── live-doc-policy.md
        └── repo-strategy.md
```

## Routing model
1. If the request is vague or mixes products, load `skills/intake/SKILL.md`.
2. If the request is product-specific, route directly to the relevant product skill page.
3. Product skill pages should point to wiki pages first.
4. If the question needs volatile details, escalate to live docs.
5. Implementation requests must also pull in `skills/testing-guidance/SKILL.md`.

## What stays out of skills
Do not duplicate long bundled references once the wiki pages exist. Skills should stay small and procedural.
