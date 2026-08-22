# Summary, Evaluation, and Appraisal Protocol — Integrated Compact v3

> Reusable standard for scientific, clinical, scholarly, and AI/ML reference HTML files. This version folds prior guardrail patches into the operating workflow, coverage rules, visual extraction rules, appraisal scoring, HTML handling, and QA gates so future updates do not accumulate as append-only context.

## Contents

1. Protocol metadata
2. Core operating standard
3. End-to-end execution contract
4. Source intake, routing, and grounding
5. Coverage manifest and inclusion gate
6. Section condensation rules
7. Figure, table, exhibit, and workflow extraction
8. Evaluation and appraisal rubric
9. Domain-specific appraisal modules
10. Reference HTML output specification
11. Reusable prompts
12. Quality-control checklist
13. Protocol maintenance rules

## 1. Protocol metadata

| Field | Standard |
|---|---|
| Protocol name | Summary, Evaluation, and Appraisal Reference HTML Protocol |
| Primary use | Scientific, clinical, scholarly, and AI/ML source evaluation |
| Output format | One self-contained, polished, single-file HTML artifact. Do not generate, plan, or substitute PDF, DOCX, slides, Markdown-only output, or alternate deliverables unless the user explicitly asks for them. |
| Default depth | Section-by-section synthesis, visual/table/workflow extraction, appraisal, implementation takeaways |
| Default tone | Concise, technical, evidence-oriented, non-promotional |
| Best fit | Papers, preprints, guidelines, protocols, benchmarks, clinical reviews, technical reports, practice documents |
| Scope warning | This protocol supports source understanding and appraisal. It does not replace primary-source reading, clinical judgment, regulatory review, or local policy. |

## 2. Core operating standard

Each reference file must make the source easier to retain, search, critique, and reuse. It must separate: what the source says, how it supports the claims, what the figures/tables/workflows contain, how credible the work is, and what should be done with it next.

Default compression is strict: summarize each source section in no more than two dense paragraphs unless greater depth is explicitly requested. Preserve load-bearing claims, methods, measurements, limitations, quantitative results, and conclusions. Decompose figures, tables, algorithms, workflows, equations, and key appendices into structured blocks because they often carry the most reusable information.

**Execution invariant:** Source access → source map → visual/table inventory → coverage decision → artifact generation → semantic QA → final response.

## 3. End-to-end execution contract

| Phase | Required action | Output / gate |
|---|---|---|
| 1. Source access | Use the user-provided source as the primary object. For remote papers, use web/PDF tooling; do not use container internet for downloads. | Source URL/file, source type, accessible text/visual strategy. |
| 2. Classify source | Identify whether it is a preprint, journal article, guideline, label, benchmark, technical report, software paper, dataset paper, protocol, review, policy, or practice document. | Appraisal lens selected. |
| 3. Map structure | Map actual headings: abstract, background, methods, results, discussion, limitations, conclusion, figures, tables, algorithms, appendices, supplements. Do not force non-IMRaD sources into IMRaD. | Source map. |
| 4. Build coverage manifest | Before drafting prose, enumerate source ID, exact title, source type, date/version, sections/headings, figures, tables, algorithms/workflows, appendices/supplements, coverage decision, and omissions. | Blocking coverage gate; do not draft narrative content or write HTML before this exists. |
| 5. Decide coverage | Reconcile every main-text figure/table/workflow against the manifest. Mark each as structured block, embedded crop/screenshot, or omitted with reason. Include appendices only when methodologically, empirically, clinically, operationally, or reproducibly important. | Coverage decision with figure/table/workflow counts reconciled. |
| 6. Extract and summarize | Condense sections, preserve magnitudes, decompose visuals/tables/workflows, and keep claims separate from appraisal. | Draft content. |
| 7. Appraise | Score only after section extraction and visual/table/workflow extraction are complete. Each rating needs score, one-sentence rationale, evidence basis, limiting factor, and what would raise or lower the score. | Appraisal block; no premature scoring. |
| 8. Generate HTML | Generate one self-contained single-file HTML artifact using the established style. Do not include internal chat/file citation syntax. Include plain source/provenance. | HTML artifact only. |
| 9. Semantic QA | Parse/check HTML, verify required anchors, source ID/title, metadata, manifest counts, figure/table/workflow reconciliation, ratings, provenance, and absence of placeholders, stale filenames/headings, planning language, or internal citation syntax. | Pass/fail gate before final. |
| 10. Final response | Provide artifact link and brief note only unless the user asks for details, citations, or something failed. | Final chat response. |

## 4. Source intake, routing, and grounding

### Minimum metadata

| Field | Required content | Notes |
|---|---|---|
| Title | Exact title | Do not silently shorten titles in the metadata card. |
| Authors / organization | Authors, group authors, issuing body, sponsor | For guidelines, include issuing body and endorsement status. |
| Source type | Preprint, article, guideline, label, benchmark, report, policy, protocol, dataset, software | Determines appraisal lens. |
| Date / version | Publication, submission, update date, version | Critical for preprints, guidelines, software, AI/ML, and practice documents. |
| Identifier | DOI, PMID, PMCID, arXiv ID, URL, registry ID, guideline ID | Prefer stable identifiers. |
| Design | RCT, cohort, case-control, modeling study, benchmark, systematic review, consensus guideline, software architecture, etc. | Do not infer stronger design than reported. |
| Scope warning | What this reference does and does not validate | Required for clinical, regulatory, and AI safety-relevant files. |

### Grounding priority

1. User-provided source or uploaded file.
2. Source metadata page for title, authors, date, version, DOI/PMID/arXiv ID, abstract, or errata.
3. Primary full text, PDF, supplementary appendix, registry, code repository, dataset card, or implementation documentation when appraisal depends on methods or visuals.
4. Guidelines, labels, society statements, or regulatory sources for clinical/practice claims that could affect care.
5. Secondary commentary only when the task asks about reception, controversy, user sentiment, implementation experience, or broader context.

### Tool-output hygiene

Use quiet, task-focused tool commands. Do not print full protocol files, skill files, generated HTML, or long intermediate artifacts to stdout unless needed to diagnose a failure. Prefer concise checks: file existence, byte size, parsed title, anchor list, missing anchors, figure/table counts, and grep checks for placeholders or planning language.

For generated artifacts, write content directly to the output file and verify it with targeted checks. Avoid bloated logs that obscure source-mapping, extraction, appraisal, or QA decisions.

**Currency rule:** Clinical practice, drug information, guidelines, regulatory status, pricing, software, benchmarks, AI model capabilities, and current events require recency verification when feasible. A source can be accurately summarized and still be outdated for practice.

## 5. Coverage manifest and inclusion gate

Before drafting the artifact, create a compact internal manifest:

```text
SOURCE COVERAGE MANIFEST
source_id:
exact_title:
source_type:
date_or_version:
sections_or_headings:
figures:
tables:
algorithms_or_workflows:
appendices_or_supplements:
visual_strategy:
  structured_blocks:
  embedded_crops_or_screenshots:
  omitted_with_reason:
coverage_decision:
omissions:```

**Gate:** Do not draft narrative prose or generate HTML until source ID, exact title, sections/headings, figures, tables, algorithms/workflows, appendices/supplements, visual strategy, coverage decision, and omissions are enumerated. Every main-text figure/table/workflow must be reconciled as one of: structured block, embedded crop/screenshot, or omitted with reason. Screenshot sparingly and only for figures/tables that cannot be reliably reconstructed from parsed text.

## 6. Section condensation rules

| Section type | Preserve | Avoid |
|---|---|---|
| Abstract | Problem, method, main result, claimed implication | Treating author framing as verified evidence. |
| Introduction / background | Rationale, claimed gap, domain context | Overweighting background as proof. |
| Methods | Design, population/data, inclusion/exclusion, intervention/model, comparator/baseline, endpoints, statistics, validation | Vague “standard methods” language. |
| Results | Primary outcomes, effect sizes, uncertainty, benchmark deltas, ablations, subgroup findings, table-linked results | Direction-only summaries without magnitude. |
| Discussion | Authors’ interpretation, stated implications, acknowledged limitations | Accepting speculation as established. |
| Limitations | Internal, external, statistical, operational, regulatory, safety, and generalizability limits | Hiding limitations only in final appraisal. |
| Conclusion | Final claim and justified next step | Letting conclusions inflate weak evidence. |

Preferred block:

```html
<div class="section-summary">
  <h3>Source heading</h3>
  <p>Paragraph 1: section function, claim, and relevance.</p>
  <p>Paragraph 2: load-bearing details, magnitudes, caveats, or limits.</p>
</div>
```

Compression discipline: preserve headings, named methods, numbered frameworks, arms/groups, metrics, timepoints, denominators, sample sizes, effect sizes, confidence intervals, p values, calibration, accuracy, latency, thresholds, and benchmark scores when central. Use “Not tested,” “Not reported,” “Unclear,” or “Out of scope” instead of vague prose. Keep author claims distinct from independent inference.

## 7. Figure, table, exhibit, and workflow extraction

### Inclusion rules

- Include all main-text figures and tables.
- Include all main-text workflows, algorithms, architecture diagrams, benchmark schemas, decision rules, and evaluation pipelines.
- Include appendix/supplement visuals only when they change interpretation, methods, evidence strength, reproducibility, safety, implementation, or appraisal.
- Reconcile every figure/table/workflow from the manifest before HTML generation.
- For each item, choose one representation:
  - structured text/code block when the content can be faithfully reconstructed;
  - embedded crop/screenshot when layout, axes, image content, or table structure is load-bearing and cannot be reliably reconstructed;
  - omitted only when it is non-load-bearing, duplicative, or inaccessible, with the reason stated.
- Do not omit visuals merely to keep the file lean.
- Screenshot sparingly: use screenshots for figures/tables that cannot be reliably reconstructed from parsed text.

### Compact extraction templates

```text
FIGURE N — Title
Purpose:
Structure/panels:
Variables/axes/groups:
Numeric details:
Main pattern:
Interpretation:
Limits:
Representation:
  structured block / embedded crop-screenshot / omitted with reason
```

```text
TABLE N — Title
Rows:
Columns:
Key values:
Pattern:
Appraisal: denominators, uncertainty, comparators, missing data, subgroup power.
Representation:
  structured block / embedded crop-screenshot / omitted with reason
```

```text
WORKFLOW / ALGORITHM — Title
Inputs:
Process / decision rules:
Outputs:
Failure modes:
Human review:
Governance: boundary checks, escalation, audit trail, versioning, monitoring triggers.
Representation:
  structured block / embedded crop-screenshot / omitted with reason
```

Visual appraisal questions: Are denominators, scales, units, uncertainty, and time windows clear? Does the visual support the text claim? Could confounding, selection bias, leakage, cherry-picking, or calibration failure explain the pattern? For AI/ML, separate training, validation, test, external validation, ablation, and deployment. For clinical work, distinguish surrogate from patient-centered outcomes.

## 8. Evaluation and appraisal rubric

Final appraisal must answer: Is the source worth reading? How much should it be trusted? What practical use should it have?

Appraisal timing rule: do not assign final scores or verdict labels until source mapping, section condensation, and figure/table/workflow extraction are complete. Preliminary impressions may guide attention, but the artifact must present only post-extraction ratings.

| Dimension | Score | Meaning |
|---|---:|---|
| Relevance | 0–10 | Fit to clinical, research, AI/ML, workflow, or implementation interests. |
| Novelty | 0–10 | Added value beyond known methods, guidelines, systems, or prior evidence. |
| Method strength | 0–10 | Design, controls, statistics, validation, baselines/comparators. |
| Evidence strength | 0–10 | How directly data support claims and whether uncertainty is reported. |
| External validity | 0–10 | Generalizability across sites, populations, datasets, tasks, or practice settings. |
| Implementation value | 0–10 | Enough detail to change practice, build a tool, or inform workflow design. |

Each score must include: score, one-sentence rationale, evidence basis, principal limiting factor, and what would raise or lower the score.

### Verdict labels

| Verdict | Use when | Typical action |
|---|---|---|
| Read first | High relevance and high utility | Read full text; preserve methods, figures, tables. |
| Read soon | Useful but not immediately central or not mature | Add to queue/notes/RAG corpus. |
| Skim deeply | One or two high-value ideas, methods, datasets, or warnings | Extract key method/visual and move on. |
| Skim | Peripheral or incremental | Capture citation and one-line takeaway. |
| Do not prioritize | Low relevance, weak methods, redundant contribution, poor fit | Skip unless needed for completeness. |
| Do not use for practice | Interesting but inadequate for clinical/operational/regulatory action | Background or hypothesis only. |

### Evidence-strength anchors

- **9–10:** Prospective/well-controlled or robust benchmark; external validation; meaningful outcomes; strong baselines/ablations; reproducible implementation; leakage checks; transparent limitations.
- **7–8:** Good design with manageable limits; uncertainty reported; reasonable generalizability; mostly clear implementation.
- **5–6:** Useful but constrained by observational/surrogate/small/narrow data, weak baselines, missing ablations, or partial reproducibility.
- **3–4:** Hypothesis-generating; serious confounding, underpowering, unclear endpoints, limited evaluation, or demo-level support.
- **0–2:** Unsupported, unsafe, irreproducible, contaminated, marketing-like, or not supported by results.

Score-capping rule: cap evidence strength and/or external validity when there is no external validation, no uncertainty reporting, weak or missing baselines, unclear denominators, limited reproducibility, benchmark-only evidence, untested deployment assumptions, or inadequate failure analysis. Do not let high relevance inflate evidence strength.

Red flags: claim inflation, missing denominators, surrogate substitution, benchmark leakage, weak comparator, no failure analysis, no implementation path, and clinical/regulatory ambiguity.

## 9. Domain-specific appraisal modules

Use the core structure for every file, then add only the relevant modules.

| Module | Preserve |
|---|---|
| Clinical trials | PICO, duration, randomization, blinding, attrition, adverse events, effect size, NNT/NNH, external validity. |
| Pharmacotherapy | Dose, route, PK/PD, renal/hepatic adjustment, exposure metrics, MIC/target attainment, interactions, contraindications, monitoring, label/guideline alignment. |
| Guidelines | Recommendation wording, evidence grade, population, exclusions, implementation notes, controversies, differences from prior guidance. |
| Systematic reviews | Search dates, databases, selection criteria, risk of bias, heterogeneity, publication bias, GRADE certainty, pooled estimates, applicability. |
| AI/ML benchmarks | Task, datasets, splits, metrics, baselines, prompts, tool use, contamination risk, ablations, compute, reproducibility, error modes, deployment relevance. |
| Agent / RAG systems | Tools, retrieval corpus, context policy, state management, verifier design, citation rules, trace logging, fallback behavior, failure analysis. |
| Parser / extraction papers | Supported formats, layout handling, table/figure extraction, citation preservation, schema, fixtures, error taxonomy, downstream use cases. |
| Practice workflows | Trigger, actors, handoffs, required data, decisions, escalation, downtime, documentation, audit trail, measurable outcomes. |

Clinical add-on:

```text
PICO:
Validity: design, bias, confounding, missing data, statistics, subgroups.
Practice translation: patient-centered benefit, safety, monitoring, exclusions, guideline alignment, local barriers.
Bottom line: use now? yes/no/maybe; strength; conditions required.
```

AI/ML add-on:

```text
Task:
Data: datasets, splits, leakage, external validation.
Method: model, retrieval/tools/agents, prompting/training, baselines, ablations.
Metrics: primary/secondary, calibration, latency/cost, human evaluation.
Failures: error taxonomy, robustness, safety, generalization.
Bottom line: conceptual, benchmark-useful, build-useful, or deployment-useful.
```

## 10. Reference HTML output specification

### Required layout

| Section | Purpose | Default content |
|---|---|---|
| Header | Identity | Source title and reference scope. The artifact target is fixed: one self-contained HTML file. |
| Table of contents | Navigation | Anchors for metadata, synthesis, sections, visuals, appraisal, takeaways. |
| Metadata | Traceability | Title, authors, source, date/version, type, domain, scope warning. |
| One-page synthesis | Compressed understanding | Core thesis, value, limitations, tags. |
| Section condensation | Faithful summary | Max two paragraphs per source section by default. |
| Figures / tables / exhibits | Visual evidence | Structured blocks for every included figure/table/workflow/algorithm. |
| Evaluation and appraisal | Independent judgment | Verdict, strengths, limitations, ratings, bottom line. |
| Implementation / practice takeaways | Actionability | What to build, monitor, change, read next, avoid, or not overclaim. |
| Footer / provenance | Scope | Source URL/identifier, generation date, caveats. |

### Style and citation standards

Use a single-file HTML document with embedded CSS; card-based sections; metadata and rating grids; dark code blocks for structured visual/table/workflow extraction; semantic HTML; print-friendly CSS; no external fonts, scripts, remote images, or external CSS. Use colored callouts sparingly: verdict/core thesis, caution, serious limitation, high-value takeaway. Do not rely on external fonts, scripts, remote images, or external CSS; embedded crops/screenshots are allowed only when selected by the visual strategy in the coverage manifest.

Do not place internal chat citation syntax, file-search citation syntax, or tool-result markers inside the HTML artifact. Use a plain source/provenance section with source title, source URL or identifier, version/date, evaluated file or URL when relevant, generation date, and caveats. The final chat response should provide the artifact link and brief note only unless the user asks for source citations, process details, or something failed.

Component vocabulary: `header`, `.wrap`, `nav.toc`, `section`, `.meta-grid`, `.rating-grid`, `.takeaway-grid`, `.mini-card`, `.verdict`, `.warning`, `.badnote`, `.goodnote`, `.section-summary`, `.tag`, `pre > code`.

### Invariant

1. Target artifact is fixed: one self-contained HTML file. Do not consider PDF, DOCX, slides, or alternate formats unless explicitly requested.

## 11. Reusable prompts

### Standard prompt

```text
[SOURCE URL OR FILE]
Create one self-contained reference HTML file using the integrated Summary, Evaluation, and Appraisal protocol. Treat HTML as the fixed output target unless I explicitly request another format. Extract metadata, map the source, build the coverage manifest before drafting prose, reconcile all figures/tables/workflows, condense each section to no more than two paragraphs, preserve quantitative and methodological details, separate summary from appraisal, score only after extraction is complete, include implementation takeaways, run semantic QA, and provide the artifact link.
```

### Clinical-practice prompt

```text
[GUIDELINE / ARTICLE / LABEL / CLINICAL SOURCE]
Use the protocol with a clinical-practice lens. Add PICO/clinical question, recommendation strength/evidence quality, population/exclusions, dosing/monitoring/contraindications/interactions/renal-hepatic considerations where relevant, safety signals, implementation constraints, and what should or should not change in practice. Warn explicitly when evidence is insufficient for clinical action.
```

### AI/ML research prompt

```text
[PAPER / PREPRINT / TECHNICAL REPORT]
Use the protocol with an AI/ML systems lens. Add task definition, datasets/splits/leakage controls, baselines, metrics, prompts/tool use/state/verifier design, ablations, compute, reproducibility, failure analysis, generalization limits, build-useful takeaways, and what not to overclaim.
```

### Batch triage prompt

```text
[LIST OF PAPERS / ABSTRACTS / LINKS]
Triage for interests in clinical pharmacy, AI/ML, RAG, parser design, agent harnesses, deterministic evaluation, scientific curation, and practical workflow implementation. For each source: title, type, one-line thesis, relevance, evidence maturity, priority, and whether it deserves full reference HTML. Do not over-rank loosely relevant or purely conceptual work.
```

## 12. Quality-control checklist

Pass condition: the finished file lets a reader understand the source’s claim, evidence, visual content, weaknesses, and practical relevance without immediately reopening the original.

Pre-output checks:

- Metadata complete: exact title, source type, date/version, authors/organization, identifier when available.
- Source ID/title match the requested source; no stale title, filename, headings, or unrelated content.
- Output target is correct: one self-contained HTML file unless another format was explicitly requested.
- Coverage manifest exists before narrative drafting and includes sections/headings, figures, tables, algorithms/workflows, appendices/supplements, visual strategy, coverage decision, and omissions.
- Sections preserved or omissions explicitly noted.
- Main-text figures/tables/workflows accounted for; appendix inclusion/omission justified when relevant.
- Each figure/table/workflow is represented as structured block, embedded crop/screenshot, or omitted with reason.
- Section summaries follow the two-paragraph default.
- Magnitudes preserved: sample sizes, denominators, rates, effect sizes, uncertainty, thresholds, metrics, benchmark deltas.
- Claims separated from appraisal; limitations appear near weakened claims and in final appraisal.
- Ratings were assigned after extraction, not before; ratings include score, rationale, evidence basis, limiting factor, and what would raise/lower the score.
- HTML is self-contained, readable, parseable, anchor-consistent, and free of placeholders, TODOs, stale headings, planning language, and internal citation syntax.
- Provenance includes source title, URL/identifier, version/date, evaluated file or URL when relevant, generation date, and caveats.
- Final response includes artifact link and brief note only unless the user requested citations, process details, or failure details.

Suggested mechanical QA:
- Verify final file exists and has nontrivial byte size.
- Parse HTML title.
- Confirm all table-of-contents anchors resolve.
- Count sections and structured visual/table/workflow blocks.
- Search for TODO, placeholder, “I will,” “I might,” “maybe,” stale filenames, and internal citation syntax.

Failure mode to prevent: a polished-looking abstract expansion that omits methods, quantitative results, visual evidence, limitations, implementation constraints, or appraisal basis.

### Minimal final appraisal block

```text
Verdict: Read first / Read soon / Skim deeply / Skim / Do not prioritize / Do not use for practice
Best use:
Do not use for:
Main strengths:
Main limitations:
Implementation / practice takeaways:
Confidence in appraisal: high / moderate / low, with reason.
```

## 13. Protocol maintenance rules

Future patch updates should not be appended as a new patch block unless they are temporary. Classify each patch as one of five types and integrate it into the relevant section:

| Patch type | Integrate into | Compression rule |
|---|---|---|
| Source/tooling rule | Source intake, routing, and grounding | Keep as a route/gate, not a narrative explanation. |
| Coverage or omission rule | Coverage manifest and inclusion gate | Add to manifest fields or inclusion rules. |
| Extraction/detail rule | Section or visual extraction sections | Convert to preserve/avoid language or compact template fields. |
| Appraisal/scoring rule | Rubric or domain modules | Add to scoring requirements, anchors, or red flags. |
| Tool-output hygiene rule | Source intake, routing, and grounding; QA checklist | Keep as a quiet-execution rule and pass/fail check; do not add long examples. |
| Output/QA rule | HTML specification or QA checklist | Add as a pass/fail check. |

Delete duplicate wording after integration. Keep invariants once, examples only where they prevent ambiguity, and prompts short enough to fit into routine task context. If a patch does not change behavior, convert it into a brief change note outside the operational protocol.
