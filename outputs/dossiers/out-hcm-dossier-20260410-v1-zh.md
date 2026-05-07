---
id: out-hcm-dossier-20260410-v1-zh
type: output
output_kind: dossier
language: zh
topic: hcm
question: "围绕疾病框架、识别、endpoint hierarchy、genotype pressure、remodeling depth 与治疗-监管边界，猫 HCM 的第一版可用中文内部 dossier 是什么？"
source_ids: [src-hcm-001, src-hcm-004, src-hcm-006, src-hcm-007, src-hcm-008, src-hcm-009, src-hcm-010, src-hcm-012, src-hcm-013, src-hcm-015, src-hcm-020, src-hcm-024]
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

# 猫 HCM Internal Dossier V1（中文）

源自：

- [out-hcm-dossier-20260410-v1-working-en.md](out-hcm-dossier-20260410-v1-working-en.md)

## 用户问题

围绕疾病框架、识别、endpoint hierarchy、genotype pressure、remodeling depth 与治疗-监管边界，猫 HCM 的第一版可用中文内部 dossier 是什么？

## 执行摘要

基于当前 seed corpus，猫 HCM 现在已经可以被当成一个可用的内部研究对象，但前提是要用对层级结构。

当前更合适的框架是把它理解成一个 `structure-first cardiomyopathy module`，而不是 biomarker-led 或 mutation-only 的对象。当前最强的组织逻辑是：

- phenotype confirmation 在前，不能让 biomarker enthusiasm 反客为主
- 用 endpoint hierarchy，而不是把 markers 压成平面列表
- 保留 genotype pressure，但不滑向 genotype determinism
- 在可见 hypertrophy 之下保留 remodeling depth
- 承认治疗现实，但同时保留明确的 evidence skepticism
- 在 product type 和 route fit 更清楚之前，把 regulatory 层停在 boundary

最重要的实际后果是，系统不应继续问“哪个单一 marker 能诊断 HCM？”更好的问题是：“哪组 structural、biomarker、genotype 与 remodeling 层的组合，最能支持 phenotype definition 和 severity interpretation，同时又不把治疗或 route readiness 说过头？”

这份中文页是建立在 working-English dossier 之上的中文派生层，不应被误解为双语 dossier，也不应被视为 decision-grade recommendation。

## 疾病框架

### quoted_fact

- broad feline cardiomyopathy 和 HCM review material 支持把 HCM 放在更宽的 feline cardiomyopathy frame 里理解。
- echocardiographic work 显示自发性 feline HCM 是结构异质性的，而不是单一均一 phenotype。
- comparative framing papers 把 feline HCM 放在 human HCM 的 spontaneous large-animal model 位置上。

### source_supported_conclusion

- HCM 应当被存成一个位于更宽 feline cardiomyopathy 框架中的 `core hypertrophic phenotype spine`。
- 系统应同时保留 `HCM core architecture` 和 `non-HCM cardiomyopathy boundary pressure`。
- cross-species model relevance 应属于 disease object，但不能替代 feline-specific phenotype logic。

## 识别与诊断流程层

### quoted_fact

- echocardiographic assessment 显示 feline HCM 的结构表型具有异质性。
- morphometry work 支持可测量的 structural phenotype discrimination。
- NT-proBNP screening work 不能可靠识别 mild-to-moderate 或 equivocal HCM。

### source_supported_conclusion

- `structural confirmation` 应继续作为 HCM recognition 的主导分支。
- `biomarkers` 应位于 phenotype definition 之下，不能超过 imaging 或 gross morphometry。
- `screening augmentation` 与 `phenotype confirmation` 在 workup architecture 里应继续分开。

## Endpoint 层

### quoted_fact

- troponin-I 在 moderate-to-severe HCM 中更高，在 active congestive heart failure 中更高。
- NT-proBNP 对 severe disease 的信号强于其 mild-disease screening 表现。
- pathology staging 与 phenotype-depth papers 支持 severity 是 layered 的，而不是一维度的。

### source_supported_conclusion

- 当前 endpoint hierarchy 应被组织成：
  - structural confirmation
  - screening augmentation
  - injury or severity pressure
  - pathology-depth context
- `troponin I` 和 `NT-proBNP` 不应再被当成可互换的 HCM endpoints。
- pathology-depth 与 late-stage remodeling 应进入 endpoint architecture，因为它们会改变 severity interpretation。

## Genotype-Severity 层

### quoted_fact

- genetics-focused clinical work 显示 homozygous MYBPC3-mutant cats 的 severity 和 penetrance pressure 高于 heterozygous cats。
- genetics review material 支持更宽 inherited HCM frame，而不是 one-mutation story。

### source_supported_conclusion

- genotype 分支应继续保持 `stratified`，而不是 binary。
- `mutation dosage` 和 `age-related penetrance` 已经足以改变当前 HCM compiled map。
- genotype 应加深 severity interpretation，而不是替代 phenotype confirmation。

## Phenotype 与 Remodeling Depth

### quoted_fact

- remodeling-focused work 支持 cardiomyocyte-initiated 和 macrophage-driven remodeling processes。
- anatomopathological staging work 支持把 end-stage HCM 理解成更宽的 remodeled phenotype，而不只是更重的 hypertrophy。

### source_supported_conclusion

- `remodeling` 应被视作位于 phenotype 之下的真实分支，而不是 wall-thickening 下的边注。
- `fibrosis` 与 remodeled late-stage structure 会加深 phenotype interpretation，而不是替代它。
- end-stage HCM 应被建模成更深的 structural change，而不是单纯 hypertrophy 的延长线。

## 治疗与监管边界

### quoted_fact

- 一篇 2025 review 把 feline HCM treatment 描述为控制临床症状、减慢 progression、改善 quality 和 life expectancy。
- 当前 seed corpus 同时包含 targeted-therapy work，也包含明确质疑 feline HCM treatment 是否更多建立在 science 还是 faith 上的论文。

### source_supported_conclusion

- 当前 treatment layer 应被写成 `real but overclaim-sensitive`。
- 当前最安全的 treatment architecture 是 `bounded management + selective targeted frontier`。
- 当前 HCM 证据可以更早支持 translation mapping，但还不能支持 route-level regulatory analysis。
- regulatory 层现在应继续停在 boundary page，直到 product type、assay-versus-drug distinction 和 route fit 更清楚。
- 当前 HCM topic layer 还没有 HCM-specific regulatory source pack。

## 不确定性 / 限制

- 当前 HCM seed corpus 已映射 24 个来源，且 24 张 paper card 均已有 round-1 deep extraction coverage；但本 dossier 仍不是全文逐行核读或决策级指导。
- 这份 dossier 主要仍建立在 first-round compiled extraction 上，而不是对整个语料逐行 full-text review。
- treatment hierarchy 仍然薄于 recognition 和 phenotype architecture。
- 当前还没有 HCM-specific regulatory source pack。

## 建议写回目标

- `topics/hcm/index.md`
- `topics/hcm/current-state-dashboard.md`
- `topics/hcm/mechanism-overview.md`
- `topics/hcm/endpoint-handbook.md`
- `topics/hcm/risk-and-recognition.md`
- `topics/hcm/translation-brief.md`
- `topics/hcm/synthesis-index.md`
