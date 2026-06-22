#!/usr/bin/env python3
"""
scripts/deep_extraction.py — Deep extraction document parsing and rendering.

Deep extraction documents live in raw/deep-extractions/ext-{source-id}.md
and contain Phase 0-3 analysis of high-value papers.

This module handles:
1. Parsing deep extraction files
2. Extracting Phase 2/3 content for display
3. Rendering the secondary detail page
"""

from __future__ import annotations

import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
import yaml

VAULT_ROOT = Path(__file__).parent.parent
DEEP_EXTRACTIONS_DIR = VAULT_ROOT / "raw" / "deep-extractions"


@dataclass
class DeepExtraction:
    """Parsed deep extraction document."""
    source_id: str
    title: str
    title_zh: Optional[str] = None
    authors: list[str] = field(default_factory=list)
    journal: Optional[str] = None
    year: Optional[int] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    research_type: Optional[str] = None
    extraction_date: Optional[str] = None
    extractor: Optional[str] = None  # "human" or "llm"
    evidence_nodes: list[str] = field(default_factory=list)

    # Phase content
    phase2_content: str = ""  # 论点-论据提炼
    phase3_content: str = ""  # 自检发现
    one_line_summary: str = ""  # 一句话总结

    # Raw content for debugging
    raw_content: str = ""
    file_path: Optional[str] = None


def get_deep_extraction_path(source_id: str) -> Path:
    """Get the path to a deep extraction file for a source."""
    return DEEP_EXTRACTIONS_DIR / f"ext-{source_id}.md"


def has_deep_extraction(source_id: str) -> bool:
    """Check if a deep extraction exists for a source."""
    return get_deep_extraction_path(source_id).exists()


def list_deep_extractions() -> list[str]:
    """List all source IDs that have deep extractions."""
    if not DEEP_EXTRACTIONS_DIR.exists():
        return []

    source_ids = []
    for f in DEEP_EXTRACTIONS_DIR.glob("ext-*.md"):
        # Extract source_id from filename: ext-src-hcm-001.md -> src-hcm-001
        match = re.match(r"ext-(src-[a-z]+-\d+)\.md", f.name)
        if match:
            source_ids.append(match.group(1))
    return sorted(source_ids)


def parse_deep_extraction(source_id: str) -> Optional[DeepExtraction]:
    """
    Parse a deep extraction file and return structured content.

    Returns None if the file doesn't exist.
    """
    path = get_deep_extraction_path(source_id)
    if not path.exists():
        return None

    content = path.read_text(encoding="utf-8")
    return _parse_deep_extraction_content(content, source_id, str(path))


def _parse_deep_extraction_content(
    content: str,
    source_id: str,
    file_path: str
) -> DeepExtraction:
    """Parse the content of a deep extraction file."""

    extraction = DeepExtraction(
        source_id=source_id,
        title="",
        raw_content=content,
        file_path=file_path,
    )

    # Parse YAML frontmatter if present
    frontmatter_match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if frontmatter_match:
        try:
            fm = yaml.safe_load(frontmatter_match.group(1))
            if fm:
                extraction.title = fm.get("title", "")
                extraction.title_zh = fm.get("title_zh")
                extraction.authors = fm.get("authors", [])
                extraction.journal = fm.get("journal")
                extraction.year = fm.get("year")
                extraction.doi = fm.get("doi")
                extraction.url = fm.get("url")
                extraction.extraction_date = fm.get("extraction_date")
                extraction.extractor = fm.get("extractor")
                extraction.evidence_nodes = fm.get("evidence_nodes", [])
        except yaml.YAMLError:
            pass

    # Extract Phase 2 content
    phase2_match = re.search(
        r"#\s*Phase\s*2[：:]\s*论点-?论据提炼\s*\n(.*?)(?=\n#\s*Phase\s*3|$)",
        content,
        re.DOTALL | re.IGNORECASE
    )
    if phase2_match:
        extraction.phase2_content = phase2_match.group(1).strip()

    # Extract Phase 3 content
    phase3_match = re.search(
        r"#\s*Phase\s*3[：:]\s*自检发现\s*\n(.*?)(?=\n#\s*一句话总结|$)",
        content,
        re.DOTALL | re.IGNORECASE
    )
    if phase3_match:
        extraction.phase3_content = phase3_match.group(1).strip()

    # Extract one-line summary
    summary_match = re.search(
        r"#\s*一句话总结\s*\n(.*?)(?=\n#|$)",
        content,
        re.DOTALL
    )
    if summary_match:
        extraction.one_line_summary = summary_match.group(1).strip()

    # If no title from frontmatter, try to extract from content
    if not extraction.title:
        title_match = re.search(
            r"\*\*论文题目[：:]\*\*\s*(.+?)(?:\n|$)",
            content
        )
        if title_match:
            extraction.title = title_match.group(1).strip()

    # Extract title_zh if not in frontmatter
    if not extraction.title_zh:
        title_zh_match = re.search(
            r"\*\*中文译名[：:]\*\*\s*(.+?)(?:\n|$)",
            content
        )
        if title_zh_match:
            extraction.title_zh = title_zh_match.group(1).strip()

    # Extract research type if not in frontmatter
    if not extraction.research_type:
        research_type_match = re.search(
            r"\*\*研究类型[：:]\*\*\s*(.+?)(?:\n|$)",
            content
        )
        if research_type_match:
            extraction.research_type = research_type_match.group(1).strip()

    return extraction


def render_detail_page_markdown(extraction: DeepExtraction) -> str:
    """
    Render a deep extraction as markdown for the detail page.

    This shows:
    - Paper metadata
    - Phase 2: 论点-论据提炼
    - Phase 3: 自检发现
    - Link to original paper
    """
    lines = []

    # Inject custom styles for the detail page
    lines.append("""
<style>
.deep-ext-container {
    font-family: 'Inter', sans-serif !important;
}
.deep-ext-header {
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border);
}
.deep-ext-title {
    font-family: 'Inter', sans-serif !important;
    font-size: 26px !important;
    font-weight: 600 !important;
    line-height: 1.3 !important;
    letter-spacing: -0.02em !important;
    color: var(--text) !important;
    margin-top: 0 !important;
    margin-bottom: 8px !important;
}
.deep-ext-subtitle {
    font-family: 'Inter', sans-serif !important;
    font-size: 16px !important;
    color: var(--text-secondary) !important;
    line-height: 1.5 !important;
    margin-bottom: 16px !important;
}
.deep-ext-meta-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    background-color: var(--surface-2);
    border: 1px solid var(--border-subtle);
    border-radius: 6px;
    padding: 16px;
    margin-bottom: 32px;
}
.deep-ext-meta-item {
    display: flex;
    flex-direction: column;
}
.deep-ext-meta-label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px !important;
    font-weight: 500 !important;
    color: var(--muted) !important;
    text-transform: uppercase;
    letter-spacing: 0.05em !important;
    margin-bottom: 4px;
}
.deep-ext-meta-value {
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    color: var(--text) !important;
    line-height: 1.4 !important;
}
.deep-ext-meta-value a {
    color: var(--accent-green) !important;
    text-decoration: none !important;
}
.deep-ext-meta-value a:hover {
    text-decoration: underline !important;
}
.deep-ext-section {
    background-color: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 24px;
    margin-bottom: 24px;
}
.deep-ext-section-title {
    font-family: 'Inter', sans-serif !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    letter-spacing: -0.01em !important;
    color: var(--text) !important;
    margin-top: 0 !important;
    margin-bottom: 16px !important;
    border-bottom: 1px solid var(--border-subtle);
    padding-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.deep-ext-section-content {
    font-family: 'Source Serif 4', Georgia, serif !important;
    font-size: 15.5px !important;
    line-height: 1.75 !important;
    color: var(--text) !important;
}
/* Ensure standard markdown lists inside container have serif font too */
.deep-ext-section-content p, 
.deep-ext-section-content li,
.deep-ext-section-content blockquote {
    font-family: 'Source Serif 4', Georgia, serif !important;
    font-size: 15.5px !important;
    color: var(--text) !important;
}
.deep-ext-summary-box {
    background-color: rgba(16, 185, 129, 0.04);
    border-left: 4px solid var(--accent-green);
    border-radius: 4px;
    padding: 16px;
    margin-top: 24px;
    margin-bottom: 24px;
}
.deep-ext-summary-title {
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    color: var(--accent-green) !important;
    margin-top: 0 !important;
    margin-bottom: 6px !important;
}
.deep-ext-summary-text {
    font-family: 'Source Serif 4', Georgia, serif !important;
    font-size: 15px !important;
    color: var(--text) !important;
    line-height: 1.6 !important;
    margin: 0 !important;
}
.evidence-tag {
    display: inline-block;
    background-color: var(--surface-2) !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: 4px;
    padding: 2px 8px;
    font-size: 11px !important;
    font-family: 'JetBrains Mono', monospace !important;
    margin-right: 6px;
    margin-bottom: 6px;
    color: var(--text-secondary) !important;
}
</style>
""")

    # Main structural markup wrapper
    lines.append('<div class="deep-ext-container">')

    # Header with title and translated title
    lines.append('<div class="deep-ext-header">')
    lines.append(f'<h1 class="deep-ext-title">{extraction.title}</h1>')
    if extraction.title_zh and extraction.title_zh != extraction.title:
        lines.append(f'<div class="deep-ext-subtitle">{extraction.title_zh}</div>')
    lines.append('</div>')

    # Bibliographic Metadata Grid
    lines.append('<div class="deep-ext-meta-grid">')
    
    # Authors
    if extraction.authors:
        authors_str = ", ".join(extraction.authors[:3])
        if len(extraction.authors) > 3:
            authors_str += ", et al."
    else:
        authors_str = "N/A"
    lines.append(f'''
    <div class="deep-ext-meta-item">
        <span class="deep-ext-meta-label">Authors / 作者</span>
        <span class="deep-ext-meta-value">{authors_str}</span>
    </div>
    ''')

    # Journal
    lines.append(f'''
    <div class="deep-ext-meta-item">
        <span class="deep-ext-meta-label">Journal / 期刊</span>
        <span class="deep-ext-meta-value">{extraction.journal or "N/A"}</span>
    </div>
    ''')

    # Year
    lines.append(f'''
    <div class="deep-ext-meta-item">
        <span class="deep-ext-meta-label">Year / 年份</span>
        <span class="deep-ext-meta-value">{extraction.year or "N/A"}</span>
    </div>
    ''')

    # Research Type
    lines.append(f'''
    <div class="deep-ext-meta-item">
        <span class="deep-ext-meta-label">Study Type / 研究类型</span>
        <span class="deep-ext-meta-value">{extraction.research_type or "N/A"}</span>
    </div>
    ''')

    # DOI / URL Link
    link = extraction.url or (f"https://doi.org/{extraction.doi}" if extraction.doi else None)
    link_html = f'<a href="{link}" target="_blank">{link}</a>' if link else "N/A"
    lines.append(f'''
    <div class="deep-ext-meta-item" style="grid-column: 1 / -1;">
        <span class="deep-ext-meta-label">Source Link / 原文链接</span>
        <span class="deep-ext-meta-value">{link_html}</span>
    </div>
    ''')
    
    # Evidence Nodes
    if extraction.evidence_nodes:
        tags_html = "".join([f'<span class="evidence-tag">{node}</span>' for node in extraction.evidence_nodes])
        lines.append(f'''
        <div class="deep-ext-meta-item" style="grid-column: 1 / -1;">
            <span class="deep-ext-meta-label">Evidence Nodes / 证据节点</span>
            <span class="deep-ext-meta-value" style="margin-top: 4px;">{tags_html}</span>
        </div>
        ''')
    
    lines.append('</div>')  # End meta-grid

    # Phase 2
    if extraction.phase2_content:
        lines.append('<div class="deep-ext-section">')
        lines.append('<h2 class="deep-ext-section-title">🔍 论点-论据提炼 / Argument-Evidence Extraction</h2>')
        lines.append('<div class="deep-ext-section-content">')
        lines.append("")
        lines.append(extraction.phase2_content)
        lines.append("")
        lines.append('</div>')
        lines.append('</div>')

    # Phase 3
    if extraction.phase3_content:
        lines.append('<div class="deep-ext-section">')
        lines.append('<h2 class="deep-ext-section-title">🛠️ 自检发现 / Methodological Boundaries & Synthesis</h2>')
        lines.append('<div class="deep-ext-section-content">')
        lines.append("")
        lines.append(extraction.phase3_content)
        lines.append("")
        lines.append('</div>')
        lines.append('</div>')

    # One-line summary
    if extraction.one_line_summary:
        lines.append(f'''
        <div class="deep-ext-summary-box">
            <h3 class="deep-ext-summary-title">💡 一句话总结 / Summary</h3>
            <p class="deep-ext-summary-text">{extraction.one_line_summary}</p>
        </div>
        ''')

    lines.append('</div>')  # End deep-ext-container

    return "\n".join(lines)


def get_distilled_why_it_matters(extraction: DeepExtraction) -> Optional[str]:
    """
    Extract a distilled "Why it matters" statement from Phase 2/3.

    Used for the primary recommendation card.
    """
    # Try to get the first argument from Phase 2
    if extraction.phase2_content:
        # Look for the first "论点" pattern
        match = re.search(
            r"\*\*论点\s*\d*[：:]\*\*\s*(.+?)(?:\n|$)",
            extraction.phase2_content
        )
        if match:
            return match.group(1).strip()

    # Fall back to one-line summary
    if extraction.one_line_summary:
        return extraction.one_line_summary[:200]

    return None


def get_distilled_takeaway(extraction: DeepExtraction) -> Optional[str]:
    """
    Extract a distilled "Takeaway" statement from Phase 2/3.

    Used for the primary recommendation card.
    """
    # Try to get from "最重要的发现" in Phase 3
    if extraction.phase3_content:
        match = re.search(
            r"##\s*最重要的发现\s*\n+(.+?)(?:\n##|$)",
            extraction.phase3_content,
            re.DOTALL
        )
        if match:
            finding = match.group(1).strip()
            # Take first sentence or first 200 chars
            first_sentence = re.split(r"[。.!！]", finding)[0]
            if len(first_sentence) < 200:
                return first_sentence
            return finding[:200] + "..."

    # Fall back to one-line summary
    if extraction.one_line_summary:
        return extraction.one_line_summary[:250]

    return None
