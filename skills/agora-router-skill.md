---
title: Agora Router Skill
created: 2026-04-16
updated: 2026-04-16
type: query
status: draft
tags: [routing, architecture, live-docs]
sources: [raw/skills/agora-intake.md, raw/skills/doc-fetching.md]
---

# Agora Router Skill

This page defines the root wiki-backed skill.

## Responsibilities
- identify whether the request is clear or vague;
- route to product skills or intake;
- enforce wiki-first lookup;
- enforce live-doc fetch for volatile details;
- pull in testing guidance for implementation tasks.

## Minimal root skill outline
- Explain supported products: RTC, RTM, Conversational AI, Cloud Recording, Server, Server Gateway.
- Say: for clear product asks, route directly; for vague asks, use intake.
- Point all stable knowledge lookups to wiki pages instead of bundled references.
- Preserve the existing live-doc boundary from [[agora-live-doc-fetch-policy]].

## Product-skill mapping
- RTC -> `skills/products/rtc.md`
- RTM -> `skills/products/rtm.md`
- Conversational AI -> `skills/products/conversational-ai.md`
- Cloud Recording -> `skills/products/cloud-recording.md`
- Server/token generation -> `skills/products/server.md`
- Server Gateway -> `skills/products/server-gateway.md`
