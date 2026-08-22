import pytest
from scholar_acquire.models import ArticleIdentifier, IdentifierKind
from scholar_acquire.errors import IdentifierError


def test_parse_pmid():
    x = ArticleIdentifier.parse("PMID: 12345678")
    assert x.kind == IdentifierKind.PMID
    assert x.value == "12345678"


def test_parse_doi_url():
    x = ArticleIdentifier.parse("https://doi.org/10.1000/ABC.123")
    assert x.kind == IdentifierKind.DOI
    assert x.value == "10.1000/abc.123"


def test_parse_pmcid():
    x = ArticleIdentifier.parse("PMC1234567.2")
    assert x.kind == IdentifierKind.PMCID
    assert x.value == "PMC1234567.2"


def test_reject_unknown():
    with pytest.raises(IdentifierError):
        ArticleIdentifier.parse("not-an-id")
