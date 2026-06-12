"""
Gap Checker for the Harness Loop.

Based on RALPH/Zenith principles:
- Compares draft output against original requirements
- Identifies missing elements before finalization
- Prevents premature completion on complex tasks
"""

from dataclasses import dataclass
from typing import List, Optional

from .schemas import ResearchRecord, TaskType, SearchDepth


@dataclass
class Gap:
    """A gap identified between draft and requirements."""
    category: str
    description: str
    severity: str  # low, medium, high, critical
    suggestion: str


@dataclass
class GapCheckResult:
    """Result of gap checking."""
    has_critical_gaps: bool
    has_high_gaps: bool
    gaps: List[Gap]
    recommendation: str  # continue, revise, or finalize


class GapChecker:
    """
    Checks research outputs for gaps against requirements.

    This is the core of the Feline-RALPH harness loop,
    ensuring complex tasks don't complete prematurely.
    """

    # Protocol completeness checklist
    PROTOCOL_REQUIRED_ELEMENTS = [
        ("purpose", ["目的", "purpose", "objective", "aim"]),
        ("animals", ["动物", "animal", "cat", "feline", "subject"]),
        ("enrollment", ["入组", "enrollment", "inclusion", "exclusion"]),
        ("grouping", ["分组", "group", "arm", "randomiz"]),
        ("intervention", ["干预", "intervention", "treatment", "drug", "dose"]),
        ("endpoints", ["终点", "endpoint", "outcome", "efficacy", "safety"]),
        ("timepoints", ["时间点", "timepoint", "day", "week", "schedule"]),
        ("statistics", ["统计", "statistic", "sample size", "analysis"]),
        ("ethics", ["伦理", "ethic", "welfare", "humane", "iacuc"]),
    ]

    # Endpoint selection checklist
    ENDPOINT_REQUIRED_ELEMENTS = [
        ("diagnosis_vs_efficacy", ["诊断", "diagnosis", "疗效", "efficacy"]),
        ("primary_secondary", ["主要", "primary", "次要", "secondary"]),
        ("species_evidence", ["猫", "feline", "cat"]),
        ("evidence_source", ["文献", "literature", "reference", "source", "pmid"]),
    ]

    # Literature review checklist
    LITERATURE_REQUIRED_ELEMENTS = [
        ("search_scope", ["检索", "search", "pubmed", "database"]),
        ("evidence_cards", ["文献", "article", "study", "paper"]),
        ("synthesis", ["总结", "summary", "synthesis", "conclusion"]),
    ]

    def check(self, record: ResearchRecord, draft: str) -> GapCheckResult:
        """
        Check draft output for gaps.

        Args:
            record: Research record with task context
            draft: Current draft output

        Returns:
            GapCheckResult with identified gaps
        """
        gaps = []

        # Run task-specific checks
        if record.task_type == TaskType.PROTOCOL_DESIGN:
            gaps.extend(self._check_protocol_gaps(draft, record))
        elif record.task_type == TaskType.ENDPOINT_SELECTION:
            gaps.extend(self._check_endpoint_gaps(draft, record))
        elif record.task_type == TaskType.LITERATURE_REVIEW:
            gaps.extend(self._check_literature_gaps(draft, record))
        elif record.task_type == TaskType.PK_DESIGN:
            gaps.extend(self._check_pk_gaps(draft, record))

        # Run universal checks
        gaps.extend(self._check_species_boundary(draft, record))
        gaps.extend(self._check_evidence_grounding(draft, record))
        gaps.extend(self._check_uncertainty_disclosure(draft, record))

        # Determine severity levels
        has_critical = any(g.severity == "critical" for g in gaps)
        has_high = any(g.severity == "high" for g in gaps)

        # Generate recommendation
        if has_critical:
            recommendation = "revise"
        elif has_high and record.search_depth in [SearchDepth.DEEP, SearchDepth.EVIDENCE_AUDIT]:
            recommendation = "revise"
        elif gaps:
            recommendation = "continue"  # May finalize with minor gaps
        else:
            recommendation = "finalize"

        return GapCheckResult(
            has_critical_gaps=has_critical,
            has_high_gaps=has_high,
            gaps=gaps,
            recommendation=recommendation,
        )

    def _check_protocol_gaps(self, draft: str, record: ResearchRecord) -> List[Gap]:
        """Check protocol design for required elements."""
        gaps = []
        draft_lower = draft.lower()

        for element, keywords in self.PROTOCOL_REQUIRED_ELEMENTS:
            found = any(kw in draft_lower for kw in keywords)
            if not found:
                severity = "high" if element in ["purpose", "endpoints", "animals"] else "medium"
                gaps.append(Gap(
                    category="protocol_completeness",
                    description=f"Missing {element} section",
                    severity=severity,
                    suggestion=f"Add {element} to the protocol",
                ))

        return gaps

    def _check_endpoint_gaps(self, draft: str, record: ResearchRecord) -> List[Gap]:
        """Check endpoint selection for required elements."""
        gaps = []
        draft_lower = draft.lower()

        for element, keywords in self.ENDPOINT_REQUIRED_ELEMENTS:
            found = any(kw in draft_lower for kw in keywords)
            if not found:
                severity = "high" if element == "species_evidence" else "medium"
                gaps.append(Gap(
                    category="endpoint_completeness",
                    description=f"Missing {element} consideration",
                    severity=severity,
                    suggestion=f"Address {element} in endpoint selection",
                ))

        # Check if endpoints are distinguished by use case
        if not any(kw in draft_lower for kw in ["入组", "enrollment", "诊断", "diagnosis"]):
            if not any(kw in draft_lower for kw in ["疗效", "efficacy", "安全", "safety"]):
                gaps.append(Gap(
                    category="endpoint_clarity",
                    description="Endpoint use cases not distinguished",
                    severity="high",
                    suggestion="Distinguish diagnosis vs enrollment vs efficacy vs safety endpoints",
                ))

        return gaps

    def _check_literature_gaps(self, draft: str, record: ResearchRecord) -> List[Gap]:
        """Check literature review for required elements."""
        gaps = []
        draft_lower = draft.lower()

        for element, keywords in self.LITERATURE_REQUIRED_ELEMENTS:
            found = any(kw in draft_lower for kw in keywords)
            if not found:
                gaps.append(Gap(
                    category="literature_completeness",
                    description=f"Missing {element}",
                    severity="medium",
                    suggestion=f"Add {element} to the review",
                ))

        return gaps

    def _check_pk_gaps(self, draft: str, record: ResearchRecord) -> List[Gap]:
        """Check PK design for required elements."""
        gaps = []
        draft_lower = draft.lower()

        pk_elements = [
            ("sampling_times", ["采血", "sampling", "time point", "时间点"]),
            ("blood_volume", ["血量", "blood volume", "ml/kg"]),
            ("sample_size", ["样本量", "sample size", "n ="]),
            ("analysis_method", ["分析", "analysis", "lc-ms", "bioanalytical"]),
        ]

        for element, keywords in pk_elements:
            found = any(kw in draft_lower for kw in keywords)
            if not found:
                gaps.append(Gap(
                    category="pk_completeness",
                    description=f"Missing {element}",
                    severity="high",
                    suggestion=f"Add {element} to PK design",
                ))

        return gaps

    def _check_species_boundary(self, draft: str, record: ResearchRecord) -> List[Gap]:
        """Check for species boundary violations."""
        gaps = []
        draft_lower = draft.lower()

        # Check for unmarked cross-species references
        cross_species_indicators = [
            ("canine", "dog evidence"),
            ("human", "human evidence"),
            ("mouse", "mouse/rodent evidence"),
            ("in vitro", "in vitro evidence"),
        ]

        for indicator, description in cross_species_indicators:
            if indicator in draft_lower:
                # Check if it's properly flagged
                warning_indicators = [
                    "外推", "extrapolat", "需注意", "caution",
                    "不能直接", "cannot directly", "限制", "limitation",
                ]
                properly_flagged = any(wi in draft_lower for wi in warning_indicators)

                if not properly_flagged:
                    gaps.append(Gap(
                        category="species_boundary",
                        description=f"Unmarked {description} found",
                        severity="high",
                        suggestion=f"Flag {description} extrapolation risk",
                    ))

        return gaps

    def _check_evidence_grounding(self, draft: str, record: ResearchRecord) -> List[Gap]:
        """Check if conclusions are grounded in evidence."""
        gaps = []
        draft_lower = draft.lower()

        # For non-trivial tasks, check for evidence citations
        if record.search_depth in [SearchDepth.DEEP, SearchDepth.EVIDENCE_AUDIT]:
            evidence_indicators = [
                "pmid", "doi", "文献", "reference", "source",
                "研究表明", "study shows", "according to",
                "src-", "et al",
            ]

            has_evidence = any(ei in draft_lower for ei in evidence_indicators)
            if not has_evidence:
                gaps.append(Gap(
                    category="evidence_grounding",
                    description="No evidence citations found",
                    severity="critical" if record.search_depth == SearchDepth.EVIDENCE_AUDIT else "high",
                    suggestion="Add evidence citations to support conclusions",
                ))

        return gaps

    def _check_uncertainty_disclosure(self, draft: str, record: ResearchRecord) -> List[Gap]:
        """Check if uncertainties are disclosed."""
        gaps = []
        draft_lower = draft.lower()

        # For deep research tasks, require uncertainty disclosure
        if record.search_depth in [SearchDepth.DEEP, SearchDepth.EVIDENCE_AUDIT]:
            uncertainty_indicators = [
                "不确定", "uncertainty", "limitation", "局限",
                "需要更多", "further research", "证据不足",
                "may", "might", "possibly", "可能",
            ]

            has_uncertainty = any(ui in draft_lower for ui in uncertainty_indicators)
            if not has_uncertainty:
                gaps.append(Gap(
                    category="uncertainty_disclosure",
                    description="No uncertainties disclosed",
                    severity="medium",
                    suggestion="Acknowledge limitations and evidence gaps",
                ))

        return gaps

    def suggest_revision_focus(self, result: GapCheckResult) -> List[str]:
        """
        Suggest areas to focus revision on.

        Args:
            result: Gap check result

        Returns:
            List of revision focus areas
        """
        focus_areas = []

        # Group gaps by category
        categories = {}
        for gap in result.gaps:
            if gap.category not in categories:
                categories[gap.category] = []
            categories[gap.category].append(gap)

        # Prioritize by severity
        for category, gaps in categories.items():
            max_severity = max(
                (g.severity for g in gaps),
                key=lambda s: {"critical": 4, "high": 3, "medium": 2, "low": 1}.get(s, 0)
            )

            if max_severity in ["critical", "high"]:
                focus_areas.append(f"{category}: {gaps[0].suggestion}")

        return focus_areas
