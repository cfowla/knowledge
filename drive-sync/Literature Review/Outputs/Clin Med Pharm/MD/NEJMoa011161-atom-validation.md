# NEJMoa011161 ATOM extraction and validation report

## Source metadata

- **Primary file:** `NEJMoa011161.pdf`
- **Title:** Effects of Losartan on Renal and Cardiovascular Outcomes in Patients with Type 2 Diabetes and Nephropathy
- **Journal citation:** N Engl J Med 2001;345:861-869
- **Trial:** RENAAL (Reduction of Endpoints in NIDDM with the Angiotensin II Antagonist Losartan)
- **Source type:** Randomized, double-blind, placebo-controlled, multinational clinical trial
- **Supporting materials:** None specified
- **Publication ID:** `1428a393-0dc7-5b36-9a01-ebb04b48cf74`
- **Extraction run:** `NEJMoa011161-primary-v1`
- **Input SHA-256:** `37dba83eb7ae73893c0172b877c3df72cd8d75924eea27ffccf3ff6e86eb83e1`

## Atom counts

- **Total atoms:** 33

| Atom kind | Count |
|---|---:|
| `adverse_event` | 1 |
| `author_conclusion` | 1 |
| `comparator_description` | 1 |
| `conflict_of_interest` | 1 |
| `eligibility_criterion` | 2 |
| `funding_disclosure` | 1 |
| `intervention_description` | 1 |
| `limitation` | 2 |
| `method` | 3 |
| `outcome_definition` | 2 |
| `population_description` | 1 |
| `qualitative_result` | 1 |
| `quantitative_result` | 15 |
| `study_objective` | 1 |

## Validation report

- Pydantic structural validation: **33/33 passed**; 0 failed.
- Atom-kind sufficiency validation: **33/33 passed**; 0 errors; 0 warnings.
- JSON serialization-schema validation: **0 errors**.

## Assertion-origin handling

- Reported source claims were kept as `directly_reported` or `normalized_from_source` depending on whether normalization/paraphrase was required.
- One safety atom uses `calculated_from_reported_data`: the -4.5 percentage-point absolute difference in adverse-event discontinuation (17.2% vs 21.7%).
- No appraisal judgments were encoded as reported study results.

## Coverage and extraction limitations

- Extraction used the raw 9-page primary PDF only; no corresponding appendix, protocol, correction, or supplement was specified for this paper.
- Main trial design, eligibility, treatment, endpoint definitions, primary renal outcomes, key secondary cardiovascular/renal outcomes, safety/tolerability, author conclusions, funding, and conflicts were atomized.
- The investigator roster and bibliography were treated as provenance/context rather than atom targets.
- The source contains additional baseline and concomitant-medication values not individually atomized because they do not each change the independently reviewable trial claim set.
- No DOI or current-practice claims were inferred or externally verified for this extraction.
- All atoms remain `needs_review`; validation establishes structural/sufficiency compliance, not human source verification.

## QA status

**PASS** — no structural, sufficiency, or JSON-schema validation errors were detected.
