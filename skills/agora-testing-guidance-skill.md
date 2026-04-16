---
title: Agora Testing Guidance Skill
created: 2026-04-16
updated: 2026-04-16
type: query
status: draft
tags: [testing, routing]
sources: [raw/skills/agora-testing-guidance.md]
---

# Agora Testing Guidance Skill

Every implementation request should include testing guidance before completion.

## Core rule
Mock at the boundary your code owns.

## Required behaviors to test
- join/login called with correct channel and identity;
- token renewal before expiry;
- cleanup order;
- ConvoAI payload type correctness;
- auth headers present and correct;
- failure paths stop partial initialization.

## Routing
- RTC Web -> stack-specific web test guidance
- RTC React -> React hook/provider guidance
- Native/mobile + RTM + token renewal -> mobile/RTM guidance
- ConvoAI REST/backends -> HTTP-client level guidance

## Validation policy
Implementation work is not complete until tests or at least test stubs are produced and validated.
