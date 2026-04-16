# Agora Skills Directory

`skills/` is the **only runtime entry layer** for agents. The stable knowledge lives under `knowledge/`, and `skills/` points to it through small policy and map files rather than duplicating long reference prose.

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
4. Read the linked canonical pages under `knowledge/` before any live-doc fetch
5. Escalate to live docs only for volatile details

## Role split
- `skills/` = orchestration, routing, runtime policy, testing guardrails
- `knowledge/` = stable entities, concepts, patterns, gotchas, queries
- `raw/` = imported source material and provenance
- `tests/` + `docs/tests/` = validation layer

## Reference discipline
The `references/` folders inside skill directories should contain only:
- knowledge maps
- live-doc policy
- architecture / maintenance notes

They should not turn back into a second large wiki.
