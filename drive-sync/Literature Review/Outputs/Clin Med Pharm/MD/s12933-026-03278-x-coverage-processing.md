# s12933-026-03278-x — coverage and processing note

## Source identity

- **Title:** A three-metabolite microbiota-associated signature for early risk stratification of gestational diabetes mellitus
- **Primary file:** `s12933-026-03278-x.pdf`
- **Journal:** Cardiovascular Diabetology. 2026;25:214.
- **DOI:** 10.1186/s12933-026-03278-x
- **Published online:** 7 August 2026
- **Source type/design:** Research article; multistage multicenter biomarker/prediction study combining retrospective nested case-control phases with independent external case-control validation and a prospective validation cohort.
- **Primary PDF length:** 19 pages.

## Coverage manifest

- **Substantive sections/headings inspected:** Abstract; Background; Materials and methods (Study design; Serum metabolomics analysis; Metagenomic sequencing and microecological analysis; Identification of key microbial taxa and multi-omics association analysis; GDM prediction model development and evaluation; Statistical analysis); Results (clinical characteristics; serum metabolomics; persistent metabolites; metagenomics/network analysis; microbial-clinical and microbial-metabolite correlations; model construction; external/prospective validation; incremental value beyond clinical factors); Discussion; Conclusion; declarations.
- **Main-text figures:** 7/7 reconciled.
  - Figure 1 — five-phase study design and analytical workflow.
  - Figure 2 — early/mid-pregnancy metabolomic separation, volcano plots, metabolite classes, KEGG enrichment.
  - Figure 3 — 14 persistent metabolites, pathway enrichment, representative ROC curves.
  - Figure 4 — species co-occurrence networks, topology, shared high-connectivity species.
  - Figure 5 — microbial taxa vs clinical metabolic parameters.
  - Figure 6 — microbial taxa vs serum metabolites and Sankey association summary.
  - Figure 7 — three-metabolite selection and GLM development/validation across cohorts.
- **Main-text tables:** 4/4 reconciled.
  - Table 1 — cohort composition and phase roles.
  - Table 2 — discovery-cohort clinical characteristics.
  - Table 3 — locked GLM performance across cohorts.
  - Table 4 — clinical-only, metabolite-only, and combined-model comparison.
- **Algorithms/workflows:** Five-phase biomarker discovery/replication/model-development/validation workflow; repeated 10-fold cross-validation; fixed Youden threshold; locked external/prospective validation; clinical incremental-value benchmark.
- **Supplementary material:** The PDF references Supplementary Materials 1–6, Supplementary Methods, Supplementary Tables/Figures/Data. These materials were **not specified or supplied for Task 12** and were not fetched or substituted.
- **Visual strategy:** Every main-text figure/table is represented in the SEA as a structured block. No screenshot was embedded because the load-bearing content could be reconstructed from the primary-PDF captions, tables, and accompanying text.
- **Omissions:** Pure bibliography pages were not condensed. Supplementary materials were omitted because they were not provided for this task.

## @ATOM extraction status

- **Atom file:** `s12933-026-03278-x-literature-atoms.json`
- **Validation file:** `s12933-026-03278-x-atom-validation.json`
- **Atoms:** 64
- **Pydantic structural validation:** PASS
- **JSON Schema validation:** PASS (0 errors)
- **Sufficiency validation:** PASS (0 errors; 0 warnings)
- **Assertion origin handling:** All extracted assertions are source-reported content; no calculated or extractor-inferred atoms were added.

## Extraction limitations

1. The primary article defers assay preparation, instrument settings, metabolite annotation, metagenomic processing details, and several model-comparison details to supplementary material that was not supplied.
2. Correlation patterns without exact numeric rho values in the main PDF were represented qualitatively rather than inventing numerical coefficients.
3. The study reports 2,693 women enrolled across the three hospitals, while Table 1 describes the analytic cohorts used for discovery/modeling/validation; these are preserved as separate reported quantities rather than reconciled by inference.
4. The prospective model has strong discrimination but only moderate PPV (0.525), and the primary PDF does not report absolute calibration metrics or decision-curve/clinical-utility analysis.
