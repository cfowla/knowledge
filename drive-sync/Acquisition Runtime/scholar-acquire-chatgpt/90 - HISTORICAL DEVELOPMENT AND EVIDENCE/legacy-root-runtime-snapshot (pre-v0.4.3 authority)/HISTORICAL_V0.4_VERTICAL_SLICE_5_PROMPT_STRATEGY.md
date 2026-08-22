# Acquisition Runtime v0.4 — Five-Prompt Vertical-Slice Strategy

## Strategy

Use these prompts sequentially. Each prompt has a hard exit gate. Do not run the next prompt until the current gate passes. The objective is to earn complexity from one real acquisition rather than continue hardening the generalized transport layer.

The v0.3.1 repository remains frozen as the controller reference implementation. The v0.4 line may reuse its validation, hashing, provenance, terminal-state semantics, artifact import, identifier/location injection, receipts, journals, and ATOM/SEA handoff concepts, but it must not depend on arbitrary raw-HTTP fetches inside ChatGPT.

---

## Prompt 1 of 5 — Freeze v0.3.1 and define the v0.4 vertical-slice contract

You are implementing the next version of the Scholarly Acquisition Runtime. Work directly from the current repository. Do not replace or delete v0.3.1.

First, freeze the current implementation as the v0.3.1 reference state and create a new v0.4 vertical-slice development line. The purpose of v0.4 is not to generalize acquisition. Its first purpose is to prove that ChatGPT can discover and materialize one lawful full-text artifact and that Python can then validate, hash, record provenance, and return a correct terminal state.

Preserve these concepts from v0.3.1:
- SHA-256 integrity and artifact provenance
- SUCCESS / EXHAUSTED / BLOCKED / FAILED
- BLOCKED != EXHAUSTED
- PDF/JATS validation
- source/version/license metadata
- session receipts and event journals
- artifact import
- resolved PMID/PMCID/DOI injection
- tool-discovered publisher/repository location injection
- ATOM/SEA handoff interfaces

Remove or disable these from the v0.4 critical path for now:
- arbitrary API URL fetching
- batch execution
- retry orchestration
- cache sophistication
- automatic provider exhaustion
- Unpaywall
- institutional repository discovery
- publisher crawling
- multiple artifact formats beyond the first PDF path
- synthetic controller acceptance as the primary success criterion

Revise the protocol and acceptance contract so that a lawful artifact discovered and materialized by ChatGPT may be admitted through runtime.import_artifact() when source URL, discovery provenance, requested identifier, and acquisition context are recorded. Python remains authoritative for validation, hashing, manifest generation, identity checks once implemented, and terminal-state assignment. Do not silently preserve a contract that requires every host retrieval to originate as an ExternalFetchRequest if that rule would make the new vertical slice impossible.

Create or update the minimum documentation/tests needed to make this contract explicit. Preserve the old v0.3.1 contract as historical reference rather than rewriting history.

Hard exit gate:
1. v0.3.1 remains recoverable and unchanged as a reference.
2. v0.4 has an explicit ChatGPT-native artifact-import contract.
3. batch/provider orchestration is disabled from the v0.4 acceptance path.
4. the new primary acceptance criterion is: PMID -> real lawful OA PDF -> runtime import -> PDF validation -> SHA-256 -> manifest -> SUCCESS.
5. existing integrity/provenance/terminal-state tests still pass or are deliberately migrated with documented reasons.

Return the exact files changed, tests run, test results, and the new acceptance contract. Do not implement provider fallbacks yet and do not proceed to Prompt 2 work.

---

## Prompt 2 of 5 — Prove one real PMID end to end

Execute the v0.4 vertical slice on exactly one PMID that you first verify is a known PMC-open-access article with a lawful PDF. This is a real acquisition test, not a synthetic controller test.

Required flow:
PMID -> ChatGPT scholarly lookup -> exact article identification -> lawful OA PDF location -> materialize the actual PDF -> runtime.import_artifact() -> PDF validation -> SHA-256 -> acquisition manifest -> SUCCESS.

Use ChatGPT web/search/navigation capabilities for discovery and materialization. Do not require the Python runtime to perform arbitrary outbound HTTP. Do not use Europe PMC API orchestration, Unpaywall, publisher fallback logic, institutional repository discovery, retries, batching, JATS, or ATOM/SEA in this prompt.

The runtime must record at minimum:
- requested PMID
- article title if known
- source URL
- discovery method/source
- access/version/license metadata when available
- local artifact path
- PDF validation result
- artifact byte size
- SHA-256
- run/session ID
- terminal state
- manifest path

Do not claim SUCCESS unless a real PDF file is materialized and the runtime validates and hashes that file. A browser-visible abstract page, HTML article page, search result, citation, or inaccessible PDF URL does not count. If the host can identify a lawful PDF but cannot materialize the file, return BLOCKED with evidence rather than SUCCESS or EXHAUSTED.

Hard exit gate:
1. exactly one real PMID is tested;
2. a real PDF exists on disk;
3. the PDF passes runtime validation;
4. SHA-256 is recorded;
5. the manifest points to that artifact and its provenance;
6. the runtime itself returns SUCCESS;
7. the run produces reproducible evidence sufficient for an independent reviewer to verify what happened.

If any gate fails, stop and diagnose only that failure. Do not add providers or generalized transport. Do not proceed to Prompt 3 work.

---

## Prompt 3 of 5 — Add identity verification and test three deliberately different papers

Starting from the successful one-PMID vertical slice, implement artifact identity verification before expanding acquisition breadth.

The runtime must resolve and preserve the strongest available identity tuple for the requested article:
- PMID
- PMCID when available
- DOI when available
- normalized title
- journal/year when useful for disambiguation

Add an identity-verification layer that determines whether the materialized artifact actually corresponds to the requested article. Use evidence appropriate to the artifact and source, such as embedded DOI/PMID/PMCID, publisher metadata, PDF first-page text, title/author matching, or trusted source metadata. Record the evidence and decision in the manifest. Identity mismatch must fail closed and must never be reported as SUCCESS.

Then execute three individual real-world tests, one at a time, without batch machinery:
1. an obvious PMC OA article;
2. a publisher-hosted OA article that is not relying on the PMC PDF route;
3. an article for which no easy lawful OA full text is found.

For each case, preserve a complete run receipt, journal, identity evidence, provenance, and terminal state. Do not force the third case into EXHAUSTED. EXHAUSTED is valid only if the configured acquisition scope was actually and lawfully exhausted; host/tool inability is BLOCKED. Search-engine absence alone is not exhaustion.

Add regression tests for:
- correct identity match;
- wrong-PDF rejection;
- DOI/PMCID/title disagreement;
- BLOCKED vs EXHAUSTED classification;
- success manifest containing identity evidence and SHA-256.

Hard exit gate:
1. zero false-success identity mismatches;
2. all three real papers have defensible terminal states;
3. the two obtainable OA cases produce real validated PDFs with hashes;
4. the difficult case demonstrates correct BLOCKED/EXHAUSTED semantics rather than optimistic inference;
5. the original one-PMID path remains working.

Return a three-case results table plus the exact implementation/test changes. Do not add JATS or multi-provider orchestration until this gate passes.

---

## Prompt 4 of 5 — Add structured PMC full text, then earn each fallback route individually

Now expand the vertical slice one capability at a time. Do not reintroduce a generalized provider engine all at once.

Phase A: PMC structured full text
For a PMID with a PMCID, add a ChatGPT-native path that can obtain lawful PMC structured full text and materialize JATS/XML. Validate it, hash it, record provenance, and attach it to the same article identity established in Prompt 3. When both are available, the preferred payload for ATOM/SEA should be article.xml and the secondary payload should be article.pdf.

Phase B: fallback routes
Add these routes one at a time, behind explicit feature flags or isolated adapters:
1. PMC/PubMed Central route;
2. publisher-hosted OA route;
3. Unpaywall-assisted OA-location route;
4. institutional repository / accepted-manuscript route.

A route is not considered implemented because code exists. Before enabling the next route, one real article must succeed specifically through the route under test with:
- exact requested identity;
- lawful source/location provenance;
- materialized full-text artifact;
- validation;
- SHA-256;
- manifest;
- correct terminal state.

Keep transport environment-specific. ChatGPT may discover and materialize lawful locations; Python owns policy, identity, validation, hashing, provenance, terminal states, and manifests. Do not make arbitrary raw HTTP inside ChatGPT a prerequisite again.

For every route, add one positive real-world acceptance case and at least one negative/blocked test. Preserve BLOCKED != EXHAUSTED. Never infer provider exhaustion from a failed search result or a tool transport limitation.

Hard exit gate:
1. at least one real JATS/XML acquisition succeeds and is identity-linked to the requested PMID;
2. PDF remains retained when available;
3. every enabled fallback route has independently passed a real article acquisition;
4. no route is enabled merely because its unit tests pass;
5. manifests expose which route supplied each artifact and its hash;
6. the system can still run acquire_one() without batch machinery.

Do not restore batching yet.

---

## Prompt 5 of 5 — Ten-PMID regression, ATOM/SEA handoff, batching, and remote-transport decision

Treat acquire_one() as the product and prove it before restoring scale.

Build a heterogeneous 10-PMID regression set that exercises the routes implemented in Prompt 4. Include a mix of PMC OA, publisher OA, structured JATS availability, and at least one difficult/unavailable case. Run all ten individually first. Do not use the batch runtime for this first pass.

For each PMID, require:
- requested and resolved identity;
- provider/route attempts actually used;
- materialized payload(s) or evidence-backed non-success state;
- PDF/JATS validation as applicable;
- SHA-256 for every successful payload;
- source/version/license provenance when available;
- run receipt and event journal;
- manifest;
- correct SUCCESS / BLOCKED / EXHAUSTED / FAILED state.

Measure and report:
- successful full-text acquisition rate;
- identity mismatch rate, which must be 0;
- false-success rate, which must be 0;
- BLOCKED rate and cause categories;
- route-specific success rate;
- median tool/discovery actions per PMID;
- median elapsed execution time if measurable;
- proportion of successes with JATS + PDF versus PDF only;
- manifest/provenance completeness.

Then complete the remaining integrations in this order:
1. hand every successful acquisition to the ATOM/SEA input interface and prove the handoff on real payloads;
2. wrap the proven acquire_one() path with batch mapping, without changing single-item acquisition semantics;
3. rerun the same 10-PMID set through batch mode and compare item-level outputs with the individual runs;
4. only after equivalence is demonstrated, evaluate whether transport should remain ChatGPT-native or move raw HTTP execution to a remote worker.

Remote-worker decision rule:
Do not move the acquisition brain out of Python. If ChatGPT-native transport materially limits otherwise valid routes, implement the smallest possible GitHub Actions/remote worker whose job is only to execute network transport and return response bytes/status/headers plus provenance. The existing Python runtime remains responsible for identity, provider strategy, policy, validation, hashing, terminal states, manifests, and ATOM/SEA handoff. Do not add intelligence to the worker that belongs in the acquisition brain.

Hard exit gate:
1. ten heterogeneous PMIDs complete with defensible item-level states;
2. zero false SUCCESS results;
3. successful items produce reusable ATOM/SEA inputs;
4. batch outputs are semantically equivalent to individual acquire_one() outputs;
5. the project has an evidence-based decision on whether a remote HTTP worker is necessary;
6. v0.4 documentation records the final supported architecture and remaining limitations.

Return the 10-PMID regression report, ATOM/SEA handoff evidence, batch-equivalence results, optimization metrics, and the remote-transport decision with supporting evidence.

---

## Operating rule for all five prompts

Do not optimize a subsystem before the immediately preceding real-world gate passes. A feature only earns its place in the critical path after it successfully acquires a real paper through that path. Runtime-generated evidence outranks assistant narrative. The sequence is:

one real PDF -> identity verification -> three varied papers -> JATS -> one provider at a time -> ten individual PMIDs -> ATOM/SEA -> batching -> remote worker only if transport evidence justifies it.
