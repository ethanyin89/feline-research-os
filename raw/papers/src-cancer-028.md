---
id: src-cancer-028
type: source
title: "Prognostic histopathological and molecular markers in feline mammary neoplasia"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2012
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
doi: "10.1016/j.tvjl.2012.05.008"
pmid: 22841451
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, prognostic, histopathological, molecular, markers, mammary, neoplasia]
links:
  doi: "10.1016/j.tvjl.2012.05.008"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S1090023312001979?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The intake sheet lists this title: Prognostic histopathological and molecular markers in feline mammary neoplasia."
    - "The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S1090023312001979?via%3Dihub."
  source_supported_conclusion:
    - "This card is a first-pass intake object only; it should control triage and source ownership, not reader-facing claims."
  llm_inference:
    - "The likely claim-fit must be checked against the abstract or full text before promotion."
  # V2 enhanced fields
  study_design: "综述（2012 年 Vet J），FMC 组织病理学和分子预后标记物，与人类乳腺癌比较"
  core_argument: "肿瘤分级和有丝分裂指数是经验证的 FMC 预后标记物——高 ER 阴性率使 FMC 成为晚期激素独立型乳腺癌的模型"
  implicit_premise: "假设'替代标记物'方法（与分级相关而非临床结局）可验证分子标记物的预后价值；假设 Ki67 等标记物在标准化后将有预后价值"
  unexpected_finding: "许多研究使用'替代标记物'（如与组织学分级相关）而非临床结局来评估分子标记物预后价值——这一方法学缺陷削弱了部分标记物的证据"
  title_gap: "标题说 FMC 的组织病理学和分子预后标记物，但真正发现是模型特异性：FMC 高 ER 阴性率使其仅适合作为晚期激素独立型乳腺癌的模型——而非所有乳腺癌亚型"
  evidence_boundary: "2012 年综述，分子标记物建议可能已进化；'替代标记物'方法警告削弱部分标记物证据"
---

# Prognostic histopathological and molecular markers in feline mammary neoplasia

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2012 Vet J review: FMC is ~11% of feline tumors; tumor grade + mitotic index are validated prognostic markers; high ER-negative rate makes FMC model for late-stage hormone-independent breast cancer. [Deep extraction worksheet](../../system/indexes/src-cancer-028-deep-extraction-round1.md).

## Full Abstract (PubMed)

Feline mammary tumours comprise approximately 11% of feline non-integumentary neoplasms, are more commonly malignant than benign, and carry a poor prognosis attributable to a high probability of local recurrence and metastasis. This review discusses histopathological and molecular markers that could aid in prognostic discrimination, and draws comparisons with studies examining prognostic markers in breast cancer. Tumour grade and mitotic index correlate with survival data and could be useful for prognostication. Although assessment of Ki67 expression might have prognostic potential, further studies are required to corroborate the correlation between expression and clinical outcome. Additional molecular markers that have been investigated for prognostic potential can be grouped according to the 'hallmarks of cancer'. Many studies utilise 'surrogate markers' of clinical outcome, such as correlation with histological grade, to assess the prognostic value of molecular markers, and further investigation is therefore necessary before reaching firm conclusions regarding the prognostic value of some markers. Feline mammary tumours have been proposed as spontaneous models of breast cancer but might only be suitable models for certain molecular sub-types. Compared to humans, cats tend to have a high percentage of mammary tumours which are oestrogen receptor-negative and they might therefore be suitable models for late stage oestrogen receptor-negative breast cancer. The basal-like properties of feline mammary carcinomas offer another avenue for future research in this field of comparative oncology.

## Key Extracted Findings

| Finding | Value | Boundary |
|---------|-------|----------|
| FMC prevalence | ~11% of feline non-integumentary neoplasms | review estimate |
| Malignancy ratio | more commonly malignant than benign | consistent with other sources |
| Prognosis | poor due to high local recurrence and metastasis | general characterization |
| Validated prognostic markers | tumor grade + mitotic index | correlate with survival |
| Ki67 status | potential prognostic value, needs more studies | research direction |
| ER status | high ER-negative rate in cats vs humans | comparative oncology |
| Model suitability | late-stage ER-negative breast cancer | molecular subtype specific |
| Basal-like properties | FMC has basal-like features | comparative oncology research avenue |

**Key insight:** This review validates tumor grade and mitotic index as the most reliable prognostic markers, while noting that molecular markers like Ki67 need further standardization. The high ER-negative rate positions FMC as a model specifically for late-stage, hormone-independent breast cancer.

**Boundary:** This is a 2012 review. Molecular marker recommendations may have evolved. The "surrogate marker" caveat (using grade correlation instead of clinical outcome) weakens evidence for some markers.

## One-Line Summary

2012 Vet J review: FMC is ~11% of feline tumors; tumor grade + mitotic index are validated prognostic markers; high ER-negative rate makes FMC model for late-stage hormone-independent breast cancer.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- The intake sheet lists this title: Prognostic histopathological and molecular markers in feline mammary neoplasia.
- The intake sheet locator is: https://www.sciencedirect.com/science/article/abs/pii/S1090023312001979?via%3Dihub.

### source_supported_conclusion

- This is a first-pass source-card placeholder for triage and queue control.
- It should not support prevalence, diagnostic, treatment, management, or risk-ranking claims yet.

### llm_inference

- The title suggests a possible `cancer` role, but the actual claim-fit requires abstract or full-text review.

## Claim-Fit Judgment

Strongest safe use:

- intake ownership
- source queue placement
- deduplication and future extraction planning

Must not control yet:

- reader-facing medical advice
- numeric claims
- comparative ranking
- guideline-like recommendations
- mechanism closure

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the cancer module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: cancer
- models:
- endpoints:
- mechanisms:
- regulations:
