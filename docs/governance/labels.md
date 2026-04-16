# Label Taxonomy

Use labels consistently to enable fast triage, milestone planning, and backlog analytics.

## Area labels

- `area:database`
- `area:visualization`
- `area:governance`
- `area:docs`
- `area:ci`

## Type labels

- `type:feature`
- `type:bug`
- `type:docs`
- `type:refactor`
- `type:qa`
- `type:security`

## Priority labels

- `priority:P0` — urgent, production/release blocking
- `priority:P1` — high, current milestone critical
- `priority:P2` — medium, important but schedulable
- `priority:P3` — low, optimization/backlog

## Status labels

- `status:triage`
- `status:ready`
- `status:in-progress`
- `status:blocked`
- `status:needs-validation`

## Risk labels

- `risk:comparability`
- `risk:data-quality`
- `risk:security`
- `risk:delivery`

## Process labels

- `process:adr-required`
- `process:needs-design`
- `process:good-first-issue`
- `process:help-wanted`

## Labeling rules

1. Each issue should include:
   - one `area:*`,
   - one `type:*`,
   - one `priority:*`,
   - one `status:*`.
2. Apply `risk:*` labels whenever impact is plausible, even if probability is uncertain.
3. If a change affects data semantics/comparability, add `process:adr-required`.
4. Keep labels stable; avoid creating one-off labels when a standard label fits.
