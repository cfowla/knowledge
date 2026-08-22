# Acceptance Test

Run before a real PMID batch:

```bash
scholar-acquire-chatgpt chatgpt verify
scholar-acquire-chatgpt chatgpt acceptance --root ./acceptance
pytest
```

The synthetic acceptance test must prove, without network I/O:

1. runtime build integrity verifies;
2. `RUN_RECEIPT.json` is emitted;
3. `step()` produces an `ExternalFetchRequest`;
4. an incorrect ingest token is rejected;
5. the correctly correlated response is hashed and ingested;
6. a later `step()` reaches `SUCCESS`;
7. the event journal contains integrity, request, ingest, artifact-validation, and terminal-success events.

For the next real regression batch, use PMIDs `20566676`, `23963895`, `26911584`, and `37496050`. The real test passes only if every external action is driven by the runtime and every item has a receipt/event journal/terminal outcome. The number of PDFs found is not itself an acceptance criterion.
