# Remote Transport Decision — v0.4.2

Decision: **implement and use a minimal remote transport worker for routes whose exact lawful response bytes cannot be materialized by ChatGPT-native transport.** Do not move the acquisition brain.

The worker implementation is `remote_worker/transport_worker.py`; its GitHub Actions wrapper is `.github/workflows/scholarly-transport.yml`. The local contract test passes and proves that a response's status, headers, exact bytes, byte count, and SHA-256 are returned without adding provider logic.

Trigger evidence from the ten-PMID regression:

- PMID 41623473: official PMC metadata identifies a world-readable CC BY JATS XML and PDF, but current host transport could not materialize XML bytes.
- PMID 20566676: PMC OA article and PDF location were resolved, but current host transport could not materialize PDF bytes.
- PMID 24766495: direct Unpaywall DOI transport was not materializable, so repository/OA exhaustion could not be proven.
- Seven direct publisher/repository PDFs succeeded through the unchanged Python validation/hashing/manifest path, demonstrating that the Python acquisition brain is not the limiting component.
