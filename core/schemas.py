"""
Core data schemas for Feline Research OS.

Based on II (Intelligent Internet) design principles:
- Research Record: durable work records (CommonGround Kernel)
- Evidence Card: structured knowledge units (II-Thought)
- Task evaluation dimensions (II-Researcher)
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional
import json
import uuid


class TaskType(Enum):
    """Research task types with different depth requirements."""
    LITERATURE_REVIEW = "literature_review"
    PROTOCOL_DESIGN = "protocol_design"
    EVIDENCE_CHECK = "evidence_check"
    BIOMARKER_MAPPING = "biomarker_mapping"
    MODEL_EVALUATION = "model_evaluation"
    PK_DESIGN = "pk_design"
    ENDPOINT_SELECTION = "endpoint_selection"
    QUICK_EXPLANATION = "quick_explanation"
    OTHER = "other"


class SpeciesType(Enum):
    """Species classification for evidence grounding."""
    CAT = "cat"
    DOG = "dog"
    HUMAN = "human"
    MOUSE = "mouse"
    MIXED = "mixed"
    UNKNOWN = "unknown"


class EvidenceStrength(Enum):
    """Evidence quality levels."""
    HIGH = "high"        # Guideline, consensus, large RCT
    MEDIUM = "medium"    # Original research, case series
    LOW = "low"          # Case report, expert opinion, extrapolation


class VerifierStatus(Enum):
    """Verification outcome states."""
    PASSED = "passed"
    FAILED = "failed"
    NEEDS_HUMAN_REVIEW = "needs_human_review"
    PENDING = "pending"


class SearchDepth(Enum):
    """Search depth levels per II-Search principles."""
    QUICK = "quick"              # 0-1 searches, simple explanation
    STANDARD = "standard"        # 2-3 sources, at least 2 types
    DEEP = "deep"                # 2+ rounds with gap reflection
    EVIDENCE_AUDIT = "evidence_audit"  # Must include contrary evidence


class SourceType(Enum):
    """Evidence source types."""
    PUBMED = "pubmed"
    PMC = "pmc"
    GUIDELINE = "guideline"
    INTERNAL_NOTE = "internal_note"
    PROTOCOL = "protocol"
    UPLOADED_FILE = "uploaded_file"
    THESIS = "thesis"
    REVIEW = "review"


class UseCase(Enum):
    """Evidence use case categories."""
    DIAGNOSIS = "diagnosis"
    ENROLLMENT = "enrollment"
    EFFICACY_ENDPOINT = "efficacy_endpoint"
    SAFETY_MONITORING = "safety_monitoring"
    PROGNOSIS = "prognosis"
    MODEL_VALIDATION = "model_validation"


@dataclass
class EvidenceCard:
    """
    Structured knowledge unit for feline research.

    Each card represents one piece of citable evidence with:
    - Source provenance (where it came from)
    - Species boundary (is this cat-specific?)
    - Use case (what can this evidence support?)
    - Quality assessment (how strong is this evidence?)
    """
    evidence_card_id: str
    title: str
    source_type: SourceType
    source_id: str  # PMID, DOI, file path, etc.

    # Species boundary - critical for feline research
    species: SpeciesType

    # Domain classification
    disease: str
    study_type: str  # guideline, review, original_research, case_series, etc.

    # Content
    biomarkers: List[str] = field(default_factory=list)
    use_cases: List[UseCase] = field(default_factory=list)
    key_finding: str = ""
    limitations: str = ""

    # Quality
    evidence_strength: EvidenceStrength = EvidenceStrength.MEDIUM

    # Metadata
    last_reviewed: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def generate_id(cls) -> str:
        """Generate unique evidence card ID."""
        return f"ec-{uuid.uuid4().hex[:8]}"

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "evidence_card_id": self.evidence_card_id,
            "title": self.title,
            "source_type": self.source_type.value,
            "source_id": self.source_id,
            "species": self.species.value,
            "disease": self.disease,
            "study_type": self.study_type,
            "biomarkers": self.biomarkers,
            "use_cases": [uc.value for uc in self.use_cases],
            "key_finding": self.key_finding,
            "limitations": self.limitations,
            "evidence_strength": self.evidence_strength.value,
            "last_reviewed": self.last_reviewed.isoformat() if self.last_reviewed else None,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceCard":
        """Create from dictionary."""
        return cls(
            evidence_card_id=data["evidence_card_id"],
            title=data["title"],
            source_type=SourceType(data["source_type"]),
            source_id=data["source_id"],
            species=SpeciesType(data["species"]),
            disease=data["disease"],
            study_type=data["study_type"],
            biomarkers=data.get("biomarkers", []),
            use_cases=[UseCase(uc) for uc in data.get("use_cases", [])],
            key_finding=data.get("key_finding", ""),
            limitations=data.get("limitations", ""),
            evidence_strength=EvidenceStrength(data.get("evidence_strength", "medium")),
            last_reviewed=datetime.fromisoformat(data["last_reviewed"]) if data.get("last_reviewed") else None,
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else datetime.now(),
        )


@dataclass
class VerificationResult:
    """Result of a single verification check."""
    check_name: str
    passed: bool
    message: str
    severity: str = "medium"  # low, medium, high, critical


@dataclass
class ResearchRecord:
    """
    Durable research task record.

    Based on CommonGround Kernel principles:
    - Preserves not just answers but procedural context
    - Enables work to be continued, reviewed, and built upon
    - Captures decisions, uncertainties, and next steps
    """
    record_id: str
    timestamp: datetime
    user_request: str

    # Task classification
    task_type: TaskType
    species: SpeciesType = SpeciesType.CAT
    disease: str = ""
    scope: str = ""

    # Search depth (per II-Search)
    search_depth: SearchDepth = SearchDepth.STANDARD

    # Retrieval tracking
    retrieval_sources: List[str] = field(default_factory=list)
    search_queries: List[str] = field(default_factory=list)

    # Evidence selection
    selected_evidence: List[str] = field(default_factory=list)  # evidence_card_ids
    excluded_evidence: List[dict] = field(default_factory=list)  # [{id, reason}]

    # Decision log
    key_decisions: List[str] = field(default_factory=list)
    uncertainties: List[str] = field(default_factory=list)

    # Harness loop tracking
    draft_versions: int = 0
    gap_checks_performed: int = 0
    revisions_made: int = 0

    # Verification
    verification_results: List[VerificationResult] = field(default_factory=list)
    verifier_status: VerifierStatus = VerifierStatus.PENDING

    # Output
    output_path: str = ""
    final_answer: str = ""

    # Continuation
    next_steps: List[str] = field(default_factory=list)
    handoff_summary: str = ""

    @classmethod
    def generate_id(cls) -> str:
        """Generate unique record ID."""
        return f"rr-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:4]}"

    @classmethod
    def create(cls, user_request: str, task_type: TaskType, disease: str = "") -> "ResearchRecord":
        """Create a new research record."""
        return cls(
            record_id=cls.generate_id(),
            timestamp=datetime.now(),
            user_request=user_request,
            task_type=task_type,
            disease=disease,
        )

    def add_decision(self, decision: str) -> None:
        """Log a key decision made during research."""
        self.key_decisions.append(decision)

    def add_uncertainty(self, uncertainty: str) -> None:
        """Log an acknowledged uncertainty."""
        self.uncertainties.append(uncertainty)

    def add_verification(self, result: VerificationResult) -> None:
        """Add a verification result."""
        self.verification_results.append(result)

    def compute_verifier_status(self) -> VerifierStatus:
        """Compute overall verification status from individual results."""
        if not self.verification_results:
            return VerifierStatus.PENDING

        has_critical_failure = any(
            not r.passed and r.severity == "critical"
            for r in self.verification_results
        )
        has_high_failure = any(
            not r.passed and r.severity == "high"
            for r in self.verification_results
        )
        all_passed = all(r.passed for r in self.verification_results)

        if has_critical_failure:
            return VerifierStatus.FAILED
        elif has_high_failure:
            return VerifierStatus.NEEDS_HUMAN_REVIEW
        elif all_passed:
            return VerifierStatus.PASSED
        else:
            return VerifierStatus.NEEDS_HUMAN_REVIEW

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "record_id": self.record_id,
            "timestamp": self.timestamp.isoformat(),
            "user_request": self.user_request,
            "task_type": self.task_type.value,
            "species": self.species.value,
            "disease": self.disease,
            "scope": self.scope,
            "search_depth": self.search_depth.value,
            "retrieval_sources": self.retrieval_sources,
            "search_queries": self.search_queries,
            "selected_evidence": self.selected_evidence,
            "excluded_evidence": self.excluded_evidence,
            "key_decisions": self.key_decisions,
            "uncertainties": self.uncertainties,
            "draft_versions": self.draft_versions,
            "gap_checks_performed": self.gap_checks_performed,
            "revisions_made": self.revisions_made,
            "verification_results": [
                {"check_name": r.check_name, "passed": r.passed, "message": r.message, "severity": r.severity}
                for r in self.verification_results
            ],
            "verifier_status": self.verifier_status.value,
            "output_path": self.output_path,
            "final_answer": self.final_answer,
            "next_steps": self.next_steps,
            "handoff_summary": self.handoff_summary,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchRecord":
        """Create from dictionary."""
        record = cls(
            record_id=data["record_id"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            user_request=data["user_request"],
            task_type=TaskType(data["task_type"]),
            species=SpeciesType(data.get("species", "cat")),
            disease=data.get("disease", ""),
            scope=data.get("scope", ""),
            search_depth=SearchDepth(data.get("search_depth", "standard")),
            retrieval_sources=data.get("retrieval_sources", []),
            search_queries=data.get("search_queries", []),
            selected_evidence=data.get("selected_evidence", []),
            excluded_evidence=data.get("excluded_evidence", []),
            key_decisions=data.get("key_decisions", []),
            uncertainties=data.get("uncertainties", []),
            draft_versions=data.get("draft_versions", 0),
            gap_checks_performed=data.get("gap_checks_performed", 0),
            revisions_made=data.get("revisions_made", 0),
            verifier_status=VerifierStatus(data.get("verifier_status", "pending")),
            output_path=data.get("output_path", ""),
            final_answer=data.get("final_answer", ""),
            next_steps=data.get("next_steps", []),
            handoff_summary=data.get("handoff_summary", ""),
        )

        # Restore verification results
        for vr_data in data.get("verification_results", []):
            record.verification_results.append(VerificationResult(
                check_name=vr_data["check_name"],
                passed=vr_data["passed"],
                message=vr_data["message"],
                severity=vr_data.get("severity", "medium"),
            ))

        return record

    def to_markdown(self) -> str:
        """Generate markdown representation for human review."""
        lines = [
            f"# Research Record: {self.record_id}",
            "",
            f"**Created:** {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Task Type:** {self.task_type.value}",
            f"**Disease:** {self.disease}",
            f"**Search Depth:** {self.search_depth.value}",
            f"**Verifier Status:** {self.verifier_status.value}",
            "",
            "## User Request",
            "",
            self.user_request,
            "",
            "## Scope",
            "",
            self.scope or "_Not specified_",
            "",
        ]

        if self.retrieval_sources:
            lines.extend([
                "## Retrieval Sources",
                "",
                *[f"- {src}" for src in self.retrieval_sources],
                "",
            ])

        if self.selected_evidence:
            lines.extend([
                "## Selected Evidence",
                "",
                *[f"- {eid}" for eid in self.selected_evidence],
                "",
            ])

        if self.key_decisions:
            lines.extend([
                "## Key Decisions",
                "",
                *[f"- {d}" for d in self.key_decisions],
                "",
            ])

        if self.uncertainties:
            lines.extend([
                "## Uncertainties",
                "",
                *[f"- {u}" for u in self.uncertainties],
                "",
            ])

        if self.verification_results:
            lines.extend([
                "## Verification Results",
                "",
                "| Check | Status | Message |",
                "|-------|--------|---------|",
            ])
            for vr in self.verification_results:
                status = "PASS" if vr.passed else "FAIL"
                lines.append(f"| {vr.check_name} | {status} | {vr.message} |")
            lines.append("")

        if self.final_answer:
            lines.extend([
                "## Final Answer",
                "",
                self.final_answer,
                "",
            ])

        if self.next_steps:
            lines.extend([
                "## Next Steps",
                "",
                *[f"- {ns}" for ns in self.next_steps],
                "",
            ])

        if self.handoff_summary:
            lines.extend([
                "## Handoff Summary",
                "",
                self.handoff_summary,
                "",
            ])

        return "\n".join(lines)
