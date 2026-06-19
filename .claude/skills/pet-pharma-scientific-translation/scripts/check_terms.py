#!/usr/bin/env python3
"""Flag prohibited or non-preferred Chinese terminology in a translated file."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys


def split_variants(value: str) -> list[str]:
    if not value:
        return []
    normalized = value.replace("；", ";").replace("，", ",")
    parts: list[str] = []
    for block in normalized.split(";"):
        parts.extend(block.split(","))
    return [p.strip() for p in parts if p.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Translated UTF-8 text/Markdown file")
    parser.add_argument("--glossary", required=True, help="Glossary CSV path")
    args = parser.parse_args()

    target_path = Path(args.target)
    glossary_path = Path(args.glossary)

    if not target_path.is_file():
        print(f"ERROR: target not found: {target_path}", file=sys.stderr)
        return 2
    if not glossary_path.is_file():
        print(f"ERROR: glossary not found: {glossary_path}", file=sys.stderr)
        return 2

    text = target_path.read_text(encoding="utf-8")
    issues: list[str] = []

    with glossary_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        required = {"source_term", "preferred_zh", "avoid_zh"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            print(f"ERROR: glossary missing columns: {sorted(missing)}", file=sys.stderr)
            return 2

        for row in reader:
            source = (row.get("source_term") or "").strip()
            preferred = (row.get("preferred_zh") or "").strip()
            for bad in split_variants(row.get("avoid_zh") or ""):
                count = text.count(bad)
                if count:
                    issues.append(
                        f"TERM: '{bad}' appears {count} time(s); concept='{source}', "
                        f"preferred='{preferred}'"
                    )

    if issues:
        print("Terminology issues found:")
        for item in issues:
            print(f"- {item}")
        return 1

    print("No prohibited terminology found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
