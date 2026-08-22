# Acquisition Runtime pathing rules

## Canonical path

`Acquisition Runtime / scholar-acquire-chatgpt / 00 - CURRENT AUTHORITATIVE RUNTIME / v0.4.3 - CURRENT AUTHORITATIVE BUILD`

Canonical Drive folder ID: `1y2SQPk-oLTG-PAcHMv1b5HU0tYEIs2_2`

Canonical build ID: `scholar-acquire-chatgpt-0.4.3-prompt3-reconciled`

Package-tree SHA-256: `fc412487fdcaf1fef556c14c18386b86f3382b0a76d3fc345fd1153572524815`

Source archive file ID: `1b0Tdt-fh3xY5jJyzofxGngyWxytgoL34`

Source archive SHA-256: `c6bb555bb6d612c0dae8b2a4f06c4274dee14143dcfdc952ffb4f116c5059daa`

## Mandatory resolution behavior

1. Use `CURRENT_RUNTIME_POINTER.json` as the machine-readable authority record.
2. Resolve by Drive ID and verified hash, not by filename, recency, prompt number, or first search match.
3. Only `00 - CURRENT AUTHORITATIVE RUNTIME` is runtime-eligible.
4. Treat everything under `90 - HISTORICAL DEVELOPMENT AND EVIDENCE` as non-executable historical evidence unless a future reconciliation explicitly promotes it and replaces the pointer.
5. Never recursively search Drive for `src`, `pyproject.toml`, `scholar-acquire-chatgpt*.zip`, `CAPABILITY_REGISTRY.json`, or `PROMPT*_REPORT*` and assume the first/latest result is current.
6. Before running code, fetch the source archive by the exact file ID above and verify its SHA-256. A mismatch is a reconciliation failure, not permission to select another archive.
7. Route support must be read from the canonical capability registry and route-proof matrix inside the authoritative build folder. GitHub workflow completion is transport evidence only.
8. Historical Prompt 1/2/3/4/5 folders are work logs, not phase-selection instructions.

## Historical path

`Acquisition Runtime / scholar-acquire-chatgpt / 90 - HISTORICAL DEVELOPMENT AND EVIDENCE`

This branch contains the pre-v0.4.3 root source snapshot, v0.4 development work, blocked/superseded Prompt 3 evidence, earlier repair prompts, and the abandoned Prompt 4 preflight. It is preserved for provenance and must not be selected as the runtime by default.
