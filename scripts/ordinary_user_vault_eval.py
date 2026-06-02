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
        "quality_groups": [
            ["猫 CKD", "慢性肾脏疾病"],
            ["怎么发现", "判断", "recognized"],
            ["creatinine", "肌酐"],
            ["USG", "尿比重"],
            ["UPCR", "蛋白尿"],
            ["血压", "blood pressure"],
            ["phosphorus", "磷"],
            ["SDMA"],
            ["renal diet", "肾脏专用饮食"],
            ["不能", "Do not"],
            ["Wikipedia", "维基百科"],
            ["下一步", "Next Step"],
        ],
    },
    {
        "question": "the explanation of feline CKD",
        "expected_disease": "ckd",
        "expected_mode": "local_explanation",
        "expected_surface": "ckd_overview",
        "min_sources": 4,
        "quality_groups": [
            ["feline CKD", "feline chronic kidney disease"],
            ["Researcher Lens"],
            ["How It Is Recognized"],
            ["creatinine"],
            ["USG"],
            ["UPCR", "proteinuria"],
            ["blood pressure"],
            ["phosphorus"],
            ["SDMA"],
            ["renal diet"],
            ["Do Not Overstate"],
            ["Wikipedia"],
            ["Next Step"],
        ],
    },
    {
        "question": "current understanding of feline CKD",
        "expected_disease": "ckd",
        "expected_mode": "local_explanation",
        "expected_surface": "ckd_overview",
        "min_sources": 4,
        "quality_groups": [
            ["feline CKD", "feline chronic kidney disease"],
            ["Researcher Lens"],
            ["disease model"],
            ["How It Is Recognized"],
            ["creatinine"],
            ["USG"],
            ["proteinuria", "UPCR"],
            ["phosphorus"],
            ["renal diet"],
            ["Do Not Overstate"],
            ["Next Step"],
        ],
    },
    {
        "question": "what should a researcher know about feline CKD",
        "expected_disease": "ckd",
        "expected_mode": "local_explanation",
        "expected_surface": "ckd_overview",
        "min_sources": 4,
        "quality_groups": [
            ["feline CKD", "feline chronic kidney disease"],
            ["Researcher Lens"],
            ["diagnostic markers"],
            ["prognostic markers"],
            ["trial endpoints"],
            ["creatinine"],
            ["SDMA"],
            ["renal diet"],
            ["Do Not Overstate"],
            ["Next Step"],
        ],
    },
    {
        "question": "FIP怎么识别",
        "expected_disease": "fip",
        "expected_mode": "local_explanation",
        "expected_surface": "fip_recognition",
        "min_sources": 4,
        "quality_groups": [
            ["FIP"],
            ["识别", "recognition"],
            ["不能靠一个症状", "one-symptom", "one-test"],
            ["effusive", "non-effusive"],
            ["诊断", "diagnostic"],
            ["下一步", "Next Step"],
        ],
    },
    {
        "question": "current understanding of feline FIP",
        "expected_disease": "fip",
        "expected_mode": "local_explanation",
        "expected_surface": "fip_overview",
        "min_sources": 4,
        "quality_groups": [
            ["FIP", "feline infectious peritonitis"],
            ["Researcher Lens"],
            ["decision model"],
            ["effusive"],
            ["non-effusive"],
            ["diagnostic uncertainty"],
            ["GS-441524", "remdesivir"],
            ["Do Not Overstate"],
            ["Next Step"],
        ],
    },
    {
        "question": "what should a researcher know about feline FIP",
        "expected_disease": "fip",
        "expected_mode": "local_explanation",
        "expected_surface": "fip_overview",
        "min_sources": 4,
        "quality_groups": [
            ["FIP", "feline infectious peritonitis"],
            ["Researcher Lens"],
            ["risk"],
            ["presentation"],
            ["testing"],
            ["treatment timing"],
            ["neurologic"],
            ["ocular"],
            ["Next Step"],
        ],
    },
    {
        "question": "feline FIP disease model overview",
        "expected_disease": "fip",
        "expected_mode": "local_explanation",
        "expected_surface": "fip_overview",
        "min_sources": 4,
        "quality_groups": [
            ["FIP", "feline infectious peritonitis"],
            ["disease form"],
            ["diagnostic-test boundaries"],
            ["antiviral-era actionability"],
            ["effusive"],
            ["non-effusive"],
            ["Do Not Overstate"],
            ["Next Step"],
        ],
    },
    {
        "question": "HCM是什么，为什么危险",
        "expected_disease": "hcm",
        "expected_mode": "local_explanation",
        "expected_surface": "hcm_overview",
        "min_sources": 4,
        "quality_groups": [
            ["HCM"],
            ["心肌", "myocardial"],
            ["为什么危险", "Why It Is Risky"],
            ["echocardiography", "超声"],
            ["biomarker"],
            ["不能", "should not"],
            ["下一步", "Next Step"],
        ],
    },
    {
        "question": "what should a researcher know about feline HCM",
        "expected_disease": "hcm",
        "expected_mode": "local_explanation",
        "expected_surface": "hcm_overview",
        "min_sources": 4,
        "quality_groups": [
            ["HCM"],
            ["Researcher Lens"],
            ["structural phenotype"],
            ["biomarkers"],
            ["AI screening"],
            ["genotype"],
            ["treatment evidence"],
            ["intervention hierarchy"],
            ["Next Step"],
        ],
    },
    {
        "question": "current understanding of feline HCM",
        "expected_disease": "hcm",
        "expected_mode": "local_explanation",
        "expected_surface": "hcm_overview",
        "min_sources": 4,
        "quality_groups": [
            ["HCM"],
            ["Researcher Lens"],
            ["phenotype definition"],
            ["echocardiography"],
            ["remodeling"],
            ["biomarker"],
            ["Why It Is Risky"],
            ["Next Step"],
        ],
    },
    {
        "question": "IBD和淋巴瘤怎么区分",
        "expected_disease": "ibd",
        "expected_mode": "local_explanation",
        "expected_surface": "ibd_lymphoma",
        "min_sources": 4,
        "quality_groups": [
            ["IBD"],
            ["淋巴瘤", "lymphoma"],
            ["区分", "鉴别", "versus"],
            ["活检", "biopsy"],
            ["marker"],
            ["不能", "should not"],
            ["下一步", "Next Step"],
        ],
    },
    {
        "question": "what should a researcher know about feline IBD and lymphoma",
        "expected_disease": "ibd",
        "expected_mode": "local_explanation",
        "expected_surface": "ibd_lymphoma",
        "min_sources": 4,
        "quality_groups": [
            ["IBD"],
            ["lymphoma"],
            ["Researcher Lens"],
            ["boundary compression"],
            ["chronic enteropathy"],
            ["food response"],
            ["biopsy site"],
            ["integrated pathology"],
            ["diet response"],
            ["Next Step"],
        ],
    },
    {
        "question": "current understanding of feline IBD versus lymphoma",
        "expected_disease": "ibd",
        "expected_mode": "local_explanation",
        "expected_surface": "ibd_lymphoma",
        "min_sources": 4,
        "quality_groups": [
            ["IBD"],
            ["lymphoma"],
            ["Researcher Lens"],
            ["one-marker problem"],
            ["workup sequencing"],
            ["muscularis thickening"],
            ["Bcl-2"],
            ["standalone separator"],
            ["Next Step"],
        ],
    },
    {
        "question": "猫肥胖症siRNA",
        "expected_disease": "obesity",
        "expected_mode": "local_search",
        "expected_surface": "none",
        "min_sources": 1,
        "must_contain": "没有找到",
        "quality_groups": [
            ["没有找到"],
            ["siRNA"],
            ["本地", "local"],
            ["Google", "未入库", "API"],
        ],
    },
    {
        "question": "what should a researcher know about feline diabetes",
        "expected_disease": "diabetes",
        "expected_mode": "local_explanation",
        "expected_surface": "diabetes_overview",
        "min_sources": 4,
        "quality_groups": [
            ["feline diabetes"],
            ["Researcher Lens"],
            ["mixed metabolic/endocrine syndrome"],
            ["remission"],
            ["SGLT2"],
            ["ketone monitoring"],
            ["Do Not Overstate"],
            ["Next Step"],
        ],
    },
    {
        "question": "current understanding of feline diabetes",
        "expected_disease": "diabetes",
        "expected_mode": "local_explanation",
        "expected_surface": "diabetes_overview",
        "min_sources": 4,
        "quality_groups": [
            ["feline diabetes"],
            ["beta-cell failure"],
            ["obesity-driven insulin resistance"],
            ["pancreatitis"],
            ["diet"],
            ["insulin"],
            ["SGLT2"],
            ["protocol ranking"],
            ["Next Step"],
        ],
    },
    {
        "question": "解释猫糖尿病",
        "expected_disease": "diabetes",
        "expected_mode": "local_explanation",
        "expected_surface": "diabetes_overview",
        "min_sources": 4,
        "quality_groups": [
            ["猫糖尿病"],
            ["研究者视角"],
            ["mixed metabolic/endocrine syndrome"],
            ["remission"],
            ["SGLT2"],
            ["不能说过头"],
            ["下一步"],
        ],
    },
    {
        "question": "猫糖尿病是什么",
        "expected_disease": "diabetes",
        "expected_mode": "local_explanation",
        "expected_surface": "diabetes_overview",
        "min_sources": 4,
        "quality_groups": [
            ["猫糖尿病"],
            ["研究者视角"],
            ["remission"],
            ["SGLT2"],
            ["不能说过头"],
            ["下一步"],
        ],
    },
    {
        "question": "what should a researcher know about feline FCV",
        "expected_disease": "fcv",
        "expected_mode": "local_explanation",
        "expected_surface": "fcv_overview",
        "min_sources": 4,
        "quality_groups": [
            ["FCV", "feline calicivirus"],
            ["Researcher Lens"],
            ["vaccine"],
            ["cellular versus humoral"],
            ["VS-FCV"],
            ["carrier persistence"],
            ["Do Not Overstate"],
            ["Next Step"],
        ],
    },
    {
        "question": "current understanding of feline calicivirus",
        "expected_disease": "fcv",
        "expected_mode": "local_explanation",
        "expected_surface": "fcv_overview",
        "min_sources": 4,
        "quality_groups": [
            ["feline calicivirus"],
            ["vaccine/immunity complexity"],
            ["epidemiology"],
            ["therapy limits"],
            ["tissue tropism"],
            ["routine upper respiratory"],
            ["protection claim"],
            ["Next Step"],
        ],
    },
    {
        "question": "解释猫杯状病毒",
        "expected_disease": "fcv",
        "expected_mode": "local_explanation",
        "expected_surface": "fcv_overview",
        "min_sources": 4,
        "quality_groups": [
            ["猫杯状病毒"],
            ["研究者视角"],
            ["vaccine"],
            ["VS-FCV"],
            ["therapy"],
            ["不能说过头"],
            ["下一步"],
        ],
    },
    {
        "question": "猫杯状病毒是什么",
        "expected_disease": "fcv",
        "expected_mode": "local_explanation",
        "expected_surface": "fcv_overview",
        "min_sources": 4,
        "quality_groups": [
            ["猫杯状病毒"],
            ["研究者视角"],
            ["vaccine"],
            ["VS-FCV"],
            ["不能说过头"],
            ["下一步"],
        ],
    },
    {
        "question": "what should a researcher know about feline obesity",
        "expected_disease": "obesity",
        "expected_mode": "local_explanation",
        "expected_surface": "obesity_overview",
        "min_sources": 4,
        "quality_groups": [
            ["feline obesity"],
            ["Evidence-Depth Caveat"],
            ["Researcher Lens"],
            ["intrinsic and extrinsic"],
            ["insulin sensitivity"],
            ["post-gonadectomy kittens"],
            ["Do Not Overstate"],
            ["Next Step"],
        ],
    },
    {
        "question": "current understanding of feline obesity",
        "expected_disease": "obesity",
        "expected_mode": "local_explanation",
        "expected_surface": "obesity_overview",
        "min_sources": 4,
        "quality_groups": [
            ["feline obesity"],
            ["compiled starter"],
            ["prevalence range"],
            ["associated conditions"],
            ["diabetes-bridge"],
            ["effect-size rankings"],
            ["weight-loss protocols"],
            ["Next Step"],
        ],
    },
    {
        "question": "解释猫肥胖",
        "expected_disease": "obesity",
        "expected_mode": "local_explanation",
        "expected_surface": "obesity_overview",
        "min_sources": 4,
        "quality_groups": [
            ["猫肥胖"],
            ["证据深度"],
            ["研究者视角"],
            ["insulin sensitivity"],
            ["post-gonadectomy kittens"],
            ["不能说过头"],
            ["下一步"],
        ],
    },
    {
        "question": "猫肥胖是什么",
        "expected_disease": "obesity",
        "expected_mode": "local_explanation",
        "expected_surface": "obesity_overview",
        "min_sources": 4,
        "quality_groups": [
            ["猫肥胖"],
            ["证据深度"],
            ["研究者视角"],
            ["insulin sensitivity"],
            ["不能说过头"],
            ["下一步"],
        ],
    },
    {
        "question": "what should a researcher know about feline cancer",
        "expected_disease": "cancer",
        "expected_mode": "local_explanation",
        "expected_surface": "cancer_overview",
        "min_sources": 4,
        "quality_groups": [
            ["feline cancer"],
            ["Evidence-Depth Caveat"],
            ["Researcher Lens"],
            ["clinical workflow"],
            ["tumor family"],
            ["denominator-labeled"],
            ["Do Not Overstate"],
            ["Next Step"],
        ],
    },
    {
        "question": "current understanding of feline cancer",
        "expected_disease": "cancer",
        "expected_mode": "local_explanation",
        "expected_surface": "cancer_overview",
        "min_sources": 4,
        "quality_groups": [
            ["feline cancer"],
            ["architecture-level only"],
            ["lymphoma"],
            ["mammary carcinoma"],
            ["oral SCC"],
            ["injection-site sarcoma"],
            ["rank treatments"],
            ["Next Step"],
        ],
    },
    {
        "question": "解释猫肿瘤",
        "expected_disease": "cancer",
        "expected_mode": "local_explanation",
        "expected_surface": "cancer_overview",
        "min_sources": 4,
        "quality_groups": [
            ["猫肿瘤"],
            ["证据深度"],
            ["研究者视角"],
            ["clinical workflow"],
            ["tumor family"],
            ["不能说过头"],
            ["下一步"],
        ],
    },
    {
        "question": "猫肿瘤是什么",
        "expected_disease": "cancer",
        "expected_mode": "local_explanation",
        "expected_surface": "cancer_overview",
        "min_sources": 4,
        "quality_groups": [
            ["猫肿瘤"],
            ["证据深度"],
            ["研究者视角"],
            ["clinical workflow"],
            ["不能说过头"],
            ["下一步"],
        ],
    },
    {
        "question": "猫癌症是什么",
        "expected_disease": "cancer",
        "expected_mode": "local_explanation",
        "expected_surface": "cancer_overview",
        "min_sources": 4,
        "quality_groups": [
            ["猫肿瘤", "猫癌症"],
            ["证据深度"],
            ["研究者视角"],
            ["tumor family"],
            ["不能说过头"],
            ["下一步"],
        ],
    },
    {
        "question": "What endpoints are usable for feline CKD efficacy evaluation?",
        "expected_disease": "ckd",
        "expected_mode": "local_explanation",
        "expected_surface": "ckd_endpoint",
        "min_sources": 4,
        "quality_groups": [
            ["endpoint"],
            ["creatinine"],
            ["USG"],
            ["UPCR", "proteinuria"],
            ["blood pressure"],
            ["phosphorus"],
            ["SDMA"],
            ["should not rely on one marker"],
            ["Next Step"],
        ],
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


def has_quality_groups(answer: str, groups: list[list[str]]) -> tuple[bool, list[str]]:
    """Check ordinary-user answer quality by requiring one term per group."""
    missing: list[str] = []
    folded = answer.lower()
    for group in groups:
        if not any(term.lower() in folded for term in group):
            missing.append("/".join(group))
    return not missing, missing


def source_trace_failures(app, answer: str, loaded_source_ids: list[str], source_index: dict) -> dict[str, list[str]]:
    """Return cited source IDs that are nonexistent or absent from loaded context."""
    cited = app.parse_source_ids_from_answer(answer)
    loaded = set(loaded_source_ids)
    return {
        "cited": cited,
        "missing_loaded": [sid for sid in cited if sid not in loaded],
        "nonexistent": [sid for sid in cited if sid not in source_index],
    }


def has_cjk_text(text: str) -> bool:
    """Return True when text contains Chinese/Japanese/Korean ideographs."""
    return bool(re.search(r"[\u4e00-\u9fff]", text))


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
        trace_failures = source_trace_failures(app, answer, result["loaded_source_ids"], source_index)
        checks["cited_sources_exist"] = not trace_failures["nonexistent"]
        checks["cited_sources_loaded"] = not trace_failures["missing_loaded"]
        if sample["expected_mode"] == "local_explanation":
            checks["has_source_tags"] = bool(trace_failures["cited"])
        if app.detect_chinese(question) and sample["expected_mode"] == "local_explanation":
            checks["language_matches_question"] = has_cjk_text(answer[:800])

        quality_missing: list[str] = []
        if "quality_groups" in sample:
            ok, quality_missing = has_quality_groups(answer, sample["quality_groups"])  # type: ignore[arg-type]
            checks["answer_quality"] = ok
        if "must_contain" in sample:
            checks["must_contain"] = str(sample["must_contain"]) in answer

        status = "PASS" if all(checks.values()) else "FAIL"
        print(f"## {question}")
        print(f"- status: {status}")
        print(f"- disease: {result['disease']}")
        print(f"- mode: {result['answer_mode']}")
        print(f"- surface: {surface}")
        print(f"- sources: {len(result['loaded_source_ids'])}")
        print(f"- cited_sources: {len(trace_failures['cited'])}")
        print(f"- sections: {sections}")
        if quality_missing:
            print(f"- quality_missing: {', '.join(quality_missing)}")
        if trace_failures["missing_loaded"]:
            print(f"- cited_not_loaded: {', '.join(trace_failures['missing_loaded'])}")
        if trace_failures["nonexistent"]:
            print(f"- cited_nonexistent: {', '.join(trace_failures['nonexistent'])}")
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
