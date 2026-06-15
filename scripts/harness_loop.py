"""
Harness Loop integration for the Streamlit app.

Wraps query processing with the Feline-RALPH harness loop:
1. TaskEvaluator: Classify query and assign search depth
2. GapChecker: Check draft for completeness gaps
3. Verifier: Independent verification before finalization
4. RecordStore: Save durable research record
"""

import sys
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

# Add parent directory for core imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import (
    RecordStore,
    TaskEvaluator,
    SearchDepthController,
    SearchDepthAssessment,
    GapChecker,
    Verifier,
    ResearchRecord,
    TaskType,
    SearchDepth,
    VerificationResult,
    VerifierStatus,
)
from core.schemas import RetrievalEvent, SourceSnapshot


class HarnessLoop:
    """
    Integrates the harness loop into query processing.

    The harness loop ensures:
    - Complex tasks get appropriate search depth
    - Drafts are checked for gaps before finalization
    - Outputs are independently verified
    - Research records are saved for future reference
    """

    def __init__(self, vault_root: Path):
        self.vault_root = vault_root
        self.evaluator = TaskEvaluator()
        self.search_depth_controller = SearchDepthController()
        self.gap_checker = GapChecker()
        self.verifier = Verifier()
        self.record_store = RecordStore(vault_root / "system" / "research-records")

    def evaluate_query(
        self, query: str, explicit_search_depth: Optional[str] = None
    ) -> ResearchRecord:
        """
        Evaluate a query and create an initial research record.

        Args:
            query: User's research question
            explicit_search_depth: Optional override for search depth (quick/standard/deep/evidence_audit)

        Returns:
            Initialized ResearchRecord with task evaluation
        """
        record = self.evaluator.create_record(query)

        # Override search depth if explicitly specified
        if explicit_search_depth:
            depth_map = {
                "quick": SearchDepth.QUICK,
                "standard": SearchDepth.STANDARD,
                "deep": SearchDepth.DEEP,
                "evidence_audit": SearchDepth.EVIDENCE_AUDIT,
            }
            if explicit_search_depth in depth_map:
                record.search_depth = depth_map[explicit_search_depth]
                record.add_decision(f"Search depth overridden to: {explicit_search_depth}")

        return record

    def check_gaps(
        self, record: ResearchRecord, draft: str
    ) -> tuple[bool, List[str], str]:
        """
        Check a draft for gaps.

        Args:
            record: Research record with task context
            draft: Current draft answer

        Returns:
            Tuple of (has_critical_gaps, gap_descriptions, recommendation)
        """
        result = self.gap_checker.check(record, draft)

        # Update record
        record.gap_checks_performed += 1

        gap_descriptions = [
            f"[{g.severity}] {g.category}: {g.description}"
            for g in result.gaps
        ]

        return (
            result.has_critical_gaps or result.has_high_gaps,
            gap_descriptions,
            result.recommendation,
        )

    def verify_answer(
        self, record: ResearchRecord, final_answer: str
    ) -> tuple[VerifierStatus, List[str]]:
        """
        Verify a final answer.

        Args:
            record: Research record with task context
            final_answer: The finalized answer text

        Returns:
            Tuple of (verification_status, verification_messages)
        """
        record = self.verifier.verify(record, final_answer)

        messages = [
            f"{'✓' if r.passed else '✗'} {r.check_name}: {r.message}"
            for r in record.verification_results
        ]

        return record.verifier_status, messages

    def save_record(self, record: ResearchRecord) -> Path:
        """
        Save a research record.

        Args:
            record: Research record to save

        Returns:
            Path to saved record
        """
        return self.record_store.save(record)

    def finalize_record(
        self,
        record: ResearchRecord,
        answer: str,
        source_ids: List[str],
        disease: str,
        research_trace: Optional[List[dict]] = None,
        loaded_source_ids: Optional[List[str]] = None,
        retrieval_events: Optional[List[RetrievalEvent]] = None,
        source_snapshots: Optional[List[SourceSnapshot]] = None,
    ) -> tuple[ResearchRecord, bool, List[str], str, SearchDepthAssessment]:
        """
        Populate a record from the current query result without persisting it.

        Returns:
            Tuple of record, has_gaps, gap_descriptions, recommendation, depth assessment.
        """
        record.disease = disease
        record.selected_evidence = list(dict.fromkeys(loaded_source_ids or source_ids))
        record.draft_versions = 1
        
        if retrieval_events:
            record.retrieval_events = retrieval_events
        if source_snapshots:
            record.source_snapshots = source_snapshots

        has_gaps, gap_descriptions, recommendation = self.check_gaps(record, answer)
        depth_assessment = self.search_depth_controller.assess(
            record=record,
            research_trace=research_trace,
            answer=answer,
        )
        record.add_verification(VerificationResult(
            check_name="search_depth_contract",
            passed=depth_assessment.passed,
            message=depth_assessment.summary,
            severity=(
                "critical"
                if record.search_depth == SearchDepth.EVIDENCE_AUDIT
                else "high"
            ),
        ))

        if record.search_depth == SearchDepth.QUICK:
            record.verifier_status = VerifierStatus.PASSED
            record.final_answer = answer
            return record, False, [], "finalize", depth_assessment

        if not has_gaps and depth_assessment.passed:
            status, _messages = self.verify_answer(record, answer)
            record.final_answer = answer
            record.verifier_status = status
        else:
            record.verifier_status = (
                VerifierStatus.FAILED
                if (
                    record.search_depth == SearchDepth.EVIDENCE_AUDIT
                    and not depth_assessment.passed
                )
                else VerifierStatus.NEEDS_HUMAN_REVIEW
            )
            if not depth_assessment.passed:
                gap_descriptions = gap_descriptions + [depth_assessment.summary]

        return record, has_gaps, gap_descriptions, recommendation, depth_assessment

    def process_query_result(
        self,
        record: ResearchRecord,
        answer: str,
        source_ids: List[str],
        disease: str,
        question_type: str,
        research_trace: Optional[List[dict]] = None,
        loaded_source_ids: Optional[List[str]] = None,
        retrieval_events: Optional[List[RetrievalEvent]] = None,
        source_snapshots: Optional[List[SourceSnapshot]] = None,
    ) -> Dict[str, Any]:
        """
        Process a query result through the harness loop.

        This is called after the main query processing returns.
        It checks gaps, verifies the answer, and saves the record.

        Args:
            record: Research record created during query evaluation
            answer: The generated answer
            source_ids: Source IDs used in the answer
            disease: Detected disease
            question_type: Question type classification

        Returns:
            Dictionary with harness loop results
        """
        finalized_record, has_gaps, gap_descriptions, recommendation, depth_assessment = self.finalize_record(
            record=record,
            answer=answer,
            source_ids=source_ids,
            disease=disease,
            research_trace=research_trace,
            loaded_source_ids=loaded_source_ids,
            retrieval_events=retrieval_events,
            source_snapshots=source_snapshots,
        )

        messages = [
            f"{'✓' if result.passed else '✗'} {result.check_name}: {result.message}"
            for result in finalized_record.verification_results
        ]

        return {
            "record_id": finalized_record.record_id,
            "record": finalized_record,
            "saved": False,
            "task_type": finalized_record.task_type.value,
            "search_depth": finalized_record.search_depth.value,
            "has_gaps": has_gaps,
            "gap_descriptions": gap_descriptions if has_gaps else [],
            "verification_status": finalized_record.verifier_status.value,
            "verification_messages": messages,
            "recommendation": recommendation,
            "search_depth_satisfied": depth_assessment.passed,
            "search_depth_failures": depth_assessment.failures,
        }


def get_harness_loop(vault_root: Path) -> HarnessLoop:
    """Get a HarnessLoop instance for the vault."""
    return HarnessLoop(vault_root)


def format_harness_summary(result: Dict[str, Any]) -> str:
    """
    Format a harness loop result for display.

    Args:
        result: Harness loop result dictionary

    Returns:
        Formatted summary string
    """
    status_icons = {
        "passed": "✓",
        "failed": "✗",
        "needs_human_review": "⚠",
        "pending": "○",
    }

    icon = status_icons.get(result["verification_status"], "?")
    lines = [
        f"**Record:** `{result['record_id']}`",
        f"**Task:** {result['task_type']} | **Depth:** {result['search_depth']}",
        f"**Status:** {icon} {result['verification_status']}",
    ]

    if result.get("gap_descriptions"):
        lines.append("**Gaps:**")
        for gap in result["gap_descriptions"][:3]:
            lines.append(f"- {gap}")
        if len(result["gap_descriptions"]) > 3:
            lines.append(f"- ...and {len(result['gap_descriptions']) - 3} more")

    return "\n".join(lines)
