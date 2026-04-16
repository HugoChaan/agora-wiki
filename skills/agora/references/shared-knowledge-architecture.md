# Shared Knowledge Architecture

`skills/` is the only runtime entry layer in this repository.

## Layer split
- `skills/` owns orchestration, routing, testing guardrails, and live-doc escalation policy
- `knowledge/` owns stable reference content
- `raw/` owns provenance snapshots

## Why
- agent entrypoints stay explicit
- stable knowledge can grow without bloating skill files
- tests can verify boundary discipline between runtime instructions and knowledge pages

## Rule
Do not place long-form product knowledge in `skills/` or its `references/` directories. Reference folders are for maps, policy docs, and architecture notes only.
