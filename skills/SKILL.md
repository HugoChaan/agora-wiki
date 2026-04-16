---
name: agora-wiki
summary: Root router for the wiki-backed Agora skill system.
version: 0.1.0
---

# Agora Wiki-Backed Skill System

Use this root skill for Agora product questions and implementation tasks.

## Routing
- Clear product request -> load the relevant file under `products/`.
- Vague or multi-product request -> load `intake/SKILL.md` first.
- Implementation request -> also load `testing-guidance/SKILL.md`.

## Knowledge strategy
- Read stable knowledge from the wiki repository pages first.
- Use live-doc lookup for volatile details like schemas, vendor configs, model names, release notes, and error-code tables.
- Do not duplicate large reference bundles in the skill layer.

## Product files
- `products/rtc.md`
- `products/rtm.md`
- `products/conversational-ai.md`
- `products/cloud-recording.md`
- `products/server.md`
- `products/server-gateway.md`
