# 141 ACC 2026 HFpEF ECDP summary processing report

## Activated macros

- `@ATOM`
- `@SEA`

## Source packet

- Drive folder: `141 - American College of Cardiology 2026 - HFpEF ECDP Summary`
- Primary supplied file: `Updated ACC Expert Consensus Decision Pathway Addresses Management of HFpEF - American College of Cardiology.pdf`
- Source type: ACC journal-scan/news summary of the 2026 HFpEF Expert Consensus Decision Pathway
- PDF pages: 3
- Source SHA-256: `87555beddbd4ea3822080d741c991438e4230c19af09a4e2f49d064833fea2b9`
- Shared LiteratureAtom publication ID: `bfdd30cc-7ceb-5a54-b8f6-64be64bcbbc0`
- Underlying ECDP citation: Kittleson M, Panjrath G, Bates K, et al. *Management of Heart Failure With Preserved Ejection Fraction: 2026 ACC Expert Consensus Decision Pathway.* JACC. DOI `10.1016/j.jacc.2026.06.018`.

The supplied source is the ACC summary page, not the full JACC ECDP. The extraction and appraisal therefore describe what the summary reports. They do not claim that the three-page summary contains the full evidence review or treatment details.

## ATOM status

- LiteratureAtoms: **14**
- Atom kinds: `{'author_conclusion': 3, 'limitation': 1, 'other': 10}`
- Semantic batches: `{'hfpef-summary-diagnosis-v1': 3, 'hfpef-summary-evidence-v1': 2, 'hfpef-summary-framing-v1': 2, 'hfpef-summary-limitations-v1': 2, 'hfpef-summary-management-v1': 5}`
- Pydantic structural validation: **PASS**
- JSON Schema validation: **PASS**
- Sufficiency validation: **PASS**
- Structural errors: 0
- Schema errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0
- Exact duplicate statement-anchor pairs: 0

The current LiteratureAtom schema has no dedicated `guideline_recommendation` kind. Recommendation-like statements from this secondary ACC summary use `atom_kind="other"` with descriptive tags. No underlying trial was represented as if the ACC webpage enrolled participants or generated trial results.

## SEA and coverage

- PDF pages rendered and visually inspected: **3/3**
- Substantive workflow visuals reconciled: **1/1**
- Tables: **0/0**
- Appendices or supplements: none supplied
- Formal references listed by the summary: **1**
- SEA verdict: **Skim deeply**

The summary is useful for orientation but lacks trial-level estimates, evidence grades, diagnostic cutoffs, drug dosing, sequencing, contraindications, and monitoring details. The full JACC ECDP is the next source to process before practice or CDS implementation.

## Governing sources

ATOM precedence was applied as specified: `literature(1).py` -> `literature_atoms(1).py` -> `literature_atom.schema.json` -> `README(2).md` -> `example_atom(1).json`. SEA used `summary-evaluation-appraisal-protocol-v4-compact.md` as authoritative. `large-source-ATOM-SEA.md` and `unslop.skill.md` were applied as supporting workflow and prose controls.

No external verification was performed because `@VERIFY` was not activated.

## Generated files

### JSON

- `141-acc-2026-hfpef-ecdp-summary-atoms.json`
- `141-acc-2026-hfpef-ecdp-summary-validation.json`
- `141-acc-2026-hfpef-ecdp-summary-coverage.json`
- `141-acc-2026-hfpef-ecdp-summary-crosswalk.json`

### HTML

- `141-acc-2026-hfpef-ecdp-summary-sea.html`

### Markdown

- `141-acc-2026-hfpef-ecdp-summary-references-task-queue.md`
- `141-acc-2026-hfpef-ecdp-summary-processing-report.md`
