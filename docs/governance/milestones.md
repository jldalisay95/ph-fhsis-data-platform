# Milestones

> Milestones are structured for predictable delivery, clear ownership, and quality gates.

## M0 — Governance & Operating Baseline

**Goal:** Establish contribution discipline, planning conventions, and quality guardrails.

- **Suggested window:** 2 weeks
- **Exit criteria:**
  - Governance docs, labels, and issue templates are complete.
  - Backlog seeded with prioritized issue set.
  - CI checks for docs/code are green.

## M1 — Source Registry & Provenance Foundation

**Goal:** Enable repeatable onboarding of source artifacts with provenance metadata.

- **Suggested window:** 2–3 weeks
- **Exit criteria:**
  - Source onboarding path documented and tested.
  - Manifest completeness rules validated.
  - Initial source inventory baseline established.

## M2 — Bronze/Silver Normalization Foundation

**Goal:** Implement reproducible staging and canonical normalization scaffolding.

- **Suggested window:** 3 weeks
- **Exit criteria:**
  - Bronze and Silver contracts documented.
  - Normalization pipeline stubs covered by baseline tests.
  - Data quality rule registry linked to pipeline checks.

## M3 — Comparability & Indicator Governance

**Goal:** Prevent unsafe cross-version analytics through explicit comparability controls.

- **Suggested window:** 3 weeks
- **Exit criteria:**
  - Comparability assessment workflow operational.
  - Indicator/version governance documented.
  - Warning/guardrail paths in place for non-validated comparisons.

## M4 — Visualization MVP with Metadata Gates

**Goal:** Deliver metadata-aware visualization with QA and audience guidance.

- **Suggested window:** 3 weeks
- **Exit criteria:**
  - View spec template operational.
  - QA checklist integrated in dashboard workflow.
  - Comparability warnings surfaced in visualization behavior/docs.

## M5 — Release Readiness (v0.1.0)

**Goal:** Package a coherent, auditable first public release of the scaffold.

- **Suggested window:** 2 weeks
- **Exit criteria:**
  - Release notes and upgrade notes drafted.
  - Critical and high-priority issues for v0.1.0 closed.
  - Governance review confirms readiness.

## Milestone assignment rules

- Every issue must have **exactly one** milestone.
- Default assignment is the earliest milestone where dependencies are satisfied.
- If an issue spans milestones, split into milestone-bounded child issues.
- Late issues should prefer scope cuts over last-minute staffing increases.
