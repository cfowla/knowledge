# Processing Report — 116 - fendo-12-713700

## Lifecycle status

**PASS - ATOM/SEA VERIFIED**

Primary publication: Tara Hyder, Christopher C. Marino, Sasha Ahmad, Azadeh Nasrazadani, and Adam M. Brufsky. *Aromatase Inhibitor-Associated Musculoskeletal Syndrome: Understanding Mechanisms and Management.* Frontiers in Endocrinology. 2021;12:713700. DOI: 10.3389/fendo.2021.713700. PMID: 34385978. PMCID: PMC8353230.

## Source audit

The packet contains one usable primary source, `fendo-12-713700.pdf` (Drive ID `1xIkvfgWcRLZ4dIFNSdcTwzrgB377z4N8`), 16 pages, SHA-256 `5a822df6f1f493df149d325a92b5bf0e3d8309f83cc63fd687e71992d9114510`. No supplement or appendix file was present in the packet, and none was identified as required by the article.

All 16 PDF pages were rendered and visually inspected. The source contains one main figure, two main tables, no algorithm/workflow, and 170 numbered references. Figure 1, Table 1, and the two-page Table 2 were reconciled against the SEA and coverage manifest.

## ATOM validation

The prior Drive search did not locate an identity-matched ATOM JSON, ATOM validation JSON, or coverage JSON for this publication, so the ATOM set was regenerated from the current source.

- Atoms: **47**
- Shared publication ID: `b4f37dd2-dcd1-5412-bbbd-92496756c2ed`
- Pydantic structural validation with supplied `literature(1).py`: **PASS — 0 errors**
- JSON Schema validation with supplied `literature_atom.schema.json`: **PASS — 0 errors**
- Atom-kind sufficiency validation with supplied `literature_atoms(1).py`: **PASS — 0 errors, 0 warnings**
- Atom IDs unique: **PASS**
- Publication identity consistent: **PASS**
- Provenance/source hash matched to current PDF: **PASS**
- Exact duplicate canonical statements: **0**

The article is a narrative review. Study-level findings summarized by Hyder et al. are represented as secondary reports rather than as if the review generated primary participant data.

## SEA verification

Existing SEA: `116 - fendo-12-713700 - SEA.html` (Drive ID `1j0k5I-AY4r6q-ieWCC2ZBBDHGq71_qki`). The artifact is identity matched by title, DOI, PMID/PMCID, evaluated filename, and exact current-source SHA-256. It is parseable, its table-of-contents anchors resolve, source metadata are correct, and it represents methods/design boundary, main claims, quantitative findings, limitations/uncertainty, provenance, Figure 1, Table 1, and Table 2. No placeholder/TODO or internal chat/file citation syntax was found.

Direct semantic spot-checks passed for the review's central AIMSS conclusion, the pooled arthralgia prevalence of 46% from 21 studies/13,177 participants, fracture OR 1.47 (95% CI 1.34-1.61), the proposed AIA definition in Table 1, management evidence, and the review's uncertainty/future-directions statements.

One source-integrity issue is preserved rather than repaired: Table 2 reports no statistically significant between-group pain-score difference for SWOG S0927, while page-10 prose reports mean BPI-SF decreases of 2.22 versus 1.81 with `p<0.001`. Both statements remain visible in ATOM/SEA with the contradiction flagged.

## ATOM/SEA reconciliation

ATOM and SEA use the same publication identity and exact current-source hash. Consequential prevalence, adherence, bone-loss/fracture, arthralgia-definition, treatment, exercise/acupuncture, uncertainty, and omega-3 conflict content were checked across both outputs. No cross-artifact contradiction requiring repair was found beyond the explicitly preserved source-level omega-3 inconsistency.

## Reference processing

Existing queue: `116 - fendo-12-713700 - Reference Task Queue.md` (Drive ID `1VQzeKNdXuCPMLf6VxBjzO1U_nIyY3Gj9`). It was not accepted on existence alone. The source bibliography contains 170 numbered references; the queue contains 170 unique numbered entries and preserves complete numbering 1 through 170. Primary-packet bibliography extraction is therefore complete.

The 170 unchecked queue items are downstream cited-publication retrieval/review tasks under the existing project lifecycle convention. They are not missing bibliography extraction from this publication packet and do not block closure of this primary packet.

## Output locations

GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON:

- `116-fendo-12-713700-atoms.json` — Drive ID `1Jscl_yRNhlp28FmVdN3zbbdGTHUY9YIL`
- `116-fendo-12-713700-validation.json` — Drive ID `1D_32jCHDbd4tbviuApTGkquGCHyBbdcf`
- `116-fendo-12-713700-coverage.json` — Drive ID `1FPsQaJ5MaS8JVrwjWrOYtDQpwD-LDh8I`

GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML:

- `116 - fendo-12-713700 - SEA.html` — Drive ID `1j0k5I-AY4r6q-ieWCC2ZBBDHGq71_qki`

GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD:

- `116 - fendo-12-713700 - Reference Task Queue.md` — Drive ID `1VQzeKNdXuCPMLf6VxBjzO1U_nIyY3Gj9`
- `116-fendo-12-713700-processing-report.md` — Drive ID `15rfE02cSRUV7MD1mH9lmlTn6e2flWE1d`

## Governing sources

ATOM structural validation used the supplied `literature(1).py`; JSON serialization validation used `literature_atom.schema.json`; atom-kind sufficiency used `literature_atoms(1).py`. `README(2).md` supplied workflow intent and `example_atom(1).json` was treated as illustrative only. SEA verification used `summary-evaluation-appraisal-protocol-v4-compact.md` as governing protocol, with `large-source-ATOM-SEA.md` as supporting coverage guidance and the v3 HTML as historical reference only.

The user's prose preference references `unslop.skill.md`, but no actual `unslop.skill.md` source file was retrievable from the available project/Drive sources; no requirements were invented from prior reports that merely mentioned it.

No external web verification was used for this packet audit.

## Lifecycle action

Status remains **PASS - ATOM/SEA VERIFIED**. The packet folder `116 - fendo-12-713700` (Drive ID `1btJEU1SDysZP2I8zkU7yH0JsHNK1kmKB`) was moved from Active Clinical Medicine & Pharmacy parent `1wA_mmV9fJvfM7ILPwPuc-Uac1SJ1hpk0` to `5 - 90 - Processed / 1 - Clinical Medicine & Pharmacy` parent `1aZFVGPyvpaeYQwXYag26y9msPjwj0-lT`. Post-move metadata readback confirmed the new parent and preserved the folder name and Drive ID.

**Exact remaining task:** none for this publication packet. The 170 unchecked reference-queue items remain downstream cited-publication tasks outside this closed primary packet.
