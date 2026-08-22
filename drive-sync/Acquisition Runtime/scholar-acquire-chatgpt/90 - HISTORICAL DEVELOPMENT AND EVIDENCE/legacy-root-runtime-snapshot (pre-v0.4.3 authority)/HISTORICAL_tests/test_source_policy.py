import pytest

from scholar_acquire.errors import AccessDeniedError
from scholar_acquire.utils import assert_allowed_url, validate_pdf


def test_scihub_is_rejected():
    with pytest.raises(AccessDeniedError):
        assert_allowed_url("https://sci-hub.example/10.1/x")


def test_mislabeled_html_is_not_pdf():
    with pytest.raises(Exception):
        validate_pdf(b"<html>login</html>", "application/pdf")
