#!/usr/bin/env python3
"""
scripts/workspace_tabs.py — Research Workspace tab structure for three-layer architecture.

Research Workspace provides dynamic research flow with tabs:
1. Research Plan - Query interpretation and search scope
2. Evidence Cards - Ranked sources with selection rationale
3. Findings - Key findings organized by theme
4. Methods - Study design and endpoint comparison
5. Gaps - Uncertainty, limitations, and next steps

This is Layer 3 of the three-layer architecture:
  Quick Start → Disease Briefing → Research Workspace
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Any
from enum import Enum


class WorkspaceTab(Enum):
    """Available tabs in Research Workspace."""
    PLAN = "plan"
    EVIDENCE = "evidence"
    FINDINGS = "findings"
    METHODS = "methods"
    GAPS = "gaps"


@dataclass
class EvidenceCard:
    """Structured representation of a source for the Evidence Cards tab."""
    source_id: str
    title: str
    year: Optional[int]
    journal: Optional[str]
    evidence_level: Optional[str]
    why_included: str  # Why this source was selected
    key_finding: str  # Main finding from this source
    limitations: str  # Limitations of this source
    url: Optional[str] = None
    doi: Optional[str] = None
    pmid: Optional[str] = None
    # Deep extraction fields
    has_deep_extraction: bool = False
    deep_why_matters: Optional[str] = None
    deep_takeaway: Optional[str] = None


@dataclass
class ExcludedSource:
    """Represents a source that was considered but excluded."""
    source_id: str
    title: str
    reason: str  # Why it was excluded


@dataclass
class ResearchPlan:
    """Structured output for the Research Plan tab."""
    query_interpretation: str  # How the system understood the query
    disease: str
    time_window: str  # e.g., "2021-2026"
    source_priorities: list[str]  # e.g., ["JVIM", "Scientific Reports", "PubMed"]
    search_scope: str  # Description of what was searched
    filters_applied: list[str]  # e.g., ["peer-reviewed", "feline-specific"]


@dataclass
class Finding:
    """A key finding for the Findings tab."""
    theme: str  # e.g., "Diagnosis", "Treatment", "Prognosis"
    finding: str
    supporting_sources: list[str]  # Source IDs that support this finding
    confidence: str  # "high", "medium", "low"


@dataclass
class MethodComparison:
    """Comparison entry for the Methods tab."""
    source_id: str
    title: str
    study_design: str
    sample_size: str
    endpoints: list[str]
    model_species: str
    key_methods: str


@dataclass
class WorkspaceOutput:
    """Complete structured output for Research Workspace."""
    research_plan: ResearchPlan
    evidence_cards: list[EvidenceCard] = field(default_factory=list)
    excluded_sources: list[ExcludedSource] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)
    method_comparisons: list[MethodComparison] = field(default_factory=list)
    gaps: list[str] = field(default_factory=list)
    next_steps: list[str] = field(default_factory=list)
    # Metadata
    total_sources_considered: int = 0
    sources_included: int = 0
    language: str = "zh"


def render_workspace_tabs(output: WorkspaceOutput, st_module) -> None:
    """
    Render Research Workspace with tabs.

    Args:
        output: WorkspaceOutput with structured data
        st_module: Streamlit module (passed to avoid circular imports)
    """
    st = st_module
    is_zh = output.language == "zh"

    # Tab labels
    tab_labels = [
        "📋 Research Plan" if not is_zh else "📋 任务摘要",
        f"📚 Evidence Map ({len(output.evidence_cards)})" if not is_zh else f"📚 证据地图 ({len(output.evidence_cards)})",
        f"💡 Findings ({len(output.findings)})" if not is_zh else f"💡 核心发现 ({len(output.findings)})",
        "🔬 Models & Endpoints" if not is_zh else "🔬 模型与药效评价价值",
        "❓ Gaps & Next" if not is_zh else "❓ 缺口与下一步",
    ]

    tabs = st.tabs(tab_labels)

    # Tab 1: Research Plan
    with tabs[0]:
        render_plan_tab(output.research_plan, is_zh, st)

    # Tab 2: Evidence Cards
    with tabs[1]:
        render_evidence_tab(output.evidence_cards, output.excluded_sources, is_zh, st)

    # Tab 3: Findings
    with tabs[2]:
        render_findings_tab(output.findings, is_zh, st)

    # Tab 4: Methods
    with tabs[3]:
        render_methods_tab(output.method_comparisons, is_zh, st)

    # Tab 5: Gaps
    with tabs[4]:
        render_gaps_tab(output.gaps, output.next_steps, is_zh, st)


def render_plan_tab(plan: ResearchPlan, is_zh: bool, st) -> None:
    """Render the Research Plan tab."""
    st.subheader("Query Interpretation" if not is_zh else "任务摘要")
    st.markdown(plan.query_interpretation)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Disease:** {plan.disease.upper()}")
        st.markdown(f"**Time Window:** {plan.time_window}")
    with col2:
        st.markdown(f"**Scope:** {plan.search_scope}")

    st.markdown("**Source Priorities:**")
    for priority in plan.source_priorities:
        st.markdown(f"- {priority}")

    if plan.filters_applied:
        st.markdown("**Filters Applied:**")
        for f in plan.filters_applied:
            st.markdown(f"- {f}")


def render_evidence_tab(cards: list[EvidenceCard], excluded: list[ExcludedSource], is_zh: bool, st) -> None:
    """Render the Evidence Cards tab."""
    if not cards:
        st.info("No evidence cards available" if not is_zh else "暂无证据卡片")
        return

    for card in cards:
        with st.expander(f"📄 {card.title} ({card.year or 'N/A'})", expanded=False):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"**Journal:** {card.journal or 'N/A'}")
                st.markdown(f"**Evidence Level:** {card.evidence_level or 'Not specified'}")
                if card.has_deep_extraction:
                    st.markdown("🔬 *Has deep extraction*")
            with col2:
                if card.doi:
                    st.markdown(f"[DOI]({card.doi})")
                if card.pmid:
                    st.markdown(f"[PubMed](https://pubmed.ncbi.nlm.nih.gov/{card.pmid})")

            st.markdown("**Why Included:**")
            st.markdown(card.why_included)

            st.markdown("**Key Finding:**")
            st.markdown(card.key_finding)

            st.markdown("**Limitations:**")
            st.markdown(card.limitations)

            if card.deep_why_matters:
                st.markdown("**Why It Matters (Deep Extraction):**")
                st.markdown(card.deep_why_matters)

    # Excluded sources
    if excluded:
        st.divider()
        with st.expander(f"Excluded / Lower Priority ({len(excluded)})" if not is_zh else f"排除项 ({len(excluded)})", expanded=False):
            for ex in excluded:
                st.markdown(f"- **{ex.title}**: {ex.reason}")


def render_findings_tab(findings: list[Finding], is_zh: bool, st) -> None:
    """Render the Findings tab."""
    if not findings:
        st.info("No findings extracted" if not is_zh else "暂无关键发现")
        return

    # Group by theme
    themes: dict[str, list[Finding]] = {}
    for f in findings:
        if f.theme not in themes:
            themes[f.theme] = []
        themes[f.theme].append(f)

    for theme, theme_findings in themes.items():
        st.subheader(theme)
        for f in theme_findings:
            confidence_color = {
                "high": "🟢",
                "medium": "🟡",
                "low": "🔴"
            }.get(f.confidence, "⚪")

            st.markdown(f"{confidence_color} {f.finding}")
            if f.supporting_sources:
                st.caption(f"Sources: {', '.join(f.supporting_sources)}")


def render_methods_tab(comparisons: list[MethodComparison], is_zh: bool, st) -> None:
    """Render the Methods comparison tab."""
    if not comparisons:
        st.info("No method comparisons available" if not is_zh else "暂无方法比较")
        return

    # Render as table
    import pandas as pd

    data = []
    for m in comparisons:
        data.append({
            "Title": m.title[:40] + "..." if len(m.title) > 40 else m.title,
            "Design": m.study_design,
            "N": m.sample_size,
            "Endpoints": ", ".join(m.endpoints[:3]),
            "Species": m.model_species,
        })

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    # Detailed view
    for m in comparisons:
        with st.expander(f"📊 {m.title[:50]}...", expanded=False):
            st.markdown(f"**Study Design:** {m.study_design}")
            st.markdown(f"**Sample Size:** {m.sample_size}")
            st.markdown(f"**Model Species:** {m.model_species}")
            st.markdown("**Endpoints:**")
            for ep in m.endpoints:
                st.markdown(f"- {ep}")
            st.markdown("**Key Methods:**")
            st.markdown(m.key_methods)


def render_gaps_tab(gaps: list[str], next_steps: list[str], is_zh: bool, st) -> None:
    """Render the Gaps and Next Steps tab."""
    st.subheader("Evidence Gaps" if not is_zh else "证据缺口")
    if gaps:
        for gap in gaps:
            st.markdown(f"- ❓ {gap}")
    else:
        st.info("No significant gaps identified" if not is_zh else "未发现显著证据缺口")

    st.divider()

    st.subheader("Recommended Next Steps" if not is_zh else "建议下一步")
    if next_steps:
        for step in next_steps:
            st.markdown(f"- ➡️ {step}")
    else:
        st.info("No specific next steps recommended" if not is_zh else "暂无具体建议")


def convert_research_mode_output_to_workspace(
    research_result: dict,
    language: str = "zh"
) -> WorkspaceOutput:
    """
    Convert existing research_mode.py output to WorkspaceOutput structure.

    This is a bridge function to integrate with existing code.
    """
    # Extract query interpretation
    query_interpretation = research_result.get("query_interpretation", "")
    if not query_interpretation:
        query_interpretation = research_result.get("question", "Research query")

    disease = research_result.get("disease", "unknown")
    time_window = research_result.get("time_window", "2020-2026")

    plan = ResearchPlan(
        query_interpretation=query_interpretation,
        disease=disease,
        time_window=time_window,
        source_priorities=research_result.get("source_priorities", ["JVIM", "Scientific Reports", "PubMed"]),
        search_scope=research_result.get("search_scope", "Local vault + PubMed"),
        filters_applied=research_result.get("filters", ["peer-reviewed", "feline-specific"]),
    )

    # Convert source cards to evidence cards and populate findings & method_comparisons
    evidence_cards = []
    findings = []
    method_comparisons = []

    for card in research_result.get("ranked_cards", []):
        evidence_cards.append(EvidenceCard(
            source_id=card.get("id", ""),
            title=card.get("title", "Untitled"),
            year=card.get("year"),
            journal=card.get("journal"),
            evidence_level=card.get("evidence_level"),
            why_included=card.get("why_included", "Relevant to query"),
            key_finding=card.get("one_line_summary", ""),
            limitations=card.get("limitations", "Not specified"),
            url=card.get("url"),
            doi=card.get("doi"),
            pmid=card.get("pmid"),
            has_deep_extraction=card.get("has_deep_extraction", False),
            deep_why_matters=card.get("deep_extraction_why"),
            deep_takeaway=card.get("deep_extraction_takeaway"),
        ))

        # Populate findings
        conclusions = card.get("supported_conclusions") or []
        for conclusion in conclusions:
            ev_level = (card.get("evidence_level") or "").upper()
            if "I" in ev_level or "II" in ev_level or "HIGH" in ev_level.lower():
                confidence = "high"
            elif "III" in ev_level or "MEDIUM" in ev_level.lower():
                confidence = "medium"
            else:
                confidence = "low"

            findings.append(Finding(
                theme="核心研究发现" if language == "zh" else "Core Research Findings",
                finding=conclusion,
                supporting_sources=[card.get("id", "")],
                confidence=confidence
            ))

        # Populate method comparisons
        study_design = card.get("study_design") or ("未标明" if language == "zh" else "Not specified")
        sample_size = "详见设计" if language == "zh" else "See design"
        import re
        match = re.search(r"(\d+)\s*(只猫|例|cats|cases|subjects|猫)", study_design, re.IGNORECASE)
        if match:
            sample_size = match.group(0)

        endpoints = card.get("endpoints") or []
        if not endpoints:
            endpoints = ["指标评估" if language == "zh" else "Endpoint evaluation"]

        method_comparisons.append(MethodComparison(
            source_id=card.get("id", ""),
            title=card.get("title", "Untitled"),
            study_design=study_design,
            sample_size=sample_size,
            endpoints=endpoints,
            model_species="猫" if language == "zh" else "Feline",
            key_methods=card.get("core_argument") or card.get("one_line_summary") or ("未标明" if language == "zh" else "Not specified")
        ))

    # Extract gaps and next steps
    gaps = research_result.get("gaps", [])
    next_steps = research_result.get("next_steps", [])

    return WorkspaceOutput(
        research_plan=plan,
        evidence_cards=evidence_cards,
        excluded_sources=[],
        findings=findings,
        method_comparisons=method_comparisons,
        gaps=gaps,
        next_steps=next_steps,
        total_sources_considered=research_result.get("total_considered", 0),
        sources_included=len(evidence_cards),
        language=language,
    )
