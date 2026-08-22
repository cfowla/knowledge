# v0.4.3 Prompt 3 — Route Re-Proof Report

## Result

**Hard gate: BLOCKED at Route C (Unpaywall).** Prompt 3 was executed through its mandated stopping condition. PMC and publisher-hosted OA were independently re-proven and promoted to `supported`. Unpaywall remains `experimental` because its positive live lookup could not be executed without a required caller email parameter. Per Prompt 3, the repository route was not attempted after Route C failed its positive gate.

## Route proof matrix

| Route | Positive | Negative/blocked | Capability | Proof |
|---|---|---|---|---|
| PMC | PASS — PMID 24782981 | PASS — PMID 24766495 → EXHAUSTED on definitive no-PMCID evidence | supported | JATS + PDF, same identity |
| Publisher OA | PASS — PMID 35124914 | PASS — same PMID with transport unavailable → BLOCKED | supported | Publisher PDF, non-Frontiers family |
| Unpaywall | BLOCKED — lookup not executed | PASS — configuration/transport uncertainty → BLOCKED, never EXHAUSTED | experimental | Required `email` parameter has no authorized configured value |
| Repository | NOT ATTEMPTED | NOT ATTEMPTED | experimental | Prompt sequencing prohibits proceeding until Unpaywall positive proof succeeds |

## Route A — PMC

Production `acquire_one()` started from PMID **24782981** and resolved PMID `24782981`, PMCID `PMC3995050`, DOI `10.3389/fonc.2014.00064`, and the exact title *Targeting PI3K/Akt/mTOR Signaling in Cancer*. The route used the current PMC Open Access Article Dataset versioned Cloud objects for `PMC3995050.1`.

- JATS `article.xml`: **126,350 bytes**, SHA-256 `ee7cdad7ae26e26dfe3d51965beba50b967e99ec446c4a1c925890a494401589`.
- PDF `article.pdf`: **810,232 bytes**, SHA-256 `54465e3c056b86551d8c5d865b0685d01a5f4fa2c11bc705a479768b3efc63cb`.
- Both payloads validated against the same article identity.
- Manifest preference: `article.xml` preferred, `article.pdf` secondary.
- GitHub Actions remote transport runs **32542031894** (JATS) and **32542094635** (PDF) returned bytes; Python independently admitted, validated, and hashed them.
- Negative PMID **24766495** had definitive no-PMCID evidence; the sole PMC route correctly ended `EXHAUSTED`.

PMC was promoted to `supported` only after positive and negative evidence existed.

## Route B — publisher-hosted OA

Production `acquire_one()` started from PMID **35124914** and acquired the publisher-hosted PDF from the Journal of Ayub Medical College Abbottabad, not Frontiers and not the PMC route.

- PDF: **504,544 bytes**, SHA-256 `ab78e51b14f60002b117c1d3e3059470948a671a80773bc694d732a0d0606304`.
- Source: `https://www.jamc.ayubmed.edu.pk/index.php/jamc/article/download/9089/3174`.
- Identity verified, PDF validated, manifest/receipt/journal written, terminal state `SUCCESS`.
- Negative case used the same lawful publisher location with no executable transport and correctly ended `BLOCKED`, with exhaustion false.

Publisher OA was promoted to `supported` only after the real positive proof.

## Route C — Unpaywall

The controller was repaired so the host may return raw Unpaywall DOI-object/OA-location facts but cannot preselect the successful location. Python applies version/format/host policy and chooses the admitted full-text URL.

The live positive gate could not be executed. Current Unpaywall v2 requires a caller `email` query parameter. The runtime checked supported configuration keys (`SCHOLAR_FETCH_EMAIL`, `UNPAYWALL_EMAIL`, `NCBI_EMAIL`) and none was configured. No placeholder email or personal identity was invented. A production single-route attempt therefore recorded `BLOCKED` with `provider_exhaustion_confirmed=false`.

Unpaywall remains `experimental`.

## Route D — repository

Not attempted. Prompt 3 explicitly says not to enable the repository route until the Unpaywall positive succeeds. Repository remains `experimental`.

## Discrepancies and repairs

1. **Early SUCCESS after first artifact — repaired.** Prompt 2 could finalize after JATS alone when JATS+PDF were requested. Prompt 3 now waits for requested payload coverage and resumes remaining locations after deferred transport.
2. **Host-selected Unpaywall location — repaired.** Raw Unpaywall observations are now evaluated by Python; host preselection no longer satisfies production acquisition.
3. **Generic current PMC media type — repaired.** Current PMC S3 objects can return `binary/octet-stream`; generic binary media types no longer defeat valid JATS/PDF before content validation.
4. **PMC dataset migration — adapted.** Live proof uses current versioned PMC Cloud Service objects instead of legacy OA dataset endpoints being retired during this release window.
5. **Unpaywall caller-email requirement — blocking discrepancy.** No authorized caller email is configured. This stops Prompt 3 before repository proof.

## Tests and capability registry

`PYTHONPATH=src pytest -q` → **26 passed, 0 failed**.

`CAPABILITY_REGISTRY.json` records only PMC and publisher OA as `supported`, with proof PMID, run ID, manifest, payload SHA-256 values, runtime version, proof date, and negative-case evidence. Unpaywall and repository remain `experimental`.

## Hard-exit gate

Gates 1, 2, 5 (for executed successes), 6, 7, and 8 pass. Gate 3 fails because Unpaywall and repository lack independent real positives; gate 4 is incomplete because repository was not reached. **Do not proceed to Prompt 4.**
