---
id: out-fip-briefing-20260410-round1-zh
type: output
output_kind: briefing
language: zh
topic: fip
question: "基于当前 FIP seed corpus，猫传染性腹膜炎在 pathobiogenesis、识别、endpoints、mutation-boundary 与抗病毒治疗上的第一版可用内部视图是什么？"
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

# 内部简报：猫 FIP Round 1

Derived from:

- [out-fip-briefing-20260410-round1-working-en.md](out-fip-briefing-20260410-round1-working-en.md)

## 用户问题

基于当前 FIP seed corpus，猫传染性腹膜炎在 pathobiogenesis、识别、endpoints、mutation-boundary 与抗病毒治疗上的第一版可用内部视图是什么？

## 执行摘要

当前证据支持把猫 FIP 理解成一个由 `diagnostic ambiguity plus treatment transformation` 共同定义的 disease module，而不是 one-test diagnosis，也不是旧时代 fatalism-only story。

当前最强的组织性结论是：猫 FIP 应该围绕以下 5 层组织：

- systemic-disease emergence from feline coronavirus background
- composite and supportive recognition
- disease-form-aware workup
- mutation utility held together with mutation limits
- antiviral treatment transformation with distinct treatment sublayers

当前 corpus 还清楚支持另外 4 点。

第一，FIP 的 recognition 仍然属于 `supportive and composite` diagnostic frame。clinicopathology 和 disease-form logic 现在比任何单一 assay 更重要。

第二，endpoint layer 最适合被建模成 `layered support`，而不是一个全局 marker ranking。

第三，mutation-related testing 是真实分支，但它是 bounded support，不足以单独支撑 certainty language。

第四，treatment branch 已经足够强，会改变整个模块，但它仍然必须分开 baseline GS efficacy、package logic、neurologic rescue 和 durability。

这是一份中文派生简报，不应被误读为更高证据强度或 decision-grade recommendation。

## 证据支持要点

### quoted_fact

- broad FIP review material 支持 supportive diagnosis，而不是 one-test certainty。
- mutation-origin 与 pathobiogenesis papers 支持 systemic disease emergence from feline coronavirus background，而不是把 enteric coronavirus 直接等同于 overt FIP。
- risk 与 clinicopathology papers 支持 young age、patterned signalment、multi-cat exposure 和 clinicopathologic pattern recognition 是重要的 suspicion-building layers。
- mutation-assay utility 和 limitation papers 同时支持 positive support value 与真实 diagnostic limits。
- CSF-based viral detection 在 neurologic and/or ocular subgroup 中明显比 ordinary workup 更有用。
- GS-441524 与 remdesivir-era papers 支持 naturally occurring disease 中真实的 treatment transformation。
- long-term remission follow-up 与 neurologic-treatment papers 支持 durability 和 disease-form-specific treatment complexity 应该被建成独立分支，而不是扁平 cure claim。

### source_supported_conclusion

- FIP 应被建模成 `supportive diagnosis + antiviral treatment transformation`，而不是 diagnosis-only 或 treatment-only。
- recognition branch 应继续保持 disease-form-aware 和 clinicopathology-led。
- endpoint logic 应继续分层：
  - suspicion-support
  - clinicopathology / disease-form support
  - mutation / molecular support
  - neurologic-extension support
  - treatment-follow-up outcomes
- mutation-related assays 应被呈现成 bounded workup support，而不是 definitive FIP proof。
- 现代 treatment evidence 已经足够强，足以支撑 dedicated translational branch。
- neurologic rescue 和 long-term remission 不应被压进 baseline GS-441524 efficacy claim。

### llm_inference

- FIP 目前是最清楚展示 `diagnostic ambiguity` 和 `treatment transformation` 可以同时存在而不矛盾的 disease module 之一。
- 这份 briefing 之后最有价值的 compiled move，很可能是更紧的 FIP output ladder，而不是继续发散 memo。

## 不确定性 / 限制

- 这份中文简报是从 working-English 输出层派生而来，不代表比底层证据更强。
- seed corpus 有 24 个 mapped sources，其中 22 个已 deep-extracted，但仍有 2 个只到 ingest 层。
- treatment access、legal status 和 regulatory route 仍然太薄，不能给出 decision-grade guidance。
- 当前仍然没有 bilingual compiled FIP layer。

## 建议写回目标

- `topics/fip/index.md`
- `topics/fip/mechanism-overview.md`
- `topics/fip/endpoint-handbook.md`
- `topics/fip/risk-and-recognition.md`
- `topics/fip/translation-brief.md`
- `topics/fip/synthesis-index.md`
