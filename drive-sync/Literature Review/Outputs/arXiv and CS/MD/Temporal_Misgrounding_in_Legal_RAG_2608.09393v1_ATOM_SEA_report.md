# ATOM + SEA execution report — arXiv:2608.09393v1

## Source metadata

- **Title:** Temporal Misgrounding in Legal RAG: A Versioned-Corpus Benchmark for French Tax Law
- **Authors:** Rose Cymbler; Daniel Guez; Laurent Fabre
- **Source type:** arXiv preprint / ICML 2026 AI4Law workshop benchmark and controlled retrieval study
- **Version/date:** v1, 10 Aug 2026
- **Identifier:** arXiv:2608.09393v1; DOI 10.48550/arXiv.2608.09393
- **Retrieved file:** `2608.09393v1.pdf`
- **PDF SHA256:** `1188737ad79483916dc75041a38e7de0ab8019f44a39f91db510e39a71f00150`
- **Publication ID:** `763d2349-287e-5b59-8a53-af6f886da925`
- **Extraction run ID:** `2608.09393v1-atom-v1`

## ATOM results

- **Extracted atoms:** 56
- **Structural validation errors:** 0
- **JSON Schema validation errors:** 0
- **Sufficiency errors:** 0
- **Sufficiency warnings:** 0

### Atom counts by kind

- `author_conclusion`: 1
- `data_availability`: 1
- `limitation`: 5
- `method`: 15
- `other`: 1
- `population_description`: 1
- `qualitative_result`: 3
- `quantitative_result`: 28
- `study_objective`: 1

### Structural / schema validation

No structural validation errors.
No JSON Schema validation errors.

### Sufficiency validation

No sufficiency errors or warnings.

## Extraction limitations

- The LiteratureAtom schema is designed for primary literature but its quantitative context fields are clinically styled. For AI/ML benchmark statistics, `population` is used for the evaluated question/dataset set, `exposures` for the retrieval/evaluation condition or extraction pipeline, and `outcome` for the reported metric. This is a schema-fit choice, not a claim that these are clinical exposures or outcomes.
- The paper reports a range (98–99%) for one link-precision audit; the quantitative atom stores the midpoint (98.5) as a normalized numeric estimate while preserving the 98–99 range as an interval and in the canonical statement.
- The leave-one-article-out result is reported as a range (98.1–99.2%); the atom stores the midpoint as the normalized estimate and preserves the range as an interval.
- Funding and conflict-of-interest atoms were not created because the retrieved PDF did not report specific funding or COI statements in the inspected main text/appendices.
- Reference-list entries were not atomized.

## SEA source / coverage manifest

```json
{
  "source_id": "arXiv:2608.09393v1",
  "exact_title": "Temporal Misgrounding in Legal RAG: A Versioned-Corpus Benchmark for French Tax Law",
  "source_type": "arXiv preprint / ICML 2026 AI4Law workshop benchmark and controlled retrieval study",
  "date_or_version": "10 Aug 2026; v1",
  "sections_or_headings": [
    "Abstract",
    "1. Introduction",
    "2. Related Work",
    "3. Why Static RAG Fails on Legal QA",
    "4. Corpus Construction",
    "5. Benchmark Design",
    "6. Experiments",
    "7. Results",
    "8. Conclusion",
    "9. Limitations and Future Work",
    "Impact Statement",
    "References",
    "Appendix A. Corpus and Benchmark Statistics",
    "Appendix B. Version-Aware Jurisprudence Linking",
    "Appendix C. Case Study: Temporal Misgrounding on Article 219 CGI",
    "Appendix D. Reproducibility",
    "Appendix E. Control Condition (Well-Formedness)"
  ],
  "figures": [
    "Figure 1 — Article 219 three-condition case study"
  ],
  "tables": [
    "Table 1 — R3 results across 11 models and four conditions",
    "Table 2 — Tax legislation corpus statistics",
    "Table 3 — R3 question distribution by article/sub-domain",
    "Table 4 — Jurisprudence links/decisions by decade"
  ],
  "algorithms_or_workflows": [
    "Versioned legislation extraction",
    "Version-aware jurisprudence citation linking",
    "Deterministic nugget scoring",
    "All-model-hard and current-version-divergence filtering",
    "Three-condition controlled experiment",
    "C_prod dense+BM25+RRF retrieval and date-version resolution",
    "Cluster-aware statistical analysis"
  ],
  "appendices_or_supplements": [
    "Appendices A–E retained because they materially affect corpus coverage, quality audit, failure interpretation, reproducibility, and well-formedness controls"
  ],
  "visual_strategy": {
    "structured_blocks": [
      "Tables 1–4 reconstructed as HTML tables",
      "Figure 1 reconstructed as a three-condition flow block"
    ],
    "embedded_crops_or_screenshots": [],
    "omitted_with_reason": []
  },
  "coverage_decision": "Full main text plus all substantive appendices A–E; bibliography not condensed beyond related-work context.",
  "omissions": [
    "Reference list entries are not individually summarized or atomized."
  ]
}
```

## SEA appraisal summary

- **Verdict:** Read first
- **Relevance:** 9/10
- **Novelty:** 8/10
- **Method strength:** 8/10
- **Evidence strength:** 8/10
- **External validity:** 5/10
- **Implementation value:** 8/10
- **Principal caveat:** The benchmark intentionally selects all-model-hard temporal-drift questions, and the current-version divergence filter removes almost all cases where current law still contains the gold value. The static-RAG floor is therefore a diagnostic conditional result, not an estimate of typical legal-RAG accuracy.
- **Reproducibility caveat:** The exact end-to-end `C_prod` retriever is proprietary; released per-question outputs permit score verification but not full pipeline reproduction.

## SEA mechanical QA

```json
{
  "title": "SEA — Temporal Misgrounding in Legal RAG (arXiv:2608.09393v1)",
  "missing_anchors": [],
  "forbidden_tokens": [],
  "byte_size": 29895
}
```

## Generated artifacts

- `Temporal_Misgrounding_in_Legal_RAG_2608.09393v1_atoms.json`
- `Temporal_Misgrounding_in_Legal_RAG_2608.09393v1_SEA.html`
- `Temporal_Misgrounding_in_Legal_RAG_2608.09393v1_ATOM_SEA_report.md`
