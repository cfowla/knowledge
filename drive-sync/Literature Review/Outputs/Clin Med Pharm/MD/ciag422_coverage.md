# ciag422 Coverage and Processing Note

## Source coverage manifest
- Source ID: `ciag422`
- Exact title: Real-World Experience of Hepatitis C Treatment With Glecaprevir-Pibrentasvir During Pregnancy
- Source type: Brief report / retrospective case series
- Version/date: Published online 11 August 2026
- Sections/headings: Abstract; Introduction/background; Methods; Results; Discussion; Notes; References.
- Main-text figures: none.
- Main-text tables: Table 1, “Characteristics and Outcomes Among Patients Completing Glecaprevir-Pibrentasvir Treatment During Pregnancy” (continued across page 2).
- Algorithms/workflows: none.
- Appendices/supplements: none specified for this task.
- Visual strategy: Table 1 reconstructed as a structured HTML table in the SEA artifact.
- Omissions: reference list not condensed beyond provenance context.

## ATOM processing
- Atom count: 30
- Structural validation: PASS
- Sufficiency validation: PASS
- Structural errors: 0
- Sufficiency errors: 0
- Sufficiency warnings: 0

## Source inconsistency retained
Table 1 reports normal on-treatment ALT/AST/total bilirubin in `n=9`, whereas the Results text states liver function testing was available in `8 of 10` completers. The extraction preserves both source statements as separate atoms and flags the discrepancy rather than selecting one denominator.

## Extraction limitations
- Primary article only.
- Retrospective design, small cohort, no comparator, and incomplete SVR12/infant follow-up.
