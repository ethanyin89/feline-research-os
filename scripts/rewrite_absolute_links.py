#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from os import path as os_path
from pathlib import Path


VAULT_ROOT = Path("/Users/jiawei/Desktop/insclaude/feline-research-os").resolve()
LINK_RE = re.compile(r"(\[[^\]]+\]\()(/Users/jiawei/Desktop/insclaude/feline-research-os/[^)#]+)(#[^)]+)?(\))")
SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    "inbox/rejected",
}


def should_skip_file(path: Path, root: Path) -> bool:
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False
    parts = rel.parts
    rel_posix = rel.as_posix()
    return any(part in SKIP_DIRS for part in parts) or any(
        rel_posix == skipped or rel_posix.startswith(f"{skipped}/")
        for skipped in SKIP_DIRS
        if "/" in skipped
    )


def relink(path: Path, text: str) -> tuple[str, int]:
    replacements = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal replacements
        prefix, absolute_target, anchor, suffix = match.groups()
        target_path = Path(absolute_target).resolve()
        relative = Path(os_path.relpath(target_path, start=path.parent.resolve())).as_posix()
        replacements += 1
        return f"{prefix}{relative}{anchor or ''}{suffix}"

    return LINK_RE.sub(replace, text), replacements


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else VAULT_ROOT
    changed_files = 0
    total_rewrites = 0

    for file in sorted(root.rglob("*.md")):
        if should_skip_file(file, root):
            continue
        text = file.read_text(encoding="utf-8")
        updated, rewrites = relink(file, text)
        if rewrites:
            file.write_text(updated, encoding="utf-8")
            changed_files += 1
            total_rewrites += rewrites

    print(f"Rewrote {total_rewrites} absolute link(s) across {changed_files} markdown file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
