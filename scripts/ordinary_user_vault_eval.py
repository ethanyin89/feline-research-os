#!/usr/bin/env python3
"""Run ordinary-user free-mode checks for the Streamlit vault answer surface.

This script does not call paid APIs. It exercises the app-local Vault Search
answer path with high-visibility ordinary-user prompts.
"""

from __future__ import annotations

import contextlib
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"


SAMPLES = [
    {
        "question": "解释CKD",
        "expected_disease": "ckd",
        "expected_mode": "local_explanation",
        "expected_surface": "ckd_overview",
        "min_sources": 4,
    },
    {
        "question": "FIP怎么识别",
        "expected_disease": "fip",
        "expected_mode": "local_explanation",
        "expected_surface": "fip_recognition",
        "min_sources": 4,
    },
    {
        "question": "HCM是什么，为什么危险",
        "expected_disease": "hcm",
        "expected_mode": "local_explanation",
        "expected_surface": "hcm_overview",
        "min_sources": 4,
    },
    {
        "question": "IBD和淋巴瘤怎么区分",
        "expected_disease": "ibd",
        "expected_mode": "local_explanation",
        "expected_surface": "ibd_lymphoma",
        "min_sources": 4,
    },
    {
        "question": "猫肥胖症siRNA",
        "expected_disease": "obesity",
        "expected_mode": "local_search",
        "expected_surface": "none",
        "min_sources": 1,
        "must_contain": "没有找到",
    },
    {
        "question": "What endpoints are usable for feline CKD efficacy evaluation?",
        "expected_disease": "ckd",
        "expected_mode": "local_explanation",
        "expected_surface": "ckd_endpoint",
        "min_sources": 4,
    },
]


def import_app():
    """Import Streamlit app helpers while suppressing bare-mode UI warnings."""
    sys.path.insert(0, str(SCRIPTS))
    with open(os.devnull, "w", encoding="utf-8") as devnull:
        with contextlib.redirect_stderr(devnull):
            import app  # type: ignore

    return app


def has_hit_list_failure(answer: str) -> bool:
    """Detect the old failure mode: broad user prompt returns only hit lists."""
    first_line = answer.strip().split("\n", 1)[0]
    return (
        first_line.startswith("这是本地 vault 检索结果")
        or first_line.startswith("This is local vault retrieval")
    ) and ("## 本地命中" in answer or "## Local hits" in answer)


def main() -> int:
    app = import_app()
    source_index = app.build_source_index(ROOT)
    failures: list[str] = []

    print("# Ordinary User Vault Eval")
    print()
    for sample in SAMPLES:
        question = sample["question"]
        result = app.run_app_local_query_core(question, ROOT, source_index)
        answer = result["answer"]
        trace = "; ".join(str(step.get("detail", "")) for step in result["research_trace"])
        sections = len(re.findall(r"^## ", answer, flags=re.MULTILINE))
        surface = "none"
        match = re.search(r"surface=([^;]+)", trace)
        if match:
            surface = match.group(1)

        checks = {
            "disease": result["disease"] == sample["expected_disease"],
            "mode": result["answer_mode"] == sample["expected_mode"],
            "surface": surface == sample["expected_surface"],
            "api0": "api_calls=0" in trace,
            "sources": len(result["loaded_source_ids"]) >= int(sample["min_sources"]),
            "sections": sections >= 3,
            "not_hit_list_only": not has_hit_list_failure(answer),
        }
        if "must_contain" in sample:
            checks["must_contain"] = str(sample["must_contain"]) in answer

        status = "PASS" if all(checks.values()) else "FAIL"
        print(f"## {question}")
        print(f"- status: {status}")
        print(f"- disease: {result['disease']}")
        print(f"- mode: {result['answer_mode']}")
        print(f"- surface: {surface}")
        print(f"- sources: {len(result['loaded_source_ids'])}")
        print(f"- sections: {sections}")
        print(f"- first_line: {answer.splitlines()[0] if answer.splitlines() else ''}")
        print()

        if status == "FAIL":
            bad = ", ".join(name for name, ok in checks.items() if not ok)
            failures.append(f"{question}: {bad}")

    if failures:
        print("FAILURES:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("All ordinary-user free-mode samples passed without API calls.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
