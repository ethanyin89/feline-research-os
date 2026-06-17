#!/usr/bin/env python3
"""
scripts/test_research_mode.py — Health check for research mode feature.

Usage:
    python scripts/test_research_mode.py
    python scripts/test_research_mode.py --verbose
"""

import sys
from pathlib import Path

# Add scripts dir to path
sys.path.insert(0, str(Path(__file__).parent))

from research_mode import (
    is_research_mode_query,
    handle_research_query,
    _is_placeholder_content,
    EXTERNAL_SEARCH_AVAILABLE,
)


def test_query_detection():
    """Test research-mode query detection."""
    # Should be detected as research mode
    positive_cases = [
        "search latest papers about HCM",
        "find CKD studies",
        "搜索HCM最新文献",
        "查找FIP相关研究",
        "literature review on diabetes",
        "最新CKD研究",
    ]

    # Should NOT be detected as research mode
    negative_cases = [
        "what is HCM",
        "explain CKD",
        "FIP怎么识别",
        "HCM是什么",
        "how to treat diabetes",
    ]

    errors = []
    for query in positive_cases:
        if not is_research_mode_query(query):
            errors.append(f"False negative: '{query}'")

    for query in negative_cases:
        if is_research_mode_query(query):
            errors.append(f"False positive: '{query}'")

    return errors


def test_placeholder_filtering():
    """Test placeholder content detection."""
    # Should be detected as placeholder
    placeholders = [
        "Candidate ckd source from sheet row 106.",
        "This card is a first-pass intake object only.",
        "Use it for triage until abstract extraction.",
    ]

    # Should NOT be detected as placeholder
    legitimate = [
        "FGF-23 may serve as a prognostic biomarker.",
        "This is a high-value bridge source.",
        "Strong candidate for deep extraction.",
    ]

    errors = []
    for text in placeholders:
        if not _is_placeholder_content(text):
            errors.append(f"Missed placeholder: '{text[:50]}...'")

    for text in legitimate:
        if _is_placeholder_content(text):
            errors.append(f"False placeholder: '{text[:50]}...'")

    return errors


def test_output_quality():
    """Test output has no internal IDs or file paths."""
    import re

    output, sources = handle_research_query(
        "search HCM papers",
        chinese=False,
        include_external=False,  # Skip external to speed up test
    )

    errors = []

    # Check for internal IDs
    if re.search(r'src-\w+-\d+', output):
        errors.append("Output contains internal IDs (src-xxx)")

    # Check for file paths
    if 'raw/papers' in output:
        errors.append("Output contains file paths")

    # Check for placeholder content
    bad_patterns = ['sheet row', 'first-pass intake', 'Use it for triage until']
    for pattern in bad_patterns:
        if pattern.lower() in output.lower():
            errors.append(f"Output contains placeholder: '{pattern}'")

    # Check output has expected sections
    expected_sections = [
        "Best recent papers",
        "What these papers collectively say",
        "must-read",
    ]
    for section in expected_sections:
        if section.lower() not in output.lower():
            errors.append(f"Missing section: '{section}'")

    return errors


def test_external_search():
    """Test PubMed augmentation (if available)."""
    if not EXTERNAL_SEARCH_AVAILABLE:
        return ["External search module not available"]

    output, sources = handle_research_query(
        "search FIP papers",
        chinese=False,
        include_external=True,
    )

    errors = []

    # Check PubMed section exists
    if "PubMed" not in output:
        errors.append("PubMed section missing from output")

    # Check for DOI URLs
    if "https://doi.org/" not in output:
        errors.append("No DOI URLs in output")

    return errors


def main():
    verbose = "--verbose" in sys.argv

    print("=== Research Mode Health Check ===\n")

    tests = [
        ("Query detection", test_query_detection),
        ("Placeholder filtering", test_placeholder_filtering),
        ("Output quality", test_output_quality),
        ("External search", test_external_search),
    ]

    all_passed = True

    for name, test_fn in tests:
        try:
            errors = test_fn()
            if errors:
                print(f"❌ {name}: {len(errors)} errors")
                if verbose:
                    for err in errors:
                        print(f"   - {err}")
                all_passed = False
            else:
                print(f"✓ {name}")
        except Exception as e:
            print(f"❌ {name}: Exception - {e}")
            all_passed = False

    print()
    if all_passed:
        print("✓ All tests passed")
        return 0
    else:
        print("❌ Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
