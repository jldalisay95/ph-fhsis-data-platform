# GitHub Issue Backlog

This backlog is written as GitHub-ready issue drafts. It uses parent tracker
issues for broad outcomes and sub-issues for independently deliverable work.

## How to Use This Backlog

1. Create the parent tracker issue first for each milestone.
2. Create only the sub-issues needed for the next planning window.
3. Keep each sub-issue small enough to complete in one focused pull request.
4. Close parent issues only after all required sub-issues are closed or
   explicitly deferred.
5. Re-triage priority at the start of each milestone.

## First Issues to Address

Start with these in order:

1. `GOV-01` - complete the governance operating model.
2. `GOV-02` - align issue templates with the label taxonomy.
3. `GOV-03` - harden CI for docs, linting, and tests.
4. `REG-02` - implement schema-backed source manifest validation.
5. `REG-04` - establish the initial public source inventory baseline.
6. `PIPE-02` - define Bronze and Silver contracts.
7. `PIPE-04` - implement provenance propagation through normalization.
8. `COMP-04` - define comparability assessment workflow.
9. `VIZ-03` - validate view specs against metadata gates.
10. `REL-02` - complete release readiness checklist.

## Parallel Work Lanes

| Lane | Can Start | Work |
| --- | --- | --- |
| Governance and CI | Immediately | `GOV-*`, `REL-02` draft checklist |
| Source Registry | After `GOV-02` | `REG-02`, `REG-03`, `REG-04` |
| Pipeline Foundation | After `REG-02` | `PIPE-02`, `PIPE-03`, `PIPE-05` |
| Comparability Governance | After `PIPE-02` | `COMP-02`, `COMP-03`, `COMP-05` |
| Visualization Specs | After `COMP-04` draft | `VIZ-02`, `VIZ-03`, `VIZ-04` |
| Release Packaging | After M4 scope is stable | `REL-*` |

## M0 - Governance & Operating Baseline

### GOV-01: Complete project governance operating model

- **Type:** Parent issue
- **Milestone:** `M0 - Governance & Operating Baseline`
- **Labels:** `area:governance`, `type:docs`, `priority:P1`, `status:ready`, `risk:delivery`
- **Problem:** Contributors need consistent rules for planning, review,
  prioritization, and documentation-first work.
- **Sub-issues:** `GOV-02`, `GOV-03`, `GOV-04`, `GOV-05`
- **Acceptance criteria:**
  - Label taxonomy, issue templates, milestone rules, and PR review expectations
    are consistent.
  - Contribution workflow explains when ADRs, validation docs, or mapping docs
    are required.
  - M0 exit criteria in `docs/governance/milestones.md` are met.
- **Definition of done:** all required M0 governance sub-issues are closed.
- **Parallelization:** parent tracker only; implementation is in sub-issues.

### GOV-02: Align issue templates with label taxonomy and milestone rules

- **Type:** Sub-issue of `GOV-01`
- **Milestone:** `M0 - Governance & Operating Baseline`
- **Labels:** `area:governance`, `type:docs`, `priority:P1`, `status:ready`
- **Problem:** Issue templates should guide contributors toward complete,
  triageable requests.
- **Acceptance criteria:**
  - Each issue template asks for area, type, priority, expected milestone, and
    validation status.
  - Mapping, transform, source onboarding, and dashboard templates reference the
    required uncertainty tags.
  - Template guidance matches `docs/governance/labels.md`.
- **Definition of done:** templates are updated and reviewed against the label
  rules.
- **Dependencies:** none.
- **Parallelization:** can run in parallel with `GOV-03`.

### GOV-03: Harden CI for docs, linting, and tests

- **Type:** Sub-issue of `GOV-01`
- **Milestone:** `M0 - Governance & Operating Baseline`
- **Labels:** `area:ci`, `type:feature`, `priority:P1`, `status:ready`, `risk:delivery`
- **Problem:** The repository needs automated checks before implementation work
  grows.
- **Acceptance criteria:**
  - CI runs Python tests.
  - CI runs linting or formatting checks configured in `pyproject.toml`.
  - Documentation link checks or equivalent docs integrity checks run in CI.
  - Local commands are documented in `CONTRIBUTING.md`.
- **Definition of done:** CI is green on the default branch.
- **Dependencies:** none.
- **Parallelization:** can run in parallel with `GOV-02` and `GOV-04`.

### GOV-04: Link documentation-first workflow from contributor entry points

- **Type:** Sub-issue of `GOV-01`
- **Milestone:** `M0 - Governance & Operating Baseline`
- **Labels:** `area:docs`, `type:docs`, `priority:P2`, `status:ready`
- **Problem:** Contributors can miss semantic documentation requirements if they
  only read top-level files.
- **Acceptance criteria:**
  - `README.md` and `CONTRIBUTING.md` link to governance, ADR, mapping, and
    validation docs.
  - Data semantics changes explicitly require docs updates.
  - Unknown source and validation tags are listed in the workflow.
- **Definition of done:** entry-point docs guide a new contributor to the right
  governance docs.
- **Dependencies:** `GOV-02` recommended.
- **Parallelization:** can run with `GOV-03`.

### GOV-05: Add ADR review requirement to PR workflow

- **Type:** Sub-issue of `GOV-01`
- **Milestone:** `M0 - Governance & Operating Baseline`
- **Labels:** `area:governance`, `type:docs`, `priority:P2`, `status:ready`, `process:adr-required`
- **Problem:** Data model, geography, indicator, and comparability changes need
  durable decisions.
- **Acceptance criteria:**
  - PR template asks whether an ADR is required.
  - ADR index describes when to create or update an ADR.
  - Changes to data semantics without ADR context are considered incomplete.
- **Definition of done:** PR review checklist includes ADR decision evidence.
- **Dependencies:** none.
- **Parallelization:** can run in parallel with `GOV-04`.

## M1 - Source Registry & Provenance Foundation

### REG-01: Establish source registry and provenance intake

- **Type:** Parent issue
- **Milestone:** `M1 - Source Registry & Provenance Foundation`
- **Labels:** `area:database`, `type:feature`, `priority:P1`, `status:ready`, `risk:data-quality`
- **Problem:** The platform cannot safely extract or normalize data until source
  identity, access level, provenance, and validation status are captured
  consistently.
- **Sub-issues:** `REG-02`, `REG-03`, `REG-04`, `REG-05`
- **Acceptance criteria:**
  - Source manifest validation is automated.
  - Source inventory baseline exists.
  - Public and restricted source boundaries are documented.
  - Required provenance fields are tested.
- **Definition of done:** M1 exit criteria are met and downstream pipeline work
  can consume validated source metadata.
- **Parallelization:** `REG-02`, `REG-03`, and `REG-04` can run in parallel after
  `GOV-02`.

### REG-02: Validate source registration manifests against a schema

- **Type:** Sub-issue of `REG-01`
- **Milestone:** `M1 - Source Registry & Provenance Foundation`
- **Labels:** `area:database`, `type:feature`, `priority:P1`, `status:ready`, `risk:data-quality`
- **Problem:** Current manifest loading parses YAML but does not enforce
  required fields or valid values.
- **Acceptance criteria:**
  - Manifest schema requires source ID, title, retrieval date, access level,
    checksum, validation status, and notes.
  - Invalid manifests produce actionable errors.
  - Passing and failing examples are covered by tests.
- **Definition of done:** schema-backed validation is implemented and tested.
- **Dependencies:** `GOV-02` recommended.
- **Parallelization:** can run with `REG-03` and `REG-04`.

### REG-03: Add checksum and retrieval metadata helper

- **Type:** Sub-issue of `REG-01`
- **Milestone:** `M1 - Source Registry & Provenance Foundation`
- **Labels:** `area:database`, `type:feature`, `priority:P2`, `status:ready`, `risk:data-quality`
- **Problem:** Source records need repeatable checksum and retrieval metadata to
  support auditability.
- **Acceptance criteria:**
  - Helper computes checksums for local public source files.
  - Helper records retrieval timestamp in a consistent format.
  - Tests cover stable checksum output and missing-file behavior.
- **Definition of done:** helper is documented and tested.
- **Dependencies:** none.
- **Parallelization:** can run with `REG-02`.

### REG-04: Create initial public source inventory baseline

- **Type:** Sub-issue of `REG-01`
- **Milestone:** `M1 - Source Registry & Provenance Foundation`
- **Labels:** `area:database`, `type:docs`, `priority:P1`, `status:ready`, `risk:data-quality`
- **Problem:** The project needs a clear source corpus scope before extraction
  work starts.
- **Acceptance criteria:**
  - Source inventory lists known public source candidates and missing inputs.
  - Each source has access level, validation status, and uncertainty tags.
  - Inventory identifies which sources are in scope for v0.1.0.
- **Definition of done:** source inventory baseline is reviewed and linked from
  source onboarding docs.
- **Dependencies:** none.
- **Parallelization:** can run with `REG-02`; does not require code changes.

### REG-05: Document restricted-data boundary and access gates

- **Type:** Sub-issue of `REG-01`
- **Milestone:** `M1 - Source Registry & Provenance Foundation`
- **Labels:** `area:governance`, `type:security`, `priority:P1`, `status:ready`, `risk:security`
- **Problem:** The repository states public aggregate data is the default, but
  restricted workflow boundaries need practical contributor guidance.
- **Acceptance criteria:**
  - Restricted files are explicitly prohibited from commits.
  - Access, storage, and processing assumptions are marked as user input needed.
  - Security guidance is linked from source onboarding docs and `SECURITY.md`.
- **Definition of done:** contributors can distinguish allowed public aggregate
  work from restricted-data work.
- **Dependencies:** none.
- **Parallelization:** can run with `REG-04`.

## M2 - Bronze/Silver Normalization Foundation

### PIPE-01: Build testable extraction and normalization foundation

- **Type:** Parent issue
- **Milestone:** `M2 - Bronze/Silver Normalization Foundation`
- **Labels:** `area:database`, `type:feature`, `priority:P1`, `status:ready`, `risk:data-quality`
- **Problem:** Pipeline stubs need stable contracts, provenance propagation, and
  quality checks before real source-specific transforms are added.
- **Sub-issues:** `PIPE-02`, `PIPE-03`, `PIPE-04`, `PIPE-05`, `PIPE-06`
- **Acceptance criteria:**
  - Bronze and Silver contracts are documented.
  - Pipeline interfaces can be tested without restricted data.
  - Required provenance survives each transformation stage.
  - Data quality rules are loaded from the rules register.
- **Definition of done:** M2 exit criteria are met and M3 comparability work can
  rely on canonical record structure.
- **Parallelization:** documentation, interface, and QA rule work can run in
  parallel after `REG-02`.

### PIPE-02: Define Bronze and Silver data contracts

- **Type:** Sub-issue of `PIPE-01`
- **Milestone:** `M2 - Bronze/Silver Normalization Foundation`
- **Labels:** `area:database`, `type:docs`, `priority:P1`, `status:ready`, `risk:data-quality`, `process:adr-required`
- **Problem:** Extract and normalization work needs explicit contracts for raw,
  Bronze, and Silver layers.
- **Acceptance criteria:**
  - Bronze contract defines source identity, raw component identity, extraction
    timestamp, and provenance fields.
  - Silver contract defines canonical observation fields and validation status.
  - Contract references existing ADRs or creates a new ADR if scope changes.
- **Definition of done:** contracts are documented and linked from pipeline docs.
- **Dependencies:** `REG-02`.
- **Parallelization:** can run with `PIPE-03`.

### PIPE-03: Add extractor interface and public fixture path

- **Type:** Sub-issue of `PIPE-01`
- **Milestone:** `M2 - Bronze/Silver Normalization Foundation`
- **Labels:** `area:database`, `type:feature`, `priority:P2`, `status:ready`
- **Problem:** Source-specific extraction should plug into a stable interface and
  be testable with public fixtures.
- **Acceptance criteria:**
  - Extractor interface accepts a validated manifest.
  - Fixture path and example output are documented.
  - Tests cover the no-op or sample public fixture extractor.
- **Definition of done:** extractor interface is importable and covered by tests.
- **Dependencies:** `REG-02`, `PIPE-02` recommended.
- **Parallelization:** can run with `PIPE-05`.

### PIPE-04: Implement provenance propagation through normalization

- **Type:** Sub-issue of `PIPE-01`
- **Milestone:** `M2 - Bronze/Silver Normalization Foundation`
- **Labels:** `area:database`, `type:qa`, `priority:P1`, `status:ready`, `risk:data-quality`
- **Problem:** Trust in normalized records requires proof that source provenance
  survives transformation.
- **Acceptance criteria:**
  - Tests verify required provenance fields survive Bronze-to-Silver conversion.
  - Missing provenance produces clear validation failures.
  - CI runs the provenance propagation tests.
- **Definition of done:** provenance propagation test fails before the behavior
  exists and passes after implementation.
- **Dependencies:** `PIPE-02`.
- **Parallelization:** should wait for contract definitions.

### PIPE-05: Load and evaluate data quality rules register

- **Type:** Sub-issue of `PIPE-01`
- **Milestone:** `M2 - Bronze/Silver Normalization Foundation`
- **Labels:** `area:database`, `type:feature`, `priority:P2`, `status:ready`, `risk:data-quality`
- **Problem:** The rules register exists as a template but is not executable.
- **Acceptance criteria:**
  - Rules register parser validates rule ID, layer, severity, status, and
    description.
  - At least one simple rule is evaluated in tests.
  - Rule failures produce structured quality issues.
- **Definition of done:** data quality rule loading and one evaluation path are
  tested.
- **Dependencies:** `REG-02`.
- **Parallelization:** can run with `PIPE-03`.

### PIPE-06: Add pipeline tests to CI

- **Type:** Sub-issue of `PIPE-01`
- **Milestone:** `M2 - Bronze/Silver Normalization Foundation`
- **Labels:** `area:ci`, `type:qa`, `priority:P1`, `status:ready`, `risk:delivery`
- **Problem:** Pipeline behavior needs to be protected by automated checks.
- **Acceptance criteria:**
  - CI runs validation, extractor, normalization, and quality rule tests.
  - Test failures include useful file or object identifiers.
  - Local test command is documented.
- **Definition of done:** CI catches a representative failing pipeline test.
- **Dependencies:** `GOV-03`, at least one pipeline test from M2.
- **Parallelization:** runs after early M2 implementation starts.

## M3 - Comparability & Indicator Governance

### COMP-01: Implement comparability governance controls

- **Type:** Parent issue
- **Milestone:** `M3 - Comparability & Indicator Governance`
- **Labels:** `area:database`, `type:feature`, `priority:P1`, `status:ready`, `risk:comparability`
- **Problem:** The project must prevent users from treating non-comparable
  indicators, geographies, or reporting periods as comparable.
- **Sub-issues:** `COMP-02`, `COMP-03`, `COMP-04`, `COMP-05`
- **Acceptance criteria:**
  - Indicator and geography version workflows are documented.
  - Comparability assessment has explicit statuses and blocking behavior.
  - Deprecated and replaced indicator mappings are validated.
- **Definition of done:** M3 exit criteria are met and visualization work has
  usable metadata gates.
- **Parallelization:** registries can run in parallel after `PIPE-02`.

### COMP-02: Define indicator definition version workflow

- **Type:** Sub-issue of `COMP-01`
- **Milestone:** `M3 - Comparability & Indicator Governance`
- **Labels:** `area:database`, `type:docs`, `priority:P1`, `status:ready`, `risk:comparability`, `process:adr-required`
- **Problem:** Indicator names and formulas can change across versions, making
  naive trend analysis unsafe.
- **Acceptance criteria:**
  - Workflow captures indicator code, version label, definition text, source,
    denominator, formula notes, and validation status.
  - Unknown formula or denominator details are explicitly tagged.
  - Workflow links to the denominator formula note register.
- **Definition of done:** indicator version workflow is documented and reviewed.
- **Dependencies:** `PIPE-02`.
- **Parallelization:** can run with `COMP-03`.

### COMP-03: Define geography version registry workflow

- **Type:** Sub-issue of `COMP-01`
- **Milestone:** `M3 - Comparability & Indicator Governance`
- **Labels:** `area:database`, `type:docs`, `priority:P1`, `status:ready`, `risk:comparability`, `process:adr-required`
- **Problem:** Geography boundaries and hierarchies can change over time and
  affect comparability.
- **Acceptance criteria:**
  - Workflow captures geography version ID, authority, effective dates, parent
    relationships, and validation status.
  - Unknown authority or cadence is explicitly tagged.
  - Mapping rules are linked from mapping docs.
- **Definition of done:** geography workflow is documented and ready for
  validation.
- **Dependencies:** `PIPE-02`.
- **Parallelization:** can run with `COMP-02`.

### COMP-04: Add comparability assessment checklist and gate statuses

- **Type:** Sub-issue of `COMP-01`
- **Milestone:** `M3 - Comparability & Indicator Governance`
- **Labels:** `area:database`, `type:docs`, `priority:P1`, `status:ready`, `risk:comparability`
- **Problem:** Cross-version analysis needs a repeatable decision process before
  charts or marts imply comparability.
- **Acceptance criteria:**
  - Checklist covers geography, indicator definition, formula, denominator,
    reporting cadence, and source version changes.
  - Gate statuses include unsafe default, under review, validated, and rejected
    or blocked.
  - Unknown comparability maps to blocked or warning behavior.
- **Definition of done:** checklist is linked from contributing and
  visualization docs.
- **Dependencies:** `COMP-02`, `COMP-03` recommended.
- **Parallelization:** can start as a draft while registry workflows are in
  review.

### COMP-05: Validate deprecated and replaced indicator crosswalks

- **Type:** Sub-issue of `COMP-01`
- **Milestone:** `M3 - Comparability & Indicator Governance`
- **Labels:** `area:database`, `type:qa`, `priority:P2`, `status:ready`, `risk:comparability`
- **Problem:** Indicator replacement mappings can create false continuity if not
  reviewed.
- **Acceptance criteria:**
  - Crosswalk entries require old indicator ID, replacement indicator ID,
    effective date, source, and validation status.
  - Tests or checks flag incomplete crosswalk rows.
  - Documentation explains when a replacement does not imply comparability.
- **Definition of done:** crosswalk validation is documented and tested.
- **Dependencies:** `COMP-02`.
- **Parallelization:** can run after indicator workflow draft exists.

## M4 - Visualization MVP with Metadata Gates

### VIZ-01: Deliver visualization MVP with metadata gates

- **Type:** Parent issue
- **Milestone:** `M4 - Visualization MVP with Metadata Gates`
- **Labels:** `area:visualization`, `type:feature`, `priority:P1`, `status:ready`, `risk:comparability`, `process:needs-design`
- **Problem:** Visualizations must show provenance and comparability status
  rather than presenting unqualified trends.
- **Sub-issues:** `VIZ-02`, `VIZ-03`, `VIZ-04`, `VIZ-05`, `VIZ-06`
- **Acceptance criteria:**
  - MVP scope is tied to audience and validated metadata.
  - View specs are validated.
  - Comparability warnings and blocked states are QA-tested.
  - Accessibility baseline is included.
- **Definition of done:** M4 exit criteria are met and the MVP can be included in
  v0.1.0 release notes.
- **Parallelization:** specs, QA, and app scaffold can run in parallel after
  metadata requirements are stable.

### VIZ-02: Define MVP dashboard audience and use-case scope

- **Type:** Sub-issue of `VIZ-01`
- **Milestone:** `M4 - Visualization MVP with Metadata Gates`
- **Labels:** `area:visualization`, `type:docs`, `priority:P1`, `status:ready`, `process:needs-design`
- **Problem:** Dashboard requirements should be grounded in audience needs and
  not generic chart inventory.
- **Acceptance criteria:**
  - MVP identifies primary audience, questions, and excluded use cases.
  - Each proposed view maps to required metadata fields.
  - Scope avoids restricted-data workflows.
- **Definition of done:** dashboard scope is documented and linked from
  visualization README.
- **Dependencies:** `COMP-04` draft.
- **Parallelization:** can run with `VIZ-03`.

### VIZ-03: Validate view specs against required metadata gates

- **Type:** Sub-issue of `VIZ-01`
- **Milestone:** `M4 - Visualization MVP with Metadata Gates`
- **Labels:** `area:visualization`, `type:feature`, `priority:P1`, `status:ready`, `risk:comparability`
- **Problem:** View specs require metadata fields but are not yet validated.
- **Acceptance criteria:**
  - Validator checks view ID, indicator IDs, source document ID, report version
    ID, indicator version ID, geography version ID, and comparability gate.
  - Invalid specs fail with actionable messages.
  - Tests cover valid and invalid view specs.
- **Definition of done:** view spec validation runs locally and in CI.
- **Dependencies:** `COMP-04`.
- **Parallelization:** can run with `VIZ-04`.

### VIZ-04: Define comparability warning and blocked-state behavior

- **Type:** Sub-issue of `VIZ-01`
- **Milestone:** `M4 - Visualization MVP with Metadata Gates`
- **Labels:** `area:visualization`, `type:feature`, `priority:P1`, `status:ready`, `risk:comparability`, `process:needs-design`
- **Problem:** Users need clear warning states when comparability is unvalidated
  or rejected.
- **Acceptance criteria:**
  - Warning trigger conditions are documented.
  - Blocked-state behavior is documented for unsafe comparisons.
  - User-facing copy is factual and avoids implying validation.
  - QA checklist includes warning and blocked-state cases.
- **Definition of done:** behavior spec and QA scenarios are merged.
- **Dependencies:** `COMP-04`.
- **Parallelization:** can run with `VIZ-03` and `VIZ-05`.

### VIZ-05: Expand visualization QA and accessibility checklist

- **Type:** Sub-issue of `VIZ-01`
- **Milestone:** `M4 - Visualization MVP with Metadata Gates`
- **Labels:** `area:visualization`, `type:qa`, `priority:P2`, `status:ready`
- **Problem:** Visualization QA should cover metadata, comparability, and
  baseline accessibility before release.
- **Acceptance criteria:**
  - QA checklist includes metadata completeness, provenance drilldown,
    comparability warning behavior, keyboard path, color contrast, and text
    alternatives.
  - Checklist is usable for manual review.
  - At least one MVP view has a completed QA example.
- **Definition of done:** QA checklist is linked from visualization docs.
- **Dependencies:** `VIZ-02`, `VIZ-04` recommended.
- **Parallelization:** can run with `VIZ-04`.

### VIZ-06: Scaffold dashboard app around validated view specs

- **Type:** Sub-issue of `VIZ-01`
- **Milestone:** `M4 - Visualization MVP with Metadata Gates`
- **Labels:** `area:visualization`, `type:feature`, `priority:P2`, `status:ready`, `process:needs-design`
- **Problem:** The app scaffold should consume validated view specs rather than
  hard-code untracked chart behavior.
- **Acceptance criteria:**
  - App scaffold reads or references validated view specs.
  - Missing metadata produces a blocked or warning state.
  - README explains how to run or inspect the MVP scaffold.
- **Definition of done:** MVP scaffold is documented and testable.
- **Dependencies:** `VIZ-03`, `VIZ-04`.
- **Parallelization:** can start after validation contract is stable.

## M5 - Release Readiness (v0.1.0)

### REL-01: Prepare v0.1.0 release

- **Type:** Parent issue
- **Milestone:** `M5 - Release Readiness (v0.1.0)`
- **Labels:** `area:governance`, `type:docs`, `priority:P1`, `status:ready`, `risk:delivery`
- **Problem:** The first public release needs a clear statement of implemented
  scope, scaffolded scope, validation status, and known limitations.
- **Sub-issues:** `REL-02`, `REL-03`, `REL-04`, `REL-05`
- **Acceptance criteria:**
  - Release readiness checklist is complete.
  - CI is green.
  - Security and restricted-data boundary review is complete.
  - Release notes distinguish implemented, scaffolded, deferred, and unknown
    items.
- **Definition of done:** v0.1.0 can be tagged without ambiguous validation
  claims.
- **Parallelization:** release docs, security review, and examples can run in
  parallel after M4 scope is stable.

### REL-02: Publish v0.1.0 release-readiness checklist

- **Type:** Sub-issue of `REL-01`
- **Milestone:** `M5 - Release Readiness (v0.1.0)`
- **Labels:** `area:governance`, `type:docs`, `priority:P1`, `status:ready`, `risk:delivery`
- **Problem:** Release quality can drift without explicit go/no-go criteria.
- **Acceptance criteria:**
  - Checklist covers docs completeness, tests, security review, unresolved
    risks, validation status, and known limitations.
  - Checklist maps each release gate to an owner or role.
  - Release PR template references the checklist.
- **Definition of done:** checklist is linked from release workflow docs.
- **Dependencies:** `GOV-01` recommended.
- **Parallelization:** can be drafted early and finalized in M5.

### REL-03: Complete public aggregate and restricted-data security review

- **Type:** Sub-issue of `REL-01`
- **Milestone:** `M5 - Release Readiness (v0.1.0)`
- **Labels:** `area:governance`, `type:security`, `priority:P1`, `status:ready`, `risk:security`
- **Problem:** The release must not imply support for restricted-data workflows
  or accidentally include restricted artifacts.
- **Acceptance criteria:**
  - Repository is checked for restricted sample files or secrets.
  - Security docs state what is allowed in public aggregate workflows.
  - Restricted workflow limitations are included in release notes.
- **Definition of done:** security review is documented and no release-blocking
  findings remain open.
- **Dependencies:** `REG-05`.
- **Parallelization:** can run with `REL-04`.

### REL-04: Create release notes and known-limitations document

- **Type:** Sub-issue of `REL-01`
- **Milestone:** `M5 - Release Readiness (v0.1.0)`
- **Labels:** `area:docs`, `type:docs`, `priority:P1`, `status:ready`, `risk:delivery`
- **Problem:** Users need to know what v0.1.0 does and does not validate.
- **Acceptance criteria:**
  - Release notes list implemented features, scaffolded features, known
    limitations, and deferred work.
  - Notes avoid unsupported claims about official indicator definitions.
  - Notes link to unresolved questions and validation docs.
- **Definition of done:** release notes are reviewed before tagging.
- **Dependencies:** M4 scope stable.
- **Parallelization:** can run with `REL-03`.

### REL-05: Add end-to-end contributor example

- **Type:** Sub-issue of `REL-01`
- **Milestone:** `M5 - Release Readiness (v0.1.0)`
- **Labels:** `area:docs`, `type:docs`, `priority:P2`, `status:ready`, `process:good-first-issue`
- **Problem:** New contributors need a concrete example that follows the
  intended source-to-view workflow without using restricted data.
- **Acceptance criteria:**
  - Example walks through source registration, validation, transform scaffold,
    quality rule, comparability note, and view spec.
  - Example uses only public or synthetic data.
  - Example clearly marks assumptions and validation status.
- **Definition of done:** example is linked from top-level README and relevant
  package READMEs.
- **Dependencies:** `REG-02`, `PIPE-04`, `COMP-04`, `VIZ-03`.
- **Parallelization:** should wait until the main workflow is stable.

## Backlog Hygiene Rules

1. Prefer outcome-based titles: start with a verb and describe the user or
   platform value.
2. Keep one behavioral change per issue where possible.
3. Use parent issues for milestone outcomes and sub-issues for pull-request-sized
   work.
4. Every issue needs acceptance criteria and a definition of done.
5. Any issue touching indicator semantics, geography, data contracts, or
   comparability needs ADR consideration.
6. Unknown source facts must be tagged with `[MISSING SOURCE]`,
   `[USER INPUT NEEDED]`, `[REQUIRES VALIDATION]`, or
   `[ASSUMPTION - LOW CONFIDENCE]`.
7. Re-prioritize at milestone boundaries. Do not silently carry stale P1 labels
   across milestones.
