---
title: Agora Testing Completeness Gate
created: 2026-04-16
updated: 2026-04-16
type: concept
status: draft
tags: [testing, completeness, quality, implementation]
sources: [raw/skills/agora-testing-guidance.md]
---

# Agora Testing Completeness Gate

Implementation work is not complete just because the code compiles or the example looks reasonable.

## Rule
When generating implementation guidance, the answer should include:
- tests, or
- explicit test stubs with concrete behaviors to verify.

## Example required behaviors
- join is called with the correct channel name and UID
- agent_rtc_uid is passed as a string, not an integer
- remote_rtc_uids is an array of strings
- RTM login resolves before subscribe is attempted
- token renewal fetches a fresh token before expiry

## Implication for skills
The testing-guidance layer should be invoked for implementation prompts, not only for explicit testing questions.
