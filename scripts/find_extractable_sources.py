#!/usr/bin/env python3
"""
Find open-access sources that need deep extraction.

Usage:
    python3 scripts/find_extractable_sources.py [--branch-controlling]

Outputs sources sorted by priority (topic page citations first).
"""

import re
import sys
from pathlib import Path

OPEN_ACCESS_PATTERNS = [
    r'10\.3390/',      # MDPI
    r'10\.1371/',      # PLOS
    r'10\.1186/',      # BMC
    r'10\.1155/',      # Hindawi
    r'10\.3389/',      # Frontiers
]

def is_open_access(content: str) -> bool:
    """Check if source has open-access DOI or PMCID."""
    # Check for PMCID
    if re.search(r'^pmcid:\s*"?PMC\d+', content, re.M):
        return True
    # Check for open-access DOI patterns
    doi_match = re.search(r'^doi:\s*"?([^"\s]+)', content, re.M)
    if doi_match:
        doi = doi_match.group(1)
        for pattern in OPEN_ACCESS_PATTERNS:
            if re.search(pattern, doi):
                return True
    return False

def needs_extraction(content: str) -> bool:
    """Check if source needs deep extraction."""
    return bool(re.search(
        r'verification_status:\s*(abstract_weighted|title_only)',
        content
    ))

def get_source_id(content: str) -> str:
    """Extract source ID from frontmatter."""
    match = re.search(r'^id:\s*(\S+)', content, re.M)
    return match.group(1) if match else ''

def get_doi(content: str) -> str:
    """Extract DOI from frontmatter."""
    match = re.search(r'^doi:\s*"?([^"\s]+)', content, re.M)
    return match.group(1) if match else ''

def count_topic_citations(source_id: str, topics_dir: Path) -> int:
    """Count how many times source is cited in topic pages."""
    count = 0
    for f in topics_dir.rglob('*.md'):
        try:
            if source_id in f.read_text(encoding='utf-8'):
                count += 1
        except Exception:
            pass
    return count

def main():
    branch_controlling_only = '--branch-controlling' in sys.argv

    raw_papers = Path('raw/papers')
    topics_dir = Path('topics')

    if not raw_papers.exists():
        print("Error: raw/papers directory not found", file=sys.stderr)
        sys.exit(1)

    extractable = []

    for f in raw_papers.glob('src-*.md'):
        try:
            content = f.read_text(encoding='utf-8')
        except Exception:
            continue

        if needs_extraction(content) and is_open_access(content):
            source_id = get_source_id(content)
            doi = get_doi(content)
            citations = count_topic_citations(source_id, topics_dir)

            if branch_controlling_only and citations == 0:
                continue

            extractable.append({
                'id': source_id,
                'doi': doi,
                'citations': citations,
                'file': str(f)
            })

    # Sort by citations (descending)
    extractable.sort(key=lambda x: -x['citations'])

    # Output
    print(f"Found {len(extractable)} extractable sources")
    print()

    if extractable:
        print(f"{'Source ID':<20} {'Citations':<10} {'DOI'}")
        print('-' * 70)
        for s in extractable:
            print(f"{s['id']:<20} {s['citations']:<10} {s['doi']}")

if __name__ == '__main__':
    main()
