# ATOM + SEA processing report — Cipolle et al. 1981

## Source metadata

- **Exact title:** Heparin kinetics: Variables related to disposition and dosage
- **Authors:** Robert J. Cipolle, Randall D. Seifert, Barbara A. Neilan, Darwin E. Zaske, Erhardt Haus
- **Journal:** Clinical Pharmacology & Therapeutics
- **Citation:** 1981;29(3):387–393
- **DOI:** 10.1038/clpt.1981.53
- **Source file:** `Clin Pharma and Therapeutics - March 1981 - Cipolle - Heparin kinetics Variables related to disposition and dosage.pdf`
- **Google Drive file ID:** `1_Ip4tvWQZOFNG7BcxzgERvsf9WVusRii`
- **Raw PDF size:** 459,971 bytes
- **PDF SHA-256:** `fcae4594fde34d60dfb1e5851dd0cf33103afeebf9efecc16170e03837e9fb38`
- **LiteratureAtom publication_id:** `6e283093-0f5d-54f5-8217-10293f8eb319`
- **Source type:** Original clinical pharmacokinetic/pharmacodynamic modeling study
- **Design classification:** Prospective clinical PK/PD modeling workflow is inferred from the sequential study procedures; the article does not use a modern formal design label.

## Coverage manifest

- **PDF pages:** 7
- **Substantive article pages:** 387–392
- **References:** p. 393; bibliography not atomized except where needed for provenance/context
- **Sections:** unlabelled abstract/summary, introduction, methods, results, discussion, references
- **Figures:** 2
  - Figure 1 — in vitro heparin sensitivity
  - Figure 2 — measured-minus-fitted concentration residuals for the one-compartment model
- **Tables:** 1 semantic table spanning pp. 390–391
  - Table I — heparin kinetics by all patients, sex, smoking, and disease subgroup
- **Algorithms/workflows:** no formal algorithm diagram; the individualized sensitivity → bolus → kinetic estimation → maintenance-dose workflow is described in Methods
- **Appendices/supplements:** none in the retrieved PDF
- **Visual strategy:** both figures and Table I were visually inspected from rendered PDF pages. SEA represents them as structured blocks/tables rather than embedded screenshots.
- **Omissions:** bibliography entries were not summarized as evidence; secondary-study results cited in the Discussion were not extracted as primary-study atoms.

## ATOM extraction

- **Atoms extracted:** 54
- **Assertion origin:** predominantly `normalized_from_source`; the printed elimination-rate equation is preserved as `directly_reported`. No calculated or extractor-inference atoms were created.
- **Review status:** all atoms are `needs_review` because extraction was performed by a language model.

### Atom counts by type

- `adverse_event`: 2
- `author_conclusion`: 2
- `funding_disclosure`: 1
- `method`: 11
- `population_description`: 4
- `qualitative_result`: 7
- `quantitative_result`: 22
- `study_objective`: 1
- `subgroup_result`: 4

## Validation report

- **Pydantic structural validation:** PASS — every atom was instantiated with the authoritative `LiteratureAtom` model from `literature.py`.
- **JSON Schema validation:** PASS — 54/54 serialized atoms conform to `literature_atom.schema.json`.
- **Sufficiency validation:** PASS — 0 errors, 0 warnings under `literature_atoms.py`.
- **Structural/schema errors:** none.
- **Sufficiency errors:** none.
- **Sufficiency warnings:** none.

## Extraction limitations and schema gaps

- The PDF text layer contains minor extraction artifacts; rendered pages were used to verify the title page, both figures, Table I, equations, and page-spanning table continuation.
- Table I continues its **Disease** columns onto p. 391; it was treated as one semantic table rather than two tables.
- The Results text says hematocrit correlated **inversely** with baseline APTT but prints `r = 0.43`; the atom preserves both the stated direction and the printed coefficient and tags this as `reported_sign_ambiguity` rather than silently changing the sign.
- The current atom schema has no dedicated fields for standard deviation or a set of multiple-regression coefficients. SDs are preserved in canonical statements/original result text, and the printed elimination-rate equation is retained as a method atom.
- Observed ranges are represented using `IntervalType.RANGE`; where a `QuantitativeResult.estimate` is mandatory, a source-reported mean (or, for Figure 1, the reported minimum) is used without inventing a midpoint.
- The article reports the predictor set and R² for the dosage model but does not print a dosage regression equation; none was fabricated.
- No explicit conflict-of-interest or data-availability statement was identified in the article; absence was not converted into a reported atom.
- Discussion statements describing results from cited external studies were not atomized as if this paper generated those data.

## SEA QA status

- **Coverage manifest before narrative:** PASS
- **Main-text figures reconciled:** 2/2
- **Main-text tables reconciled:** 1/1 semantic table
- **Section condensation completed:** PASS
- **Appraisal assigned after extraction/reconciliation:** PASS
- **Clinical/practice currency check:** PASS — limited external verification against a current U.S. heparin sodium label is clearly separated from source-derived findings in the HTML.
- **HTML self-contained:** PASS — embedded CSS; no remote images/scripts/fonts
- **Internal chat/file citation syntax in HTML:** none
- **Placeholders/TODO/planning language:** none

## Output files

- JSON: `cipolle_1981_heparin_kinetics.atoms.json`
- HTML: `cipolle_1981_heparin_kinetics.sea.html`
- Markdown: `cipolle_1981_heparin_kinetics.report.md`
