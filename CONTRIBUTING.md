# Contributing

## Principles
- Documentation first.
- Do not invent FHSIS definitions or mappings.
- Keep changes reviewable and provenance-preserving.

## Contribution flow
1. Open issue using template.
2. Update docs (`docs/`, ADRs) before implementation.
3. Add/modify schema/templates.
4. Add tests/checks.
5. Submit PR with unresolved items clearly labeled.

## Agent-friendly workflows
- Add new source: update source inventory + `source_registration_manifest` template.
- Propose mapping: use crosswalk template and comparability assessment.
- Add transform safely: stub pipeline, add provenance fields, add tests.
- Document uncertainties: append to unresolved questions/assumptions logs.
- Block unsafe comparisons: require comparability status != `validated` to show warning.
- Add dashboard view: only after required metadata is present in view spec.
