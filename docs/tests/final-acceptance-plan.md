# Final Acceptance Plan for Agora Wiki-Backed Skills

## Goal
Move from prototype structure validation to completion-level behavior validation.

## Required test layers
1. Structural tests
2. Prompt-routing acceptance tests
3. Live-doc escalation tests
4. Implementation/testing-guidance tests
5. Migration-coverage audit

## Minimum completion threshold
- Structural tests passing
- 12+ prompt cases executed with evidence
- 0 failures in live-doc boundary handling
- 0 failures in testing-guidance behavior for implementation prompts
- All legacy reference areas mapped to wiki or live-doc-only policy

## Blocking defects
Treat these as release blockers:
- Wrong product routing
- Failure to escalate volatile schema/details to live docs
- Implementation answers with no testing guidance
- Missing mapping for a major legacy Agora reference area

## Release decision
Only mark the new skills complete when all blocking defects are cleared and the evidence package is attached.
