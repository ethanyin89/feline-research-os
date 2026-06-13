#!/usr/bin/env python3
"""
Batch-extract year metadata for source cards that have DOIs but no year field.

Strategy:
1. Scan all source cards for missing `year:` field
2. Attempt to extract year from DOI string patterns
3. Attempt to extract year from title text (parenthetical years)
4. Write the year back into the frontmatter

This is a safe, non-destructive operation that only adds the `year:` field
when it's missing and can be confidently inferred.
"""

import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
RAW_PAPERS = VAULT_ROOT / "raw" / "papers"


def extract_year_from_doi(doi: str) -> int | None:
    """Try to extract a publication year from a DOI string."""
    if not doi:
        return None

    # Look for 4-digit year in DOI path
    year_match = re.search(r'(?:^|[./\-_])(?:20|19)(\d{2})(?:[./\-_]|$)', doi)
    if year_match:
        year_str = doi[year_match.start():year_match.end()].strip('./-_')
        year_4d = re.search(r'((?:19|20)\d{2})', year_str)
        if year_4d:
            year = int(year_4d.group(1))
            if 1950 <= year <= 2026:
                return year
    
    # More aggressive: look for any 4-digit year in the DOI
    all_years = re.findall(r'((?:19|20)\d{2})', doi)
    if len(all_years) == 1:
        year = int(all_years[0])
        if 1990 <= year <= 2026:
            return year
    
    return None


def extract_year_from_title(title: str) -> int | None:
    """Try to extract a publication year from the title."""
    if not title:
        return None
    
    # Look for year ranges like (1994-2001) or (2010-2020)
    range_match = re.search(r'\((\d{4})[–\-](\d{4})\)', title)
    if range_match:
        end_year = int(range_match.group(2))
        if 1990 <= end_year <= 2026:
            return end_year + 1
    
    # Look for standalone year in parentheses
    year_match = re.search(r'\((\d{4})\)', title)
    if year_match:
        year = int(year_match.group(1))
        if 1980 <= year <= 2026:
            return year
    
    return None


def process_card(card_path: Path, dry_run: bool = True) -> dict | None:
    """Process a single source card, returning info if year was extractable."""
    text = card_path.read_text(encoding="utf-8")
    
    if re.search(r'^year:\s*\d', text, re.MULTILINE):
        return None
    
    doi_match = re.search(r'^\s+doi:\s*["\']?([^"\'"\n]+)', text, re.MULTILINE)
    doi = doi_match.group(1).strip() if doi_match else ""
    
    title_match = re.search(r'^title:\s*["\']?([^"\'"\n]+)', text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""
    
    year = extract_year_from_doi(doi)
    source = "doi"
    if not year:
        year = extract_year_from_title(title)
        source = "title"
    
    if not year:
        return None
    
    if not dry_run:
        insert_patterns = [
            r'(^extraction_depth:\s*\S+\s*\n)',
            r'(^verification_status:\s*\S+\s*\n)',
            r'(^status:\s*\S+\s*\n)',
        ]
        inserted = False
        for pattern in insert_patterns:
            match = re.search(pattern, text, re.MULTILINE)
            if match:
                insert_pos = match.end()
                text = text[:insert_pos] + f"year: {year}\n" + text[insert_pos:]
                inserted = True
                break
        
        if not inserted:
            ep_match = re.search(r'^evidence_policy:', text, re.MULTILINE)
            if ep_match:
                text = text[:ep_match.start()] + f"year: {year}\n" + text[ep_match.start():]
                inserted = True
        
        if inserted:
            card_path.write_text(text, encoding="utf-8")
    
    return {
        "card": card_path.name,
        "year": year,
        "source": source,
        "doi": doi[:50] if doi else "",
        "title": title[:60] if title else "",
    }


def main():
    dry_run = "--apply" not in sys.argv
    disease_filter = None
    for arg in sys.argv[1:]:
        if arg.startswith("--disease="):
            disease_filter = arg.split("=", 1)[1].lower()
    
    if dry_run:
        print("[DRY RUN] Use --apply to write changes. Showing what would be updated:")
        print()
    
    cards = sorted(RAW_PAPERS.glob("src-*.md"))
    if disease_filter:
        cards = [c for c in cards if f"src-{disease_filter}-" in c.name]
    
    total = 0
    updated = 0
    skipped_has_year = 0
    no_year_found = 0
    results_by_disease: dict[str, list] = {}
    
    for card_path in cards:
        total += 1
        result = process_card(card_path, dry_run=dry_run)
        if result is None:
            text = card_path.read_text(encoding="utf-8")
            if re.search(r'^year:\s*\d', text, re.MULTILINE):
                skipped_has_year += 1
            else:
                no_year_found += 1
        else:
            updated += 1
            disease = re.match(r'src-([a-z]+)-', card_path.name)
            disease_name = disease.group(1) if disease else "unknown"
            results_by_disease.setdefault(disease_name, []).append(result)
    
    print(f"Scanned: {total} cards")
    print(f"Already have year: {skipped_has_year}")
    print(f"Year extractable: {updated}")
    print(f"No year found: {no_year_found}")
    print()
    
    for disease, results in sorted(results_by_disease.items()):
        print(f"  {disease.upper()}: {len(results)} cards {'updated' if not dry_run else 'would be updated'}")
        for r in results[:5]:
            print(f"    {r['card']}: year={r['year']} (from {r['source']})")
        if len(results) > 5:
            print(f"    ... and {len(results) - 5} more")
    
    if dry_run and updated > 0:
        print()
        print("Run with --apply to write these changes.")


if __name__ == "__main__":
    main()
