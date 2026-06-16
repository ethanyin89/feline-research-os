#!/usr/bin/env python3
"""
scripts/search.py — Full-text search across the feline research OS vault.

Usage (CLI):
    python scripts/search.py "phosphorus binder" [--scope raw|topics|system|all] [--limit 10]

Usage (imported by query.py or other agents):
    from search import vault_search
    results = vault_search("phosphorus binder", scope="raw", limit=5)

This fills the "naive search engine" layer from Karpathy's LLM wiki architecture.
No vector DB, no embeddings — just fast substring/regex matching over .md files
with source-id extraction and snippet context.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional

VAULT_ROOT = Path(__file__).parent.parent

# Directories mapped to scope keywords
_SCOPE_DIRS: dict[str, list[str]] = {
    "raw": ["raw"],
    "topics": ["topics"],
    "system": ["system"],
    "entities": ["entities"],
    "all": ["raw", "topics", "system", "entities", "outputs"],
}

# Max snippet chars on each side of a match
_SNIPPET_RADIUS = 120


def _extract_id_from_frontmatter(content: str) -> Optional[str]:
    """Pull the `id:` field from YAML frontmatter, if present."""
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    for line in content[3:end].splitlines():
        if line.startswith("id:"):
            return line.split(":", 1)[1].strip().strip("\"'")
    return None


def _extract_title_from_frontmatter(content: str) -> Optional[str]:
    """Pull the `title:` field from YAML frontmatter, if present."""
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    for line in content[3:end].splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().strip("\"'")
    return None


def _build_snippet(content: str, match_start: int, match_end: int) -> str:
    """Build a context snippet around a match position."""
    start = max(0, match_start - _SNIPPET_RADIUS)
    end = min(len(content), match_end + _SNIPPET_RADIUS)
    snippet = content[start:end].replace("\n", " ").strip()
    prefix = "..." if start > 0 else ""
    suffix = "..." if end < len(content) else ""
    return f"{prefix}{snippet}{suffix}"


def _extract_int_from_frontmatter(content: str, field: str) -> Optional[int]:
    """Extract an integer field from frontmatter."""
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    for line in content[3:end].splitlines():
        if line.startswith(f"{field}:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                return None
    return None


def _extract_float_from_frontmatter(content: str, field: str) -> Optional[float]:
    """Extract a float field from frontmatter."""
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    for line in content[3:end].splitlines():
        if line.startswith(f"{field}:"):
            try:
                return float(line.split(":", 1)[1].strip())
            except ValueError:
                return None
    return None


def vault_search(
    query: str,
    vault_root: Path = VAULT_ROOT,
    scope: str = "all",
    limit: int = 20,
    case_sensitive: bool = False,
    sort_by: str = "relevance",
) -> list[dict]:
    """
    Search .md files in the vault for a query string (plain text or regex).

    Args:
        query: Search query (plain text or regex)
        vault_root: Root path of the vault
        scope: Search scope (raw, topics, system, all)
        limit: Maximum number of results
        case_sensitive: Whether to match case
        sort_by: Sort order - "relevance", "year_desc", "citations_desc", "if_desc"

    Returns a list of result dicts:
      {
        "file": str,              # vault-relative path
        "id": str | None,         # frontmatter id if present
        "title": str | None,      # frontmatter title if present
        "matches": int,           # number of matches in file
        "snippets": list[str],    # up to 3 context snippets
        "year": int | None,       # publication year
        "citation_count": int | None,  # citation count
        "impact_factor": float | None, # journal impact factor
      }
    """
    dirs = _SCOPE_DIRS.get(scope, _SCOPE_DIRS["all"])
    flags = 0 if case_sensitive else re.IGNORECASE

    try:
        pattern = re.compile(query, flags)
    except re.error:
        # Fall back to literal match if query isn't valid regex
        pattern = re.compile(re.escape(query), flags)

    results: list[dict] = []

    for dir_name in dirs:
        search_dir = vault_root / dir_name
        if not search_dir.exists():
            continue
        for md_file in search_dir.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue

            matches = list(pattern.finditer(content))
            if not matches:
                continue

            rel_path = str(md_file.relative_to(vault_root))
            doc_id = _extract_id_from_frontmatter(content)
            title = _extract_title_from_frontmatter(content)

            # Extract researcher-facing metadata
            year = _extract_int_from_frontmatter(content, "year")
            citation_count = _extract_int_from_frontmatter(content, "citation_count")
            impact_factor = _extract_float_from_frontmatter(content, "impact_factor")

            # Build up to 3 snippets from the first 3 matches
            snippets = []
            for m in matches[:3]:
                snippets.append(_build_snippet(content, m.start(), m.end()))

            results.append({
                "file": rel_path,
                "id": doc_id,
                "title": title,
                "matches": len(matches),
                "snippets": snippets,
                "year": year,
                "citation_count": citation_count,
                "impact_factor": impact_factor,
            })

    # Sort based on sort_by parameter
    if sort_by == "year_desc":
        # Sort by year descending (newest first), then by matches for ties
        results.sort(key=lambda r: (-(r["year"] or 0), -r["matches"], r["file"]))
    elif sort_by == "citations_desc":
        # Sort by citation count descending, then by matches for ties
        results.sort(key=lambda r: (-(r["citation_count"] or 0), -r["matches"], r["file"]))
    elif sort_by == "if_desc":
        # Sort by impact factor descending, then by matches for ties
        results.sort(key=lambda r: (-(r["impact_factor"] or 0), -r["matches"], r["file"]))
    else:
        # Default: sort by match count descending (relevance)
        results.sort(key=lambda r: (-r["matches"], r["file"]))

    return results[:limit]


def format_results_for_llm(results: list[dict]) -> str:
    """
    Format search results as a text block suitable for injection into
    an LLM context window. Compact, structured, parseable.
    """
    if not results:
        return "No results found."

    lines = [f"SEARCH RESULTS ({len(results)} files):\n"]
    for i, r in enumerate(results, 1):
        id_tag = f" [{r['id']}]" if r["id"] else ""
        title_tag = f" — {r['title']}" if r["title"] else ""
        lines.append(f"{i}. {r['file']}{id_tag}{title_tag} ({r['matches']} matches)")
        for snippet in r["snippets"]:
            lines.append(f"   > {snippet}")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Full-text search across the feline research OS vault.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("query", help="Search query (plain text or regex)")
    parser.add_argument(
        "--scope",
        choices=["raw", "topics", "system", "entities", "all"],
        default="all",
        help="Limit search to a specific directory scope (default: all)",
    )
    parser.add_argument(
        "--limit", type=int, default=20,
        help="Maximum number of results to return (default: 20)",
    )
    parser.add_argument(
        "--case-sensitive", action="store_true",
        help="Enable case-sensitive matching",
    )
    parser.add_argument(
        "--llm-format", action="store_true",
        help="Output in compact format suitable for LLM context injection",
    )
    args = parser.parse_args()

    results = vault_search(
        args.query,
        scope=args.scope,
        limit=args.limit,
        case_sensitive=args.case_sensitive,
    )

    if args.llm_format:
        print(format_results_for_llm(results))
    else:
        if not results:
            print("No results found.")
            sys.exit(0)

        print(f"\n{'='*60}")
        print(f"  Search: \"{args.query}\"  |  Scope: {args.scope}  |  {len(results)} results")
        print(f"{'='*60}\n")

        for i, r in enumerate(results, 1):
            id_tag = f"  [{r['id']}]" if r["id"] else ""
            title_tag = f"  {r['title']}" if r["title"] else ""
            print(f"  {i}. {r['file']}{id_tag}{title_tag}")
            print(f"     ({r['matches']} match{'es' if r['matches'] != 1 else ''})")
            for snippet in r["snippets"]:
                print(f"     > {snippet[:200]}")
            print()


if __name__ == "__main__":
    main()
