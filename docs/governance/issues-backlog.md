# Seed Backlog (Issue Drafts)

This file provides high-quality issue drafts that can be copied into GitHub Issues with milestone and labels pre-selected.

---

## 1) Define source registration quality gate

- **Title:** `Define and enforce source registration quality gate`
- **Milestone:** `M1 — Source Registry & Provenance Foundation`
- **Labels:** `area:database`, `type:feature`, `priority:P1`, `status:triage`, `risk:data-quality`
- **Problem:** Source onboarding can be inconsistent without mandatory provenance fields.
- **Acceptance criteria:**
  - Required manifest fields are listed and justified.
  - Validation helper checks required fields.
  - Failing example and passing example are documented.
- **Definition of done:** docs + validation logic + tests merged.

## 2) Add comparability assessment decision checklist

- **Title:** `Add comparability assessment checklist for cross-version indicators`
- **Milestone:** `M3 — Comparability & Indicator Governance`
- **Labels:** `area:database`, `type:docs`, `priority:P1`, `status:triage`, `risk:comparability`, `process:adr-required`
- **Problem:** Cross-version analyses risk false comparability.
- **Acceptance criteria:**
  - Checklist includes geography, formula, denominator, and reporting cadence deltas.
  - Escalation path defined when comparability is unknown.
  - Linked from contributing guidance.
- **Definition of done:** checklist doc merged and referenced in workflow docs.

## 3) Implement bronze→silver provenance propagation test

- **Title:** `Implement provenance propagation test across bronze-to-silver path`
- **Milestone:** `M2 — Bronze/Silver Normalization Foundation`
- **Labels:** `area:database`, `type:qa`, `priority:P1`, `status:triage`, `risk:data-quality`
- **Problem:** Pipeline trust requires lineage continuity checks.
- **Acceptance criteria:**
  - Test verifies required provenance columns survive transformation.
  - Failure messages identify missing provenance fields.
  - Test is executed in CI.
- **Definition of done:** automated test merged and passing in CI.

## 4) Define dashboard comparability warning behavior

- **Title:** `Define UI behavior for non-validated comparability warnings`
- **Milestone:** `M4 — Visualization MVP with Metadata Gates`
- **Labels:** `area:visualization`, `type:feature`, `priority:P1`, `status:triage`, `risk:comparability`, `process:needs-design`
- **Problem:** Users may misinterpret trends without in-context warning states.
- **Acceptance criteria:**
  - Warning trigger conditions documented.
  - Copy guidelines for warning text approved.
  - QA checklist includes warning verification scenario.
- **Definition of done:** behavior spec and QA criteria merged.

## 5) Harden CI for docs integrity and broken link prevention

- **Title:** `Harden CI checks for docs structure and link integrity`
- **Milestone:** `M0 — Governance & Operating Baseline`
- **Labels:** `area:ci`, `type:feature`, `priority:P2`, `status:triage`, `risk:delivery`
- **Problem:** Broken docs degrade contributor velocity and trust.
- **Acceptance criteria:**
  - CI validates markdown links in docs paths.
  - Failure output points to actionable file/line references.
  - Contributing guide updated with local check command.
- **Definition of done:** CI workflow + docs instructions merged.

## 6) Publish release-readiness checklist for v0.1.0

- **Title:** `Publish v0.1.0 release-readiness checklist`
- **Milestone:** `M5 — Release Readiness (v0.1.0)`
- **Labels:** `area:governance`, `type:docs`, `priority:P1`, `status:triage`, `risk:delivery`
- **Problem:** Release quality can drift without explicit go/no-go criteria.
- **Acceptance criteria:**
  - Checklist covers docs completeness, tests, security review, and unresolved risk review.
  - Checklist mapped to owners.
  - Release PR template references checklist.
- **Definition of done:** checklist published and linked from release workflow docs.

---

## Backlog hygiene rules

- Keep issue descriptions outcome-based, not implementation-prescriptive.
- Prefer splitting large work into issues that fit one milestone.
- Avoid adding contributors to late tasks as a substitute for scope control.
- Re-triage priorities at each sprint planning boundary.
