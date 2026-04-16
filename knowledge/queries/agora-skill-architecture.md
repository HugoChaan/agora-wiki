---
title: Agora skill architecture
created: 2026-04-16
updated: 2026-04-16
type: query
status: stable
tags: [architecture, routing, testing, live-docs]
sources: [skills/agora/SKILL.md, skills/README.md, SCHEMA.md]
---

# Agora skill architecture

## Question
What is the best production shape for an Agora agent repository that needs skills, durable knowledge, and live-doc escalation?

## Answer
The best production shape for Agora is **skills-first, knowledge-backed, live-doc-aware**.

That means:
- `skills/` is the only runtime entry layer for agents
- `knowledge/` contains the stable reference pages that skills point to
- `raw/` contains provenance snapshots and imported source material
- live official docs are used only when the requested detail is volatile

## Why this split works
### 1. It matches runtime behavior
Agents should not enter through a flat documentation tree. They should:
1. load the root skill
2. route to intake or a product skill
3. load testing guidance for implementation work
4. read canonical knowledge pages
5. escalate to live docs only when needed

### 2. It keeps control and knowledge separate
`skills/` owns orchestration, routing, policy, and test guardrails.
`knowledge/` owns durable product understanding, concepts, patterns, and gotchas.

This keeps the skill files short and procedural instead of turning them back into large reference bundles.

### 3. It supports same-repo maintenance without collapsing boundaries
Keep the runtime skills and the knowledge base in the same `agora-wiki` repository, but do **not** flatten them into a single undifferentiated wiki tree.

Same repo is useful because:
- links stay stable
- tests can verify both structure and policy
- routing logic and canonical knowledge evolve together

Separate layers are useful because:
- skill maintenance cadence differs from knowledge maintenance cadence
- long-form reference content can grow without bloating runtime entrypoints
- provenance and volatile details stay out of the stable knowledge layer

## Recommended directory shape
```text
repo/
├── skills/
│   ├── agora/
│   ├── agora-intake/
│   ├── agora-testing-guidance/
│   ├── agora-rtc/
│   ├── agora-rtm/
│   └── ...
├── knowledge/
│   ├── entities/
│   ├── concepts/
│   ├── patterns/
│   ├── gotchas/
│   ├── comparisons/
│   └── queries/
├── raw/
├── docs/tests/
└── tests/
```

## Maintenance rule
- change `skills/` when runtime behavior changes
- change `knowledge/` when stable understanding improves
- change `raw/` when source snapshots need refresh
- add or update tests whenever a boundary rule changes
