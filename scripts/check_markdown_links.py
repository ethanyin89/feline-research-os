#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
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


def should_skip(target: str) -> bool:
    return (
        target.startswith("http://")
        or target.startswith("https://")
        or target.startswith("mailto:")
        or target.startswith("#")
    )


def normalize_target(raw: str) -> str:
    return raw.strip().split("#", 1)[0].strip()


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), start=1):
        for raw_target in LINK_RE.findall(line):
            target = normalize_target(raw_target)
            if not target or should_skip(target):
                continue
            if target.startswith("/Users/"):
                errors.append(f"{path}:{lineno}: absolute local path link: {target}")
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{path}:{lineno}: missing target: {target}")
    return errors


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    files = sorted(
        file for file in root.rglob("*.md")
        if not should_skip_file(file, root)
    )
    errors: list[str] = []
    for file in files:
        errors.extend(check_file(file))
    if errors:
        print("\n".join(errors))
        print(f"\nFAIL: {len(errors)} markdown link issue(s) found.")
        return 1
    print(f"PASS: checked {len(files)} markdown files, no local link issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
