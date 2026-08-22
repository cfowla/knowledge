# scholar-acquire-chatgpt v0.4.2 Final Supported Architecture

## Product boundary

`acquire_one()` is the acquisition product. Batch mode is only a map over this function and must never change item semantics.

### Python acquisition brain

Python owns:

- requested/resolved article identity and fail-closed identity admission;
- route feature flags and provider strategy;
- lawful/OA evidence admission policy;
- PDF/JATS validation and JATS `<article>` normalization;
- SHA-256 integrity;
- SUCCESS / BLOCKED / EXHAUSTED / FAILED semantics;
- run receipts, append-only event journals, manifests, and provenance;
- ATOM/SEA handoff construction;
- batch item semantics.

### Transport adapters

Transport owns only movement of bytes and low-level response facts.

1. **ChatGPT-native transport** is preferred when it can materialize an exact lawful payload directly.
2. **Remote worker transport** is used when the current host cannot return raw bytes for an otherwise valid route. It executes a pre-authorized HTTP(S) GET/HEAD and returns bytes/status/headers/provenance. It makes no scholarly decisions.

## Route support matrix after Prompt 5

| Route | Code path | Real route proof | Current declaration |
|---|---|---|---|
| Publisher OA | implemented | 6 real PDF successes | supported with ChatGPT-native transport |
| Institutional repository / accepted-manuscript route | implemented | UC eScholarship real PDF success | supported with ChatGPT-native transport for materializable locations |
| PMC structured JATS/PDF | implemented admission/validation path; current PMC dataset location understood | lawful locations proven, byte materialization blocked | requires remote transport before live-support declaration |
| Unpaywall-assisted OA location | isolated adapter/attempt semantics present | host transport blocked; no real success | requires remote transport before live-support declaration |

## Payload ranking

When both validated forms exist:

1. `article.xml` (normalized JATS) is the preferred ATOM/SEA payload.
2. `article.pdf` is the secondary payload.

When only a valid PDF is acquired, `article.pdf` is a valid reusable handoff input.

## Terminal-state semantics

- **SUCCESS:** at least one exact-identity, lawful, locally materialized full-text payload passes validation and SHA-256 verification.
- **BLOCKED:** acquisition could potentially continue, but host/transport/tool limitations prevent a required action. BLOCKED is not provider exhaustion.
- **EXHAUSTED:** every enabled lawful route has been actually attempted with definitive negative evidence; transport uncertainty prohibits EXHAUSTED.
- **FAILED:** runtime/protocol/validation/identity failure where provider exhaustion is not established.

## 2026 PMC transport requirement

PMC's current Cloud Service organizes article versions under the world-readable `pmc-oa-opendata` S3 bucket and exposes per-version JSON metadata plus JATS XML, PDF when available, and other assets. PMC announced removal of legacy dataset distribution paths on or after August 24, 2026. The remote worker should therefore use the current per-version Cloud Service objects rather than restore deprecated legacy fetch assumptions.

## Remote worker contract

Input fields:

- `request_id`
- absolute `http`/`https` `url`
- method `GET` or `HEAD`
- optional headers
- optional timeout

Output fields:

- same `request_id`
- `transport_state`
- requested/final URL
- HTTP status
- response headers
- exact body bytes encoded as base64
- byte count
- body SHA-256 (transport checksum, not an acquisition decision)
- start/retrieval timestamps and elapsed milliseconds
- transport error details when no response was obtained

The acquisition runtime must correlate this response to its pending request before ingest. The worker must not resolve PMIDs/DOIs, select providers, decide OA/license suitability, validate scholarly content, assign terminal states, or write acquisition manifests.

## Remaining limitations

- No live real-JATS success yet because ChatGPT-native transport could not materialize the known PMC XML object during the regression.
- No live Unpaywall-assisted success yet for the same transport reason.
- End-to-end network latency was not consistently measurable; reported runtime timing covers Python execution after host evidence/payload preparation.
- The GitHub Actions transport workflow is implemented and locally contract-tested, but it was not deployed/executed in a dedicated Acquisition Runtime GitHub repository because no such repository is currently connected. The durable v0.4 source remains in the Drive project tree.
