# LiteratureAtoms Health Reports

This directory stores historical LiteratureAtoms repository assessments. Reports preserve the analysis and evidence that led to project-management decisions; GitHub Issues remain the execution layer for actionable work.

## Cadence

- **Weekly lightweight health check:** focus on changes since the previous assessment, recurring extraction friction, validation signals, provenance problems, ATOM ↔ SEA inconsistencies, and newly repeated manual work.
- **Monthly deep architecture review:** examine longer-running patterns across the corpus, schema pressure, source- and atom-type coverage, project boundaries, test strategy, documentation drift, and performance/scalability signals.

## Naming

- Weekly: `YYYY-MM-DD-weekly.md`
- Monthly: `YYYY-MM-DD-monthly-architecture.md`

## Minimum report contents

1. Scope and comparison baseline.
2. New or materially changed evidence.
3. Findings classified as `OBSERVATION`, `WATCH`, `ISSUE`, or `URGENT`.
4. Existing issues linked to relevant findings.
5. New issues created, if any.
6. Findings resolved or downgraded since the prior report.
7. Recommended baseline for the next assessment.

Health checks should be delta-oriented. A recurring concern can be promoted from `WATCH` to `ISSUE` when repeated evidence demonstrates that changing the project is warranted.
