# Agora Skills Directory

This repository keeps the wiki and the standard skill bundle together.

## Skill entrypoints
- `agora/SKILL.md` — root router for all Agora requests
- `agora-intake/SKILL.md` — intake for vague or multi-product requests
- `agora-testing-guidance/SKILL.md` — test requirements for implementation work
- `agora-rtc/SKILL.md`
- `agora-rtm/SKILL.md`
- `agora-conversational-ai/SKILL.md`
- `agora-cloud-recording/SKILL.md`
- `agora-server/SKILL.md`
- `agora-server-gateway/SKILL.md`

## Recommended loading order
1. Load `agora/SKILL.md`
2. Route to one or more product skills or `agora-intake/SKILL.md`
3. If the task is implementation work, also load `agora-testing-guidance/SKILL.md`
4. Read the linked wiki pages before any live-doc fetch
5. Escalate to live docs only for volatile details

## Repository role split
- `skills/` = orchestration and routing layer for agents
- `entities/`, `concepts/`, `patterns/`, `gotchas/`, `queries/` = stable wiki knowledge layer
- `raw/` = imported source material
- `tests/` and `docs/tests/` = validation layer
