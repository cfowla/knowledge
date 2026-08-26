# Processing report - 8 - 08-1632_finalL

Status: `PASS - ATOM/SEA VERIFIED`

## Source and packet boundary

The packet contains one usable primary source, `08-1632_finalL.pdf`, Google Drive file ID `1sJuP28fJVx1jyblMMpj1X5R220lXZzrm`. No supplements are present.

The target publication is:

- Title: *Methicillin-Resistant Staphylococcus aureus USA400 Clone, Italy*
- Authors: Carla Vignaroli, Pietro E. Varaldo, Alessandro Camporese
- Journal: *Emerging Infectious Diseases*
- Year: 2009
- Volume/issue/pages: 15(6):995-996
- DOI: `10.3201/eid1506.081632`
- Source SHA-256: `9401cf126d1ce779f8d836ae388356ce9d9d6da072a590dd2782b3039edc2030`

The two-page PDF contains the target letter on journal page 995, with references 4 through 10 continuing at the top of page 996. A separate letter, *Meningitis and Radiculomyelitis Caused by Angiostrongylus cantonensis*, begins later on page 996. That adjacent publication was excluded from ATOM, SEA, coverage, and reference processing.

## Artifact audit and repair

The existing SEA and reference queue were identity-matched by title, DOI, source metadata, content, and source hash. Before repair, no identity-matched ATOM JSON, authoritative ATOM validation JSON, or coverage JSON was found in the Clinical Medicine & Pharmacy JSON output folder.

The missing ATOM-side outputs were regenerated from the current primary source and written to `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`:

- `8 - 08-1632_finalL - atoms.json`, Drive ID `1cayNIrZx6wo035h9AC1da9oCZ4DBkaoH`
- `8 - 08-1632_finalL - validation.json`, Drive ID `10QCQHtiRD3c0lQpVr19z6U3qKY96-Bzq`
- `8 - 08-1632_finalL - coverage.json`, Drive ID `1R9mWbzbiOJsW22aajCC3LvXTPUUpMdvU`

Existing verified outputs:

- `8 - 08-1632_finalL - SEA.html`, Drive ID `1_WGG9oYLkJI-AKLGFMF0VbUAZp9Rpxpm`, in the Clinical Medicine & Pharmacy HTML output folder
- `8 - 08-1632_finalL - References Task Queue.md`, Drive ID `1yU2HrLUYkV0X5UaJb9wg2jodGW2y-ge4`, in the Clinical Medicine & Pharmacy MD output folder

No duplicate identity-matched outputs were found that required removal.

## ATOM validation

ATOM validation ran in the required order against the supplied governing files:

1. `literature.py` Pydantic structural validation: PASS
2. `literature_atom.schema.json` Draft 2020-12 JSON Schema validation: PASS
3. `literature_atoms.py` atom-kind sufficiency validation: PASS

Validation results:

- Atom count: 13
- Structural errors: 0
- JSON Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Shared publication ID: `413e71c3-5bc4-56c9-ae91-06320fe55e5a`
- Unique atom IDs: PASS
- Exact duplicate statement and anchor pairs: 0
- Source hash preserved in provenance: PASS

Semantic spot checks passed for the publication purpose, treatment doses and durations, molecular characterization, and clinical follow-up. The atoms preserve USA400/ST1, SCCmec IVa, PVL positivity, agr III, spa t128, amoxicillin/clavulanate 1 g three times daily for 10 days, levofloxacin 500 mg once daily for 7 days, complete resolution, and no recurrence for more than one year. The treatment observation was not converted into comparative treatment-effect evidence.

All model-extracted atoms remain `needs_review` because no independent human reviewer step is represented. This is a provenance state, not a structural or sufficiency validation failure.

## SEA verification

The existing SEA is parseable, self-contained, and identity-matched to the current source and source SHA-256. It includes the source metadata, case-report design, principal epidemiologic claim, treatment details, molecular findings, limitations, uncertainty, and provenance.

Coverage reconciliation:

- PDF pages inspected: 2/2
- Main figures: 0/0
- Main tables: 0/0
- Algorithms/workflows: 0/0
- Supplements: 0/0
- Adjacent unrelated letter: explicitly excluded
- Internal chat or file citation syntax: absent
- Placeholder/TODO scan: PASS
- Table-of-contents anchors: PASS

Direct semantic checks confirmed the primary importation conclusion, the numerical medication regimens, the single-case limitation, and the absence of a figure/table-derived claim because the target publication contains no figures or tables.

## ATOM and SEA reconciliation

ATOM and SEA use the same title, DOI, source file, publication boundary, and SHA-256. Both preserve the case as a single-patient report and distinguish the observed levofloxacin response from evidence of treatment efficacy. Both exclude the unrelated letter that begins on page 996. No consequential contradiction or source-integrity mismatch remains.

## Reference processing

The reference queue was checked against the primary article instead of being accepted on file presence alone. It contains all 10 target-publication references in source order, preserves the printed identifiers where available, and excludes references belonging to the adjacent page-996 letter.

Reference reconciliation result: 10/10 PASS.

The unchecked queue boxes are downstream tasks for processing the cited publications themselves. They do not represent missing bibliography extraction or an incomplete reference queue for this packet.

## Warnings and limitations

- The PDF includes the beginning of an unrelated publication on page 996, which required an explicit source boundary.
- The paper is a 2009 single-patient letter. Its treatment outcome cannot establish comparative efficacy, prevalence, or transmission frequency.
- Model-extracted atoms remain `needs_review` pending any future independent human review step.

None of these items blocks packet closure.

## Lifecycle action

The packet folder `8 - 08-1632_finalL` was moved from `2 - 10 - Active Literature / 1 - Clinical Medicine & Pharmacy` to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy`. The folder name was preserved.

Exact remaining packet-repair task: none.

Generated 2026-08-25.
