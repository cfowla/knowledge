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

## Known superseded pattern

The 2026-08-27 Clinical Medicine & Pharmacy audit identified ten packets as reference-processing-only failures. That classification is no longer a defined repair queue. Those packets require **lifecycle re-evaluation under this rule**, with valid existing artifacts preserved.

The ADA 2026 workflow provides the clearest current pattern: bibliography entries are extracted and reconciled as parent-packet provenance infrastructure, while independent reading/processing of cited studies is separate downstream work and does not block parent lifecycle completion.
