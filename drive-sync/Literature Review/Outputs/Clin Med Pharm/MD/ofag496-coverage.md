# ofag496 — ATOM coverage and processing notes

## Source identity

- File: `ofag496.pdf`
- Title: *Clinical characteristics and outcomes of invasive Listeria monocytogenes infection: a 45-year retrospective study at a U.S. Tertiary Center*
- DOI: `10.1093/ofid/ofag496`
- Source form: accepted manuscript, Open Forum Infectious Diseases
- PDF pages: 17
- SHA-256: `4d8535816e0d0f5320f3c03034b2a7136fa9eb55e6b2cea3a1f034e009d1cde8`
- ATOM extraction run: `ofag496-primary-v1`

## Coverage

The complete 17-page primary PDF was inspected, including the abstract, introduction, methods, results, discussion, conclusion, disclosures, references, Tables 1–4, and Figure 1 graphical abstract. Pure bibliography entries were not atomized. Table 3 individual endovascular-case details were reconciled for SEA and represented in ATOM at the syndrome-level rather than as a separate atom for every case-field cell.

## Validation

- Atoms: **104**
- Pydantic structural validation: **PASS**
- JSON Schema serialization validation: **PASS**
- Sufficiency validation: **PASS**
- Sufficiency warnings: **0**

## Source-internal inconsistencies retained, not silently repaired

1. Methods describes a cohort across Mayo Clinic Health System sites; Discussion/Limitations calls the study single-center.
2. Results prose reports median treatment duration 21 days (IQR 21–28); Table 1 reports 21 days (IQR 14–28).
3. Results prose cites Table 4 for adjunctive gentamicin HR 0.40 (95% CI 0.05–3.42), but the rendered Table 4 has no gentamicin row.
4. Figure 1 reports fever absent in 32%, while Table 1 reports fever present in 62%; the source does not reconcile the mismatch.
5. Figure 1 reports rhombencephalitis in 42%, while Results text reports 5/13 (39%) among imaged neurolisteriosis cases.

## Missing source material

The article cites Supplementary Tables 1–5 and Supplementary Figure 1. They were not embedded as PDF attachments, and no separate supplement/appendix/companion file was present in the designated Google Drive source folder. Supplementary-only details were therefore not reconstructed or imported.

## Extraction boundary

Assertions were kept as reported/normalized from the primary PDF. No current-guideline, drug-information, or external-practice verification was added to ATOM content.
