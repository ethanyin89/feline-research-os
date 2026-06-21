---
id: src-ckd-029
type: source
title: "A long term feed supplementation based on phosphate binders in Feline Chronic Kidney Disease"
source_kind: paper
species: feline
diseases: [CKD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2018
status: extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, long, term, feed, supplementation, based, phosphate, binders]
links:
  doi: "10.1007/s11259-018-9719-z"
  url: "https://doi.org/10.1007/s11259-018-9719-z"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The full article reports a 360-day study of 20 cats with IRIS stage 3 or 4 CKD: 10 supplemented cats and 10 database controls."
    - "The multi-ingredient supplement contained calcium carbonate, calcium-lactate gluconate, chitosan, and sodium bicarbonate at 0.2 g/kg/day with food."
    - "Two authors were employees of the supplement manufacturer."
  source_supported_conclusion:
    - "The study supports a source-specific serum-phosphorus reduction signal in advanced CKD."
    - "Nonrandomized grouping, small sample size, a multi-ingredient product, and commercial conflict prevent comparative or product-level recommendations."
  llm_inference:
    - "The most reusable lesson is the need to pair phosphorus response with calcium, bicarbonate, renal-function, and tolerability monitoring."
  # V2 enhanced fields
  study_design: "非随机化 360 天研究，20 只 IRIS 3 或 4 期 CKD 猫（10 只补充组、10 只数据库对照），多成分磷酸盐结合和碱化补充剂"
  core_argument: "多成分磷酸盐结合补充剂（碳酸钙、乳酸葡萄糖酸钙、壳聚糖、碳酸氢钠）可降低晚期 CKD 猫血清磷——但非随机化设计和商业利益冲突需要独立验证"
  implicit_premise: "假设数据库对照（拒绝补充剂的所有者的猫）具有可比性；假设多成分制剂效果可归因于磷酸盐结合"
  unexpected_finding: "离子钙升高但据作者称仍在范围内——钙基磷酸盐结合剂需要钙监测"
  title_gap: "标题说磷酸盐结合剂长期补充，但真正发现是方法学警告：非随机化设计、商业利益冲突、钙升高——需要独立验证才能转化为实践"
  evidence_boundary: "不能建立生存获益、肾功能恢复或成分特异性效应；两位作者为制造商员工；不应用于早期 CKD"
---

# A long term feed supplementation based on phosphate binders in Feline Chronic Kidney Disease

## Evidence-Depth Caveat

This card is based on review of the complete eight-page article PDF. It is deep-extracted as a guarded intervention study, not promoted as product guidance.

## Source Check, 2026-06-06

Crossref + PubMed abstract was checked as a repeatable second-pass intake step.

- Metadata resolved: yes
- Metadata provider: Crossref + PubMed abstract
- Container: Veterinary Research Communications
- Year: 2018
- Abstract available: yes

Use boundary:

- This source check was superseded by complete PDF review on 2026-06-06.
- Reuse must follow `system/indexes/src-ckd-029-deep-extraction-round1.md`.

Abstract lead for scope check only: Chronic kidney disease (CKD) is a very common disorder in elderly cats. A proper renal diet represents the most efficient therapeutic intervention to improve survival and life qua...

## Deep Extraction, 2026-06-06

- Access: complete eight-page article PDF.
- Worksheet: `system/indexes/src-ckd-029-deep-extraction-round1.md`.
- Promotion boundary: guarded source-specific phosphorus signal only; no product, dosing, comparative, or survival recommendation.

## One-Line Summary

Small nonrandomized 360-day study of a multi-ingredient phosphate-binding and alkalinizing supplement in cats with stage 3 or 4 CKD.

## Why It Matters For Feline CKD

The study provides a long-duration phosphorus-control signal and exposes the monitoring and evidence-quality boundaries that product-like CKD interventions require.

## Key Findings

### quoted_fact

- Twenty cats were included: 10 supplemented and 10 controls.
- All cats had IRIS stage 3 or 4 CKD, hyperphosphatemia, and the same renal diet.
- The supplement was given at 0.2 g/kg/day for 360 days.
- Treated-group mean phosphorus changed from 7.72 to 3.76 mg/dL; control mean changed from 7.83 to 8.91 mg/dL.
- Two authors were manufacturer employees.

### source_supported_conclusion

- The supplement was associated with lower serum phosphorus and higher bicarbonate in this small advanced-CKD cohort.
- Ionized calcium increased but remained within the range stated by the authors.
- The study did not establish survival benefit, renal recovery, ingredient-specific effects, or binder-class superiority.

### llm_inference

- This source belongs below guideline and independent trial evidence in any treatment hierarchy.

## Claim-Fit Judgment

Strongest safe use:

- source-specific phosphorus endpoint signal
- calcium and bicarbonate monitoring boundary
- evidence-quality example for product-like CKD interventions

Must not control:

- product recommendation or dosing
- comparative phosphate-binder ranking
- survival or disease-modification claims
- use in early-stage CKD

## Study Design Details

### Intervention Composition

- Calcium carbonate + calcium-lactate gluconate (phosphate binding)
- Chitosan (phosphate binding)
- Sodium bicarbonate (alkalinization)
- Dose: 0.2 g/kg/day, divided into two administrations with food

### Population

- 20 cats total: 10 supplemented, 10 database controls
- IRIS stages: 80% stage 3, 20% stage 4
- All cats hyperphosphatemic and on the same renal diet
- Controls selected from clinic database (owners had declined supplements)

### Key Limitations

- Not randomized: selection bias cannot be excluded
- Small sample: only 10 treated cats
- Multi-ingredient: cannot attribute effects to single component
- Manufacturer employees among authors: requires independent replication

### Monitoring Parameters

| Parameter | Baseline (treated) | Day 360 (treated) | Change |
|-----------|-------------------|-------------------|--------|
| Phosphorus | 7.72 mg/dL | 3.76 mg/dL | -48% |
| Bicarbonate | 16.08 mmol/L | 17.08 mmol/L | increased |
| Ionized calcium | 1.20 mmol/L | 1.33 mmol/L | increased (within range) |
| Creatinine | - | 4.18 mg/dL | stable |

## Image Assets

No figures captured. Tables document phosphorus-control signal but do not warrant reader-facing promotion without randomized controlled trial replication.

## Linked Entities

- diseases: CKD (stages 3-4)
- models: nonrandomized supplementation study
- endpoints: serum phosphorus, creatinine, BUN, ionized calcium, bicarbonate, UPC
- mechanisms: phosphate binding, alkalinization
- regulations: none applicable
