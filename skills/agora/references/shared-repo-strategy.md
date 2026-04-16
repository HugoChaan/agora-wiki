# Shared Repository Strategy

The wiki-backed Agora skills should live in the same `agora-wiki` repository.

## Why
- skill routing and wiki content evolve together
- page links remain stable
- migration coverage is easier to audit
- tests can verify structure and behavior in one place

## Layout
- `entities/`, `concepts/`, `patterns/`, `gotchas/`, `queries/`, `raw/`
- `skills/` for orchestration and routing as a standard skill bundle
- `tests/` and `docs/tests/` for validation assets
