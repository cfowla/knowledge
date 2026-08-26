# Processing Report — 44 - S1936879820320124

## Lifecycle status

**PASS - ATOM/SEA VERIFIED**

Source identity: *Indigo Aspiration System for Treatment of Pulmonary Embolism: Results of the EXTRACT-PE Trial*. JACC: Cardiovascular Interventions. 2021;14(3):319-329. DOI `10.1016/j.jcin.2020.09.053`. Trial `NCT03218566`.

## Source audit

- Primary PDF: `1-s2.0-S1936879820320124-main.pdf`, 11 pages, SHA-256 `b176f90f60836d2be78edf447d3fb6647fffc2a2904ea6e57eda5bee0ba95e60`.
- Material supplement: `1-s2.0-S1936879820320124-mmc1.docx`, 9 rendered pages, SHA-256 `50378b0a16de0a0056493bd5f18ec0a50847305c97355af57dfdaf0fdc49365b`.
- The primary source is readable and identity-consistent with the supplement and retained outputs.
- The full 11-page primary PDF and 9 rendered supplement pages were inspected. Main-text Figures 1-4, Tables 1-6, the Central Illustration, and the methodologically material supplement were reconciled.

## Artifact audit and repair

| Artifact | Drive location | Result |
|---|---|---|
| ATOM JSON | `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON / 44-S1936879820320124-EXTRACT-PE-atoms.json` — `https://drive.google.com/file/d/1xZpv-Pu8Vdg7ydmqV9IWIwLdRQ4QfUIM/view` | Regenerated from the current primary article plus material supplement; 39 atoms; one shared publication ID; unique atom IDs; current source hashes preserved. |
| ATOM validation JSON | `... / JSON / 44-S1936879820320124-EXTRACT-PE-validation.json` — `https://drive.google.com/file/d/1DiteZozAjHJ1X1PC0PK0p0Xd0f1Slyj7/view` | PASS. Zero blocking errors and zero sufficiency warnings. |
| Coverage JSON | `... / JSON / 44-S1936879820320124-EXTRACT-PE-coverage.json` — `https://drive.google.com/file/d/1bKYnBHv66kgG-eW_k6pntzJINr5rUMaR/view` | PASS. All load-bearing main-text visuals and material supplement content represented; administrative supplement addresses/PI listing explicitly omitted as non-load-bearing. |
| SEA HTML | `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML / 44-S1936879820320124-EXTRACT-PE-SEA.html` — `https://drive.google.com/file/d/1kaM2un82jxRbB8A-MFtPy-I5s2NxxP8i/view` | Existing identity-matched artifact independently revalidated against the current source and source hashes; no source-mismatch repair required. Mechanical and semantic QA pass. |
| Reference task queue | `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD / 44-S1936879820320124-EXTRACT-PE-reference-task-queue.md` — `https://drive.google.com/file/d/178Ka51sGuAAr-YAkSKQ9C1DFLYGoKBjO/view` | PASS after content verification: 22 source references and 22 contiguous queue entries (1-22); title/DOI/source ID match; representative citations spot-checked. |
| Processing report | `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD / 44-S1936879820320124-EXTRACT-PE-processing-report.md` | This report. |

## Authoritative ATOM validation

Validation was executed using the governing project contracts supplied for this task, in the required order:

1. `literature.py` Pydantic structural validation: **39/39 PASS**.
2. `literature_atom.schema.json` JSON Schema validation: **39/39 PASS**.
3. `literature_atoms.py` atom-kind sufficiency validation: **39/39 PASS**.

Blocking errors: **0**. Sufficiency warnings: **0**. Merge integrity: one publication UUID (`8dd06ab1-3510-5ed4-b1e4-d883cfd8ab0a`), 39 unique atom IDs, no exact duplicate canonical statements, source-specific provenance, and current primary/supplement hashes.

Direct ATOM semantic spot-checks passed for:
- Primary efficacy: RV/LV ratio mean reduction `0.43` (95% CI `0.38-0.47`; `p<0.0001`) from Table 3/Figure 3.
- Primary safety: 48-hour major adverse event rate `1.7%` (`2/119`; 95% CI `0.0-4.0`) from Table 4.
- Figure/table-derived procedural claim: median device time `37.0` min (IQR `23.5-60.0`) and technical access `99.2%` from Table 2.
- Limitation: lack of randomization/comparator, 30-day follow-up, and surrogate primary efficacy endpoint.
- Supplement-derived analysis rule: mITT excludes adjunctive clot-reduction treatment/thrombolytics through 48 hours.

Atom `review_status` remains `needs_review`; human verification status was not fabricated. This does not create a structural or sufficiency validation failure.

## SEA validation

- HTML parses successfully; IDs are unique and all table-of-contents anchors resolve.
- Exact title, DOI, trial registration, design, population, intervention, endpoints, methods, principal findings, limitations/uncertainty, funding/COI context, provenance, and practice-translation boundaries are present.
- All six appraisal dimensions are present, and each contains a rationale, evidence basis, principal limiting factor, and raise/lower condition.
- Figures 1-4, Tables 1-6, the Central Illustration, and the material supplement are represented as structured evidence blocks.
- Direct semantic checks passed for the primary result/conclusion, the primary numerical efficacy result, a limitation/uncertainty claim, Table 2 procedural data, Table 4 safety data, and the supplement's mITT definition.
- No internal chat/file citation syntax, TODOs, placeholders, stale source identity, or planning language remains.

## ATOM ↔ SEA reconciliation

ATOM and SEA resolve to the same title, DOI, trial, primary PDF hash, and supplement hash. Trial design, eligibility boundaries, intervention/device details, primary efficacy and safety results, procedural characteristics, limitations, funding/COI context, and the material supplement are handled consistently. No consequential contradiction or source-integrity mismatch remains.

## Reference-processing verification

The primary article contains 22 numbered references. The queue contains exactly 22 contiguous numbered entries, 1 through 22, under the correct article title, DOI, and source ID. References 1, 6, 14, 19, and 22 were spot-checked against the source list. The unchecked boxes represent downstream acquisition/review tasks and do not indicate missing reference extraction from this publication packet.

## Warnings

- EXTRACT-PE is a prospective single-arm device trial without a randomized comparator.
- The primary efficacy endpoint is the surrogate RV/LV ratio; follow-up is limited to 30 days, and the study was not designed or powered for long-term patient-centered outcomes.
- Generalization to higher-risk pulmonary embolism is limited by the enrolled population and exclusion criteria.
- The trial was funded by Penumbra, with disclosed investigator relationships to Penumbra.
- This audit validates the 2021 source and packet artifacts; it does not independently establish current 2026 pulmonary-embolism treatment guidance.

## Lifecycle action

All packet-specific requirements pass. The packet was moved, preserving the folder name, from `2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy` to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`. Drive readback confirmed the packet folder parent is the Processed clinical-medicine folder (`1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`) and it is no longer a child of the Active clinical-medicine folder (`1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0`).

**Exact remaining task:** none for this publication packet.
