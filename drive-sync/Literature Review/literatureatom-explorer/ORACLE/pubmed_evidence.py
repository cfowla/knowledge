#!/usr/bin/env python3
"""Retrieve PubMed abstracts and map them to the CDS evidence schema.

The script intentionally keeps three boundaries in one standalone file:

- PubMedClient: NCBI E-utilities I/O
- PubMedXMLMapper: external PubMed XML -> typed evidence documents
- CLI: user input and JSON serialization

This makes the first implementation directly usable while keeping it easy to
split into repositories/, mappers/, domain/, and interfaces/ later.

Requires Python 3.10+ and uses only the standard library.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


EUTILS_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
PUBMED_RECORD_URL = "https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
DEFAULT_TOOL = "cds_pubmed_evidence"
MAX_ESEARCH_RESULTS = 10_000
MAX_FETCH_BATCH_SIZE = 200
RETRYABLE_HTTP_STATUS = {429, 500, 502, 503, 504}


# ---------------------------------------------------------------------------
# Typed CDS evidence schema
# ---------------------------------------------------------------------------


@dataclass(slots=True)
class EvidenceParagraph:
    text: str
    page: int | None = None
    element_type: str = "NarrativeText"


@dataclass(slots=True)
class EvidenceSection:
    heading: str
    level: int = 1
    paragraphs: list[EvidenceParagraph] = field(default_factory=list)


@dataclass(slots=True)
class EvidenceDocument:
    document_id: str
    title: str
    authors: list[str]
    date: str | None
    source_type: str
    source_url: str
    sections: list[EvidenceSection]
    tables: list[dict[str, Any]] = field(default_factory=list)
    figures: list[dict[str, Any]] = field(default_factory=list)
    references: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


EXPECTED_DOCUMENT_KEYS = {
    "document_id",
    "title",
    "authors",
    "date",
    "source_type",
    "source_url",
    "sections",
    "tables",
    "figures",
    "references",
}


# ---------------------------------------------------------------------------
# Typed errors
# ---------------------------------------------------------------------------


class PubMedError(RuntimeError):
    """Base error for expected PubMed retrieval or mapping failures."""


class PubMedAPIError(PubMedError):
    """NCBI request failed or returned an invalid response."""


class PubMedParseError(PubMedError):
    """PubMed XML could not be parsed into the evidence schema."""


class SchemaValidationError(PubMedError):
    """Mapped output does not satisfy the CDS evidence contract."""


# ---------------------------------------------------------------------------
# PubMed API repository boundary
# ---------------------------------------------------------------------------


class PubMedClient:
    """Small NCBI E-utilities client with batching, throttling, and retries."""

    def __init__(
        self,
        *,
        email: str | None = None,
        api_key: str | None = None,
        tool: str = DEFAULT_TOOL,
        timeout_seconds: float = 30.0,
        max_retries: int = 4,
    ) -> None:
        self.email = email.strip() if email else None
        self.api_key = api_key.strip() if api_key else None
        self.tool = tool.strip() or DEFAULT_TOOL
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries
        self._last_request_at = 0.0

        # NCBI permits 3 requests/second without a key and 10/second with one.
        self._minimum_interval = 0.11 if self.api_key else 0.34

    def search(self, query: str, *, max_results: int = 20) -> list[str]:
        """Return PMIDs for a PubMed query using ESearch."""
        query = query.strip()
        if not query:
            raise ValueError("PubMed query cannot be empty.")
        if not 1 <= max_results <= MAX_ESEARCH_RESULTS:
            raise ValueError(
                f"max_results must be between 1 and {MAX_ESEARCH_RESULTS}."
            )

        payload = self._request(
            "esearch.fcgi",
            {
                "db": "pubmed",
                "term": query,
                "retmode": "json",
                "retmax": str(max_results),
            },
            use_post=False,
        )

        try:
            decoded = json.loads(payload.decode("utf-8"))
            result = decoded["esearchresult"]
            if "ERROR" in result:
                raise PubMedAPIError(str(result["ERROR"]))
            if result.get("errorlist"):
                raise PubMedAPIError(
                    "NCBI ESearch rejected part of the query: "
                    + json.dumps(result["errorlist"], ensure_ascii=False)
                )
            ids = result.get("idlist", [])
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise PubMedAPIError("NCBI ESearch returned malformed JSON.") from exc

        return _deduplicate_pmids(ids)

    def fetch_xml_batches(
        self,
        pmids: Sequence[str],
        *,
        batch_size: int = MAX_FETCH_BATCH_SIZE,
    ) -> Iterator[bytes]:
        """Yield PubMed XML responses for validated PMID batches."""
        normalized = _deduplicate_pmids(pmids)
        if not normalized:
            return
        if not 1 <= batch_size <= MAX_FETCH_BATCH_SIZE:
            raise ValueError(
                f"batch_size must be between 1 and {MAX_FETCH_BATCH_SIZE}."
            )

        for batch in _batched(normalized, batch_size):
            yield self._request(
                "efetch.fcgi",
                {
                    "db": "pubmed",
                    "id": ",".join(batch),
                    "retmode": "xml",
                },
                use_post=True,
            )

    def _request(
        self,
        endpoint: str,
        params: dict[str, str],
        *,
        use_post: bool,
    ) -> bytes:
        request_params = dict(params)
        request_params["tool"] = self.tool
        if self.email:
            request_params["email"] = self.email
        if self.api_key:
            request_params["api_key"] = self.api_key

        encoded = urllib.parse.urlencode(request_params)
        url = f"{EUTILS_BASE_URL}/{endpoint}"
        data = encoded.encode("utf-8") if use_post else None
        if not use_post:
            url = f"{url}?{encoded}"

        user_agent = self.tool
        if self.email:
            user_agent = f"{user_agent} ({self.email})"

        request = urllib.request.Request(
            url,
            data=data,
            headers={
                "Accept": "application/json, application/xml, text/xml;q=0.9",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": user_agent,
            },
            method="POST" if use_post else "GET",
        )

        last_error: Exception | None = None
        for attempt in range(self.max_retries + 1):
            self._throttle()
            try:
                with urllib.request.urlopen(
                    request, timeout=self.timeout_seconds
                ) as response:
                    payload = response.read()
                self._raise_for_embedded_error(payload)
                return payload
            except urllib.error.HTTPError as exc:
                last_error = exc
                if exc.code not in RETRYABLE_HTTP_STATUS or attempt >= self.max_retries:
                    body = _safe_http_error_body(exc)
                    suffix = f" Response: {body}" if body else ""
                    raise PubMedAPIError(
                        f"NCBI request failed with HTTP {exc.code}.{suffix}"
                    ) from exc
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                last_error = exc
                if attempt >= self.max_retries:
                    raise PubMedAPIError(
                        f"NCBI request failed after {attempt + 1} attempts: {exc}"
                    ) from exc

            delay = min(8.0, (2**attempt) * 0.5) + random.uniform(0.0, 0.25)
            time.sleep(delay)

        raise PubMedAPIError(f"NCBI request failed: {last_error}")

    def _throttle(self) -> None:
        elapsed = time.monotonic() - self._last_request_at
        remaining = self._minimum_interval - elapsed
        if remaining > 0:
            time.sleep(remaining)
        self._last_request_at = time.monotonic()

    @staticmethod
    def _raise_for_embedded_error(payload: bytes) -> None:
        stripped = payload.lstrip()
        if not stripped:
            raise PubMedAPIError("NCBI returned an empty response.")

        if stripped.startswith(b"<"):
            try:
                root = ET.fromstring(payload)
            except ET.ParseError:
                return
            _strip_namespaces(root)
            error = root if root.tag == "ERROR" else root.find(".//ERROR")
            if error is not None:
                message = _element_text(error) or "Unknown NCBI error"
                raise PubMedAPIError(message)


# ---------------------------------------------------------------------------
# PubMed XML mapper boundary
# ---------------------------------------------------------------------------


class PubMedXMLMapper:
    """Map NCBI PubMed XML into the exact CDS evidence document contract."""

    _NLM_CATEGORY_HEADINGS = {
        "BACKGROUND": "Background",
        "OBJECTIVE": "Objective",
        "METHODS": "Methods",
        "RESULTS": "Results",
        "CONCLUSIONS": "Conclusions",
    }

    _PUBMED_HISTORY_PRIORITY = (
        "epublish",
        "ppublish",
        "aheadofprint",
        "pubmed",
    )

    def parse(self, xml_payload: bytes | str) -> list[EvidenceDocument]:
        try:
            root = ET.fromstring(xml_payload)
        except ET.ParseError as exc:
            raise PubMedParseError(f"Invalid PubMed XML: {exc}") from exc

        _strip_namespaces(root)
        documents: list[EvidenceDocument] = []

        for record in root.findall(".//PubmedArticle"):
            document = self._parse_pubmed_article(record)
            validate_evidence_document(document)
            documents.append(document)

        for record in root.findall(".//PubmedBookArticle"):
            document = self._parse_pubmed_book_article(record)
            validate_evidence_document(document)
            documents.append(document)

        if not documents:
            error = root if root.tag == "ERROR" else root.find(".//ERROR")
            if error is not None:
                raise PubMedAPIError(_element_text(error) or "Unknown NCBI error")

        return documents

    def _parse_pubmed_article(self, record: ET.Element) -> EvidenceDocument:
        citation = record.find("MedlineCitation")
        if citation is None:
            raise PubMedParseError("PubmedArticle is missing MedlineCitation.")

        pmid = _element_text(citation.find("PMID"))
        if not pmid or not pmid.isdigit():
            raise PubMedParseError("PubmedArticle is missing a valid PMID.")

        article = citation.find("Article")
        if article is None:
            raise PubMedParseError(f"PMID {pmid} is missing Article metadata.")

        title = (
            _element_text(article.find("ArticleTitle"))
            or _element_text(citation.find("VernacularTitle"))
            or f"PubMed record {pmid}"
        )
        authors = self._parse_authors(article.find("AuthorList"))
        publication_date = self._parse_publication_date(record, article)
        sections = self._parse_abstract_sections(article, citation)

        return EvidenceDocument(
            document_id=f"pubmed-{pmid}",
            title=title,
            authors=authors,
            date=publication_date,
            source_type="pubmed",
            source_url=PUBMED_RECORD_URL.format(pmid=pmid),
            sections=sections,
        )

    def _parse_pubmed_book_article(self, record: ET.Element) -> EvidenceDocument:
        book_document = record.find("BookDocument")
        if book_document is None:
            raise PubMedParseError("PubmedBookArticle is missing BookDocument.")

        pmid = _element_text(book_document.find("PMID"))
        if not pmid or not pmid.isdigit():
            raise PubMedParseError("PubmedBookArticle is missing a valid PMID.")

        title = (
            _element_text(book_document.find("ArticleTitle"))
            or _element_text(book_document.find("Book/BookTitle"))
            or f"PubMed book record {pmid}"
        )
        authors = self._parse_authors(book_document.find("AuthorList"))
        publication_date = self._parse_book_date(book_document, record)
        sections = self._parse_abstract_container(book_document.find("Abstract"))

        return EvidenceDocument(
            document_id=f"pubmed-{pmid}",
            title=title,
            authors=authors,
            date=publication_date,
            source_type="pubmed",
            source_url=PUBMED_RECORD_URL.format(pmid=pmid),
            sections=sections,
        )

    def _parse_authors(self, author_list: ET.Element | None) -> list[str]:
        if author_list is None:
            return []

        authors: list[str] = []
        for author in author_list.findall("Author"):
            collective = _element_text(author.find("CollectiveName"))
            if collective:
                authors.append(collective)
                continue

            last_name = _element_text(author.find("LastName"))
            fore_name = _element_text(author.find("ForeName"))
            initials = _element_text(author.find("Initials"))
            suffix = _element_text(author.find("Suffix"))

            given_name = fore_name or initials
            parts = [part for part in (given_name, last_name, suffix) if part]
            if parts:
                authors.append(" ".join(parts))

        return authors

    def _parse_publication_date(
        self,
        record: ET.Element,
        article: ET.Element,
    ) -> str | None:
        for article_date in article.findall("ArticleDate"):
            parsed = _date_from_parts(article_date)
            if parsed:
                return parsed

        journal_pub_date = article.find("Journal/JournalIssue/PubDate")
        parsed = _date_from_pubdate(journal_pub_date)
        if parsed:
            return parsed

        history_dates = record.findall("PubmedData/History/PubMedPubDate")
        by_status = {
            element.get("PubStatus", "").lower(): element
            for element in history_dates
        }
        for status in self._PUBMED_HISTORY_PRIORITY:
            parsed = _date_from_parts(by_status.get(status))
            if parsed:
                return parsed

        return None

    def _parse_book_date(
        self,
        book_document: ET.Element,
        record: ET.Element,
    ) -> str | None:
        candidates = (
            book_document.find("ArticleDate"),
            book_document.find("Book/PubDate"),
            record.find("PubmedBookData/History/PubMedPubDate"),
        )
        for candidate in candidates:
            parsed = _date_from_pubdate(candidate)
            if parsed:
                return parsed
        return None

    def _parse_abstract_sections(
        self,
        article: ET.Element,
        citation: ET.Element,
    ) -> list[EvidenceSection]:
        primary = article.find("Abstract")
        sections = self._parse_abstract_container(primary)
        if sections:
            return sections

        # OtherAbstract is a MedlineCitation child in PubMed XML. Use it only
        # when no primary Article/Abstract is available.
        other = citation.find("OtherAbstract")
        return self._parse_abstract_container(other)

    def _parse_abstract_container(
        self,
        abstract: ET.Element | None,
    ) -> list[EvidenceSection]:
        if abstract is None:
            return []

        sections: list[EvidenceSection] = []
        for abstract_text in abstract.findall("AbstractText"):
            text = _element_text(abstract_text)
            if not text:
                continue

            heading = self._abstract_heading(abstract_text)
            paragraph = EvidenceParagraph(text=text)

            if sections and sections[-1].heading == heading:
                sections[-1].paragraphs.append(paragraph)
            else:
                sections.append(
                    EvidenceSection(
                        heading=heading,
                        level=1,
                        paragraphs=[paragraph],
                    )
                )

        return sections

    def _abstract_heading(self, abstract_text: ET.Element) -> str:
        label = _clean_text(abstract_text.get("Label", ""))
        if label:
            return label

        category = abstract_text.get("NlmCategory", "").strip().upper()
        if category and category != "UNASSIGNED":
            return self._NLM_CATEGORY_HEADINGS.get(category, category)

        return "Abstract"


# ---------------------------------------------------------------------------
# Validation and shared utilities
# ---------------------------------------------------------------------------


def validate_evidence_document(document: EvidenceDocument) -> None:
    """Validate the structural contract without inventing missing evidence."""
    payload = document.to_dict()
    if set(payload) != EXPECTED_DOCUMENT_KEYS:
        raise SchemaValidationError(
            f"Unexpected document fields: {sorted(set(payload) ^ EXPECTED_DOCUMENT_KEYS)}"
        )
    if not document.document_id:
        raise SchemaValidationError("document_id is required.")
    if not document.title:
        raise SchemaValidationError("title is required.")
    if document.source_type != "pubmed":
        raise SchemaValidationError("source_type must be 'pubmed'.")
    if not document.source_url.startswith("https://pubmed.ncbi.nlm.nih.gov/"):
        raise SchemaValidationError("source_url must be a PubMed record URL.")

    for section in document.sections:
        if not section.heading:
            raise SchemaValidationError("Every section must have a heading.")
        if section.level < 1:
            raise SchemaValidationError("Section level must be at least 1.")
        for paragraph in section.paragraphs:
            if not paragraph.text:
                raise SchemaValidationError("Paragraph text cannot be empty.")
            if paragraph.element_type != "NarrativeText":
                raise SchemaValidationError(
                    "PubMed abstract paragraphs must use NarrativeText."
                )


def retrieve_documents(
    client: PubMedClient,
    mapper: PubMedXMLMapper,
    pmids: Sequence[str],
    *,
    batch_size: int = MAX_FETCH_BATCH_SIZE,
) -> list[EvidenceDocument]:
    """Fetch, map, validate, deduplicate, and preserve requested PMID order."""
    requested = _deduplicate_pmids(pmids)
    mapped: dict[str, EvidenceDocument] = {}

    for xml_batch in client.fetch_xml_batches(requested, batch_size=batch_size):
        for document in mapper.parse(xml_batch):
            pmid = document.document_id.removeprefix("pubmed-")
            mapped[pmid] = document

    return [mapped[pmid] for pmid in requested if pmid in mapped]


def _deduplicate_pmids(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    normalized: list[str] = []
    for raw_value in values:
        value = str(raw_value).strip()
        if not value:
            continue
        if not value.isdigit():
            raise ValueError(f"Invalid PMID: {value!r}. PMIDs must contain digits only.")
        value = value.lstrip("0") or "0"
        if value not in seen:
            seen.add(value)
            normalized.append(value)
    return normalized


def _batched(values: Sequence[str], size: int) -> Iterator[list[str]]:
    for start in range(0, len(values), size):
        yield list(values[start : start + size])


def _strip_namespaces(root: ET.Element) -> None:
    for element in root.iter():
        if isinstance(element.tag, str) and "}" in element.tag:
            element.tag = element.tag.rsplit("}", 1)[-1]


def _element_text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return _clean_text("".join(element.itertext()))


def _clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _date_from_pubdate(element: ET.Element | None) -> str | None:
    if element is None:
        return None
    parsed = _date_from_parts(element)
    if parsed:
        return parsed
    medline_date = _element_text(element.find("MedlineDate"))
    return _date_from_medline_date(medline_date)


def _date_from_parts(element: ET.Element | None) -> str | None:
    if element is None:
        return None

    year = _element_text(element.find("Year"))
    month = _element_text(element.find("Month"))
    day = _element_text(element.find("Day"))

    if not re.fullmatch(r"\d{4}", year):
        return None

    normalized_month = _normalize_month(month)
    normalized_day = _normalize_day(day)

    if normalized_month and normalized_day:
        return f"{year}-{normalized_month}-{normalized_day}"
    if normalized_month:
        return f"{year}-{normalized_month}"
    return year


def _date_from_medline_date(value: str) -> str | None:
    if not value:
        return None

    year_match = re.search(r"\b(18|19|20|21)\d{2}\b", value)
    if not year_match:
        return None
    year = year_match.group(0)

    remainder = value[year_match.end() :].strip(" .,-/")
    month_token = re.split(r"[\s\-/]+", remainder, maxsplit=1)[0] if remainder else ""
    month = _normalize_month(month_token)
    return f"{year}-{month}" if month else year


def _normalize_month(value: str) -> str | None:
    if not value:
        return None

    value = value.strip()
    if value.isdigit():
        number = int(value)
        return f"{number:02d}" if 1 <= number <= 12 else None

    month_names = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }
    number = month_names.get(value[:3].lower())
    return f"{number:02d}" if number else None


def _normalize_day(value: str) -> str | None:
    if not value or not value.isdigit():
        return None
    number = int(value)
    return f"{number:02d}" if 1 <= number <= 31 else None


def _safe_http_error_body(error: urllib.error.HTTPError) -> str:
    try:
        body = error.read(500).decode("utf-8", errors="replace")
    except OSError:
        return ""
    return _clean_text(body)


def _read_pmids_file(path: Path) -> list[str]:
    values: list[str] = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        values.extend(token for token in re.split(r"[\s,]+", line) if token)
    return _deduplicate_pmids(values)


def _write_documents(
    documents: Sequence[EvidenceDocument],
    *,
    output: str,
    json_lines: bool,
    compact: bool,
) -> None:
    destination = sys.stdout if output == "-" else open(output, "w", encoding="utf-8")
    try:
        if json_lines:
            for document in documents:
                destination.write(
                    json.dumps(document.to_dict(), ensure_ascii=False, separators=(",", ":"))
                )
                destination.write("\n")
        else:
            kwargs: dict[str, Any] = {"ensure_ascii": False}
            if compact:
                kwargs["separators"] = (",", ":")
            else:
                kwargs["indent"] = 2
            json.dump([document.to_dict() for document in documents], destination, **kwargs)
            destination.write("\n")
    finally:
        if destination is not sys.stdout:
            destination.close()


# ---------------------------------------------------------------------------
# Self-test fixture
# ---------------------------------------------------------------------------


_SELF_TEST_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<PubmedArticleSet>
  <PubmedArticle>
    <MedlineCitation Status="MEDLINE" Owner="NLM">
      <PMID Version="1">12345678</PMID>
      <Article PubModel="Electronic">
        <Journal>
          <JournalIssue CitedMedium="Internet">
            <PubDate><Year>2026</Year><Month>Jul</Month></PubDate>
          </JournalIssue>
        </Journal>
        <ArticleTitle>A <i>structured</i> PubMed abstract.</ArticleTitle>
        <ArticleDate DateType="Electronic">
          <Year>2026</Year><Month>7</Month><Day>9</Day>
        </ArticleDate>
        <Abstract>
          <AbstractText Label="BACKGROUND" NlmCategory="BACKGROUND">Background text.</AbstractText>
          <AbstractText Label="METHODS" NlmCategory="METHODS">Methods with <sup>2</sup> groups.</AbstractText>
          <AbstractText Label="RESULTS" NlmCategory="RESULTS">Results text.</AbstractText>
          <CopyrightInformation>Copyright text that should not be imported.</CopyrightInformation>
        </Abstract>
        <AuthorList CompleteYN="Y">
          <Author ValidYN="Y">
            <LastName>Smith</LastName><ForeName>Alex J</ForeName><Initials>AJ</Initials>
          </Author>
          <Author ValidYN="Y"><CollectiveName>CDS Study Group</CollectiveName></Author>
        </AuthorList>
      </Article>
    </MedlineCitation>
    <PubmedData>
      <History>
        <PubMedPubDate PubStatus="pubmed"><Year>2026</Year><Month>7</Month><Day>10</Day></PubMedPubDate>
      </History>
    </PubmedData>
  </PubmedArticle>
  <PubmedArticle>
    <MedlineCitation Status="Publisher" Owner="NLM">
      <PMID Version="1">23456789</PMID>
      <Article PubModel="Print">
        <Journal><JournalIssue><PubDate><MedlineDate>2025 Jan-Feb</MedlineDate></PubDate></JournalIssue></Journal>
        <ArticleTitle>Unstructured abstract example.</ArticleTitle>
        <Abstract><AbstractText>One unstructured paragraph.</AbstractText></Abstract>
      </Article>
    </MedlineCitation>
  </PubmedArticle>
</PubmedArticleSet>
"""


def run_self_test() -> None:
    mapper = PubMedXMLMapper()
    documents = mapper.parse(_SELF_TEST_XML)
    assert len(documents) == 2

    first = documents[0]
    assert first.document_id == "pubmed-12345678"
    assert first.title == "A structured PubMed abstract."
    assert first.authors == ["Alex J Smith", "CDS Study Group"]
    assert first.date == "2026-07-09"
    assert [section.heading for section in first.sections] == [
        "BACKGROUND",
        "METHODS",
        "RESULTS",
    ]
    assert first.sections[1].paragraphs[0].text == "Methods with 2 groups."
    assert first.tables == [] and first.figures == [] and first.references == []
    assert set(first.to_dict()) == EXPECTED_DOCUMENT_KEYS

    second = documents[1]
    assert second.date == "2025-01"
    assert second.sections[0].heading == "Abstract"
    assert second.sections[0].paragraphs[0].page is None
    assert second.sections[0].paragraphs[0].element_type == "NarrativeText"

    assert _date_from_medline_date("2024 Winter") == "2024"
    assert _date_from_medline_date("2023 Dec 15") == "2023-12"
    assert _deduplicate_pmids(["00123", "123", "456"]) == ["123", "456"]

    print("Self-test passed: PubMed XML maps to the CDS evidence schema.")


# ---------------------------------------------------------------------------
# CLI interface
# ---------------------------------------------------------------------------


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Retrieve PubMed abstracts into the CDS evidence JSON schema.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--pmid",
        action="append",
        nargs="+",
        default=[],
        metavar="PMID",
        help="One or more PMIDs; may be supplied multiple times.",
    )
    parser.add_argument(
        "--pmid-file",
        type=Path,
        help="Text file containing PMIDs separated by whitespace or commas.",
    )
    parser.add_argument(
        "--query",
        help="PubMed search query. Matching PMIDs are retrieved with ESearch.",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=20,
        help=f"Maximum query results, up to {MAX_ESEARCH_RESULTS}.",
    )
    parser.add_argument(
        "--xml-file",
        type=Path,
        help="Parse a saved PubMed EFetch XML file without making API calls.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=MAX_FETCH_BATCH_SIZE,
        help=f"PMIDs per EFetch request, up to {MAX_FETCH_BATCH_SIZE}.",
    )
    parser.add_argument(
        "--email",
        default=os.getenv("NCBI_EMAIL"),
        help="Contact email sent to NCBI; defaults to NCBI_EMAIL.",
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv("NCBI_API_KEY"),
        help="NCBI API key; defaults to NCBI_API_KEY.",
    )
    parser.add_argument(
        "--tool",
        default=os.getenv("NCBI_TOOL", DEFAULT_TOOL),
        help="Tool name sent to NCBI; defaults to NCBI_TOOL.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP timeout in seconds.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=4,
        help="Retries for transient network and server errors.",
    )
    parser.add_argument(
        "--output",
        default="-",
        help="Output JSON path, or '-' for standard output.",
    )
    parser.add_argument(
        "--jsonl",
        action="store_true",
        help="Write one compact JSON document per line instead of a JSON array.",
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Write compact JSON when not using --jsonl.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run offline mapper/schema tests and exit.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_argument_parser()
    args = parser.parse_args(argv)

    if args.self_test:
        run_self_test()
        return 0

    try:
        if args.retries < 0:
            raise ValueError("--retries cannot be negative.")
        if args.timeout <= 0:
            raise ValueError("--timeout must be greater than zero.")
        if not 1 <= args.batch_size <= MAX_FETCH_BATCH_SIZE:
            raise ValueError(
                f"--batch-size must be between 1 and {MAX_FETCH_BATCH_SIZE}."
            )

        mapper = PubMedXMLMapper()

        if args.xml_file:
            if args.query or args.pmid or args.pmid_file:
                raise ValueError(
                    "--xml-file cannot be combined with --query, --pmid, or --pmid-file."
                )
            documents = mapper.parse(args.xml_file.read_bytes())
        else:
            supplied_pmids = [item for group in args.pmid for item in group]
            if args.pmid_file:
                supplied_pmids.extend(_read_pmids_file(args.pmid_file))

            client = PubMedClient(
                email=args.email,
                api_key=args.api_key,
                tool=args.tool,
                timeout_seconds=args.timeout,
                max_retries=args.retries,
            )

            if args.query:
                supplied_pmids.extend(
                    client.search(args.query, max_results=args.max_results)
                )

            pmids = _deduplicate_pmids(supplied_pmids)
            if not pmids:
                raise ValueError(
                    "Provide --pmid, --pmid-file, --query, or --xml-file."
                )

            documents = retrieve_documents(
                client,
                mapper,
                pmids,
                batch_size=args.batch_size,
            )
            retrieved_ids = {
                document.document_id.removeprefix("pubmed-") for document in documents
            }
            missing = [pmid for pmid in pmids if pmid not in retrieved_ids]
            if missing:
                print(
                    "Warning: NCBI returned no supported PubMed record for PMID(s): "
                    + ", ".join(missing),
                    file=sys.stderr,
                )

        _write_documents(
            documents,
            output=args.output,
            json_lines=args.jsonl,
            compact=args.compact,
        )
        return 0

    except (PubMedError, ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
