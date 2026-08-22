# v0.4 Remote Transport Decision

Decision date: 2026-08-21

## Decision

Use a hybrid transport architecture:

1. Keep ChatGPT-native discovery/materialization as the first transport choice when it can produce real bytes directly.
2. Use the GitHub Actions transport shim only when Python has selected a lawful route but the ChatGPT host cannot materialize the response bytes.
3. Keep every acquisition decision in the Python runtime.

This is not a migration of the acquisition brain to GitHub. It is a narrow network I/O fallback.

## Evidence

The ten-PMID regression produced five real PDFs through ChatGPT-native transport, so moving all transport away from ChatGPT would add unnecessary infrastructure.

The same regression also demonstrated material transport gaps:

- PMC article browser routes repeatedly returned anti-bot/reCAPTCHA pages.
- PMC officially supports full-text JATS through OAI-PMH and exposes article XML/PDF objects through its AWS dataset service.
- PLOS officially exposes individual article JATS XML using a DOI-based `type=manuscript` endpoint.
- For PMID 38330007, that PLOS endpoint returned HTTP 200 with `application/xml`, but the host materializer refused to save the XML payload.
- Unpaywall's DOI-specific route/API could not be reliably executed in the current host environment, preventing defensible exhaustion in the difficult case.

Official references used for the architectural decision:

- PMC AWS article datasets: https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/
- PMC OAI-PMH JATS API: https://pmc.ncbi.nlm.nih.gov/tools/oai/
- PMC automated-retrieval policy: https://pmc.ncbi.nlm.nih.gov/tools/openftlist/
- PLOS TDM/JATS access: https://api.plos.org/text-and-data-mining.html

The current date is before PMC's announced on-or-after 2026-08-24 removal of legacy dataset distribution paths. New work should target the updated AWS object structure and current OAI-PMH base URL rather than building new dependencies on legacy FTP/OA API paths.

## Implemented shim

The source tree now contains:

- `.github/workflows/acquisition-transport.yml`
- `remote_transport/transport_worker.py`
- `remote_transport/README.md`
- `tests/test_remote_transport_worker.py`

The worker accepts only an opaque request ID and an exact URL selected by Python. It executes one unauthenticated GET and returns raw response bytes, final URL, HTTP status, response headers, timestamps, and transport errors.

It does not:

- resolve PMID/PMCID/DOI identity;
- choose or order providers;
- infer OA eligibility or licenses;
- bypass access controls;
- validate PDF or JATS;
- compute acquisition SHA-256;
- choose SUCCESS/BLOCKED/EXHAUSTED/FAILED;
- write acquisition manifests;
- build ATOM/SEA handoffs.

Those functions remain in Python.

## Validation status

The worker has a local transport-contract test using a real local HTTP server that returns `application/xml`. The test proves byte-for-byte XML materialization plus status/header/provenance return while confirming that content validation and acquisition hashing remain disabled in the worker. The complete suite passes 38/38 tests.

The workflow is implemented in the v0.4 source tree but is not deployed to an unrelated existing GitHub repository. No dedicated Acquisition Runtime repository is connected in this session, and creating a new GitHub repository is not exposed by the connector. Deployment therefore remains an environment step, not an acquisition-brain change.
