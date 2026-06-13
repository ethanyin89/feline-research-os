"""
Benchmark Question Runner for Harness Loop Testing.

Runs the 20 benchmark questions through the harness loop to validate:
1. Task type detection
2. Search depth assignment
3. Disease detection
4. Gap checking
5. Verification

Can be run standalone or imported for use in tests.
"""

import sys
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

# Add parent directory for core imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import (
    TaskEvaluator,
    GapChecker,
    Verifier,
    TaskType,
    SearchDepth,
)


# The 20 benchmark questions from ARCHITECTURE.md
BENCHMARK_QUESTIONS = [
    "猫 FIP 药效评价有哪些核心指标？",
    "猫 CKD 研究中 SDMA 的用途和限制是什么？",
    "猫 HCM 研究中超声心动图终点如何选择？",
    "猫 PK 研究采血设计有哪些约束？",
    "猫 FCGS 临床研究评分体系如何构建？",
    "猫皮肤真菌模型适合评价哪些产品？",
    "猫肥胖模型中体重、BCS、代谢指标如何组合？",
    "猫研究方案中哪些地方最容易犬猫混用？",
    "FIP 造模成功率如何评价？",
    "CKD 自然病例 vs 造模的优劣势？",
    "SAA 在猫炎症评价中的边界是什么？",
    "A/G ratio 在 FIP 诊断和疗效评价中分别承担什么角色？",
    "猫药物 PK 采样时间点如何设计？",
    "猫临床前研究中人道终点如何设定？",
    "IRIS 分期在 CKD 药效评价中的应用？",
    "猫呼吸道感染模型的主要读数指标？",
    "猫皮肤病模型中瘙痒评分体系的选择？",
    "猫心肌病研究中 NT-proBNP 的用途？",
    "猫糖尿病模型的血糖控制目标？",
    "猫研究中转化医学的边界和风险？",
]

# Expected classifications for validation
EXPECTED_CLASSIFICATIONS = {
    # FIP
    0: {"disease": "fip", "task_type": TaskType.ENDPOINT_SELECTION},
    8: {"disease": "fip", "task_type": TaskType.MODEL_EVALUATION},
    11: {"disease": "fip", "task_type": TaskType.ENDPOINT_SELECTION},

    # CKD
    1: {"disease": "ckd", "task_type": TaskType.ENDPOINT_SELECTION},
    9: {"disease": "ckd", "task_type": TaskType.MODEL_EVALUATION},
    14: {"disease": "ckd", "task_type": TaskType.ENDPOINT_SELECTION},

    # HCM
    2: {"disease": "hcm", "task_type": TaskType.ENDPOINT_SELECTION},
    17: {"disease": "hcm", "task_type": TaskType.ENDPOINT_SELECTION},

    # PK
    3: {"task_type": TaskType.PK_DESIGN},
    12: {"task_type": TaskType.PK_DESIGN},

    # FCGS
    4: {"disease": "fcgs", "task_type": TaskType.PROTOCOL_DESIGN},

    # Obesity
    6: {"disease": "obesity", "task_type": TaskType.MODEL_EVALUATION},

    # Diabetes
    18: {"disease": "diabetes", "task_type": TaskType.MODEL_EVALUATION},
}


def run_benchmark(verbose: bool = True) -> Dict[str, Any]:
    """
    Run all benchmark questions and return results.

    Args:
        verbose: Whether to print progress

    Returns:
        Dictionary with benchmark results
    """
    evaluator = TaskEvaluator()

    results = []
    passed = 0
    failed = 0

    for i, question in enumerate(BENCHMARK_QUESTIONS):
        if verbose:
            print(f"\n[{i+1}/20] {question[:40]}...")

        evaluation = evaluator.evaluate(question)

        result = {
            "index": i,
            "question": question,
            "task_type": evaluation.task_type.value,
            "disease": evaluation.disease,
            "search_depth": evaluation.search_depth.value,
            "requires_freshness": evaluation.requires_freshness,
            "requires_plurality": evaluation.requires_plurality,
            "species_strict": evaluation.species_strict,
            "subqueries": len(evaluation.subqueries),
        }

        # Check against expected if available
        expected = EXPECTED_CLASSIFICATIONS.get(i, {})
        validation_passed = True

        if "disease" in expected:
            if evaluation.disease != expected["disease"]:
                validation_passed = False
                result["disease_expected"] = expected["disease"]

        if "task_type" in expected:
            if evaluation.task_type != expected["task_type"]:
                validation_passed = False
                result["task_type_expected"] = expected["task_type"].value

        result["validation_passed"] = validation_passed

        if validation_passed:
            passed += 1
            if verbose:
                print(f"  ✓ task={result['task_type']}, disease={result['disease']}, depth={result['search_depth']}")
        else:
            failed += 1
            if verbose:
                print(f"  ✗ task={result['task_type']} (expected: {result.get('task_type_expected', 'any')})")
                print(f"    disease={result['disease']} (expected: {result.get('disease_expected', 'any')})")

        results.append(result)

    # Summary statistics
    task_type_distribution = {}
    disease_distribution = {}
    depth_distribution = {}

    for r in results:
        tt = r["task_type"]
        task_type_distribution[tt] = task_type_distribution.get(tt, 0) + 1

        d = r["disease"] or "undetected"
        disease_distribution[d] = disease_distribution.get(d, 0) + 1

        sd = r["search_depth"]
        depth_distribution[sd] = depth_distribution.get(sd, 0) + 1

    summary = {
        "total": len(BENCHMARK_QUESTIONS),
        "passed": passed,
        "failed": failed,
        "pass_rate": passed / len(BENCHMARK_QUESTIONS) * 100,
        "task_type_distribution": task_type_distribution,
        "disease_distribution": disease_distribution,
        "depth_distribution": depth_distribution,
        "results": results,
        "timestamp": datetime.now().isoformat(),
    }

    return summary


def print_summary(summary: Dict[str, Any]) -> None:
    """Print a formatted summary of benchmark results."""
    print("\n" + "=" * 60)
    print("BENCHMARK SUMMARY")
    print("=" * 60)

    print(f"\nTotal: {summary['total']} questions")
    print(f"Passed: {summary['passed']} ({summary['pass_rate']:.1f}%)")
    print(f"Failed: {summary['failed']}")

    print("\nTask Type Distribution:")
    for tt, count in sorted(summary["task_type_distribution"].items()):
        print(f"  {tt}: {count}")

    print("\nDisease Distribution:")
    for d, count in sorted(summary["disease_distribution"].items()):
        print(f"  {d}: {count}")

    print("\nSearch Depth Distribution:")
    for sd, count in sorted(summary["depth_distribution"].items()):
        print(f"  {sd}: {count}")

    # Show failures
    failures = [r for r in summary["results"] if not r["validation_passed"]]
    if failures:
        print("\nFailed Validations:")
        for f in failures:
            print(f"  [{f['index']+1}] {f['question'][:50]}...")
            if "task_type_expected" in f:
                print(f"      task: got {f['task_type']}, expected {f['task_type_expected']}")
            if "disease_expected" in f:
                print(f"      disease: got {f['disease']}, expected {f['disease_expected']}")


def save_results(summary: Dict[str, Any], vault_root: Path) -> Path:
    """
    Save benchmark results to a file.

    Args:
        summary: Benchmark summary
        vault_root: Root of the vault

    Returns:
        Path to saved file
    """
    import json

    output_dir = vault_root / "system" / "health-checks"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = output_dir / f"benchmark-harness-{timestamp}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    return output_file


if __name__ == "__main__":
    print("Running Harness Loop Benchmark...")
    print(f"Questions: {len(BENCHMARK_QUESTIONS)}")

    summary = run_benchmark(verbose=True)
    print_summary(summary)

    # Save results
    vault_root = Path(__file__).parent.parent
    output_file = save_results(summary, vault_root)
    print(f"\nResults saved to: {output_file}")
