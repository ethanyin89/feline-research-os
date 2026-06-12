"""
Independent Verifier for Research Outputs.

Based on II-Thought principles:
- Performs independent verification of research outputs
- Checks species boundary compliance
- Validates evidence grounding
- Ensures quality standards before finalization
"""

import re
from dataclasses import dataclass
from typing import List, Optional, Tuple

from .schemas import (
    ResearchRecord,
    VerificationResult,
    VerifierStatus,
    SearchDepth,
    TaskType,
)


class Verifier:
    """
    Independent verification of research outputs.

    The verifier runs after the gap checker approves a draft,
    providing a final quality gate before output is finalized.
    """

    # Species boundary keywords that require flagging
    CROSS_SPECIES_TERMS = {
        "dog": ["dog", "canine", "犬"],
        "human": ["human", "人", "患者", "patient"],
        "mouse": ["mouse", "mice", "rodent", "小鼠", "大鼠"],
        "in_vitro": ["in vitro", "体外", "cell culture", "细胞培养"],
    }

    # Required warning phrases for cross-species content
    WARNING_PHRASES = [
        "外推", "extrapolat", "需注意", "caution", "注意",
        "不能直接", "cannot directly", "限制", "limitation",
        "跨物种", "cross-species", "非猫", "non-feline",
    ]

    # Evidence citation patterns
    CITATION_PATTERNS = [
        r"pmid[:\s]*\d+",
        r"doi[:\s]*10\.\d+",
        r"src-\w+-\d+",
        r"\d{4}\s*;\s*\d+",  # Journal citation format
        r"et\s+al\.?",
        r"文献[：:]\s*\[",
    ]

    def verify(self, record: ResearchRecord, final_output: str) -> ResearchRecord:
        """
        Perform independent verification of research output.

        Args:
            record: Research record with task context
            final_output: The finalized output text

        Returns:
            Updated ResearchRecord with verification results
        """
        # Run all verification checks
        results = []

        # 1. Species boundary check
        results.extend(self._verify_species_boundary(final_output, record))

        # 2. Evidence grounding check
        results.extend(self._verify_evidence_grounding(final_output, record))

        # 3. Task-specific completeness check
        results.extend(self._verify_task_completeness(final_output, record))

        # 4. Uncertainty disclosure check
        results.extend(self._verify_uncertainty_disclosure(final_output, record))

        # 5. Consistency check
        results.extend(self._verify_consistency(final_output, record))

        # Add all results to record
        for result in results:
            record.add_verification(result)

        # Compute overall status
        record.verifier_status = record.compute_verifier_status()

        return record

    def _verify_species_boundary(
        self, output: str, record: ResearchRecord
    ) -> List[VerificationResult]:
        """Verify species boundary compliance."""
        results = []
        output_lower = output.lower()

        for species, terms in self.CROSS_SPECIES_TERMS.items():
            for term in terms:
                if term.lower() in output_lower:
                    # Found cross-species reference, check for warning
                    has_warning = any(
                        wp.lower() in output_lower for wp in self.WARNING_PHRASES
                    )

                    if has_warning:
                        results.append(VerificationResult(
                            check_name=f"species_boundary_{species}",
                            passed=True,
                            message=f"Cross-species reference to {species} properly flagged",
                            severity="low",
                        ))
                    else:
                        results.append(VerificationResult(
                            check_name=f"species_boundary_{species}",
                            passed=False,
                            message=f"Cross-species reference to {species} without extrapolation warning",
                            severity="high",
                        ))
                    break  # One result per species type

        # If no cross-species references found, that's good
        if not results:
            results.append(VerificationResult(
                check_name="species_boundary",
                passed=True,
                message="No unmarked cross-species references found",
                severity="low",
            ))

        return results

    def _verify_evidence_grounding(
        self, output: str, record: ResearchRecord
    ) -> List[VerificationResult]:
        """Verify evidence citations are present and proper."""
        results = []
        output_lower = output.lower()

        # Check for citation presence
        has_citations = any(
            re.search(pattern, output_lower)
            for pattern in self.CITATION_PATTERNS
        )

        # Determine required citation level based on search depth
        if record.search_depth in [SearchDepth.DEEP, SearchDepth.EVIDENCE_AUDIT]:
            if not has_citations:
                results.append(VerificationResult(
                    check_name="evidence_grounding",
                    passed=False,
                    message="Deep research task requires evidence citations",
                    severity="critical" if record.search_depth == SearchDepth.EVIDENCE_AUDIT else "high",
                ))
            else:
                # Count approximate citations
                citation_count = sum(
                    len(re.findall(pattern, output_lower))
                    for pattern in self.CITATION_PATTERNS
                )

                min_required = 3 if record.search_depth == SearchDepth.EVIDENCE_AUDIT else 2

                if citation_count < min_required:
                    results.append(VerificationResult(
                        check_name="evidence_grounding",
                        passed=False,
                        message=f"Found ~{citation_count} citations, expected at least {min_required}",
                        severity="medium",
                    ))
                else:
                    results.append(VerificationResult(
                        check_name="evidence_grounding",
                        passed=True,
                        message=f"Adequate evidence citations found (~{citation_count})",
                        severity="low",
                    ))

        elif record.search_depth == SearchDepth.STANDARD:
            if not has_citations:
                results.append(VerificationResult(
                    check_name="evidence_grounding",
                    passed=False,
                    message="Standard research task should include at least one citation",
                    severity="medium",
                ))
            else:
                results.append(VerificationResult(
                    check_name="evidence_grounding",
                    passed=True,
                    message="Evidence citations found",
                    severity="low",
                ))
        else:
            # Quick tasks don't require citations
            results.append(VerificationResult(
                check_name="evidence_grounding",
                passed=True,
                message="Quick task - citations not required",
                severity="low",
            ))

        return results

    def _verify_task_completeness(
        self, output: str, record: ResearchRecord
    ) -> List[VerificationResult]:
        """Verify task-specific completeness requirements."""
        results = []
        output_lower = output.lower()

        if record.task_type == TaskType.PROTOCOL_DESIGN:
            required_sections = [
                ("purpose", ["目的", "purpose", "objective"]),
                ("subjects", ["动物", "animal", "subject", "cat", "feline"]),
                ("design", ["设计", "design", "group", "arm"]),
                ("endpoints", ["终点", "endpoint", "outcome"]),
            ]

            for section_name, keywords in required_sections:
                found = any(kw in output_lower for kw in keywords)
                results.append(VerificationResult(
                    check_name=f"protocol_{section_name}",
                    passed=found,
                    message=f"Protocol {section_name} section {'found' if found else 'missing'}",
                    severity="high" if not found else "low",
                ))

        elif record.task_type == TaskType.ENDPOINT_SELECTION:
            required_elements = [
                ("diagnosis_vs_efficacy", ["诊断", "diagnosis", "疗效", "efficacy"]),
                ("primary_secondary", ["主要", "primary", "次要", "secondary"]),
            ]

            for element_name, keywords in required_elements:
                found = any(kw in output_lower for kw in keywords)
                results.append(VerificationResult(
                    check_name=f"endpoint_{element_name}",
                    passed=found,
                    message=f"Endpoint {element_name} consideration {'addressed' if found else 'missing'}",
                    severity="medium" if not found else "low",
                ))

        elif record.task_type == TaskType.PK_DESIGN:
            pk_elements = [
                ("sampling", ["采血", "sampling", "time point"]),
                ("analysis", ["分析", "analysis", "lc-ms"]),
            ]

            for element_name, keywords in pk_elements:
                found = any(kw in output_lower for kw in keywords)
                results.append(VerificationResult(
                    check_name=f"pk_{element_name}",
                    passed=found,
                    message=f"PK {element_name} {'specified' if found else 'missing'}",
                    severity="high" if not found else "low",
                ))

        else:
            # Generic completeness check
            results.append(VerificationResult(
                check_name="task_completeness",
                passed=True,
                message="Task type does not require specific structure verification",
                severity="low",
            ))

        return results

    def _verify_uncertainty_disclosure(
        self, output: str, record: ResearchRecord
    ) -> List[VerificationResult]:
        """Verify that uncertainties are properly disclosed."""
        results = []
        output_lower = output.lower()

        # Uncertainty indicators
        uncertainty_terms = [
            "不确定", "uncertainty", "uncertain",
            "局限", "limitation", "limited",
            "需要更多", "further research", "more research",
            "证据不足", "insufficient evidence",
            "可能", "may", "might", "possibly", "perhaps",
            "初步", "preliminary", "tentative",
        ]

        has_uncertainty = any(term in output_lower for term in uncertainty_terms)

        # Deep tasks must disclose uncertainties
        if record.search_depth in [SearchDepth.DEEP, SearchDepth.EVIDENCE_AUDIT]:
            if not has_uncertainty:
                results.append(VerificationResult(
                    check_name="uncertainty_disclosure",
                    passed=False,
                    message="Deep research should acknowledge limitations or uncertainties",
                    severity="medium",
                ))
            else:
                results.append(VerificationResult(
                    check_name="uncertainty_disclosure",
                    passed=True,
                    message="Uncertainties/limitations properly disclosed",
                    severity="low",
                ))
        else:
            # Not required for quick/standard tasks
            results.append(VerificationResult(
                check_name="uncertainty_disclosure",
                passed=True,
                message="Uncertainty disclosure not required for this search depth",
                severity="low",
            ))

        return results

    def _verify_consistency(
        self, output: str, record: ResearchRecord
    ) -> List[VerificationResult]:
        """Verify internal consistency of the output."""
        results = []

        # Check if the output addresses the original request
        request_lower = record.user_request.lower()
        output_lower = output.lower()

        # Extract key terms from request
        request_terms = set(re.findall(r'\b\w+\b', request_lower))
        # Filter to meaningful terms (length > 2)
        request_terms = {t for t in request_terms if len(t) > 2}

        # Check overlap
        output_terms = set(re.findall(r'\b\w+\b', output_lower))
        overlap = request_terms.intersection(output_terms)

        overlap_ratio = len(overlap) / len(request_terms) if request_terms else 1.0

        if overlap_ratio < 0.3:
            results.append(VerificationResult(
                check_name="request_relevance",
                passed=False,
                message="Output may not adequately address the original request",
                severity="high",
            ))
        else:
            results.append(VerificationResult(
                check_name="request_relevance",
                passed=True,
                message="Output addresses the original request",
                severity="low",
            ))

        # Check for contradictions (simple heuristic)
        contradiction_pairs = [
            ("是", "不是"),
            ("可以", "不可以"),
            ("有效", "无效"),
            ("推荐", "不推荐"),
            ("should", "should not"),
            ("effective", "ineffective"),
            ("recommended", "not recommended"),
        ]

        has_contradictions = False
        for term1, term2 in contradiction_pairs:
            if term1 in output_lower and term2 in output_lower:
                # This is not necessarily a contradiction - could be comparing options
                # Just flag for review
                has_contradictions = True
                break

        if has_contradictions:
            results.append(VerificationResult(
                check_name="internal_consistency",
                passed=True,  # Pass but flag
                message="Contains contrasting statements - verify context is clear",
                severity="medium",
            ))
        else:
            results.append(VerificationResult(
                check_name="internal_consistency",
                passed=True,
                message="No obvious contradictions detected",
                severity="low",
            ))

        return results

    def quick_verify(self, output: str, record: ResearchRecord) -> bool:
        """
        Quick verification check without full analysis.

        Returns True if output likely passes verification.
        Use for preliminary checks before full verification.
        """
        output_lower = output.lower()

        # Quick checks
        # 1. Minimum length
        if len(output) < 100:
            return False

        # 2. Has some structure (headers, lists)
        if not any(marker in output for marker in ["#", "-", "1.", "•", "："]):
            return False

        # 3. For deep tasks, has citations
        if record.search_depth in [SearchDepth.DEEP, SearchDepth.EVIDENCE_AUDIT]:
            has_citations = any(
                re.search(pattern, output_lower)
                for pattern in self.CITATION_PATTERNS
            )
            if not has_citations:
                return False

        return True

    def format_verification_report(self, record: ResearchRecord) -> str:
        """
        Generate a human-readable verification report.

        Args:
            record: Research record with verification results

        Returns:
            Formatted markdown report
        """
        lines = [
            "# Verification Report",
            "",
            f"**Record ID:** {record.record_id}",
            f"**Overall Status:** {record.verifier_status.value}",
            "",
            "## Verification Results",
            "",
            "| Check | Status | Severity | Message |",
            "|-------|--------|----------|---------|",
        ]

        for result in record.verification_results:
            status = "PASS" if result.passed else "FAIL"
            lines.append(
                f"| {result.check_name} | {status} | {result.severity} | {result.message} |"
            )

        lines.extend([
            "",
            "## Summary",
            "",
        ])

        passed_count = sum(1 for r in record.verification_results if r.passed)
        total_count = len(record.verification_results)

        lines.append(f"**Passed:** {passed_count}/{total_count} checks")

        # List failures
        failures = [r for r in record.verification_results if not r.passed]
        if failures:
            lines.extend([
                "",
                "### Issues to Address",
                "",
            ])
            for f in failures:
                lines.append(f"- **{f.check_name}** ({f.severity}): {f.message}")

        # Add recommendations based on status
        lines.extend([
            "",
            "## Recommendation",
            "",
        ])

        if record.verifier_status == VerifierStatus.PASSED:
            lines.append("Output has passed all verification checks and is ready for use.")
        elif record.verifier_status == VerifierStatus.NEEDS_HUMAN_REVIEW:
            lines.append("Output requires human review before finalization. Please address the flagged issues.")
        elif record.verifier_status == VerifierStatus.FAILED:
            lines.append("Output has failed critical verification checks and should not be used without revision.")
        else:
            lines.append("Verification is pending or incomplete.")

        return "\n".join(lines)
