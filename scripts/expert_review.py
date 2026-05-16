#!/usr/bin/env python3
"""
Reusable expert-review prompt helpers for Ask the vault answers.

This module is intentionally pure: no API calls, no file writes, no Streamlit import.
The UI can present the manual review loop without pretending the workflow is
fully codified before the 3-10 sample gate is met.
"""

from __future__ import annotations


EXPERT_REVIEW_SAMPLE_COUNT = 3
EXPERT_REVIEW_SAMPLE_MIN = 3
EXPERT_REVIEW_SAMPLE_MAX = 10


def expert_review_stage_label(
    sample_count: int = EXPERT_REVIEW_SAMPLE_COUNT,
    sample_min: int = EXPERT_REVIEW_SAMPLE_MIN,
    sample_max: int = EXPERT_REVIEW_SAMPLE_MAX,
) -> str:
    """Return the current manual-sample stage label for the review loop."""
    return f"manual sample {sample_count}/{sample_min}-{sample_max}"


def build_expert_review_prompt(
    *,
    question: str,
    answer: str,
    disease: str = "",
    question_type: str = "",
    confidence: str = "",
    source_ids: list[str] | None = None,
    sample_count: int = EXPERT_REVIEW_SAMPLE_COUNT,
    sample_min: int = EXPERT_REVIEW_SAMPLE_MIN,
    sample_max: int = EXPERT_REVIEW_SAMPLE_MAX,
) -> str:
    """Build a copy-ready prompt for manual domain-expert review of one answer."""
    source_ids = source_ids or []
    source_line = ", ".join(source_ids) if source_ids else "not captured"
    disease_line = disease or "auto-detected / not captured"
    qtype_line = question_type or "not captured"
    confidence_line = confidence or "not captured"
    stage = expert_review_stage_label(sample_count, sample_min, sample_max)

    return f"""# Ask the vault Expert Review Pack

Workflow stage: {stage}

This is a manual review sample, not source evidence and not a final automated skill.

## Step 1: Choose the reviewer

我想探讨【领域】里的【问题类型/场景】。先别回答。请你先选一位最适合的领域顶尖名人专家来思考它。可以是活人或历史人物，名字可以小众，但必须在该细分领域很专业。如果你不确定该选谁，可以先反问我2个定位问题再选。先输出：

1. 你选谁，他对应的细分领域
2. 为啥选他，三句话

然后再让我描述详细的问题。

Suggested field:
{disease_line}

Suggested question type / scene:
{qtype_line}

## Step 2: Ask for strict review

请以你刚才选择的专家视角，严格审核下面这个 Ask the vault 回答是否准确、严谨、证据分层是否正确。不要只润色。请指出：

1. 哪些表述应该降级
2. 哪些终点、场景、对象被混在一起
3. 哪些地方需要 source card 或原文核验
4. 哪些内容只适合保留为 inference
5. 如果要写回知识库，最小应该写回到 topic、memo、source queue、query test、health check 里的哪一层

请最后给出：

- 保留
- 修改
- 删除或降级
- 需要补证据
- 不应写回，只保留聊天

## Original Question

{question.strip() or "not captured"}

## Ask the vault Metadata

- disease: {disease_line}
- question_type: {qtype_line}
- confidence: {confidence_line}
- source_ids: {source_line}

## Ask the vault Answer

{answer.strip() or "not captured"}
"""

