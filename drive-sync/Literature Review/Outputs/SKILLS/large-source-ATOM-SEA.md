---
name: large-source-atom-sea
description: Apply LiteratureAtom extraction and SEA appraisal to large or semantically dense sources using semantic batching, shared source identity, per-batch validation, hierarchical synthesis, and whole-source QA.
---

# Large-Source ATOM + SEA

Use this skill when a source is too large or too dense for a single high-confidence `@ATOM`, `@SEA`, or `@LIT-PIPELINE` pass.

The objective is not merely to fit the source into context. Preserve **coverage, provenance, semantic boundaries, quantitative detail, validation, and whole-source interpretation**.

This skill supplements the governing ATOM and SEA protocols; it does not replace them.

## Governing sources

### ATOM precedence

1. `literature.py` — domain model + structural validation
2. `literature_atoms.py` — atom-kind sufficiency validation
3. `literature_atom.schema.json` — serialization contract
4. `README(2).md` — workflow intent
5. `example_atom.json` — illustrative only

### SEA precedence

1. `summary-evaluation-appraisal-protocol-v4-compact.md`
2. v3 material — historical/reference only
3. primary source content
4. external material only when permitted or required for verification

If sources conflict, follow the governing source and report the conflict.

---

# Core invariants

1. **A batch is an extraction boundary, not a publication boundary.**
   - One source keeps one source/publication identity across all batches.

2. **Batch semantically, not mechanically.**
   - Prefer complete sections, questions, experiments, recommendation blocks, disease states, or result families.
   - Equal page-count chunks are a fallback.

3. **Use original source material for every extraction pass.**
   - Do not atomize a prior batch summary.
   - Intermediate summaries provide context only.

4. **Preserve assertion origin.**
   - Keep directly reported, normalized, calculated, and inferred assertions distinct.
   - Never turn appraisal into reported evidence.

5. **Preserve source anchors.**
   - Every atom must remain traceable to the original source.

6. **Validate each batch before merging.**
   - Structural validation first.
   - Sufficiency validation second.

7. **Do not invent missing context.**
   - Missing details remain missing.

8. **Do not perform final SEA scoring until whole-source extraction and reconciliation are complete.**

9. **References are normally provenance infrastructure, not extraction targets.**
   - Read cited primary studies directly when primary-study atoms are needed.

10. **Respect source type.**
    - A guideline or review that summarizes a trial did not generate that trial result.

---

# 1. Decide whether to batch

There is no authoritative page-count cutoff. Batch when one-pass processing creates a material risk of incomplete coverage, weak anchoring, over-compression, or insufficient working context.

Strong signals:

- many independently reviewable claims or recommendations;
- many figures, tables, algorithms, or appendices;
- multiple clinical questions, disease states, experiments, or result families;
- long quantitative methods/results sections;
- large reference sections inflating total page count;
- the source technically fits in context but leaves little room for careful extraction and QA.

When uncertain, prefer several coherent passes over one maximal-context pass.

---

# 2. Build the large-source manifest

Before ATOM extraction or SEA narrative drafting, map the source.

```text
LARGE-SOURCE MANIFEST
source_id:
exact_title:
source_type:
version_or_date:
stable_identifier:
source_hash_if_available:
page_count:
substantive_page_range:
reference_page_range:
sections_or_headings:
clinical_questions_or_experiments:
figures:
tables:
algorithms_or_workflows:
appendices_or_supplements:
shared_context_material:
batch_plan:
  - batch_id:
    page_or_section_range:
    semantic_scope:
    required_context:
    known_cross_references:
coverage_decision:
omissions_and_reasons:
```

## Boundary rules

Avoid splitting:

- a clinical question from its suggested approach/rationale;
- a result from methods needed to interpret it;
- a recommendation from its conditions/exceptions;
- a figure from its legend/discussion;
- a table from its title/footnotes;
- a multi-page algorithm in the middle of its decision path.

If a semantic section is still too large, subdivide one level deeper by numbered question, experiment, endpoint family, or subsection.

---

# 3. Establish shared source identity

For LiteratureAtom work, create one source-level identity before the first batch:

```text
publication_id: <one UUID shared by every atom from the source>
```

Each atom receives its own `atom_id`.

Each batch receives its own provenance-level identifier:

```text
extraction_run_id:
  source-general-v1
  source-section-a-v1
  source-section-b-v1
```

Do not change publication identity merely because extraction is batched.

---

# 4. Execute ATOM by semantic batch

For each batch:

1. Load the **original source pages/content** for that semantic unit.
2. Add only the minimum shared context needed to interpret the section.
3. Identify in-scope tables, figures, and cross-references.
4. Extract one atom per independently reviewable assertion.
5. Preserve reported vs normalized vs calculated vs inferred status.
6. Populate only source-supported atom context.
7. Attach a reliable source anchor and batch-specific provenance.
8. Run structural validation.
9. Run sufficiency validation.
10. Repair only directly supportable issues.
11. Save atoms and validation separately.

Recommended files:

```text
<source>-<batch>-atoms.json
<source>-<batch>-validation.json
```

## Atom context and sufficiency

Follow `literature_atoms.py` exactly. Examples:

- `quantitative_result` requires population + exposures + outcome + quantitative result;
- `adverse_event` requires exposures + outcome + quantitative result;
- `subgroup_result` requires population + exposures + outcome + quantitative result and `population.subgroup=true`;
- intervention/exposure/comparator descriptions require the matching exposure role.

Keep structural errors, sufficiency errors, and warnings separate.

## Source anchoring

Prefer the most specific defensible locator available:

```text
section + page + paragraph/sentence
section + page + table + row/column
section + page + figure
section + page + verbatim excerpt
supplement + locator
```

---

# 5. Guideline and secondary-source guardrail

The current LiteratureAtom model is oriented toward primary literature and has no dedicated `guideline_recommendation` atom kind.

For guidelines or consensus documents:

- preserve recommendation wording as panel/guideline language;
- use `author_conclusion` or `other` only when defensible under the current schema;
- descriptive tags such as `guideline_recommendation` may be used;
- preserve conditions, alternatives, exclusions, and uncertainty;
- do not invent recommendation strength or evidence grade.

When a guideline reports an underlying study result:

- represent it as **the guideline's report of that study**;
- anchor provenance to the guideline page;
- a descriptive tag such as `secondary_reported_result` may be useful;
- do not imply the guideline itself enrolled participants or generated the result;
- extract the cited primary publication separately when primary-study atoms are required.

Do not redesign the atom schema midway through one extraction. Record schema gaps separately.

---

# 6. Merge ATOM batches deterministically

Merge only after every batch completes local validation.

Confirm:

- one shared `publication_id`;
- compatible `schema_version`;
- unique `atom_id` values;
- valid provenance on every atom;
- traceable `extraction_run_id` values;
- all expected substantive sections are represented or explicitly omitted.

## Cross-batch duplicate review

Check for duplicate extraction caused by overlap/shared context:

- near-identical canonical statement + same anchor;
- same table row or recommendation extracted twice;
- same population/exposure/outcome/result repeated across adjacent batches.

Do **not** deduplicate solely because two distinct source assertions have similar wording.

## Cross-batch consistency review

Check for:

- apparently conflicting numbers from different populations/timepoints;
- repeated recommendations with different conditions;
- terminology changes;
- definitions established globally but applied locally;
- cross-referenced results fully reported elsewhere.

Resolve only when supported by the source. Otherwise retain the distinction and flag it.

Recommended merged outputs:

```text
<source>-atoms.json
<source>-validation.json
<source>-coverage.json
```

---

# 7. Execute SEA hierarchically

Large-source SEA should use hierarchical synthesis rather than one-pass compression.

## SEA Pass 0 — global scaffold

Create Pass 0 before deep section passes. Capture:

- exact source identity and type;
- purpose and scope;
- methods/development process;
- global populations/settings;
- definitions and terminology;
- recommendation/evidence framework if present;
- general management principles;
- complete section map;
- global figures/tables/workflows;
- substantive vs reference/appendix ranges;
- appraisal constraints;
- deep-pass plan and cross-references.

Pass 0 is context and coverage infrastructure. **It is not the final appraisal.**

## Deep passes — one semantic section at a time

Each deep pass must inspect the original source section. Pass 0 supplies only global context.

Recommended intermediate artifact:

```text
SECTION PASS
batch_id:
source_pages_or_headings:
section_purpose:
clinical_questions_or_claims:
recommendations_or_main_findings:
key_rationale_or_mechanism:
quantitative_evidence:
comparators:
safety_or_failure_signals:
limitations_and_uncertainty:
implementation_or_practice_notes:
figures_tables_workflows:
cross_references:
source_anchors:
open_questions_or_conflicts:
```

Preserve load-bearing magnitudes: denominators, effect estimates, confidence intervals, thresholds, doses, timepoints, sample sizes, and central benchmark values.

For guidelines, keep separate:

1. suggested approach/recommendation;
2. rationale;
3. evidence summarized from underlying studies;
4. model appraisal of that evidence.

## Final SEA synthesis

After all deep passes:

1. combine Pass 0 and all section artifacts;
2. revisit the original source for unresolved conflicts/cross-references;
3. reconcile every main-text figure, table, algorithm, and workflow;
4. identify cross-cutting themes, exceptions, and dependencies;
5. separate source claims from appraisal;
6. apply the source-type-specific SEA module;
7. assign final scores only now;
8. generate one self-contained HTML artifact;
9. run semantic and mechanical QA.

Do not simply concatenate section summaries.

Do not average section scores to create a whole-source score.

---

# 8. References, appendices, figures, and tables

## References

Normally exclude pure bibliography pages from ATOM extraction and routine SEA condensation.

Use references to:

- identify primary sources behind summarized results;
- resolve provenance;
- locate studies requiring separate extraction;
- assess the composition/recency of the evidence base when relevant to appraisal.

Do not treat citation entries themselves as evidence atoms.

## Appendices/supplements

Include when they materially affect methods, results, dosing, algorithms, recommendations, safety, reproducibility, implementation, or appraisal. Otherwise record the omission and reason.

## Figures/tables/workflows

Before a batch is complete, reconcile every in-scope visual as:

- structured extraction;
- embedded crop/screenshot for SEA when layout is load-bearing;
- omitted with reason.

For ATOM, anchor table/figure-derived atoms to the specific visual locator.

Treat a multi-page table as one semantic object even if it crosses a nominal batch boundary.

---

# 9. Combined ATOM + SEA workflow

When both are requested, map the source once and reuse semantic boundaries where appropriate:

```text
source map + coverage manifest
→ shared source identity
→ Pass 0 global context
→ for each semantic batch:
     original source section
     → ATOM extraction
     → structural validation
     → sufficiency validation
     → SEA deep pass
→ merge atoms
→ duplicate + consistency QA
→ reconcile SEA passes
→ claims/sections ↔ atoms crosswalk where defensible
→ identify schema gaps
→ final JSON + validation + HTML
```

ATOM and SEA do not have to use identical boundaries if one workflow has a stronger semantic reason to split differently.

---

# 10. Quality gates

## ATOM batch gate

A batch is complete only when:

- the intended semantic unit was fully inspected;
- assertions were anchored to original source content;
- structural validation completed;
- sufficiency validation completed;
- errors/warnings are recorded;
- unsupported details were not invented;
- limitations are documented.

## Whole-source ATOM gate

The merged set is complete only when:

- all planned substantive sections are represented or explicitly omitted;
- one publication identity is preserved;
- provenance remains traceable;
- duplicates and cross-batch inconsistencies were reviewed;
- final validation was rerun;
- schema gaps are separated from extraction failures.

## SEA section gate

A deep pass is complete only when:

- the full semantic unit was inspected;
- main claims/recommendations are represented;
- central quantitative evidence is preserved;
- visuals/workflows are reconciled;
- limitations are captured near weakened claims;
- source claims remain distinct from appraisal;
- unresolved cross-references are listed.

## Final SEA gate

The final artifact is complete only when:

- Pass 0 and all required deep passes are represented;
- source-wide visual/table/workflow coverage is reconciled;
- cross-section contradictions/exceptions were checked;
- appraisal occurred after synthesis;
- HTML is self-contained and parseable;
- internal chat/file citation syntax is absent from the HTML;
- provenance/caveats are present;
- no TODOs, placeholders, stale headings, or planning language remain.

---

# 11. Recommended artifact layout

```text
source/
  manifest/
    source-manifest.md
    source-coverage.json

  atom/
    batch-00-general-atoms.json
    batch-00-general-validation.json
    batch-01-section-a-atoms.json
    batch-01-section-a-validation.json
    ...
    source-atoms.json
    source-validation.json

  sea/
    pass-00-global.md
    pass-01-section-a.md
    pass-02-section-b.md
    ...
    source-sea.html

  audit/
    cross-batch-duplicates.md
    schema-gaps.md
    unresolved-crossrefs.md
```

Exact filenames may follow project conventions.

---

# 12. Practical guideline batching pattern

For a large clinical guideline:

```text
Batch 0: front matter + methods + global management + shared tables
Batch 1: complete clinical topic / organism / recommendation family
Batch 2: next complete topic
Batch 3: next complete topic
...
References: normally excluded from atomization and routine SEA condensation
```

If one topic remains too dense, subdivide by complete numbered question/recommendation blocks.

Reuse front-matter/global content as **context**, not as repeatedly extracted evidence.

Suggested batch naming:

```text
<source-slug>-general-v1
<source-slug>-<semantic-section>-v1
<source-slug>-<semantic-section>-q1-v1
```

---

# 13. Common failure modes

Avoid:

- one huge pass that produces polished but incomplete extraction;
- arbitrary page chunks that split semantic units;
- treating each batch as a separate publication;
- extracting from prior summaries instead of original source pages;
- duplicating global context into every batch's atom set;
- converting appraisal into reported data;
- presenting secondary trial summaries as primary-study results;
- ignoring figures/tables because prose is easier;
- merging before validation;
- silently deduplicating distinct assertions;
- atomizing the bibliography;
- assigning final SEA scores before whole-source synthesis;
- concatenating section summaries without reconciliation.

---

# Final output contract

Unless otherwise requested, report:

## ATOM

- source metadata and batch manifest;
- atom counts by kind/batch;
- validated merged JSON;
- structural errors;
- sufficiency errors/warnings;
- duplicate/consistency findings;
- extraction limitations;
- schema gaps.

## SEA

- source/coverage manifest;
- hierarchical pass inventory;
- one self-contained HTML appraisal;
- unresolved source limitations;
- concise QA status.

## Combined workflow

Also provide a claim/section ↔ atom crosswalk when it can be created defensibly.

---

# Decision rule

Ask:

> Can the entire source be mapped, independently atomized, anchored, visually reconciled, validated, synthesized, and appraised in one pass without sacrificing completeness or working context?

If uncertain, **batch semantically**.

The objective is not the fewest passes. The objective is a reproducible final artifact whose parts remain traceable to the original source and whose whole-source interpretation is assembled only after those parts have been validated.
