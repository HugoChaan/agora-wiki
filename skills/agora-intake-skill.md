---
title: Agora Intake Skill
created: 2026-04-16
updated: 2026-04-16
type: query
status: draft
tags: [routing, architecture]
sources: [raw/skills/agora-intake.md]
---

# Agora Intake Skill

Use when the user's need is unclear or spans multiple Agora products.

## Responsibilities
- classify the user into RTC / RTM / ConvoAI / Cloud Recording / Server Gateway / token service / multi-product flow;
- identify whether the user needs browser client, mobile client, or server-side media;
- route to the minimum set of product skills;
- recommend common product combinations such as RTC + RTM, RTC + ConvoAI, or RTC + Cloud Recording.

## Output contract
The intake step should end with:
1. selected product set,
2. target platform(s),
3. auth model,
4. whether live-doc lookup is required,
5. which product skill pages to load next.
