#!/usr/bin/env python3
"""
scripts/health.py — Aggregate vault health checks into one markdown report.

This is intentionally a thin wrapper around existing checks. It does not add
new inference or call an LLM. It gives the operator one command for the
Karpathy-style linting layer:

    python3 scripts/health.py
    python3 scripts/health.py --skip-slow
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


VAULT_ROOT = Path(__file__).parent.parent
REPORT_DIR = VAULT_ROOT / "system" / "health-checks"
DISEASES = ["ckd", "fip", "hcm", "ibd", "diabetes", "fcv"]
IMAGE_EXTS = {".jpg", ".jpeg", ".png"}
CANDIDATE_ASSET_RE = re.compile(r"raw/images/[^\]\s,)]+candidate-[^\]\s,)]+(?:\.png|\.jpg|\.jpeg)")
REQUIRED_SOURCE_FIELDS = ["verification_status", "decision_grade", "language_qa_status"]
VALID_SOURCE_VERIFICATION = {"title_only", "abstract_weighted", "source_checked", "deep_extracted", "audited"}
VALID_SOURCE_DECISION = {"no", "provisional", "yes"}
VALID_LANGUAGE_QA = {"unchecked", "light_checked", "bilingual_checked", "not_applicable"}
READER_CONTENT_ROOTS = ("topics", "outputs/briefings", "outputs/dossiers", "outputs/slides")
HIGH_TRACEABILITY_PATTERNS = (
    "synthesis-index",
    "translation-brief",
    "regulatory-brief",
    "ranking-memo",
    "route-memo",
)
VALIDATED_LANGUAGE_QA = {"light_checked", "bilingual_checked", "not_applicable"}
QUANTIFIED_CLAIM_RE = re.compile(
    r"\b(?:"
    r"[0-9]+(?:\.[0-9]+)?\s*(?:%|percent|mg|mg/mL|kg|days?|weeks?|months?|years?|cats?|cases?)|"
    r"[0-9]+/[0-9]+|"
    r"[Aa][Uu][Cc]\s*(?:of\s*)?[0-9]+\.[0-9]+|"
    r"[Nn]\s*=\s*[0-9]+|"
    r"kappa\s*=\s*[0-9]+\.[0-9]+|"
    r"[0-9]+\.[0-9]+"
    r")\b"
)
INTERNAL_NUMBER_CONTEXT_RE = re.compile(
    r"\b(?:"
    r"source[- ]?cards?|source_ids|round-1|deep[- ]?extraction|worksheet|vault|"
    r"changed source cards|downstream files|health report|Level [0-9]|[0-9]+/[0-9]+`?"
    r")\b",
    re.I,
)
READER_QUOTED_FACT_META_RE = re.compile(
    r"\b(?:"
    r"vault|current (?:module|topic layer)|source corpus|source pack|mapped into the vault|"
    r"supports keeping|branch (?:already|is|now)|treatment branch|regulatory branch|"
    r"real-world treatment package layer|high-complexity rescue branch|durability layer|"
    r"evidence map"
    r")\b",
    re.I,
)


def today_stamp() -> str:
    return datetime.now().strftime("%Y%m%d")


def today_iso() -> str:
    return datetime.now().date().isoformat()


def run_command(args: list[str], timeout: int = 180) -> dict:
    try:
        proc = subprocess.run(
            args,
            cwd=VAULT_ROOT,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        return {
            "args": args,
            "exit_code": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
            "timed_out": False,
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "args": args,
            "exit_code": 124,
            "stdout": (exc.stdout or "").strip() if isinstance(exc.stdout, str) else "",
            "stderr": "timeout",
            "timed_out": True,
        }


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


def frontmatter_block(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    if end == -1:
        return ""
    return text[3:end]


def frontmatter_list(fm_text: str, key: str) -> list[str]:
    inline_match = re.search(rf"^{re.escape(key)}:\s*\[(.*?)\]\s*$", fm_text, re.M)
    if inline_match:
        return split_frontmatter_list(inline_match.group(1))

    block_match = re.search(rf"^{re.escape(key)}:\s*$", fm_text, re.M)
    if not block_match:
        return []

    values = []
    for line in fm_text[block_match.end():].splitlines():
        if re.match(r"^\S[^:]*:", line):
            break
        item_match = re.match(r"^\s*-\s*(.+?)\s*$", line)
        if item_match:
            value = item_match.group(1).strip().strip("\"'")
            if value:
                values.append(value)
    return values


def split_frontmatter_list(raw: str) -> list[str]:
    values = []
    for item in raw.split(","):
        value = item.strip().strip("\"'")
        if value:
            values.append(value)
    return values


def nested_frontmatter_value(fm_text: str, section: str, key: str) -> str:
    in_section = False
    for line in fm_text.splitlines():
        if re.match(r"^\S[^:]*:", line):
            in_section = line.split(":", 1)[0].strip() == section
            continue
        if not in_section:
            continue
        match = re.match(rf"^\s+{re.escape(key)}:\s*(.*)$", line)
        if match:
            return match.group(1).strip().strip("\"'")
    return ""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def source_inventory() -> dict:
    result: dict = {
        "paper_total": 0,
        "expected_paper_total": 0,
        "reg_total": 0,
        "by_disease": {},
        "low_word_cards": [],
        "duplicate_ids": {},
        "missing_ids": [],
        "missing_required_fields": [],
        "invalid_field_values": [],
        "decision_grade_gate_violations": [],
        "source_link_issues": [],
        "source_evidence_policy_gaps": [],
        "source_quoted_fact_discipline_issues": [],
        "compiled_bad_source_refs": [],
        "compiled_missing_source_ids": [],
        "compiled_empty_source_ids": [],
        "compiled_thin_source_refs": [],
        "compiled_thin_source_uncaveated": [],
        "compiled_title_only_uncaveated": [],
        "traceability_gaps": [],
        "quantified_traceability_gaps": [],
        "reader_quoted_fact_discipline_issues": [],
        "language_qa_gaps": [],
        "source_state_conflicts": [],
        "source_verification_by_id": {},
    }

    seen: dict[str, list[str]] = defaultdict(list)

    for disease in DISEASES:
        cards = sorted((VAULT_ROOT / "raw" / "papers").glob(f"src-{disease}-*.md"))
        result["expected_paper_total"] += 24
        depth_counts: Counter[str] = Counter()
        verification_counts: Counter[str] = Counter()
        for card in cards:
            text = read_text(card)
            fm = frontmatter(text)
            fm_text = frontmatter_block(text)
            source_id = fm.get("id")
            if source_id:
                seen[source_id].append(str(card.relative_to(VAULT_ROOT)))
            else:
                result["missing_ids"].append(str(card.relative_to(VAULT_ROOT)))
            rel = str(card.relative_to(VAULT_ROOT))
            doi = nested_frontmatter_value(fm_text, "links", "doi")
            url = nested_frontmatter_value(fm_text, "links", "url")
            if not doi and not url:
                result["source_link_issues"].append({
                    "file": rel,
                    "id": source_id or "missing",
                    "reason": "source card has neither `links.doi` nor `links.url`",
                })
            if not source_evidence_policy_has_content(fm_text):
                result["source_evidence_policy_gaps"].append({
                    "file": rel,
                    "id": source_id or "missing",
                    "reason": "frontmatter `evidence_policy` has no machine-readable claims",
                })
            add_quoted_fact_discipline_issues(result, rel, source_id or "missing", fm_text)
            missing_fields = [field for field in REQUIRED_SOURCE_FIELDS if not fm.get(field)]
            if missing_fields:
                result["missing_required_fields"].append({
                    "file": rel,
                    "fields": missing_fields,
                })
            verification_status = fm.get("verification_status", "missing")
            if source_id:
                result["source_verification_by_id"][source_id] = verification_status
            decision_grade = fm.get("decision_grade", "missing")
            language_qa_status = fm.get("language_qa_status", "missing")
            validate_source_field(result, rel, "verification_status", verification_status, VALID_SOURCE_VERIFICATION)
            validate_source_field(result, rel, "decision_grade", decision_grade, VALID_SOURCE_DECISION)
            validate_source_field(result, rel, "language_qa_status", language_qa_status, VALID_LANGUAGE_QA)
            if decision_grade == "yes" and verification_status != "audited":
                result["decision_grade_gate_violations"].append({
                    "file": rel,
                    "decision_grade": decision_grade,
                    "verification_status": verification_status,
                    "reason": "`decision_grade: yes` requires `verification_status: audited`",
                })
            if decision_grade == "provisional" and verification_status in {"missing", "title_only", "abstract_weighted"}:
                result["decision_grade_gate_violations"].append({
                    "file": rel,
                    "decision_grade": decision_grade,
                    "verification_status": verification_status,
                    "reason": "`decision_grade: provisional` requires source_checked or stronger source verification",
                })
            depth_counts[fm.get("extraction_depth", "missing")] += 1
            verification_counts[verification_status] += 1
            extraction_depth = fm.get("extraction_depth", "missing")
            status = fm.get("status", "missing")
            if verification_status == "title_only" and (
                extraction_depth == "full" or status == "deep_extracted"
            ):
                result["source_state_conflicts"].append({
                    "file": rel,
                    "id": source_id or "missing",
                    "verification_status": verification_status,
                    "extraction_depth": extraction_depth,
                    "status": status,
                    "reason": "`title_only` source cannot be marked `full` or `deep_extracted`",
                })
            words = len(re.findall(r"\S+", text))
            if words < 700 and fm.get("extraction_depth", "missing") != "partial":
                result["low_word_cards"].append({
                    "file": rel,
                    "words": words,
                })
        result["paper_total"] += len(cards)
        result["by_disease"][disease] = {
            "cards": len(cards),
            "extraction_depth": dict(sorted(depth_counts.items())),
            "verification_status": dict(sorted(verification_counts.items())),
        }

    reg_cards = sorted((VAULT_ROOT / "raw" / "regulations").glob("src-reg-*.md"))
    result["reg_total"] = len(reg_cards)
    for card in reg_cards:
        text = read_text(card)
        fm = frontmatter(text)
        fm_text = frontmatter_block(text)
        source_id = fm.get("id")
        if source_id:
            seen[source_id].append(str(card.relative_to(VAULT_ROOT)))
        else:
            result["missing_ids"].append(str(card.relative_to(VAULT_ROOT)))
        verification_status = fm.get("verification_status", "missing")
        if source_id:
            result["source_verification_by_id"][source_id] = verification_status
        doi = nested_frontmatter_value(fm_text, "links", "doi")
        url = nested_frontmatter_value(fm_text, "links", "url")
        if not doi and not url:
            result["source_link_issues"].append({
                "file": str(card.relative_to(VAULT_ROOT)),
                "id": source_id or "missing",
                "reason": "source card has neither `links.doi` nor `links.url`",
            })
        if not source_evidence_policy_has_content(fm_text):
            result["source_evidence_policy_gaps"].append({
                "file": str(card.relative_to(VAULT_ROOT)),
                "id": source_id or "missing",
                "reason": "frontmatter `evidence_policy` has no machine-readable claims",
            })
        add_quoted_fact_discipline_issues(result, str(card.relative_to(VAULT_ROOT)), source_id or "missing", fm_text)

    result["duplicate_ids"] = {
        source_id: paths for source_id, paths in sorted(seen.items()) if len(paths) > 1
    }
    add_content_proof_inventory(result, set(seen.keys()))
    return result


def add_content_proof_inventory(result: dict, known_source_ids: set[str]) -> None:
    reader_paths = []
    for root in READER_CONTENT_ROOTS:
        reader_paths.extend(sorted((VAULT_ROOT / root).rglob("*.md")))
    # Validate source refs anywhere they are explicitly declared, but only require
    # source_ids on reader-facing content pages.
    declared_paths = set(reader_paths)
    declared_paths.update(sorted((VAULT_ROOT / "system" / "indexes").glob("*.md")))

    for path in sorted(declared_paths):
        text = read_text(path)
        fm = frontmatter(text)
        fm_text = frontmatter_block(text)
        rel = str(path.relative_to(VAULT_ROOT))
        source_ids_declared = bool(re.search(r"^source_ids:", fm_text, re.M))
        source_ids = frontmatter_list(fm_text, "source_ids")
        is_disease_content = fm.get("topic") in DISEASES or fm.get("disease")

        if path in reader_paths and is_disease_content and path.name != "navigation.md" and not source_ids_declared:
            result["compiled_missing_source_ids"].append(rel)
        if source_ids_declared and is_disease_content and not source_ids and path.name != "navigation.md":
            result["compiled_empty_source_ids"].append(rel)

        for source_id in source_ids:
            if source_id not in known_source_ids:
                result["compiled_bad_source_refs"].append({
                    "file": rel,
                    "source_id": source_id,
                })

        if should_report_thin_source_usage(path, fm, reader_paths):
            thin_refs = []
            title_only_refs = []
            for source_id in source_ids:
                verification_status = result["source_verification_by_id"].get(source_id)
                if verification_status in {"abstract_weighted", "title_only"}:
                    thin_refs.append({
                        "source_id": source_id,
                        "verification_status": verification_status,
                    })
                if verification_status == "title_only":
                    title_only_refs.append(source_id)
            if thin_refs:
                result["compiled_thin_source_refs"].append({
                    "file": rel,
                    "thin_refs": thin_refs,
                })
                if not has_thin_source_boundary_note(text):
                    result["compiled_thin_source_uncaveated"].append({
                        "file": rel,
                        "thin_refs": thin_refs,
                    })
            if title_only_refs and not has_title_only_boundary_note(text):
                result["compiled_title_only_uncaveated"].append({
                    "file": rel,
                    "source_ids": title_only_refs,
                })

        if is_high_traceability_page(path) and "## Key-Claim Traceability" not in text:
            result["traceability_gaps"].append(rel)

        quantified_lines = quantified_claim_lines(text)
        if (
            path in reader_paths
            and is_disease_content
            and path.name != "navigation.md"
            and quantified_lines
            and "## Key-Claim Traceability" not in text
            and "## Quantified Claim Traceability" not in text
        ):
            result["quantified_traceability_gaps"].append({
                "file": rel,
                "examples": quantified_lines[:5],
            })

        if path in reader_paths and is_disease_content and path.name != "navigation.md":
            add_reader_quoted_fact_discipline_issues(result, rel, text)

        if is_high_visibility_language_page(path, fm):
            language_qa_status = fm.get("language_qa_status", "missing")
            if language_qa_status not in VALIDATED_LANGUAGE_QA:
                result["language_qa_gaps"].append({
                    "file": rel,
                    "language_qa_status": language_qa_status,
                })


def is_high_traceability_page(path: Path) -> bool:
    rel = str(path.relative_to(VAULT_ROOT))
    name = path.name
    if rel.startswith("topics/") or rel.startswith("outputs/briefings/") or rel.startswith("outputs/dossiers/"):
        return any(pattern in name for pattern in HIGH_TRACEABILITY_PATTERNS)
    if rel.startswith("system/indexes/"):
        return any(pattern in name for pattern in HIGH_TRACEABILITY_PATTERNS)
    return False


def is_high_visibility_language_page(path: Path, fm: dict[str, str]) -> bool:
    rel = str(path.relative_to(VAULT_ROOT))
    name = path.name
    if rel.startswith("outputs/briefings/") or rel.startswith("outputs/dossiers/") or rel.startswith("outputs/slides/"):
        return True
    if rel.startswith("topics/"):
        return (
            "current-state-dashboard" in name
            or "synthesis-index" in name
            or "translation-brief" in name
            or "regulatory-brief" in name
        )
    if rel.startswith("system/indexes/"):
        return (
            "ranking-memo" in name
            or "route-memo" in name
            or "archetype" in name
            or fm.get("question_type") in {"regulatory", "translation", "synthesis"}
        )
    return False


def quantified_claim_lines(text: str) -> list[dict[str, str | int]]:
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            body = text[end + 4:]
    lines: list[dict[str, str | int]] = []
    for line_no, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("|---"):
            continue
        if not QUANTIFIED_CLAIM_RE.search(stripped):
            continue
        if INTERNAL_NUMBER_CONTEXT_RE.search(stripped):
            continue
        if re.search(r"\b(?:src-[a-z]+-[0-9]+|NADA\s+[0-9-]+|20[0-9]{2}-[0-9]{2}-[0-9]{2})\b", stripped):
            continue
        lines.append({"line": line_no, "text": stripped})
    return lines


def add_reader_quoted_fact_discipline_issues(result: dict, rel: str, text: str) -> None:
    in_quoted_fact = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        if re.match(r"^###\s+quoted_fact\s*$", line):
            in_quoted_fact = True
            continue
        if in_quoted_fact and re.match(r"^###\s+", line):
            in_quoted_fact = False
        if not in_quoted_fact:
            continue
        item = line.strip()
        if not item.startswith("- "):
            continue
        if READER_QUOTED_FACT_META_RE.search(item):
            result["reader_quoted_fact_discipline_issues"].append({
                "file": rel,
                "line": line_no,
                "item": item[2:],
                "reason": "reader `quoted_fact` contains vault/module/branch/layer interpretation",
            })


def should_report_thin_source_usage(path: Path, fm: dict[str, str], reader_paths: list[Path]) -> bool:
    is_disease_content = fm.get("topic") in DISEASES or fm.get("disease")
    if not is_disease_content:
        return False
    return path in reader_paths or is_high_visibility_language_page(path, fm)


def has_title_only_boundary_note(text: str) -> bool:
    return bool(
        re.search(
            r"title[- ]?(?:only|level)|partial|workflow[- ]?only|workflow[- ]?orientation|"
            r"not\s+(?:full|claim-heavy|decision-grade)|标题|部分",
            text,
            re.I,
        )
    )


def has_thin_source_boundary_note(text: str) -> bool:
    return bool(
        re.search(
            r"abstract[-_ ]?weighted|title[- ]?(?:only|level)|partial|full[- ]?text|"
            r"decision[- ]?grade|not\s+(?:clinical|diagnostic|treatment|regulatory|routine|"
            r"jurisdiction|route|product|submission|owner-facing|veterinary\s+medical)"
            r"(?:\s+\w+){0,4}\s+guidance|not\s+replacing\s+the\s+raw\s+source\s+layer|"
            r"does\s+not\s+imply\s+stronger\s+evidence|证据强度|原始来源层|不用于替代",
            text,
            re.I,
        )
    )


def validate_source_field(result: dict, rel: str, field: str, value: str, allowed: set[str]) -> None:
    if value == "missing":
        return
    if value not in allowed:
        result["invalid_field_values"].append({
            "file": rel,
            "field": field,
            "value": value,
            "allowed": sorted(allowed),
        })


def source_evidence_policy_has_content(fm_text: str) -> bool:
    section_match = re.search(r"^evidence_policy:\s*$", fm_text, re.M)
    if not section_match:
        return False
    for line in fm_text[section_match.end():].splitlines():
        if re.match(r"^\S[^:]*:", line):
            break
        if re.match(r"^\s{4}-\s+\S", line):
            return True
    return False


def evidence_policy_items(fm_text: str, section: str) -> list[str]:
    items: list[str] = []
    in_section = False
    for line in fm_text.splitlines():
        section_match = re.match(r"^\s{2}(quoted_fact|source_supported_conclusion|llm_inference):", line)
        if section_match:
            in_section = section_match.group(1) == section
            continue
        if re.match(r"^\S[^:]*:", line):
            in_section = False
        if not in_section:
            continue
        item_match = re.match(r"^\s{4}-\s+(.+?)\s*$", line)
        if item_match:
            items.append(item_match.group(1).strip().strip("\"'"))
    return items


def add_quoted_fact_discipline_issues(result: dict, rel: str, source_id: str, fm_text: str) -> None:
    for item in evidence_policy_items(fm_text, "quoted_fact"):
        if looks_like_compiled_interpretation(item):
            result["source_quoted_fact_discipline_issues"].append({
                "file": rel,
                "id": source_id,
                "item": item,
                "reason": "`quoted_fact` should hold source-stated facts, not vault interpretation",
            })


def looks_like_compiled_interpretation(item: str) -> bool:
    return bool(
        re.search(
            r"^(This (?:source|paper|review|study|card|chapter|guideline)|"
            r"The (?:source|paper|review|study|card)|The vault|"
            r"(?:Mechanism|Translation|Treatment|Endpoint|Recognition|Risk|Synthesis|"
            r"Default|Future|Later|Regulatory|Diet|HCM|CKD|IBD|FIP|Diabetes) pages?\b|"
            r"The safest|Safe current|Safest current|Model value|Evidence skepticism|"
            r"Comparative framing|Frontier biomarker|Bexacat should|Senvelgo should|"
            r"Compounded GS).*\b(should|supports?|belongs|anchor|branch|useful|role|"
            r"modeled|framed|logic|boundary|candidate|target|promot|treat|read|keep|"
            r"represent|govern|become|matters|valuable)\b",
            item,
            re.I,
        )
    )


def image_inventory() -> dict:
    result: dict = {"by_disease": {}, "candidate_local_asset_refs": []}
    for disease in DISEASES:
        image_dir = VAULT_ROOT / "raw" / "images" / disease
        verified = []
        if image_dir.exists():
            verified = [
                p for p in image_dir.iterdir()
                if p.is_file()
                and p.suffix.lower() in IMAGE_EXTS
                and not p.name.startswith("candidate-")
            ]

        candidate_refs = set()
        candidate_frontmatter_refs = set()
        for card in sorted((VAULT_ROOT / "raw" / "papers").glob(f"src-{disease}-*.md")):
            text = read_text(card)
            candidate_refs.update(CANDIDATE_ASSET_RE.findall(text))
            fm_text = ""
            if text.startswith("---") and "\n---" in text[3:]:
                fm_text = text[3:text.find("\n---", 3)]
            if "local_assets:" in fm_text:
                candidate_frontmatter_refs.update(candidate_local_assets(fm_text))

        result["by_disease"][disease] = {
            "verified_images": len(verified),
            "candidate_refs": len(candidate_refs),
            "candidate_local_asset_refs": len(candidate_frontmatter_refs),
        }
        for ref in sorted(candidate_frontmatter_refs):
            result["candidate_local_asset_refs"].append({"disease": disease, "ref": ref})
    return result


def candidate_local_assets(fm_text: str) -> set[str]:
    refs: set[str] = set()
    in_local_assets = False
    for line in fm_text.splitlines():
        stripped = line.strip()
        if re.match(r"^\S[^:]*:", line) and not line.startswith("local_assets:"):
            in_local_assets = False
        if stripped.startswith("local_assets:"):
            in_local_assets = True
        if in_local_assets:
            refs.update(CANDIDATE_ASSET_RE.findall(line))
    return refs


def inbox_inventory() -> dict:
    inbox = VAULT_ROOT / "inbox"
    active = []
    rejected = []
    if not inbox.exists():
        return {"active": [], "rejected": []}
    for path in sorted(inbox.rglob("*")):
        if not path.is_file() or path.name == ".gitkeep":
            continue
        rel = str(path.relative_to(VAULT_ROOT))
        if rel.startswith("inbox/rejected/"):
            rejected.append(rel)
        else:
            active.append(rel)
    return {"active": active, "rejected": rejected}


def latest_acceptance_report(prefix: str = "ask-the-vault-acceptance-report") -> dict:
    reports = sorted(REPORT_DIR.glob(f"{prefix}-*.md"))
    if not reports:
        return {"path": None, "mode": "missing", "status": "missing"}
    latest = reports[-1]
    text = read_text(latest)
    mode_match = re.search(r"^Execution mode:\s*(.+)$", text, re.M)
    status_match = re.search(r"^status:\s*(.+)$", text, re.M)
    acceptance_status_match = re.search(r"^Acceptance status:\s*(.+)$", text, re.M)
    return {
        "path": str(latest.relative_to(VAULT_ROOT)),
        "mode": mode_match.group(1).strip() if mode_match else "unknown",
        "status": (
            acceptance_status_match.group(1).strip()
            if acceptance_status_match
            else status_match.group(1).strip() if status_match else "unknown"
        ),
    }


def ordinary_user_acceptance_ok(report: dict) -> bool:
    return (
        (report["mode"] == "executed" and report["status"] == "pass")
        or (report["mode"] == "route-only" and report["status"] == "route_pass")
    )


def compile_trigger_status() -> dict:
    result = run_command(["python3", "scripts/compile_trigger.py", "--since", "1", "--json"], timeout=60)
    if result["exit_code"] != 0:
        return {"ok": False, "error": result["stderr"] or result["stdout"]}
    try:
        data = json.loads(result["stdout"] or "{}")
    except json.JSONDecodeError:
        return {"ok": False, "error": "invalid JSON from compile_trigger.py"}
    return {
        "ok": True,
        "changed_sources": data.get("changed_sources", []),
        "queue_count": len(data.get("recompile_queue", [])),
    }


def api_key_status() -> dict[str, bool]:
    return {
        "ANTHROPIC_API_KEY": bool(os.environ.get("ANTHROPIC_API_KEY")),
        "OPENROUTER_API_KEY": bool(os.environ.get("OPENROUTER_API_KEY")),
        "OPENAI_API_KEY": bool(os.environ.get("OPENAI_API_KEY")),
    }


def command_summary(command_result: dict) -> str:
    if command_result["timed_out"]:
        return "TIMEOUT"
    return "PASS" if command_result["exit_code"] == 0 else "FAIL"


def render_report(data: dict) -> str:
    inventory = data["source_inventory"]
    images = data["image_inventory"]
    inbox = data["inbox_inventory"]
    acceptance = data["acceptance"]
    ordinary_acceptance = data["ordinary_user_acceptance"]
    compile_status = data["compile_trigger"]
    keys = data["api_keys"]
    link_result = data["link_check"]
    query_result = data["query_tests"]

    has_hard_failure = (
        link_result["exit_code"] != 0
        or query_result["exit_code"] != 0
        or bool(inventory["duplicate_ids"])
        or bool(inventory["missing_ids"])
        or bool(inventory["low_word_cards"])
        or bool(inventory["missing_required_fields"])
        or bool(inventory["invalid_field_values"])
        or bool(inventory["decision_grade_gate_violations"])
        or bool(inventory["source_link_issues"])
        or bool(inventory["source_evidence_policy_gaps"])
        or bool(inventory["source_state_conflicts"])
        or bool(inventory["compiled_bad_source_refs"])
        or bool(inventory["compiled_missing_source_ids"])
        or bool(inventory["compiled_empty_source_ids"])
    )
    status = "needs_attention" if has_hard_failure else "active"

    lines = [
        "---",
        f"id: system-health-report-{today_stamp()}",
        "type: health-check",
        "topic: operating-system",
        "question_type: health",
        "language: bilingual",
        f"last_compiled_at: {today_iso()}",
        "verification_status: compiled",
        "decision_grade: provisional",
        "language_qa_status: light_checked",
        "owner: codex",
        f"status: {status}",
        "---",
        "",
        f"# Vault Health Report, {today_iso()}",
        "",
        "This report aggregates existing checks. It does not call an LLM and does not replace human review.",
        "",
        "## Summary",
        "",
        "| Check | Status | Read |",
        "|---|---|---|",
        summary_row("Markdown links", command_summary(link_result), first_line(link_result["stdout"])),
        summary_row("Query tests", command_summary(query_result), test_summary(query_result["stdout"])),
        summary_row("Paper source cards", "PASS" if inventory["paper_total"] == inventory["expected_paper_total"] else "FAIL", f"{inventory['paper_total']} strict disease paper cards"),
        summary_row("Regulation source cards", "PASS" if inventory["reg_total"] == 14 else "WARN", f"{inventory['reg_total']} regulation cards"),
        summary_row("Source IDs", "PASS" if not inventory["duplicate_ids"] and not inventory["missing_ids"] else "FAIL", f"{len(inventory['duplicate_ids'])} duplicates, {len(inventory['missing_ids'])} missing ids"),
        summary_row("Low-word paper cards", "PASS" if not inventory["low_word_cards"] else "FAIL", f"{len(inventory['low_word_cards'])} cards below 700 words"),
        summary_row("Source schema fields", "PASS" if not inventory["missing_required_fields"] and not inventory["invalid_field_values"] else "FAIL", f"{len(inventory['missing_required_fields'])} cards missing required fields, {len(inventory['invalid_field_values'])} invalid field values"),
        summary_row("Source state consistency", "PASS" if not inventory["source_state_conflicts"] else "FAIL", f"{len(inventory['source_state_conflicts'])} title-only depth/status conflicts"),
        summary_row("Source link proof", "PASS" if not inventory["source_link_issues"] else "FAIL", f"{len(inventory['source_link_issues'])} source cards without DOI or URL"),
        summary_row("Source evidence policy", "PASS" if not inventory["source_evidence_policy_gaps"] else "FAIL", f"{len(inventory['source_evidence_policy_gaps'])} source cards with empty evidence_policy"),
        summary_row("Source quoted-fact discipline", "PASS" if not inventory["source_quoted_fact_discipline_issues"] else "WARN", f"{len(inventory['source_quoted_fact_discipline_issues'])} quoted_fact items look interpretive"),
        summary_row("Compiled source refs", "PASS" if not inventory["compiled_bad_source_refs"] else "FAIL", f"{len(inventory['compiled_bad_source_refs'])} invalid source refs"),
        summary_row("Reader page source_ids", "PASS" if not inventory["compiled_missing_source_ids"] and not inventory["compiled_empty_source_ids"] else "FAIL", f"{len(inventory['compiled_missing_source_ids'])} missing, {len(inventory['compiled_empty_source_ids'])} empty"),
        summary_row("Thin source usage", "PASS" if not inventory["compiled_thin_source_refs"] else "WARN", f"{len(inventory['compiled_thin_source_refs'])} reader/high-visibility pages use abstract-weighted or title-only sources"),
        summary_row("Thin source caveats", "PASS" if not inventory["compiled_thin_source_uncaveated"] else "WARN", f"{len(inventory['compiled_thin_source_uncaveated'])} thin-source pages without visible evidence-depth caveat"),
        summary_row("Title-only caveats", "PASS" if not inventory["compiled_title_only_uncaveated"] else "WARN", f"{len(inventory['compiled_title_only_uncaveated'])} pages cite title-only sources without visible caveat"),
        summary_row("Key-claim traceability", "PASS" if not inventory["traceability_gaps"] else "WARN", f"{len(inventory['traceability_gaps'])} high-value pages missing traceability table"),
        summary_row("Quantified claim traceability", "PASS" if not inventory["quantified_traceability_gaps"] else "WARN", f"{len(inventory['quantified_traceability_gaps'])} quantified reader pages missing traceability table"),
        summary_row("Reader quoted-fact discipline", "PASS" if not inventory["reader_quoted_fact_discipline_issues"] else "WARN", f"{len(inventory['reader_quoted_fact_discipline_issues'])} reader quoted_fact items look interpretive"),
        summary_row("High-visibility language QA", "PASS" if not inventory["language_qa_gaps"] else "WARN", f"{len(inventory['language_qa_gaps'])} high-visibility pages unchecked or missing"),
        summary_row("Decision-grade gate", "PASS" if not inventory["decision_grade_gate_violations"] else "FAIL", f"{len(inventory['decision_grade_gate_violations'])} source-card violations"),
        summary_row("Candidate image gate", "PASS" if not images["candidate_local_asset_refs"] else "WARN", f"{len(images['candidate_local_asset_refs'])} candidate refs remain gated in local_assets frontmatter"),
        summary_row("Inbox backlog", "PASS" if not inbox["active"] else "WARN", f"{len(inbox['active'])} active files, {len(inbox['rejected'])} rejected audit files"),
        summary_row("Acceptance report", "PASS" if acceptance["mode"] == "executed" and acceptance["status"] == "pass" else "WARN", f"{acceptance['path'] or 'missing'}; mode={acceptance['mode']}; status={acceptance['status']}"),
        summary_row("Ordinary-user acceptance", "PASS" if ordinary_user_acceptance_ok(ordinary_acceptance) else "WARN", f"{ordinary_acceptance['path'] or 'missing'}; mode={ordinary_acceptance['mode']}; status={ordinary_acceptance['status']}"),
        summary_row("Compile trigger", "PASS" if compile_status.get("ok") else "FAIL", compile_read(compile_status)),
        summary_row("API keys", "PASS" if any(keys.values()) else "WARN", key_read(keys)),
        "",
        "## Source Card Reality",
        "",
        "| Disease | Cards | extraction_depth | verification_status |",
        "|---|---:|---|---|",
    ]

    for disease in DISEASES:
        item = inventory["by_disease"][disease]
        lines.append(
            f"| {disease} | {item['cards']} | {fmt_counts(item['extraction_depth'])} | {fmt_counts(item['verification_status'])} |"
        )

    lines.extend([
        "",
        "## Image Reality",
        "",
        "| Disease | Verified images | Candidate refs | Candidate refs in local_assets |",
        "|---|---:|---:|---:|",
    ])

    for disease in DISEASES:
        item = images["by_disease"][disease]
        lines.append(
            f"| {disease} | {item['verified_images']} | {item['candidate_refs']} | {item['candidate_local_asset_refs']} |"
        )

    lines.extend([
        "",
        "## Inbox Backlog",
        "",
    ])
    if inbox["active"]:
        lines.extend(f"- {path}" for path in inbox["active"])
    else:
        lines.append("- No active inbox files outside `.gitkeep`.")
    if inbox["rejected"]:
        lines.append("")
        lines.append("Rejected / audit notes:")
        lines.extend(f"- {path}" for path in inbox["rejected"])

    if inventory["missing_required_fields"] or inventory["invalid_field_values"]:
        lines.extend(["", "## Source Schema Issues", ""])
        for item in inventory["missing_required_fields"]:
            lines.append(f"- {item['file']}: missing {', '.join(item['fields'])}")
        for item in inventory["invalid_field_values"]:
            lines.append(f"- {item['file']}: `{item['field']}: {item['value']}` is outside the allowed set")

    if inventory["source_link_issues"]:
        lines.extend(["", "## Source Link Proof Issues", ""])
        for item in inventory["source_link_issues"]:
            lines.append(f"- {item['file']}: {item['reason']} (`{item['id']}`)")

    if inventory["source_state_conflicts"]:
        lines.extend(["", "## Source State Consistency Issues", ""])
        for item in inventory["source_state_conflicts"]:
            lines.append(
                f"- {item['file']}: {item['reason']} "
                f"(`verification_status: {item['verification_status']}`, "
                f"`extraction_depth: {item['extraction_depth']}`, `status: {item['status']}`)"
            )

    if inventory["source_evidence_policy_gaps"]:
        lines.extend(["", "## Source Evidence Policy Issues", ""])
        for item in inventory["source_evidence_policy_gaps"]:
            lines.append(f"- {item['file']}: {item['reason']} (`{item['id']}`)")

    if inventory["source_quoted_fact_discipline_issues"]:
        lines.extend(["", "## Source Quoted-Fact Discipline Issues", ""])
        lines.append(
            "`quoted_fact` should stay close to source-stated facts. Interpretive routing, branch, and promotion language belongs in "
            "`source_supported_conclusion` or `llm_inference`."
        )
        for item in inventory["source_quoted_fact_discipline_issues"][:80]:
            lines.append(f"- {item['file']}: {item['reason']} (`{item['id']}`) — {item['item']}")
        if len(inventory["source_quoted_fact_discipline_issues"]) > 80:
            lines.append(f"- ... {len(inventory['source_quoted_fact_discipline_issues']) - 80} more items")

    if (
        inventory["compiled_bad_source_refs"]
        or inventory["compiled_missing_source_ids"]
        or inventory["compiled_empty_source_ids"]
    ):
        lines.extend(["", "## Compiled Provenance Issues", ""])
        for item in inventory["compiled_bad_source_refs"]:
            lines.append(f"- {item['file']}: unknown source id `{item['source_id']}`")
        for item in inventory["compiled_missing_source_ids"][:80]:
            lines.append(f"- {item}: missing frontmatter `source_ids`")
        if len(inventory["compiled_missing_source_ids"]) > 80:
            lines.append(f"- ... {len(inventory['compiled_missing_source_ids']) - 80} more pages missing `source_ids`")
        for item in inventory["compiled_empty_source_ids"]:
            lines.append(f"- {item}: empty frontmatter `source_ids`")

    if inventory["compiled_thin_source_refs"]:
        lines.extend(["", "## Thin Source Usage", ""])
        lines.append(
            "`abstract_weighted` and `title_only` sources can support cautious synthesis, "
            "but should not be read as full-text or decision-grade proof."
        )
        for item in inventory["compiled_thin_source_refs"][:80]:
            refs = ", ".join(
                f"{ref['source_id']} ({ref['verification_status']})"
                for ref in item["thin_refs"]
            )
            lines.append(f"- {item['file']}: {refs}")
        if len(inventory["compiled_thin_source_refs"]) > 80:
            lines.append(f"- ... {len(inventory['compiled_thin_source_refs']) - 80} more pages")

    if inventory["compiled_thin_source_uncaveated"]:
        lines.extend(["", "## Thin Source Caveat Gaps", ""])
        lines.append(
            "Pages that cite `abstract_weighted` or `title_only` sources should visibly state the evidence-depth boundary."
        )
        for item in inventory["compiled_thin_source_uncaveated"][:80]:
            refs = ", ".join(
                f"{ref['source_id']} ({ref['verification_status']})"
                for ref in item["thin_refs"]
            )
            lines.append(f"- {item['file']}: {refs}")
        if len(inventory["compiled_thin_source_uncaveated"]) > 80:
            lines.append(f"- ... {len(inventory['compiled_thin_source_uncaveated']) - 80} more pages")

    if inventory["compiled_title_only_uncaveated"]:
        lines.extend(["", "## Title-Only Caveat Gaps", ""])
        lines.append(
            "Pages that cite title-only sources should include a visible boundary note before readers reuse those claims."
        )
        for item in inventory["compiled_title_only_uncaveated"][:80]:
            lines.append(f"- {item['file']}: {', '.join(item['source_ids'])}")
        if len(inventory["compiled_title_only_uncaveated"]) > 80:
            lines.append(f"- ... {len(inventory['compiled_title_only_uncaveated']) - 80} more pages")

    if inventory["traceability_gaps"]:
        lines.extend(["", "## Key-Claim Traceability Gaps", ""])
        lines.append(
            "High-value synthesis / translation / regulatory / ranking / route pages should "
            "bind their strongest claims to source ids."
        )
        for item in inventory["traceability_gaps"][:80]:
            lines.append(f"- {item}")
        if len(inventory["traceability_gaps"]) > 80:
            lines.append(f"- ... {len(inventory['traceability_gaps']) - 80} more pages")

    if inventory["quantified_traceability_gaps"]:
        lines.extend(["", "## Quantified Claim Traceability Gaps", ""])
        lines.append(
            "Reader-facing pages with clinical, regulatory, or dosage-style numbers should include a traceability table "
            "so high-risk numeric claims are tied to source cards rather than left as free prose."
        )
        for item in inventory["quantified_traceability_gaps"][:80]:
            lines.append(f"- {item['file']}")
            for example in item["examples"]:
                lines.append(f"  - line {example['line']}: {example['text']}")
        if len(inventory["quantified_traceability_gaps"]) > 80:
            lines.append(f"- ... {len(inventory['quantified_traceability_gaps']) - 80} more pages")

    if inventory["reader_quoted_fact_discipline_issues"]:
        lines.extend(["", "## Reader Quoted-Fact Discipline Issues", ""])
        lines.append(
            "Reader-facing `### quoted_fact` sections should hold source-stated facts. Vault, module, branch, layer, "
            "and routing judgments belong under `source_supported_conclusion` or `llm_inference`."
        )
        for item in inventory["reader_quoted_fact_discipline_issues"][:80]:
            lines.append(f"- {item['file']}:{item['line']}: {item['reason']} — {item['item']}")
        if len(inventory["reader_quoted_fact_discipline_issues"]) > 80:
            lines.append(f"- ... {len(inventory['reader_quoted_fact_discipline_issues']) - 80} more items")

    if inventory["language_qa_gaps"]:
        lines.extend(["", "## High-Visibility Language QA Gaps", ""])
        lines.append(
            "Unchecked high-visibility pages can make source-supported claims sound stronger than the evidence."
        )
        for item in inventory["language_qa_gaps"][:80]:
            lines.append(f"- {item['file']}: `language_qa_status: {item['language_qa_status']}`")
        if len(inventory["language_qa_gaps"]) > 80:
            lines.append(f"- ... {len(inventory['language_qa_gaps']) - 80} more pages")

    if inventory["decision_grade_gate_violations"]:
        lines.extend(["", "## Decision-Grade Gate Violations", ""])
        for item in inventory["decision_grade_gate_violations"]:
            lines.append(
                f"- {item['file']}: {item['reason']} "
                f"(current `{item['verification_status']}`, `{item['decision_grade']}`)"
            )

    lines.extend([
        "",
        "## Next Actions",
        "",
    ])
    lines.extend(next_actions(data))

    if link_result["exit_code"] != 0:
        lines.extend(["", "## Link Check Output", "", "```text", clip(link_result["stdout"] or link_result["stderr"]), "```"])
    if query_result["exit_code"] != 0:
        lines.extend(["", "## Query Test Output", "", "```text", clip(query_result["stdout"] or query_result["stderr"]), "```"])

    return "\n".join(lines) + "\n"


def first_line(text: str) -> str:
    return (text.splitlines() or [""])[-1].strip()


def md_cell(text: object) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def summary_row(check: str, status: str, read: str) -> str:
    return f"| {md_cell(check)} | {md_cell(status)} | {md_cell(read)} |"


def test_summary(text: str) -> str:
    match = re.search(r"(\d+ passed\s+\|\s+\d+ failed\s+\|\s+\d+ total)", text)
    return match.group(1) if match else first_line(text)


def fmt_counts(counts: dict[str, int]) -> str:
    return ", ".join(f"{key}: {value}" for key, value in sorted(counts.items()))


def key_read(keys: dict[str, bool]) -> str:
    present = [key for key, value in keys.items() if value]
    if present:
        return "present: " + ", ".join(present)
    return "no API keys in current shell"


def compile_read(status: dict) -> str:
    if not status.get("ok"):
        return status.get("error", "compile_trigger failed")
    return f"{len(status['changed_sources'])} changed source cards, {status['queue_count']} downstream files"


def clip(text: str, limit: int = 4000) -> str:
    return text if len(text) <= limit else text[:limit] + "\n... clipped ..."


def next_actions(data: dict) -> list[str]:
    actions: list[str] = []
    keys = data["api_keys"]
    acceptance = data["acceptance"]
    ordinary_acceptance = data["ordinary_user_acceptance"]
    inventory = data["source_inventory"]
    images = data["image_inventory"]

    if not any(keys.values()) or acceptance["mode"] != "executed":
        actions.append("- Run live acceptance once `OPENROUTER_API_KEY` or `ANTHROPIC_API_KEY` is present.")
    elif acceptance["status"] != "pass":
        actions.append("- Review and fix the latest executed acceptance report until `Acceptance status: pass`.")
    if not ordinary_user_acceptance_ok(ordinary_acceptance):
        actions.append("- Run `python3 scripts/run_acceptance_checklist.py --suite ordinary-user --route-only` or the live ordinary-user suite so ordinary-user routing stays under health checks.")
    if inventory["by_disease"]["ckd"]["verification_status"].get("missing"):
        actions.append("- Backfill CKD `verification_status` frontmatter so mature CKD cards no longer show as `missing` in health reports.")
    if inventory["missing_required_fields"] or inventory["invalid_field_values"]:
        actions.append("- Fix source-card schema fields before compiling downstream topic/output pages.")
    if inventory["source_link_issues"]:
        actions.append("- Add a DOI or URL to every source card before using it as evidence.")
    if inventory["source_state_conflicts"]:
        actions.append("- Fix source-card state conflicts where title-only cards are marked full or deep-extracted.")
    if inventory["source_evidence_policy_gaps"]:
        actions.append("- Backfill source-card frontmatter `evidence_policy` so proof tags are machine-readable.")
    if inventory["source_quoted_fact_discipline_issues"]:
        actions.append("- Move interpretive `quoted_fact` entries into `source_supported_conclusion` or `llm_inference`.")
    if inventory["compiled_bad_source_refs"]:
        actions.append("- Fix invalid `source_ids` before trusting compiled topic/output pages.")
    if inventory["compiled_missing_source_ids"] or inventory["compiled_empty_source_ids"]:
        actions.append("- Backfill reader-facing topic/output `source_ids` so every compiled content page can trace back to real source cards.")
    if inventory["compiled_thin_source_uncaveated"]:
        actions.append("- Add visible evidence-depth caveats where reader-facing pages cite abstract-weighted or title-only sources.")
    if inventory["compiled_title_only_uncaveated"]:
        actions.append("- Add visible title-only / partial-source caveats where reader-facing pages cite title-only sources.")
    if inventory["traceability_gaps"]:
        actions.append("- Add `## Key-Claim Traceability` tables to high-value synthesis / translation / regulatory / ranking / route pages.")
    if inventory["quantified_traceability_gaps"]:
        actions.append("- Add `## Quantified Claim Traceability` tables to reader-facing pages with clinical or regulatory numbers.")
    if inventory["reader_quoted_fact_discipline_issues"]:
        actions.append("- Move reader-facing `quoted_fact` module/branch/layer judgments into `source_supported_conclusion` or `llm_inference`.")
    if inventory["language_qa_gaps"]:
        actions.append("- Language-QA high-visibility pages so source-supported claims do not become overstrong through wording drift.")
    if inventory["decision_grade_gate_violations"]:
        actions.append("- Resolve decision-grade gate violations before using affected source cards for high-risk conclusions.")
    non_ckd_without_images = [
        disease for disease in ["fip", "hcm", "ibd", "diabetes"]
        if images["by_disease"][disease]["verified_images"] == 0
    ]
    if non_ckd_without_images:
        actions.append("- Verify one non-candidate image/table asset for: " + ", ".join(non_ckd_without_images) + ".")
    if data["inbox_inventory"]["active"]:
        actions.append("- Clear active inbox files by promote / reject / keep-with-blocker.")
    if not actions:
        actions.append("- No immediate structural action from this report.")
    return actions


def main() -> int:
    parser = argparse.ArgumentParser(description="Run vault health checks and write a markdown report.")
    parser.add_argument("--skip-slow", action="store_true", help="Skip link and query test subprocesses.")
    args = parser.parse_args()

    if args.skip_slow:
        link_check = {"exit_code": 0, "stdout": "SKIPPED", "stderr": "", "timed_out": False}
        query_tests = {"exit_code": 0, "stdout": "SKIPPED", "stderr": "", "timed_out": False}
    else:
        link_check = run_command(["python3", "scripts/check_markdown_links.py"])
        query_tests = run_command(["python3", "scripts/test_query.py"])

    data = {
        "link_check": link_check,
        "query_tests": query_tests,
        "source_inventory": source_inventory(),
        "image_inventory": image_inventory(),
        "inbox_inventory": inbox_inventory(),
        "acceptance": latest_acceptance_report(),
        "ordinary_user_acceptance": latest_acceptance_report("ordinary-user-acceptance-report"),
        "compile_trigger": compile_trigger_status(),
        "api_keys": api_key_status(),
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / f"health-report-{today_stamp()}.md"
    report_path.write_text(render_report(data), encoding="utf-8")
    print(report_path.relative_to(VAULT_ROOT))

    hard_fail = (
        data["link_check"]["exit_code"] != 0
        or data["query_tests"]["exit_code"] != 0
        or bool(data["source_inventory"]["duplicate_ids"])
        or bool(data["source_inventory"]["missing_ids"])
        or bool(data["source_inventory"]["low_word_cards"])
        or bool(data["source_inventory"]["missing_required_fields"])
        or bool(data["source_inventory"]["invalid_field_values"])
        or bool(data["source_inventory"]["decision_grade_gate_violations"])
        or bool(data["source_inventory"]["source_link_issues"])
        or bool(data["source_inventory"]["source_evidence_policy_gaps"])
        or bool(data["source_inventory"]["source_state_conflicts"])
        or bool(data["source_inventory"]["compiled_bad_source_refs"])
        or bool(data["source_inventory"]["compiled_missing_source_ids"])
        or bool(data["source_inventory"]["compiled_empty_source_ids"])
    )
    return 1 if hard_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
