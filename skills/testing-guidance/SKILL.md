---
name: agora-testing-guidance
summary: Testing guardrails for wiki-backed Agora implementation tasks.
version: 0.1.0
---

# Agora Testing Guidance

Every implementation task must include tests or explicit test stubs.

## Must verify
- correct join/login identity
- token renewal behavior
- cleanup order
- payload and header correctness
- failure-path handling

## Guidance source
The detailed testing expectations are captured in `../concepts/testing/` and `../docs/tests/`, with this skill serving as the routing and guardrail layer.
