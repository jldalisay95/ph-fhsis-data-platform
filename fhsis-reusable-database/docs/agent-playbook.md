# Agent Playbook

## Add a new source
1. Add source inventory entry.
2. Create `source_registration_manifest` from template.
3. Record checksum and retrieval timestamp.

## Propose new mapping
1. Fill crosswalk template.
2. Attach comparability assessment.
3. Mark unresolved evidence explicitly.

## Add transform safely
1. Start in pipeline stub with TODO markers.
2. Preserve layer boundaries.
3. Emit transform/provenance metadata.

## Document uncertainties
Use standardized tags in docs/templates: `[MISSING SOURCE]`, `[USER INPUT NEEDED]`, `[REQUIRES VALIDATION]`, `[ASSUMPTION — LOW CONFIDENCE]`.

## Block unsafe comparisons
Any non-`validated` comparability status must trigger warning in downstream outputs.

## Add dashboard view
Only after required metadata is defined in view spec template and review checklist passes.
