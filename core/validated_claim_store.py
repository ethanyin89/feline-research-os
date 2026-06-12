"""Validated claim persistence and freshness tracking.

This is the 6C storage layer:
- write promotion manifests after human confirmation
- keep validated claims separate from workflow records
- mark claims stale when source fingerprints change
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable, Optional

from .claim_promotion import PromotionDraft, ResearchClaim
from .source_metadata import find_source_card


@dataclass
class ValidatedClaim:
    claim_id: str
    record_id: str
    target_page: str
    text: str
    source_ids: list[str] = field(default_factory=list)
    source_fingerprints: dict[str, str] = field(default_factory=dict)
    provenance: str = "source_supported_conclusion"
    boundary: str = ""
    validated_at: str = ""
    validated_by: str = "human"
    status: str = "current"
    stale_reason: str = ""


@dataclass
class PromotionManifest:
    manifest_id: str
    record_id: str
    target_page: str
    validated_at: str
    validated_by: str
    claim_ids: list[str] = field(default_factory=list)
    source_ids: list[str] = field(default_factory=list)
    source_fingerprints: dict[str, str] = field(default_factory=dict)
    status: str = "validated"


class ValidatedClaimStore:
    """Persistent storage for validated claims."""

    def __init__(self, base_path: Path):
        self.base_path = Path(base_path).resolve()
        self.json_path = self.base_path / "json"
        self.markdown_path = self.base_path / "markdown"
        self.manifest_path = self.base_path / "manifests"
        self.stale_queue_path = self.base_path / "stale-queue.json"
        self.json_path.mkdir(parents=True, exist_ok=True)
        self.markdown_path.mkdir(parents=True, exist_ok=True)
        self.manifest_path.mkdir(parents=True, exist_ok=True)

    def _record_json_path(self, claim_id: str) -> Path:
        path = (self.json_path / f"{claim_id}.json").resolve()
        path.relative_to(self.json_path)
        return path

    def _record_markdown_path(self, claim_id: str) -> Path:
        path = (self.markdown_path / f"{claim_id}.md").resolve()
        path.relative_to(self.markdown_path)
        return path

    def _manifest_json_path(self, manifest_id: str) -> Path:
        path = (self.manifest_path / f"{manifest_id}.json").resolve()
        path.relative_to(self.manifest_path)
        return path

    def _manifest_markdown_path(self, manifest_id: str) -> Path:
        path = (self.manifest_path / f"{manifest_id}.md").resolve()
        path.relative_to(self.manifest_path)
        return path

    def _target_page_path(self, vault_root: Path, target_page: str) -> Path:
        normalized = target_page.strip().replace("\\", "/")
        if not normalized:
            raise ValueError("Target page is required.")
        if normalized.startswith("/") or ".." in Path(normalized).parts:
            raise ValueError("Target page must stay inside the vault.")
        if not normalized.startswith(("topics/", "system/indexes/")):
            raise ValueError("Target page is outside the allowed promotion areas.")
        path = (vault_root / normalized).resolve()
        path.relative_to(vault_root.resolve())
        return path

    @contextmanager
    def _locked(self, lock_name: str):
        lock_path = (self.base_path / f".{lock_name}.lock").resolve()
        with lock_path.open("a+", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    def _atomic_write_text(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        temp_path: Optional[Path] = None
        try:
            with tempfile.NamedTemporaryFile(
                "w",
                encoding="utf-8",
                dir=path.parent,
                prefix=f".{path.stem}-",
                suffix=".tmp",
                delete=False,
            ) as handle:
                temp_path = Path(handle.name)
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp_path, path)
            dir_fd = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        finally:
            if temp_path and temp_path.exists():
                temp_path.unlink()

    @staticmethod
    def _manifest_id(record_id: str, target_page: str) -> str:
        digest = hashlib.sha256(f"{record_id}:{target_page}".encode("utf-8")).hexdigest()[:12]
        return f"manifest-{digest}"

    @staticmethod
    def _fingerprint(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def source_fingerprints(self, vault_root: Path, source_ids: Iterable[str]) -> dict[str, str]:
        fingerprints: dict[str, str] = {}
        for source_id in source_ids:
            card_path = find_source_card(vault_root, source_id)
            if card_path is None:
                continue
            fingerprints[source_id] = self._fingerprint(card_path)
        return fingerprints

    def _load_claims(self) -> list[ValidatedClaim]:
        claims: list[ValidatedClaim] = []
        for path in sorted(self.json_path.glob("*.json")):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                claims.append(ValidatedClaim(**data))
            except (json.JSONDecodeError, TypeError, KeyError):
                continue
        return claims

    def _load_stale_queue(self) -> dict[str, dict[str, str]]:
        if not self.stale_queue_path.exists():
            return {}
        try:
            payload = json.loads(self.stale_queue_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}
        items = payload.get("items", [])
        return {
            item.get("claim_id", ""): item
            for item in items
            if isinstance(item, dict) and item.get("claim_id")
        }

    def _save_stale_queue(self, items: list[dict[str, str]]) -> None:
        self._atomic_write_text(
            self.stale_queue_path,
            json.dumps(
                {
                    "updated_at": datetime.now().isoformat(),
                    "items": items,
                },
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
        )

    def _render_claim_markdown(self, claim: ValidatedClaim, manifest: PromotionManifest) -> str:
        lines = [
            f"# Validated Claim: {claim.claim_id}",
            "",
            f"**Record:** `{claim.record_id}`",
            f"**Target:** `{claim.target_page}`",
            f"**Validated at:** {claim.validated_at}",
            f"**Status:** {claim.status}",
            "",
            "## Claim",
            "",
            claim.text,
            "",
            "## Sources",
            "",
        ]
        for source_id in claim.source_ids:
            fingerprint = claim.source_fingerprints.get(source_id, "unknown")
            lines.append(f"- `{source_id}` `{fingerprint}`")
        lines.extend(
            [
                "",
                "## Boundary",
                "",
                claim.boundary or "_Not specified_",
                "",
                "## Manifest",
                "",
                f"- Manifest ID: `{manifest.manifest_id}`",
                f"- Validated by: `{manifest.validated_by}`",
            ]
        )
        return "\n".join(lines).rstrip() + "\n"

    def _render_manifest_markdown(self, manifest: PromotionManifest) -> str:
        lines = [
            f"# Promotion Manifest: {manifest.manifest_id}",
            "",
            f"**Record:** `{manifest.record_id}`",
            f"**Target:** `{manifest.target_page}`",
            f"**Validated at:** {manifest.validated_at}",
            f"**Validated by:** `{manifest.validated_by}`",
            f"**Status:** `{manifest.status}`",
            "",
            "## Claims",
            "",
        ]
        for claim_id in manifest.claim_ids:
            lines.append(f"- `{claim_id}`")
        lines.extend(
            [
                "",
                "## Sources",
                "",
            ]
        )
        for source_id in manifest.source_ids:
            fingerprint = manifest.source_fingerprints.get(source_id, "unknown")
            lines.append(f"- `{source_id}` `{fingerprint}`")
        return "\n".join(lines).rstrip() + "\n"

    @staticmethod
    def _slugify(value: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
        return slug or "validated-claims"

    def _render_target_page(
        self,
        vault_root: Path,
        target_page: str,
        manifest: PromotionManifest,
        claims: list[ValidatedClaim],
    ) -> str:
        target_parts = Path(target_page).parts
        if len(target_parts) >= 3 and target_parts[0] == "topics":
            disease_label = target_parts[1]
        else:
            disease_label = Path(target_page).stem.replace("-validated-claims", "")
        disease = disease_label.replace("_", " ").strip()
        claim_ids = ", ".join(f"`{claim.claim_id}`" for claim in claims) or "_None_"
        source_ids = sorted({source_id for claim in claims for source_id in claim.source_ids})
        source_ids_text = ", ".join(f"`{source_id}`" for source_id in source_ids) or "_None_"
        frontmatter = [
            "---",
            f"id: validated-claims-{self._slugify(target_page)}",
            "type: synthesis",
            f"topic: {disease or 'general'}",
            "question_type: validated-claims",
            f"source_ids: [{', '.join(source_ids)}]",
            f"last_compiled_at: {datetime.now().date().isoformat()}",
            "verification_status: compiled",
            "decision_grade: no",
            "language_qa_status: not_applicable",
            "owner: codex",
            "status: active",
            f"promotion_manifest_id: {manifest.manifest_id}",
            "---",
            "",
            f"# Validated Claims for {disease or 'the selected topic'}",
            "",
            "This page is the write-back surface for human-confirmed claims.",
            "It keeps the promoted claims, their traceability, and the boundary for reuse in one place.",
            "",
            "## Promotion Manifest",
            "",
            f"- Manifest ID: `{manifest.manifest_id}`",
            f"- Record ID: `{manifest.record_id}`",
            f"- Validated at: `{manifest.validated_at}`",
            f"- Validated by: `{manifest.validated_by}`",
            f"- Target page: `{target_page}`",
            "",
            "## Promotion Judgment",
            "",
            "- repeated? `yes`",
            "- structurally clarifying? `yes`",
            "- evidence-safe enough for this layer? `yes`",
            "- smallest durable home: `validated-claims page`",
            "",
            "### Reason",
            "",
            "- the claims are now source-traced and selected for reuse",
            "- the target page can carry the stable traceability layer without re-deriving it in chat",
            "- the remaining uncertainty belongs below this page, not inside it",
            "",
            "### Decision",
            "",
            "- promote",
            "",
            "## Key-Claim Traceability",
            "",
        ]
        if claims:
            frontmatter.extend(
                [
                    "| ID | Claim | Level | Source ids | Boundary |",
                    "|---|---|---|---|---|",
                ]
            )
            for claim in claims:
                joined_sources = ", ".join(f"`{source_id}`" for source_id in claim.source_ids) or "_None_"
                boundary = claim.boundary.replace("|", "\\|")
                text = claim.text.replace("|", "\\|")
                frontmatter.append(
                    f"| `{claim.claim_id}` | {text} | `{claim.provenance}` | {joined_sources} | {boundary or '_Not specified_'} |"
                )
        else:
            frontmatter.append("_No current validated claims for this target yet._")

        frontmatter.extend(
            [
                "",
                "## Source Coverage",
                "",
                f"- Claims selected: {claim_ids}",
                f"- Sources covered: {source_ids_text}",
                "",
                "## Boundary",
                "",
                "Validated claims in this page are source-traced and current only.",
                "Stale claims are excluded from future retrieval and from this page.",
            ]
        )
        return "\n".join(frontmatter).rstrip() + "\n"

    def _write_target_page(
        self,
        vault_root: Path,
        target_page: str,
        manifest: PromotionManifest,
        claims: list[ValidatedClaim],
    ) -> Path:
        target_path = self._target_page_path(vault_root, target_page)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        content = self._render_target_page(vault_root, target_page, manifest, claims)
        self._atomic_write_text(target_path, content)
        return target_path

    def _write_claim(self, claim: ValidatedClaim, manifest: PromotionManifest) -> None:
        json_file = self._record_json_path(claim.claim_id)
        md_file = self._record_markdown_path(claim.claim_id)
        self._atomic_write_text(json_file, json.dumps(asdict(claim), indent=2, ensure_ascii=False) + "\n")
        self._atomic_write_text(md_file, self._render_claim_markdown(claim, manifest))

    def _write_manifest(self, manifest: PromotionManifest) -> None:
        json_file = self._manifest_json_path(manifest.manifest_id)
        md_file = self._manifest_markdown_path(manifest.manifest_id)
        self._atomic_write_text(json_file, json.dumps(asdict(manifest), indent=2, ensure_ascii=False) + "\n")
        self._atomic_write_text(md_file, self._render_manifest_markdown(manifest))

    def _refresh_stale_status(self, vault_root: Path) -> None:
        claims = self._load_claims()
        stale_items: list[dict[str, str]] = []
        for claim in claims:
            current_fingerprints = self.source_fingerprints(vault_root, claim.source_ids)
            if not claim.source_ids:
                claim.status = "stale"
                claim.stale_reason = "Missing source IDs"
            elif any(current_fingerprints.get(source_id) != claim.source_fingerprints.get(source_id) for source_id in claim.source_ids):
                claim.status = "stale"
                claim.stale_reason = "Source fingerprint changed"
            else:
                claim.status = "current"
                claim.stale_reason = ""
            self._atomic_write_text(
                self._record_json_path(claim.claim_id),
                json.dumps(asdict(claim), indent=2, ensure_ascii=False) + "\n",
            )
            if claim.status == "stale":
                stale_items.append(
                    {
                        "claim_id": claim.claim_id,
                        "record_id": claim.record_id,
                        "target_page": claim.target_page,
                        "stale_reason": claim.stale_reason,
                        "updated_at": datetime.now().isoformat(),
                }
                )
        self._save_stale_queue(stale_items)
        self._rebuild_target_pages(vault_root)

    def _rebuild_target_pages(self, vault_root: Path) -> None:
        current_claims = [claim for claim in self._load_claims() if claim.status == "current"]
        claims_by_target: dict[str, list[ValidatedClaim]] = {}
        manifests_by_target: dict[str, PromotionManifest] = {}
        for claim in current_claims:
            claims_by_target.setdefault(claim.target_page, []).append(claim)

        for claim_list in claims_by_target.values():
            claim_list.sort(key=lambda item: item.claim_id)

        for manifest_path in sorted(self.manifest_path.glob("*.json")):
            try:
                manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
                manifest = PromotionManifest(**manifest_data)
            except (json.JSONDecodeError, TypeError, KeyError):
                continue
            manifests_by_target[manifest.target_page] = manifest

        target_pages = sorted(set(claims_by_target) | set(manifests_by_target))
        for target_page in target_pages:
            claim_list = claims_by_target.get(target_page, [])
            manifest = manifests_by_target.get(target_page)
            if manifest is None:
                manifest = PromotionManifest(
                    manifest_id=self._manifest_id("rebuild", target_page),
                    record_id="rebuild",
                    target_page=target_page,
                    validated_at=datetime.now().isoformat(),
                    validated_by="system",
                    claim_ids=[claim.claim_id for claim in claim_list],
                    source_ids=sorted({source_id for claim in claim_list for source_id in claim.source_ids}),
                    source_fingerprints={},
                    status="validated",
                )
            self._write_target_page(vault_root, target_page, manifest, claim_list)

    def promote_draft(
        self,
        draft: PromotionDraft,
        vault_root: Path,
        validated_by: str = "human",
    ) -> dict[str, object]:
        """Persist a validated promotion draft, target page, and return a promotion result."""
        if not draft.ready_for_patch:
            raise ValueError("Promotion draft must be validated before promotion.")

        manifest_id = self._manifest_id(draft.record_id, draft.target_page)
        source_ids = list(dict.fromkeys(
            source_id
            for claim in draft.selected_claims
            for source_id in claim.source_ids
        ))
        fingerprints = self.source_fingerprints(vault_root, source_ids)
        if len(fingerprints) != len(source_ids):
            missing = sorted(set(source_ids) - set(fingerprints))
            raise ValueError(
                f"Promotion blocked because source fingerprints could not be resolved for: {', '.join(missing)}"
            )
        validated_at = datetime.now().isoformat()
        manifest = PromotionManifest(
            manifest_id=manifest_id,
            record_id=draft.record_id,
            target_page=draft.target_page,
            validated_at=validated_at,
            validated_by=validated_by,
            claim_ids=[claim.claim_id for claim in draft.selected_claims],
            source_ids=source_ids,
            source_fingerprints=fingerprints,
            status="validated",
        )

        written: list[ValidatedClaim] = []
        written_paths: list[Path] = []
        target_path: Path | None = None
        try:
            with self._locked(manifest_id):
                self._write_manifest(manifest)
                written_paths.append(self._manifest_json_path(manifest.manifest_id))
                written_paths.append(self._manifest_markdown_path(manifest.manifest_id))
                for claim in draft.selected_claims:
                    entry = ValidatedClaim(
                        claim_id=claim.claim_id,
                        record_id=draft.record_id,
                        target_page=draft.target_page,
                        text=claim.text,
                        source_ids=list(claim.source_ids),
                        source_fingerprints={sid: fingerprints.get(sid, "") for sid in claim.source_ids},
                        provenance=claim.provenance,
                        boundary=claim.boundary,
                        validated_at=validated_at,
                        validated_by=validated_by,
                        status="current",
                    )
                    self._write_claim(entry, manifest)
                    written.append(entry)
                    written_paths.append(self._record_json_path(entry.claim_id))
                    written_paths.append(self._record_markdown_path(entry.claim_id))

                current_claims = [
                    claim
                    for claim in self._load_claims()
                    if claim.target_page == draft.target_page and claim.status == "current"
                ]
                current_claims.sort(key=lambda item: item.claim_id)
                target_path = self._write_target_page(vault_root, draft.target_page, manifest, current_claims)
            self._refresh_stale_status(vault_root)
            return {
                "manifest": manifest,
                "claims": written,
                "target_path": target_path,
            }
        except Exception:
            if target_path and target_path.exists():
                target_path.unlink()
            for path in reversed(written_paths):
                if path.exists():
                    path.unlink()
            raise

    def query_validated_claims(self, vault_root: Path) -> list[ValidatedClaim]:
        """Return only fresh validated claims."""
        self._refresh_stale_status(vault_root)
        fresh: list[ValidatedClaim] = []
        for claim in self._load_claims():
            if claim.status != "current":
                continue
            fresh.append(claim)
        return fresh
