# Hochsmann Schafhausen 2026 processing report

## Source

*Eltrombopag plus cyclosporine A for moderate aplastic anemia (EMAA): a placebo-controlled, double-blind, phase 3 trial*

PMID 42611779. DOI 10.1182/blood.2025032682. Published online in *Blood* in August 2026. Trial registration NCT02773225.

## Result

Processing is **blocked**, not complete.

The source packet contains only the earlier acquisition log. A current identity recheck resolved the DOI and the exact publisher PDF endpoint, but the article payload still could not be retrieved through the available lawful web/PDF path.

The project ATOM contract requires source-anchored assertions from the primary publication, followed by structural and atom-kind sufficiency validation. The SEA protocol requires source mapping and reconciliation of sections, figures, tables, and workflows before scoring and final HTML generation. Neither whole-source gate can be passed from an acquisition log plus indexed abstract text.

## ATOM status

Validated LiteratureAtoms generated: **0**

Structural validation: not run.

Sufficiency validation: not run.

JSON Schema validation: not run.

The EHA conference abstract was not substituted for the requested *Blood* publication. Indexed abstract text was not treated as a complete replacement for the article body.

## SEA status

SEA appraisal: **not run**

SEA HTML: **not generated**

SEA scoring and QA: **not run**

This avoids presenting an abstract expansion as a whole-source appraisal.

## Reference task queue

References extracted: **0**

The source bibliography was unavailable. A blocked reference task queue was created instead of inferring or inventing references.

## Lifecycle status

The completion gate was not met, so this packet must not be moved to `90 - Processed`.

Move the source packet from the active queue to `3 - Needs Resolution`. Keep the parent PubMed trending task unchecked until full ATOM, SEA, and bibliography processing are complete.

## Next action

Retry the exact *Blood* article or a lawful repository or accepted-manuscript route. Once the primary publication body is available, rerun `@ATOM + @SEA + reference task queue`.

## Governing sources

ATOM precedence used for the completion decision:

1. `literature(1).py`
2. `literature_atoms(1).py`
3. `literature_atom.schema.json`
4. `README(2).md`
5. `example_atom(1).json`

SEA governing protocol: `summary-evaluation-appraisal-protocol-v4-compact.md`

Large-source guardrail: `large-source-ATOM-SEA.md`
