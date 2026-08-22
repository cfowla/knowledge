# Acquisition Runtime v0.4.3 repair strategy

## Purpose

The current v0.4.2 build proved several useful pieces, but it did not complete the original five-prompt sequence. The repair should preserve the parts that work and correct the product boundary before adding more acquisition breadth.

The main problems to fix are concrete:

- `acquire_one()` currently accepts a prepared specification that already contains resolved identity, route outcomes, local artifact paths, and terminal-state information. That is evidence replay and finalization, not a complete acquisition controller.
- Python does not yet own enough of provider strategy, OA policy, identity resolution, and terminal-state assignment.
- `EXHAUSTED` can be reached from route errors or skipped routes. Transport uncertainty must make exhaustion impossible.
- PMC JATS/PDF and Unpaywall have code paths but no live successful route proof.
- The original strategy deadlocked by requiring PMC JATS before Prompt 5 while postponing the remote-transport decision until Prompt 5.
- The ten-PMID regression and batch comparison reused pre-materialized artifacts and caller-supplied metrics. They proved deterministic finalization more strongly than acquisition.
- The evidence package did not preserve enough batch item output to independently recompute every equivalence claim.

Freeze v0.4.2 as a diagnostic reference. Do not delete it or rewrite its reports. Build the repair as a new v0.4.3 development line.

## Repair rules

Use the five prompts below in order. Stop when a hard gate fails.

The production path must begin with an identifier and acquisition configuration. Host tools may return observations, locations, response bytes, status codes, headers, and provenance. They must not choose the terminal state or tell Python that a provider is exhausted.

Keep replay support, but name it honestly. A replay or fixture API may accept prepared identities, artifact paths, and route histories. Production `acquire_one()` may not.

A route earns supported status only after a real article succeeds through that route in the repaired production path. Unit tests do not count as route proof.

Runtime-generated evidence outranks prose reports. Metrics must come from journals, receipts, transport records, and manifests rather than hand-entered counters.

The remote worker is allowed before route proof because transport was the blocker in v0.4.2. It remains transport-only. Python keeps acquisition policy and scholarly decisions.

---

## Prompt 1 of 5: repair the product boundary and terminal-state contract

Work from the current v0.4.2 source. Preserve v0.3.1 and v0.4.2 as recoverable reference builds. Create a v0.4.3 development line.

The first task is to separate real acquisition from replay.

### Production API

Replace the current production use of a prepared `AcquisitionSpec` with an acquisition entry point that starts from only an identifier plus configuration. The exact type names may differ, but the public contract should be equivalent to:

```python
acquire_one(
    identifier=Identifier.pmid("12345678"),
    config=AcquisitionConfig(...),
    root=Path(...),
    host=HostAdapter(...),
    transports=TransportRegistry(...),
) -> AcquisitionResult
```

Python must own:

- normalization of the requested identifier;
- resolution and preservation of PMID, PMCID, DOI, normalized title, and useful journal/year evidence;
- provider ordering and route feature state;
- lawful/OA evidence admission rules;
- identity verification;
- PDF/JATS validation;
- SHA-256;
- SUCCESS, BLOCKED, EXHAUSTED, and FAILED assignment;
- receipts, event journals, manifests, provenance, and ATOM/SEA handoff construction.

The host may satisfy explicit requests from Python and return facts. Examples include search observations, trusted metadata, discovered locations, or transport responses. Python decides what those facts mean.

### Replay API

Retain the current prepared-spec workflow for tests and evidence reproduction, but rename or isolate it as something such as `AcquisitionReplaySpec` and `replay_acquisition()`. It may not be the function used to claim live acquisition success.

A production request must not accept these caller-controlled fields:

- final terminal state;
- provider exhaustion declaration;
- pre-decided route success/failure;
- trusted resolved identity without an evidence source;
- successful artifact admission without provenance and identity checks.

### Terminal-state repair

Rewrite exhaustion logic so `EXHAUSTED` is possible only when every enabled route has definitive negative evidence.

The following must prohibit EXHAUSTED:

- transport error;
- timeout;
- CAPTCHA or anti-bot challenge;
- response not materializable;
- unknown result;
- search result absence without definitive provider evidence;
- skipped route unless policy proves the route is inapplicable;
- unexecuted route.

Those conditions should resolve to BLOCKED, FAILED, or continued acquisition as appropriate.

Add tests that try to force EXHAUSTED using only errors, skipped routes, unknown responses, and transport failures. All must fail closed.

### Route capability registry

Replace simple enabled booleans with an explicit capability status or equivalent policy. At minimum distinguish:

- `supported`;
- `experimental`;
- `disabled`.

At the start of v0.4.3, do not claim PMC or Unpaywall as supported. Existing publisher and repository proofs may be retained as historical evidence, but the repaired production controller must re-earn route support later in this sequence.

### Required real check

Use one previously acquired lawful OA PDF to prove that the repaired production path can start from a PMID, request or accept host observations through the new observation contract, admit the real file, verify identity, validate it, hash it, and return SUCCESS without a caller-supplied terminal state.

Do not add new provider breadth in this prompt.

### Hard exit gate

1. v0.3.1 and v0.4.2 remain recoverable and unchanged.
2. Production `acquire_one()` begins with an identifier and configuration, not a replay specification.
3. Replay is visibly separated from live acquisition.
4. Python assigns terminal states without caller input.
5. EXHAUSTED cannot be produced from transport errors, unknown results, or incomplete route coverage.
6. One real existing OA PDF passes through the repaired production contract and returns SUCCESS.
7. Receipts, events, identity evidence, artifact hash, and manifest are preserved.
8. Tests document the new contract and pass.

Return the exact source changes, API changes, tests, the real check evidence, and any migration notes. Do not proceed to Prompt 2 if any gate fails.

---

## Prompt 2 of 5: integrate transport before re-earning providers

Starting from the repaired v0.4.3 product boundary, make transport a replaceable execution service rather than an acquisition decision-maker.

This prompt fixes the deadlock in the original strategy. Remote transport is allowed now because v0.4.2 already demonstrated that valid PMC and Unpaywall routes can fail solely because ChatGPT-native tooling cannot materialize their response bytes.

### Transport contract

Define one transport request and response contract used by both ChatGPT-native materialization and the remote worker.

A request should contain only transport facts needed to execute an already-authorized operation, such as:

- request/correlation ID;
- URL;
- GET or HEAD;
- allowed headers;
- timeout;
- expected media type when useful;
- source route and provenance context supplied by Python.

A response should contain only low-level results:

- request/correlation ID;
- requested and final URL;
- status;
- response headers;
- exact response bytes or a materialized file reference;
- byte count;
- transport checksum;
- timestamps and elapsed time;
- transport error information.

The worker must not resolve identifiers, choose providers, decide whether an article is OA, validate scholarly content, assign terminal states, or write acquisition manifests.

### Runtime integration

Wire the transport response back into the same `acquire_one()` state machine. The flow should be real:

```text
acquire_one(PMID)
  -> Python selects a route/action
  -> Python emits a transport request
  -> preferred transport executes it
  -> response is correlated and ingested
  -> Python evaluates identity, policy, media type, and validation
  -> acquisition continues or terminates
```

Use ChatGPT-native transport first when it can return exact bytes. Use the remote worker when native transport cannot materialize an otherwise valid request.

Do not create separate acquisition logic inside the worker.

### Remote execution proof

Deploy or otherwise execute the transport-only worker in a real remote environment. Prefer a dedicated GitHub Actions repository or workflow. If no remote execution target is available, stop with BLOCKED and preserve the worker package. Do not pretend local contract tests prove remote transport.

Run at least two real transport checks:

1. one ordinary public PDF or XML that both native and remote transport can retrieve, so response parity can be checked;
2. one route that v0.4.2 could identify but could not materialize natively, preferably a PMC JATS/XML object.

For each check, preserve request, response metadata, byte count, checksum, and correlation evidence.

### Hard exit gate

1. A single transport request/response contract exists for native and remote execution.
2. The worker contains no scholarly/provider intelligence.
3. `acquire_one()` can suspend for transport and resume from a correlated response.
4. At least one real remote GET returns materialized bytes through the integrated runtime.
5. At least one previously blocked machine endpoint is successfully transported, preferably PMC JATS/XML.
6. Python validates and hashes the returned payload independently of the transport checksum.
7. Transport failure remains BLOCKED, not EXHAUSTED.
8. All request/response evidence is preserved and replayable.

Return the transport contract, deployment/execution evidence, checksums, tests, and any remaining host limitations. Do not proceed to Prompt 3 until the remote path is live-proven.

---

## Prompt 3 of 5: re-earn JATS and every provider route one at a time

Do not restore a generalized ladder all at once. Use the repaired `acquire_one()` controller and the integrated transport layer from Prompts 1 and 2.

Test one route at a time. A route remains experimental until its positive real-world gate passes.

### Route A: PMC structured full text and PDF

Choose one PMID with a PMCID and lawful PMC OA distribution.

Required result:

- resolve the exact identity in Python;
- retrieve and materialize real JATS/XML through the PMC route;
- validate JATS;
- hash it;
- retain a real PDF from the same article when available;
- verify both payloads against the same article identity;
- write route-specific provenance and hashes to the manifest;
- set `article.xml` as preferred ATOM/SEA payload and `article.pdf` as secondary.

Add a negative PMC case that produces BLOCKED or a definitive non-success without false exhaustion.

Do not enable the next route until this succeeds.

### Route B: publisher-hosted OA

Choose a publisher-hosted OA article that does not depend on the PMC payload route. Avoid using only Frontiers as proof. Use a publisher family that broadens the transport evidence.

Acquire a real published full-text artifact, verify identity, validate, hash, manifest, and return SUCCESS through the publisher route.

Add one publisher negative/blocked case.

### Route C: Unpaywall-assisted OA location

Choose an article where Unpaywall materially contributes the OA location. Direct publisher discovery that happens to match an Unpaywall record does not count.

Python should request the Unpaywall lookup, evaluate the returned OA-location metadata, select an allowed location according to policy, retrieve the full text through the normal transport contract, and complete validation, identity, hashing, provenance, and manifest generation.

Record both the Unpaywall discovery provenance and the final payload provenance.

Add one Unpaywall negative case, such as no usable OA location or transport failure. Preserve BLOCKED versus definitive exhaustion semantics.

Do not enable the repository route until this succeeds.

### Route D: institutional repository or accepted manuscript

Choose an article whose successful acquisition depends on a repository or accepted-manuscript location rather than a direct publisher OA payload.

Record manuscript version, repository source, license/access basis when available, identity evidence, validation, hash, and manifest.

Add one repository negative/blocked case.

### Capability promotion

After each real positive succeeds, promote only that route from experimental to supported. Store the proof article, run ID, manifest path, artifact hashes, runtime version, and proof date in a machine-readable capability registry.

### Hard exit gate

1. At least one real PMC JATS acquisition succeeds through the repaired production controller.
2. The same PMC identity retains PDF when available.
3. PMC, publisher OA, Unpaywall-assisted OA, and repository routes each have an independent real positive acquisition.
4. Each route has at least one negative or blocked acceptance case.
5. Every success has exact identity, lawful provenance, validation, SHA-256, receipt, journal, and manifest.
6. No route is marked supported without its real proof record.
7. `acquire_one()` still runs one item without batch machinery.
8. No success or exhaustion state is supplied by the host or test data.

Return a route-proof matrix with article IDs, source routes, artifact hashes, negative cases, and capability-registry changes. Do not proceed to Prompt 4 if any route remains unproven.

---

## Prompt 4 of 5: run a clean ten-PMID individual regression and prove ATOM/SEA handoff

Now test the repaired acquisition product at realistic breadth. Do not use batch mode in this prompt.

Build a fixed heterogeneous set of ten PMIDs after all routes in Prompt 3 are supported. Freeze the set before the first run.

The set must include:

- at least two PMC OA articles, including one with JATS plus PDF;
- at least two publisher-hosted OA articles from different publisher families;
- at least one case where Unpaywall supplies the usable OA location;
- at least one institutional repository or accepted-manuscript case;
- at least one article expected to be difficult, blocked, or lawfully unavailable;
- enough diversity that no single publisher accounts for more than two successful publisher-route cases.

### Execution rule

Run all ten from clean individual roots through production `acquire_one(PMID, config, ...)`.

Do not preload:

- terminal states;
- resolved identities without evidence;
- route outcomes;
- materialized payload paths;
- hand-entered discovery-action counts.

Normal host observations and transport responses must enter through the production request/response contracts.

### Per-item evidence

Require:

- requested and resolved identity with evidence;
- provider/route decisions generated by Python;
- host and transport actions actually executed;
- materialized payloads or evidence-backed non-success state;
- PDF/JATS validation as applicable;
- SHA-256 for every successful payload;
- source, version, license/access provenance when available;
- run receipt;
- append-only event journal;
- manifest for success and non-success states;
- correct terminal state.

### Metrics

Compute metrics from runtime evidence rather than caller-supplied fields:

- successful full-text acquisition rate;
- identity mismatch rate, target 0%;
- false-success rate, required 0%;
- BLOCKED rate and causes;
- EXHAUSTED rate and evidence basis;
- route-specific success rate;
- native versus remote transport use;
- median host/discovery actions per PMID from journals;
- median transport actions per PMID;
- median end-to-end elapsed time when timestamps allow it;
- median Python processing time separately;
- proportion of successes with JATS plus PDF versus PDF only;
- manifest/provenance completeness.

### ATOM/SEA handoff

Only after all ten individual acquisitions finish, hand every success to the ATOM/SEA input interface.

For each success, reopen the handed-off payload, revalidate its format, recompute SHA-256, verify the manifest link, and preserve a handoff receipt.

At least one handoff must prove the intended structured preference:

```text
preferred = article.xml
secondary = article.pdf
```

when both exist.

### Evidence package

Build a self-contained evidence package with relative or relocatable references. An independent verifier must be able to recompute artifact hashes and inspect item states without relying on the original `/mnt/data/...` paths.

### Hard exit gate

1. Ten fixed heterogeneous PMIDs finish through production `acquire_one()`.
2. Identity mismatch rate is 0%.
3. False-success rate is 0%.
4. Every terminal state is supported by item evidence.
5. Every success has a reusable ATOM/SEA handoff.
6. At least one real JATS plus PDF handoff succeeds with JATS preferred.
7. Metrics are computed from recorded events and transport evidence.
8. The evidence archive is self-contained and independently verifiable.

Return the ten-item report, metrics, handoff proof, hashes, and evidence-verifier results. Do not add batching until this gate passes.

---

## Prompt 5 of 5: restore batch mapping, prove equivalence, and publish the supported architecture

Batching is the last repair step. It must wrap the production `acquire_one()` path without adding provider logic or item-level policy.

Use the exact frozen ten-PMID set and acquisition configuration from Prompt 4.

### Clean batch run

Run the batch in a new root. Each item must begin from its identifier and normal configuration. Do not point batch items at the individual run's already-materialized files, route histories, terminal states, or prepared replay specifications.

For the primary equivalence run, use an empty or controlled cache so the batch test does not pass merely because individual artifacts are reused. A separate warm-cache benchmark may be run afterward as an optimization test.

### Equivalence comparison

Compute item semantic fingerprints from preserved individual and batch outputs. At minimum compare:

- requested/resolved identifiers;
- final terminal state and reason code;
- provider/route sequence and definitive outcomes;
- artifact format, source route, source URL, version, license/access basis, and SHA-256;
- identity decision;
- ATOM/SEA preferred and secondary payload hashes;
- BLOCKED/EXHAUSTED semantics.

Exclude only values that should differ by execution, such as run IDs, timestamps, and local output paths.

The independent verifier must recompute the fingerprints from the preserved item manifests and journals. It may not trust a summary field that says equivalence passed.

### Batch evidence preservation

Preserve:

- batch receipt;
- batch event journal;
- batch manifest;
- all ten batch item directories or relocatable equivalents;
- all item manifests and journals;
- equivalence report;
- independent verifier output.

### Optimization report

After the cold equivalence run passes, measure optional optimizations without changing acquisition semantics:

- warm-cache performance;
- native versus remote transport frequency;
- route-level latency;
- tool/discovery action counts;
- avoidable repeated lookups;
- payload reuse opportunities.

Do not add retries, concurrency, or cache complexity unless a measured bottleneck justifies it.

### Final support declaration

Publish the v0.4.3 architecture and support matrix from machine-readable route proof records.

A route may be called supported only if:

1. it passed the real route proof in Prompt 3;
2. it appeared successfully in the Prompt 4 regression or has an explicit reason why the ten-item set did not exercise it;
3. its transport dependency is available in the deployed environment;
4. its proof artifacts remain verifiable.

Document remaining limitations plainly.

### Hard exit gate

1. Batch maps the production `acquire_one()` function and adds no item-level acquisition policy.
2. The same ten identifiers run from clean batch inputs.
3. Individual versus batch semantic equivalence is 10/10.
4. An independent verifier recomputes, rather than trusts, equivalence.
5. All individual and batch evidence is preserved and relocatable.
6. False-success rate remains 0%.
7. ATOM/SEA handoff semantics remain unchanged in batch mode.
8. The final architecture and supported-route matrix match the actual proof record.
9. Any optimization added after equivalence has measured evidence and does not alter item semantics.

Return the batch report, independently recomputed equivalence results, optimization measurements, final support matrix, remaining limitations, and release/build provenance.

---

## What v0.4.3 should mean when these five prompts pass

A successful v0.4.3 release should support this claim without qualification:

```text
PMID
  -> Python resolves identity and selects the next lawful route
  -> Python emits host/discovery/transport work
  -> ChatGPT-native or remote transport returns facts and bytes
  -> Python decides policy and identity
  -> Python validates and hashes the payload
  -> Python assigns the terminal state
  -> Python writes receipts, journal, provenance, and manifest
  -> successful payloads become reusable ATOM/SEA inputs
  -> batch mode maps the same acquire_one() behavior
```

The release should not need a prepared object that already knows the answer.

## Files to preserve from the current project

Do not delete or overwrite these reference materials while repairing the build:

- `V0.4_VERTICAL_SLICE_5_PROMPT_STRATEGY.md`
- v0.3.1 frozen source, contracts, build provenance, and test evidence
- v0.4.2 source and Prompt 5 evidence bundle
- `PROMPT5_REGRESSION_REPORT.md`
- `V0_4_FINAL_ARCHITECTURE.md`
- `REMOTE_TRANSPORT_DECISION.md`
- v0.4.2 build provenance and portable release archive

Treat them as evidence of what was tried, including the parts that did not satisfy the original gates.
