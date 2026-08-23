# Yao et al. 2024 - processing report

Source: BMJ 2024;384:e076410. DOI: 10.1136/bmj-2023-076410. PMID: 38286487.

## Inputs
- `bmj-2023-076410.full.pdf` - 11-page main article; SHA-256 `bb96b9a885b8b9f7342425e73c22e191ca880852fb46e7a710ae1782d9458223`.
- `yaoh076410.ww.pdf` - 242-page supplementary appendix; SHA-256 `872a86753725dcdeb3b27ef83d050dafe5772f1c4d3c7482acc2c57bdda3be4b`.
- Active packet folder label was `13 - Yao Zhou 2023`; publication metadata in the source identifies Yao et al., with Anqi Zhang as second author, first published in 2024. The pre-existing packet label was not used as bibliographic authority.

## ATOM
- Shared publication ID: `73bbf5e8-059d-5456-aacc-253a3ee134e7`.
- Total LiteratureAtoms: **166**.
- Counts by kind: {"adverse_event": 59, "author_conclusion": 2, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 2, "funding_disclosure": 1, "limitation": 5, "method": 18, "population_description": 1, "qualitative_result": 10, "quantitative_result": 56, "study_objective": 1, "subgroup_result": 9}.
- Pydantic structural validation: **PASS**.
- JSON Schema validation: **PASS** (0 errors).
- Sufficiency validation: **PASS** (0 errors; 0 warnings).
- Exact duplicate canonical statements: **0**.

## SEA / coverage
- Main-text figures reconciled: **8/8**.
- Main-text tables: **0**.
- Supplementary appendices mapped: **17/17**.
- Supplementary figure families reconciled: **58**.
- Supplementary table occurrences reconciled: **52** (51 unique labels because Table S4 is reused by the source).
- SEA HTML semantic/mechanical QA: **PASS**.

## Reference task queue
- Printed bibliography entries extracted: **46**.
- Entries remain unchecked tasks for separate primary-source acquisition/review.
- No external bibliography correction was applied.

## Preserved source-integrity issues
1. Appendix 8 title says 75 trials; the main article reports 76 RCTs in the final quantitative synthesis.
2. Table S4 is reused for both an Embase search strategy and a risk-of-bias table.
3. Results prose says all 15 GLP-1RAs significantly reduced fasting blood glucose, while Figure 5 displays 14 agents and omits ITCA 650.
4. Main Figure 7 reports lixisenatide body-weight MD -0.62 kg (95% CI -1.51 to 0.87), while Supplementary Table S8.3 reports -0.32 kg with the same CI.

## Output files
- `yao-zhang-2024-bmj-2023-076410-atoms.json`
- `yao-zhang-2024-bmj-2023-076410-validation.json`
- `yao-zhang-2024-bmj-2023-076410-coverage.json`
- `yao-zhang-2024-bmj-2023-076410-crosswalk.json`
- `yao-zhang-2024-bmj-2023-076410-sea.html`
- `yao-zhang-2024-bmj-2023-076410-sea-qa.json`
- `yao-zhang-2024-bmj-2023-076410-reference-task-queue.md`
- `yao-zhang-2024-bmj-2023-076410-processing-report.md`
