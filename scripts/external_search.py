#!/usr/bin/env python3
"""
scripts/external_search.py — Gated external source search for feline research OS.

This module provides a controlled interface for external literature searches
(PubMed, Crossref, etc.). External searches are gated and only run when
explicitly requested, never automatically.

Usage:
    from external_search import search_pubmed, search_crossref, ExternalSearchConfig

    # External search requires explicit opt-in
    config = ExternalSearchConfig(allow_external=True, max_results=10)
    results = search_pubmed("feline CKD phosphorus", config)

CLI:
    python scripts/external_search.py pubmed "feline CKD phosphorus" --max-results 10
    python scripts/external_search.py crossref "feline infectious peritonitis" --max-results 5
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
import urllib.parse
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path
from typing import Optional

VAULT_ROOT = Path(__file__).parent.parent


@dataclass
class ExternalSearchConfig:
    """Configuration for external searches with explicit gating."""
    allow_external: bool = False  # Must be explicitly set to True
    max_results: int = 10
    timeout_seconds: int = 30
    user_confirmed: bool = False  # UI confirmation received


@dataclass
class ExternalSearchResult:
    """Single result from external search."""
    source: str  # pubmed, crossref
    title: str
    authors: list[str]
    year: str
    doi: str
    pmid: str  # PubMed ID if available
    abstract: str
    journal: str
    relevance_score: float  # 0-1, search engine ranking


@dataclass
class ExternalSearchResponse:
    """Response from external search."""
    query: str
    source: str
    results: list[ExternalSearchResult]
    total_found: int
    search_time_ms: int
    gated: bool  # Whether this was a gated/controlled search
    error: Optional[str] = None


def _check_gate(config: ExternalSearchConfig) -> Optional[str]:
    """Check if external search is allowed. Returns error message if blocked."""
    if not config.allow_external:
        return (
            "External search is disabled. External searches only run when explicitly "
            "requested by the user. Set allow_external=True to enable."
        )
    return None


def search_pubmed(query: str, config: ExternalSearchConfig) -> ExternalSearchResponse:
    """
    Search PubMed for feline veterinary literature.

    This function is GATED - it will not run unless config.allow_external is True.
    This prevents accidental external API calls and ensures searches are intentional.

    Args:
        query: Search query
        config: Search configuration with gating controls

    Returns:
        ExternalSearchResponse with results or error
    """
    gate_error = _check_gate(config)
    if gate_error:
        return ExternalSearchResponse(
            query=query,
            source="pubmed",
            results=[],
            total_found=0,
            search_time_ms=0,
            gated=True,
            error=gate_error,
        )

    import time
    start = time.time()

    # Build PubMed E-utilities search URL
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": config.max_results,
        "retmode": "json",
        "sort": "pub_date",  # Sort by publication date (newest first)
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    try:
        with urllib.request.urlopen(url, timeout=config.timeout_seconds) as response:
            data = json.loads(response.read().decode("utf-8"))

        pmids = data.get("esearchresult", {}).get("idlist", [])
        total_found = int(data.get("esearchresult", {}).get("count", 0))

        # Fetch details for each PMID
        results = []
        if pmids:
            results = _fetch_pubmed_details(pmids, config.timeout_seconds)

        elapsed_ms = int((time.time() - start) * 1000)

        return ExternalSearchResponse(
            query=query,
            source="pubmed",
            results=results,
            total_found=total_found,
            search_time_ms=elapsed_ms,
            gated=True,
        )

    except Exception as e:
        return ExternalSearchResponse(
            query=query,
            source="pubmed",
            results=[],
            total_found=0,
            search_time_ms=0,
            gated=True,
            error=f"PubMed search failed: {e}",
        )


def _fetch_pubmed_details(pmids: list[str], timeout: int) -> list[ExternalSearchResult]:
    """Fetch article details for a list of PMIDs."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json",
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    # Fetch abstracts via efetch (batch request)
    abstracts_map = {}
    efetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={','.join(pmids)}&retmode=xml"
    try:
        req = urllib.request.Request(efetch_url, headers={"User-Agent": "feline-research-os/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            xml_data = response.read().decode("utf-8")
        articles = re.findall(r"<PubmedArticle>.*?</PubmedArticle>", xml_data, re.DOTALL)
        for art in articles:
            pmid_match = re.search(r"<PMID[^>]*>(\d+)</PMID>", art)
            if pmid_match:
                p_id = pmid_match.group(1)
                abstract_parts = []
                for match in re.finditer(r"<AbstractText[^>]*>(.*?)</AbstractText>", art, re.DOTALL):
                    text = match.group(1)
                    text = re.sub(r"<[^>]+>", "", text)
                    abstract_parts.append(text.strip())
                if abstract_parts:
                    abstracts_map[p_id] = " ".join(abstract_parts)
    except Exception as e:
        print(f"Error fetching abstracts via efetch: {e}")

    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))

        result_data = data.get("result", {})
        results = []
        for i, pmid in enumerate(pmids):
            article = result_data.get(pmid, {})
            if not article or not isinstance(article, dict) or "error" in article:
                continue

            # Extract DOI from article IDs
            doi = ""
            for aid in article.get("articleids", []):
                if aid.get("idtype") == "doi":
                    doi = aid.get("value", "")
                    break

            results.append(ExternalSearchResult(
                source="pubmed",
                title=article.get("title", ""),
                authors=[a.get("name", "") for a in article.get("authors", [])[:5]],
                year=article.get("pubdate", "")[:4],
                doi=doi,
                pmid=pmid,
                abstract=abstracts_map.get(pmid, ""),
                journal=article.get("fulljournalname", ""),
                relevance_score=1.0 - (i / len(pmids)),  # Rank-based score
            ))

        return results

    except Exception:
        return []


def search_crossref(query: str, config: ExternalSearchConfig) -> ExternalSearchResponse:
    """
    Search Crossref for veterinary literature.

    This function is GATED - it will not run unless config.allow_external is True.

    Args:
        query: Search query
        config: Search configuration with gating controls

    Returns:
        ExternalSearchResponse with results or error
    """
    gate_error = _check_gate(config)
    if gate_error:
        return ExternalSearchResponse(
            query=query,
            source="crossref",
            results=[],
            total_found=0,
            search_time_ms=0,
            gated=True,
            error=gate_error,
        )

    import time
    start = time.time()

    # Detect direct DOI query to fetch exact metadata
    is_doi = bool(re.match(r"^10\.\d{4,9}/[-._;()/:A-Z0-9]+$", query.strip(), re.I))
    if is_doi:
        url = f"https://api.crossref.org/works/{urllib.parse.quote(query.strip())}"
    else:
        base_url = "https://api.crossref.org/works"
        params = {
            "query": query,
            "rows": config.max_results,
            "filter": "type:journal-article",
        }
        url = f"{base_url}?{urllib.parse.urlencode(params)}"

    headers = {
        "User-Agent": "feline-research-os/1.0 (https://github.com/feline-research-os; mailto:research@example.com)",
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=config.timeout_seconds) as response:
            data = json.loads(response.read().decode("utf-8"))

        if is_doi:
            items = [data.get("message", {})] if "message" in data else []
            total_found = len(items)
        else:
            items = data.get("message", {}).get("items", [])
            total_found = data.get("message", {}).get("total-results", 0)

        results = []
        for i, item in enumerate(items):
            # Extract year from published date
            year = ""
            published = item.get("published-print") or item.get("published-online")
            if published and "date-parts" in published:
                parts = published["date-parts"]
                if parts and parts[0]:
                    year = str(parts[0][0])

            # Extract authors
            authors = []
            for author in item.get("author", [])[:5]:
                name = f"{author.get('given', '')} {author.get('family', '')}".strip()
                if name:
                    authors.append(name)

            results.append(ExternalSearchResult(
                source="crossref",
                title=item.get("title", [""])[0] if item.get("title") else "",
                authors=authors,
                year=year,
                doi=item.get("DOI", ""),
                pmid="",
                abstract=item.get("abstract", ""),
                journal=item.get("container-title", [""])[0] if item.get("container-title") else "",
                relevance_score=item.get("score", 0) / 100 if item.get("score") else 1.0 - (i / len(items)),
            ))

        elapsed_ms = int((time.time() - start) * 1000)

        return ExternalSearchResponse(
            query=query,
            source="crossref",
            results=results,
            total_found=total_found,
            search_time_ms=elapsed_ms,
            gated=True,
        )

    except Exception as e:
        return ExternalSearchResponse(
            query=query,
            source="crossref",
            results=[],
            total_found=0,
            search_time_ms=0,
            gated=True,
            error=f"Crossref search failed: {e}",
        )


def generate_intake_stubs(
    results: list[ExternalSearchResult],
    disease: str,
    output_dir: Optional[Path] = None,
) -> list[Path]:
    """
    Generate source card stubs from external search results.

    These are draft files that need human review before extraction.

    Args:
        results: External search results
        disease: Disease code (ckd, fip, etc.)
        output_dir: Directory for stubs (default: system/intake-queue/)

    Returns:
        List of generated stub file paths
    """
    if output_dir is None:
        output_dir = VAULT_ROOT / "system" / "intake-queue"
    output_dir.mkdir(parents=True, exist_ok=True)

    stub_paths = []
    for i, result in enumerate(results):
        # Generate stub filename
        safe_title = re.sub(r"[^\w\s-]", "", result.title[:50]).strip().replace(" ", "-").lower()
        filename = f"stub-{disease}-{date.today().isoformat()}-{i+1:02d}-{safe_title}.md"

        stub_content = f"""---
status: intake_stub
source: {result.source}
doi: "{result.doi}"
pmid: "{result.pmid}"
title: "{result.title}"
authors: {json.dumps(result.authors)}
year: "{result.year}"
journal: "{result.journal}"
disease: {disease}
created_at: {date.today().isoformat()}
---

# Intake Stub: {result.title}

**Status:** Needs review before extraction

## Source Info

- **DOI:** {result.doi}
- **PMID:** {result.pmid}
- **Journal:** {result.journal}
- **Year:** {result.year}
- **Authors:** {', '.join(result.authors)}

## Abstract

{result.abstract or "_Abstract not available in search results. Fetch from source._"}

## Review Checklist

- [ ] Confirm this is feline-specific or has feline subgroup data
- [ ] Confirm this is relevant to {disease.upper()} evidence
- [ ] Confirm this is not a duplicate of existing source cards
- [ ] If approved, run full extraction to create src-{disease}-XXX.md

## Notes

_Add review notes here._
"""

        stub_path = output_dir / filename
        stub_path.write_text(stub_content, encoding="utf-8")
        stub_paths.append(stub_path)

    return stub_paths


def format_search_results_markdown(response: ExternalSearchResponse) -> str:
    """Format search response as markdown for display."""
    lines = [
        f"# External Search: {response.source.upper()}",
        "",
        f"**Query:** {response.query}",
        f"**Results:** {len(response.results)} of {response.total_found} total",
        f"**Time:** {response.search_time_ms}ms",
        "",
    ]

    if response.error:
        lines.append(f"**Error:** {response.error}")
        lines.append("")

    if response.results:
        lines.append("## Results")
        lines.append("")
        for i, result in enumerate(response.results, 1):
            lines.append(f"### {i}. {result.title}")
            lines.append("")
            lines.append(f"- **Authors:** {', '.join(result.authors[:3])}{'...' if len(result.authors) > 3 else ''}")
            lines.append(f"- **Year:** {result.year}")
            lines.append(f"- **Journal:** {result.journal}")
            if result.doi:
                lines.append(f"- **DOI:** [{result.doi}](https://doi.org/{result.doi})")
            if result.pmid:
                lines.append(f"- **PMID:** [{result.pmid}](https://pubmed.ncbi.nlm.nih.gov/{result.pmid}/)")
            lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gated external source search for feline research OS.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Search source")

    # PubMed search
    pubmed_parser = subparsers.add_parser("pubmed", help="Search PubMed")
    pubmed_parser.add_argument("query", help="Search query")
    pubmed_parser.add_argument("--max-results", "-n", type=int, default=10, help="Max results")
    pubmed_parser.add_argument("--generate-stubs", action="store_true", help="Generate intake stubs")
    pubmed_parser.add_argument("--disease", "-d", help="Disease for stub generation")

    # Crossref search
    crossref_parser = subparsers.add_parser("crossref", help="Search Crossref")
    crossref_parser.add_argument("query", help="Search query")
    crossref_parser.add_argument("--max-results", "-n", type=int, default=10, help="Max results")
    crossref_parser.add_argument("--generate-stubs", action="store_true", help="Generate intake stubs")
    crossref_parser.add_argument("--disease", "-d", help="Disease for stub generation")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # External search requires explicit opt-in via CLI
    config = ExternalSearchConfig(allow_external=True, max_results=args.max_results)

    if args.command == "pubmed":
        response = search_pubmed(args.query, config)
    elif args.command == "crossref":
        response = search_crossref(args.query, config)
    else:
        parser.print_help()
        return

    print(format_search_results_markdown(response))

    if args.generate_stubs and response.results:
        disease = args.disease or "unknown"
        stub_paths = generate_intake_stubs(response.results, disease)
        print(f"\n## Generated {len(stub_paths)} intake stubs")
        for path in stub_paths:
            print(f"- {path.relative_to(VAULT_ROOT)}")


if __name__ == "__main__":
    main()
