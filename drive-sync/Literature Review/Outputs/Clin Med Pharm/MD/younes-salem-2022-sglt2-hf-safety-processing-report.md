# Processing report — Younes Salem 2022

## Source

- **Title:** Safety outcomes of SGLT2i in the heart failure trials: A systematic review and Meta-analysis
- **Journal:** International Journal of Cardiology 366 (2022) 51–56.
- **DOI:** `10.1016/j.ijcard.2022.06.059`
- **PMID:** `35777490`
- **Main PDF SHA-256:** `95b333b5196c5d02cfcb8c84a7e111a44fd69ec97b45c3e1b43e8364bb4f4bdf`
- **Appendix A DOCX SHA-256:** `3c6339367c57661fd866f64296bc99c549cd781d8c26869878e5872bb1b2f8e3`
- **Appendix B DOCX SHA-256:** `72aaa1f147fcb7d8ff1571af141ecd8ddef2a034344c64821ecb27bf07de0afa`

## ATOM

- Shared publication ID: `71a4e659-9ee7-4c81-b41c-b2299b930851`
- LiteratureAtoms: **66**
- Counts by kind: `{"adverse_event": 41, "author_conclusion": 1, "comparator_description": 1, "conflict_of_interest": 1, "eligibility_criterion": 1, "funding_disclosure": 1, "intervention_description": 1, "limitation": 5, "method": 10, "outcome_definition": 1, "population_description": 2, "study_objective": 1}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS** (0 errors)
- Sufficiency validation: **PASS** (0 errors, 0 warnings)
- Exact duplicate review: **0 duplicates**

## SEA

- Main coverage: **3 figures + 1 table**.
- Supplement coverage: **Appendix A search strategies + Appendix B Figures 4–7**.
- SEA QA: **PASS**.
- Verdict: **Read soon**.

## Reference list

- Printed reference entries captured: **25**.
- Source numbering is preserved.

## Source consistency / interpretation flags

1. The protocol registry is printed as `PRESPRO`; the source spelling was preserved rather than silently corrected.
2. The study-selection sentence around trials with <300 participants and “Phase 2 and 3 clinical trials” is syntactically ambiguous; no unsupported phase-based eligibility rule was inferred.
3. Appendix B §6.2 says `symptomatic hypertension`, while the main article and forest plot label the outcome symptomatic hypotension.
4. Appendix B §7.2 points to Figure 5 for HFpEF-exclusion sensitivity results even though the supplement captions identify Figures 6–7 for that analysis.
5. Appendix B Figure 7's hyperkalemia panel duplicates the AKI rows and pooled OR 0.67 (95% CI 0.36–1.25). Because the narrative omits a corresponding hyperkalemia result, no HFpEF-exclusion hyperkalemia atom was generated from that panel.
6. Safety outcomes were not uniformly reported across trials, so pooled denominators differ by outcome; rare-event estimates can be imprecise.

## Schema gap

The current LiteratureAtom model has no dedicated systematic-review/meta-analysis result kind. Review-level pooled safety findings were represented as `adverse_event` atoms with descriptive `systematic_review`, `meta_analysis`, and `review_level_evidence` tags without altering the schema.

## Output files

### JSON
- `younes-salem-2022-sglt2-hf-safety-atoms.json`
- `younes-salem-2022-sglt2-hf-safety-validation.json`
- `younes-salem-2022-sglt2-hf-safety-coverage.json`
- `younes-salem-2022-sglt2-hf-safety-crosswalk.json`
- `younes-salem-2022-sglt2-hf-safety-sea-qa.json`

### HTML
- `younes-salem-2022-sglt2-hf-safety-sea.html`

### Markdown
- `younes-salem-2022-sglt2-hf-safety-references.md`
- `younes-salem-2022-sglt2-hf-safety-processing-report.md`
