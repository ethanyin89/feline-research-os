# Source Schema

Use this frontmatter for every ingested source card.

Important:

- `source_kind` is a file/source-family label, not an authority ranking.
- `evidence_level` is a study/guidance type label, not a substitute for claim-fit judgment.
- Every new source should also be classified using [source hierarchy and claim-fit policy](../indexes/source-hierarchy-and-claim-fit-policy.md).

```yaml
---
id: src-ckd-001
type: source
title: ""
source_kind: paper # paper | regulation | guidance | dataset | image | web
species: feline
diseases: []
models: []
endpoints: []
jurisdictions: []
evidence_level: "" # review | guideline | original-study | case-series | regulation | commentary
year: 2026
status: ingested # inbox | ingested | reviewed | superseded
verification_status: source_checked # title_only | abstract_weighted | source_checked | deep_extracted | audited
decision_grade: no # no | provisional | yes
language_qa_status: not_applicable # unchecked | light_checked | bilingual_checked | not_applicable
tags: []
links:
  doi: ""
  url: ""
  local_assets: []
evidence_policy:
  quoted_fact: []
  source_supported_conclusion: []
  llm_inference: []
  # V2 enhanced fields for Research Mode presentation
  study_design: ""  # 研究设计摘要（如：回顾性横断面，91猫按ACVIM分期）
  core_argument: ""  # 论文的核心论点（一句话完整主张）
  implicit_premise: ""  # 论点成立需要的隐含前提假设
  unexpected_finding: ""  # 意外发现或反直觉结果（可选）
  evidence_boundary: ""  # 证据边界：这篇论文回答不了什么问题
  tension_with: []  # 与其他文献的张力（可选）
    # - source_id: "src-xxx-nnn"
    #   type: "contradicts|extends|qualifies"
    #   description: "张力描述"
---
```

`links.local_assets` should point to files under `raw/images/` when the source has
high-value figures, panels, or image-only tables that matter for later retrieval.

During ingest, do not stop at `source_kind` + `evidence_level`.

The source card body should make clear:

1. what source family this really belongs to
2. what this source most safely controls
3. what this source must not control

If images are not downloaded yet, keep `local_assets: []` and add an `Image Asset TODO`
section in the source card body.

## Required Sections

1. One-line summary
2. Why it matters for CKD
3. Key findings
4. Limits / caveats
5. Open follow-up questions
6. Linked entities

## V2 Enhanced Evidence Policy Fields

These fields power Research Mode's enhanced literature presentation.
Use them for deep-extracted sources to make recommendations more compelling.

### study_design (optional)

Brief description of the research method and cohort.

- Format: "研究类型，样本描述，主要方法"
- Example: "回顾性横断面研究，91 只猫按 ACVIM 分期，采用常规及斑点追踪超声心动图"
- Skip if the paper does not disclose sufficient methodological detail

### core_argument (required for V2)

The paper's central thesis as a complete, specific claim.

- Wrong: "This paper is about HCM biomarkers"
- Right: "NT-proBNP combined with cardiac troponin I provides better prognostic stratification than either marker alone"

### implicit_premise (required for V2)

The unstated assumption the core argument depends on.

- Example: "Assumes echocardiographic cutoffs from human studies apply to feline populations"

### unexpected_finding (optional)

Counter-intuitive or surprising results worth highlighting.

- Example: "Despite strong correlation with disease severity, the biomarker failed to predict thromboembolic events"

### evidence_boundary (required for V2)

What questions this paper explicitly cannot answer.

- Example: "Cross-sectional design cannot determine if LACI-ED changes precede clinical deterioration"

### tension_with (optional)

Conflicts with other vault sources. Use when you can identify specific source IDs.

```yaml
tension_with:
  - source_id: "src-hcm-015"
    type: "contradicts"  # or "extends" or "qualifies"
    description: "Reports different NT-proBNP cutoffs for risk stratification"
```

For extraction workflow, see [deep-extraction-prompt-v2.md](../prompts/deep-extraction-prompt-v2.md).
