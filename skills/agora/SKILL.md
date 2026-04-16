---
name: agora
description: Root router for the standard Agora wiki-backed skill bundle. Use for any Agora request before selecting a more specific sub-skill.
version: 0.2.0
---

# Agora Skill Bundle

Use this as the root skill for Agora product questions and implementation tasks.

## What this skill does
- routes clear requests to a product-specific skill;
- routes vague or multi-product requests to intake;
- enforces wiki-first lookup;
- enforces live-doc escalation for volatile details;
- adds testing guidance for implementation work.

## Routing
- Clear RTC request -> load `../agora-rtc/SKILL.md`
- Clear RTM request -> load `../agora-rtm/SKILL.md`
- Clear Conversational AI request -> load `../agora-conversational-ai/SKILL.md`
- Clear Cloud Recording request -> load `../agora-cloud-recording/SKILL.md`
- Clear server / token generation request -> load `../agora-server/SKILL.md`
- Clear Server Gateway request -> load `../agora-server-gateway/SKILL.md`
- Vague or multi-product request -> load `../agora-intake/SKILL.md`
- Implementation request -> also load `../agora-testing-guidance/SKILL.md`

## Knowledge strategy
- Read stable knowledge from the wiki repository pages first.
- Read `references/wiki-map.md` to find the relevant wiki pages.
- Use live docs for volatile details like exact schemas, vendor configs, model names, release notes, and error-code tables.
- Do not duplicate large reference bundles in the skill layer.

## Shared policy references
- `references/shared-live-doc-policy.md`
- `references/shared-repo-strategy.md`
