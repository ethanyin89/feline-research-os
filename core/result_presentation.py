"""
Result presentation helpers for Feline Research OS.

Implements the ResultPresentation contract defined in:
  .claude/skills/render-result-page.md

This module provides:
- Data models for user-facing result presentation
- Label translation from internal values to user-facing Chinese
- Builder functions for evidence profiles, source displays, and full presentations
- Validation and safe fallbacks for edge cases

IMPORTANT: This is a pure presentation layer. It does NOT:
- Execute paid APIs
- Modify source data
- Make retrieval decisions
"""

from dataclasses import dataclass, field
from enum import Enum
import html as html_lib
import re
from typing import List, Optional, Dict, Any, Literal


# =============================================================================
# LABEL MAPS: Internal values → User-facing labels
# =============================================================================

# Evidence depth labels (how deeply the source was verified)
EVIDENCE_DEPTH_LABELS: Dict[str, str] = {
    # Full verification
    "deep_extracted": "已核查全文",
    "audited": "已核查全文",
    "full_text": "已核查全文",
    # Source-level check
    "source_checked": "已核查来源",
    # Abstract only
    "abstract_weighted": "基于摘要",
    "abstract": "基于摘要",
    # Title only (discovery, not support)
    "title_only": "仅题录信息",
    # Missing or unrecognized metadata
    "unknown": "核查状态未知",
    "metadata_unavailable": "元数据不可用",
}

# Provenance type labels (how the claim relates to source)
PROVENANCE_LABELS: Dict[str, str] = {
    "quoted_fact": "直接来源",
    "source_supported_conclusion": "来源支持",
    "llm_inference": "分析推断",
}

# Authority state labels
AUTHORITY_STATE_LABELS: Dict[str, str] = {
    "automated": "自动生成，未经人工审核",
    "human_reviewed": "已经人工审核",
}

# Source type labels (for display)
SOURCE_TYPE_LABELS: Dict[str, str] = {
    "paper": "论文",
    "pubmed": "PubMed",
    "pmc": "PMC",
    "guideline": "指南",
    "review": "综述",
    "original-study": "原始研究",
    "thesis": "学位论文",
    "internal_note": "内部笔记",
    "protocol": "方案",
    "uploaded_file": "上传文件",
}


# =============================================================================
# ENUMS
# =============================================================================

class Audience(Enum):
    """Target audience for presentation."""
    ORDINARY = "ordinary"      # Cat owner, general user
    PROFESSIONAL = "professional"  # Veterinarian, researcher


class Language(Enum):
    """Display language."""
    ZH = "zh"  # Chinese (primary)
    EN = "en"  # English


class AuthorityState(Enum):
    """Whether content has been human-reviewed."""
    AUTOMATED = "automated"
    HUMAN_REVIEWED = "human_reviewed"


class ActionType(Enum):
    """Types of next actions available to users."""
    NAVIGATE = "navigate"       # Go to another page
    SEARCH = "search"          # Run a new search
    EXPAND = "expand"          # Expand collapsed content
    EXTERNAL = "external"      # Open external URL


# =============================================================================
# DATA MODELS
# =============================================================================

@dataclass
class SourceDisplay:
    """
    User-facing source card structure.

    NEVER includes internal IDs (src-xxx) in user-facing fields.
    """
    title: str                              # Paper title, never internal ID
    canonical_url: Optional[str] = None     # DOI or PubMed URL, None if unavailable
    publication_year: Optional[int] = None   # Year of publication
    publish_date: str = ""                  # Optional publication date string
    source_type_label: str = ""             # User-facing source type
    evidence_depth_label: str = ""          # User-facing depth tag
    source_family_label: str = ""           # User-facing source family label
    species_label: str = ""                 # Species/applicability boundary
    decision_grade_label: str = ""          # no / provisional / yes
    safest_use: str = ""                    # Deterministic claim-fit annotation
    must_not_control: str = ""              # Deterministic overclaim boundary
    journal: str = ""                       # Optional journal name
    pmcid: str = ""                         # Optional PMC identifier
    pmid: str = ""                          # Optional PubMed identifier
    doi: str = ""                          # Optional DOI
    authors: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)

    # Internal reference (not displayed to ordinary users)
    _internal_id: str = ""

    def has_valid_link(self) -> bool:
        """Check if source has a usable canonical URL."""
        return bool(self.canonical_url and self.canonical_url.startswith("http"))

    def get_link_text(self) -> str:
        """Get link display text, handling missing URLs."""
        if self.has_valid_link():
            if "doi.org" in self.canonical_url:
                return "DOI"
            elif "pubmed" in self.canonical_url.lower():
                return "PubMed"
            return "Link"
        return "链接不可用"


@dataclass
class InlineCitation:
    """Citation embedded in answer text."""
    text: str                   # Display text (shortened paper title)
    source_ref: str             # Reference to SourceDisplay
    provenance_type: str        # Internal provenance type
    provenance_label: str       # User-facing provenance label


@dataclass
class AnswerSection:
    """A section within the primary answer."""
    title: str
    content: str
    citations: List[InlineCitation] = field(default_factory=list)


@dataclass
class EvidenceProfile:
    """
    Factual representation of evidence backing a result.

    NOTE: This replaces removed global confidence badges (high/medium/low).
    Shows factual counts instead of subjective assessments.
    """
    authority_state: AuthorityState
    source_count: int               # unique source cards
    direct_support_count: int       # quoted_fact claims
    supported_synthesis_count: int  # source_supported_conclusion claims
    inference_count: int            # llm_inference claims
    limited_source_count: int       # title_only sources (discovery only)
    unknown_source_count: int       # missing or unrecognized verification state
    unresolved_gap_count: int       # Known evidence gaps

    # Depth breakdown
    deep_extracted_count: int = 0
    source_checked_count: int = 0
    abstract_weighted_count: int = 0

    def total_sources(self) -> int:
        """Return the number of unique source cards."""
        return self.source_count

    def is_sparse(self) -> bool:
        """Check if evidence is thin enough to warrant warning."""
        return self.total_sources() <= 1 or (
            self.inference_count > self.direct_support_count + self.supported_synthesis_count
        )

    def get_summary_text(self) -> str:
        """Generate user-facing summary text."""
        total = self.total_sources()
        parts = [f"基于 {total} 篇来源"]

        if self.deep_extracted_count > 0:
            parts.append(f"{self.deep_extracted_count} 篇已核查全文")
        if self.source_checked_count > 0:
            parts.append(f"{self.source_checked_count} 篇已核查来源")
        if self.abstract_weighted_count > 0:
            parts.append(f"{self.abstract_weighted_count} 篇基于摘要")
        if self.unknown_source_count > 0:
            parts.append(f"{self.unknown_source_count} 篇核查状态未知")

        return " | ".join(parts)

    def get_provenance_breakdown(self) -> List[Dict[str, Any]]:
        """Generate provenance breakdown for display."""
        breakdown = []

        if self.direct_support_count > 0:
            breakdown.append({
                "icon": "🟢",
                "label": "直接来源",
                "count": self.direct_support_count
            })

        if self.supported_synthesis_count > 0:
            breakdown.append({
                "icon": "🟡",
                "label": "来源支持",
                "count": self.supported_synthesis_count
            })

        if self.inference_count > 0:
            breakdown.append({
                "icon": "⚪",
                "label": "分析推断",
                "count": self.inference_count
            })

        return breakdown


@dataclass
class ResearchTraceStep:
    """Single step in research trace."""
    step: int
    action: str
    result: str


@dataclass
class NextAction:
    """Suggested next action for user."""
    label: str
    action_type: ActionType
    target: str

    def is_specific(self) -> bool:
        """Check if action is task-specific (not generic)."""
        generic_patterns = [
            "还有其他问题吗",
            "ask anything",
            "other questions",
        ]
        return not any(p in self.label.lower() for p in generic_patterns)


@dataclass
class PresentationContext:
    """Context for result presentation."""
    title: str
    subtitle: str
    audience: Audience = Audience.ORDINARY
    language: Language = Language.ZH


@dataclass
class ResultPresentation:
    """
    Complete result presentation model.

    This is the top-level structure that all surface types consume.
    """
    context: PresentationContext
    evidence_profile: EvidenceProfile

    # Primary answer
    lead: str                                       # First paragraph, always visible
    sections: List[AnswerSection] = field(default_factory=list)
    inline_citations: List[InlineCitation] = field(default_factory=list)

    # Evidence
    source_cards: List[SourceDisplay] = field(default_factory=list)
    boundary_notice: str = ""                       # What this result does NOT cover
    research_trace: List[ResearchTraceStep] = field(default_factory=list)

    # Next steps
    next_actions: List[NextAction] = field(default_factory=list)

    def validate(self) -> List[str]:
        """
        Validate presentation against anti-patterns.

        Returns list of validation errors (empty if valid).
        """
        errors = []

        # Check for internal IDs in source cards
        for i, card in enumerate(self.source_cards):
            if card.title.startswith("src-"):
                errors.append(f"Source card {i}: title contains internal ID")
            if card._internal_id and card._internal_id in card.title:
                errors.append(f"Source card {i}: internal ID leaked to title")

        # Check for raw internal labels
        for i, citation in enumerate(self.inline_citations):
            if citation.provenance_type in citation.text:
                errors.append(f"Citation {i}: raw provenance type in display text")

        # Check next actions are specific
        generic_actions = [a for a in self.next_actions if not a.is_specific()]
        if generic_actions:
            errors.append(f"Found {len(generic_actions)} generic next actions")

        # Check title-only sources are not counted as support
        title_only_count = sum(
            1 for c in self.source_cards
            if c.evidence_depth_label == "仅题录信息"
        )
        if title_only_count > 0 and self.evidence_profile.limited_source_count == 0:
            errors.append("Title-only sources exist but not counted in limited_source_count")

        forbidden_patterns = (
            r"\bsrc-[a-z0-9-]+-\d+\b",
            r"\b(?:deep_extracted|abstract_weighted|source_checked|title_only)\b",
            r"\b(?:quoted_fact|source_supported_conclusion|llm_inference)\b",
        )
        visible_texts = [
            self.context.title,
            self.context.subtitle,
            self.lead,
            self.boundary_notice,
            *(section.title for section in self.sections),
            *(section.content for section in self.sections),
            *(citation.text for citation in self.inline_citations),
            *(citation.provenance_label for citation in self.inline_citations),
            *(card.title for card in self.source_cards),
            *(item for card in self.source_cards for item in card.limitations),
            *(action.label for action in self.next_actions),
        ]
        for pattern in forbidden_patterns:
            if any(re.search(pattern, str(text), re.IGNORECASE) for text in visible_texts):
                errors.append(f"Visible text contains internal token matching {pattern}")

        return errors


# =============================================================================
# BUILDER FUNCTIONS
# =============================================================================

def translate_evidence_depth(internal_value: str) -> str:
    """
    Translate internal evidence depth to user-facing label.

    Safe fallback: returns "未知" for unrecognized values.
    """
    return EVIDENCE_DEPTH_LABELS.get(internal_value, "未知")


def translate_provenance(internal_value: str) -> str:
    """
    Translate internal provenance type to user-facing label.

    Safe fallback: returns original value wrapped in brackets.
    """
    return PROVENANCE_LABELS.get(internal_value, f"[{internal_value}]")


def translate_source_type(internal_value: str) -> str:
    """
    Translate internal source type to user-facing label.

    Safe fallback: returns capitalized original value.
    """
    return SOURCE_TYPE_LABELS.get(internal_value, internal_value.capitalize())


def _derive_safe_use(source_kind: str, evidence_level: str) -> tuple[str, str]:
    kind = (source_kind or "").lower().strip()
    level = (evidence_level or "").lower().strip()

    if kind in {"regulation", "guidance"} or level in {"regulation", "guideline", "guidance"}:
        return "说明书/管辖边界 (label / jurisdiction boundary)", "病理机制或生物学细节 (disease superiority or biology)"
    if level == "review":
        return "分支图谱/证据综合 (branch map / synthesis)", "单一研究决定性主张 (single-study winner claims)"
    if level == "original-study":
        return "特定指标/分支细节 (specific endpoint / branch detail)", "过度泛化或常规指导 (broad generalization or routine leadership)"
    if level == "case-series":
        return "罕见信号/分支可见性 (rare signal / branch visibility)", "流行率或常规层级 (prevalence or routine hierarchy)"
    if level == "commentary":
        return "仅限上下文背景 (context only)", "决策性主张 (decision-bearing claims)"
    return "仅作发现/背景了解 (discovery / background only)", "强有力结论 (strong conclusions)"


def build_evidence_profile(
    sources: List[Dict[str, Any]],
    claims: Optional[List[Dict[str, Any]]] = None,
    authority_state: str = "automated",
) -> EvidenceProfile:
    """
    Build evidence profile from source and claim data.

    Args:
        sources: List of source dictionaries with verification_status field
        claims: Optional list of claim dictionaries with provenance field
        authority_state: "automated" or "human_reviewed"

    Returns:
        EvidenceProfile with computed counts
    """
    unique_sources: List[Dict[str, Any]] = []
    seen_source_keys = set()
    for index, source in enumerate(sources):
        source_key = (
            source.get("source_id")
            or source.get("id")
            or source.get("doi")
            or source.get("pmid")
            or source.get("url")
            or f"anonymous-{index}"
        )
        if source_key in seen_source_keys:
            continue
        seen_source_keys.add(source_key)
        unique_sources.append(source)

    # Count by depth
    deep_extracted = 0
    source_checked = 0
    abstract_weighted = 0
    title_only = 0
    unknown = 0

    for src in unique_sources:
        status = src.get("verification_status", "").lower()
        if status in ("deep_extracted", "audited", "full_text"):
            deep_extracted += 1
        elif status == "source_checked":
            source_checked += 1
        elif status in ("abstract_weighted", "abstract"):
            abstract_weighted += 1
        elif status == "title_only":
            title_only += 1
        else:
            unknown += 1

    # Count by provenance (if claims provided)
    direct_support = 0
    supported_synthesis = 0
    inference = 0

    if claims:
        for claim in claims:
            prov = claim.get("provenance", "").lower()
            if prov == "quoted_fact":
                direct_support += 1
            elif prov == "source_supported_conclusion":
                supported_synthesis += 1
            elif prov == "llm_inference":
                inference += 1
    return EvidenceProfile(
        authority_state=AuthorityState(authority_state),
        source_count=len(unique_sources),
        direct_support_count=direct_support,
        supported_synthesis_count=supported_synthesis,
        inference_count=inference,
        limited_source_count=title_only,
        unknown_source_count=unknown,
        unresolved_gap_count=0,  # Caller should set if known
        deep_extracted_count=deep_extracted,
        source_checked_count=source_checked,
        abstract_weighted_count=abstract_weighted,
    )


def build_source_display(
    source: Dict[str, Any],
    include_internal_id: bool = False,
) -> SourceDisplay:
    """
    Build user-facing source display from internal source data.

    Args:
        source: Source dictionary with fields like title, doi, pmid, etc.
        include_internal_id: Whether to preserve internal ID (for debugging)

    Returns:
        SourceDisplay with user-facing labels
    """
    # Get title (prefer paper title, fall back to internal ID warning)
    title = source.get("title", "")
    internal_id = source.get("source_id", source.get("id", ""))

    if not title or title.startswith("src-"):
        # Try to extract from other fields
        title = source.get("paper_title", source.get("display_title", ""))

    if not title or title.startswith("src-"):
        if internal_id:
            # e.g., src-ckd-004 -> 文献 [CKD-004]
            match = re.match(r"src-([a-z0-9-]+)-(\d+)", internal_id, re.I)
            if match:
                disease, num = match.groups()
                title = f"文献 [{disease.upper()}-{num}]"
            else:
                title = f"文献 [{internal_id.upper()}]"
        else:
            title = "[标题待补充]"

    # Build canonical URL
    canonical_url = None
    doi = source.get("doi", "")
    pmid = source.get("pmid", "")
    fallback_url = source.get("url", source.get("canonical_url", ""))

    if doi:
        if doi.startswith("http"):
            canonical_url = doi
        elif doi.startswith("10."):
            canonical_url = f"https://doi.org/{doi}"
    elif pmid:
        canonical_url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    elif source.get("pmcid"):
        pmcid = str(source.get("pmcid"))
        canonical_url = (
            f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
            if pmcid.upper().startswith("PMC")
            else f"https://pmc.ncbi.nlm.nih.gov/articles/PMC{pmcid}/"
        )
    elif isinstance(fallback_url, str) and fallback_url.startswith(("https://", "http://")):
        canonical_url = fallback_url

    # Translate labels
    source_type = translate_source_type(
        source.get("source_type", source.get("type", "unknown"))
    )
    evidence_depth = translate_evidence_depth(
        source.get("verification_status", source.get("depth", "unknown"))
    )
    source_kind = source.get("source_kind", source.get("source_type", source.get("type", "")))
    evidence_level = source.get("evidence_level", "")
    safest_use, must_not_control = _derive_safe_use(source_kind, evidence_level)

    species_raw = source.get("species", "")
    if isinstance(species_raw, list):
        species_raw = ", ".join(species_raw)
    species_map = {
        "feline": "猫科 (feline)",
        "canine": "犬科 (canine)",
        "human": "人 (human)",
    }
    species_label = species_map.get(str(species_raw).lower().strip(), species_raw) or ""

    decision_raw = source.get("decision_grade", "")
    decision_map = {
        "no": "非决策级 (no)",
        "yes": "决策级 (yes)",
        "provisional": "暂定决策级 (provisional)",
    }
    decision_grade = decision_map.get(str(decision_raw).lower().strip(), decision_raw) or ""
    authors = source.get("authors", [])
    if isinstance(authors, str):
        authors = [item.strip() for item in re.split(r"[;,]", authors) if item.strip()]
    tags = source.get("tags", [])
    if isinstance(tags, str):
        tags = [item.strip() for item in re.split(r"[;,]", tags) if item.strip()]
    journal = source.get("journal", "")
    pmcid = source.get("pmcid", "")
    pmid_value = source.get("pmid", "")
    doi_value = source.get("doi", "")
    publish_date = source.get("publish_date", source.get("date", ""))

    # Extract limitations
    limitations = source.get("limitations", [])
    if isinstance(limitations, str):
        limitations = [limitations] if limitations else []

    return SourceDisplay(
        title=title,
        canonical_url=canonical_url,
        publication_year=source.get("year", source.get("publication_year")),
        publish_date=publish_date,
        source_type_label=source_type,
        evidence_depth_label=evidence_depth,
        source_family_label=translate_source_type(source_kind or source.get("source_type", source.get("type", "unknown"))),
        species_label=species_label,
        decision_grade_label=decision_grade,
        safest_use=safest_use,
        must_not_control=must_not_control,
        journal=journal,
        pmcid=pmcid,
        pmid=pmid_value,
        doi=doi_value,
        authors=authors,
        tags=tags,
        limitations=limitations,
        # Identity remains available for citation matching but is never rendered by
        # ordinary-user adapters.
        _internal_id=internal_id,
    )


def build_source_displays(
    sources: List[Dict[str, Any]],
    include_internal_ids: bool = False,
) -> List[SourceDisplay]:
    """
    Build list of source displays from internal source data.

    Args:
        sources: List of source dictionaries
        include_internal_ids: Whether to preserve internal IDs

    Returns:
        List of SourceDisplay objects
    """
    return [
        build_source_display(src, include_internal_ids)
        for src in sources
    ]


def build_inline_citation(
    source_display: SourceDisplay,
    provenance_type: str,
) -> InlineCitation:
    """
    Build inline citation from source display.

    Args:
        source_display: The source being cited
        provenance_type: Internal provenance type

    Returns:
        InlineCitation with shortened title and labels
    """
    # Shorten title for inline display
    short_title = source_display.title
    if len(short_title) > 50:
        short_title = short_title[:47] + "..."

    # Add year if available
    if source_display.publication_year:
        short_title = f"{short_title} ({source_display.publication_year})"

    return InlineCitation(
        text=short_title,
        source_ref=source_display._internal_id or source_display.title,
        provenance_type=provenance_type,
        provenance_label=translate_provenance(provenance_type),
    )


def render_user_facing_provenance(
    text: str,
    source_cards: List[SourceDisplay],
    html_output: bool = False,
) -> str:
    """Replace internal provenance tags with titles and translated labels."""
    source_map = {
        card._internal_id: card
        for card in source_cards
        if card._internal_id
    }

    def source_text(source_ids: str, use_links: bool) -> str:
        values = []
        for source_id in (item.strip() for item in source_ids.split(",")):
            card = source_map.get(source_id)
            if card is None:
                values.append("来源信息不可用")
                continue
            title = html_lib.escape(card.title) if use_links else card.title
            if use_links and card.has_valid_link():
                url = html_lib.escape(card.canonical_url or "", quote=True)
                values.append(
                    f'<a href="{url}" target="_blank" rel="noopener">{title}</a>'
                )
            else:
                values.append(title)
        return "；".join(values)

    def replace_tag(match: re.Match) -> str:
        provenance_type = match.group(1) or match.group(3)
        source_ids = match.group(2) or ""
        label = translate_provenance(provenance_type)
        sources = source_text(source_ids, html_output)
        suffix = f"：{sources}" if sources else ""
        if not html_output:
            return f"[{label}{suffix}]"
        color = {
            "quoted_fact": "#16a34a",
            "source_supported_conclusion": "#ca8a04",
            "llm_inference": "#6b7280",
        }.get(provenance_type, "#8b90a0")
        return (
            f'<span style="color:{color};font-size:0.78em">'
            f"{html_lib.escape(label)}{suffix}</span>"
        )

    pattern = re.compile(
        r"\[(quoted_fact|source_supported_conclusion):\s*([^\]]+)\]"
        r"|\[(llm_inference)\]"
    )
    res = pattern.sub(replace_tag, text)

    # Proactively clean up any loose internal IDs that might have leaked into the prose
    def replace_loose_id(match_obj: re.Match) -> str:
        full_id = match_obj.group(0)
        card = source_map.get(full_id)
        if card:
            title = html_lib.escape(card.title) if html_output else card.title
            if html_output and card.has_valid_link():
                url = html_lib.escape(card.canonical_url or "", quote=True)
                return f'<a href="{url}" target="_blank" rel="noopener">{title}</a>'
            return title
        # Fallback to normalized title format
        disease = match_obj.group(1).upper()
        num = match_obj.group(2)
        return f"文献 [{disease}-{num}]"

    res = re.sub(r"\bsrc-([a-z0-9-]+)-(\d+)\b", replace_loose_id, res, flags=re.I)
    return res


def build_next_actions(
    topic: str,
    surface_type: Literal["overview", "ranked", "vault"] = "vault",
    related_topics: Optional[List[str]] = None,
) -> List[NextAction]:
    """
    Build task-specific next actions.

    IMPORTANT: Generic actions like "还有其他问题吗" are NOT allowed.
    All actions must be specific to the topic and surface.

    Args:
        topic: Current topic being viewed
        surface_type: Type of surface (overview, ranked, vault)
        related_topics: Optional list of related topics

    Returns:
        List of 2-4 specific NextAction objects
    """
    actions = []

    if surface_type == "overview":
        actions.append(NextAction(
            label=f"查看{topic}的治疗选项对比",
            action_type=ActionType.NAVIGATE,
            target=f"/topics/{topic}/treatments",
        ))
        actions.append(NextAction(
            label=f"了解{topic}的诊断流程",
            action_type=ActionType.NAVIGATE,
            target=f"/topics/{topic}/diagnosis",
        ))

    elif surface_type == "ranked":
        actions.append(NextAction(
            label="对比其他治疗方案的证据强度",
            action_type=ActionType.EXPAND,
            target="collapsed-treatments",
        ))
        actions.append(NextAction(
            label="查看支持这些结论的原始文献",
            action_type=ActionType.EXPAND,
            target="source-cards",
        ))

    elif surface_type == "vault":
        actions.append(NextAction(
            label=f"深入了解{topic}的机制",
            action_type=ActionType.SEARCH,
            target=f"{topic} 病理生理机制",
        ))
        actions.append(NextAction(
            label="查看相关的临床指南",
            action_type=ActionType.SEARCH,
            target=f"{topic} ISFM guidelines",
        ))

    # Add related topics if provided
    if related_topics:
        for rt in related_topics[:2]:  # Max 2 related
            actions.append(NextAction(
                label=f"探索相关主题：{rt}",
                action_type=ActionType.NAVIGATE,
                target=f"/topics/{rt}",
            ))

    return actions[:4]  # Max 4 actions


def build_result_presentation(
    title: str,
    subtitle: str,
    lead: str,
    sources: List[Dict[str, Any]],
    claims: Optional[List[Dict[str, Any]]] = None,
    sections: Optional[List[Dict[str, Any]]] = None,
    boundary_notice: str = "",
    topic: str = "",
    surface_type: Literal["overview", "ranked", "vault"] = "vault",
    audience: str = "ordinary",
    language: str = "zh",
    authority_state: str = "automated",
    related_topics: Optional[List[str]] = None,
) -> ResultPresentation:
    """
    Build complete result presentation.

    This is the main entry point for creating presentation objects.

    Args:
        title: Page/result title
        subtitle: Explanatory subtitle
        lead: First paragraph (always visible)
        sources: List of source dictionaries
        claims: Optional list of claim dictionaries with provenance
        sections: Optional list of section dictionaries
        boundary_notice: What this result does NOT cover
        topic: Topic name for generating next actions
        surface_type: Type of surface
        audience: "ordinary" or "professional"
        language: "zh" or "en"
        authority_state: "automated" or "human_reviewed"
        related_topics: Optional related topics for next actions

    Returns:
        Complete ResultPresentation object
    """
    # Build components
    evidence_profile = build_evidence_profile(
        sources=sources,
        claims=claims,
        authority_state=authority_state,
    )

    source_cards = build_source_displays(
        sources=sources,
        include_internal_ids=audience == "professional",
    )

    # Build sections if provided
    answer_sections = []
    all_citations = []

    if sections:
        for sec in sections:
            section_citations = []
            for cit in sec.get("citations", []):
                # Find matching source card
                source_ref = cit.get("source_ref", "")
                matching_card = next(
                    (c for c in source_cards if c._internal_id == source_ref or c.title == source_ref),
                    None
                )
                if matching_card:
                    inline_cit = build_inline_citation(
                        matching_card,
                        cit.get("provenance", "source_supported_conclusion"),
                    )
                    section_citations.append(inline_cit)
                    all_citations.append(inline_cit)

            content_clean = render_user_facing_provenance(
                sec.get("content", ""),
                source_cards,
                html_output=False,
            )
            answer_sections.append(AnswerSection(
                title=sec.get("title", ""),
                content=content_clean,
                citations=section_citations,
            ))

    # Build next actions
    next_actions = build_next_actions(
        topic=topic or title,
        surface_type=surface_type,
        related_topics=related_topics,
    )

    lead_clean = render_user_facing_provenance(lead, source_cards, html_output=False)
    if len(lead_clean) > 500:
        lead_clean = lead_clean[:497] + "..."

    return ResultPresentation(
        context=PresentationContext(
            title=title,
            subtitle=subtitle,
            audience=Audience(audience),
            language=Language(language),
        ),
        evidence_profile=evidence_profile,
        lead=lead_clean,
        sections=answer_sections,
        inline_citations=all_citations,
        source_cards=source_cards,
        boundary_notice=boundary_notice,
        research_trace=[],  # Caller should populate if available
        next_actions=next_actions,
    )


# =============================================================================
# STATE DETECTION HELPERS
# =============================================================================

def detect_presentation_state(presentation: ResultPresentation) -> str:
    """
    Detect the presentation state based on content.

    Returns one of the state matrix values:
    - supported-profile: Direct, deep support
    - mixed-profile: Mixed depth or synthesis
    - sparse-profile: Few sources or material inference
    - no-direct-evidence: No relevant source cards
    - title-only: Source has no abstract/full text

    See render-result-page.md State Matrix for full list.
    """
    profile = presentation.evidence_profile

    if not presentation.source_cards:
        return "no-direct-evidence"

    # Check for title-only dominant
    title_only_ratio = (
        profile.limited_source_count / len(presentation.source_cards)
        if presentation.source_cards else 0
    )
    if title_only_ratio > 0.5:
        return "title-only"

    # Check for sparse
    if profile.is_sparse():
        return "sparse-profile"

    # Check for mixed
    if profile.inference_count > 0 and profile.direct_support_count > 0:
        return "mixed-profile"

    return "supported-profile"


def get_state_warning(state: str) -> Optional[str]:
    """
    Get warning text for a given state.

    Returns None if no warning needed.
    """
    warnings = {
        "sparse-profile": "⚠️ 证据较薄",
        "no-direct-evidence": "⚠️ 未找到直接证据",
        "title-only": "⚠️ 来源仅有题录信息，未能核查内容",
    }
    return warnings.get(state)


def should_show_research_action(state: str) -> bool:
    """Check if state warrants showing 'run deeper research' action."""
    return state in ("sparse-profile", "no-direct-evidence", "title-only")
