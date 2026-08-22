# v0.3.1 Freeze Record

v0.3.1 is the recoverable reference implementation. The v0.4 development line was copied from this frozen source and does not replace it.

Canonical frozen artifact:

```text
file: scholar-acquire-chatgpt-0.3.1.zip
sha256: 90832c9d4b6c35037616e95e9e406320b278bf6a0bc1342fc23674fa9481e716
package_tree_sha256: ddd4cb104105825bf476ccfe4024c8471ea28c7df9ab871b35a685d8f8037d4c
baseline_tests: 23 passed, 0 failed
baseline_command: PYTHONPATH=src pytest -q
```

The frozen distribution also contains the v0.3.1 wheel, build provenance, test results, and acceptance report.

The following files in `contracts/v0.3.1/` are byte-for-byte copies of the v0.3.1 contract documents:

```text
EXECUTION_CONTRACT.md       ee8ed87fe79955ebae0a5b26751cfdcd5632d58691fcf6f914055e70cde0ea37
ACCEPTANCE_TEST.md          25d55dfd7455bcc540c4e747e2b67e9d6af3cfa706220d84c14efa288de35223
CHATGPT_RUNTIME_PROTOCOL.md 01887e94e6246c633d32801591ed7509651d33205aa356f173f5841a40ba79bc
API_CONTRACTS.md            a2a826273990e8c201364a3850e5c1b2b7a5c4f168635161b2764d68b990e82d
```

Nothing in `V0.4_EXECUTION_CONTRACT.md` retroactively changes the v0.3.1 execution contract.
