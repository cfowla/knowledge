# API contracts verified 2026-08-21

This implementation was built against the following current public contracts:

- Europe PMC REST API: `GET https://www.ebi.ac.uk/europepmc/webservices/rest/search` and `GET /{PMCID}/fullTextXML` for OA JATS XML.
- PMC ID Converter: `GET https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/`, including `versions=yes` and `showaiid=yes`.
- PMC OAI-PMH: `GET https://pmc.ncbi.nlm.nih.gov/api/oai/v1/mh/` with `verb=GetRecord`, identifier `oai:pubmedcentral.nih.gov:{numeric_pmcid}`, and `metadataPrefix=pmc` for reusable JATS full text.
- PMC Article Datasets on AWS: world-readable bucket `pmc-oa-opendata`, organized by article version beginning in 2026, with per-version JSON metadata exposing `xml_url`, `pdf_url`, `text_url`, license, and manuscript flags. This is used instead of the legacy PMC OA Web Service, which NCBI announced will be removed on or after 2026-08-24.
- Unpaywall REST API v2: `GET https://api.unpaywall.org/v2/{doi}?email=...`; `oa_locations` expose host type, landing/PDF URLs, license, and version. Version 2 is the only supported API version.
- OpenAlex singleton work API: DOI/PMID lookup; work `locations` expose repository source type, OA status, landing/PDF URLs, license, and version. A free API key is recommended; low-volume no-key access may be available subject to the current service budget.

The implementation intentionally does not call legacy PMC `oa.fcgi` or FTP distribution paths.
