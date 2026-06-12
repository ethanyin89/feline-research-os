"""
Test the harness loop: TaskEvaluator → GapChecker → Verifier.

This validates the core infrastructure for the ChatAcademia Research Workbench.
"""

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import (
    TaskEvaluator,
    SearchDepthController,
    GapChecker,
    Verifier,
    ResearchRecord,
    TaskType,
    SearchDepth,
    VerifierStatus,
)
from scripts.harness_loop import HarnessLoop


def test_task_evaluation():
    """Test query evaluation and task classification."""
    evaluator = TaskEvaluator()

    # Test protocol design query
    query1 = "请帮我设计一个猫FIP的临床研究方案"
    eval1 = evaluator.evaluate(query1)
    assert eval1.task_type == TaskType.PROTOCOL_DESIGN, f"Expected PROTOCOL_DESIGN, got {eval1.task_type}"
    assert eval1.disease == "fip", f"Expected fip, got {eval1.disease}"
    assert eval1.search_depth == SearchDepth.DEEP
    print(f"✓ Protocol query: task_type={eval1.task_type.value}, disease={eval1.disease}")

    # Test endpoint selection query
    query2 = "猫CKD的终点指标有哪些"
    eval2 = evaluator.evaluate(query2)
    assert eval2.task_type == TaskType.ENDPOINT_SELECTION
    assert eval2.disease == "ckd"
    print(f"✓ Endpoint query: task_type={eval2.task_type.value}, disease={eval2.disease}")

    # Test quick explanation query
    query3 = "什么是FIP"
    eval3 = evaluator.evaluate(query3)
    assert eval3.task_type == TaskType.QUICK_EXPLANATION
    assert eval3.search_depth == SearchDepth.QUICK
    print(f"✓ Quick query: task_type={eval3.task_type.value}, depth={eval3.search_depth.value}")

    # Test record creation
    record = evaluator.create_record(query1)
    assert record.task_type == TaskType.PROTOCOL_DESIGN
    assert record.disease == "fip"
    assert len(record.key_decisions) > 0
    print(f"✓ Record created: {record.record_id}")

    return record


def test_gap_checker(record: ResearchRecord):
    """Test gap checking for protocol design."""
    checker = GapChecker()

    # Draft missing key sections
    incomplete_draft = """
    研究目的：评估新药物对猫FIP的疗效。

    研究动物：自然发病的FIP猫。
    """

    result = checker.check(record, incomplete_draft)
    assert result.has_high_gaps or len(result.gaps) > 0, "Should detect missing sections"
    assert result.recommendation in ["revise", "continue"]
    print(f"✓ Gap check (incomplete): {len(result.gaps)} gaps found, recommendation={result.recommendation}")

    # Draft with more sections
    better_draft = """
    研究目的：评估新药物对猫FIP的疗效和安全性。

    研究动物：自然发病的FIP猫，符合入组标准。

    入组标准：
    - 年龄 > 6月龄
    - 确诊FIP

    分组设计：随机分为治疗组和对照组。

    干预措施：治疗组给予新药物，对照组给予安慰剂。

    疗效终点：
    - 主要终点：30天生存率
    - 次要终点：临床症状改善

    时间点：Day 0, 7, 14, 21, 30

    统计分析：样本量计算基于...

    伦理：研究获得IACUC批准，遵循动物福利指南。

    参考文献：
    - src-fip-001: 最新FIP诊断标准
    - PMID: 12345678

    研究局限：样本量可能有限，需要更多研究验证。
    """

    result2 = checker.check(record, better_draft)
    print(f"✓ Gap check (better): {len(result2.gaps)} gaps found, recommendation={result2.recommendation}")

    return better_draft


def test_verifier(record: ResearchRecord, draft: str):
    """Test independent verification."""
    verifier = Verifier()

    # Quick verify
    quick_pass = verifier.quick_verify(draft, record)
    print(f"✓ Quick verify: {'passed' if quick_pass else 'failed'}")

    # Full verification
    record = verifier.verify(record, draft)
    print(f"✓ Full verification: status={record.verifier_status.value}")
    print(f"  - Total checks: {len(record.verification_results)}")

    passed = sum(1 for r in record.verification_results if r.passed)
    failed = sum(1 for r in record.verification_results if not r.passed)
    print(f"  - Passed: {passed}, Failed: {failed}")

    # Show any failures
    for result in record.verification_results:
        if not result.passed:
            print(f"  - FAIL [{result.severity}]: {result.check_name} - {result.message}")

    # Generate report
    report = verifier.format_verification_report(record)
    print(f"✓ Verification report generated ({len(report)} chars)")

    return record


def test_species_boundary_detection():
    """Test cross-species reference detection."""
    verifier = Verifier()
    evaluator = TaskEvaluator()

    record = evaluator.create_record("猫CKD终点指标")

    # Draft with unmarked cross-species reference
    draft_with_unmarked = """
    CKD biomarkers include:
    - SDMA (validated in dogs)
    - Creatinine
    - BUN

    Human studies show GFR is the gold standard.
    """

    record_checked = verifier.verify(record, draft_with_unmarked)
    species_failures = [
        r for r in record_checked.verification_results
        if "species_boundary" in r.check_name and not r.passed
    ]
    assert len(species_failures) > 0, "Should detect unmarked cross-species references"
    print(f"✓ Detected {len(species_failures)} unmarked cross-species references")

    # Draft with properly flagged cross-species reference
    draft_with_flagged = """
    CKD biomarkers include:
    - SDMA (validated in dogs, 需注意跨物种外推)
    - Creatinine
    - BUN

    Human studies show GFR is the gold standard, but extrapolation to cats has limitations.
    """

    record2 = evaluator.create_record("猫CKD终点指标")
    record2_checked = verifier.verify(record2, draft_with_flagged)
    species_passes = [
        r for r in record2_checked.verification_results
        if "species_boundary" in r.check_name and r.passed
    ]
    print(f"✓ Properly flagged references detected: {len(species_passes)}")


def test_search_depth_controller():
    """Test that assigned depth is backed by observable retrieval work."""
    evaluator = TaskEvaluator()
    controller = SearchDepthController()

    deep_record = evaluator.create_record("猫CKD的终点指标有哪些")
    deep_record.selected_evidence = ["src-ckd-001"]
    deep_record.gap_checks_performed = 1

    insufficient = controller.assess(
        deep_record,
        research_trace=[
            {
                "step": "Searched vault",
                "detail": "scope=raw; results=1",
                "items": [{"id": "src-ckd-001", "file": "raw/papers/src-ckd-001.md"}],
            }
        ],
    )
    assert not insufficient.passed
    assert any("evidence" in failure for failure in insufficient.failures)
    assert any("retrieval rounds" in failure for failure in insufficient.failures)

    deep_record.selected_evidence = [
        "src-ckd-001",
        "src-ckd-002",
        "src-ckd-003",
    ]
    sufficient = controller.assess(
        deep_record,
        research_trace=[
            {
                "step": "Loaded routed files",
                "detail": "1/1 files loaded",
                "items": [{"file": "topics/ckd/model-map.md", "loaded": True}],
            },
            {
                "step": "Searched vault",
                "detail": "scope=raw; results=3",
                "items": [
                    {"id": "src-ckd-001", "file": "raw/papers/src-ckd-001.md"},
                    {"id": "src-ckd-002", "file": "raw/papers/src-ckd-002.md"},
                    {"id": "src-ckd-003", "file": "raw/papers/src-ckd-003.md"},
                ],
            },
        ],
    )
    assert sufficient.passed, sufficient.failures

    audit_record = evaluator.create_record("审查猫CKD终点指标的证据")
    audit_record.selected_evidence = deep_record.selected_evidence
    audit_record.gap_checks_performed = 1
    audit_without_counterevidence = controller.assess(
        audit_record,
        research_trace=[
            {
                "step": "Loaded routed files",
                "detail": "1/1 files loaded",
                "items": [{"file": "system/indexes/ckd-source-index.md"}],
            },
            {
                "step": "Searched vault",
                "detail": "scope=raw; results=3",
                "items": [{"id": "src-ckd-001", "file": "raw/papers/src-ckd-001.md"}],
            },
        ],
    )
    assert audit_record.search_depth == SearchDepth.EVIDENCE_AUDIT
    assert not audit_without_counterevidence.passed
    assert "counterevidence check missing" in audit_without_counterevidence.failures
    print("✓ Search depth contracts enforce retrieval work and counterevidence")


def test_audit_depth_failure_status():
    """Audit tasks fail rather than pass through when depth work is missing."""
    with TemporaryDirectory() as tmp:
        harness = HarnessLoop(Path(tmp))
        record = harness.evaluate_query("审查猫CKD终点指标的证据")
        result = harness.process_query_result(
            record=record,
            answer="现有证据包括 src-ckd-001。",
            source_ids=["src-ckd-001"],
            loaded_source_ids=["src-ckd-001"],
            disease="ckd",
            question_type="claim_verification",
            research_trace=[
                {
                    "step": "Searched vault",
                    "detail": "scope=raw; results=1",
                    "items": [
                        {
                            "id": "src-ckd-001",
                            "file": "raw/papers/src-ckd-001.md",
                        }
                    ],
                }
            ],
        )
        assert result["search_depth_satisfied"] is False
        assert result["verification_status"] == VerifierStatus.FAILED.value
        records_root = Path(tmp) / "system" / "research-records"
        assert not list((records_root / "json").glob("*.json"))
        assert not list((records_root / "markdown").glob("*.md"))
    print("✓ Evidence Audit depth failures produce failed status")


def test_explicit_record_save():
    """Finalization returns a draft record and persistence is explicit."""
    with TemporaryDirectory() as tmp:
        harness = HarnessLoop(Path(tmp))
        record = harness.evaluate_query("什么是FIP")
        result = harness.process_query_result(
            record=record,
            answer="FIP is feline infectious peritonitis. It is a serious disease.",
            source_ids=["src-fip-001"],
            loaded_source_ids=["src-fip-001"],
            disease="fip",
            question_type="quick_explanation",
            research_trace=[
                {
                    "step": "Searched vault",
                    "detail": "scope=raw; results=1",
                    "items": [
                        {
                            "id": "src-fip-001",
                            "file": "raw/papers/src-fip-001.md",
                        }
                    ],
                }
            ],
        )

        assert "record" in result
        assert result["saved"] is False
        draft = result["record"]
        assert draft.final_answer.startswith("FIP is feline infectious peritonitis")
        records_root = Path(tmp) / "system" / "research-records"
        assert not list((records_root / "json").glob("*.json"))
        assert not list((records_root / "markdown").glob("*.md"))

        out_path = harness.save_record(draft)
        assert out_path.exists()
        assert list((records_root / "json").glob("*.json"))
        assert list((records_root / "markdown").glob("*.md"))
        loaded = harness.record_store.load(draft.record_id)
        assert loaded is not None
        assert loaded.final_answer == draft.final_answer
    print("✓ Explicit record save writes only on demand")


def run_all_tests():
    """Run all harness loop tests."""
    print("=" * 60)
    print("Testing Harness Loop Infrastructure")
    print("=" * 60)
    print()

    print("1. Testing Task Evaluation...")
    record = test_task_evaluation()
    print()

    print("2. Testing Gap Checker...")
    draft = test_gap_checker(record)
    print()

    print("3. Testing Verifier...")
    record = test_verifier(record, draft)
    print()

    print("4. Testing Species Boundary Detection...")
    test_species_boundary_detection()
    print()

    print("5. Testing Search Depth Controller...")
    test_search_depth_controller()
    print()

    print("6. Testing Audit Failure Status...")
    test_audit_depth_failure_status()
    print()

    print("7. Testing Explicit Record Save...")
    test_explicit_record_save()
    print()

    print("=" * 60)
    print("All tests passed!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
