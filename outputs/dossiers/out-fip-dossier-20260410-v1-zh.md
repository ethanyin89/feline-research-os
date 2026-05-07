---
id: out-fip-dossier-20260410-v1-zh
type: output
output_kind: dossier
language: zh
topic: fip
question: "围绕疾病框架、识别、endpoint hierarchy、mutation-boundary、treatment transformation 与 regulatory boundary，猫 FIP 的第一版可用中文内部 dossier 是什么？"
source_ids: [src-fip-003, src-fip-004, src-fip-005, src-fip-006, src-fip-009, src-fip-010, src-fip-013, src-fip-014, src-fip-015, src-fip-016, src-fip-017, src-fip-019, src-fip-020, src-fip-022, src-fip-023, src-fip-024]
generated_at: 2026-04-10
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: draft
evidence_policy:
  quoted_fact: []
  source_supported_conclusion: []
  llm_inference: []
---

# 猫 FIP Internal Dossier V1（中文）

源自：

- [out-fip-dossier-20260410-v1-working-en.md](out-fip-dossier-20260410-v1-working-en.md)

## 用户问题

围绕疾病框架、识别、endpoint hierarchy、mutation-boundary、treatment transformation 与 regulatory boundary，猫 FIP 的第一版可用中文内部 dossier 是什么？

## 执行摘要

基于当前 seed corpus，猫 FIP 现在已经可以被当成一个可用的内部研究对象，但前提是模块必须同时保留 `supportive diagnosis` 和 `treatment transformation`。

当前最强的组织逻辑是：

- systemic disease emergence from feline coronavirus background
- recognition through composite suspicion rather than one-test proof
- endpoint hierarchy instead of marker flattening
- mutation utility held together with diagnostic limitations
- disease-form-aware treatment transformation
- regulatory boundary held back behind route and legitimacy ambiguity

最重要的实际后果是，系统不该继续问“哪个 test 能 settle FIP？”更好的问题是：“哪组 recognition、mutation-support、disease-form 与 treatment layers 能支持一个 bounded working diagnosis，同时又不假装 certainty？”

这份中文页是建立在 working-English dossier 之上的中文派生层，不应被误解为双语 dossier，也不应被视为 decision-grade recommendation。

## 疾病框架

### quoted_fact

- broad review material 支持把 FIP 理解成 supportive diagnosis，而不是 one-test disease。
- mutation-origin 和 pathobiogenesis work 支持 systemic-disease emergence from feline coronavirus background。
- recombinant-outbreak 和 spread-boundary work 让任何 one-route mechanism simplification 都不成立。

### source_supported_conclusion

- FIP 应被建模成一个 `supportive diagnosis + pathobiogenesis-aware disease module`。
- 模块应同时保留 `feline coronavirus background` 与 `systemic FIP emergence logic`，不要把两者压成一层。
- mechanism 应该约束 diagnosis，而不是制造 diagnostic certainty。

## Recognition 层

### quoted_fact

- risk-factor 和 endemic multi-cat studies 支持 age、patterned signalment 和 ecology-aware exposure risk。
- Sydney 和 Taiwan clinicopathology series 支持 practical staged suspicion logic。
- effusive、non-effusive 和 neurologic branches 会带来不同的 recognition pressure。

### source_supported_conclusion

- recognition 应被分成 `risk context` 和 `suspicion-pattern recognition`。
- clinicopathology 目前仍然是最接近 operational 的 FIP recognition branch 之一。
- disease form 应改变 workup logic，而不是只被当成晚期 severity footnote。

## Endpoint 与 Marker Hierarchy

### quoted_fact

- acute-phase 和 immunoglobulin work 支持 supportive inflammatory laboratory context。
- older serology 仍然有历史意义，但在当前 workup authority 中更弱。
- mutation-assay studies 同时支持 diagnostic utility 和 diagnostic limitation。
- CSF viral detection 在 neurologic and/or ocular subgroup workup 中明显比 generic workup 更有用。

### source_supported_conclusion

- FIP endpoint logic 应继续保持分层：
  - suspicion-support
  - clinicopathology / disease-form support
  - mutation / molecular support
  - neurologic-extension support
  - treatment-follow-up outcomes
- mutation assays 和 CSF detection 都应继续被 use-case 约束。
- treatment follow-up outcomes 不应和 initial diagnostic support 混在一起。

## Mutation Boundary

### quoted_fact

- mutation-origin work 支持从 feline enteric coronavirus background 里出现 overt FIP。
- mutation-utility work 支持真实 diagnostic strengthening。
- mutation-limitation work 强烈支持不要把 mutation detection 扁平成 definitive diagnosis。

### source_supported_conclusion

- mutation 同时属于 mechanism 和 diagnosis，但不是以同一种方式属于。
- positive mutation support 和 mutation limits 必须一起保留。
- mutation testing 应当 strengthen workup，而不是替代 composite recognition。

## Treatment Transformation

### quoted_fact

- experimental 和 tissue-culture GS work 支持 preclinical antiviral foundation。
- natural-disease GS-441524 work 支持真实的 treatment transformation。

### source_supported_conclusion

- treatment branch 应继续分成 preclinical foundation、baseline efficacy、package logic、neurologic rescue 和 durability。
- FIP treatment 应被建模成 transformed，但不能被压平成 universal efficacy claim。
- neurologic disease 和 post-treatment durability 都是结构性重要的 treatment branches。
- remdesivir-plus-GS case series、neurologic treatment work 和 long-term remission follow-up 应分别保留为 package、rescue 和 durability layers。

## Regulatory Boundary

### source_supported_conclusion

- regulatory interpretation 目前应继续停在 boundary-page level。
- access-path、legitimacy 和 route-level interpretation 不应通过 treatment success language 被偷渡进来。
- FIP 可以比 route-level regulatory planning 更早支持 translation mapping。
- 当前 FIP topic layer 还没有 jurisdiction-specific regulatory source pack，且 treatment branch 明显比 regulatory branch 更厚。

## 不确定性 / 限制

- 当前 seed corpus 有 24 个 mapped sources，但仍有 2 个只是 ingest，还没有 deep extraction。
- 这份 dossier 主要建立在 compiled extraction 上，而不是对整个 corpus 的 full-text review。
- treatment access 和 regulatory route 相比 treatment efficacy architecture 仍然明显偏薄。
- 当前仍然没有 bilingual compiled FIP layer。

## 建议写回目标

- `topics/fip/index.md`
- `topics/fip/current-state-dashboard.md`
- `topics/fip/mechanism-overview.md`
- `topics/fip/endpoint-handbook.md`
- `topics/fip/risk-and-recognition.md`
- `topics/fip/translation-brief.md`
- `topics/fip/synthesis-index.md`
