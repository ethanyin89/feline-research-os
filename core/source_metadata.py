"""Pure source-card metadata loading for presentation adapters."""

from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Any, Iterable

import yaml


def frontmatter_block(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def frontmatter_yaml(text: str) -> dict[str, Any]:
    """Parse YAML frontmatter with safe fallback."""
    block = frontmatter_block(text)
    if not block:
        return {}
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def frontmatter_scalar(text: str, key: str) -> str:
    block = frontmatter_block(text)
    match = re.search(rf"^{re.escape(key)}:\s*(.*?)\s*$", block, re.M)
    return match.group(1).strip().strip("\"'") if match else ""


def frontmatter_text(text: str, key: str) -> str:
    """Read a scalar frontmatter value, including YAML block scalars."""
    block = frontmatter_block(text)
    block_match = re.search(rf"^{re.escape(key)}:\s*[|>]\s*$", block, re.M)
    if block_match:
        values = []
        for line in block[block_match.end():].splitlines():
            if line and not line.startswith((" ", "\t")):
                break
            values.append(line[2:] if line.startswith("  ") else line.lstrip())
        return "\n".join(values).strip()
    return frontmatter_scalar(text, key)


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


def nested_frontmatter_list(text: str, section: str, key: str) -> list[str]:
    """Read a simple list nested one level inside a frontmatter section."""
    block = frontmatter_block(text)
    in_section = False
    in_key = False
    values = []

    for line in block.splitlines():
        if re.match(r"^\S[^:]*:", line):
            current = line.split(":", 1)[0].strip()
            in_section = current == section
            in_key = False
            continue
        if not in_section:
            continue

        key_match = re.match(rf"^\s+{re.escape(key)}:\s*$", line)
        if key_match:
            in_key = True
            continue
        inline_match = re.match(rf"^\s+{re.escape(key)}:\s*\[(.*?)\]\s*$", line)
        if inline_match:
            return [
                item.strip().strip("\"'")
                for item in inline_match.group(1).split(",")
                if item.strip()
            ]

        if in_key:
            item = re.match(r"^\s+-\s*(.+?)\s*$", line)
            if item:
                values.append(item.group(1).strip().strip("\"'"))
                continue
            if re.match(r"^\s+\S[^:]*:", line):
                break

    return values


def _parse_int(value: str) -> int | None:
    """Parse integer from string, return None if invalid."""
    if not value:
        return None
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def _parse_float(value: str) -> float | None:
    """Parse float from string, return None if invalid or inf/nan."""
    if not value:
        return None
    try:
        result = float(value)
        # Reject inf and nan values
        if math.isinf(result) or math.isnan(result):
            return None
        return result
    except (ValueError, TypeError):
        return None


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


def _normalize_source_passages(value: Any) -> list[dict[str, Any]]:
    """Keep only well-formed source passage dictionaries."""
    if not isinstance(value, list):
        return []
    passages: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, dict):
            continue
        quoted = str(item.get("quoted_passage", "")).strip()
        highlight = str(item.get("highlight_text", "")).strip()
        if not quoted or not highlight:
            continue
        passages.append({
            "passage_id": str(item.get("passage_id", "")).strip(),
            "section": str(item.get("section", "")).strip(),
            "quoted_passage": quoted,
            "highlight_text": highlight,
            "supports_claim_types": item.get("supports_claim_types", []),
            "evidence_type": str(item.get("evidence_type", "")).strip(),
            "chinese_explanation": str(item.get("chinese_explanation", "")).strip(),
            "why_it_supports": str(item.get("why_it_supports", "")).strip(),
        })
    return passages


def _load_linked_source_passages(path: Path, local_assets: list[str]) -> list[dict[str, Any]]:
    """Load passage traces from linked deep-extraction frontmatter."""
    for asset in local_assets:
        asset_path = (path.parent / asset).resolve()
        try:
            if not asset_path.exists():
                continue
            data = frontmatter_yaml(asset_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError):
            continue
        passages = _normalize_source_passages(data.get("source_passages"))
        if passages:
            return passages
    return []


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

    fm = frontmatter_yaml(text)
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
    local_assets = (
        frontmatter_list(text, "local_assets")
        or nested_frontmatter_list(text, "links", "local_assets")
    )
    publish_date = frontmatter_scalar(text, "publish_date") or frontmatter_scalar(text, "date")
    source_passages = _normalize_source_passages(fm.get("source_passages"))
    if not source_passages and local_assets:
        source_passages = _load_linked_source_passages(path, local_assets)

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
        "extraction_depth": frontmatter_scalar(text, "extraction_depth") or "unknown",
        "safe_claim_types": frontmatter_list(text, "safe_claim_types"),
        "prohibited_claim_types": frontmatter_list(text, "prohibited_claim_types"),
        "limitations": frontmatter_list(text, "limitations"),
        "superseded_by": frontmatter_scalar(text, "superseded_by"),
        "journal": frontmatter_scalar(text, "journal"),
        # Researcher-facing metadata (enriched from external APIs)
        "citation_count": _parse_int(frontmatter_scalar(text, "citation_count")),
        "impact_factor": _parse_float(frontmatter_scalar(text, "impact_factor")),
        "abstract_text": frontmatter_text(text, "abstract") or "",
        "methods_summary": frontmatter_scalar(text, "methods_summary") or "",
        "reference_ids": frontmatter_list(text, "references"),
        "quoted_facts": nested_frontmatter_list(text, "evidence_policy", "quoted_fact"),
        "supported_conclusions": nested_frontmatter_list(text, "evidence_policy", "source_supported_conclusion"),
        "llm_inferences": nested_frontmatter_list(text, "evidence_policy", "llm_inference"),
        "source_passages": source_passages,
        "metadata_enriched": frontmatter_scalar(text, "metadata_enriched"),
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
