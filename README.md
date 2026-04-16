# Philippine FHSIS Data Platform (Starter Monorepo Scaffold)

## 1) What this repository is
A documentation-first, version-aware starter scaffold for two linked product areas:
- `fhsis-reusable-database`: harmonization, provenance, schema, and quality layers
- `fhsis-visualization`: metadata-aware visualization specifications and QA surfaces

This scaffold is designed for iterative implementation with explicit provenance and comparability controls.

## 2) What this repository is not
- Not an official DOH/FHSIS publication.
- Not a validated source of indicator definitions, formulas, or legal interpretation.
- Not a complete implementation.

## 3) Why provenance and versioning matter
FHSIS artifacts can evolve in structure, geography references, and reporting logic. Without source/version metadata, results may look comparable while being non-comparable. This repo treats comparability as unsafe by default until validated.

## 4) Public vs restricted data boundary
- Public aggregate pathway: default in this repository.
- Restricted pathway: represented as scaffolding only; no restricted files should be committed.
- Any restricted workflow must be implemented with separate access controls. `[REQUIRES VALIDATION]`

## 5) Repository structure
- `docs/`: charter, scope, ADRs, governance, mapping/validation docs
- `fhsis-reusable-database/`: raw/extract/registry/models and Python stubs
- `fhsis-visualization/`: specs/app/qa/docs/templates
- `.github/`: issue templates, CI workflows, PR template

## 6) Development workflow
1. Create or update docs first.
2. Register source metadata (manifest + schema checks).
3. Add extraction/normalization scaffold changes.
4. Add tests and quality rules.
5. Add visualization view specs only after metadata readiness.

## 7) Documentation-first contribution rule
Any code change that affects data semantics, schemas, mappings, or comparability must include docs updates (ADR and/or domain docs).

## 8) Quality and comparability principles
- Provenance first-class in all layers.
- Bronze/Silver/Gold separation.
- Explicit comparability assessment required for cross-version analyses.
- Unknowns must be labeled with: `[MISSING SOURCE]`, `[USER INPUT NEEDED]`, `[REQUIRES VALIDATION]`, or `[ASSUMPTION — LOW CONFIDENCE]`.

## 9) Initial roadmap
- Phase 0: scaffold and governance
- Phase 1: source inventory + report version registry
- Phase 2: extraction and normalization foundations
- Phase 3: indicator/version comparability controls
- Phase 4: metadata-aware visualization MVP

## 10) Open questions and missing inputs
- Official source corpus scope and access permissions `[USER INPUT NEEDED]`
- Approved geography version authority and cadence `[MISSING SOURCE]`
- Indicator governance process ownership `[USER INPUT NEEDED]`
- License holder legal name in `LICENSE` `[USER INPUT NEEDED]`

## Quick start
```bash
make setup
make check
make test
```

> Status: starter scaffold ready for the next evidence-backed implementation phase.
