# Weber et al. 2016 processing report

## Source
- Title: Blood pressure and glycaemic effects of dapagliflozin versus placebo in patients with type 2 diabetes on combination antihypertensive therapy: a randomised, double-blind, placebo-controlled, phase 3 study
- DOI: 10.1016/S2213-8587(15)00417-9
- PMID: 26620248
- Trial registration: NCT01195662
- Source packet: main article PDF + peer-reviewed supplementary appendix
- Main PDF SHA-256: `42fd99ac6a88460709e5a8ec93c827561e6fd74331e0b3c57ac89571c89c3f1e`
- Supplement SHA-256: `d35ab7f238250e40cf960ef6cbee0dc8045b85d354747ec77279e1c824e54224`

## ATOM
- Publication identity: `bd40990b-28ab-54a6-97ab-42d55e5897f0`
- LiteratureAtoms: **105**
- Pydantic structural validation: **PASS** (0 errors)
- JSON Schema validation: **PASS** (0 errors)
- Sufficiency validation: **PASS** (0 errors; 0 warnings)
- Exact duplicate canonical statements: **0**
- Exact duplicate statement-anchor pairs: **0**
- Atom counts by kind: {'adverse_event': 10, 'author_conclusion': 3, 'comparator_description': 1, 'conflict_of_interest': 1, 'eligibility_criterion': 13, 'funding_disclosure': 2, 'intervention_description': 1, 'limitation': 5, 'method': 13, 'outcome_definition': 10, 'population_description': 7, 'quantitative_result': 22, 'study_objective': 1, 'subgroup_result': 16}

## SEA
- Coverage: 3/3 main figures, 2/2 main tables, 3/3 supplementary figures, 2/2 supplementary tables, full eligibility appendix.
- SEA QA: **PASS**
- Verdict: **Read soon**.
- Main boundary: overall randomized efficacy is strong short-term evidence; antihypertensive-class differences are post-hoc exploratory analyses.

## Source-integrity / extraction notes
- The thiazide-subgroup seated-SBP CI was reconciled against the article summary and rendered Figure 3 as **−6.16 to +1.40 mm Hg**; a text-extraction sign loss was not propagated.
- The bibliography was not atomized as trial-generated evidence.
- Calculated risk differences and selected between-arm laboratory differences are explicitly tagged `calculated_from_reported_data`.

## Reference task queue
- 27 bibliography entries extracted.
- Reference 27 (Zinman et al. 2015; NEJMoa1504720) is marked complete because its validated ATOM/SEA package already exists in the current TBR stream.
- Remaining references stay unchecked until processed directly.

## Output routing
- JSON outputs → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / JSON`
- SEA HTML → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / HTML`
- Reference queue + this report → `GitHub Sync / Literature Review / Outputs / Clin Med Pharm / MD`
- Source packet → `TBR / 90 - Processed / Clinical Medicine & Pharmacy / 57 - Weber Mansfield 2016`
