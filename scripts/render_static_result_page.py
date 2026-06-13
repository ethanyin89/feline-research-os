#!/usr/bin/env python3
"""Render approved static research pages through the ResultPresentation contract."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from core.static_result_adapter import (  # noqa: E402
    build_overview_presentation,
    build_ranked_presentation,
)
from core.static_result_renderer import render_overview, render_ranked  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--surface", choices=("overview", "ranked"), required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    source = args.source if args.source.is_absolute() else ROOT / args.source
    output = args.out if args.out.is_absolute() else ROOT / args.out
    if args.surface == "overview":
        document = render_overview(build_overview_presentation(source, ROOT))
    else:
        document = render_ranked(build_ranked_presentation(source, ROOT))

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")
    print(f"Wrote {output.relative_to(ROOT) if output.is_relative_to(ROOT) else output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
