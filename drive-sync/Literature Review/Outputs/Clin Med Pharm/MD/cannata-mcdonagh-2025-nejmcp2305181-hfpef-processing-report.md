# Cannata and McDonagh 2025 HFpEF processing report

## Scope

Activated macros: `@ATOM` + `@SEA`.

Source packet: `NEJMcp2305181.pdf` plus `nejmcp2305181_appendix.pdf` from `3/2/1/19`, resolved to `19 - Cannata McDonagh 2025`.

The publication is a New England Journal of Medicine Clinical Practice narrative review. It is not a primary trial or systematic review. Trial effects and guideline statements therefore remain secondary reports anchored to this review.

## ATOM

- LiteratureAtoms: **121**
- Semantic batches: **9**
- Atom kinds: `{"study_objective": 1, "method": 1, "other": 95, "author_conclusion": 14, "limitation": 9, "conflict_of_interest": 1}`
- Pydantic structural validation: **PASS**
- Supplied JSON Schema validation: **PASS**
- Supplied sufficiency validation: **PASS**
- Structural errors: **0**
- Schema errors: **0**
- Sufficiency errors: **0**
- Sufficiency warnings: **0**
- Unique atom IDs: **PASS**
- Shared publication ID: **PASS**

The current LiteratureAtom model has no dedicated secondary-trial-report or narrative-review-recommendation kind. Trial summaries are represented mainly as `other` with `secondary_reported_result` tags. Author treatment language is represented as `author_conclusion`. No cited trial was represented as if this review enrolled its participants.

## SEA and coverage

All 12 main article pages and all 3 supplementary pages were inspected. Figure 1, Figure 2, the two-page Table 1, and Supplementary Table S1 were reconciled. Supplementary Table S1 contains **36** trial rows and each row has an anchored atom. The bibliography was excluded from ATOM extraction and exported separately.

SEA verdict: **Read first** as a practical HFpEF synthesis. It should not serve as the sole 2026 practice authority because an updated ACC HFpEF Expert Consensus Decision Pathway was published in July 2026.

## Source-integrity findings

1. The PDF prints the PARAGLIDE-HF NT-proBNP geometric mean ratio as 0.85 with 95% CI 0.73 to 0.10. The interval is internally impossible. No correction was guessed.
2. The selected PDF says the article was updated June 9, 2026. The official NEJM page retrieved August 23, 2026 says updated July 9, 2026. The source PDF remains unchanged and the version difference is reported separately as external verification.
3. Printed reference 8 calls the National Heart Failure Audit a 2022 summary report but prints the date June 16, 2002. The reference queue preserves the printed citation.
4. Several major treatment trials summarized in the review enrolled LVEF greater than 40 or 45 percent, not only strict contemporary HFpEF at LVEF at least 50 percent. The SEA keeps this evidence boundary explicit.

## Reference task queue

- Printed references extracted: **61**
- P0 direct diagnostic, guideline, or pivotal-treatment candidates: **24**
- P1 important supporting candidates: **29**
- P2 background or contextual candidates: **8**
- Bibliography atomized: **No**
- External bibliographic correction: **No**. The source order and printed wording were preserved.

## Governing sources applied

ATOM precedence:
1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json`

SEA governing protocol: `summary-evaluation-appraisal-protocol-v4-compact.md`.

Large-source workflow: `large-source-ATOM-SEA.md`.

Writing control: `unslop.skill.md`.

The named Pydantic model, sufficiency validator, and JSON Schema were executed directly. SEA scoring followed the supplied v4 protocol. The v3 HTML was historical reference only.

## External currency verification

The official NEJM page and the July 23, 2026 ACC HFpEF Expert Consensus Decision Pathway summary were checked because SEA v4 requires recency verification for clinical-practice material. This verification is separated from source-derived findings in the SEA artifact.

## Output files

### JSON

- `cannata-mcdonagh-2025-nejmcp2305181-hfpef-atoms.json`
- `cannata-mcdonagh-2025-nejmcp2305181-hfpef-validation.json`
- `cannata-mcdonagh-2025-nejmcp2305181-hfpef-coverage.json`
- `cannata-mcdonagh-2025-nejmcp2305181-hfpef-crosswalk.json`
- `cannata-mcdonagh-2025-nejmcp2305181-hfpef-sea-qa.json`

### HTML

- `cannata-mcdonagh-2025-nejmcp2305181-hfpef-sea.html`

### Markdown

- `cannata-mcdonagh-2025-nejmcp2305181-hfpef-reference-task-queue.md`
- `cannata-mcdonagh-2025-nejmcp2305181-hfpef-processing-report.md`
