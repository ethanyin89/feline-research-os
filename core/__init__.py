"""
Feline Research OS Core Module

Six-layer architecture implementation:
- Layer 1: Human-in-the-Loop Workspace (Streamlit UI)
- Layer 2: Professional Team Mode (Agent roles)
- Layer 3: Research Pipeline (Query → Search → Synthesize)
- Layer 4: Research Record (Durable task records)
- Layer 5: Retrieval Memory (Evidence card search)
- Layer 6: Data Quality & Verification (Species/evidence checks)
"""

from .schemas import (
    ResearchRecord,
    EvidenceCard,
    TaskType,
    SpeciesType,
    EvidenceStrength,
    VerificationResult,
    VerifierStatus,
    SearchDepth,
)

from .record_store import RecordStore
from .evidence_card import EvidenceCardStore
from .task_evaluator import TaskEvaluator
from .search_depth_controller import (
    SearchDepthAssessment,
    SearchDepthController,
    SearchDepthPolicy,
)
from .gap_checker import GapChecker
from .verifier import Verifier
from .claim_promotion import (
    ResearchClaim,
    ClaimValidationResult,
    PromotionDraft,
    extract_claim_candidates,
    build_promotion_draft,
)
from .validated_claim_store import (
    ValidatedClaim,
    PromotionManifest,
    ValidatedClaimStore,
)

__all__ = [
    # Schemas
    "ResearchRecord",
    "EvidenceCard",
    "TaskType",
    "SpeciesType",
    "EvidenceStrength",
    "VerificationResult",
    "VerifierStatus",
    "SearchDepth",
    # Stores
    "RecordStore",
    "EvidenceCardStore",
    # Pipeline
    "TaskEvaluator",
    "SearchDepthPolicy",
    "SearchDepthAssessment",
    "SearchDepthController",
    "GapChecker",
    "Verifier",
    # Claim promotion
    "ResearchClaim",
    "ClaimValidationResult",
    "PromotionDraft",
    "extract_claim_candidates",
    "build_promotion_draft",
    "ValidatedClaim",
    "PromotionManifest",
    "ValidatedClaimStore",
]
