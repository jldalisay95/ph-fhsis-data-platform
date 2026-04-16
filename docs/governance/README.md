# Governance Playbook

This repository follows **open-source default practices** with explicit controls for health-data comparability, delivery quality, and transparent decision-making.

## 1) Working model

- **Documentation-first delivery**: design intent, assumptions, and tradeoffs are documented before implementation.
- **Small-batch changes**: pull requests should be scoped to one deliverable slice and stay reviewable.
- **Open-by-default communication**: roadmap, issue triage, architecture decisions, and QA status remain visible in-repo.

## 2) Agile operating norms (practical)

- Use **issue-driven planning** with milestone assignment before implementation.
- Keep a groomed backlog with acceptance criteria and definition of done.
- Ship in thin vertical slices where possible (docs + schema + transform + tests).
- Run lightweight sprint cadence (recommended: 2 weeks) with:
  - backlog refinement,
  - planning,
  - daily async standups,
  - sprint review,
  - retrospective with action items.

## 3) Mythical Man-Month inspired guardrails

To avoid coordination drag and low-quality parallelism:

- **Brooks's Law awareness**: do not add people late to already-late tasks without reducing scope.
- **Conceptual integrity over parallel churn**: assign a clear DRI (directly responsible individual) per architecture slice.
- **Surgical-team mindset**: one owner for core design, with focused support roles for testing/docs/review.
- **Build one to throw away (safely)**: use explicit spikes/prototypes before scaling complex pipelines.
- **Plan for communication cost**: issue dependencies must be explicit; avoid hidden cross-team coupling.

## 4) Required governance artifacts

- `docs/governance/milestones.md` for release milestones and exit criteria.
- `docs/governance/labels.md` for standardized triage labels.
- `docs/governance/issues-backlog.md` for prioritized issue drafts.
- `docs/adr/` for architecture decisions that impact data semantics or comparability.

## 5) Definition of Ready (DoR)

An issue is ready when it has:

1. Problem statement and outcome.
2. Scope boundaries (in/out).
3. Acceptance criteria.
4. Labels and milestone.
5. Known dependencies and risks.

## 6) Definition of Done (DoD)

A change is done when:

1. Linked issue acceptance criteria are met.
2. Required docs/ADR updates are complete.
3. Quality checks and tests pass in CI.
4. Comparability and provenance impacts are documented.
5. Reviewer confirms no unresolved high-severity risks.

## 7) Issue lifecycle

1. **Intake** → create issue via template.
2. **Triage** → apply labels + milestone + priority.
3. **Ready** → DoR satisfied.
4. **In progress** → branch + PR linked to issue.
5. **Review/validate** → tests + documentation + QA evidence.
6. **Done** → merged and milestone burndown updated.

## 8) Change policy

- Any schema, mapping, or indicator semantic change requires ADR or explicit rationale in PR.
- Unknown or unverified claims must use repository uncertainty tags.
- Security and privacy concerns must follow `SECURITY.md` and public aggregate defaults.

## 9) Cadence recommendations

- Weekly triage for new issues.
- Mid-sprint risk review for milestone-critical work.
- Monthly roadmap check against milestone completion and drift.
