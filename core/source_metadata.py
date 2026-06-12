"""Pure source-card metadata loading for presentation adapters."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable


def frontmatter_block(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def frontmatter_scalar(text: str, key: str) -> str:
    block = frontmatter_block(text)
    match = re.search(rf"^{re.escape(key)}:\s*(.*?)\s*$", block, re.M)
    return match.group(1).strip().strip("\"'") if match else ""


def frontmatter_list(text: str, key: str) -> list[str]:
    block = frontmatter_block(text)
    inline = re.search(rf"^{re.escape(key)}:\s*\[(.*?)\]\s*$", block, re.M)
    if inline:
        return [
            item.strip().strip("\"'")
            for item in inline.group(1).split(",")
            if item.strip()
        ]

    start = re.search(rf"^{re.escape(key)}:\s*$", block, re.M)
    if not start:
        return []
    values = []
    for line in block[start.end():].splitlines():
        if re.match(r"^\S[^:]*:", line):
            break
        item = re.match(r"^\s*-\s*(.+?)\s*$", line)
        if item:
            values.append(item.group(1).strip().strip("\"'"))
    return values


def nested_frontmatter_scalar(text: str, section: str, key: str) -> str:
    block = frontmatter_block(text)
    in_section = False
    for line in block.splitlines():
        if re.match(r"^\S[^:]*:", line):
            in_section = line.split(":", 1)[0].strip() == section
            continue
        if not in_section:
            continue
        match = re.match(rf"^\s+{re.escape(key)}:\s*(.*?)\s*$", line)
        if match:
            return match.group(1).strip().strip("\"'")
    return ""


def normalize_doi(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value, flags=re.I)
    return value if value.startswith("10.") else ""


def parse_source_card(path: Path, source_id: str = "") -> dict[str, Any]:
    """Return normalized metadata without promoting missing fields."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {
            "id": source_id or path.stem,
            "source_id": source_id or path.stem,
            "title": "",
            "verification_status": "metadata_unavailable",
        }

    sid = frontmatter_scalar(text, "id") or source_id or path.stem
    doi = normalize_doi(
        frontmatter_scalar(text, "doi")
        or nested_frontmatter_scalar(text, "links", "doi")
    )
    pmid = (
        frontmatter_scalar(text, "pmid")
        or nested_frontmatter_scalar(text, "links", "pmid")
    )
    pmcid = (
        frontmatter_scalar(text, "pmcid")
        or nested_frontmatter_scalar(text, "links", "pmcid")
    )
    url = (
        frontmatter_scalar(text, "url")
        or nested_frontmatter_scalar(text, "links", "url")
    )
    if not url.startswith(("https://", "http://")):
        url = ""

    year_raw = frontmatter_scalar(text, "year")
    try:
        year = int(year_raw) if year_raw else None
    except ValueError:
        year = None

    authors = frontmatter_list(text, "authors")
    tags = frontmatter_list(text, "tags")
    diseases = frontmatter_list(text, "diseases")
    models = frontmatter_list(text, "models")
    endpoints = frontmatter_list(text, "endpoints")
    jurisdictions = frontmatter_list(text, "jurisdictions")
    local_assets = frontmatter_list(text, "local_assets")
    publish_date = frontmatter_scalar(text, "publish_date") or frontmatter_scalar(text, "date")

    return {
        "id": sid,
        "source_id": sid,
        "title": frontmatter_scalar(text, "title"),
        "authors": authors,
        "year": year,
        "publish_date": publish_date,
        "doi": doi,
        "pmid": pmid,
        "pmcid": pmcid,
        "url": url,
        "source_type": (
            frontmatter_scalar(text, "source_kind")
            or frontmatter_scalar(text, "evidence_level")
            or "unknown"
        ),
        "source_kind": frontmatter_scalar(text, "source_kind"),
        "evidence_level": frontmatter_scalar(text, "evidence_level"),
        "species": frontmatter_scalar(text, "species"),
        "decision_grade": frontmatter_scalar(text, "decision_grade"),
        "status": frontmatter_scalar(text, "status"),
        "language_qa_status": frontmatter_scalar(text, "language_qa_status"),
        "tags": tags,
        "diseases": diseases,
        "models": models,
        "endpoints": endpoints,
        "jurisdictions": jurisdictions,
        "local_assets": local_assets,
        "verification_status": (
            frontmatter_scalar(text, "verification_status") or "unknown"
        ),
    }


def find_source_card(vault_root: Path, source_id: str) -> Path | None:
    for directory in ("raw/papers", "raw/regulations"):
        candidate = vault_root / directory / f"{source_id}.md"
        if candidate.exists():
            return candidate
    matches = list((vault_root / "raw").rglob(f"{source_id}.md"))
    return matches[0] if matches else None


def load_source_metadata(vault_root: Path, source_ids: Iterable[str]) -> list[dict[str, Any]]:
    """Load ordered, deduplicated source metadata with explicit missing states."""
    loaded = []
    seen = set()
    for source_id in source_ids:
        if source_id in seen:
            continue
        seen.add(source_id)
        path = find_source_card(vault_root, source_id)
        if path is None:
            loaded.append({
                "id": source_id,
                "source_id": source_id,
                "title": "",
                "verification_status": "metadata_unavailable",
            })
            continue
        loaded.append(parse_source_card(path, source_id))
    return loaded
