#!/usr/bin/env python3
"""Compare numerical tokens between source and translated files.

This is a screening tool, not a proof of accuracy. It flags numbers that appear only in one file
or occur a different number of times. Review all flagged items manually.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys

NUMBER_RE = re.compile(
    r"(?<![A-Za-z])(?:[<>≤≥≈~]?\s*)?[-−]?\d{1,3}(?:,\d{3})*(?:\.\d+)?(?:\s*%|\s*[eE][+-]?\d+)?"
)


def normalize(token: str) -> str:
    token = token.replace("−", "-").replace(",", "")
    token = re.sub(r"\s+", "", token)
    return token


def extract(path: Path) -> Counter[str]:
    text = path.read_text(encoding="utf-8")
    return Counter(normalize(m.group(0)) for m in NUMBER_RE.finditer(text))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("target")
    args = parser.parse_args()

    source = Path(args.source)
    target = Path(args.target)
    for p in (source, target):
        if not p.is_file():
            print(f"ERROR: file not found: {p}", file=sys.stderr)
            return 2

    a = extract(source)
    b = extract(target)
    keys = sorted(set(a) | set(b))
    diffs = [(k, a[k], b[k]) for k in keys if a[k] != b[k]]

    if diffs:
        print("Numerical-token differences found (manual review required):")
        for token, source_count, target_count in diffs:
            print(f"- {token}: source={source_count}, target={target_count}")
        return 1

    print("Numerical token counts match.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
