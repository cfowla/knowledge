# Clinical Packet Failure-Gate Rule

**Effective:** 2026-08-27  
**Scope:** Clinical Medicine & Pharmacy publication packets  
**Status:** Governing interpretation for failure-gate classification and lifecycle review

## Authority and precedence

Use this rule when determining whether a Clinical Medicine & Pharmacy packet fails its publication gate. It supersedes older packet reports, reference queues, audit notes, or lifecycle fields **only where those artifacts treat unresolved downstream cited-publication processing as a blocking parent-packet requirement**.

Historical processing reports remain valid evidence for source integrity, ATOM validation, SEA/SEA-QA, coverage/reconciliation, provenance, and other packet-specific findings. Do not rewrite history merely to remove an obsolete lifecycle interpretation.

## Blocking parent-packet gates

A parent publication may fail when the first unsatisfied requirement is one of the following:

1. **Source integrity** — wrong, incomplete, unusable, mismatched, or insufficient primary source or required supplement.
2. **ATOM validation** — structural, schema, sufficiency, identity, anchoring, semantic, or provenance failure under the current applicable validators.
3. **SEA / SEA-QA** — missing, mismatched, materially incomplete, semantically incorrect, or failing the current SEA QA gate.
4. **Coverage / reconciliation / crosswalk** — required figures, tables, workflows, recommendations, sections, supplements, or ATOM↔SEA relationships are not reconciled when applicable.
5. **Bibliography extraction / reconciliation** — the parent publication's bibliography or reference set is missing, materially incomplete, or not reconciled to the source when the workflow requires it.
6. **Output completeness** — a required parent-packet artifact is absent or incomplete.
7. **Provenance / identity** — source hash, publication identity, source version, artifact identity, or traceability cannot be established.
8. **Another explicitly named packet-level gate** required by the current authoritative protocol.

Classify the packet by the **first actual unsatisfied parent-level requirement**, not by the presence of an open downstream work queue.

## Nonblocking cited-publication work

The following do **not**, by themselves, fail the parent publication:

- unchecked entries in a reference task queue;
- a nonzero unresolved-reference or unresolved-citation count;
- cited publications that have not yet been independently acquired;
- cited publications that have not received their own ATOM, SEA, QA, or lifecycle disposition;
- downstream citation-bank or literature-development work that remains open;
- `ready_to_move_to_processed=false` or equivalent lifecycle output when the only reason is unresolved downstream cited-publication work.

A bibliography queue may therefore remain open after the parent packet passes. Track that work separately as cited-publication follow-up.

## Required audit behavior

When reviewing a clinical packet:

1. Verify the exact source and packet identity.
2. Read the current processing report and validation evidence, but do not accept its lifecycle conclusion uncritically if it predates or conflicts with this rule.
3. Verify source integrity, ATOM validation, SEA/SEA-QA, coverage/crosswalk when applicable, bibliography extraction/reconciliation, output completeness, and provenance.
4. If all applicable parent-level gates pass, classify the packet as parent-gate **PASS** even when downstream cited-publication work remains open.
5. If an older report says FAIL only because references remain unresolved, treat that failure classification as superseded. Preserve passing artifacts and re-evaluate lifecycle promotion; do not regenerate ATOM/SEA and do not process every cited paper merely to make the parent pass.
6. If several packets show the same implementation-derived false failure, treat it as a shared implementation issue rather than ten independent packet repairs.

## Bounded discovery and forward-production rule

Artifact discovery is a prewalk step. It must end.

After confirming the exact packet and source identity:

1. Search the packet, the expected output locations, and reasonable identity or basename variants in one bounded pass.
2. If a required artifact exists, inspect it and preserve it when it already passes.
3. If a required artifact family is absent after that bounded pass, record it as `CONFIRMED ABSENT`. Do not search for the same artifact family again unless new identity evidence, a new plausible location, or a conflicting artifact appears.
4. Treat confirmed absence as evidence that a required production or output-completeness requirement is unsatisfied. A missing ATOM is an output-completeness problem until an ATOM exists to validate. A missing SEA is an output-completeness problem and requires SEA production.
5. Move immediately to the earliest missing required artifact in the current authoritative dependency sequence. Generate it, run its required validation or QA, then continue downstream. Preserve every upstream artifact that already passes.
6. Do not jump to a processing report or lifecycle decision while an earlier required artifact is absent.
7. Discovery without production is incomplete work unless a real blocker prevents safe generation. Valid blockers include unusable or missing primary source material, unresolved publication identity, unavailable governing protocol or validator when the protocol requires it, or another explicitly named packet-level blocker.

Examples:

- Source usable, ATOM absent: generate the ATOM, then run ATOM validation. Do not perform another ATOM existence search.
- ATOM present and passing, SEA absent: preserve the ATOM and generate SEA, then run SEA-QA.
- ATOM, validation, and SEA all absent: start with the earliest required upstream artifact under the current protocol and work forward. Do not spend another pass proving that the outputs are absent.

`NO COMPLETION EVIDENCE` is therefore a temporary audit classification. Once a bounded packet-level search proves that required outputs are absent, the execution state must change to `GENERATION REQUIRED` or to a specific blocker. It must not remain in repeated evidence-establishment mode.

## Known superseded pattern

The 2026-08-27 Clinical Medicine & Pharmacy audit identified ten packets as reference-processing-only failures. That classification is no longer a defined repair queue. Those packets require **lifecycle re-evaluation under this rule**, with valid existing artifacts preserved.

The ADA 2026 workflow provides the clearest current pattern: bibliography entries are extracted and reconciled as parent-packet provenance infrastructure, while independent reading/processing of cited studies is separate downstream work and does not block parent lifecycle completion.
