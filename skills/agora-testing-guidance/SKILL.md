---
name: agora-testing-guidance
description: Testing guardrails for wiki-backed Agora implementation tasks.
version: 0.2.0
---

# Agora Testing Guidance

Every implementation task must include tests or explicit test stubs.

## Must verify
- correct join/login identity
- token renewal behavior
- cleanup order
- payload and header correctness
- failure-path handling

## Wiki-first references
- `../../knowledge/concepts/testing/agora-testing-completeness-gate.md`
- `../../knowledge/concepts/testing/agora-token-renewal-testing.md`
- `../../knowledge/concepts/testing/agora-rtc-web-testing.md`
- `../../knowledge/concepts/testing/agora-convoai-rest-testing.md`

## Guidance source
The detailed testing expectations are captured in `../../knowledge/concepts/testing/` and `../../docs/tests/`, with this skill serving as the routing and guardrail layer.
