# Next Steps

## Immediate next step
Run prompt-level acceptance against the actual agent runtime using the new repository shape:
- `skills/` as the only entry layer
- `knowledge/` as the stable reference layer
- live docs only for volatile facts

## Acceptance priorities
1. Direct product routing
2. Vague / multi-product intake routing
3. Knowledge-first answers for stable conceptual questions
4. Live-doc escalation for volatile API details
5. Implementation prompts that must include tests or explicit test stubs

## Maintenance priorities
1. Keep `skills/` procedural and short
2. Keep long-form knowledge under `knowledge/`
3. Keep provenance updates in `raw/`
4. Extend tests whenever a new runtime boundary rule is introduced

## Future refinement
If distribution needs diverge later, split packaging from the main repository only after the current same-repo architecture has proven stable in production use.
