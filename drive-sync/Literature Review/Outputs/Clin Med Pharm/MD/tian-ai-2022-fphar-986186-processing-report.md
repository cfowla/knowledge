# Processing Report — Tian et al. 2022

## Source
- Title: Cardiovascular and renal outcomes with sodium glucose co-transporter 2 inhibitors in patients with type 2 diabetes mellitus: A system review and network meta-analysis
- DOI: 10.3389/fphar.2022.986186
- PMID: 36506550
- PMCID: PMC9731650
- Main file SHA-256: `4c1c4cb713b72ce0654486a2d7fb057b7741a3c4e8e396d4130e5c312bf77564`
- Supplement SHA-256: `1b24466e923305d8a63985d155ade6d4d54bed3d2cf7eb6b8801955cf3f2cbad`

## ATOM
- Publication ID: `aef1f680-eb8a-5e17-99c8-78324b03ed87`
- LiteratureAtoms: 80
- Structural validation: PASS (0 errors)
- JSON Schema validation: PASS (0 errors)
- Sufficiency validation: PASS (0 errors, 0 warnings)
- Exact duplicate canonical statements: 0
- Counts by kind: {"author_conclusion": 3, "conflict_of_interest": 1, "data_availability": 1, "eligibility_criterion": 4, "funding_disclosure": 1, "limitation": 3, "method": 7, "other": 6, "outcome_definition": 2, "population_description": 12, "qualitative_result": 5, "quantitative_result": 34, "study_objective": 1}

## SEA
- Source map/coverage manifest: complete
- Main figures reconciled: 5/5
- Supplement tables reconciled: 2/2
- SEA HTML semantic/mechanical QA: FAIL
- Verdict: Skim deeply; useful as an evidence map, not as sole support for agent-level formulary superiority.

## Reference task queue
- References extracted: 51
- Output: `tian-ai-2022-fphar-986186-references.md`

## Source consistency findings preserved
1. Abstract n=68,723 vs Results n=67,823.
2. Renal-composite definition differs between Methods and Abstract/Results.
3. Renal HRs for ertugliflozin and sotagliflozin conflict between Results prose and Abstract/Supplement Table 2.
4. DAPA-HF diabetes-status description conflicts between main Results and Supplement Table 1.
5. Figure captions use “credible intervals” despite the stated frequentist method/confidence-interval terminology.

## Extraction boundaries
- This is a secondary-source network meta-analysis. Trial-level results are represented as reported by Tian et al.; primary trial publications were not re-atomized in this run.
- Bibliography entries were not atomized; they were converted to the reference task queue.
- Safety was not developed as a substantive outcome set in the supplied review.

## Protocol/version note
The governing project source filename is `summary-evaluation-appraisal-protocol-v4-compact.md`, but its internal title identifies itself as “Integrated Compact v3.” Per project precedence, the file designated as the v4 governing source was followed; the internal version-label mismatch is preserved here rather than silently reconciled.
