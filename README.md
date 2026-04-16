# Agora Skills + Knowledge Base

Agent-facing Agora repository with **`skills/` as the runtime entry layer** and a separate **`knowledge/` layer** for stable reference content.

## Purpose
This repository is designed to be consumed by agents through `skills/`, not by treating the whole repo as a flat wiki.

The split is:
- `skills/` — routing, intake, testing guardrails, and live-doc escalation policy
- `knowledge/` — stable product knowledge, concepts, patterns, gotchas, and durable query pages
- `raw/` — source snapshots and provenance material
- live official docs — volatile schemas, release-note-sensitive details, and exact API field references

## Start Here
1. Read `skills/README.md` for runtime entrypoints
2. Read `SCHEMA.md` for repository rules
3. Read `knowledge/index.md` for canonical knowledge navigation
4. Check `log.md` for recent changes

## Repository layout
- `skills/` — agent runtime entry layer
- `knowledge/` — stable reference layer loaded by skills
- `raw/` — imported source snapshots and future official-doc captures
- `tests/` — structural and anti-drift checks
- `docs/tests/` — acceptance planning and execution artifacts

## Runtime model
1. Load `skills/agora/SKILL.md`
2. Route to the relevant product skill or `skills/agora-intake/SKILL.md`
3. For implementation tasks, also load `skills/agora-testing-guidance/SKILL.md`
4. Use the skill's `references/` files to locate canonical pages under `knowledge/`
5. Escalate to live docs only for volatile details

## Maintenance model
- Update `skills/` when routing, runtime policy, or testing guardrails change
- Update `knowledge/` when stable product knowledge improves
- Update `raw/` when provenance snapshots need refresh

This keeps agent behavior explicit while letting the knowledge base grow without bloating the skill layer.
