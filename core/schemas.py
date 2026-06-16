"""
Core data schemas for Feline Research OS.

Based on II (Intelligent Internet) design principles:
- Research Record: durable work records (CommonGround Kernel)
- Evidence Card: structured knowledge units (II-Thought)
- Task evaluation dimensions (II-Researcher)

Schema Version History:
- v1: Initial schema (2026-06-11)
- v2: Added RetrievalEvent, SourceSnapshot, ResearchClaim, schema_version (2026-06-13)
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict, Any
import hashlib
import json
import uuid

# Current schema version - increment when making breaking changes
SCHEMA_VERSION = 2


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


class PromotionStatus(Enum):
    """Claim promotion status for the knowledge flywheel."""
    RECORD_ONLY = "record_only"      # Saved but not considered for promotion
    CANDIDATE = "candidate"           # Selected for potential promotion
    VALIDATED = "validated"           # Passed promotion validation
    PROMOTED = "promoted"             # Applied to target page
    REJECTED = "rejected"             # Validation failed or user rejected


class FreshnessStatus(Enum):
    """Source freshness for promoted claims."""
    CURRENT = "current"               # Source fingerprints match
    STALE = "stale"                   # Source content changed
    SUPERSEDED = "superseded"         # Source replaced by newer version


class ClaimProvenance(Enum):
    """How a claim was derived from sources."""
    QUOTED_FACT = "quoted_fact"                       # Direct quote from source
    SOURCE_SUPPORTED_CONCLUSION = "source_supported_conclusion"  # Synthesized from sources
    INFERENCE = "inference"                           # LLM-generated inference


@dataclass
class RetrievalEvent:
    """
    Tracks an actual retrieval event during research.

    Gate 6A requirement: derive visible scope from actual events,
    never claim searches that didn't happen.
    """
    event_id: str
    timestamp: datetime
    engine: str                           # "vault", "pubmed", "crossref", etc.
    query: str                            # Actual query executed
    scope: str                            # "raw", "topics", "indexes", etc.
    candidate_count: int                  # Total results before filtering
    retained_ids: List[str]               # Source IDs kept
    excluded_ids: List[str] = field(default_factory=list)
    exclusion_reasons: Dict[str, str] = field(default_factory=dict)  # {source_id: reason}
    filters_applied: List[str] = field(default_factory=list)
    load_outcome: str = "success"         # "success", "partial", "failed"

    @classmethod
    def generate_id(cls) -> str:
        return f"re-{uuid.uuid4().hex[:8]}"

    def to_dict(self) -> dict:
        return {
            "event_id": self.event_id,
            "timestamp": self.timestamp.isoformat(),
            "engine": self.engine,
            "query": self.query,
            "scope": self.scope,
            "candidate_count": self.candidate_count,
            "retained_ids": self.retained_ids,
            "excluded_ids": self.excluded_ids,
            "exclusion_reasons": self.exclusion_reasons,
            "filters_applied": self.filters_applied,
            "load_outcome": self.load_outcome,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "RetrievalEvent":
        return cls(
            event_id=data["event_id"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            engine=data["engine"],
            query=data["query"],
            scope=data["scope"],
            candidate_count=data["candidate_count"],
            retained_ids=data.get("retained_ids", []),
            excluded_ids=data.get("excluded_ids", []),
            exclusion_reasons=data.get("exclusion_reasons", {}),
            filters_applied=data.get("filters_applied", []),
            load_outcome=data.get("load_outcome", "success"),
        )


@dataclass
class SourceSnapshot:
    """
    Captures source metadata at retrieval time.

    Used for:
    - Presentation: translates to user-facing labels
    - Validation: checks claim-fit before promotion
    - Freshness: fingerprint comparison for stale detection
    """
    source_id: str
    content_fingerprint: str              # SHA-256 of source content
    title: str
    canonical_url: Optional[str] = None
    doi: Optional[str] = None
    pmid: Optional[str] = None
    pmcid: Optional[str] = None

    # Quality dimensions (the 6 dimensions from the plan)
    source_family: str = "unknown"        # guideline, review, original_research, etc.
    study_type: str = "unknown"
    species: str = "unknown"
    applicability_boundary: str = ""
    extraction_depth: str = "unknown"     # deep_extracted, source_checked, abstract_weighted, title_only
    verification_status: str = "unknown"

    # Claim-fit policy
    safe_claim_types: List[str] = field(default_factory=list)
    prohibited_claim_types: List[str] = field(default_factory=list)
    decision_grade: str = "unknown"
    limitations: List[str] = field(default_factory=list)

    # Supersession tracking
    superseded_by: Optional[str] = None
    supersession_date: Optional[datetime] = None

    # Metadata
    publication_year: Optional[int] = None
    authors: List[str] = field(default_factory=list)
    journal: Optional[str] = None
    tags: List[str] = field(default_factory=list)

    # Researcher-facing metadata (enriched from external APIs)
    citation_count: Optional[int] = None
    impact_factor: Optional[float] = None
    abstract_text: str = ""
    methods_summary: str = ""
    reference_ids: List[str] = field(default_factory=list)
    metadata_enriched: Optional[str] = None  # ISO date of last enrichment

    @staticmethod
    def compute_fingerprint(content: str) -> str:
        """Compute SHA-256 fingerprint of content."""
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def to_dict(self) -> dict:
        return {
            "source_id": self.source_id,
            "content_fingerprint": self.content_fingerprint,
            "title": self.title,
            "canonical_url": self.canonical_url,
            "doi": self.doi,
            "pmid": self.pmid,
            "pmcid": self.pmcid,
            "source_family": self.source_family,
            "study_type": self.study_type,
            "species": self.species,
            "applicability_boundary": self.applicability_boundary,
            "extraction_depth": self.extraction_depth,
            "verification_status": self.verification_status,
            "safe_claim_types": self.safe_claim_types,
            "prohibited_claim_types": self.prohibited_claim_types,
            "decision_grade": self.decision_grade,
            "limitations": self.limitations,
            "superseded_by": self.superseded_by,
            "supersession_date": self.supersession_date.isoformat() if self.supersession_date else None,
            "publication_year": self.publication_year,
            "authors": self.authors,
            "journal": self.journal,
            "tags": self.tags,
            "citation_count": self.citation_count,
            "impact_factor": self.impact_factor,
            "abstract_text": self.abstract_text,
            "methods_summary": self.methods_summary,
            "reference_ids": self.reference_ids,
            "metadata_enriched": self.metadata_enriched,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "SourceSnapshot":
        return cls(
            source_id=data["source_id"],
            content_fingerprint=data["content_fingerprint"],
            title=data["title"],
            canonical_url=data.get("canonical_url"),
            doi=data.get("doi"),
            pmid=data.get("pmid"),
            pmcid=data.get("pmcid"),
            source_family=data.get("source_family", "unknown"),
            study_type=data.get("study_type", "unknown"),
            species=data.get("species", "unknown"),
            applicability_boundary=data.get("applicability_boundary", ""),
            extraction_depth=data.get("extraction_depth", "unknown"),
            verification_status=data.get("verification_status", "unknown"),
            safe_claim_types=data.get("safe_claim_types", []),
            prohibited_claim_types=data.get("prohibited_claim_types", []),
            decision_grade=data.get("decision_grade", "unknown"),
            limitations=data.get("limitations", []),
            superseded_by=data.get("superseded_by"),
            supersession_date=datetime.fromisoformat(data["supersession_date"]) if data.get("supersession_date") else None,
            publication_year=data.get("publication_year"),
            authors=data.get("authors", []),
            journal=data.get("journal"),
            tags=data.get("tags", []),
            citation_count=data.get("citation_count"),
            impact_factor=data.get("impact_factor"),
            abstract_text=data.get("abstract_text", ""),
            methods_summary=data.get("methods_summary", ""),
            reference_ids=data.get("reference_ids", []),
            metadata_enriched=data.get("metadata_enriched"),
        )


@dataclass
class ResearchClaim:
    """
    A single claim extracted from research output.

    The unit of selection, validation, promotion, and factual reuse.
    Gate 6B introduces claim selection; Gate 6C enables promotion.
    """
    claim_id: str
    text: str
    original_answer_span: str             # Exact text from the answer
    ordinal: int                          # Position in the answer
    source_ids: List[str]                 # Sources supporting this claim
    provenance: ClaimProvenance

    # Claim boundaries
    supported_use: str = ""               # What this claim can support
    boundary: str = ""                    # What this claim cannot establish

    # Selection and promotion
    selected_by_human: bool = False
    promotion_status: PromotionStatus = PromotionStatus.RECORD_ONLY
    freshness_status: FreshnessStatus = FreshnessStatus.CURRENT

    # Validation
    promotion_validation_results: List[Dict[str, Any]] = field(default_factory=list)

    # Target (for promoted claims)
    target_page: Optional[str] = None
    target_section: Optional[str] = None
    promotion_timestamp: Optional[datetime] = None

    @classmethod
    def generate_id(cls) -> str:
        return f"rc-{uuid.uuid4().hex[:8]}"

    def is_promotable(self) -> bool:
        """Check if this claim can be selected for promotion."""
        # Inference-only claims cannot be promoted
        if self.provenance == ClaimProvenance.INFERENCE:
            return False
        # Must have source mapping
        if not self.source_ids:
            return False
        return True

    def to_dict(self) -> dict:
        return {
            "claim_id": self.claim_id,
            "text": self.text,
            "original_answer_span": self.original_answer_span,
            "ordinal": self.ordinal,
            "source_ids": self.source_ids,
            "provenance": self.provenance.value,
            "supported_use": self.supported_use,
            "boundary": self.boundary,
            "selected_by_human": self.selected_by_human,
            "promotion_status": self.promotion_status.value,
            "freshness_status": self.freshness_status.value,
            "promotion_validation_results": self.promotion_validation_results,
            "target_page": self.target_page,
            "target_section": self.target_section,
            "promotion_timestamp": self.promotion_timestamp.isoformat() if self.promotion_timestamp else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchClaim":
        return cls(
            claim_id=data["claim_id"],
            text=data["text"],
            original_answer_span=data["original_answer_span"],
            ordinal=data["ordinal"],
            source_ids=data.get("source_ids", []),
            provenance=ClaimProvenance(data["provenance"]),
            supported_use=data.get("supported_use", ""),
            boundary=data.get("boundary", ""),
            selected_by_human=data.get("selected_by_human", False),
            promotion_status=PromotionStatus(data.get("promotion_status", "record_only")),
            freshness_status=FreshnessStatus(data.get("freshness_status", "current")),
            promotion_validation_results=data.get("promotion_validation_results", []),
            target_page=data.get("target_page"),
            target_section=data.get("target_section"),
            promotion_timestamp=datetime.fromisoformat(data["promotion_timestamp"]) if data.get("promotion_timestamp") else None,
        )


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

    Schema v2 additions (Gate 6A):
    - schema_version: enables forward-compatible migrations
    - title: user-editable record title
    - parent_record_id: for continuation chains
    - record_version: increments on updates
    - retrieval_events: actual search events (truthful scope)
    - source_snapshots: source metadata at retrieval time
    - research_claims: extracted claims for promotion (Gate 6B)
    """
    record_id: str
    timestamp: datetime
    user_request: str
    task_type: TaskType

    # Schema version for migrations
    schema_version: int = SCHEMA_VERSION

    # Task classification
    species: SpeciesType = SpeciesType.CAT
    disease: str = ""
    scope: str = ""

    # User-editable metadata (v2)
    title: str = ""                                    # Editable record title
    parent_record_id: Optional[str] = None             # For continuation chains
    record_version: int = 1                            # Increments on updates

    # Search depth (per II-Search)
    search_depth: SearchDepth = SearchDepth.STANDARD

    # Retrieval tracking (legacy, kept for v1 compatibility)
    retrieval_sources: List[str] = field(default_factory=list)
    search_queries: List[str] = field(default_factory=list)

    # Truthful retrieval (v2) - derived from actual events
    retrieval_events: List[RetrievalEvent] = field(default_factory=list)
    source_snapshots: List[SourceSnapshot] = field(default_factory=list)

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

    # Claims extracted from answer (v2, Gate 6B)
    research_claims: List[ResearchClaim] = field(default_factory=list)

    # Continuation
    next_steps: List[str] = field(default_factory=list)
    handoff_summary: str = ""

    # Persistence health (v2)
    persistence_status: str = "healthy"                # healthy, partial, reconciling
    last_saved: Optional[datetime] = None

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
            # Schema version for migrations
            "schema_version": self.schema_version,

            # Core fields
            "record_id": self.record_id,
            "timestamp": self.timestamp.isoformat(),
            "user_request": self.user_request,
            "task_type": self.task_type.value,
            "species": self.species.value,
            "disease": self.disease,
            "scope": self.scope,

            # v2 user-editable metadata
            "title": self.title,
            "parent_record_id": self.parent_record_id,
            "record_version": self.record_version,

            "search_depth": self.search_depth.value,

            # Legacy retrieval (v1 compatibility)
            "retrieval_sources": self.retrieval_sources,
            "search_queries": self.search_queries,

            # Truthful retrieval (v2)
            "retrieval_events": [e.to_dict() for e in self.retrieval_events],
            "source_snapshots": [s.to_dict() for s in self.source_snapshots],

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

            # v2 claims (Gate 6B)
            "research_claims": [c.to_dict() for c in self.research_claims],

            "next_steps": self.next_steps,
            "handoff_summary": self.handoff_summary,

            # v2 persistence health
            "persistence_status": self.persistence_status,
            "last_saved": self.last_saved.isoformat() if self.last_saved else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchRecord":
        """
        Create from dictionary with backward compatibility.

        Handles both v1 (no schema_version) and v2 records.
        """
        # Detect schema version (v1 records don't have this field)
        stored_version = data.get("schema_version", 1)

        record = cls(
            record_id=data["record_id"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            user_request=data["user_request"],
            schema_version=stored_version,
            task_type=TaskType(data["task_type"]),
            species=SpeciesType(data.get("species", "cat")),
            disease=data.get("disease", ""),
            scope=data.get("scope", ""),

            # v2 fields with defaults for v1 records
            title=data.get("title", ""),
            parent_record_id=data.get("parent_record_id"),
            record_version=data.get("record_version", 1),

            search_depth=SearchDepth(data.get("search_depth", "standard")),

            # Legacy retrieval
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

            # v2 persistence health
            persistence_status=data.get("persistence_status", "healthy"),
            last_saved=datetime.fromisoformat(data["last_saved"]) if data.get("last_saved") else None,
        )

        # Restore verification results
        for vr_data in data.get("verification_results", []):
            record.verification_results.append(VerificationResult(
                check_name=vr_data["check_name"],
                passed=vr_data["passed"],
                message=vr_data["message"],
                severity=vr_data.get("severity", "medium"),
            ))

        # Restore v2 retrieval events
        for event_data in data.get("retrieval_events", []):
            record.retrieval_events.append(RetrievalEvent.from_dict(event_data))

        # Restore v2 source snapshots
        for snapshot_data in data.get("source_snapshots", []):
            record.source_snapshots.append(SourceSnapshot.from_dict(snapshot_data))

        # Restore v2 research claims
        for claim_data in data.get("research_claims", []):
            record.research_claims.append(ResearchClaim.from_dict(claim_data))

        return record

    @classmethod
    def migrate_v1_to_v2(cls, record: "ResearchRecord") -> "ResearchRecord":
        """
        Migrate a v1 record to v2 schema.

        This is additive only - no data is lost.
        """
        if record.schema_version >= 2:
            return record

        # Generate title from user request if not set
        if not record.title:
            # Use first 50 chars of request as default title
            record.title = record.user_request[:50] + ("..." if len(record.user_request) > 50 else "")

        # Update schema version
        record.schema_version = 2

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
