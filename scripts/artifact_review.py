#!/usr/bin/env python3
"""
scripts/artifact_review.py — Human review workflow for business artifacts.

Provides an inbox/promotion workflow where business artifacts go through
review before being marked as final. Tracks status (draft/review/approved)
and reviewer notes.

Usage:
    python scripts/artifact_review.py list
    python scripts/artifact_review.py list --status review
    python scripts/artifact_review.py submit outputs/business/ckd-brief.md
    python scripts/artifact_review.py review outputs/business/ckd-brief.md --approve
    python scripts/artifact_review.py review outputs/business/ckd-brief.md --reject --note "Missing sources"
    python scripts/artifact_review.py promote outputs/business/ckd-brief.md

Usage (imported):
    from artifact_review import ArtifactReviewQueue, submit_for_review
    queue = ArtifactReviewQueue()
    queue.submit("outputs/business/ckd-brief.md")
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional

VAULT_ROOT = Path(__file__).parent.parent
REVIEW_QUEUE_FILE = VAULT_ROOT / "system" / "indexes" / "artifact-review-queue.json"


@dataclass
class ReviewComment:
    """A comment on an artifact during review."""
    timestamp: str
    reviewer: str
    action: str  # submit, comment, approve, reject, promote
    note: str


@dataclass
class ArtifactReview:
    """Review state for a single artifact."""
    artifact_id: str
    artifact_path: str
    artifact_type: str  # opportunity_brief, endpoint_memo, claim_evidence, dossier
    disease: str
    status: str  # draft, review, approved, rejected, promoted
    submitted_at: str
    submitted_by: str
    reviewed_at: Optional[str]
    reviewed_by: Optional[str]
    promoted_at: Optional[str]
    promoted_to: Optional[str]
    comments: list[ReviewComment]
    tags: list[str]


class ArtifactReviewQueue:
    """Human review queue for business artifacts."""

    def __init__(self, queue_file: Path = REVIEW_QUEUE_FILE):
        self.queue_file = queue_file
        self.artifacts: list[ArtifactReview] = []
        self._load()

    def _load(self) -> None:
        """Load artifacts from JSON file."""
        if self.queue_file.exists():
            try:
                data = json.loads(self.queue_file.read_text(encoding="utf-8"))
                for item in data.get("artifacts", []):
                    comments = [ReviewComment(**c) for c in item.pop("comments", [])]
                    self.artifacts.append(ArtifactReview(**item, comments=comments))
            except (json.JSONDecodeError, TypeError):
                self.artifacts = []
        else:
            self.artifacts = []

    def _save(self) -> None:
        """Save artifacts to JSON file."""
        self.queue_file.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "last_updated": datetime.now().isoformat(),
            "total_artifacts": len(self.artifacts),
            "pending_review": sum(1 for a in self.artifacts if a.status == "review"),
            "artifacts": [
                {**asdict(a), "comments": [asdict(c) for c in a.comments]}
                for a in self.artifacts
            ],
        }
        self.queue_file.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def _generate_id(self, artifact_path: str) -> str:
        """Generate a unique artifact ID."""
        path = Path(artifact_path)
        base = path.stem.replace("-", "_")[:20]
        existing = [a for a in self.artifacts if a.artifact_id.startswith(f"ART-{base}")]
        return f"ART-{base}-{len(existing) + 1:02d}"

    def _detect_type(self, content: str, path: str) -> str:
        """Detect artifact type from content."""
        path_lower = path.lower()
        if "opportunity-brief" in path_lower or "opportunity brief" in content.lower()[:500]:
            return "opportunity_brief"
        if "endpoint" in path_lower or "endpoint" in content.lower()[:500]:
            return "endpoint_memo"
        if "claim" in path_lower or "claim evidence" in content.lower()[:500]:
            return "claim_evidence"
        if "dossier" in path_lower:
            return "dossier"
        return "unknown"

    def _detect_disease(self, content: str, path: str) -> str:
        """Detect disease from content or path."""
        diseases = ["ckd", "fip", "hcm", "ibd", "diabetes", "fcv", "obesity", "cancer"]
        path_lower = path.lower()
        for disease in diseases:
            if disease in path_lower:
                return disease.upper()
        content_lower = content.lower()[:1000]
        for disease in diseases:
            if disease in content_lower:
                return disease.upper()
        return "UNKNOWN"

    def submit(
        self,
        artifact_path: str,
        submitter: str = "system",
        tags: Optional[list[str]] = None,
    ) -> ArtifactReview:
        """Submit an artifact for review."""
        path = Path(artifact_path)
        if not path.exists():
            raise ValueError(f"Artifact not found: {artifact_path}")

        # Check if already submitted
        for artifact in self.artifacts:
            if artifact.artifact_path == str(path):
                return artifact

        content = path.read_text(encoding="utf-8")
        artifact_type = self._detect_type(content, artifact_path)
        disease = self._detect_disease(content, artifact_path)

        artifact = ArtifactReview(
            artifact_id=self._generate_id(artifact_path),
            artifact_path=str(path),
            artifact_type=artifact_type,
            disease=disease,
            status="review",
            submitted_at=datetime.now().isoformat(),
            submitted_by=submitter,
            reviewed_at=None,
            reviewed_by=None,
            promoted_at=None,
            promoted_to=None,
            comments=[
                ReviewComment(
                    timestamp=datetime.now().isoformat(),
                    reviewer=submitter,
                    action="submit",
                    note="Submitted for review",
                )
            ],
            tags=tags or [],
        )
        self.artifacts.append(artifact)
        self._save()
        return artifact

    def add_comment(
        self,
        artifact_id: str,
        reviewer: str,
        note: str,
    ) -> Optional[ArtifactReview]:
        """Add a review comment to an artifact."""
        for artifact in self.artifacts:
            if artifact.artifact_id == artifact_id:
                artifact.comments.append(ReviewComment(
                    timestamp=datetime.now().isoformat(),
                    reviewer=reviewer,
                    action="comment",
                    note=note,
                ))
                self._save()
                return artifact
        return None

    def review(
        self,
        artifact_id: str,
        reviewer: str,
        approve: bool,
        note: str = "",
    ) -> Optional[ArtifactReview]:
        """Review an artifact (approve or reject)."""
        for artifact in self.artifacts:
            if artifact.artifact_id == artifact_id:
                artifact.status = "approved" if approve else "rejected"
                artifact.reviewed_at = datetime.now().isoformat()
                artifact.reviewed_by = reviewer
                artifact.comments.append(ReviewComment(
                    timestamp=datetime.now().isoformat(),
                    reviewer=reviewer,
                    action="approve" if approve else "reject",
                    note=note or ("Approved" if approve else "Rejected"),
                ))
                self._save()
                return artifact
        return None

    def promote(
        self,
        artifact_id: str,
        target_dir: Optional[str] = None,
    ) -> Optional[ArtifactReview]:
        """Promote an approved artifact to final location."""
        for artifact in self.artifacts:
            if artifact.artifact_id == artifact_id:
                if artifact.status != "approved":
                    raise ValueError(f"Cannot promote artifact in status: {artifact.status}")

                # Determine promotion target
                if target_dir:
                    target = Path(target_dir)
                else:
                    target = VAULT_ROOT / "outputs" / "final"
                target.mkdir(parents=True, exist_ok=True)

                # Copy to final location
                src_path = Path(artifact.artifact_path)
                if not src_path.exists():
                    raise ValueError(f"Source artifact not found: {artifact.artifact_path}")

                dst_path = target / src_path.name
                dst_path.write_text(src_path.read_text(encoding="utf-8"), encoding="utf-8")

                artifact.status = "promoted"
                artifact.promoted_at = datetime.now().isoformat()
                artifact.promoted_to = str(dst_path)
                artifact.comments.append(ReviewComment(
                    timestamp=datetime.now().isoformat(),
                    reviewer="system",
                    action="promote",
                    note=f"Promoted to {dst_path}",
                ))
                self._save()
                return artifact
        return None

    def list_artifacts(
        self,
        status: Optional[str] = None,
        artifact_type: Optional[str] = None,
        disease: Optional[str] = None,
    ) -> list[ArtifactReview]:
        """List artifacts with optional filtering."""
        results = self.artifacts
        if status:
            results = [a for a in results if a.status == status]
        if artifact_type:
            results = [a for a in results if a.artifact_type == artifact_type]
        if disease:
            results = [a for a in results if a.disease.lower() == disease.lower()]
        return results

    def get_artifact(self, artifact_id: str) -> Optional[ArtifactReview]:
        """Get artifact by ID or path."""
        for artifact in self.artifacts:
            if artifact.artifact_id == artifact_id or artifact.artifact_path == artifact_id:
                return artifact
        return None

    def get_stats(self) -> dict:
        """Get queue statistics."""
        return {
            "total": len(self.artifacts),
            "draft": sum(1 for a in self.artifacts if a.status == "draft"),
            "review": sum(1 for a in self.artifacts if a.status == "review"),
            "approved": sum(1 for a in self.artifacts if a.status == "approved"),
            "rejected": sum(1 for a in self.artifacts if a.status == "rejected"),
            "promoted": sum(1 for a in self.artifacts if a.status == "promoted"),
            "by_type": {},
            "by_disease": {},
        }


def format_artifact_list(artifacts: list[ArtifactReview], verbose: bool = False) -> str:
    """Format a list of artifacts for display."""
    if not artifacts:
        return "No artifacts found."

    lines = [
        "",
        f"{'='*70}",
        f"  ARTIFACT REVIEW QUEUE ({len(artifacts)} items)",
        f"{'='*70}",
        "",
    ]

    status_icons = {
        "draft": "📝",
        "review": "🔍",
        "approved": "✅",
        "rejected": "❌",
        "promoted": "🚀",
    }

    for artifact in artifacts:
        icon = status_icons.get(artifact.status, "❓")
        path = Path(artifact.artifact_path)
        lines.append(f"{icon} {artifact.artifact_id} | {artifact.disease} | {path.name[:40]}...")
        lines.append(f"   Type: {artifact.artifact_type} | Status: {artifact.status}")

        if verbose:
            lines.append(f"   Submitted: {artifact.submitted_at} by {artifact.submitted_by}")
            if artifact.reviewed_at:
                lines.append(f"   Reviewed: {artifact.reviewed_at} by {artifact.reviewed_by}")
            if artifact.comments:
                last_comment = artifact.comments[-1]
                lines.append(f"   Last action: {last_comment.action} - {last_comment.note[:50]}...")
            lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Human review workflow for business artifacts.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list command
    list_parser = subparsers.add_parser("list", help="List artifacts in review queue")
    list_parser.add_argument("--status", "-s", choices=["draft", "review", "approved", "rejected", "promoted"], help="Filter by status")
    list_parser.add_argument("--type", "-t", choices=["opportunity_brief", "endpoint_memo", "claim_evidence", "dossier"], help="Filter by type")
    list_parser.add_argument("--disease", "-d", help="Filter by disease")
    list_parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed info")

    # submit command
    submit_parser = subparsers.add_parser("submit", help="Submit artifact for review")
    submit_parser.add_argument("path", help="Path to artifact file")
    submit_parser.add_argument("--submitter", "-s", default="cli", help="Submitter name")
    submit_parser.add_argument("--tags", "-t", nargs="+", help="Tags for the artifact")

    # review command
    review_parser = subparsers.add_parser("review", help="Review an artifact")
    review_parser.add_argument("artifact_id", help="Artifact ID or path")
    review_parser.add_argument("--approve", "-a", action="store_true", help="Approve the artifact")
    review_parser.add_argument("--reject", "-r", action="store_true", help="Reject the artifact")
    review_parser.add_argument("--note", "-n", default="", help="Review note")
    review_parser.add_argument("--reviewer", default="cli", help="Reviewer name")

    # comment command
    comment_parser = subparsers.add_parser("comment", help="Add a comment to an artifact")
    comment_parser.add_argument("artifact_id", help="Artifact ID")
    comment_parser.add_argument("note", help="Comment text")
    comment_parser.add_argument("--reviewer", default="cli", help="Reviewer name")

    # promote command
    promote_parser = subparsers.add_parser("promote", help="Promote approved artifact to final")
    promote_parser.add_argument("artifact_id", help="Artifact ID or path")
    promote_parser.add_argument("--target", "-t", help="Target directory")

    # stats command
    stats_parser = subparsers.add_parser("stats", help="Show queue statistics")

    args = parser.parse_args()
    queue = ArtifactReviewQueue()

    if args.command == "list":
        artifacts = queue.list_artifacts(
            status=args.status,
            artifact_type=getattr(args, 'type', None),
            disease=args.disease,
        )
        print(format_artifact_list(artifacts, verbose=args.verbose))

    elif args.command == "submit":
        try:
            artifact = queue.submit(
                artifact_path=args.path,
                submitter=args.submitter,
                tags=args.tags,
            )
            print(f"Submitted: {artifact.artifact_id} | {artifact.artifact_type} | {artifact.disease}")
            print(f"Status: {artifact.status}")
        except ValueError as e:
            print(f"Error: {e}")

    elif args.command == "review":
        if not args.approve and not args.reject:
            print("Error: Must specify --approve or --reject")
            return
        if args.approve and args.reject:
            print("Error: Cannot both approve and reject")
            return

        artifact = queue.get_artifact(args.artifact_id)
        if not artifact:
            print(f"Artifact not found: {args.artifact_id}")
            return

        result = queue.review(
            artifact_id=artifact.artifact_id,
            reviewer=args.reviewer,
            approve=args.approve,
            note=args.note,
        )
        if result:
            action = "Approved" if args.approve else "Rejected"
            print(f"{action}: {result.artifact_id}")
            print(f"Status: {result.status}")

    elif args.command == "comment":
        result = queue.add_comment(
            artifact_id=args.artifact_id,
            reviewer=args.reviewer,
            note=args.note,
        )
        if result:
            print(f"Comment added to: {result.artifact_id}")
        else:
            print(f"Artifact not found: {args.artifact_id}")

    elif args.command == "promote":
        artifact = queue.get_artifact(args.artifact_id)
        if not artifact:
            print(f"Artifact not found: {args.artifact_id}")
            return

        try:
            result = queue.promote(
                artifact_id=artifact.artifact_id,
                target_dir=args.target,
            )
            if result:
                print(f"Promoted: {result.artifact_id}")
                print(f"Destination: {result.promoted_to}")
        except ValueError as e:
            print(f"Error: {e}")

    elif args.command == "stats":
        stats = queue.get_stats()
        print(f"""
Artifact Review Queue Statistics
================================
Total artifacts: {stats['total']}
Draft: {stats['draft']}
Pending review: {stats['review']}
Approved: {stats['approved']}
Rejected: {stats['rejected']}
Promoted: {stats['promoted']}
""")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
