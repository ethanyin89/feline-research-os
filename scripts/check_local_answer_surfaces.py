#!/usr/bin/env python3
"""Check deterministic no-API local answer surfaces used by public_test_app."""

from __future__ import annotations

import re
from pathlib import Path

from local_answer_surfaces import build_local_surface_answer
from query import build_source_index, parse_source_ids_from_answer


ROOT = Path(__file__).resolve().parent.parent


CASES = [
    {
        "question": "FIP怎么识别",
        "disease": "fip",
        "question_type": "recognition",
        "mode": "local_surface",
        "surface": "fip_recognition",
        "min_sources": 3,
        "must_contain": [
            "FIP怎么识别",
            "立即就医",
            "不能仅靠单一症状",
            "src-fip-006",
            "没有调用 API",
        ],
    },
    {
        "question": "FIP药效评价指标",
        "disease": "fip",
        "question_type": "endpoints",
        "mode": "local_surface",
        "surface": "fip_endpoint",
        "min_sources": 10,
        "must_contain": [
            "Key-Claim Traceability",
            "FE1",
            "Endpoint Hierarchy",
            "topics/fip/endpoint-handbook.md",
            "没有调用 API",
        ],
    },
    {
        "question": "GS-441524疗效证据",
        "disease": "fip",
        "question_type": "treatment",
        "mode": "local_surface",
        "surface": "fip_treatment_evidence",
        "min_sources": 6,
        "must_contain": [
            "Key-Claim Traceability",
            "FT1",
            "src-fip-016",
            "topics/fip/translation-brief.md",
            "没有调用 API",
        ],
    },
    {
        "question": "什么是FIP",
        "disease": "fip",
        "question_type": "overview",
        "mode": "local_surface",
        "surface": "fip_what_is",
        "min_sources": 3,
        "must_contain": [
            "什么是FIP",
            "简单回答",
            "src-fip-003",
            "不能替代兽医诊断",
            "没有调用 API",
        ],
    },
    {
        "question": "CKD endpoint",
        "disease": "ckd",
        "question_type": "endpoints",
        "mode": "local_surface",
        "surface": "ckd_endpoint",
        "min_sources": 10,
        "must_contain": [
            "Key-Claim Traceability",
            "Endpoint Hierarchy",
            "topics/ckd/endpoint-handbook.md",
            "No API call was made",
        ],
    },
    {
        "question": "CKD治疗证据",
        "disease": "ckd",
        "question_type": "treatment",
        "mode": "local_surface",
        "surface": "ckd_treatment_evidence",
        "min_sources": 10,
        "must_contain": [
            "Key-Claim Traceability",
            "topics/ckd/translation-brief.md",
            "没有调用 API",
        ],
    },
    {
        "question": "current understanding of feline CKD",
        "disease": "ckd",
        "question_type": "overview",
        "mode": "local_surface",
        "surface": "ckd_researcher_overview",
        "min_sources": 8,
        "must_contain": [
            "Researcher Map",
            "Evidence Backbone",
            "Key-Claim Traceability",
            "topics/ckd/mechanism-overview.md",
            "No API call was made",
        ],
    },
    {
        "question": "HCM评价指标",
        "disease": "hcm",
        "question_type": "endpoints",
        "mode": "local_surface",
        "surface": "hcm_endpoint",
        "min_sources": 8,
        "must_contain": [
            "Key-Claim Traceability",
            "Endpoint Hierarchy",
            "topics/hcm/endpoint-handbook.md",
            "没有调用 API",
        ],
    },
    {
        "question": "IBD endpoint",
        "disease": "ibd",
        "question_type": "endpoints",
        "mode": "local_surface",
        "surface": "ibd_endpoint",
        "min_sources": 7,
        "must_contain": [
            "Key-Claim Traceability",
            "Endpoint Hierarchy",
            "topics/ibd/endpoint-handbook.md",
            "No API call was made",
        ],
    },
    {
        "question": "糖尿病疗效评价指标",
        "disease": "diabetes",
        "question_type": "endpoints",
        "mode": "local_surface",
        "surface": "diabetes_endpoint",
        "min_sources": 10,
        "must_contain": [
            "Key-Claim Traceability",
            "Endpoint Hierarchy",
            "topics/diabetes/endpoint-handbook.md",
            "没有调用 API",
        ],
    },
    {
        "question": "FCV治疗证据",
        "disease": "fcv",
        "question_type": "treatment",
        "mode": "local_surface",
        "surface": "fcv_treatment_evidence",
        "min_sources": 10,
        "must_contain": [
            "Key-Claim Traceability",
            "Translation Boundaries",
            "topics/fcv/translation-brief.md",
            "没有调用 API",
        ],
    },
]


def main() -> int:
    source_index = build_source_index(ROOT)
    failures: list[str] = []

    print("# Local Answer Surface Check")
    print()
    for case in CASES:
        question = str(case["question"])
        result = build_local_surface_answer(question, ROOT)
        if result is None:
            failures.append(f"{question}: no surface matched")
            print(f"## {question}\n- status: FAIL\n- reason: no surface matched\n")
            continue

        answer = str(result["answer"])
        cited = parse_source_ids_from_answer(answer)
        loaded = list(result["loaded_source_ids"])
        missing_text = [needle for needle in case["must_contain"] if str(needle) not in answer]
        missing_loaded = [sid for sid in cited if sid not in loaded]
        nonexistent = [sid for sid in cited if sid not in source_index]
        trace = "; ".join(str(step.get("detail", "")) for step in result["research_trace"])
        checks = {
            "disease": result["disease"] == case["disease"],
            "question_type": result["question_type"] == case["question_type"],
            "mode": result["answer_mode"] == case["mode"],
            "surface": result["first_family_loaded"] == case["surface"],
            "sources": len(loaded) >= int(case["min_sources"]),
            "has_source_tags": bool(cited),
            "cited_sources_loaded": not missing_loaded,
            "cited_sources_exist": not nonexistent,
            "api0": "api_calls=0" in trace and ("没有调用 API" in answer or "No API call was made" in answer),
            "must_contain": not missing_text,
        }

        status = "PASS" if all(checks.values()) else "FAIL"
        print(f"## {question}")
        print(f"- status: {status}")
        print(f"- disease: {result['disease']}")
        print(f"- question_type: {result['question_type']}")
        print(f"- mode: {result['answer_mode']}")
        print(f"- sources: {len(loaded)}")
        print(f"- cited_sources: {len(cited)}")
        print(f"- first_family_loaded: {result['first_family_loaded']}")
        if missing_text:
            print(f"- missing_text: {', '.join(missing_text)}")
        if missing_loaded:
            print(f"- cited_not_loaded: {', '.join(missing_loaded)}")
        if nonexistent:
            print(f"- cited_nonexistent: {', '.join(nonexistent)}")
        print()

        if status == "FAIL":
            bad = ", ".join(name for name, ok in checks.items() if not ok)
            failures.append(f"{question}: {bad}")

    if failures:
        print("FAILURES:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("All local answer surfaces passed without API calls.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
