"""Compute source-card inventory from the current vault contents."""

from __future__ import annotations

import re
from pathlib import Path


KNOWN_STATUSES = (
    "audited",
    "deep_extracted",
    "source_checked",
    "abstract_weighted",
    "title_only",
)


def _frontmatter_scalar(content: str, key: str) -> str:
    if not content.startswith("---"):
        return ""
    end = content.find("\n---", 3)
    if end == -1:
        return ""
    match = re.search(
        rf"^{re.escape(key)}:\s*[\"']?([^\"'\n]+)[\"']?\s*$",
        content[3:end],
        re.MULTILINE,
    )
    return match.group(1).strip() if match else ""


def get_source_inventory(vault_root: Path, disease: str) -> dict:
    """Return current source-card counts without inferring readiness."""
    disease = disease.lower().strip()
    papers_dir = vault_root / "raw" / "papers"
    counts = {status: 0 for status in KNOWN_STATUSES}
    counts["other"] = 0

    paths = sorted(papers_dir.glob(f"src-{disease}-*.md")) if papers_dir.exists() else []
    for path in paths:
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            counts["other"] += 1
            continue
        status = _frontmatter_scalar(content, "verification_status").lower()
        if status in counts:
            counts[status] += 1
        else:
            counts["other"] += 1

    return {
        "disease": disease,
        "total": len(paths),
        "verification_status": counts,
    }


def format_source_inventory(inventory: dict, chinese: bool = False) -> str:
    """Format factual inventory counts without a maturity judgment."""
    counts = inventory["verification_status"]
    details = [
        ("deep", counts["deep_extracted"]),
        ("source-checked", counts["source_checked"]),
        ("abstract", counts["abstract_weighted"]),
        ("title-only", counts["title_only"]),
    ]
    detail_text = ", ".join(f"{label} {count}" for label, count in details if count)
    if not detail_text:
        detail_text = "no classified extraction status"

    if chinese:
        return f"来源清单：{inventory['total']} 篇 source cards（{detail_text}）；这不是成熟度或决策评级"
    return (
        f"Source inventory: {inventory['total']} cards ({detail_text}); "
        "this is not a maturity or decision rating"
    )
