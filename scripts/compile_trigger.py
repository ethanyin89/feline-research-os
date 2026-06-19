#!/usr/bin/env python3
"""
scripts/compile_trigger.py — Auto-compile trigger for the feline research OS vault.

Detects which source cards have changed and finds all downstream files
(topic pages, system indexes, entities) that reference those source IDs.
Outputs a recompile queue so the operator or an LLM agent knows what to update.

Usage:
    # Show what needs recompiling based on git changes since last commit
    python scripts/compile_trigger.py

    # Check specific source cards
    python scripts/compile_trigger.py --sources src-ckd-001 src-ckd-004

    # Check all source cards modified in the last N days
    python scripts/compile_trigger.py --since 2

    # Output as JSON (for LLM consumption)
    python scripts/compile_trigger.py --json

Fills the "auto-compile trigger" gap from the Karpathy LLM wiki architecture:
when source cards change, downstream compiled pages should be flagged for recompilation.
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

VAULT_ROOT = Path(__file__).parent.parent


def get_changed_source_cards_git(vault_root: Path) -> list[str]:
    """
    Find source cards changed in git (staged + unstaged + untracked in raw/).
    Returns list of source IDs.
    """
    source_ids = []
    try:
        # Staged and unstaged changes
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD", "--", "raw/"],
            capture_output=True, text=True, cwd=vault_root,
        )
        changed_files = result.stdout.strip().splitlines() if result.stdout.strip() else []

        # Also check unstaged
        result2 = subprocess.run(
            ["git", "diff", "--name-only", "--", "raw/"],
            capture_output=True, text=True, cwd=vault_root,
        )
        changed_files += result2.stdout.strip().splitlines() if result2.stdout.strip() else []

        # Untracked in raw/
        result3 = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard", "raw/"],
            capture_output=True, text=True, cwd=vault_root,
        )
        changed_files += result3.stdout.strip().splitlines() if result3.stdout.strip() else []

        for f in set(changed_files):
            if f.endswith(".md") and "/papers/" in f:
                sid = _extract_source_id(vault_root / f)
                if sid:
                    source_ids.append(sid)
    except FileNotFoundError:
        pass  # git not available
    return sorted(set(source_ids))


def get_changed_source_cards_since(vault_root: Path, days: int) -> list[str]:
    """Find source cards modified in the last N days by file mtime."""
    source_ids = []
    cutoff = datetime.now() - timedelta(days=days)
    papers_dir = vault_root / "raw" / "papers"
    if not papers_dir.exists():
        return []
    for md_file in papers_dir.rglob("*.md"):
        mtime = datetime.fromtimestamp(md_file.stat().st_mtime)
        if mtime >= cutoff:
            sid = _extract_source_id(md_file)
            if sid:
                source_ids.append(sid)
    return sorted(set(source_ids))


def _extract_source_id(path: Path) -> Optional[str]:
    """Pull the id: field from YAML frontmatter."""
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    for line in content[3:end].splitlines():
        if line.startswith("id:"):
            return line.split(":", 1)[1].strip().strip("\"'")
    return None


def find_downstream_files(source_ids: list[str], vault_root: Path) -> dict[str, list[str]]:
    """
    For each source_id, find all .md files outside raw/ that reference it.
    Returns {source_id: [list of vault-relative paths]}.
    """
    downstream: dict[str, list[str]] = {sid: [] for sid in source_ids}

    # Build regex that matches any of the source IDs
    if not source_ids:
        return downstream
    pattern = re.compile("|".join(re.escape(sid) for sid in source_ids))

    # Scan topics/, entities/, system/, outputs/
    scan_dirs = ["topics", "entities", "system", "outputs"]
    for dir_name in scan_dirs:
        scan_dir = vault_root / dir_name
        if not scan_dir.exists():
            continue
        for md_file in scan_dir.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            rel_path = str(md_file.relative_to(vault_root))
            for sid in source_ids:
                if sid in content:
                    downstream[sid].append(rel_path)

    return downstream


def build_recompile_queue(downstream: dict[str, list[str]]) -> list[dict]:
    """
    Flatten the downstream map into a deduplicated recompile queue,
    sorted by number of changed sources affecting each file (most affected first).
    """
    file_sources: dict[str, list[str]] = {}
    for sid, files in downstream.items():
        for f in files:
            file_sources.setdefault(f, []).append(sid)

    queue = [
        {
            "file": f,
            "affected_by": sorted(sids),
            "source_count": len(sids),
        }
        for f, sids in file_sources.items()
    ]
    queue.sort(key=lambda x: (-x["source_count"], x["file"]))
    return queue


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find downstream files that need recompilation after source card changes.",
    )
    parser.add_argument(
        "--sources", nargs="+",
        help="Specific source IDs to check (e.g. src-ckd-001 src-ckd-004)",
    )
    parser.add_argument(
        "--since", type=int,
        help="Check source cards modified in the last N days",
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output as JSON for LLM consumption",
    )
    args = parser.parse_args()

    # Determine which source cards changed
    if args.sources:
        changed = args.sources
    elif args.since:
        changed = get_changed_source_cards_since(VAULT_ROOT, args.since)
    else:
        changed = get_changed_source_cards_git(VAULT_ROOT)

    if not changed:
        if args.json:
            print(json.dumps({"changed_sources": [], "recompile_queue": []}))
        else:
            print("No changed source cards detected.")
        sys.exit(0)

    # Find downstream
    downstream = find_downstream_files(changed, VAULT_ROOT)
    queue = build_recompile_queue(downstream)

    if args.json:
        print(json.dumps({
            "changed_sources": changed,
            "recompile_queue": queue,
            "total_files": len(queue),
        }, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"  Changed source cards: {len(changed)}")
        print(f"  Downstream files to recompile: {len(queue)}")
        print(f"{'='*60}\n")

        print("  Changed sources:")
        for sid in changed:
            n = len(downstream.get(sid, []))
            print(f"    {sid} → {n} downstream file{'s' if n != 1 else ''}")
        print()

        if queue:
            print("  Recompile queue (most affected first):")
            for i, item in enumerate(queue, 1):
                sources_str = ", ".join(item["affected_by"])
                print(f"    {i}. {item['file']}")
                print(f"       affected by: {sources_str}")
            print()

        # Also print topic pages specifically (the high-value targets)
        topic_files = [q for q in queue if q["file"].startswith("topics/")]
        if topic_files:
            print("  Priority topic pages:")
            for t in topic_files:
                print(f"    → {t['file']} ({t['source_count']} sources)")
            print()


if __name__ == "__main__":
    main()
