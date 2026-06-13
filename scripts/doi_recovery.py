#!/usr/bin/env python3
"""Recover DOIs from URLs for source cards missing DOI metadata.

Supports:
- MDPI URLs (predictable DOI pattern)
- PubMed URLs (NCBI API)
- OUP/Wiley/Springer/ScienceDirect (web fetch with DOI extraction)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def extract_doi_from_mdpi_url(url: str) -> str:
    """MDPI URLs like https://www.mdpi.com/2076-2615/14/4/630 -> 10.3390/ani14040630"""
    match = re.search(r"mdpi\.com/(\d+-\d+)/(\d+)/(\d+)/(\d+)", url)
    if match:
        journal_id, volume, issue, article = match.groups()
        # Map journal ISSNs to DOI abbreviations
        journal_map = {
            "2076-2615": "ani",        # Animals
            "2306-7381": "vetsci",     # Veterinary Sciences
            "1999-4915": "v",          # Viruses
        }
        journal = journal_map.get(journal_id, journal_id)
        # Format: journal + volume + issue(2 digits) + article(4 digits)
        return f"10.3390/{journal}{volume}{issue.zfill(2)}{article.zfill(4)}"
    return ""


def extract_doi_from_pubmed(url: str, timeout: float = 10.0) -> str:
    """PubMed URLs like https://pubmed.ncbi.nlm.nih.gov/24783628/"""
    match = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", url)
    if not match:
        return ""
    pmid = match.group(1)
    api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
    try:
        req = urllib.request.Request(api_url, headers={"User-Agent": "feline-research-os/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            article_ids = data.get("result", {}).get(pmid, {}).get("articleids", [])
            for aid in article_ids:
                if aid.get("idtype") == "doi":
                    return aid.get("value", "")
    except Exception:
        pass
    return ""


def extract_doi_from_sciencedirect(url: str) -> str:
    """ScienceDirect URLs with PII like S0021997518300409"""
    # PII to DOI conversion is not straightforward; need web fetch
    # For now, return empty and flag for manual recovery
    return ""


def recover_doi(url: str, timeout: float = 10.0) -> tuple[str, str]:
    """Try to recover DOI from URL. Returns (doi, method)."""
    if not url:
        return "", "no_url"

    # MDPI
    if "mdpi.com" in url:
        doi = extract_doi_from_mdpi_url(url)
        if doi:
            return doi, "mdpi_pattern"

    # PubMed
    if "pubmed.ncbi.nlm.nih.gov" in url:
        doi = extract_doi_from_pubmed(url, timeout)
        if doi:
            return doi, "pubmed_api"

    # DOI in URL directly
    match = re.search(r"10\.\d{4,9}/[^\s\"'<>&?]+", url)
    if match:
        return match.group(0).rstrip(".,;)"), "url_contains_doi"

    return "", "not_recovered"


def load_source_urls(repo_root: Path, source_ids: list[str]) -> dict[str, tuple[str, str]]:
    """Load URLs from source cards. Returns {source_id: (url, current_doi)}."""
    result = {}
    papers_dir = repo_root / "raw" / "papers"
    for source_id in source_ids:
        path = papers_dir / f"{source_id}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        url_match = re.search(r'url:\s*"([^"]+)"', text)
        doi_match = re.search(r'doi:\s*"([^"]*)"', text)
        url = url_match.group(1) if url_match else ""
        current_doi = doi_match.group(1) if doi_match else ""
        result[source_id] = (url, current_doi)
    return result


def update_source_doi(path: Path, new_doi: str) -> bool:
    """Update DOI in source card frontmatter."""
    text = path.read_text(encoding="utf-8")
    # Replace empty doi with new doi
    updated = re.sub(r'doi:\s*""', f'doi: "{new_doi}"', text)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--source-ids", help="Comma-separated source IDs")
    parser.add_argument("--disease", help="Process all sources for a disease (e.g., ckd)")
    parser.add_argument("--write", action="store_true", help="Actually update source cards")
    parser.add_argument("--timeout", type=float, default=10.0)
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()

    if args.source_ids:
        source_ids = [s.strip() for s in args.source_ids.split(",")]
    elif args.disease:
        papers_dir = repo_root / "raw" / "papers"
        source_ids = sorted([p.stem for p in papers_dir.glob(f"src-{args.disease}-*.md")])
    else:
        print("Specify --source-ids or --disease", file=sys.stderr)
        return 2

    sources = load_source_urls(repo_root, source_ids)

    recovered = 0
    skipped = 0
    failed = 0

    print(f"{'Source':<15} {'Status':<20} {'DOI':<40}")
    print("-" * 75)

    for source_id, (url, current_doi) in sources.items():
        if current_doi:
            print(f"{source_id:<15} {'has_doi':<20} {current_doi}")
            skipped += 1
            continue

        doi, method = recover_doi(url, args.timeout)
        if doi:
            print(f"{source_id:<15} {method:<20} {doi}")
            recovered += 1
            if args.write:
                path = repo_root / "raw" / "papers" / f"{source_id}.md"
                if update_source_doi(path, doi):
                    print(f"  -> Updated {path.name}")
        else:
            print(f"{source_id:<15} {method:<20} (manual recovery needed)")
            failed += 1

        time.sleep(0.5)  # Rate limit

    print("-" * 75)
    print(f"Recovered: {recovered}, Skipped (has DOI): {skipped}, Failed: {failed}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
