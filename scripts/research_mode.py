#!/usr/bin/env python3
"""
scripts/research_mode.py — Research-mode structured output for Ask the Vault.

Inspired by agent.ii.inc's literature search UX. When users ask research-style
questions like "search latest papers about HCM", outputs a structured response
with categorized papers, synthesis, and limitations.

Architecture: Local-first, API-augmented
- Local vault (Karpathy-style processed source cards) is the foundation
- PubMed API provides augmentation for newer/uncovered research
- Results clearly labeled by source (local vs external)
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field

VAULT_ROOT = Path(__file__).parent.parent

# Import external search module for PubMed augmentation
# Try both relative and absolute imports to handle different execution contexts
try:
    from external_search import (
        search_pubmed,
        ExternalSearchConfig,
        ExternalSearchResult,
        ExternalSearchResponse,
    )
    EXTERNAL_SEARCH_AVAILABLE = True
except ImportError:
    try:
        import sys
        sys.path.insert(0, str(VAULT_ROOT / "scripts"))
        from external_search import (
            search_pubmed,
            ExternalSearchConfig,
            ExternalSearchResult,
            ExternalSearchResponse,
        )
        EXTERNAL_SEARCH_AVAILABLE = True
    except ImportError:
        EXTERNAL_SEARCH_AVAILABLE = False


@dataclass
class SourceCard:
    """Structured representation of a source card from raw/papers/."""
    id: str  # Internal only - never show in user-facing output
    title: str
    year: Optional[int]
    evidence_level: Optional[str]
    source_kind: Optional[str]
    diseases: list[str] = field(default_factory=list)
    endpoints: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    doi: Optional[str] = None
    pmid: Optional[str] = None
    pmcid: Optional[str] = None
    # Optional metadata (not all cards have these)
    authors: list[str] = field(default_factory=list)
    journal: Optional[str] = None
    # Evidence policy fields
    quoted_facts: list[str] = field(default_factory=list)
    supported_conclusions: list[str] = field(default_factory=list)
    llm_inferences: list[str] = field(default_factory=list)
    # Computed
    one_line_summary: Optional[str] = None
    file_path: Optional[str] = None  # Internal only


def is_research_mode_query(query: str) -> bool:
    """
    Detect if a query is a research-mode literature search.

    Examples:
    - "search latest papers about HCM"
    - "find recent studies on feline CKD"
    - "最新HCM文献"
    - "搜索FIP研究"
    """
    query_lower = query.lower()

    # English patterns
    en_patterns = [
        r"search.*papers",
        r"search.*studies",
        r"search.*research",
        r"search.*literature",
        r"find.*papers",
        r"find.*studies",
        r"latest.*papers",
        r"latest.*research",
        r"recent.*papers",
        r"recent.*studies",
        r"literature.*search",
        r"literature.*review",
    ]

    # Chinese patterns
    zh_patterns = [
        r"搜索.*文献",
        r"搜索.*研究",
        r"搜索.*论文",
        r"查找.*文献",
        r"查找.*研究",
        r"最新.*文献",
        r"最新.*研究",
        r"最新.*论文",
        r"文献.*搜索",
        r"文献.*检索",
    ]

    for pattern in en_patterns + zh_patterns:
        if re.search(pattern, query_lower):
            return True

    return False


def extract_disease_from_query(query: str) -> Optional[str]:
    """Extract the disease focus from a research query."""
    query_lower = query.lower()

    # For acronyms: just match the letters directly (works in both English and Chinese contexts)
    # For full names: use the full pattern
    disease_patterns = {
        "hcm": ["hcm", r"hypertrophic cardiomyopathy", r"心肌病", r"肥厚"],
        "ckd": ["ckd", r"chronic kidney", r"renal", r"肾", r"慢性肾"],
        "fip": ["fip", r"feline infectious peritonitis", r"传腹", r"传染性腹膜炎"],
        "ibd": ["ibd", r"inflammatory bowel", r"炎症性肠", r"肠病"],
        "fcv": ["fcv", r"calicivirus", r"杯状"],
        "diabetes": [r"diabetes", r"diabetic", r"糖尿病"],
        "obesity": [r"obesity", r"obese", r"肥胖"],
        "cancer": [r"cancer", r"tumor", r"carcinoma", r"lymphoma", r"肿瘤", r"癌"],
    }

    for disease, patterns in disease_patterns.items():
        for pattern in patterns:
            if re.search(pattern, query_lower):
                return disease

    return None


def parse_source_card(file_path: Path) -> Optional[SourceCard]:
    """Parse a source card markdown file into structured data."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    if not content.startswith("---"):
        return None

    # Find frontmatter boundaries
    end_idx = content.find("\n---", 3)
    if end_idx == -1:
        return None

    frontmatter = content[3:end_idx]
    body = content[end_idx + 4:]

    def extract_field(fm: str, field: str) -> Optional[str]:
        for line in fm.splitlines():
            if line.startswith(f"{field}:"):
                value = line.split(":", 1)[1].strip().strip("\"'")
                return value if value else None
        return None

    def extract_list(fm: str, field: str) -> list[str]:
        result = []
        in_field = False
        for line in fm.splitlines():
            if line.startswith(f"{field}:"):
                # Could be inline list or start of block
                inline = line.split(":", 1)[1].strip()
                if inline.startswith("["):
                    # Parse inline array
                    items = re.findall(r'[\w-]+', inline)
                    return items
                in_field = True
                continue
            if in_field:
                if line.startswith("  -"):
                    result.append(line[3:].strip().strip("\"'"))
                elif line and not line.startswith(" "):
                    break
        return result

    def extract_evidence_policy_list(fm: str, category: str) -> list[str]:
        """Extract items from evidence_policy.<category>."""
        result = []
        lines = fm.splitlines()
        in_evidence_policy = False
        in_category = False

        for i, line in enumerate(lines):
            if line.strip() == "evidence_policy:":
                in_evidence_policy = True
                continue
            if in_evidence_policy:
                if line.strip() == f"{category}:":
                    in_category = True
                    continue
                if in_category:
                    if line.startswith("    -"):
                        item = line[5:].strip().strip("\"'")
                        result.append(item)
                    elif line.strip() and not line.startswith("    "):
                        if not line.startswith("  "):
                            in_evidence_policy = False
                        in_category = False

        return result

    def extract_nested_field(fm: str, parent: str, child: str) -> Optional[str]:
        """Extract a field nested under a parent, e.g., links.doi."""
        lines = fm.splitlines()
        in_parent = False
        for line in lines:
            if line.strip() == f"{parent}:":
                in_parent = True
                continue
            if in_parent:
                if line.startswith(f"  {child}:"):
                    value = line.split(":", 1)[1].strip().strip("\"'")
                    return value if value else None
                elif line.strip() and not line.startswith(" "):
                    break
        return None

    # Extract one-line summary from body
    one_line_summary = None
    summary_match = re.search(r"##\s*One-Line Summary\s*\n+(.+?)(?:\n\n|\n##|$)", body)
    if summary_match:
        one_line_summary = summary_match.group(1).strip()

    card_id = extract_field(frontmatter, "id")
    if not card_id:
        return None

    year_str = extract_field(frontmatter, "year")
    year = int(year_str) if year_str and year_str.isdigit() else None

    # DOI can be at root level OR under links:
    doi = extract_field(frontmatter, "doi") or extract_nested_field(frontmatter, "links", "doi")

    # Extract authors if available (some cards have them)
    authors = extract_list(frontmatter, "authors")

    # Extract journal if available
    journal = extract_field(frontmatter, "journal")

    return SourceCard(
        id=card_id,
        title=extract_field(frontmatter, "title") or card_id,
        year=year,
        evidence_level=extract_field(frontmatter, "evidence_level"),
        source_kind=extract_field(frontmatter, "source_kind"),
        diseases=extract_list(frontmatter, "diseases"),
        endpoints=extract_list(frontmatter, "endpoints"),
        tags=extract_list(frontmatter, "tags"),
        doi=doi,
        pmid=extract_field(frontmatter, "pmid"),
        pmcid=extract_field(frontmatter, "pmcid"),
        authors=authors,
        journal=journal,
        quoted_facts=extract_evidence_policy_list(frontmatter, "quoted_fact"),
        supported_conclusions=extract_evidence_policy_list(frontmatter, "source_supported_conclusion"),
        llm_inferences=extract_evidence_policy_list(frontmatter, "llm_inference"),
        one_line_summary=one_line_summary,
        file_path=str(file_path.relative_to(VAULT_ROOT)),  # Internal use only
    )


def load_disease_sources(disease: str, vault_root: Path = VAULT_ROOT) -> list[SourceCard]:
    """Load all source cards for a specific disease."""
    papers_dir = vault_root / "raw" / "papers"
    if not papers_dir.exists():
        return []

    cards = []

    # Map disease to source prefix
    disease_prefixes = {
        "hcm": "src-hcm-",
        "ckd": "src-ckd-",
        "fip": "src-fip-",
        "ibd": "src-ibd-",
        "fcv": "src-fcv-",
        "diabetes": "src-diabetes-",
        "obesity": "src-obesity-",
        "cancer": "src-cancer-",
    }

    prefix = disease_prefixes.get(disease)
    if not prefix:
        return []

    for md_file in papers_dir.glob(f"{prefix}*.md"):
        card = parse_source_card(md_file)
        if card:
            cards.append(card)

    return cards


def categorize_sources(cards: list[SourceCard]) -> dict[str, list[SourceCard]]:
    """
    Categorize sources into clinical/therapeutic, diagnostic, and other.
    """
    clinical = []
    diagnostic = []
    other = []

    clinical_keywords = {"treatment", "therapy", "intervention", "efficacy", "outcome", "survival", "response", "remission"}
    diagnostic_keywords = {"diagnostic", "diagnosis", "biomarker", "screening", "detection", "marker", "imaging", "assessment"}

    for card in cards:
        endpoints_lower = {e.lower() for e in card.endpoints}
        tags_lower = {t.lower() for t in card.tags}
        combined = endpoints_lower | tags_lower

        is_clinical = bool(combined & clinical_keywords)
        is_diagnostic = bool(combined & diagnostic_keywords)

        if is_clinical:
            clinical.append(card)
        elif is_diagnostic:
            diagnostic.append(card)
        else:
            other.append(card)

    return {
        "clinical": clinical,
        "diagnostic": diagnostic,
        "other": other,
    }


def rank_sources(cards: list[SourceCard], top_n: int = 10) -> list[SourceCard]:
    """
    Rank sources by year (descending), evidence level, and completeness.
    """
    def score(card: SourceCard) -> tuple:
        year_score = card.year or 0

        # Evidence level scoring
        level_scores = {
            "meta-analysis": 5,
            "systematic-review": 4,
            "rct": 4,
            "original-study": 3,
            "case-series": 2,
            "review": 2,
            "case-report": 1,
        }
        level_score = level_scores.get(card.evidence_level or "", 0)

        # Completeness: has summary, has evidence policy
        completeness = 0
        if card.one_line_summary:
            completeness += 1
        if card.quoted_facts:
            completeness += 1
        if card.supported_conclusions:
            completeness += 1

        return (year_score, level_score, completeness)

    ranked = sorted(cards, key=score, reverse=True)
    return ranked[:top_n]


def build_research_mode_output(
    disease: str,
    cards: list[SourceCard],
    chinese: bool = False,
) -> str:
    """
    Build agent.ii.inc-style structured output for research queries.
    """
    categorized = categorize_sources(cards)

    # Get top papers overall
    top_papers = rank_sources(cards, top_n=10)

    # Get top clinical and diagnostic papers
    top_clinical = rank_sources(categorized["clinical"], top_n=5)
    top_diagnostic = rank_sources(categorized["diagnostic"], top_n=5)

    # Collect limitations from llm_inferences
    limitations = []
    for card in top_papers[:5]:
        limitations.extend(card.llm_inferences)

    # Build output
    if chinese:
        return _build_chinese_output(disease, top_papers, top_clinical, top_diagnostic, limitations)
    else:
        return _build_english_output(disease, top_papers, top_clinical, top_diagnostic, limitations)


def _is_placeholder_content(text: str) -> bool:
    """
    Check if text is placeholder/low-quality content that shouldn't be shown to users.

    NOTE: Be careful not to filter legitimate research content. Only filter
    actual internal placeholder messages, not mentions of research methodologies.
    """
    if not text:
        return True
    text_lower = text.lower()

    # Specific placeholder patterns - must be precise to avoid false positives
    placeholder_patterns = [
        "first-pass intake object",
        "candidate source from sheet",  # More specific than just "candidate"
        "from sheet row",
        "use it for triage until",
        "until abstract or full-text extraction proves",
        "placeholder",
        "needs extraction",
        "this card is a first-pass",
        "this card should control triage",
    ]
    return any(pattern in text_lower for pattern in placeholder_patterns)


def _format_paper_entry(card: SourceCard, index: int, chinese: bool = False) -> str:
    """
    Format a single paper entry for user-facing output.

    Format follows academic citation style similar to agent.ii.inc:
    1. Author, et al. *Title.* Journal. Year.
    2. URL: https://doi.org/...
    3. **Why it matters:** Key finding
    4. **Takeaway:** Insight

    NOTE: Internal identifiers (src-xxx, file_path) are NEVER shown.
    Placeholder content is filtered out.
    """
    lines = []

    # Line 1: Author (if available), Title (italicized), Journal, Year
    author_str = ""
    if card.authors:
        if len(card.authors) == 1:
            author_str = f"{card.authors[0]}. "
        elif len(card.authors) == 2:
            author_str = f"{card.authors[0]} & {card.authors[1]}. "
        else:
            author_str = f"{card.authors[0]}, et al. "

    journal_str = f" *{card.journal}.*" if card.journal else ""
    year_str = f" {card.year}." if card.year else ""

    # Main citation line
    lines.append(f"{index}. {author_str}*{card.title}.*{journal_str}{year_str}")

    # Line 2: URL (DOI preferred, then PMID, then PMCID)
    if card.doi:
        url_label = "URL" if not chinese else "链接"
        lines.append(f"   {url_label}: https://doi.org/{card.doi}")
    elif card.pmid:
        url_label = "PubMed" if not chinese else "PubMed"
        lines.append(f"   {url_label}: https://pubmed.ncbi.nlm.nih.gov/{card.pmid}/")
    elif card.pmcid:
        url_label = "PMC" if not chinese else "PMC"
        lines.append(f"   {url_label}: https://pmc.ncbi.nlm.nih.gov/articles/{card.pmcid}/")

    # Line 3: Why it matters (from supported_conclusions - skip placeholders)
    why_shown = False
    if card.supported_conclusions:
        for conclusion in card.supported_conclusions:
            if not _is_placeholder_content(conclusion):
                why_label = "**要点：**" if chinese else "**Why it matters:**"
                lines.append(f"   {why_label} {conclusion}")
                why_shown = True
                break

    # Line 4: Takeaway (from one_line_summary or quoted_facts - skip placeholders)
    if not why_shown:
        takeaway = None
        if card.one_line_summary and not _is_placeholder_content(card.one_line_summary):
            takeaway = card.one_line_summary
        elif card.quoted_facts:
            # Find first non-placeholder quoted fact
            for fact in card.quoted_facts:
                if not _is_placeholder_content(fact):
                    takeaway = fact
                    break

        if takeaway:
            takeaway_label = "**要点：**" if chinese else "**Takeaway:**"
            lines.append(f"   {takeaway_label} {takeaway[:200]}{'...' if len(takeaway) > 200 else ''}")

    return "\n".join(lines)


def _build_english_output(
    disease: str,
    top_papers: list[SourceCard],
    top_clinical: list[SourceCard],
    top_diagnostic: list[SourceCard],
    limitations: list[str],
) -> str:
    """Build English structured output."""
    sections = []

    disease_upper = disease.upper()

    sections.append(f"# Research Literature: Feline {disease_upper}\n")
    sections.append(f"Found {len(top_papers)} relevant sources in the local vault. [source_supported_conclusion]\n")

    # Best recent papers
    if top_papers:
        sections.append("## Best recent papers to read first\n")
        sections.append("*Ranked by year, evidence level, and extraction depth.*\n")
        for i, card in enumerate(top_papers[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=False))
            sections.append("")

    # Clinical/therapeutic papers
    if top_clinical:
        sections.append("## Latest clinical/therapeutic papers\n")
        for i, card in enumerate(top_clinical[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=False))
            sections.append("")

    # Diagnostic papers
    if top_diagnostic:
        sections.append("## Best recent diagnostic papers\n")
        for i, card in enumerate(top_diagnostic[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=False))
            sections.append("")

    # What papers collectively say (synthesis)
    sections.append("## What these papers collectively say\n")
    if top_papers:
        key_findings = []
        for card in top_papers[:5]:
            if card.supported_conclusions:
                # Find first non-placeholder conclusion
                for conclusion in card.supported_conclusions:
                    if not _is_placeholder_content(conclusion):
                        key_findings.append(f"- {conclusion}")
                        break
        if key_findings:
            sections.append("Key supported conclusions across sources:\n")
            sections.extend(key_findings)
            sections.append("")
        else:
            sections.append("*No synthesis available — sources lack extracted conclusions.*\n")

    # Shortest must-read list
    sections.append("## If you want the shortest \"must-read\" list\n")
    if top_papers:
        sections.append(f"If I had to narrow it to {min(3, len(top_papers))} papers:\n")
        for i, card in enumerate(top_papers[:3], 1):
            year_str = f" ({card.year})" if card.year else ""
            # Use title (truncated if needed), not internal ID
            title_short = card.title[:80] + "..." if len(card.title) > 80 else card.title
            # Only show summary if it's not placeholder content
            summary = card.one_line_summary or ""
            if summary and not _is_placeholder_content(summary):
                sections.append(f"{i}. *{title_short}*{year_str} — {summary[:100]}")
            else:
                sections.append(f"{i}. *{title_short}*{year_str}")
        sections.append("")

    # Important limitations
    sections.append("## Important limitations\n")
    if limitations:
        seen = set()
        for lim in limitations[:5]:
            if lim not in seen:
                sections.append(f"- {lim}")
                seen.add(lim)
    else:
        sections.append("- These are local vault sources only; external databases may have newer publications.")
        sections.append("- Evidence depth varies across sources; some are title-only placeholders.")
        sections.append("- Cross-species translation (rodent → feline) requires careful boundary checking.")
    sections.append("")

    sections.append("---")
    sections.append("*This output is generated from the local feline-research-os vault using structured source cards.*")

    return "\n".join(sections)


def _build_chinese_output(
    disease: str,
    top_papers: list[SourceCard],
    top_clinical: list[SourceCard],
    top_diagnostic: list[SourceCard],
    limitations: list[str],
) -> str:
    """Build Chinese structured output."""
    sections = []

    disease_names = {
        "hcm": "肥厚型心肌病 (HCM)",
        "ckd": "慢性肾脏病 (CKD)",
        "fip": "传染性腹膜炎 (FIP)",
        "ibd": "炎症性肠病 (IBD)",
        "fcv": "杯状病毒 (FCV)",
        "diabetes": "糖尿病",
        "obesity": "肥胖症",
        "cancer": "肿瘤",
    }

    disease_cn = disease_names.get(disease, disease.upper())

    sections.append(f"# 文献检索：猫{disease_cn}\n")
    sections.append(f"在本地知识库中找到 {len(top_papers)} 个相关文献。 [source_supported_conclusion]\n")

    # Best recent papers
    if top_papers:
        sections.append("## 推荐优先阅读的文献\n")
        sections.append("*按年份、证据等级和提取深度排序。*\n")
        for i, card in enumerate(top_papers[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=True))
            sections.append("")

    # Clinical/therapeutic papers
    if top_clinical:
        sections.append("## 临床/治疗类文献\n")
        for i, card in enumerate(top_clinical[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=True))
            sections.append("")

    # Diagnostic papers
    if top_diagnostic:
        sections.append("## 诊断类文献\n")
        for i, card in enumerate(top_diagnostic[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=True))
            sections.append("")

    # What papers collectively say
    sections.append("## 这些文献共同表明\n")
    if top_papers:
        key_findings = []
        for card in top_papers[:5]:
            if card.supported_conclusions:
                # Find first non-placeholder conclusion
                for conclusion in card.supported_conclusions:
                    if not _is_placeholder_content(conclusion):
                        key_findings.append(f"- {conclusion}")
                        break
        if key_findings:
            sections.append("各文献的核心结论：\n")
            sections.extend(key_findings)
            sections.append("")
        else:
            sections.append("*暂无综合结论 — 源文献缺少提取的结论。*\n")

    # Shortest must-read list
    sections.append("## 最短必读清单\n")
    if top_papers:
        sections.append(f"如果只能读 {min(3, len(top_papers))} 篇：\n")
        for i, card in enumerate(top_papers[:3], 1):
            year_str = f" ({card.year})" if card.year else ""
            # Use title (truncated if needed), not internal ID
            title_short = card.title[:80] + "..." if len(card.title) > 80 else card.title
            # Only show summary if it's not placeholder content
            summary = card.one_line_summary or ""
            if summary and not _is_placeholder_content(summary):
                sections.append(f"{i}. *{title_short}*{year_str} — {summary[:100]}")
            else:
                sections.append(f"{i}. *{title_short}*{year_str}")
        sections.append("")

    # Important limitations
    sections.append("## 重要局限\n")
    if limitations:
        seen = set()
        for lim in limitations[:5]:
            if lim not in seen:
                sections.append(f"- {lim}")
                seen.add(lim)
    else:
        sections.append("- 这些仅为本地知识库的文献；外部数据库可能有更新的发表。")
        sections.append("- 各文献的证据深度不同；部分仅为标题占位符。")
        sections.append("- 跨物种转化（啮齿类→猫）需谨慎评估边界。")
    sections.append("")

    sections.append("---")
    sections.append("*此输出由本地 feline-research-os 知识库的结构化文献卡片生成。*")

    return "\n".join(sections)


# ---------------------------------------------------------------------------
# PubMed API Augmentation Layer
# ---------------------------------------------------------------------------

def _build_pubmed_query(disease: str) -> str:
    """Build an optimized PubMed query for feline disease research."""
    # Use specific feline terms to ensure veterinary relevance
    # Note: "cat" and "cats" alone are too ambiguous (CAT scans, catalysis, etc.)
    # Using "feline" as primary filter, with "Felis catus" for species specificity
    feline_filter = '("feline"[Title/Abstract] OR "Felis catus"[Title/Abstract] OR "domestic cat"[Title/Abstract])'

    disease_terms = {
        "hcm": f'{feline_filter} AND ("hypertrophic cardiomyopathy"[Title/Abstract] OR "HCM"[Title/Abstract])',
        "ckd": f'{feline_filter} AND ("chronic kidney disease"[Title/Abstract] OR "renal failure"[Title/Abstract] OR "kidney failure"[Title/Abstract])',
        "fip": '("feline infectious peritonitis"[Title/Abstract] OR "FIP"[Title/Abstract]) AND (coronavirus OR treatment OR diagnosis)',
        "ibd": f'{feline_filter} AND ("inflammatory bowel disease"[Title/Abstract] OR "lymphocytic enteritis"[Title/Abstract])',
        "fcv": '"feline calicivirus"[Title/Abstract]',
        "diabetes": f'{feline_filter} AND ("diabetes mellitus"[Title/Abstract] OR "diabetic"[Title/Abstract])',
        "obesity": f'{feline_filter} AND ("obesity"[Title/Abstract] OR "overweight"[Title/Abstract] OR "body condition"[Title/Abstract])',
        "cancer": f'{feline_filter} AND ("cancer"[Title/Abstract] OR "tumor"[Title/Abstract] OR "neoplasm"[Title/Abstract] OR "carcinoma"[Title/Abstract] OR "lymphoma"[Title/Abstract])',
    }
    return disease_terms.get(disease, f'{feline_filter} AND "{disease}"[Title/Abstract]')


def _format_external_result(result: "ExternalSearchResult", index: int, chinese: bool = False) -> str:
    """Format a single external search result."""
    year_str = f" ({result.year})" if result.year else ""

    lines = [f"{index}. **{result.title}**{year_str} [external]"]

    # Authors
    if result.authors:
        author_str = ", ".join(result.authors[:3])
        if len(result.authors) > 3:
            author_str += " et al."
        author_label = "作者" if chinese else "Authors"
        lines.append(f"   {author_label}: {author_str}")

    # Journal
    if result.journal:
        journal_label = "期刊" if chinese else "Journal"
        lines.append(f"   {journal_label}: {result.journal}")

    # DOI/PMID links
    if result.doi:
        lines.append(f"   DOI: https://doi.org/{result.doi}")
    elif result.pmid:
        lines.append(f"   PubMed: https://pubmed.ncbi.nlm.nih.gov/{result.pmid}/")

    return "\n".join(lines)


def fetch_pubmed_augmentation(
    disease: str,
    max_results: int = 5,
    chinese: bool = False,
) -> tuple[str, list["ExternalSearchResult"]]:
    """
    Fetch PubMed results as augmentation layer.

    Returns:
        (formatted_section, results_list)
    """
    if not EXTERNAL_SEARCH_AVAILABLE:
        note = "PubMed 增强不可用（缺少 external_search 模块）" if chinese else "PubMed augmentation unavailable (external_search module not found)"
        return f"\n*{note}*\n", []

    query = _build_pubmed_query(disease)
    config = ExternalSearchConfig(
        allow_external=True,
        max_results=max_results,
        timeout_seconds=15,
    )

    response = search_pubmed(query, config)

    if response.error:
        error_label = "错误" if chinese else "Error"
        return f"\n*PubMed {error_label}: {response.error}*\n", []

    if not response.results:
        no_results = "PubMed 未返回结果" if chinese else "PubMed returned no results"
        return f"\n*{no_results}*\n", []

    # Build section
    lines = []
    if chinese:
        lines.append(f"\n## PubMed 最新文献（外部检索）\n")
        lines.append(f"*从 PubMed 检索到 {response.total_found} 篇相关文献，显示前 {len(response.results)} 篇。*\n")
    else:
        lines.append(f"\n## Latest from PubMed (external search)\n")
        lines.append(f"*Found {response.total_found} results on PubMed, showing top {len(response.results)}.*\n")

    for i, result in enumerate(response.results, 1):
        lines.append(_format_external_result(result, i, chinese))
        lines.append("")

    # Add note about external sources
    if chinese:
        lines.append("*注：外部文献未经本地知识库处理；需人工审核后方可入库。*\n")
    else:
        lines.append("*Note: External results are not processed by the local vault; manual review required before intake.*\n")

    return "\n".join(lines), response.results


def handle_research_query(
    query: str,
    chinese: bool = False,
    include_external: bool = True,
) -> tuple[str, list[str]]:
    """
    Main entry point for research-mode queries.

    Returns:
        (formatted_output, source_ids)
    """
    disease = extract_disease_from_query(query)

    if not disease:
        # Fallback: search all diseases
        if chinese:
            return (
                "未能识别具体疾病类型。请在查询中包含疾病名称，如：\n\n"
                "- \"搜索HCM最新文献\"\n"
                "- \"查找CKD相关研究\"\n"
                "- \"FIP文献检索\"\n\n"
                "[llm_inference]",
                []
            )
        else:
            return (
                "Could not identify a specific disease in your query. Please include a disease name, e.g.:\n\n"
                "- \"search latest papers about HCM\"\n"
                "- \"find CKD studies\"\n"
                "- \"FIP literature search\"\n\n"
                "[llm_inference]",
                []
            )

    cards = load_disease_sources(disease)

    if not cards:
        if chinese:
            return (
                f"未在本地知识库中找到 {disease.upper()} 相关文献。\n\n"
                "可能原因：\n"
                "- 该疾病模块尚未构建\n"
                "- 文献卡片缺少必要的元数据\n\n"
                "[llm_inference]",
                []
            )
        else:
            return (
                f"No {disease.upper()} sources found in the local vault.\n\n"
                "Possible reasons:\n"
                "- The disease module is not yet built\n"
                "- Source cards lack required metadata\n\n"
                "[llm_inference]",
                []
            )

    # Build local vault output
    output = build_research_mode_output(disease, cards, chinese=chinese)
    source_ids = [card.id for card in cards[:10]]

    # Add PubMed augmentation if enabled
    if include_external and EXTERNAL_SEARCH_AVAILABLE:
        pubmed_section, external_results = fetch_pubmed_augmentation(
            disease,
            max_results=5,
            chinese=chinese,
        )
        if external_results:
            # Insert before the final "---" separator
            output_parts = output.rsplit("---", 1)
            if len(output_parts) == 2:
                output = output_parts[0] + pubmed_section + "---" + output_parts[1]
            else:
                output += pubmed_section

    return output, source_ids


def handle_research_query_local_only(query: str, chinese: bool = False) -> tuple[str, list[str]]:
    """
    Research query without external API calls.
    Use this for local-only mode or when external search is not desired.
    """
    return handle_research_query(query, chinese=chinese, include_external=False)


# ---------------------------------------------------------------------------
# CLI for testing
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python research_mode.py 'search latest papers about HCM'")
        print("       python research_mode.py --local-only 'search CKD papers'")
        sys.exit(1)

    local_only = "--local-only" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--local-only"]

    query = " ".join(args)
    chinese = any(ord(c) > 0x3000 for c in query)

    if is_research_mode_query(query):
        output, sources = handle_research_query(
            query,
            chinese=chinese,
            include_external=not local_only,
        )
        print(output)
        print(f"\n[Local sources: {', '.join(sources)}]")
    else:
        print(f"Not a research-mode query: {query}")
