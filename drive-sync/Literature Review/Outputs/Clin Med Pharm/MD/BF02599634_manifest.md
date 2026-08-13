# BF02599634.pdf — ATOM + SEA Processing Manifest

## Source identity

- **Title:** *Intravenous Heparin Dosing: Patterns and Variations in Internists' Practices*
- **Authors:** Brendan M. Reilly, Robert Raschke, Sandhya Srinivas, Theresa Nieman
- **Source:** *Journal of General Internal Medicine*. 1993;8:536-542.
- **Source type:** Cross-sectional physician practice survey
- **Retrieved file:** `BF02599634.pdf`
- **Drive source folder:** `TBR/Lit Cluster: Heparin Deep Dive`
- **Raw file size:** 700,581 bytes
- **SHA-256:** `b52d8c197006144392d51274f88ae7401a932bbae5d6c5440f47f8a5ba112d76`
- **PDF pages:** 7

## Activated workflows

- `@ATOM`
- `@SEA`

No external verification macro was activated. Extraction and appraisal were grounded in the retrieved PDF plus the governing project source files.

## ATOM output

- **Total atoms:** 49
- **Structural validation:** PASS (Pydantic)
- **JSON-Schema validation:** PASS; 49/49 atoms validate against `literature_atom.schema.json`
- **Sufficiency validation:** PASS; 0 errors, 0 warnings
- **Review status:** `needs_review` (language-model extraction; no human reviewer asserted)

### Atom counts by kind

| Atom kind | Count |
|---|---:|
| study_objective | 1 |
| method | 7 |
| population_description | 1 |
| quantitative_result | 24 |
| subgroup_result | 7 |
| author_conclusion | 4 |
| limitation | 5 |

### Extraction boundaries

The paper's own survey findings were atomized. Quantitative findings from secondary studies cited in the Discussion were **not** re-labeled as primary-study results. Calculated between-group differences derived directly from Table 2 were marked `calculated_from_reported_data`; source-reported values remained attached as arm observations.

## SEA coverage manifest

- **Sections:** structured abstract; background/introduction; Methods; Results; Discussion; References
- **Tables:** 2
  - Table 1 — Dose changes in response to APTT levels, p. 538 — structured reconstruction
  - Table 2 — Therapeutic ranges and associated dosing decisions, p. 539 — structured reconstruction
- **Figures:** 1
  - Figure 1 — Published descriptions of heparin management, p. 540 — embedded crop in self-contained HTML
- **Algorithms/workflows:** no formal algorithm; Figure 1 compares dosing schemas
- **Appendices/supplements:** none in retrieved PDF
- **Omissions:** bibliography not condensed; unrelated American Board of Internal Medicine announcement on the final PDF page omitted

## SEA appraisal status

- **HTML generation:** PASS
- **Required anchors:** PASS
- **Main-text figure/table reconciliation:** PASS (1 figure, 2 tables)
- **Internal tool/file citation syntax in HTML:** none
- **TODO/placeholders/planning language:** none detected
- **Primary verdict:** **Skim deeply** — high historical value for heparin protocolization and APTT-target variability, but not a basis for contemporary dosing recommendations.

## Output files

- `BF02599634_atoms.json`
- `BF02599634_atom_validation.json`
- `BF02599634_sea.html`
- `BF02599634_manifest.md`

## Limitations

- The retrieved paper is a 1993 physician survey, not a patient-outcomes trial.
- The source does not report a stable identifier such as DOI in the retrieved PDF; none was added from outside sources.
- Current heparin dosing or monitoring guidance was not externally verified in this run.
