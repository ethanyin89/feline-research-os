# /v2-extract — Add V2 Enhanced Fields to Source Cards

Add V2 evidence_policy fields to deep-extracted source cards for enhanced Research Mode presentation.

## When to Use

- User says "v2 extract [paper-id]" or "add v2 fields to [paper-id]"
- User provides a list of papers needing V2 enhancement
- After deep extraction, to add the enhanced presentation fields

## Prerequisites

- Paper must already be `status: deep_extracted`
- Paper must have existing `evidence_policy` section with `quoted_fact`, `source_supported_conclusion`, `llm_inference`

## V2 Fields to Add

Add these fields under `evidence_policy:` after `llm_inference:`:

```yaml
  # V2 enhanced fields
  study_design: "研究类型，样本描述，主要方法"  # Optional, skip if not disclosed
  core_argument: "论文的核心论点（一句话完整主张，不是话题描述）"  # Required
  implicit_premise: "论点成立需要的隐含前提假设"  # Required
  unexpected_finding: "意外发现或反直觉结果"  # Optional, include when present
  evidence_boundary: "证据边界：这篇论文回答不了什么问题"  # Required
  tension_with:  # Optional, include when identifiable
    - source_id: "src-xxx-nnn"
      type: "contradicts|extends|qualifies"
      description: "张力描述"
```

## Field Guidelines

### study_design (optional)
- Format: "研究类型，样本描述，主要方法"
- Examples:
  - "回顾性横断面研究，91 只猫按 ACVIM 分期，采用常规及斑点追踪超声心动图"
  - "系统综述，11 项临床研究（2018-2024），共 650 只 FIP 猫"
  - "病例对照研究，382 例确诊 FIP 猫 vs 普通猫群"
- Skip if paper does not disclose sufficient methodological detail

### core_argument (required)
- Must be a complete, specific claim — NOT a topic description
- Wrong: "This paper is about feline HCM"
- Wrong: "This study investigates biomarkers"
- Right: "LACI-ED 反映猫 HCM 疾病严重程度，但对血栓栓塞事件的预测判别力有限"
- Right: "GS-441524 将 FIP 从「致死性疾病」转变为「可治疗疾病」——总体成功率 84.6%"

### implicit_premise (required)
- What must be true for the core argument to hold?
- Usually an unstated methodological or theoretical assumption
- Example: "假设横断面研究中的关联可以反映其作为临床预测指标的价值"

### unexpected_finding (optional)
- Counter-intuitive results, negative findings, or results that contradict common assumptions
- Example: "尽管 LACI-ED >150% 与 FATE 显著相关，但其 ROC AUC 仅为 0.575——几乎等同于随机猜测"
- Skip if nothing surprising

### evidence_boundary (required)
- What questions does this paper explicitly NOT answer?
- Example: "横断面设计无法建立因果方向；不能回答成本效益问题"

### tension_with (optional)
- Only include when you can identify specific vault sources
- Types: contradicts, extends, qualifies

## Workflow

1. Read the paper file
2. Understand existing evidence_policy content
3. Synthesize V2 fields based on:
   - `quoted_fact` for study_design details
   - `source_supported_conclusion` for core_argument
   - Overall content for implicit_premise, unexpected_finding, evidence_boundary
4. Edit the file to add V2 fields after `llm_inference:`
5. Verify with: `python3 -c "from scripts.research_mode import parse_source_card; from pathlib import Path; c = parse_source_card(Path('[file]')); print(f'core_argument: {bool(c.core_argument)}, evidence_boundary: {bool(c.evidence_boundary)}')"`

## Quality Gates

Before completing, verify:
- [ ] `core_argument` is > 50 characters and is a complete claim
- [ ] `evidence_boundary` is non-empty and specific
- [ ] If surprising finding exists, `unexpected_finding` captures it
- [ ] Fields are in Chinese for consistency with vault style

## Example

Input paper: src-fip-028.md (GS-441524 vs molnupiravir comparison)

Added V2 fields:
```yaml
  # V2 enhanced fields
  study_design: "前瞻性比较队列研究，118 只 FIP 猫（GS-441524 59 只 vs molnupiravir 59 只），84 天疗程"
  core_argument: "GS-441524 与 molnupiravir 在猫 FIP 治疗中疗效相当——死亡率无显著差异（20.3% vs 13.6%, p=0.326），完成治疗者缓解率均接近 100%"
  implicit_premise: "假设非随机队列设计中的两组匹配足以支持因果推断；假设 84 天随访足以评估缓解"
  unexpected_finding: "大多数死亡发生在治疗前 10 天——这提示早期死亡可能反映入组时疾病严重程度，而非药物选择的差异"
  evidence_boundary: "非 RCT 设计无法排除选择偏倚；未报告长期复发率；不能回答成本效益或药物耐药性问题"
```
