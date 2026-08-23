# Processing report

## Source

- Folder: `Tsapas Karagiannis 2021`
- Source files: `dom14451-sup-0001-supinfo01.pdf`; `dom14451-sup-0002-supinfo02.docx`
- Title: Comparative efficacy of glucose-lowering medications on body weight and blood pressure in patients with type 2 diabetes: a systematic review and network meta-analysis
- DOI: `10.1111/dom.14451`
- PMID: `34047443`
- PDF SHA-256: `8d5faeebed3bbb5283fe9bbda1c8bf852323d982f9950aca3dad2e3dd158610a`
- PRISMA checklist SHA-256: `f1fc8bc4abdd00e712a211e52472f8f507ea402030bf96cbb5bea8f6956adfbb`
- Source-package limitation: **the main article full text is not present in the selected Drive folder**.

## ATOM

- Atoms: **45**
- Kinds: `{"method": 3, "qualitative_result": 7, "quantitative_result": 34, "study_objective": 1}`
- Semantic batches: `{"tsapas-karagiannis-2021-dom14451-body-weight-v1": 12, "tsapas-karagiannis-2021-dom14451-confidence-v1": 3, "tsapas-karagiannis-2021-dom14451-diastolic-bp-v1": 11, "tsapas-karagiannis-2021-dom14451-general-v1": 1, "tsapas-karagiannis-2021-dom14451-methods-v1": 2, "tsapas-karagiannis-2021-dom14451-quality-v1": 5, "tsapas-karagiannis-2021-dom14451-systolic-bp-v1": 11}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**

The source is a systematic review/network meta-analysis. Review-generated network estimates are tagged `secondary_source` and `review_level_result`; individual trial results are not presented as if the review itself enrolled participants. The appendix contains hundreds of matrix cells, so extraction atomizes all drug-class-versus-placebo NMA cells for the three outcomes plus key review methods/quality assertions rather than every pairwise, individual-drug, subgroup, sensitivity, and CINeMA cell. Those unatomized matrices remain explicitly represented in the coverage manifest.

## SEA

The 177-page supplementary appendix was text-extracted and key load-bearing pages were rendered for visual verification. The flow diagram, inconsistency table, and class-level body-weight, systolic-BP, and diastolic-BP league tables were visually inspected; the SEA embeds the flow and three principal league tables. All 20 numbered supplements, the reference section, and the PRISMA-NMA checklist are represented in the coverage map.

Because the main article full text was absent from the folder, the SEA is explicitly supplement-focused. PubMed/Wiley metadata and abstract were used only to verify identity and high-level article context, not to silently fill missing full-text sections.

## Source-integrity / interpretation findings

1. The final flow diagram yields 424 trials (406 prior + 18 newly eligible trials).
2. Global inconsistency is detectable for body weight (8/94 comparisons; p=0.01) but not for systolic BP (p=0.94) or diastolic BP (p=0.93).
3. CINeMA confidence varies by comparison; rankings should not be interpreted as uniformly high-certainty.
4. The selected packet lacks the main article full text, so article-level narrative appraisal is incomplete by design rather than reconstructed.

## References

The supplement contains **422** numbered references. They were exported to `tsapas-karagiannis-2021-dom14451-references.md` with line wrapping normalized and without external bibliographic correction.

## Governing-source boundary

Applied: `literature(1).py`, `literature_atoms(1).py`, `literature_atom.schema.json`, `README(2).md`, `example_atom(1).json`, `large-source-ATOM-SEA.md`, and `summary-evaluation-appraisal-protocol-v4-compact.md`. The available file named `summary-evaluation-appraisal-protocol-v4-compact.md` internally identifies itself as **Integrated Compact v3**; this version-label conflict is preserved rather than silently corrected. The requested `unslop.skill.md` was not available in the runtime/project source set and therefore could not be inspected.

## Output files

- `tsapas-karagiannis-2021-dom14451-atoms.json`
- `tsapas-karagiannis-2021-dom14451-validation.json`
- `tsapas-karagiannis-2021-dom14451-coverage.json`
- `tsapas-karagiannis-2021-dom14451-crosswalk.json`
- `tsapas-karagiannis-2021-dom14451-sea.html`
- `tsapas-karagiannis-2021-dom14451-sea-qa.json`
- `tsapas-karagiannis-2021-dom14451-references.md`
- `tsapas-karagiannis-2021-dom14451-processing-report.md`
