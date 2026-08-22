# Scholar Acquire v0.4 Supported Architecture

## Product boundary

`acquire_one(PMID)` is the product. Batch mode is a mapping layer over the proven single-item path.

Python owns:

- requested/resolved identity binding and mismatch rejection;
- route order and feature flags;
- provider/route evidence;
- lawful-access context and provenance;
- PDF/JATS validation;
- SHA-256;
- SUCCESS / BLOCKED / EXHAUSTED / FAILED semantics;
- item manifests, receipts, and event journals;
- preferred payload selection;
- ATOM/SEA handoff;
- batch semantic-equivalence checking.

Transport owns only response acquisition. The preferred transport is ChatGPT-native materialization. A remote GitHub Actions shim is available only for exact URLs that Python/ChatGPT has already selected and whose bytes cannot otherwise be materialized.

## Single-item flow

```text
PMID
  -> exact identity resolution
  -> PMC route
  -> publisher OA route
  -> Unpaywall-assisted OA-location route
  -> institutional repository / accepted manuscript route
  -> materialized JATS/PDF OR evidence-backed terminal non-success
  -> Python validation
  -> Python SHA-256
  -> item manifest + receipt + event journal
  -> ATOM/SEA handoff (SUCCESS only)
```

A route error/barrier prevents a false EXHAUSTED claim. SUCCESS requires a real validated payload owned by a recorded successful route attempt. A browser page, abstract, URL, or search result is never SUCCESS.

## Payload preference

When available:

1. `article.xml` — structured JATS
2. `article.pdf` — PDF

The regression's ChatGPT-native successes were all PDF-only because the structured-machine endpoints encountered transport limitations. That limitation is why the narrow remote shim exists.

## Non-success manifests

BLOCKED, EXHAUSTED, and FAILED are first-class item results. Each now writes `terminal_manifest.json` with requested/resolved identity, actual route attempts, terminal evidence, receipt path, event-journal path, and no fabricated artifacts.

## Batch

Batch mode contains no acquisition policy. It invokes the same single-item replay/acquire path for each case and records stable item semantic signatures. The Prompt 5 regression demonstrated 10/10 equivalence.

## Remote transport boundary

The remote worker is intentionally dumb. It may return bytes/status/headers/provenance, but it cannot decide what those bytes mean. The existing Python runtime remains the acquisition brain.

## Known limitations after Prompt 5

- ChatGPT-native transport is unreliable for PMC browser pages that present anti-bot challenges.
- The host can reject otherwise valid XML responses based on MIME/materialization support.
- Unpaywall requires a transport/configuration path not reliably available in this host session.
- The GitHub Actions shim is implemented but was not deployed because no dedicated Acquisition Runtime GitHub repository is connected and repository creation is unavailable through the connector.
- The first ten-PMID regression therefore has no JATS+PDF SUCCESS item; all five successes are PDF-only.
- The new PMC dataset distribution structure becomes relevant on or after 2026-08-24; new integrations should use the current AWS/OAI-PMH documentation rather than legacy paths.
