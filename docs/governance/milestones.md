# Milestones

These milestones are ordered for a documentation-first, provenance-first data
platform. Each milestone has a narrow outcome, measurable exit criteria, and a
clear handoff into the next milestone.

## Recommended Delivery Order

1. `M0 - Governance & Operating Baseline`
2. `M1 - Source Registry & Provenance Foundation`
3. `M2 - Bronze/Silver Normalization Foundation`
4. `M3 - Comparability & Indicator Governance`
5. `M4 - Visualization MVP with Metadata Gates`
6. `M5 - Release Readiness (v0.1.0)`

The critical path is M0 -> M1 -> M2 -> M3 -> M4 -> M5. Visualization work can
start in parallel during M2 only for documentation, view specifications, and QA
checklists; user-facing charts should wait until M3 gates are defined.

## M0 - Governance & Operating Baseline

**Goal:** Make contribution, planning, review, and CI expectations explicit
before implementation work expands.

**Suggested window:** 1-2 weeks

**Must happen first because:** later data and visualization work depends on
consistent labels, issue templates, review rules, CI checks, and documentation
standards.

**Exit criteria:**

- Issue templates, label taxonomy, milestones, and planning rules are complete.
- The backlog has parent issues, sub-issues, dependencies, and priority order.
- CI validates Python tests, linting, and documentation structure.
- Documentation-first contribution rules are linked from `README.md` and
  `CONTRIBUTING.md`.

**Parallel work allowed:**

- Governance docs and issue template cleanup can run in parallel with CI
  hardening.
- Architecture docs can be reviewed while test workflow fixes are implemented.

## M1 - Source Registry & Provenance Foundation

**Goal:** Enable repeatable onboarding of source artifacts with source identity,
retrieval metadata, checksums, validation status, and access boundaries.

**Suggested window:** 2-3 weeks

**Depends on:** M0 governance baseline.

**Exit criteria:**

- Source registration manifest schema is validated by automated tests.
- Required provenance fields are documented and enforced.
- Public vs restricted source handling rules are explicit.
- Initial source inventory baseline exists with all unknowns marked using the
  repository's required uncertainty tags.
- Checksums and retrieval metadata are captured consistently.

**Parallel work allowed:**

- Manifest schema validation, inventory documentation, and checksum helper work
  can run in parallel.
- Restricted-data policy documentation can run in parallel with public-source
  onboarding, but no restricted processing implementation should start yet.

## M2 - Bronze/Silver Normalization Foundation

**Goal:** Build the first testable extraction and normalization path while
preserving provenance from source registration through canonical records.

**Suggested window:** 3 weeks

**Depends on:** M1 manifest validation and source inventory baseline.

**Exit criteria:**

- Bronze and Silver contracts are documented.
- Extract and normalize pipeline interfaces have typed inputs and outputs.
- Provenance fields survive extract-to-bronze and bronze-to-silver transforms.
- Data quality rules can be loaded from the rules register and evaluated in
  tests.
- CI runs focused pipeline and validation tests.

**Parallel work allowed:**

- Bronze contract documentation can run in parallel with extractor interface
  work.
- Data quality rule runner work can run in parallel with provenance propagation
  tests once required provenance fields are settled.

## M3 - Comparability & Indicator Governance

**Goal:** Prevent unsafe cross-version analysis by making indicator, formula,
denominator, geography, and reporting-period comparability explicit.

**Suggested window:** 3 weeks

**Depends on:** M2 canonical record shape and provenance propagation.

**Exit criteria:**

- Indicator definition/version registry workflow is documented and testable.
- Geography version registry workflow is documented and testable.
- Deprecated and replaced indicator crosswalk rules are documented.
- Comparability assessment checklist is complete and linked from contributor
  guidance.
- Unknown comparability defaults to a blocked or warning state, not a silent
  chart or metric.

**Parallel work allowed:**

- Indicator registry, geography registry, and denominator/formula note workflows
  can run in parallel.
- Visualization warning copy can be drafted during this milestone, but final
  behavior should wait for comparability gate decisions.

## M4 - Visualization MVP with Metadata Gates

**Goal:** Deliver a metadata-aware visualization MVP that only presents charts
when required provenance and comparability metadata are available.

**Suggested window:** 3 weeks

**Depends on:** M3 comparability gate rules and M2/M3 metadata contracts.

**Exit criteria:**

- View specification template is validated.
- Dashboard MVP scope is tied to explicit audience and use cases.
- Charts require source, report version, indicator version, geography version,
  and comparability metadata.
- Comparability warnings and blocked states are verified by QA scenarios.
- Accessibility baseline checks are included in visualization QA.

**Parallel work allowed:**

- View spec validation, QA checklist expansion, and dashboard app scaffold can
  run in parallel after metadata requirements are frozen.
- Copy review and accessibility review can run in parallel with dashboard
  implementation.

## M5 - Release Readiness (v0.1.0)

**Goal:** Package a coherent, auditable first public release of the scaffold.

**Suggested window:** 1-2 weeks

**Depends on:** all P1 issues in M0-M4 closed or explicitly deferred with an
accepted-risk note.

**Exit criteria:**

- Release readiness checklist is complete.
- Release notes describe what is implemented, scaffolded, and explicitly out of
  scope.
- Security and restricted-data boundary review is complete.
- Documentation landing pages guide new contributors through the intended
  workflow.
- CI is green on the release branch.

**Parallel work allowed:**

- Release notes, security review, and documentation cleanup can run in parallel.
- Final packaging should wait until all release-blocking issues are closed or
  deferred.

## Milestone Assignment Rules

1. Every issue must have exactly one milestone.
2. Every issue must have one area label, one type label, one priority label, and
   one status label.
3. Assign an issue to the earliest milestone where its dependencies are
   satisfied.
4. If an issue spans milestones, split it into milestone-bounded sub-issues.
5. Do not use late staffing as a substitute for scope control. If a milestone is
   slipping, split, defer, or reduce scope.
6. Any issue affecting data semantics, indicator definitions, geography, or
   comparability must reference an ADR or create one.

## Cross-Milestone Dependency Map

| Dependency | Unlocks | Notes |
| --- | --- | --- |
| Label and issue taxonomy | All milestones | Needed for triage and reporting. |
| Source manifest validation | Extract and normalize pipelines | Pipelines need stable source metadata. |
| Provenance field contract | Bronze/Silver tests, Gold marts, visualization metadata | Treat as platform infrastructure. |
| Data quality rule register | Normalization QA and release readiness | Needed before trusting transformed data. |
| Indicator and geography version registries | Comparability gates and dashboard warnings | Required before cross-version charts. |
| Comparability gate behavior | Visualization MVP | Charts should not silently imply comparability. |
| Security/restricted-data boundary | Release | Required before public distribution. |
