---
id: src-fip-027
type: source
title: "Open label clinical trial of orally administered molnupiravir as a first-line treatment for naturally occurring effusive feline infectious peritonitis"
source_kind: paper
species: feline
diseases: [FIP]
models: [open-label clinical trial]
endpoints: [clinical remission, survival]
jurisdictions: []
evidence_level: original-study
status: ingested
extraction_depth: partial
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, molnupiravir, antiviral, treatment, clinical-trial, effusive]
links:
  doi: "10.1111/jvim.17187"
  url: "https://onlinelibrary.wiley.com/doi/10.1111/jvim.17187"
  local_assets: []
year: 2024
evidence_policy:
  quoted_fact:
    - "Ten cats with naturally occurring effusive FIP treated with molnupiravir; 10 historical control cats treated with PO GS-441524."
    - "Dose: 10-15 mg/kg PO q12h for 84 days."
    - "Eight of the 10 cats treated with MPV survived and were in remission at 16 weeks."
    - "The 2 non-survivors died in the first 24 hours of treatment."
    - "Non-inferiority trial comparing molnupiravir to GS-441524."
  source_supported_conclusion:
    - "80% remission rate (8/10) at 16 weeks with molnupiravir for effusive FIP."
    - "Early deaths (first 24 hours) likely reflect disease severity at presentation, not drug failure."
    - "Clinicopathologic features compared to historical GS-441524 controls."
  llm_inference:
    - "Prospective non-inferiority design strengthens molnupiravir evidence vs retrospective case series."
    - "Oral administration may offer practical advantages over GS-441524 formulations."
  # V2 enhanced fields
  study_design: "开放标签临床试验，10 只渗出型 FIP 猫使用莫努匹韦 10-15 mg/kg PO BID 84 天，10 只历史对照使用 GS-441524"
  core_argument: "莫努匹韦作为渗出型 FIP 一线治疗有效——8/10（80%）在 16 周达到缓解，2 只非存活者在治疗前 24 小时内死亡"
  implicit_premise: "假设历史对照与前瞻性治疗组可比；假设 24 小时内死亡反映疾病严重程度而非药物失败"
  unexpected_finding: "较低剂量范围（10-15 mg/kg）与病例系列（10-20 mg/kg）相比仍有效——可能降低成本和不良反应"
  title_gap: "标题说一线治疗有效性，但真正价值是剂量发现：10-15 mg/kg 比文献中 10-20 mg/kg 更低却仍有效——这可能显著降低治疗成本和不良反应风险"
  evidence_boundary: "小样本（n=10）；开放标签设计；不能外推至非渗出型 FIP；与 GS-441524 的比较为历史对照而非随机对照"
---

# Open label clinical trial of molnupiravir as a first-line treatment for effusive FIP

## Evidence-Depth Caveat

Abstract-weighted extraction only. Full text review needed for remission rates, adverse events, and comparison methodology.

## One-Line Summary

Open-label trial of 10 cats with effusive FIP demonstrated molnupiravir effectiveness at 10-15 mg/kg BID for 84 days.

## Why It Matters For Feline FIP

Provides prospective clinical trial evidence for molnupiravir as first-line FIP treatment, strengthening the evidence base beyond case series.

## Key Findings (Abstract-Level)

### quoted_fact

- Study design: Open-label clinical trial
- Population: 10 cats with naturally occurring effusive FIP
- Dose: 10-15 mg/kg PO q12h × 84 days
- Evaluation timepoints: 0, 6, 16 weeks
- Author: Reagan et al., 2024

### source_supported_conclusion

- Molnupiravir effective for effusive FIP
- First-line treatment viable

### llm_inference

- Prospective design strengthens evidence vs retrospective case series
- Lower dose range (10-15 mg/kg) vs case series (10-20 mg/kg)

## Claim-Fit Judgment

Strongest safe use:
- Molnupiravir efficacy for effusive FIP
- First-line treatment evidence

Must not control yet:
- Specific remission percentages (need full text)
- Non-effusive FIP extrapolation
- Comparison to GS-441524 outcomes

## Linked Entities

- diseases: FIP (effusive form)
- models: open-label clinical trial
- endpoints: clinical remission at 6 and 16 weeks
- mechanisms: antiviral (nucleoside analog)
- regulations: none applicable
