# knowledge
WIP for WIPs

## LiteratureAtoms project management loop

This repository treats accumulated ATOM, validation, and SEA artifacts as evidence about how LiteratureAtoms performs in real use. Project changes should be driven by recurring evidence rather than speculative redesign.

```text
ARTIFACT PRODUCTION
        ↓
validation / SEA / usage evidence
        ↓
periodic repository assessment
        ↓
find recurring friction or gaps
        ↓
GitHub Issue
        ↓
design → implementation → testing
        ↓
close issue with evidence
        ↓
new artifacts exercise revised system
```

### Operating model

- **Artifacts are evidence.** ATOM JSON, validation outputs, SEA documents, and usage results show what happens in real use.
- **`PROJECT_HEALTH.md` is the assessment contract.** It defines the domains to inspect, the finding classifications, and the threshold for creating Issues.
- **`health-reports/` preserves assessment history.** Weekly and monthly reports record findings, trends, resolved concerns, and the evidence behind project-management decisions.
- **GitHub Issues are the execution layer.** Only findings classified as `ISSUE` or `URGENT` should normally become Issues. Search existing Issues first and require repository evidence plus acceptance criteria.
- **GitHub Projects can be the prioritization view.** Issues remain the source of truth; a Project board may later provide workflow and prioritization without replacing them.

### Review cadence

- **Weekly lightweight health check:** delta-oriented review of changes since the previous assessment, with emphasis on recurring extraction friction, validation signals, provenance, ATOM ↔ SEA consistency, and repeated manual work.
- **Monthly deep architecture review:** broader review of accumulated health reports and corpus-level evidence for schema pressure, source- and atom-type coverage, test/documentation drift, project organization, and performance/scalability signals.

Scheduled GitHub Actions create recurring task Issues for both reviews. The review itself should use `PROJECT_HEALTH.md`, write the resulting assessment into `health-reports/`, search for existing Issues before creating new ones, and keep actionable work narrowly scoped.
