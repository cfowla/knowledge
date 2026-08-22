from __future__ import annotations

import html
import re
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

from bs4 import BeautifulSoup

from .errors import AccessDeniedError, ContentValidationError

_FORBIDDEN_HOST_FRAGMENTS = ("sci-hub.", "scihub.")
_PAYWALL_MARKERS = (
    "purchase this article",
    "rent this article",
    "institutional access",
    "sign in to access",
    "subscribe to read",
    "access through your institution",
)


def assert_allowed_url(url: str) -> None:
    host = (urlsplit(url).hostname or "").lower()
    if any(fragment in host for fragment in _FORBIDDEN_HOST_FRAGMENTS):
        raise AccessDeniedError(f"Forbidden source domain: {host}")


def normalize_url(url: str) -> str:
    parts = urlsplit(html.unescape(url.strip()))
    return urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, ""))


def is_pdf(content: bytes, content_type: str | None = None) -> bool:
    # Content-Type is advisory; publisher error/login pages are sometimes mislabeled as PDFs.
    return content.lstrip().startswith(b"%PDF-")


def validate_pdf(content: bytes, content_type: str | None = None) -> None:
    if not is_pdf(content, content_type):
        raise ContentValidationError("Expected PDF content")
    if b"%%EOF" not in content[-4096:]:
        # Some valid incremental PDFs are unusual, so keep this as a weak check.
        if len(content) < 1024:
            raise ContentValidationError("PDF appears truncated")


def extract_jats_article(xml_bytes: bytes) -> bytes:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as exc:
        raise ContentValidationError("Invalid XML") from exc
    if _local(root.tag) == "article":
        return ET.tostring(root, encoding="utf-8", xml_declaration=True)
    for el in root.iter():
        if _local(el.tag) == "article":
            return ET.tostring(el, encoding="utf-8", xml_declaration=True)
    raise ContentValidationError("No JATS <article> element found")


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def looks_like_fulltext_html(content: bytes, content_type: str | None = None) -> bool:
    if content_type and "html" not in content_type.lower():
        return False
    text = content.decode("utf-8", errors="ignore")
    lower = text.lower()
    if any(marker in lower for marker in _PAYWALL_MARKERS):
        return False
    soup = BeautifulSoup(text, "html.parser")
    candidates = [
        soup.find("article"),
        soup.select_one(".article-body"),
        soup.select_one("#article-body"),
        soup.select_one(".fulltext"),
        soup.select_one("#fulltext"),
    ]
    return any(node and len(node.get_text(" ", strip=True)) >= 1500 for node in candidates)


def pdf_links_from_html(base_url: str, content: bytes) -> list[str]:
    soup = BeautifulSoup(content, "html.parser")
    found: list[str] = []
    meta_names = {
        "citation_pdf_url",
        "eprints.document_url",
        "pdf_url",
        "wkhealth_pdf_url",
        "dc.identifier",
    }
    for meta in soup.find_all("meta"):
        name = (meta.get("name") or meta.get("property") or "").lower()
        value = meta.get("content")
        if value and name in meta_names and (".pdf" in value.lower() or name == "citation_pdf_url"):
            found.append(urljoin(base_url, value))
    for link in soup.find_all("link"):
        href = link.get("href")
        typ = (link.get("type") or "").lower()
        if href and ("pdf" in typ or ".pdf" in href.lower()):
            found.append(urljoin(base_url, href))
    for a in soup.find_all("a", href=True):
        href = a["href"]
        label = a.get_text(" ", strip=True).lower()
        if ".pdf" in href.lower() or re.search(r"\b(pdf|download pdf|full text pdf)\b", label):
            found.append(urljoin(base_url, href))
    out: list[str] = []
    seen: set[str] = set()
    for url in found:
        url = normalize_url(url)
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


def s3_to_https(url: str) -> str:
    if not url.startswith("s3://"):
        return url
    rest = url[5:]
    bucket, _, key = rest.partition("/")
    return f"https://{bucket}.s3.amazonaws.com/{key}"


def link_or_copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        return
    try:
        dst.hardlink_to(src)
    except OSError:
        shutil.copy2(src, dst)
