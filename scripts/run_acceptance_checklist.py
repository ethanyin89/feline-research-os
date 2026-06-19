#!/usr/bin/env python3
"""
scripts/run_acceptance_checklist.py — Run or scaffold the Ask The Vault acceptance checklist.

Usage:
    python3 scripts/run_acceptance_checklist.py --template-only
    python3 scripts/run_acceptance_checklist.py --suite ordinary-user --template-only
    python3 scripts/run_acceptance_checklist.py --backend openrouter
    python3 scripts/run_acceptance_checklist.py --backend openrouter --write-back
"""

import argparse
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
import sys
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))

from query import compute_confidence, parse_source_ids_from_answer
from query import (
    _classify_page_family,
    heuristic_files_for_route,
    heuristic_question_type,
    infer_disease_from_question,
    parse_source_ids_from_frontmatter,
)

VAULT_ROOT = Path(__file__).parent.parent
REPORT_DIR = VAULT_ROOT / "system" / "health-checks"

QUESTIONS = [
    {
        "id": "Q1",
        "topic": "CKD mechanism spine",
        "question": "CKD 的核心机制主线是什么？",
        "must_see": "至少落到 CKD mechanism 强答案面，且至少 2 个真实 source ids。",
        "expected_question_type": "mechanism",
        "expected_primary_family": "mechanism-overview",
        "expected_primary_surface": "topics/ckd/mechanism-overview.md",
    },
    {
        "id": "Q2",
        "topic": "CKD endpoint selection",
        "question": "What endpoints are most usable for feline CKD efficacy evaluation, and why?",
        "must_see": "有 endpoint shortlist 和 why，不只是罗列。",
        "expected_question_type": "endpoints",
        "expected_primary_family": "endpoint-handbook",
        "expected_primary_surface": "topics/ckd/endpoint-handbook.md",
    },
    {
        "id": "Q3",
        "topic": "CKD claim verification",
        "question": "Verify whether SDMA should already be treated as a core early-detection anchor in this vault.",
        "must_see": "必须是 verification 风格，同时呈现支持与保留条件。",
        "expected_question_type": "claim_verification",
        "expected_primary_family": "verify-a-claim",
        "expected_primary_surface": "system/indexes/verify-a-claim.md",
    },
    {
        "id": "Q4",
        "topic": "FIP diagnostic workup",
        "question": "What is the current diagnostic workup architecture for feline FIP?",
        "must_see": "不能把 diagnosis 简化成单一 assay。",
        "expected_question_type": "recognition",
        "expected_primary_family": "risk-and-recognition",
        "expected_primary_surface": "topics/fip/risk-and-recognition.md",
    },
    {
        "id": "Q5",
        "topic": "HCM recognition versus endpoint",
        "question": "For feline HCM, what should be separated between recognition and endpoints?",
        "must_see": "承认 recognition 和 endpoint 是两层。",
        "expected_question_type": "recognition",
        "expected_primary_family": "risk-and-recognition",
        "expected_primary_surface": "topics/hcm/risk-and-recognition.md",
    },
    {
        "id": "Q6",
        "topic": "IBD versus lymphoma boundary",
        "question": "Where is the current IBD versus small-cell lymphoma boundary in this vault?",
        "must_see": "应该像 boundary answer，不应像 generic disease summary。",
        "expected_question_type": "recognition",
        "expected_primary_family": "risk-and-recognition",
        "expected_primary_surface": "topics/ibd/risk-and-recognition.md",
    },
    {
        "id": "Q7",
        "topic": "Cross-disease question",
        "question": "Compare CKD and HCM on the maturity of their endpoint architecture.",
        "must_see": "要么稳妥回答，要么诚实降级，不能假精确。",
        "expected_question_type": "synthesis",
        "expected_primary_family": "disease-module-maturity-ladder",
        "expected_primary_surface": "system/indexes/disease-module-maturity-ladder.md",
    },
    {
        "id": "Q8",
        "topic": "Regulatory question",
        "question": "What is the current regulatory path surface for feline CKD programs across China, FDA, and VMD?",
        "must_see": "至少承认 jurisdiction split。",
        "expected_question_type": "regulatory",
        "expected_primary_family": "regulatory-brief",
        "expected_primary_surface": "topics/ckd/regulatory-brief.md",
    },
]

ORDINARY_USER_QUESTIONS = [
    {
        "id": "OU1",
        "topic": "CKD overview",
        "question": "解释CKD",
        "must_see": "普通用户能看懂的 CKD starter answer，证据和 next step 可见。",
        "expected_question_type": "overview",
        "expected_primary_family": "current-state-dashboard",
        "expected_primary_surface": "topics/ckd/current-state-dashboard.md",
    },
    {
        "id": "OU2",
        "topic": "FIP recognition",
        "question": "FIP怎么识别",
        "must_see": "识别 / workup 逻辑，不是 generic disease summary。",
        "expected_question_type": "recognition",
        "expected_primary_family": "risk-and-recognition",
        "expected_primary_surface": "topics/fip/risk-and-recognition.md",
    },
    {
        "id": "OU3",
        "topic": "HCM overview and risk",
        "question": "HCM是什么，为什么危险",
        "must_see": "解释为什么危险，而不是只给病名定义。",
        "expected_question_type": "overview",
        "expected_primary_family": "current-state-dashboard",
        "expected_primary_surface": "topics/hcm/current-state-dashboard.md",
    },
    {
        "id": "OU4",
        "topic": "IBD versus lymphoma boundary",
        "question": "IBD和淋巴瘤怎么区分",
        "must_see": "boundary answer，不是百科式概览。",
        "expected_question_type": "recognition",
        "expected_primary_family": "risk-and-recognition",
        "expected_primary_surface": "topics/ibd/risk-and-recognition.md",
    },
    {
        "id": "OU5",
        "topic": "Diabetes remission",
        "question": "糖尿病猫为什么会缓解",
        "must_see": "解释缓解不是治愈，并落到结果 / 缓解解释面。",
        "expected_question_type": "endpoints",
        "expected_primary_family": "endpoint-handbook",
        "expected_primary_surface": "topics/diabetes/endpoint-handbook.md",
    },
    {
        "id": "OU6",
        "topic": "Elevated creatinine worry",
        "question": "我的猫肌酐升高，这个库能告诉我什么",
        "must_see": "直接面向读者解释风险，并给出下一步页面。",
        "expected_question_type": "overview",
        "expected_primary_family": "current-state-dashboard",
        "expected_primary_surface": "topics/ckd/current-state-dashboard.md",
    },
]


SUITES = {
    "research": {
        "questions": QUESTIONS,
        "report_prefix": "ask-the-vault-acceptance-report",
        "title": "Ask The Vault Acceptance Report",
        "pass_min": 6,
        "pass_rule_lines": [
            "1. 8 个核心问题里至少 6 个答案可接受",
            "2. 0 个答案出现伪造 source id",
            "3. 0 个答案把明显推断伪装成 `quoted_fact`",
            "4. 至少 4 个答案能把用户直接带到最短答案面",
            "5. `--write-back` 产物 frontmatter 完整且文件名稳定",
            "6. 至少 1 个 cross-disease 问题被明确降级处理，而不是乱猜",
        ],
    },
    "ordinary-user": {
        "questions": ORDINARY_USER_QUESTIONS,
        "report_prefix": "ordinary-user-acceptance-report",
        "title": "Ordinary User Acceptance Report",
        "pass_min": 5,
        "pass_rule_lines": [
            "1. 6 个普通用户问题里至少 5 个答案可接受",
            "2. 每个通过答案都要有真实 source ids",
            "3. overview 问题要落到 current-state-dashboard 起步面",
            "4. recognition / endpoints 问题不能被误判成 generic overview",
            "5. answer 要能被普通读者扫读，并给出 next step",
        ],
    },
}


def today_stamp() -> str:
    return datetime.now().strftime("%Y%m%d")


def suite_config(suite: str) -> dict:
    return SUITES[suite]


def report_path(suite: str) -> Path:
    config = suite_config(suite)
    return REPORT_DIR / f"{config['report_prefix']}-{today_stamp()}.md"


def required_key_for_backend(backend: str) -> str:
    if backend == "openrouter":
        return "OPENROUTER_API_KEY"
    if backend == "anthropic":
        return "ANTHROPIC_API_KEY"
    return ""


def missing_budget_guard_for_backend(backend: str) -> str:
    if backend != "openrouter":
        return ""
    raw = os.environ.get("OPENROUTER_DAILY_BUDGET_USD", "").strip()
    if not raw:
        return "OPENROUTER_DAILY_BUDGET_USD"
    try:
        budget = float(raw)
    except ValueError:
        return "OPENROUTER_DAILY_BUDGET_USD:invalid"
    if budget <= 0 or budget > 1.00:
        return "OPENROUTER_DAILY_BUDGET_USD:outside-0-to-1"
    return ""


def render_header(suite: str, execution_mode: str, backend: str, write_back: bool, status: str) -> list[str]:
    config = suite_config(suite)
    return [
        "---",
        f"id: system-{config['report_prefix']}-{today_stamp()}",
        "type: health-check",
        "topic: operating-system",
        "question_type: acceptance",
        "language: zh",
        f"last_compiled_at: {datetime.now().date()}",
        "verification_status: compiled",
        "decision_grade: provisional",
        "language_qa_status: light_checked",
        "owner: codex",
        f"status: {status}",
        "---",
        "",
        f"# {config['title']}, {datetime.now().date()}",
        "",
        f"Suite: {suite}",
        f"Execution mode: {execution_mode}",
        f"Backend: {backend}",
        f"Write-back: {'on' if write_back else 'off'}",
        f"Acceptance status: {status}",
        "",
        "Pass rule reminder:",
        "",
        *config["pass_rule_lines"],
        "",
        "## Scoreboard",
        "",
        "| ID | Topic | Exit | QType | First Family | Strongest Surface | Clear Miss | Failure Type | Next Fix Layer | Source IDs | Confidence | Initial Read |",
        "|---|---|---:|---|---|---|---|---|---|---:|---|---|",
    ]


def run_one(question: str, backend: str, write_back: bool) -> dict:
    cmd = [
        sys.executable,
        "scripts/query.py",
        question,
        "--backend",
        backend,
    ]
    if write_back:
        cmd.append("--write-back")

    proc = subprocess.run(
        cmd,
        cwd=VAULT_ROOT,
        text=True,
        capture_output=True,
    )
    stdout = proc.stdout.strip()
    stderr = proc.stderr.strip()
    source_ids = parse_source_ids_from_answer(stdout)
    confidence = compute_confidence(stdout) if stdout else "low"
    runtime_blocker = classify_runtime_blocker(stderr)
    return {
        "exit_code": proc.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "source_ids": source_ids,
        "confidence": confidence,
        "runtime_blocker": runtime_blocker,
        "router_question_type": "",
        "first_family": "",
        "loaded_paths": [],
        "strongest_surface_hit": "manual-review",
        "clear_miss": "manual-review",
        "failure_type": "manual-review",
        "next_fix_layer": "manual-review",
    }


def classify_runtime_blocker(stderr: str) -> str:
    lowered = stderr.lower()
    if "authenticationerror" in lowered or "user not found" in lowered or "error code: 401" in lowered:
        return "backend-auth"
    if "operation not permitted" in lowered or "connecterror" in lowered:
        return "network"
    if "rate limit" in lowered or "429" in lowered:
        return "rate-limit"
    return ""


def run_one_route_only(question: str) -> dict:
    qtype = heuristic_question_type(question)
    disease = infer_disease_from_question(question)
    loaded_paths = heuristic_files_for_route(qtype, disease)
    source_ids: list[str] = []
    for rel in loaded_paths:
        path = VAULT_ROOT / rel
        if not path.exists():
            continue
        ids = parse_source_ids_from_frontmatter(path.read_text(encoding="utf-8"))
        for sid in ids:
            if sid not in source_ids:
                source_ids.append(sid)

    first_family = _classify_page_family(loaded_paths[0]) if loaded_paths else ""
    stderr_lines = [
        f"[meta] ROUTER_QTYPE={qtype}",
        f"[meta] ROUTER_DISEASE={disease}",
        f"[meta] FIRST_FAMILY={first_family}",
        f"[meta] LOADED_PATHS={','.join(loaded_paths) if loaded_paths else '(none)'}",
    ]
    return {
        "exit_code": 0 if loaded_paths else 1,
        "stdout": "",
        "stderr": "\n".join(stderr_lines),
        "source_ids": source_ids,
        "confidence": "route-only",
        "runtime_blocker": "",
        "router_question_type": qtype,
        "first_family": first_family,
        "loaded_paths": loaded_paths,
        "strongest_surface_hit": "manual-review",
        "clear_miss": "manual-review",
        "failure_type": "manual-review",
        "next_fix_layer": "manual-review",
    }


def infer_family(text: str) -> str:
    lowered = text.lower()
    family_markers = [
        ("mechanism-overview", "mechanism-overview"),
        ("endpoint-handbook", "endpoint-handbook"),
        ("risk-and-recognition", "risk-and-recognition"),
        ("translation-brief", "translation-brief"),
        ("regulatory-brief", "regulatory-brief"),
        ("synthesis-index", "synthesis-index"),
        ("current-state-dashboard", "current-state-dashboard"),
        ("verify-a-claim", "verify-a-claim"),
        ("disease-module-maturity-ladder", "disease-module-maturity-ladder"),
        ("src-reg-", "src-reg-source"),
    ]
    for needle, label in family_markers:
        if needle in lowered:
            return label
    return ""


def annotate_routing(item: dict, result: dict) -> None:
    stderr = result["stderr"]
    stdout = result["stdout"]

    def meta_value(key: str) -> str:
        prefix = f"{key}="
        for line in stderr.splitlines():
            if prefix in line:
                return line.split(prefix, 1)[1].strip()
        return ""

    qtype = meta_value("ROUTER_QTYPE")
    if not qtype and "→" in stderr:
        for line in stderr.splitlines():
            if "→" in line:
                fragment = line.split("→", 1)[1].strip()
                qtype = fragment.split("/", 1)[0].strip()
                break
    result["router_question_type"] = qtype

    first_family = meta_value("FIRST_FAMILY")
    if not first_family:
        first_family = infer_family(stderr) or infer_family(stdout)
    result["first_family"] = first_family

    loaded_paths: list[str] = []
    loaded_paths_meta = meta_value("LOADED_PATHS")
    if loaded_paths_meta and loaded_paths_meta != "(none)":
        for rel in loaded_paths_meta.split(","):
            rel = rel.strip()
            if rel and rel not in loaded_paths:
                loaded_paths.append(rel)
    router_files = meta_value("ROUTER_FILES")
    if router_files and router_files != "(none)":
        for rel in router_files.split(","):
            rel = rel.strip()
            if rel and rel not in loaded_paths:
                loaded_paths.append(rel)
    for line in stderr.splitlines():
        prefix = "[info] Loaded: "
        if line.startswith(prefix):
            rel = line[len(prefix):].strip()
            if rel and rel not in loaded_paths:
                loaded_paths.append(rel)
    result["loaded_paths"] = loaded_paths

    expected_surface = item.get("expected_primary_surface", "")
    strongest_surface_hit = "no"
    if expected_surface and expected_surface in loaded_paths:
        strongest_surface_hit = "yes"
    elif not expected_surface:
        strongest_surface_hit = "n/a"
    result["strongest_surface_hit"] = strongest_surface_hit

    clear_miss = "unknown"
    if item["expected_question_type"] and qtype and qtype != item["expected_question_type"]:
        clear_miss = "qtype-miss"
    elif item["expected_primary_family"] and first_family and first_family != item["expected_primary_family"]:
        clear_miss = "family-miss"
    elif qtype or first_family:
        clear_miss = "no"
    result["clear_miss"] = clear_miss

    failure_type = "manual-review"
    next_fix_layer = "manual-review"
    if clear_miss == "qtype-miss":
        failure_type = "qtype-miss"
        next_fix_layer = "qtype"
    elif clear_miss == "family-miss":
        failure_type = "family-miss"
        next_fix_layer = "family"
    elif result.get("runtime_blocker"):
        failure_type = f"runtime-blocked:{result['runtime_blocker']}"
        next_fix_layer = result["runtime_blocker"]
    elif result["strongest_surface_hit"] == "no":
        failure_type = "strongest-surface-miss"
        next_fix_layer = "family"
    elif result["exit_code"] != 0:
        failure_type = "execution-miss"
        next_fix_layer = "runtime"
    elif not result["source_ids"]:
        failure_type = "provenance-miss"
        next_fix_layer = "provenance"
    elif result["confidence"] == "low":
        failure_type = "answer-compression-miss"
        next_fix_layer = "answer-compression"
    elif clear_miss == "no":
        failure_type = "no-clear-failure"
        next_fix_layer = "none"

    result["failure_type"] = failure_type
    result["next_fix_layer"] = next_fix_layer


def summarize_row(item: dict, result: Optional[dict]) -> str:
    if result is None:
        return (
            f"| {item['id']} | {item['topic']} | — | {item['expected_question_type']} | "
            f"{item['expected_primary_family']} | pending | pending | pending | pending | — | — | pending |"
        )

    if result.get("confidence") == "route-only":
        initial = "route-pass" if result_is_acceptable(result) else "route-needs-review"
    else:
        initial = "pass-leaning" if result["exit_code"] == 0 and result["source_ids"] else "needs-review"
    return (
        f"| {item['id']} | {item['topic']} | {result['exit_code']} | "
        f"{result['router_question_type'] or '(none)'} | {result['first_family'] or '(none)'} | "
        f"{result['strongest_surface_hit']} | {result['clear_miss']} | {result['failure_type']} | {result['next_fix_layer']} | "
        f"{len(result['source_ids'])} | {result['confidence']} | {initial} |"
    )


def result_is_acceptable(result: dict) -> bool:
    if result.get("confidence") == "route-only":
        return (
            result["exit_code"] == 0
            and result["strongest_surface_hit"] in {"yes", "n/a"}
            and result["clear_miss"] == "no"
        )
    return (
        result["exit_code"] == 0
        and bool(result["source_ids"])
        and result["strongest_surface_hit"] in {"yes", "n/a"}
        and result["clear_miss"] == "no"
        and result["failure_type"] == "no-clear-failure"
        and result["confidence"] in {"high", "medium"}
    )


def acceptance_status(results: dict[str, dict], execution_mode: str, suite: str) -> str:
    if execution_mode == "template-only":
        return "template"
    if execution_mode.startswith("blocked"):
        return "blocked"
    acceptable = sum(1 for result in results.values() if result_is_acceptable(result))
    no_execution_failures = all(result["exit_code"] == 0 for result in results.values())
    no_qtype_or_family_miss = all(
        result["clear_miss"] in {"no", "unknown"} for result in results.values()
    )
    no_missing_sources = all(result["source_ids"] for result in results.values())
    if execution_mode == "route-only":
        if acceptable >= int(suite_config(suite)["pass_min"]) and no_execution_failures and no_qtype_or_family_miss:
            return "route_pass"
        return "route_needs_review"
    pass_min = int(suite_config(suite)["pass_min"])
    if acceptable >= pass_min and no_execution_failures and no_qtype_or_family_miss and no_missing_sources:
        return "pass"
    return "needs_review"


def render_acceptance_summary(results: dict[str, dict], execution_mode: str, status: str, suite: str) -> list[str]:
    if execution_mode == "template-only":
        return ["", "Acceptance summary: template only; no queries executed."]
    if execution_mode.startswith("blocked"):
        completed = len(results)
        return ["", f"Acceptance summary: blocked during query execution after {completed} run(s)."]
    acceptable = sum(1 for result in results.values() if result_is_acceptable(result))
    execution_failures = sum(1 for result in results.values() if result["exit_code"] != 0)
    missing_sources = sum(1 for result in results.values() if not result["source_ids"])
    route_misses = sum(
        1 for result in results.values() if result["clear_miss"] in {"qtype-miss", "family-miss"}
    )
    total = len(suite_config(suite)["questions"])
    route_note = ""
    read_label = "automated pass-leaning answers"
    if execution_mode == "route-only":
        read_label = "route checks"
        route_note = " Route-only checks routing and source-surface availability; it does not judge final answer quality."
    return [
        "",
        f"Acceptance summary: {acceptable}/{total} {read_label}; "
        f"{execution_failures} execution failures; {missing_sources} provenance misses; "
        f"{route_misses} route misses. Status: {status}.{route_note}",
    ]


def render_question_block(item: dict, result: Optional[dict]) -> list[str]:
    lines = [
        "",
        f"## {item['id']}. {item['topic']}",
        "",
        f"Question: `{item['question']}`",
        "",
        f"Must see: {item['must_see']}",
        f"Expected question_type: `{item['expected_question_type']}`",
        f"Expected primary family: `{item['expected_primary_family']}`",
        f"Expected strongest surface: `{item['expected_primary_surface']}`",
        "",
    ]

    if result is None:
        lines.extend([
            "Status: pending",
            "",
            "Routing read:",
            "",
            "- router question_type: pending",
            "- first family: pending",
            "- strongest surface hit: pending",
            "- clear miss: pending",
            "- failure type: pending",
            "- next fix layer: pending",
            "",
            "Result excerpt:",
            "",
            "_Not executed yet._",
        ])
        return lines

    lines.extend([
        f"Exit code: `{result['exit_code']}`",
        f"Confidence: `{result['confidence']}`",
        f"Source IDs found: `{', '.join(result['source_ids']) if result['source_ids'] else 'none'}`",
        "",
        "Routing read:",
        "",
        f"- router question_type: `{result['router_question_type'] or '(none)'}`",
        f"- first family: `{result['first_family'] or '(none)'}`",
        f"- strongest surface hit: `{result['strongest_surface_hit']}`",
        f"- clear miss: `{result['clear_miss']}`",
        f"- failure type: `{result['failure_type']}`",
        f"- next fix layer: `{result['next_fix_layer']}`",
        f"- loaded paths: `{', '.join(result['loaded_paths']) if result['loaded_paths'] else '(none)'}`",
        "",
        "stderr:",
        "",
        "```text",
        result["stderr"][:4000] if result["stderr"] else "(empty)",
        "```",
        "",
        "Result excerpt:",
        "",
        "```text",
        report_excerpt(result["stdout"], 6000) if result["stdout"] else "(empty)",
        "```",
    ])
    return lines


def report_excerpt(text: str, limit: int) -> str:
    excerpt = text[:limit]
    # Acceptance reports live under system/health-checks, so relative markdown
    # links emitted by an answer become false broken links in repo-wide linting.
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", excerpt)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run or scaffold Ask The Vault acceptance.")
    parser.add_argument("--suite", choices=sorted(SUITES), default="research")
    parser.add_argument("--backend", choices=["anthropic", "ollama", "openrouter"], default="anthropic")
    parser.add_argument("--write-back", action="store_true", help="Pass --write-back through to query.py")
    parser.add_argument("--template-only", action="store_true", help="Create the report skeleton without executing queries")
    parser.add_argument("--route-only", action="store_true", help="Run deterministic routing checks without calling an LLM")
    args = parser.parse_args()

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = report_path(args.suite)
    questions = suite_config(args.suite)["questions"]

    execution_mode = "template-only" if args.template_only else "executed"
    if args.route_only:
        execution_mode = "route-only"
    results = {}
    missing_key = ""
    missing_budget_guard = ""
    if not args.template_only and not args.route_only:
        required_key = required_key_for_backend(args.backend)
        if required_key and not os.environ.get(required_key):
            execution_mode = f"blocked-missing-key:{required_key}"
            missing_key = required_key
        else:
            missing_budget_guard = missing_budget_guard_for_backend(args.backend)
            if missing_budget_guard:
                execution_mode = f"blocked-budget-guard:{missing_budget_guard}"
    if args.route_only:
        for item in questions:
            results[item["id"]] = run_one_route_only(item["question"])
            annotate_routing(item, results[item["id"]])
    elif not args.template_only and not missing_key and not missing_budget_guard:
        for item in questions:
            results[item["id"]] = run_one(item["question"], args.backend, args.write_back)
            annotate_routing(item, results[item["id"]])
            blocker = results[item["id"]].get("runtime_blocker")
            if blocker:
                execution_mode = f"blocked-runtime:{blocker}"
                break

    status = acceptance_status(results, execution_mode, args.suite)
    lines = render_header(
        suite=args.suite,
        execution_mode=execution_mode,
        backend=args.backend,
        write_back=args.write_back,
        status=status,
    )

    for item in questions:
        lines.append(summarize_row(item, results.get(item["id"])))

    lines.extend(render_acceptance_summary(results, execution_mode, status, args.suite))
    if missing_key:
        lines.extend([
            "",
            f"Blocked reason: `{missing_key}` is not set in the current shell.",
            "",
            "Set the key, then rerun:",
            "",
            "```bash",
            f"python3 scripts/run_acceptance_checklist.py --backend {args.backend}",
            "```",
        ])
    elif execution_mode.startswith("blocked-runtime:"):
        blocker = execution_mode.split(":", 1)[1]
        lines.extend([
            "",
            f"Blocked reason: runtime blocker `{blocker}`.",
            "",
            "This is not an answer-quality or routing failure. Fix the backend/runtime condition, then rerun the same suite.",
        ])

    lines.extend([
        "",
        "## Detailed Runs",
    ])

    for item in questions:
        lines.extend(render_question_block(item, results.get(item["id"])))

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(path)
    if missing_key:
        sys.exit(2)
    if status == "blocked":
        sys.exit(2)
    if status in {"needs_review", "route_needs_review"}:
        sys.exit(1)


if __name__ == "__main__":
    main()
