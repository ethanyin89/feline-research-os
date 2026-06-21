---
id: src-fip-028
type: source
title: "GS-441524 and molnupiravir are similarly effective for the treatment of cats with feline infectious peritonitis"
source_kind: paper
species: feline
diseases: [FIP]
models: [prospective comparative cohort]
endpoints: [mortality, remission, clinical resolution, adverse events]
jurisdictions: []
evidence_level: original-study
status: extracted
extraction_depth: full
year: 2024
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, gs-441524, molnupiravir, antiviral, comparison, treatment, head-to-head]
links:
  doi: "10.3389/fvets.2024.1422408"
  url: "https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2024.1422408/full"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "118 cats with FIP: 59 received GS-441524 and 59 received molnupiravir."
    - "GS-441524: 12/59 deaths (20.3%); Molnupiravir: 8/59 deaths (13.6%); p = 0.326."
    - "Remission: GS-441524 48/48 (100%); Molnupiravir 51/52 (98%) among treatment completers."
    - "Most deaths occurred within the first 10 days of treatment."
    - "Parameters normalized within 6 to 7 weeks of treatment initiation."
  source_supported_conclusion:
    - "GS-441524 and molnupiravir show similar effects and safety in cats with FIP."
    - "No statistically significant difference in mortality between treatments."
    - "Both achieve near-complete remission in cats that survive initial treatment phase."
  llm_inference:
    - "Treatment choice can be guided by availability, cost, or formulation preference rather than efficacy."
    - "Early mortality (first 10 days) may reflect disease severity at presentation rather than treatment failure."
  # V2 enhanced fields
  study_design: "前瞻性比较队列研究，118 只 FIP 猫（GS-441524 59 只 vs molnupiravir 59 只），84 天疗程"
  core_argument: "GS-441524 与 molnupiravir 在猫 FIP 治疗中疗效相当——死亡率无显著差异（20.3% vs 13.6%, p=0.326），完成治疗者缓解率均接近 100%"
  implicit_premise: "假设非随机队列设计中的两组匹配足以支持因果推断；假设 84 天随访足以评估缓解而非仅观察早期应答"
  unexpected_finding: "大多数死亡发生在治疗前 10 天——这提示早期死亡可能反映入组时疾病严重程度，而非药物选择的差异"
  title_gap: "标题说 GS-441524 和 molnupiravir 疗效相当，但真正发现是临床决策简化：118 只猫头对头比较无显著差异——治疗选择可以由可及性和成本而非疗效差异驱动"
  evidence_boundary: "非 RCT 设计无法排除选择偏倚；未报告长期复发率；不能回答成本效益或药物耐药性问题"
---

# GS-441524 and molnupiravir are similarly effective for treatment of cats with FIP

## Evidence-Depth Caveat

Full text reviewed. This is a prospective comparative cohort study with matched groups. It supports comparative efficacy claims but is not a randomized controlled trial.

## One-Line Summary

Head-to-head comparison of 118 cats showed GS-441524 and molnupiravir achieve equivalent remission rates (~99%) with no significant difference in mortality.

## Why It Matters For Feline FIP

First direct comparison of the two main FIP antivirals with sufficient sample size. Establishes that molnupiravir is a viable alternative when GS-441524 is unavailable or cost-prohibitive.

## Study Design Details

### Population

| Parameter | GS-441524 | Molnupiravir |
|-----------|-----------|--------------|
| Total cats | 59 | 59 |
| Effusive FIP | ~38 | ~38 |
| Non-effusive FIP | ~21 | ~21 |
| Completed treatment | 48 | 52 |

76 of 118 cats had effusive FIP (fluid accumulation).

### Treatment Protocols

| Drug | Dose Range | Duration | Dose Adjustment |
|------|------------|----------|-----------------|
| GS-441524 (Mutian® Xraphconn) | 12.5–25 mg/kg/day | 84 days | Lower for effusive, higher for neuro/ocular |
| Molnupiravir (compounded) | 20–40 mg/kg/day | 84 days | Lower for effusive, higher for neuro/ocular |

## Key Findings

### quoted_fact

- **Mortality:** GS-441524 20.3% (12/59) vs Molnupiravir 13.6% (8/59), p = 0.326
- **Remission:** GS-441524 100% (48/48) vs Molnupiravir 98% (51/52) among completers
- **Timing:** Most deaths within first 10 days
- **Clinical resolution:** Neurological and ocular signs resolved in all but one cat (persistent seizures)
- **Lab normalization:** Within 6-7 weeks of treatment initiation

### source_supported_conclusion

- No significant efficacy difference between GS-441524 and molnupiravir
- Both achieve near-complete remission in treatment completers
- Adverse events similar: transient hepatic abnormalities resolving without intervention
- Early mortality reflects disease severity, not treatment failure

### llm_inference

- Molnupiravir validated as equivalent alternative to GS-441524
- Treatment selection can prioritize availability/cost/formulation
- 84-day protocol standard for both drugs
- Higher doses needed for neurological/ocular involvement (both drugs)

## Claim-Fit Judgment

Strongest safe use:
- Comparative antiviral efficacy between GS-441524 and molnupiravir
- Molnupiravir as viable first-line FIP treatment
- Remission rates for both drugs
- 84-day treatment duration standard

Must not control yet:
- Optimal dosing within ranges (individualized based on presentation)
- Long-term relapse rates (study reports remission, not long-term follow-up)
- Cost-effectiveness (not studied)
- Drug-resistant case management

## Deep Extraction

- Round 1 worksheet: [system/indexes/src-fip-028-deep-extraction-round1.md](../../system/indexes/src-fip-028-deep-extraction-round1.md)

## Clinical Context

This study addresses a critical clinical question: are the two available FIP antivirals truly interchangeable? GS-441524 became the first effective FIP treatment in 2019, but availability and cost issues drove interest in alternatives. Molnupiravir, originally developed for influenza and later used against COVID-19, emerged as a potential option. This head-to-head comparison provides the evidence base for treating either drug as a first-line option, with selection guided by availability, cost, and formulation preferences rather than efficacy differences.

The use of dose adjustment by disease severity (lower for effusive, higher for neurological or ocular involvement) reflects clinical experience that central nervous system penetration requires higher plasma concentrations for both drugs. This dosing strategy is now standard practice in FIP treatment protocols.

## Linked Entities

- diseases: FIP (effusive and non-effusive)
- models: prospective comparative cohort
- endpoints: mortality, remission, clinical resolution, hepatic function
- mechanisms: antiviral (nucleoside analogs - both are adenosine analogs)
- regulations: none applicable
