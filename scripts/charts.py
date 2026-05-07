#!/usr/bin/env python3
"""
scripts/charts.py — Matplotlib chart generation for the feline research OS.

Generates visual outputs from vault data:
  - Endpoint comparison radar chart
  - Source card coverage heatmap
  - Disease module maturity bar chart

Usage (CLI):
    python scripts/charts.py endpoint-radar --disease ckd --output outputs/figures/
    python scripts/charts.py source-coverage --disease ckd
    python scripts/charts.py maturity-bar

Usage (imported):
    from charts import endpoint_radar, source_coverage_heatmap
    fig = endpoint_radar("ckd", vault_root)
    fig.savefig("endpoint-radar-ckd.png")
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional

VAULT_ROOT = Path(__file__).parent.parent

try:
    import matplotlib
    matplotlib.use("Agg")  # non-interactive backend
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import numpy as np
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False


def _check_matplotlib():
    if not MATPLOTLIB_AVAILABLE:
        print("matplotlib not installed. Run: pip install matplotlib", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Data extraction from vault
# ---------------------------------------------------------------------------

def _extract_frontmatter(path: Path) -> dict:
    """Minimal YAML-free frontmatter parser."""
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}
    if not content.startswith("---"):
        return {}
    end = content.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in content[3:end].splitlines():
        if ":" in line and not line.startswith(" ") and not line.startswith("\t"):
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip().strip("\"'")
    return fm


def _count_source_references(vault_root: Path, disease: str) -> dict[str, int]:
    """Count how many times each source card is referenced across topics/."""
    topics_dir = vault_root / "topics" / disease
    if not topics_dir.exists():
        return {}
    counts: dict[str, int] = {}
    pattern = re.compile(r"src-" + re.escape(disease) + r"-\d{3}")
    for md in topics_dir.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for match in pattern.findall(text):
            counts[match] = counts.get(match, 0) + 1
    return dict(sorted(counts.items()))


def _extract_endpoints(vault_root: Path, disease: str) -> dict[str, dict]:
    """
    Extract endpoint data from the endpoint handbook.
    Returns {endpoint_name: {"strength": str, "source_count": int}}.
    """
    handbook = vault_root / "topics" / disease / "endpoint-handbook.md"
    if not handbook.exists():
        return {}
    try:
        content = handbook.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    endpoints = {}
    # Parse table rows like: | creatinine | staging ... | core | strong | ... | src-ckd-001, src-ckd-004 |
    for line in content.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 6:
            continue
        name = cells[1].lower().strip()
        if name in ("", "endpoint", "---", "marker"):
            continue
        # Look for strength indicators
        strength_map = {"strong": 3, "moderate": 2, "emerging": 1, "weak": 1}
        strength_val = 1
        for cell in cells[2:]:
            lower = cell.lower()
            for key, val in strength_map.items():
                if key in lower:
                    strength_val = max(strength_val, val)
        # Count source references in the row
        src_pattern = re.compile(r"src-\w+-\d{3}")
        sources = src_pattern.findall(line)
        endpoints[name] = {
            "strength": strength_val,
            "source_count": len(set(sources)),
        }
    return endpoints


def _get_disease_modules(vault_root: Path) -> dict[str, dict]:
    """
    Extract maturity data for each disease module.
    Returns {disease: {"source_cards": int, "topic_pages": int, "images": int}}.
    """
    diseases = ["ckd", "fip", "hcm", "ibd"]
    result = {}
    for d in diseases:
        # Count source cards
        papers_dir = vault_root / "raw" / "papers"
        src_count = len(list(papers_dir.glob(f"src-{d}-*.md"))) if papers_dir.exists() else 0
        # Count topic pages
        topics_dir = vault_root / "topics" / d
        topic_count = len(list(topics_dir.rglob("*.md"))) if topics_dir.exists() else 0
        # Count images
        images_dir = vault_root / "raw" / "images" / d
        img_count = 0
        if images_dir.exists():
            for ext in ("*.png", "*.jpg", "*.jpeg", "*.gif"):
                img_count += len(list(images_dir.glob(ext)))
        result[d] = {
            "source_cards": src_count,
            "topic_pages": topic_count,
            "images": img_count,
        }
    return result


# ---------------------------------------------------------------------------
# Chart generators
# ---------------------------------------------------------------------------

def endpoint_radar(disease: str, vault_root: Path = VAULT_ROOT) -> "plt.Figure":
    """Generate a radar chart of endpoint strength and coverage."""
    _check_matplotlib()
    endpoints = _extract_endpoints(vault_root, disease)
    if not endpoints:
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.text(0.5, 0.5, f"No endpoint data found for {disease.upper()}",
                ha="center", va="center", fontsize=14)
        return fig

    # Take top 8 endpoints by combined score
    scored = sorted(endpoints.items(),
                    key=lambda x: (x[1]["strength"] + x[1]["source_count"]), reverse=True)[:8]
    labels = [name.replace("/", "/\n") for name, _ in scored]
    strength = [d["strength"] for _, d in scored]
    coverage = [min(d["source_count"], 5) for _, d in scored]  # cap at 5 for visual

    N = len(labels)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]
    strength += strength[:1]
    coverage += coverage[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=7, color="gray")

    ax.plot(angles, strength, "o-", linewidth=2, color="#16a34a", label="Evidence strength")
    ax.fill(angles, strength, alpha=0.15, color="#16a34a")
    ax.plot(angles, coverage, "s-", linewidth=2, color="#2563eb", label="Source coverage")
    ax.fill(angles, coverage, alpha=0.1, color="#2563eb")

    ax.set_title(f"{disease.upper()} Endpoint Landscape", fontsize=14, fontweight="bold", pad=20)
    ax.legend(loc="lower right", bbox_to_anchor=(1.15, -0.05), fontsize=9)

    fig.tight_layout()
    return fig


def source_coverage_heatmap(disease: str, vault_root: Path = VAULT_ROOT) -> "plt.Figure":
    """Generate a bar chart of source card citation frequency across topic pages."""
    _check_matplotlib()
    counts = _count_source_references(vault_root, disease)
    if not counts:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.text(0.5, 0.5, f"No source references found for {disease.upper()}",
                ha="center", va="center", fontsize=14)
        return fig

    labels = list(counts.keys())
    values = list(counts.values())

    fig, ax = plt.subplots(figsize=(max(10, len(labels) * 0.6), 5))
    colors = ["#16a34a" if v >= 10 else "#ca8a04" if v >= 5 else "#6b7280" for v in values]
    bars = ax.bar(range(len(labels)), values, color=colors, edgecolor="white", linewidth=0.5)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Citations in topic pages", fontsize=10)
    ax.set_title(f"{disease.upper()} Source Card Citation Frequency", fontsize=13, fontweight="bold")

    # Legend
    patches = [
        mpatches.Patch(color="#16a34a", label="≥10 citations (high)"),
        mpatches.Patch(color="#ca8a04", label="5-9 citations (medium)"),
        mpatches.Patch(color="#6b7280", label="<5 citations (low)"),
    ]
    ax.legend(handles=patches, fontsize=8, loc="upper right")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    return fig


def maturity_bar(vault_root: Path = VAULT_ROOT) -> "plt.Figure":
    """Generate a grouped bar chart comparing disease module maturity."""
    _check_matplotlib()
    modules = _get_disease_modules(vault_root)

    diseases = list(modules.keys())
    src_counts = [modules[d]["source_cards"] for d in diseases]
    topic_counts = [modules[d]["topic_pages"] for d in diseases]
    img_counts = [modules[d]["images"] for d in diseases]

    x = np.arange(len(diseases))
    width = 0.25

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width, src_counts, width, label="Source cards", color="#2563eb")
    ax.bar(x, topic_counts, width, label="Topic pages", color="#16a34a")
    ax.bar(x + width, img_counts, width, label="Images", color="#ca8a04")

    ax.set_xticks(x)
    ax.set_xticklabels([d.upper() for d in diseases], fontsize=12)
    ax.set_ylabel("Count", fontsize=11)
    ax.set_title("Disease Module Maturity Comparison", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Add value labels on bars
    for bars_group in [ax.containers[0], ax.containers[1], ax.containers[2]]:
        for bar in bars_group:
            height = bar.get_height()
            if height > 0:
                ax.text(bar.get_x() + bar.get_width() / 2., height + 0.3,
                        str(int(height)), ha="center", va="bottom", fontsize=9)

    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate charts from vault data.")
    parser.add_argument("chart", choices=["endpoint-radar", "source-coverage", "maturity-bar"],
                        help="Chart type to generate")
    parser.add_argument("--disease", default="ckd",
                        help="Disease module (default: ckd)")
    parser.add_argument("--output", default=None,
                        help="Output directory (default: outputs/figures/)")
    parser.add_argument("--show", action="store_true",
                        help="Display chart interactively (requires GUI)")
    args = parser.parse_args()

    _check_matplotlib()

    out_dir = Path(args.output) if args.output else VAULT_ROOT / "outputs" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.chart == "endpoint-radar":
        fig = endpoint_radar(args.disease)
        out_path = out_dir / f"endpoint-radar-{args.disease}.png"
    elif args.chart == "source-coverage":
        fig = source_coverage_heatmap(args.disease)
        out_path = out_dir / f"source-coverage-{args.disease}.png"
    elif args.chart == "maturity-bar":
        fig = maturity_bar()
        out_path = out_dir / "maturity-bar.png"

    fig.savefig(out_path, dpi=150, bbox_inches="tight", facecolor="white")
    print(f"[saved] {out_path.relative_to(VAULT_ROOT)}")

    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
