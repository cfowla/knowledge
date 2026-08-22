from __future__ import annotations

from .detection import SourceKind, detect_source
from .extractors.arxiv import ArxivExtractor
from .extractors.base import AbstractExtractor
from .extractors.pubmed import PubmedExtractor
from .models import ParsedDocument
from .validation import validate_document


_EXTRACTORS: dict[SourceKind, AbstractExtractor] = {
    SourceKind.ARXIV: ArxivExtractor(),
    SourceKind.PUBMED: PubmedExtractor(),
}


def parse_abstract_html(html: str, source_url: str | None = None) -> ParsedDocument:
    source = detect_source(html, source_url)
    document = _EXTRACTORS[source].extract(html, source_url)
    return validate_document(document)
