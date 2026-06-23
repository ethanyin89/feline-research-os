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

# Import deep extraction module
try:
    from deep_extraction import (
        has_deep_extraction,
        parse_deep_extraction,
        get_distilled_why_it_matters,
        get_distilled_takeaway,
    )
    DEEP_EXTRACTION_AVAILABLE = True
except ImportError:
    DEEP_EXTRACTION_AVAILABLE = False


@dataclass
class TensionWith:
    """Represents tension between this source and another source."""
    source_id: str
    tension_type: str  # "contradicts" | "extends" | "qualifies"
    description: str


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
    url: Optional[str] = None
    status: Optional[str] = None
    verification_status: Optional[str] = None
    # Optional metadata (not all cards have these)
    authors: list[str] = field(default_factory=list)
    journal: Optional[str] = None
    # Evidence policy fields (existing)
    quoted_facts: list[str] = field(default_factory=list)
    supported_conclusions: list[str] = field(default_factory=list)
    llm_inferences: list[str] = field(default_factory=list)
    # Evidence policy fields (new for enhanced presentation)
    core_argument: Optional[str] = None  # 论文的核心论点（一句话）
    implicit_premise: Optional[str] = None  # 论文隐含的前提假设
    unexpected_finding: Optional[str] = None  # 意外发现或反直觉结果（旧字段，向后兼容）
    title_gap: Optional[str] = None  # 这篇论文比标题看起来更值得读的原因
    evidence_boundary: Optional[str] = None  # 证据边界：这篇论文回答不了什么问题
    study_design: Optional[str] = None  # 研究设计摘要（如：回顾性横断面，91猫按ACVIM分期）
    tension_with: list[TensionWith] = field(default_factory=list)  # 与其他文献的张力
    # Deep extraction (V3)
    has_deep_extraction: bool = False  # Whether a deep extraction file exists
    evidence_nodes: list[str] = field(default_factory=list)
    deep_extraction_why: Optional[str] = None  # Distilled from Phase 2/3
    deep_extraction_takeaway: Optional[str] = None  # Distilled from Phase 2/3
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
    - "构建 feline HCM 近三年证据地图"
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
        r"evidence.*map",
        r"endpoint",
        r"workspace",
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
        r"构建.*证据",
        r"构建.*地图",
        r"比较.*指标",
        r"比较.*诊断",
        r"梳理.*终点",
        r"梳理.*药效",
        r"提炼.*指标",
        r"提炼.*发现",
        r"分析.*病毒",
        r"分析.*演化",
        r"研究.*工作台",
    ]

    for pattern in en_patterns + zh_patterns:
        if re.search(pattern, query_lower):
            return True

    # Check for direct presence of research task keywords in Chinese
    research_task_keywords = ["构建", "比较", "梳理", "提炼", "证据地图", "药效终点", "评价指标", "工作台"]
    if any(kw in query_lower for kw in research_task_keywords):
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

    def extract_evidence_policy_field(fm: str, field_name: str) -> Optional[str]:
        """Extract a simple string field from evidence_policy."""
        lines = fm.splitlines()
        in_evidence_policy = False
        for line in lines:
            if line.strip() == "evidence_policy:":
                in_evidence_policy = True
                continue
            if in_evidence_policy:
                if line.startswith(f"  {field_name}:"):
                    value = line.split(":", 1)[1].strip().strip("\"'")
                    return value if value else None
                elif line.strip() and not line.startswith(" "):
                    break
        return None

    def extract_tension_with(fm: str) -> list[TensionWith]:
        """Extract tension_with list from evidence_policy."""
        lines = fm.splitlines()
        tensions = []
        in_evidence_policy = False
        in_tension_with = False
        current_tension: dict = {}

        for line in lines:
            if line.strip() == "evidence_policy:":
                in_evidence_policy = True
                continue
            if in_evidence_policy:
                if line.strip() == "tension_with:":
                    in_tension_with = True
                    continue
                if in_tension_with:
                    if line.startswith("    - source_id:"):
                        if current_tension:
                            tensions.append(TensionWith(
                                source_id=current_tension.get("source_id", ""),
                                tension_type=current_tension.get("type", ""),
                                description=current_tension.get("description", ""),
                            ))
                        current_tension = {"source_id": line.split(":", 1)[1].strip().strip("\"'")}
                    elif line.startswith("      type:"):
                        current_tension["type"] = line.split(":", 1)[1].strip().strip("\"'")
                    elif line.startswith("      description:"):
                        current_tension["description"] = line.split(":", 1)[1].strip().strip("\"'")
                    elif line.strip() and not line.startswith("    "):
                        if current_tension:
                            tensions.append(TensionWith(
                                source_id=current_tension.get("source_id", ""),
                                tension_type=current_tension.get("type", ""),
                                description=current_tension.get("description", ""),
                            ))
                        break
        if current_tension and in_tension_with:
            tensions.append(TensionWith(
                source_id=current_tension.get("source_id", ""),
                tension_type=current_tension.get("type", ""),
                description=current_tension.get("description", ""),
            ))
        return tensions

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

    # Links can be at root level OR under links:
    doi = extract_field(frontmatter, "doi") or extract_nested_field(frontmatter, "links", "doi")
    url = extract_field(frontmatter, "url") or extract_nested_field(frontmatter, "links", "url")

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
        url=url,
        status=extract_field(frontmatter, "status"),
        verification_status=extract_field(frontmatter, "verification_status"),
        authors=authors,
        journal=journal,
        quoted_facts=extract_evidence_policy_list(frontmatter, "quoted_fact"),
        supported_conclusions=extract_evidence_policy_list(frontmatter, "source_supported_conclusion"),
        llm_inferences=extract_evidence_policy_list(frontmatter, "llm_inference"),
        # New enhanced evidence policy fields
        core_argument=extract_evidence_policy_field(frontmatter, "core_argument"),
        implicit_premise=extract_evidence_policy_field(frontmatter, "implicit_premise"),
        unexpected_finding=extract_evidence_policy_field(frontmatter, "unexpected_finding"),
        title_gap=extract_evidence_policy_field(frontmatter, "title_gap"),
        evidence_boundary=extract_evidence_policy_field(frontmatter, "evidence_boundary"),
        study_design=extract_evidence_policy_field(frontmatter, "study_design"),
        tension_with=extract_tension_with(frontmatter),
        one_line_summary=one_line_summary,
        file_path=str(file_path.relative_to(VAULT_ROOT)),  # Internal use only
        # Deep extraction fields populated later by enrich_with_deep_extraction
        has_deep_extraction=False,
        deep_extraction_why=None,
        deep_extraction_takeaway=None,
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
            # Enrich with deep extraction if available
            card = enrich_with_deep_extraction(card)
            cards.append(card)

    return cards


def enrich_with_deep_extraction(card: SourceCard) -> SourceCard:
    """
    Enrich a source card with content from its deep extraction file if available.

    Updates:
    - has_deep_extraction: True if ext-{source_id}.md exists
    - deep_extraction_why: Distilled "Why it matters" from Phase 2/3
    - deep_extraction_takeaway: Distilled takeaway from Phase 2/3
    """
    if not DEEP_EXTRACTION_AVAILABLE:
        return card

    if not has_deep_extraction(card.id):
        return card

    extraction = parse_deep_extraction(card.id)
    if not extraction:
        return card

    card.has_deep_extraction = True
    card.deep_extraction_why = get_distilled_why_it_matters(extraction)
    card.deep_extraction_takeaway = get_distilled_takeaway(extraction)
    card.evidence_nodes = getattr(extraction, "evidence_nodes", [])

    return card


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
    Rank sources using the 4-factor weighted formula defined in DESIGN.md:

    ranking_score = (evidence_level × 0.35) + (recency × 0.25) +
                    (source_kind × 0.25) + (extraction_depth × 0.15)

    See DESIGN.md "Research Mode — Best Papers 排序标准" for full specification.
    """
    def compute_score(card: SourceCard) -> float:
        # Factor 1: Evidence Level (35%)
        evidence_scores = {
            "meta-analysis": 10,
            "systematic-review": 9,
            "rct": 8,
            "guideline": 8,
            "original-study": 6,
            "review": 5,
            "case-series": 3,
            "case-report": 2,
            "expert-opinion": 1,
        }
        evidence_score = evidence_scores.get(card.evidence_level or "", 0)

        # Factor 2: Recency (25%)
        year = card.year or 0
        if year >= 2024:
            recency_score = 10
        elif year >= 2021:
            recency_score = 8
        elif year >= 2018:
            recency_score = 6
        elif year >= 2015:
            recency_score = 4
        elif year >= 2010:
            recency_score = 2
        else:
            recency_score = 1

        # Factor 3: Source Kind (25%)
        kind_scores = {
            "guideline": 10,
            "paper": 7,
            "review-article": 6,
            "regulatory": 5,
            "product-info": 3,
            "internal-doc": 2,
            "marketing": 1,
        }
        kind_score = kind_scores.get(card.source_kind or "", 5)  # Default 5 for unlabeled

        # Factor 4: Extraction Depth (15%)
        if card.quoted_facts and card.supported_conclusions:
            depth_score = 10  # Full deep extraction
        elif card.one_line_summary:
            depth_score = 6   # Has summary
        elif card.title:
            depth_score = 3   # Only frontmatter
        else:
            depth_score = 1   # Minimal

        # Weighted combination
        ranking_score = (
            evidence_score * 0.35 +
            recency_score * 0.25 +
            kind_score * 0.25 +
            depth_score * 0.15
        )

        return ranking_score

    ranked = sorted(cards, key=compute_score, reverse=True)
    return ranked[:top_n]


def is_research_ready_source(card: SourceCard) -> bool:
    """Return True when a card can support reader-facing research synthesis."""
    status = _clean_label(card.status)
    verification = _clean_label(card.verification_status)
    if verification in {"title-only", "metadata-unavailable"}:
        return False
    if status == "ingested" and not (
        card.quoted_facts or card.supported_conclusions or card.one_line_summary
    ):
        return False
    low_quality_text = " ".join([
        card.one_line_summary or "",
        *(card.quoted_facts or []),
        *(card.supported_conclusions or []),
        *(card.llm_inferences or []),
    ])
    if _is_placeholder_content(low_quality_text):
        return False
    return True


def rank_research_ready_sources(cards: list[SourceCard], top_n: int = 10) -> list[SourceCard]:
    """Rank only sources deep enough for the main research report."""
    ready = [card for card in cards if is_research_ready_source(card)]
    return rank_sources(ready, top_n=top_n)


def rank_depth_queue_sources(cards: list[SourceCard], top_n: int = 10) -> list[SourceCard]:
    """Rank sources that look important but need extraction before reader-facing use."""
    queued = [card for card in cards if not is_research_ready_source(card)]
    return rank_sources(queued, top_n=top_n)


def build_research_mode_output(
    disease: str,
    cards: list[SourceCard],
    chinese: bool = False,
    bilingual: bool = False,
) -> str:
    """
    Build agent.ii.inc-style structured output for research queries.
    """
    categorized = categorize_sources(cards)

    # Get top papers overall. The main report excludes title-only / first-pass
    # records; those belong in a depth queue, not in reader-facing recommendations.
    top_papers = rank_research_ready_sources(cards, top_n=10)
    depth_queue = rank_depth_queue_sources(cards, top_n=5)

    # Get top clinical and diagnostic papers
    top_clinical = rank_research_ready_sources(categorized["clinical"], top_n=5)
    top_diagnostic = rank_research_ready_sources(categorized["diagnostic"], top_n=5)

    # Collect limitations from llm_inferences
    limitations = []
    for card in top_papers[:5]:
        limitations.extend(card.llm_inferences)

    if bilingual:
        english = _build_english_output(disease, top_papers, top_clinical, top_diagnostic, limitations, depth_queue=depth_queue)
        chinese_report = _build_chinese_output(disease, top_papers, top_clinical, top_diagnostic, limitations, depth_queue=depth_queue)
        if chinese:
            return "\n\n".join([
                "# 研究交付物 / Research Deliverables",
                "## 中文报告",
                chinese_report,
                "## English report",
                english,
            ])
        return "\n\n".join([
            "# Research Deliverables / 研究交付物",
            "## English report",
            english,
            "## Chinese report",
            chinese_report,
        ])

    # Build output
    if chinese:
        return _build_chinese_output(disease, top_papers, top_clinical, top_diagnostic, limitations, depth_queue=depth_queue)
    else:
        return _build_english_output(disease, top_papers, top_clinical, top_diagnostic, limitations, depth_queue=depth_queue)


def _research_scope_label(disease: str, chinese: bool) -> str:
    disease_names = {
        "hcm": "feline hypertrophic cardiomyopathy (HCM)",
        "ckd": "feline chronic kidney disease (CKD)",
        "fip": "feline infectious peritonitis (FIP)",
        "ibd": "feline inflammatory bowel disease (IBD)",
        "fcv": "feline calicivirus (FCV)",
        "diabetes": "feline diabetes mellitus",
        "obesity": "feline obesity",
        "cancer": "feline cancer / neoplasia",
    }
    disease_names_zh = {
        "hcm": "猫肥厚型心肌病 (HCM)",
        "ckd": "猫慢性肾脏病 (CKD)",
        "fip": "猫传染性腹膜炎 (FIP)",
        "ibd": "猫炎症性肠病 (IBD)",
        "fcv": "猫杯状病毒 (FCV)",
        "diabetes": "猫糖尿病",
        "obesity": "猫肥胖症",
        "cancer": "猫肿瘤 / 癌症",
    }
    return (disease_names_zh if chinese else disease_names).get(disease, disease.upper())


def _build_research_contract_section(
    query: str,
    disease: str,
    local_count: int,
    pubmed_query: Optional[str],
    pubmed_total: Optional[int],
    pubmed_shown: int,
    include_external: bool,
    chinese: bool,
) -> str:
    """
    Build a concise, user-facing research contract / audit note.

    This is intentionally not a raw chain-of-thought panel. It exposes the
    decisions that matter for trust: scope, source hierarchy, ranking rule, and
    freshness boundary.
    """
    scope = _research_scope_label(disease, chinese)

    if chinese:
        lines = [
            "## 研究范围与审计说明",
            "",
            f"- **用户请求解释：** 将 `{query}` 解释为围绕 **{scope}** 的近期文献检索与证据综述。",
            "- **标准转换：** 用户请求 → 疾病边界 → 本地文献检索 → 论文排序 → 临床/诊断主题分组 → PubMed 外部补充。",
            f"- **本地证据范围：** 本地知识库中可解析的该疾病文献记录：{local_count} 篇；下方优先展示排序最高的文献。",
            "- **Best 排序标准：** evidence level 35% + recency 25% + source kind 25% + extraction depth 15%。",
            "- **high-impact 边界：** 当前优先使用 higher-visibility / broader journals 与临床相关性；若未接入 JCR、Scimago、CiteScore 或 Clarivate，不把它声称为严格影响因子排名。",
        ]
        if include_external and pubmed_query:
            total = "未知" if pubmed_total is None else str(pubmed_total)
            lines.extend([
                f"- **外部新文献检查：** PubMed query `{pubmed_query}`；返回总数 {total}，展示 {pubmed_shown} 条。",
                "- **latest 边界：** PubMed 结果按发表日期检索补充；外部条目尚未入库，不能直接当作已审计证据。未返回结果也不等于证明不存在新论文。",
            ])
        elif include_external:
            lines.append("- **外部新文献检查：** PubMed 增强不可用或未返回可展示结果；不要据此声称没有更新论文。")
        else:
            lines.append("- **外部新文献检查：** 本次为 local-only 输出；不能声称覆盖最新外部数据库。")
        lines.append("")
        return "\n".join(lines)

    lines = [
        "## Research contract and audit note",
        "",
        f"- **Interpreted request:** `{query}` was treated as a recent literature search and evidence summary for **{scope}**.",
        "- **Standard conversion:** user request -> disease boundary -> local literature retrieval -> paper ranking -> clinical/diagnostic grouping -> PubMed augmentation.",
        f"- **Local evidence scope:** {local_count} parseable disease literature records in the local vault; the report surfaces the highest-ranked papers first.",
        "- **Best-paper ranking:** evidence level 35% + recency 25% + source kind 25% + extraction depth 15%.",
        "- **High-impact boundary:** this prioritizes higher-visibility / broader journals plus clinical relevance; without JCR, Scimago, CiteScore, or Clarivate data, it is not a strict impact-factor ranking.",
    ]
    if include_external and pubmed_query:
        total = "unknown" if pubmed_total is None else str(pubmed_total)
        lines.extend([
            f"- **External freshness check:** PubMed query `{pubmed_query}`; total returned {total}, showing {pubmed_shown}.",
            "- **Latest boundary:** PubMed augments the local vault by publication date; external items still need intake before becoming audited vault evidence. A missing result here is not proof that no newer paper exists.",
        ])
    elif include_external:
        lines.append("- **External freshness check:** PubMed augmentation was unavailable or returned no displayable results; do not treat this as proof that no newer paper exists.")
    else:
        lines.append("- **External freshness check:** this is a local-only output and cannot claim live external-database coverage.")
    lines.append("")
    return "\n".join(lines)


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
        "the intake sheet lists this title",  # Auto-generated placeholder
        "intake sheet lists",
        "the intake sheet locator is",  # Auto-generated placeholder with URL
        "intake sheet locator",
    ]
    return any(pattern in text_lower for pattern in placeholder_patterns)


def _to_chinese_research_text(text: str) -> str:
    """
    Produce a readable Chinese rendering for extracted source-card snippets.

    The local vault stores many source-card conclusions in English. Research Mode
    must preserve an English report and also provide a Chinese deliverable without
    exposing raw internal IDs. This lightweight terminology pass keeps paper titles
    and identifiers intact, while translating common veterinary research language.
    It is deliberately conservative; unclear biomedical terms are left in English.
    """
    if not text:
        return text
    if re.search(r"[\u3400-\u9fff]", text):
        return text

    lowered = text.lower()
    exact_meaning_map = {
        "frontier biomarker work already exists": "HCM 文献中已经出现前沿生物标志物研究；这类研究应与常规筛查标志物分开解读。",
        "nt-probnp and cardiac troponin i have several limitations": "摘要指出，NT-proBNP 和心肌肌钙蛋白 I 用于 HCM 筛查时存在多项局限。",
        "genotype-phenotype and severity pressure": "基因型-表型关系以及疾病严重程度，已经是猫 HCM 研究中的重要分支。",
        "feline hcm is primarily related to mutations in the mybpc3 and myh7 genes": "摘要指出，猫 HCM 主要与 MYBPC3 和 MYH7 基因突变相关。",
        "targeted pharmacology for hcm with lvot obstruction": "摘要将该研究定位为 HCM 合并左心室流出道梗阻的靶向药理学研究，因此肌节靶向干预应作为明确的转化研究分支。",
        "left-ventricular outflow tract obstruction is present in approximately two-thirds": "摘要指出，左心室流出道梗阻在人类 HCM 患者中较常见，并会显著增加疾病并发症风险；这为猫 HCM 的转化治疗研究提供背景。",

        # src-ckd-030
        "the open full article reports a single-arm eight-week pilot: 12 cats enrolled, 6 completed, and 6 dropped out": "公开全文报告了一项为期8周的单臂试点研究：12只猫入组，6只完成，6只脱落。",
        "the six completers included one stage 2 and five stage 3 ckd cats": "完成试验的6只猫包括1只2期和5只3期慢性肾脏病（CKD）猫。",
        "plasma tmao, indoxyl sulfate, p-cresyl sulfate, and phenyl sulfate changes were not statistically significant; serum phosphate significantly increased": "血浆 TMAO、硫酸吲哚酚、硫酸对甲酚及苯基硫酸盐的变化无统计学显著性；血清磷显著增加。",
        "the study supports feasibility and trial-design learning for paired microbiome, toxin, renal, and owner-reported endpoints": "该研究支持了配对微生物组、毒素、肾脏及主人报告终点的可行性和试验设计经验。",
        "it does not demonstrate probiotic efficacy, uremic-toxin reduction, or controlled ckd improvement": "它未能证实益生菌疗效、尿毒素降低或对照下的慢性肾脏病（CKD）改善。",
        "microbiome changes and creatinine movement remain hypothesis-generating because there was no control group and only six completers": "由于缺乏对照组且仅有6只猫完成，微生物组的变化和肌酐的波动仍仅具有假设生成意义。",
        "single-arm six-completer probiotic-treat pilot that is useful for endpoint and failure-mode design, but insufficient for efficacy claims": "单臂、6例完成者的益生菌零食试点研究，有助于终点和失败模式设计，但不足以证实临床疗效。",

        # src-ckd-128
        "this study evaluated urinary levels of fgf23 (ufgf23) and soluble α-klotho (ukl) in cats across various stages of chronic kidney disease (ckd), including acute decompensated chronic kidney disease (ackd)": "本研究评估了不同阶段慢性肾脏病（CKD）猫（包括急性失代偿性慢性肾脏病 ACKD）的尿液 FGF23（uFGF23）和可溶性 α-Klotho（uKL）水平。",
        "the study cohort included 112 cats (13 healthy control cats, 71 cats with ckd, and 28 cats with ackd)": "研究队列包括112只猫（13只健康对照猫，71只 CKD 猫和28只 ACKD 猫）。",
        "the ufgf23-to-urine-creatinine ratio was significantly increased in cats with late-stage ckd and ackd compared to healthy controls and early-stage ckd cats": "与健康对照和早期 CKD 猫相比，晚期 CKD 和 ACKD 猫 of uFGF23 与尿肌酐比值显著升高。",
        "lower levels of ukl were identified as an independent prognostic factor for the progression of feline ckd": "较低的 uKL 水平被确定为猫 CKD 进展的独立预后因素。",
        "the urinary klotho/fgf23 ratio showed a progressive decline as the disease advanced": "随着疾病的进展，尿液 Klotho/FGF23 比值呈现进行性下降。",
        "ufgf23, ukl, and their ratio can serve as useful biomarkers for evaluating and predicting the progression of chronic kidney disease in cats": "尿液 FGF23（uFGF23）、可溶性 α-Klotho（uKL）及其比值可作为评估和预测猫慢性肾脏病进展的有益生物标志物。",
        "these biomarkers reflect renal mineral and bone disorder (ckd-mbd) pathophysiology in feline ckd": "这些生物标志物反映了猫慢性肾脏病中肾性骨矿物质代谢紊乱（CKD-MBD）的病理生理学。",
        "ukl holds promise as a negative prognostic marker, meaning lower urinary excretion of soluble klotho correlates with a higher risk of disease progression": "uKL 有望作为阴性预后标志物，即尿液中可溶性 Klotho 排泄量减少与更高的疾病进展风险相关。",
        "this study demonstrates that urinary fgf23 and soluble α-klotho levels, as well as their ratio, are altered across different stages of feline ckd (including ackd), and lower ukl is an independent prognostic factor for ckd progression": "该研究表明，尿液 FGF23 和可溶性 α-Klotho 水平及其比值在猫 CKD（包括 ACKD）的不同阶段发生改变，且较低的 uKL 是 CKD 进展的独立预后因素。",

        # src-hcm-169
        "the study investigated left ventricular (lv) longitudinal systolic function in cats with hypertrophic cardiomyopathy (hcm) compared to healthy control cats using tissue motion annular displacement (tmad)": "该研究使用组织运动环向位移（TMAD）调查了肥厚型心肌病（HCM）猫与健康对照猫的左心室纵向收缩功能。",
        "the prospective study included 21 cats with hcm and 26 healthy control cats": "该项前瞻性研究包括21只 HCM 猫和26只健康对照猫。",
        "both global tmad (in mm) and percentage (%) global tmad were significantly decreased in cats with hcm compared to the control group (p <0.001)": "与对照组相比，HCM 猫的全局 TMAD（毫米）和百分比全局 TMAD 均显著降低（P <0.001）。",
        "global tmad and % global tmad measurements were not influenced by breed, sex, age, or heart rate": "全局 TMAD 和百分比全局 TMAD 测量值不受品种、性别、年龄或心率的影响。",
        "tmad is a sensitive and feasible method for evaluating left ventricular longitudinal systolic function in cats with hcm": "组织运动环向位移（TMAD）是评估猫肥厚型心肌病（HCM）左心室纵向收缩功能的一种敏感且可行的方法。",
        "tmad can detect myocardial longitudinal systolic dysfunction in hcm cats even when conventional parameters like fractional shortening (lvfs) remain normal": "即使在传统参数（如左心室缩短分数 LVFS）保持正常时，TMAD 也能检测到 HCM 猫的心肌纵向收缩功能障碍。",
        "tmad provides an efficient speckle-tracking based surrogate for assessing subclinical systolic impairment in cats before overt global systolic failure develops": "TMAD 提供了一种高效的基于斑点追踪的替代方法，用于在猫出现明显的全局收缩衰竭之前评估亚临床收缩损伤。",
        "this study demonstrates that left ventricular longitudinal systolic function, measured via tissue motion annular displacement (tmad), is significantly decreased in cats with hcm compared to healthy controls, independent of breed, sex, age, or heart rate": "该研究表明，与健康对照组相比，HCM 猫通过组织运动环向位移（TMAD）测量的左心室纵向收缩功能显著降低，且不受品种、性别、年龄或心率的影响。",

        # src-fip-070
        "the study described the outcomes of 307 cats with feline infectious peritonitis (fip) treated with legally sourced veterinary compounded preparations of remdesivir and gs-441524 in the uk": "该研究描述了英国307只使用合法来源的兽用复配瑞德西韦和 GS-441524 制剂治疗的猫传染性腹膜炎（FIP）猫的治疗结局。",
        "at the end of the initial treatment period, 88.6% of the cats were alive": "在初始治疗期结束时，88.6% 的猫存活。",
        "the overall survival rate at the longest follow-up point (median 248 days) was 84.4%": "在最长随访点（中位数 248 天）的总体存活率为 84.4%。",
        "survival to 6 months was approximately 86% overall, and increased to 96% for cats surviving the first 48 hours of treatment": "总体 6 个月存活率约为 86%，对于度过治疗最初 48 小时关键期的猫，存活率升至 96%。",
        "the most common forms of fip were abdominal effusive (49.5%) and neurological fip (14.3%)": "最常见的 FIP 形式是腹部渗出型（49.5%）和神经型 FIP（14.3%）。",
        "three treatment protocols evaluated were remdesivir alone (33.9%), remdesivir followed by gs-441524 (55.7%), and gs-441524 alone (10.4%)": "评估的三种治疗方案为单独使用瑞德西韦（33.9%）、瑞德西韦后接续 GS-441524（55.7%）以及单独使用 GS-441524（10.4%）。",
        "regulated veterinary compounded preparations of remdesivir and gs-441524 are highly effective and well-tolerated for the treatment of fip": "受监管的兽用复配瑞德西韦和 GS-441524 制剂治疗 FIP 高度有效且耐受性良好。",
        "cats surviving the initial critical 48 hours of antiviral therapy have a highly favorable long-term prognosis (96% survival)": "在抗病毒治疗最初关键的 48 小时内存活下来的猫具有极佳的长期预后（存活率达 96%）。",
        "transitioning from injectable remdesivir to oral gs-441524 represents a safe and effective clinical protocol that minimizes injection-site reactions and owner distress while maintaining efficacy": "从注射用瑞德西韦过渡到口服 GS-441524 代表了一种安全且临床有效的方案，能在保持疗效的同时最大程度地减少注射部位反应和宠物主人的焦虑。",
        "this retrospective study of 307 cats with fip demonstrates high treatment efficacy (88.6% survival at initial treatment end and 96% 6-month survival for those surviving the first 48 hours) using legally compounded remdesivir and gs-441524": "这项针对 307 只 FIP 猫的回顾性研究表明，使用合法复配的瑞德西韦和 GS-441524 具有极高疗效（初始治疗结束时存活率达 88.6%，通过前 48 小时关键期的猫 6 个月存活率达 96%）。",

        # src-diabetes-035
        "the sensation study was a prospective, multicenter clinical field trial evaluating the safety and effectiveness of velagliflozin as a once-daily, liquid, oral stand-alone therapy in 252 client-owned diabetic cats": "SENSATION 研究是一项前瞻性、多中心临床现场试验，评估了维拉格列净作为每日一次液态口服独立疗法在 252 只宠物糖尿病猫中的安全性和有效性。",
        "at day 180, 81% of the cats remaining in the study achieved glycemic reference ranges (blood glucose and/or fructosamine)": "在第 180 天，留在研究中的 81% 的猫实现了血糖控制（血糖和/或果糖胺达到参考范围）。",
        "clinical signs of diabetes improved significantly, including polyuria (88.6%) and polydipsia (87.7%)": "糖尿病的临床症状显著改善，包括多尿（88.6%）和多饮（87.7%）。",
        "improvement was also observed in cats with diabetic neuropathy-associated plantigrade stance": "在伴有糖尿病神经病变相关跗关节下地（跖行姿势）的猫中也观察到了改善。",
        "ketonuria occurred in 13.9% of cats, and diabetic ketoacidosis (dka) was reported in 7.1%": "13.9% 的猫出现了酮尿症，有报道 7.1% 的猫发生了糖尿病酮症酸中毒（DKA）。",
        "the risk of dka was significantly higher in cats previously treated with insulin (18.4%) compared to insulin-naïve cats (5.1%)": "与未接受过胰岛素治疗的猫（5.1%）相比，既往接受过胰岛素治疗的猫发生 DKA 的风险显著升高（18.4%）。",
        "no episodes of clinical hypoglycemia were observed during the study": "研究期间未观察到临床低血糖发作。",
        "velagliflozin is highly effective as a once-daily oral stand-alone therapy for feline diabetes mellitus, providing rapid glycemic control and clinical sign resolution": "维拉格列净作为每日一次的口服独立疗法治疗猫糖尿病高度有效，能提供快速的血糖控制和临床症状改善。",
        "cats previously treated with insulin carry a significantly higher risk of developing diabetic ketoacidosis when starting or switching to sglt2 inhibitors": "既往接受过胰岛素治疗的猫在开始或转换使用 SGLT2 抑制剂时，发生糖尿病酮症酸中毒（DKA）的风险显著升高。",
        "the safety profile of sglt2 inhibitors requires strict monitoring for ketosis and dka, especially during the first 14 days of therapy": "SGLT2 抑制剂的安全性需要对酮症 and DKA 进行严格监测，特别是在治疗的最初 14 天内。",
        "velagliflozin provides an attractive, high-compliance alternative to twice-daily insulin injections for newly diagnosed, stable diabetic cats without ketonuria": "维拉格列净为新诊断、无酮尿症的稳定糖尿病猫提供了一种有吸引力、依从性高的替代方案，可替代每日两次的胰岛素注射。",
        "the sensation study shows that once-daily oral velagliflozin is highly effective for feline diabetes mellitus, achieving glycemic control in 81% of cats by day 180, but requires vigilance due to a 7.1% risk of dka (higher in insulin-experienced cats)": "SENSATION 研究表明，每日一次口服维拉格列净治疗猫糖尿病高度有效，在第 180 天时使 81% 的猫实现了血糖控制，但由于存在 7.1% 的 DKA 风险（在接受过胰岛素治疗的猫中更高）需要保持警惕。",

        # src-obesity-039
        "the study investigated the prevalence of overweight and obese cats visiting veterinary hospitals in maisons-alfort and toulouse, france, between 2020 and 2022": "该研究调查了 2020 至 2022 年间就诊于法国迈松阿尔福和图卢兹兽医医院的超重和肥胖猫的患病率。",
        "out of 274 cats studied, 47.5% were found to be overweight or obese": "在研究的 274 只猫中，发现有 47.5% 超重或肥胖。",
        "the remaining study population consisted of 43.4% cats with an ideal body condition and 9.1% underweight cats": "其余研究人群由 43.4% 具有理想体况的猫和 9.1% 体重不足的猫组成。",
        "factors positively associated with overweight status included age, being crossbred, being male, and owner underestimation of their cat's body condition": "与超重状态呈正相关的因素包括年龄、混血品种、公猫以及宠物主人对猫体况的低估。",
        "feline overweight and obesity represent a highly prevalent health concern in french veterinary hospital populations, affecting nearly half of all visiting cats": "猫超重和肥胖是法国兽医医院就诊猫群中高度普遍的健康问题，影响了近一半的就诊猫只。",
        "owner underestimation of body condition is a critical risk factor, indicating that owner education is key to preventing feline obesity": "宠物主人低估猫的体况是一个关键的风险因素，表明主人教育是预防猫肥胖的关键。",
        "during the covid-19 pandemic, lifestyle factors, close confinement with owners, and owner misperceptions of feline body condition likely exacerbated weight gain in domestic cats": "在 COVID-19 疫情期间，生活方式因素、与主人的密切接触以及主人对猫体况的误解，可能加剧了家猫的体重增加。",
        "this study conducted in french veterinary hospitals between 2020 and 2022 shows that 47.5% of cats are overweight or obese, with risk factors including age, crossbred status, male sex, and owner underestimation of body condition": "这项 2020 至 2022 年在法国兽医医院进行的研究显示，47.5% 的猫超重或肥胖，其风险因素包括年龄、混血品种、公猫以及主人对体况的低估。",
    }
    for needle, zh in exact_meaning_map.items():
        if needle in lowered:
            return zh

    phrase_replacements = {
        r"\b[Tt]he abstract states that\b": "摘要指出",
        r"\b[Tt]his abstract states that\b": "该摘要指出",
        r"\b[Tt]he paper reports that\b": "论文报告",
        r"\b[Tt]his paper reports that\b": "该论文报告",
        r"\b[Tt]he study reports that\b": "研究报告",
        r"\b[Tt]his study reports that\b": "该研究报告",
        r"\b[Tt]he study shows that\b": "研究显示",
        r"\b[Tt]his study shows that\b": "该研究显示",
        r"\b[Tt]he abstract frames the study as\b": "摘要将该研究定位为",
        r"\b[Ff]rontier biomarker work already exists\b": "前沿生物标志物研究已经存在",
        r"\band should be kept separate from\b": "，应与……区分开",
        r"\bis primarily related to\b": "主要与……相关",
        r"\bis present in approximately\b": "约见于",
        r"\bsubstantially increases the risk of\b": "会显著增加……风险",
        r"\bmaking sarcomere-directed intervention an explicit translational branch\b": "因此肌节靶向干预应作为明确的转化研究分支",
        r"\bwith several limitations when used for\b": "在用于……时存在多项局限",
    }

    translated = text
    for pattern, replacement in phrase_replacements.items():
        translated = re.sub(pattern, replacement, translated)

    replacements = {
        "feline chronic kidney disease": "猫慢性肾脏病",
        "chronic kidney disease": "慢性肾脏病",
        "hypertrophic cardiomyopathy": "肥厚型心肌病",
        "feline infectious peritonitis": "猫传染性腹膜炎",
        "inflammatory bowel disease": "炎症性肠病",
        "diabetes mellitus": "糖尿病",
        "domestic cats": "家猫",
        "feline": "猫",
        "cats": "猫",
        "cat": "猫",
        "clinical relevance": "临床相关性",
        "clinical outcome": "临床结局",
        "clinical outcomes": "临床结局",
        "diagnostic": "诊断",
        "diagnosis": "诊断",
        "biomarker": "生物标志物",
        "biomarkers": "生物标志物",
        "treatment": "治疗",
        "therapy": "治疗",
        "therapeutic": "治疗",
        "intervention": "干预",
        "outcome": "结局",
        "outcomes": "结局",
        "survival": "生存",
        "prognosis": "预后",
        "prognostic": "预后",
        "risk factor": "风险因素",
        "risk factors": "风险因素",
        "sample size": "样本量",
        "study": "研究",
        "studies": "研究",
        "evidence": "证据",
        "method": "方法",
        "methods": "方法",
        "model": "模型",
        "models": "模型",
        "cohort": "队列",
        "review": "综述",
        "guideline": "指南",
        "original study": "原始研究",
        "case series": "病例系列",
        "case report": "病例报告",
        "association": "关联",
        "associated with": "与……相关",
        "suggests": "提示",
        "suggest": "提示",
        "supports": "支持",
        "support": "支持",
        "shows": "显示",
        "showed": "显示",
        "indicates": "表明",
        "indicated": "表明",
        "may": "可能",
        "should": "应",
        "requires": "需要",
        "require": "需要",
        "measurement": "测量",
        "measurements": "测量",
        "echocardiography": "超声心动图",
        "ultrasound": "超声",
        "histopathology": "组织病理学",
        "pathophysiology": "病理生理",
        "proteinuria": "蛋白尿",
        "creatinine": "肌酐",
        "phosphorus": "磷",
        "blood pressure": "血压",
        "owner": "主人",
        "caregiver": "照护者",
        "burden": "负担",
        "quality of life": "生活质量",
    }

    for source, target in sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True):
        translated = re.sub(rf"\b{re.escape(source)}\b", target, translated, flags=re.IGNORECASE)

    translated = translated.replace(" ,", "，").replace(", ", "，")
    translated = translated.replace("; ", "；").replace(": ", "：")
    translated = translated.replace(". ", "。")
    if translated and translated[-1] == ".":
        translated = translated[:-1] + "。"
    return translated


def _clean_label(value: Optional[str]) -> str:
    return (value or "").replace("_", "-").strip().lower()


def _evidence_level_label(level: Optional[str]) -> str:
    labels = {
        "meta-analysis": "荟萃分析",
        "systematic-review": "系统综述",
        "rct": "随机对照研究",
        "guideline": "指南/共识",
        "review": "综述",
        "original-study": "原始研究",
        "case-series": "病例系列",
        "case-report": "病例报告",
        "expert-opinion": "专家意见",
    }
    return labels.get(_clean_label(level), level or "证据类型未标注")


def _source_kind_label(kind: Optional[str]) -> str:
    labels = {
        "paper": "论文",
        "review-article": "综述论文",
        "guideline": "指南",
        "regulatory": "监管/标签文件",
        "product-info": "产品资料",
        "internal-doc": "内部资料",
    }
    return labels.get(_clean_label(kind), kind or "来源类型未标注")


def _theme_labels(card: SourceCard) -> list[str]:
    values = {item.lower() for item in (card.tags + card.endpoints) if item}
    themes: list[str] = []
    theme_rules = [
        ({"diagnostic", "diagnosis", "screening", "detection", "biomarker", "marker", "imaging", "assessment"}, "诊断/筛查"),
        ({"treatment", "therapy", "intervention", "efficacy", "drug", "pharmacology"}, "治疗/干预"),
        ({"outcome", "survival", "prognosis", "prognostic", "risk"}, "预后/风险分层"),
        ({"genetic", "genetics", "genotype", "mutation", "wgs", "rna-seq", "multiomics", "omics"}, "遗传/组学"),
        ({"mechanism", "pathophysiology", "fibrosis", "inflammation", "metabolism", "metabolomics"}, "机制/病理生理"),
        ({"nutrition", "diet", "microbiome", "uremic", "toxin"}, "营养/代谢/微生物组"),
    ]
    for needles, label in theme_rules:
        if values & needles:
            themes.append(label)
    return themes[:3]


def _evidence_depth_label(card: SourceCard) -> str:
    if card.quoted_facts and card.supported_conclusions:
        return "已提取关键事实和综合结论"
    if card.supported_conclusions:
        return "已提取综合结论"
    if card.one_line_summary:
        return "已有一句话摘要"
    return "主要依据题录和基础元数据"


def _chinese_clinical_relevance(card: SourceCard) -> str:
    themes = _theme_labels(card)
    theme_text = "、".join(themes) if themes else "该疾病研究"
    evidence = _evidence_level_label(card.evidence_level)

    if "诊断/筛查" in themes:
        return f"临床上主要用于理解{theme_text}方向，但仍需结合样本量、验证队列和真实病例场景判断可用性。"
    if "治疗/干预" in themes:
        return f"临床上主要用于评估{theme_text}线索；若不是随机对照或长期随访研究，不能直接外推为常规疗效结论。"
    if "预后/风险分层" in themes:
        return f"临床上可作为{theme_text}的证据线索，但观察性关联不能自动解释为因果关系。"
    if "遗传/组学" in themes or "机制/病理生理" in themes:
        return f"这类研究更适合解释疾病机制和分型，不应直接替代临床诊断或治疗决策。"
    if evidence in {"综述", "指南/共识"}:
        return "适合用来建立研究地图和证据边界，但具体临床决策仍需回到原始研究和病例条件。"
    return "适合放入优先阅读清单，用于判断该方向是否值得继续做全文提取和证据审计。"


def _first_non_placeholder(values: list[str]) -> Optional[str]:
    for value in values:
        if value and not _is_placeholder_content(value):
            return value.strip()
    return None


def _sample_size_signal(card: SourceCard) -> Optional[str]:
    """Extract a compact sample-size/method signal from source facts when present."""
    candidates = [card.one_line_summary or "", *(card.quoted_facts or []), *(card.supported_conclusions or [])]
    joined = " ".join(value for value in candidates if value)
    patterns = [
        r"\b\d+\s+cats?\b",
        r"\b\d+\s+healthy cats?\b",
        r"\b\d+\s+completed\b",
        r"\b\d+\s+completers?\b",
        r"\b\d+\s+cases?\b",
    ]
    hits: list[str] = []
    for pattern in patterns:
        for match in re.finditer(pattern, joined, flags=re.IGNORECASE):
            context_before = joined[max(0, match.start() - 12):match.start()].lower()
            if re.search(r"stage\s+$", context_before):
                continue
            cleaned = match.group(0).strip()
            if cleaned.lower() not in {hit.lower() for hit in hits}:
                hits.append(cleaned)
            if len(hits) >= 3:
                break
        if len(hits) >= 3:
            break
    if not hits:
        return None
    localized_hits = []
    for hit in hits:
        localized = re.sub(r"\bcats?\b", "只猫", hit, flags=re.IGNORECASE)
        localized = re.sub(r"\bhealthy 只猫\b", "只健康猫", localized, flags=re.IGNORECASE)
        localized = re.sub(r"\bcompleted\b", "例完成", localized, flags=re.IGNORECASE)
        localized = re.sub(r"\bcompleters?\b", "例完成者", localized, flags=re.IGNORECASE)
        localized = re.sub(r"\bcases?\b", "例病例", localized, flags=re.IGNORECASE)
        localized_hits.append(localized)
    return "；".join(localized_hits)


def _chinese_reading_hook(card: SourceCard) -> str:
    """
    Explain why a researcher should open the paper first.

    Priority order (field-first approach):
    1. title_gap → directly use as the hook (it's already a complete statement)
    2. unexpected_finding → legacy field, also use directly
    3. core_argument + implicit_premise → show argument with its hidden assumption
    4. tension_with → highlight the conflict with other sources
    5. Fall back to existing heuristics and theme-based hooks
    """
    # Priority 1: title_gap - the most compelling (already a complete sentence)
    # title_gap explains why this paper is worth reading beyond the title
    if card.title_gap:
        return card.title_gap

    # Priority 2: unexpected_finding (legacy, backward compatible)
    # If present, use it directly without mechanical prefix
    if card.unexpected_finding:
        return card.unexpected_finding

    # Priority 3: core_argument + implicit_premise
    if card.core_argument and card.implicit_premise:
        return f"{card.core_argument}——但隐含前提是{card.implicit_premise}"
    if card.core_argument:
        return card.core_argument

    # Priority 4: tension_with - show intellectual conflict
    if card.tension_with:
        tension = card.tension_with[0]
        return f"与现有研究存在张力：{tension.description}"

    # Fallback: existing heuristics for deep_extracted cards
    if card.verification_status == "deep_extracted":
        conclusion = _first_non_placeholder(card.supported_conclusions or [])
        if conclusion:
            translated = _acceptable_chinese_snippet(conclusion)
            if translated:
                return translated
        if card.one_line_summary:
            translated = _acceptable_chinese_snippet(card.one_line_summary)
            if translated:
                return translated

    # Fallback: keyword-based heuristics
    text = " ".join(
        value for value in [
            card.one_line_summary or "",
            *(card.supported_conclusions or []),
            *(card.quoted_facts or []),
            card.title,
        ]
        if value
    )
    lower = text.lower()

    if any(term in lower for term in ["single-arm", "pilot", "completer", "dropout", "dropped out"]):
        return "值得读的是它暴露了干预研究的真实难点：入组、脱落、端点选择和主人报告都可能决定试验是否站得住，而不是只看标题里的「有效性」。"
    if any(term in lower for term in ["proteinuria", "upc"]):
        return "值得读的是它把早期风险分层前移到看似边界的临床信号，适合判断哪些猫需要更密集随访。"
    if any(term in lower for term in ["machine-learning", "machine learning", "3-hydroxykynurenine", "biomarker", "metabolite model"]):
        return "值得读的是它把早期识别从单一指标推进到代谢组学和模型判别，并明确提示这种进展距离常规筛查仍有验证距离。"
    if any(term in lower for term in ["metabolomics", "tryptophan", "uremic toxin", "uremic-toxin", "gut-derived"]):
        return "值得读的是它把 CKD 从肌酐/尿比重问题扩展到代谢网络，尤其是肠源性尿毒素、色氨酸代谢和多通路异常。"
    if any(term in lower for term in ["progenitor", "regenerative", "cell-based", "cell lineage"]):
        return "值得读的是它代表再生医学方向的早期技术储备；重点是细胞系建立与表征，而不是已经可临床使用的治疗方案。"
    if any(term in lower for term in ["risk factor", "risk factors", "predict"]):
        return "值得读的是它把早期风险分层前移到看似边界的临床信号，适合判断哪些猫需要更密集随访。"
    if any(term in lower for term in ["no single", "wgs", "rna-seq", "multiomics", "variant"]):
        return "值得读的是它保留了阴性或复杂结果：疾病可能不是一个常见变异就能解释，组学信号更适合用来重画机制地图。"
    if any(term in lower for term in ["myosin", "inhibitor", "treatment", "therapy", "efficacy"]):
        return "值得读的是它提供治疗方向线索，但需要先分清模型、端点和随访时长，不能直接当成常规疗效结论。"

    conclusion = _first_non_placeholder(card.supported_conclusions or [])
    if conclusion:
        translated = _acceptable_chinese_snippet(conclusion)
        if translated:
            return translated

    themes = _theme_labels(card)
    if themes:
        return f"值得读的是它代表{ '、'.join(themes) }这条证据分支，可帮助判断后续报告应把注意力放在哪类问题上。"
    return "值得读的是它在当前本地排序中靠前，适合先打开核对摘要、方法、结果和局限，再决定是否进入深度提取。"


def _chinese_key_finding(card: SourceCard) -> str:
    """
    Return structured key findings for a paper card.

    For cards with new enhanced fields, returns multi-part structure:
    - 核心论点
    - 关键证据
    - 证据边界
    - 意外发现（如有）

    Falls back to existing behavior for cards without new fields.
    """
    # Check if we have the new enhanced fields
    has_enhanced_fields = card.core_argument or card.evidence_boundary or card.title_gap or card.unexpected_finding

    if has_enhanced_fields:
        parts = []

        # Core argument (required if present)
        if card.core_argument:
            parts.append(f"**核心论点：** {card.core_argument}")

        # Study design (optional, but valuable for quick assessment)
        if card.study_design:
            parts.append(f"**研究设计：** {card.study_design}")

        # Key evidence from quoted_facts or supported_conclusions
        fact = _first_non_placeholder(card.quoted_facts or [])
        conclusion = _first_non_placeholder(card.supported_conclusions or [])
        key_evidence = None
        if fact:
            key_evidence = _acceptable_chinese_snippet(fact)
        if not key_evidence and conclusion:
            key_evidence = _acceptable_chinese_snippet(conclusion)
        if key_evidence:
            parts.append(f"**关键证据：** {key_evidence}")

        # Evidence boundary (required if present)
        if card.evidence_boundary:
            parts.append(f"**证据边界：** {card.evidence_boundary}")

        # Title gap or unexpected finding (the hook that creates curiosity)
        if card.title_gap:
            parts.append(f"**标题之外：** {card.title_gap}")
        elif card.unexpected_finding:
            parts.append(f"**意外发现：** {card.unexpected_finding}")

        if parts:
            return "\n\n".join(parts)

    # Fallback: existing behavior for cards without new fields
    conclusion = _first_non_placeholder(card.supported_conclusions or [])
    summary = card.one_line_summary if card.one_line_summary and not _is_placeholder_content(card.one_line_summary) else None
    fact = _first_non_placeholder(card.quoted_facts or [])

    if card.verification_status == "deep_extracted":
        if summary:
            translated = _acceptable_chinese_snippet(summary)
            if translated:
                return translated
        if conclusion:
            translated = _acceptable_chinese_snippet(conclusion)
            if translated:
                return translated
        if fact:
            translated = _acceptable_chinese_snippet(fact)
            if translated:
                return translated

    if conclusion:
        translated = _acceptable_chinese_snippet(conclusion)
        if translated:
            return translated

    lower = " ".join(value for value in [summary or "", conclusion or "", fact or ""] if value).lower()
    if "insufficient for efficacy" in lower or "does not demonstrate" in lower:
        return "关键结论是：它更支持试验设计和端点探索，不足以证明干预疗效或 CKD 改善。"
    if "six months" in lower or "3-hydroxykynurenine" in lower:
        return "关键结论是：3-hydroxykynurenine 和多代谢物模型可能早于传统 CKD2 诊断识别风险，但还不是成熟筛查方案。"
    if "proteinuria" in lower or "upc" in lower:
        return "关键结论是：边界性蛋白尿可能是非氮质血症猫后续 CKD 风险分层的早期信号，但仍需结合随访设计和其他风险因素判断。"
    if "94 cats with ckd" in lower or "183 ckd-associated compounds" in lower:
        return "关键结论是：CKD 猫的血清/尿液代谢谱存在多通路改变，属于发现级关联，不能直接推出治疗建议。"
    if "progenitor" in lower or "regenerative" in lower:
        return "关键结论是：研究建立并表征了潜在肾脏祖细胞工具，为未来细胞治疗研究铺路，但临床转化仍早。"

    if summary:
        translated = _acceptable_chinese_snippet(summary)
        if translated:
            return translated

    if fact:
        sample = _sample_size_signal(card)
        if sample:
            return f"已提取到方法/样本线索：{sample}；需要继续核对摘要或全文来确定端点和局限。"
    return "目前已有排序和基础元数据，但仍需要更完整的方法、结果和局限提取。"


def _chinese_evidence_boundary(card: SourceCard) -> str:
    sample = _sample_size_signal(card)
    depth = _evidence_depth_label(card)
    parts = [depth]
    if sample:
        parts.append(f"样本/设计线索：{sample}")
    if card.verification_status in {"title_only", "metadata_unavailable"}:
        parts.append("不可作为读者推荐证据，应进入深度提取队列")
    elif card.verification_status == "abstract_weighted":
        parts.append("主要依据摘要层信息，不能替代全文审计")
    elif card.verification_status == "deep_extracted":
        parts.append("可作为优先阅读入口，但仍需按原文核对统计方法和局限")
    return "；".join(parts) + "。"


def _source_link(card: SourceCard) -> Optional[str]:
    """Return the best user-facing source locator for a paper."""
    if card.doi:
        return f"https://doi.org/{card.doi}"
    if card.pmid:
        return f"https://pubmed.ncbi.nlm.nih.gov/{card.pmid}/"
    if card.pmcid:
        return f"https://pmc.ncbi.nlm.nih.gov/articles/{card.pmcid}/"
    if card.url and card.url.startswith(("http://", "https://")):
        return card.url
    return None


def _acceptable_chinese_snippet(text: str) -> Optional[str]:
    if not text or _is_placeholder_content(text):
        return None
    translated = _to_chinese_research_text(text)
    if not translated:
        return None
    ascii_letters = len(re.findall(r"[A-Za-z]", translated))
    cjk_chars = len(re.findall(r"[\u3400-\u9fff]", translated))
    # Avoid the failure mode shown in QA screenshots: Chinese labels with an
    # English sentence body. Keep the report natural instead of pretending.
    if cjk_chars == 0 or ascii_letters > cjk_chars * 0.75:
        return None
    bad_fragments = (" in the ", " and ", " with ", " for ", " that ", "……")
    if any(fragment in translated for fragment in bad_fragments):
        return None
    return translated


def _format_chinese_paper_entry(card: SourceCard, index: int) -> str:
    """Format a paper as a professional Chinese research-summary entry."""
    lines: list[str] = []
    year = f"（{card.year}）" if card.year else ""
    journal = f"｜{card.journal}" if card.journal else ""
    author = ""
    if card.authors:
        author = f"{card.authors[0]} 等｜" if len(card.authors) > 1 else f"{card.authors[0]}｜"

    evidence = _evidence_level_label(card.evidence_level)
    kind = _source_kind_label(card.source_kind)
    themes = _theme_labels(card)
    theme_text = "、".join(themes) if themes else "该疾病研究"

    # Avoid duplicate labels when evidence_level and source_kind overlap
    # e.g., both "guideline" would show "指南/共识｜指南" - skip kind in this case
    if "指南" in evidence and kind == "指南":
        kind = ""

    if card.has_deep_extraction:
        lines.append(f"### 📖 {index}. {card.title}")
    else:
        lines.append(f"### {index}. {card.title}")
    lines.append("")
    meta_bits = [bit for bit in [author.rstrip("｜"), str(card.year or ""), card.journal or "", evidence, kind, theme_text] if bit]
    if meta_bits:
        lines.append(f"**文献信息：** {'｜'.join(meta_bits)}")
        lines.append("")
    link = _source_link(card)
    if link:
        lines.append(f"**链接：** {link}")
        lines.append("")

    # Use deep extraction content when available, otherwise fall back to heuristics
    if card.has_deep_extraction and card.deep_extraction_why:
        lines.append(f"**为什么值得读：** {card.deep_extraction_why}")
    else:
        lines.append(f"**为什么值得读：** {_chinese_reading_hook(card)}")
    lines.append("")

    # Handle key findings: prefer deep extraction takeaway
    if card.has_deep_extraction and card.deep_extraction_takeaway:
        lines.append(f"**关键发现：** {card.deep_extraction_takeaway}")
    else:
        key_finding = _chinese_key_finding(card)
        if "\n" in key_finding:
            # Multi-part structured finding - use section header then content
            lines.append("**关键发现：**")
            lines.append("")
            lines.append(key_finding)
        else:
            # Single-line finding - inline format
            lines.append(f"**关键发现：** {key_finding}")
    lines.append("")

    # For cards with explicit evidence_boundary field, don't duplicate
    # The _chinese_key_finding already includes it for enhanced cards
    has_enhanced_fields = card.core_argument or card.evidence_boundary or card.title_gap or card.unexpected_finding
    if not has_enhanced_fields and not card.has_deep_extraction:
        lines.append(f"**证据边界：** {_chinese_evidence_boundary(card)}")
        lines.append("")

    lines.append(f"**临床相关性：** {_chinese_clinical_relevance(card)}")

    # Add evidence nodes if present
    if card.has_deep_extraction and card.evidence_nodes:
        lines.append("")
        lines.append(f"**证据节点：** {', '.join(card.evidence_nodes)}")

    # Add link to detail page if deep extraction exists
    if card.has_deep_extraction:
        lines.append("")
        lines.append(f"📖 [查看深度提炼详情](?detail={card.id})")

    return "\n".join(lines)


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
    if chinese:
        return _format_chinese_paper_entry(card, index)

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

    journal_str = f" {card.journal}." if card.journal else ""
    year_str = f" {card.year}." if card.year else ""

    # Main citation line
    if card.has_deep_extraction:
        lines.append(f"📖 {index}. {author_str}*{card.title}.*{journal_str}{year_str}")
    else:
        lines.append(f"{index}. {author_str}*{card.title}.*{journal_str}{year_str}")

    # Line 2: URL (DOI preferred, then PMID, then PMCID, then source URL)
    link = _source_link(card)
    if link:
        lines.append(f"   URL: {link}")

    # Line 3: Why it matters - prefer deep extraction, then fall back to heuristics
    why_shown = False
    if card.has_deep_extraction and card.deep_extraction_why:
        lines.append(f"   **Why it matters:** {card.deep_extraction_why}")
        why_shown = True
    elif card.supported_conclusions:
        for conclusion in card.supported_conclusions:
            if not _is_placeholder_content(conclusion):
                why_label = "**要点：**" if chinese else "**Why it matters:**"
                why_text = _to_chinese_research_text(conclusion) if chinese else conclusion
                lines.append(f"   {why_label} {why_text}")
                why_shown = True
                break

    # Line 4: Takeaway - prefer deep extraction, then fall back to heuristics
    takeaway = None
    if card.has_deep_extraction and card.deep_extraction_takeaway:
        takeaway = card.deep_extraction_takeaway
    elif card.one_line_summary and not _is_placeholder_content(card.one_line_summary):
        takeaway = card.one_line_summary
    elif card.quoted_facts:
        # Find first non-placeholder quoted fact
        for fact in card.quoted_facts:
            if not _is_placeholder_content(fact):
                takeaway = fact
                break

    if takeaway:
        takeaway_label = "**总结：**" if chinese else "**Takeaway:**"
        # Truncate if too long
        takeaway_text = _to_chinese_research_text(takeaway) if chinese else takeaway
        takeaway_text = takeaway_text[:250] + '...' if len(takeaway_text) > 250 else takeaway_text
        lines.append(f"   {takeaway_label} {takeaway_text}")

    # Add evidence nodes if present
    if card.has_deep_extraction and card.evidence_nodes:
        lines.append(f"   **Evidence nodes:** {', '.join(card.evidence_nodes)}")

    # Add link to detail page if deep extraction exists
    if card.has_deep_extraction:
        lines.append(f"   📖 [View deep extraction](?detail={card.id})")

    return "\n".join(lines)


def _build_english_output(
    disease: str,
    top_papers: list[SourceCard],
    top_clinical: list[SourceCard],
    top_diagnostic: list[SourceCard],
    limitations: list[str],
    depth_queue: Optional[list[SourceCard]] = None,
) -> str:
    """Build English structured output."""
    sections = []

    disease_upper = disease.upper()

    sections.append(f"# Research Literature: Feline {disease_upper}\n")
    sections.append(f"Showing the top {len(top_papers)} ranked local-vault sources for this disease.\n")

    # Best recent papers
    if top_papers:
        sections.append("## Best recent papers to read first\n")
        sections.append("### Higher-visibility / broader journals\n")
        sections.append("*Ranked by evidence level, recency, source kind, and extraction depth.*\n")
        for i, card in enumerate(top_papers[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=False))
            sections.append("")

    # Clinical/therapeutic papers
    if top_clinical:
        sections.append("## Clinical & therapeutic research\n")
        sections.append("### Treatment outcomes and interventions\n")
        for i, card in enumerate(top_clinical[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=False))
            sections.append("")

    # Diagnostic papers
    if top_diagnostic:
        sections.append("## Diagnostic research\n")
        sections.append("### Biomarkers and detection methods\n")
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

    if depth_queue:
        sections.append("## Evidence depth queue\n")
        sections.append(
            "*These papers are not used as main recommendations yet because they need abstract/full-text extraction before reader-facing synthesis.*\n"
        )
        for i, card in enumerate(depth_queue[:5], 1):
            year = f" ({card.year})" if card.year else ""
            status = card.verification_status or card.status or "needs extraction"
            title_short = card.title[:110] + "..." if len(card.title) > 110 else card.title
            sections.append(f"{i}. *{title_short}*{year} — status: {status}")
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
    depth_queue: Optional[list[SourceCard]] = None,
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
    sections.append(f"展示该疾病在本地知识库中排序最高的 {len(top_papers)} 篇来源。\n")

    # Best recent papers
    if top_papers:
        sections.append("## 推荐优先阅读的文献\n")
        sections.append("### 高影响力期刊 / Higher-visibility journals\n")
        sections.append("*按证据等级、近期性、来源类型和提取深度排序。*\n")
        for i, card in enumerate(top_papers[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=True))
            sections.append("")

    # Clinical/therapeutic papers
    if top_clinical:
        sections.append("## 临床与治疗研究\n")
        sections.append("### 治疗结果和干预措施\n")
        for i, card in enumerate(top_clinical[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=True))
            sections.append("")

    # Diagnostic papers
    if top_diagnostic:
        sections.append("## 诊断研究\n")
        sections.append("### 生物标志物与检测方法\n")
        for i, card in enumerate(top_diagnostic[:5], 1):
            sections.append(_format_paper_entry(card, i, chinese=True))
            sections.append("")

    # What papers collectively say
    sections.append("## 这些文献共同表明\n")
    if top_papers:
        years = [card.year for card in top_papers if card.year]
        recent_count = sum(1 for year in years if year >= 2024)
        theme_counts: dict[str, int] = {}
        for card in top_papers:
            for theme in _theme_labels(card):
                theme_counts[theme] = theme_counts.get(theme, 0) + 1
        top_themes = sorted(theme_counts.items(), key=lambda item: (-item[1], item[0]))[:3]
        if recent_count:
            sections.append(f"- 排序靠前的文献中有 {recent_count} 篇来自 2024 年及以后，说明该方向仍在持续更新。")
        if top_themes:
            theme_text = "、".join(label for label, _ in top_themes)
            sections.append(f"- 当前证据主要集中在 {theme_text}，不应只按期刊影响力单线排序。")
        sections.append("- “高影响力”在小众猫科疾病领域需要降级理解为 higher-visibility 与临床相关性组合，而不是严格 JCR 排名。")
        sections.append("- 外部 PubMed 条目用于最新性补充；未入库前仍应视为待审计线索，而不是已完成证据。")
        sections.append("")

    # Shortest must-read list
    sections.append("## 最短必读清单\n")
    if top_papers:
        sections.append(f"如果只能读 {min(3, len(top_papers))} 篇：\n")
        for i, card in enumerate(top_papers[:3], 1):
            year_str = f" ({card.year})" if card.year else ""
            # Use title (truncated if needed), not internal ID
            title_short = card.title[:80] + "..." if len(card.title) > 80 else card.title
            themes = _theme_labels(card)
            reason = "、".join(themes) if themes else _evidence_level_label(card.evidence_level)
            sections.append(f"{i}. *{title_short}*{year_str} — 优先用于理解{reason}。")
        sections.append("")

    # Important limitations
    sections.append("## 重要局限\n")
    sections.append("- 这些是本地知识库排序最高的一组文献，不等于该领域全部最新论文。")
    sections.append("- 题录型、占位型或尚未提取摘要/全文的记录已从上方推荐清单中剔除，改列入下方“深度提取队列”。")
    sections.append("- 观察性研究、病例系列和机制研究不能自动推出因果、疗效或临床指南级结论。")
    sections.append("- 若用户要求“latest”，必须把 PubMed/期刊官网的新文献补充结果单独审计后再写入最终报告。")
    sections.append("")

    if depth_queue:
        sections.append("## 深度提取队列\n")
        sections.append("*以下文献看起来可能重要，但目前不能作为读者可用证据；需要先补摘要、方法、结果和局限提取。*\n")
        for i, card in enumerate(depth_queue[:5], 1):
            year = f" ({card.year})" if card.year else ""
            status = card.verification_status or card.status or "待提取"
            title_short = card.title[:90] + "..." if len(card.title) > 90 else card.title
            sections.append(f"{i}. *{title_short}*{year} — 当前状态：{status}")
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
        # FIP: Use full term to avoid false positives; "FIP" alone matches unrelated acronyms
        "fip": '"feline infectious peritonitis"[Title/Abstract]',
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
) -> tuple[str, list["ExternalSearchResult"], Optional["ExternalSearchResponse"]]:
    """
    Fetch PubMed results as augmentation layer.

    Returns:
        (formatted_section, results_list)
    """
    if not EXTERNAL_SEARCH_AVAILABLE:
        note = "PubMed 增强不可用（缺少 external_search 模块）" if chinese else "PubMed augmentation unavailable (external_search module not found)"
        return f"\n*{note}*\n", [], None

    query = _build_pubmed_query(disease)
    config = ExternalSearchConfig(
        allow_external=True,
        max_results=max_results,
        timeout_seconds=15,
    )

    response = search_pubmed(query, config)

    if response.error:
        error_label = "错误" if chinese else "Error"
        return f"\n*PubMed {error_label}: {response.error}*\n", [], response

    if not response.results:
        no_results = "PubMed 未返回结果" if chinese else "PubMed returned no results"
        return f"\n*{no_results}*\n", [], response

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

    return "\n".join(lines), response.results, response


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

    # Build local vault output. Source IDs should follow the same ranking used
    # by the report, otherwise the UI source cards can disagree with the prose.
    output = build_research_mode_output(disease, cards, chinese=chinese, bilingual=True)
    ranked_cards = rank_research_ready_sources(cards, top_n=10)
    source_ids = [card.id for card in ranked_cards]

    pubmed_query = None
    pubmed_total = None
    pubmed_shown = 0

    # Add PubMed augmentation if enabled
    if include_external and EXTERNAL_SEARCH_AVAILABLE:
        pubmed_section, external_results, pubmed_response = fetch_pubmed_augmentation(
            disease,
            max_results=5,
            chinese=chinese,
        )
        if pubmed_response:
            pubmed_query = pubmed_response.query
            pubmed_total = pubmed_response.total_found
        pubmed_shown = len(external_results)
        if external_results:
            # Insert before the final "---" separator
            output_parts = output.rsplit("---", 1)
            if len(output_parts) == 2:
                output = output_parts[0] + pubmed_section + "---" + output_parts[1]
            else:
                output += pubmed_section

    contract = _build_research_contract_section(
        query=query,
        disease=disease,
        local_count=len(cards),
        pubmed_query=pubmed_query,
        pubmed_total=pubmed_total,
        pubmed_shown=pubmed_shown,
        include_external=include_external,
        chinese=chinese,
    )
    output = contract + output

    return output, source_ids


def handle_research_query_local_only(query: str, chinese: bool = False) -> tuple[str, list[str]]:
    """
    Research query without external API calls.
    Use this for local-only mode or when external search is not desired.
    """
    return handle_research_query(query, chinese=chinese, include_external=False)


def handle_research_query_structured(
    query: str,
    chinese: bool = False,
    include_external: bool = True,
) -> dict:
    """
    Research query returning structured output for Workspace Tabs.

    Returns:
        Dict with structured data for WorkspaceOutput conversion.
    """
    disease = extract_disease_from_query(query)

    if not disease:
        return {
            "error": True,
            "message": "未能识别具体疾病类型" if chinese else "Could not identify disease",
            "query": query,
        }

    cards = load_disease_sources(disease)

    if not cards:
        return {
            "error": True,
            "message": f"未找到 {disease.upper()} 相关文献" if chinese else f"No {disease.upper()} sources found",
            "query": query,
            "disease": disease,
        }

    # Rank cards
    ranked_cards = rank_research_ready_sources(cards, top_n=10)

    # Build structured output
    result = {
        "error": False,
        "query": query,
        "disease": disease,
        "query_interpretation": f"Searching for {disease.upper()} literature" if not chinese else f"搜索 {disease.upper()} 相关文献",
        "time_window": "2020-2026",
        "search_scope": "Local vault + PubMed" if include_external else "Local vault only",
        "source_priorities": ["JVIM", "J Vet Cardiol", "Scientific Reports", "Frontiers", "PubMed indexed journals"],
        "filters": ["peer-reviewed", "feline-specific"],
        "total_considered": len(cards),
        "ranked_cards": [],
        "gaps": [],
        "next_steps": [],
    }

    # Convert cards to structured format
    for card in ranked_cards:
        card_dict = {
            "id": card.id,
            "title": card.title,
            "year": card.year,
            "journal": card.journal,
            "evidence_level": card.evidence_level,
            "why_included": f"Relevant to {disease.upper()} research; Evidence level: {card.evidence_level or 'not specified'}",
            "one_line_summary": card.one_line_summary or "",
            "limitations": card.evidence_boundary or "Not specified",
            "url": card.url,
            "doi": card.doi,
            "pmid": card.pmid,
            "has_deep_extraction": card.has_deep_extraction,
            "deep_extraction_why": card.deep_extraction_why,
            "deep_extraction_takeaway": card.deep_extraction_takeaway,
            "supported_conclusions": card.supported_conclusions or [],
            "study_design": card.study_design or "",
            "endpoints": card.endpoints or [],
            "core_argument": card.core_argument or "",
        }
        result["ranked_cards"].append(card_dict)

    # Extract gaps from evidence boundaries
    gaps = []
    for card in ranked_cards[:5]:
        if card.evidence_boundary:
            gaps.append(card.evidence_boundary)
    result["gaps"] = gaps[:3]  # Top 3 gaps

    # Suggest next steps
    result["next_steps"] = [
        f"Review deep extractions for top {disease.upper()} papers",
        f"Compare study designs and endpoints across {disease.upper()} literature",
        f"Check for recent PubMed publications not yet in vault",
    ]

    return result


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
