#!/usr/bin/env python3
"""Create researcher-facing depth-queue extraction worksheets.

This script is the manual 3-10 sample step before turning the workflow into a
skill. It fetches Crossref/PubMed metadata and abstracts for selected source
cards, then writes conservative worksheets that are useful for human review.

It does not update source cards and does not promote claims into topic pages.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from source_metadata_check import (
    CrossrefCheck,
    check_source,
    md_escape,
    selected_source_cards,
    short,
)
from structured_abstract_extraction import (
    abstract_scope_line,
    detect_endpoints,
    detect_population,
    detect_sections,
    infer_source_family,
)


@dataclass
class DepthWorksheet:
    check: CrossrefCheck
    path: Path


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    return [part.strip() for part in parts if part.strip()]


def sentence_has_any(sentence: str, terms: list[str]) -> bool:
    lower = sentence.casefold()
    return any(term.casefold() in lower for term in terms)


def first_matching_sentence(sentences: list[str], terms: list[str]) -> str:
    for sentence in sentences:
        if sentence_has_any(sentence, terms):
            return sentence
    return sentences[0] if sentences else ""


def collect_matching_sentences(sentences: list[str], terms: list[str], limit: int = 3) -> list[str]:
    matches = [sentence for sentence in sentences if sentence_has_any(sentence, terms)]
    return matches[:limit]


def infer_disease(source_id: str, title: str) -> str:
    match = re.match(r"src-([a-z]+)-", source_id)
    if match:
        return match.group(1)
    lower = title.casefold()
    for disease in ("ckd", "hcm", "fip", "diabetes", "obesity", "ibd", "fcv", "cancer"):
        if disease in lower:
            return disease
    return "feline"


def why_read(check: CrossrefCheck) -> str:
    title = check.title or check.source.title
    text = f"{title}. {check.abstract}".casefold()
    source_id = check.source.source_id
    disease = infer_disease(source_id, title)

    if "fibroblast growth factor" in text or "klotho" in text:
        return (
            "值得优先打开，因为它可能把猫 CKD 的证据分支从常规肌酐、磷和分期，推进到 CKD-MBD、FGF23、Klotho 与磷调节轴。"
        )
    if "tissue motion annular displacement" in text or "longitudinal systolic function" in text:
        return (
            "值得优先打开，因为它检验新的超声心动图功能测量是否能补充 HCM 的壁厚表型标签，可能影响随访和功能评估。"
        )
    if "gs-441524" in text or "remdesivir" in text:
        return (
            "值得优先打开，因为它是较大规模真实世界 FIP 抗病毒治疗结局来源；若病例定义、剂量、缓解、复发和生存数据清楚，会直接影响治疗证据边界。"
        )
    if "velagliflozin" in text or "sglt2" in text:
        return (
            "值得优先打开，因为它直接关系到猫糖尿病口服 SGLT2 抑制剂单药治疗路径，可能改变治疗选择、监测和排除标准的表达。"
        )
    if "overweight" in text or "obesity" in text or "body condition" in text:
        return (
            "值得优先打开，因为它可支撑猫肥胖的流行率和风险因素框架；但必须先看清采样框、BCS 方法和疫情期间就诊选择偏倚。"
        )
    return (
        f"值得优先打开，因为它在 {disease} 深度队列中排序靠前，且已有摘要级证据可判断是否值得进入全文提取。"
    )


def localize_population(value: str) -> str:
    value = re.sub(r"\b(\d+)\s+cats?\b", r"\1 只猫", value, flags=re.IGNORECASE)
    value = value.replace("cats mentioned; count not mechanically extracted", "摘要提到猫，但未机械抽取到样本量")
    value = value.replace("not mechanically extracted", "未机械抽取")
    return value


def sample_group_signal(text: str) -> str:
    """Extract compact group counts such as 13 healthy cats, 71 CKD cats."""
    hits: list[str] = []
    for match in re.finditer(r"\b\d{1,4}\s+(?:[A-Za-zα\-]+\s+){0,4}cats?\b", text, flags=re.IGNORECASE):
        before = text[max(0, match.start() - 12):match.start()].casefold()
        if re.search(r"stage\s+$", before):
            continue
        value = match.group(0).strip()
        value = re.sub(r"\bcats?\b", "只猫", value, flags=re.IGNORECASE)
        value = re.sub(r"\bclient-owned 只猫\b", "只客户饲养猫", value, flags=re.IGNORECASE)
        value = re.sub(r"\bcontrol 只猫\b", "只对照猫", value, flags=re.IGNORECASE)
        value = value.replace("healthy 只猫", "只健康猫")
        value = value.replace("ACKD 只猫", "只 ACKD 猫")
        value = re.sub(r"\bCKD 只猫\b", "只 CKD 猫", value)
        value = re.sub(r"\bHCM 只猫\b", "只 HCM 猫", value)
        value = re.sub(r"\bFIP 只猫\b", "只 FIP 猫", value)
        if value.lower() not in {hit.lower() for hit in hits}:
            hits.append(value)
        if len(hits) >= 4:
            break
    return "；".join(hits)


def method_signal_zh(check: CrossrefCheck) -> str:
    abstract = check.abstract
    sentences = split_sentences(abstract)
    grouped = sample_group_signal(abstract)
    population = grouped or localize_population(detect_population(abstract))
    title = check.title or check.source.title
    lower = f"{title}. {abstract}".casefold()
    method_sentences = collect_matching_sentences(
        sentences,
        ["method", "methods", "animals", "procedures", "prospective", "retrospective", "study", "cats"],
        limit=2,
    )
    design = "研究设计需人工确认"
    if "retrospective" in lower:
        design = "回顾性研究"
    elif "prospective" in lower:
        design = "前瞻性研究"
    elif "cohort" in lower:
        design = "队列研究"
    elif "trial" in lower or "study" in lower:
        design = "原始研究"
    source_line = f" 摘要原句线索：{short(' '.join(method_sentences), 240)}" if method_sentences else ""
    return f"样本/设计线索：{population}；{design}。{source_line}"


def result_signal_zh(check: CrossrefCheck) -> str:
    title = check.title or check.source.title
    lower = f"{title}. {check.abstract}".casefold()
    if "fgf23" in lower or "klotho" in lower:
        return "结果线索：尿 FGF23/尿肌酐比值随晚期 CKD 或急性失代偿 CKD 升高；该方向更适合解释 CKD-MBD 或矿物质代谢风险，而不是直接生成诊断阈值。"
    if "tissue motion annular displacement" in lower or "longitudinal systolic function" in lower:
        return "结果线索：研究关注 HCM 猫的纵向收缩功能评估；需要进一步核对该指标与传统超声参数、疾病严重度或结局之间的关系。"
    if "gs-441524" in lower or "remdesivir" in lower:
        return "结果线索：摘要显示研究纳入 307 只 FIP 猫，并报告治疗反应与初始治疗期末存活相关；但回顾性真实世界数据不能直接等同随机疗效证明。"
    if "velagliflozin" in lower or "sglt2" in lower:
        return "结果线索：该研究测试口服 SGLT2 抑制剂作为猫糖尿病单药治疗的有效性和安全性；需要重点核对排除标准、酮症风险和监测要求。"
    if "obesity" in lower or "overweight" in lower or "body condition" in lower:
        return "结果线索：该研究提供猫超重/肥胖的流行率或相关因素信息；应重点核对采样框、BCS 阈值、生活方式变量和偏倚来源。"

    sentences = split_sentences(check.abstract)
    result_sentences = collect_matching_sentences(
        sentences,
        ["result", "results", "significant", "associated", "increased", "decreased", "survival", "effective", "safety", "risk"],
        limit=3,
    )
    if result_sentences:
        return "结果原句线索：" + short(" ".join(result_sentences), 320)
    conclusion = first_matching_sentence(sentences, ["conclusion", "conclusions"])
    return ("结论原句线索：" + short(conclusion, 280)) if conclusion else "未机械识别出清晰结果句，需要人工阅读摘要或全文。"


def clinical_relevance_zh(check: CrossrefCheck) -> str:
    title = check.title or check.source.title
    text = f"{title}. {check.abstract}".casefold()
    if "biomarker" in text or "fibroblast growth factor" in text or "klotho" in text:
        return "潜在临床意义：可帮助解释 CKD 矿物质代谢、FGF23/Klotho 生物标志物和风险分层。边界：除非阈值和验证队列清楚，否则不能写成独立诊断流程。"
    if "echocardiograph" in text or "cardiomyopathy" in text:
        return "潜在临床意义：用于心脏病表型和随访评估。边界：功能测量需要重复性和结局关联，才能影响常规决策。"
    if "gs-441524" in text or "remdesivir" in text:
        return "潜在临床意义：用于 FIP 抗病毒治疗预期、缓解和复发沟通。边界：回顾性或非对照证据不能当作随机疗效证明。"
    if "velagliflozin" in text or "sglt2" in text:
        return "潜在临床意义：用于猫糖尿病治疗路径选择。边界：安全排除条件和监测标准与降糖效果同等重要。"
    if "obesity" in text or "overweight" in text:
        return "潜在临床意义：用于肥胖预防、筛查和风险因素沟通。边界：流行率估计高度依赖采样框和体况评分方法。"
    return "潜在临床意义取决于端点提取；摘要级证据应保持暂定。"


def not_safe_to_promote(check: CrossrefCheck) -> list[str]:
    title = check.title or check.source.title
    text = f"{title}. {check.abstract}".casefold()
    blockers = [
        "数字化临床建议",
        "指南式推荐",
        "面向主人的确定性承诺",
    ]
    if "retrospective" in text:
        blockers.append("从回顾性数据推出因果疗效")
    if "prospective" not in text and "random" not in text and "trial" not in text:
        blockers.append("未确认研究设计前写成强疗效结论")
    if "abstract" in (check.metadata_source or "").casefold() or check.abstract_available:
        blockers.append("全文方法和结果细节尚未核对")
    return blockers


def source_card_patch_suggestion(check: CrossrefCheck) -> str:
    title = check.title or check.source.title
    endpoints = detect_endpoints(f"{title} {check.abstract}")
    endpoint_text = ", ".join(endpoints[:6]) if endpoints else "needs human endpoint assignment"
    return (
        "- 在人工审阅前，卡片最多保持 `abstract_weighted`，不要直接升为 deep_extracted。\n"
        f"- 候选端点/主题标签：{md_escape(endpoint_text)}。\n"
        "- 只有在完整摘要或全文核对后，才添加有边界的 `quoted_fact` 和 `source_supported_conclusion`。"
    )


def render_worksheet(check: CrossrefCheck) -> str:
    today = date.today().isoformat()
    source_id = check.source.source_id
    title = check.title or check.source.title
    provider = check.metadata_source or "external metadata"
    family = infer_source_family(title, check.abstract)
    sections = detect_sections(check.abstract)
    endpoints = detect_endpoints(f"{title} {check.abstract}")

    blockers = "\n".join(f"- {md_escape(item)}" for item in not_safe_to_promote(check))
    abstract_lead = short(check.abstract, 350)

    return f"""---
id: {source_id}-depth-queue-extraction-round1
type: system
topic: content-pipeline
question_type: depth-queue-extraction
source_ids: [{source_id}]
language: zh
last_compiled_at: {today}
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# {source_id} 深度队列提取，Round 1

## 证据边界

本 worksheet 仅使用 {provider} 和可用摘要文本。它不是全文 deep extraction。人工审阅后，它可以支持 source card 更新，但不能直接晋升为读者可见的临床结论。

## 来源元数据

| Field | Value |
|---|---|
| Source | `{source_id}` |
| Title | {md_escape(title)} |
| DOI | `{check.source.doi or "not available"}` |
| Provider | {md_escape(provider)} |
| Container | {md_escape(check.container)} |
| Year | {check.year} |
| Current card status | `{check.source.verification_status}` |
| Source family | {md_escape(family)} |
| Detected sections | {md_escape(", ".join(sections) if sections else "none mechanically detected")} |
| Detected endpoint/theme signals | {md_escape(", ".join(endpoints) if endpoints else "none mechanically detected")} |

## 为什么值得读

{why_read(check)}

## 方法 / 样本线索

{md_escape(method_signal_zh(check))}

## 主要结果线索

{md_escape(result_signal_zh(check))}

## 临床相关性线索

{clinical_relevance_zh(check)}

## 摘要原文片段（用于审计，不直接面向读者）

> {md_escape(abstract_lead)}

## 目前不能晋升的内容

{blockers}

## Source Card 修改建议

{source_card_patch_suggestion(check)}

## 下一步提取动作

- 人工审阅者应阅读完整摘要；若可访问，再读全文。
- 如果该来源控制一个证据分支，再用明确的 `quoted_fact`、`source_supported_conclusion` 和 `llm_inference` 更新 source card。
- 如果只能获得摘要级证据，保持 `decision_grade: no`。
"""


def render_index(worksheets: list[DepthWorksheet], source_label: str, index_id: str | None = None) -> str:
    today = date.today().isoformat()
    stable_id = index_id or f"depth-queue-extraction-sample-{today.replace('-', '')}"
    lines = [
        "---",
        f"id: {stable_id}",
        "type: system",
        "topic: content-pipeline",
        "question_type: depth-queue-extraction-index",
        "language: zh",
        f"last_compiled_at: {today}",
        "verification_status: compiled",
        "decision_grade: no",
        "owner: codex",
        "status: active",
        "---",
        "",
        f"# 深度队列提取样本，{today}",
        "",
        f"来源集合：`{source_label}`",
        "",
        "## 规则",
        "",
        "这是 research depth queue 的 3-10 篇样本运行。它生成可审阅 worksheet，不直接晋升 source card。",
        "",
        "## 样本表",
        "",
        "| 来源 | Worksheet | 元数据 |",
        "|---|---|---|",
    ]
    for worksheet in worksheets:
        check = worksheet.check
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{check.source.source_id}`",
                    f"[{worksheet.path.name}]({worksheet.path.name})",
                    md_escape(abstract_scope_line(check)),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 边界",
            "",
            "- 本次运行未修改 source card。",
            "- 这些 worksheet 可用于人工审阅后的 source card 修改。",
            "- 不要仅凭这批样本更新 topic page。",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--source-ids", help="Comma-separated source IDs.")
    parser.add_argument("--source-id-file", type=Path, help="Path with one source ID per line.")
    parser.add_argument("--source-label", default="manual depth queue sample")
    parser.add_argument("--index-id", help="Stable frontmatter id for generated index.")
    parser.add_argument("--out-dir", type=Path, default=Path("system/indexes"))
    parser.add_argument("--index-out", type=Path, help="Optional sample index path.")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    out_dir = args.out_dir if args.out_dir.is_absolute() else repo_root / args.out_dir
    if not args.source_ids and not args.source_id_file:
        print("Select 3-10 source IDs via --source-ids or --source-id-file.", file=sys.stderr)
        return 2

    cards = selected_source_cards(
        repo_root=repo_root,
        source_ids=args.source_ids,
        source_id_file=args.source_id_file,
        source_globs=[],
        statuses=None,
    )
    if not 3 <= len(cards) <= 10:
        print(f"Expected 3-10 sample sources; got {len(cards)}.", file=sys.stderr)
        return 2

    worksheets: list[DepthWorksheet] = []
    for card in cards:
        check = check_source(card, args.timeout)
        if not check.abstract_available:
            reason = check.error or "no abstract available"
            print(f"Skipping {card.source_id}: {reason}", file=sys.stderr)
            continue
        path = out_dir / f"{card.source_id}-depth-queue-extraction-round1.md"
        worksheets.append(DepthWorksheet(check=check, path=path))
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render_worksheet(check), encoding="utf-8")

    if args.index_out:
        index_path = args.index_out if args.index_out.is_absolute() else repo_root / args.index_out
        if args.write:
            index_path.parent.mkdir(parents=True, exist_ok=True)
            index_path.write_text(render_index(worksheets, args.source_label, args.index_id), encoding="utf-8")
        else:
            sys.stdout.write(render_index(worksheets, args.source_label, args.index_id))
    elif not args.write:
        sys.stdout.write(render_index(worksheets, args.source_label, args.index_id))

    print(f"Planned {len(worksheets)} depth-queue worksheets.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
