"""Search-depth execution contracts for research tasks."""

from dataclasses import dataclass, field
from typing import Any, Iterable

from .schemas import ResearchRecord, SearchDepth


@dataclass(frozen=True)
class SearchDepthPolicy:
    """Minimum observable retrieval work for one search depth."""

    min_evidence: int
    min_retrieval_rounds: int
    min_source_families: int
    require_gap_reflection: bool = False
    require_counterevidence: bool = False


@dataclass
class SearchDepthAssessment:
    """Result of comparing actual execution with the assigned depth."""

    passed: bool
    depth: SearchDepth
    evidence_count: int
    retrieval_rounds: int
    source_families: list[str] = field(default_factory=list)
    gap_reflection_performed: bool = False
    counterevidence_checked: bool = False
    failures: list[str] = field(default_factory=list)

    @property
    def summary(self) -> str:
        if self.passed:
            return (
                f"{self.depth.value} contract satisfied: "
                f"{self.evidence_count} evidence items, "
                f"{self.retrieval_rounds} retrieval rounds, "
                f"{len(self.source_families)} source families"
            )
        return f"{self.depth.value} contract not satisfied: {'; '.join(self.failures)}"


class SearchDepthController:
    """Verify that a task performed the retrieval work its label promises."""

    POLICIES = {
        SearchDepth.QUICK: SearchDepthPolicy(0, 0, 0),
        SearchDepth.STANDARD: SearchDepthPolicy(2, 1, 2),
        SearchDepth.DEEP: SearchDepthPolicy(
            3, 2, 2, require_gap_reflection=True
        ),
        SearchDepth.EVIDENCE_AUDIT: SearchDepthPolicy(
            3,
            2,
            2,
            require_gap_reflection=True,
            require_counterevidence=True,
        ),
    }

    RETRIEVAL_STEPS = {
        "loaded routed files",
        "searched vault",
        "applied selected source",
        "loaded overview baseline evidence",
        "fallback source preload",
        "loaded evidence",
    }

    COUNTEREVIDENCE_TERMS = (
        "counterevidence",
        "counter evidence",
        "contrary evidence",
        "contradict",
        "反证",
        "相反证据",
        "不支持",
        "证据冲突",
    )

    def assess(
        self,
        record: ResearchRecord,
        research_trace: Iterable[dict[str, Any]] | None = None,
        answer: str = "",
    ) -> SearchDepthAssessment:
        """Assess actual retrieval execution without making network calls."""
        policy = self.POLICIES[record.search_depth]
        trace = list(research_trace or [])
        source_families = sorted(self._source_families(trace))
        retrieval_rounds = self._retrieval_rounds(trace)
        evidence_count = len(set(record.selected_evidence))
        gap_reflection = record.gap_checks_performed > 0
        counterevidence = self._counterevidence_checked(record, trace, answer)

        failures: list[str] = []
        if evidence_count < policy.min_evidence:
            failures.append(f"evidence {evidence_count}/{policy.min_evidence}")
        if retrieval_rounds < policy.min_retrieval_rounds:
            failures.append(
                f"retrieval rounds {retrieval_rounds}/{policy.min_retrieval_rounds}"
            )
        if len(source_families) < policy.min_source_families:
            failures.append(
                f"source families {len(source_families)}/{policy.min_source_families}"
            )
        if policy.require_gap_reflection and not gap_reflection:
            failures.append("gap reflection missing")
        if policy.require_counterevidence and not counterevidence:
            failures.append("counterevidence check missing")

        return SearchDepthAssessment(
            passed=not failures,
            depth=record.search_depth,
            evidence_count=evidence_count,
            retrieval_rounds=retrieval_rounds,
            source_families=source_families,
            gap_reflection_performed=gap_reflection,
            counterevidence_checked=counterevidence,
            failures=failures,
        )

    def _retrieval_rounds(self, trace: list[dict[str, Any]]) -> int:
        rounds = 0
        for entry in trace:
            step = str(entry.get("step", "")).strip().lower()
            detail = str(entry.get("detail", "")).lower()
            if step in self.RETRIEVAL_STEPS:
                rounds += 1
            elif step.startswith("agent hop") and any(
                action in detail
                for action in ("action=load_more", "action=load_sources")
            ):
                rounds += 1
        return rounds

    def _source_families(self, trace: list[dict[str, Any]]) -> set[str]:
        families: set[str] = set()
        for entry in trace:
            step = str(entry.get("step", "")).lower()
            detail = str(entry.get("detail", "")).lower()
            if "searched vault" in step or "scope=raw" in detail:
                families.add("source_cards")
            for item in entry.get("items", []) or []:
                path = str(item.get("file", "")).lower()
                source_id = str(item.get("source_id") or item.get("id") or "")
                if source_id.startswith("src-") or path.startswith("raw/"):
                    families.add("source_cards")
                elif path.startswith("topics/"):
                    families.add("topic_synthesis")
                elif path.startswith("system/"):
                    families.add("system_guidance")
                elif path.startswith("outputs/"):
                    families.add("prior_outputs")
            if any(name in detail for name in ("pubmed", "pmc", "crossref")):
                families.add("external_literature")
        return families

    def _counterevidence_checked(
        self,
        record: ResearchRecord,
        trace: list[dict[str, Any]],
        answer: str,
    ) -> bool:
        if record.excluded_evidence:
            return True
        searchable = " ".join(
            [answer]
            + [
                f"{entry.get('step', '')} {entry.get('detail', '')}"
                for entry in trace
            ]
        ).lower()
        return any(term in searchable for term in self.COUNTEREVIDENCE_TERMS)
