# v0.4.3 Prompt 1 repair report

## Result

Prompt 1 passes all eight hard exit gates.

The repair starts from the preserved v0.4.2 source archive. No v0.3.1 or v0.4.2 Drive artifact was overwritten. The new build identifies itself as `0.4.3` with build ID `scholar-acquire-chatgpt-0.4.3-repair-prompt1`.

## Product boundary

Production `acquire_one()` now accepts `identifier`, `config`, `root`, `host`, and optional `transports`. It does not accept a prepared acquisition specification.

The old prepared workflow is now `AcquisitionReplaySpec` plus `replay_acquisition()`. Batch code from v0.4.2 was moved onto the replay path because production batching is not restored until Prompt 5.

Python now emits host requests, validates correlation, resolves the article identity from evidence-bearing observations, chooses route order from the capability registry, admits lawful OA artifacts, verifies identity, validates PDF or JATS, computes SHA-256, and assigns the terminal state.

## Terminal-state repair

The previous `mark_exhausted()` accepted any attempt outcome, including `error` and `skipped`, as route coverage. v0.4.3 requires at least one `miss` carrying `definitive_negative=true` for every enabled route.

The Prompt 1 tests explicitly run transport error, timeout, CAPTCHA, response-not-materializable, unknown, search-absence, and skipped observations. Every case returns `BLOCKED` with `provider_exhaustion_confirmed=false`. A separate definitive-negative case returns `EXHAUSTED` only when the sole enabled route has evidence marked definitive.

## Capability registry

Production route policy now uses `RouteCapabilityRegistry` with three states: `supported`, `experimental`, and `disabled`. All four routes start v0.4.3 as experimental. No Prompt 1 test or real check promotes a route to supported.

## Real check

PMID `24782981` used the lawful OA PDF preserved in the v0.4.2 Prompt 5 evidence package.

Resolved identity:

- PMID `24782981`
- PMCID `PMC3995050`
- DOI `10.3389/fonc.2014.00064`
- Title `Targeting PI3K/Akt/mTOR signaling in cancer`
- Journal `Frontiers in Oncology`
- Year `2014`

The host supplied the preserved v0.4.2 manifest as identity and provenance evidence and supplied the preserved PDF as a materialized artifact observation. The caller did not supply a terminal state. Publisher OA remained `experimental` during the check.

Python matched the PDF on DOI and title. PDF validation passed. The copied output is 810,232 bytes. SHA-256 is `54465e3c056b86551d8c5d865b0685d01a5f4fa2c11bc705a479768b3efc63cb`, identical to the preserved v0.4.2 artifact hash. The run ended in `SUCCESS` and wrote a run receipt, append-only event journal, identity report, manifest, terminal outcome, and ATOM/SEA handoff.

## Tests

`pytest -q` result: `13 passed`.

The contract tests cover the new public signature, replay separation, initial capability state, fail-closed exhaustion for uncertain or blocked observations, definitive-negative exhaustion, and the no-enabled-route case.

## Hard exit gate

1. PASS. v0.3.1 and v0.4.2 remain separate, recoverable Drive artifacts. This work did not update them.
2. PASS. Production `acquire_one()` starts from identifier and configuration.
3. PASS. Prepared evidence is under `AcquisitionReplaySpec` and `replay_acquisition()`.
4. PASS. Python assigns SUCCESS, BLOCKED, EXHAUSTED, or FAILED. No production request field can set a terminal state.
5. PASS. Transport errors, unknown results, skipped routes, search absence, and incomplete coverage cannot produce EXHAUSTED.
6. PASS. The real OA PDF for PMID 24782981 returned SUCCESS through the repaired production path.
7. PASS. Receipt, event journal, identity evidence, artifact hash, manifest, and ATOM/SEA handoff are present.
8. PASS. Thirteen Prompt 1 tests pass against the verified 0.4.3 build.

## Discrepancies and boundaries

The Prompt 1 API example is identifier-generic, but this repaired controller still restricts the live entry point to PMID. The hard gate requires a PMID-starting production path, so this does not block Prompt 1. DOI and PMCID live entry points remain unfinished.

`TransportRegistry` is present in the public contract but has no execution logic yet. Prompt 2 explicitly owns transport integration and remote execution proof.

The required real check reuses a previously acquired PDF, as the prompt instructs. It does not prove fresh publisher transport. It proves the repaired product boundary, observation flow, evidence admission, identity check, validation, hashing, and Python-owned terminal state.

No provider route is marked supported. Route promotion remains gated on Prompt 3 real route proofs.
