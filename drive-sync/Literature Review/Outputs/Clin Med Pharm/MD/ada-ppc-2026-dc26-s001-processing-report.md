# Processing report: 1. Improving Care and Promoting Health in Populations: Standards of Care in Diabetes—2026

Source packet: `1 - American Diabetes Association 2026`  
Input: `dc26s001.pdf`  
DOI: `10.2337/dc26-S001`  
SHA-256: `785b8263debfe064e5a735381afdecdf0e4277c8f1c3b9b17a7b8da5e5004214`

## ATOM

- LiteratureAtoms: 65
- Shared publication ID: `951b9ffb-cfb5-5bb5-a06a-65ce3d1ec1f0`
- Atom counts by kind: `{"author_conclusion": 11, "limitation": 3, "other": 31, "quantitative_result": 20}`
- Semantic extraction runs: `{"ada-ppc-2026-dc26-s001-frontmatter-v1": 2, "ada-ppc-2026-dc26-s001-social-context-v1": 10, "ada-ppc-2026-dc26-s001-systems-table-v1": 9, "ada-ppc-2026-dc26-s001-systems-v1": 44}`
- Pydantic structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Duplicate canonical statements: 0
- Duplicate statement-anchor pairs: 0

Guideline boundary: recommendations are represented as panel/guideline statements (`author_conclusion` plus `guideline_recommendation` tags). Quantitative effects reported from trials, systematic reviews, surveillance sources, and programs are tagged `secondary_reported_result`; the chapter is not represented as if it enrolled those populations.

## SEA

- Source type: clinical practice guideline / standards chapter
- Substantive coverage: S13–S22
- Figures reconciled: 0/0
- Tables reconciled: 1/1 (Table 1.1)
- Algorithms/workflows reconciled: 0/0
- External methodology document: not supplied; limitation preserved
- Verdict: `Read soon`
- SEA QA: PASS

## Reference queue

- Bibliography entries extracted: 171
- P0 direct support for central quantitative/population claims: 17
- P1 high-value implementation/access/SDOH/telehealth evidence: 96
- P2 contextual/background evidence: 58

## Extraction limitations / schema gaps

- The LiteratureAtom schema has no dedicated `guideline_recommendation` atom kind, so recommendations use `author_conclusion` with descriptive tags as permitted by the large-source workflow.
- The ADA evidence-grade definitions and full guideline-development method are delegated to the separate Introduction and Methodology and were not supplied in this input.
- Bibliography entries were not atomized; they were preserved as a reference task queue.
- No external verification was performed; this workflow is grounded in the supplied source and project protocols.

## Protocol/version note

The project designates `summary-evaluation-appraisal-protocol-v4-compact.md` as the governing SEA source. The supplied file's internal heading still says Integrated Compact v3. The workflow followed the v4-named file as authoritative and recorded the mismatch rather than silently changing it.

## Drive lifecycle

- ATOM/validation/coverage/crosswalk/SEA-QA JSON files saved to `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`.
- SEA HTML saved to `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`.
- Reference task queue and processing report saved to `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`.
- `dc26s001.pdf` moved from `10 - Active Literature / 1 - American Diabetes Association 2026` to `90 - Processed / Clinical Medicine & Pharmacy / 47 - American Diabetes Association 2026`.
- The active ADA folder retains 15 unprocessed section PDFs.
- `TBR - Current Task Queue` updated to record this completion and reconcile current Active/Processed counts.
