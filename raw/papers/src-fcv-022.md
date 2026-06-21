---
id: src-fcv-022
type: source
title: "Modified-Live Feline Calicivirus Vaccination Elicits Cellular Immunity against a Current Feline Calicivirus Field Strain in an Experimental Feline Challenge Study"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [cellular immunity, cross-immunity, challenge response]
jurisdictions: []
evidence_level: original-study
year: 2021
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, vaccine, cellular-immunity, challenge, mlv]
links:
  doi: "10.3390/v13091736"
  url: "https://www.mdpi.com/1999-4915/13/9/1736"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Accessible abstract reports that modified-live FCV vaccination induced cellular but not humoral cross-immunity in the reported challenge setting."
    - "Accessible abstract reports that vaccinated cats developed Th1 cytokine responses against heterologous challenge strains."
    - "Accessible abstract reports that vaccinated cats developed IFN-gamma-releasing PBMC responses against heterologous challenge strains."
    - "Accessible title and summary report an experimental challenge study against a current FCV field strain."
  source_supported_conclusion:
    - This is the current key FCV vaccine-immunology paper for separating cellular from humoral cross-protection.
    - The paper supports a more nuanced reading of vaccine benefit than neutralising-antibody titres alone.
    - The paper supports cellular immunity as a distinct endpoint family under the FCV vaccine branch.
    - The paper should strengthen challenge- and endpoint-layer reasoning, not product-ranking rhetoric.
  llm_inference:
    - This source now serves as the first deep-extracted cellular-immunity anchor in the FCV vaccine branch.
    - The safest downstream wording is `benefit beyond titre logic`, not `superior vaccine`.
  # V2 enhanced fields
  study_design: "实验性挑战研究，使用接种了改良活疫苗的家猫，评估其针对异源野外流行毒株的免疫反应"
  core_argument: "改良活疫苗接种的猫虽缺乏体液交叉中和抗体，但能产生针对当前流行猫杯状病毒毒株的显著细胞免疫应答"
  implicit_premise: "细胞免疫反应的存在及其测定能反映疫苗诱导的保护效果，且不同免疫指标（细胞免疫与体液免疫）对保护作用有独立贡献"
  title_gap: "标题强调疫苗诱导细胞免疫，但实际上其发现揭示了细胞免疫能在缺乏体液交叉中和的情况下提供保护——提示传统抗体检测可能低估了疫苗效益"
  evidence_boundary: "未评价疫苗对整体临床保护率的直接影响，也未研究长期免疫持续性及不同病毒亚型间完整交叉保护能力"
  unexpected_finding: "接种疫苗的猫在缺乏体液交叉中和抗体的情况下仍能显著产生针对异源毒株的Th1细胞因子及IFN-γ释放，表明细胞免疫在交叉保护中起关键作用"
---

# Modified-Live Feline Calicivirus Vaccination Elicits Cellular Immunity against a Current Feline Calicivirus Field Strain in an Experimental Feline Challenge Study

## One-Line Summary

Challenge study showing modified-live FCV vaccination can induce meaningful cellular cross-immunity even when humoral cross-neutralisation is limited.

## Why It Matters For FCV

- gives the module a cellular-immunity explanation for why vaccine benefit may exceed simple antibody breadth
- helps interpret older neutralisation papers without flattening them into vaccine success or failure
- now serves as the first FCV deep-extracted cellular-immunity anchor

## Key Findings

### quoted_fact

- Accessible abstract reports modified-live FCV vaccination induced cellular but not humoral cross-immunity in the reported challenge setting.
- Accessible abstract reports vaccinated cats developed Th1 cytokine responses after vaccination and heterologous challenge.
- Accessible abstract reports vaccinated cats developed IFN-gamma-releasing PBMC responses against heterologous challenge strains.
- Accessible title and summary report an experimental challenge study against a current FCV field strain.

### source_supported_conclusion

- This source is the current best FCV endpoint paper for separating cellular cross-immunity from humoral breadth.
- The paper supports vaccine benefit as layered immune function rather than one flat antibody number.
- The strongest safe read is `cellular benefit without product-superiority claims`.

### llm_inference

- If the module later builds a vaccine-comparison page, this card should sit above simple titre rhetoric and below field-effectiveness claims.

## Limits / Caveats

- experimental SPF-cat challenge work does not equal field performance
- current card is deep-extracted at worksheet level, but still not full-text reviewed section by section
- this paper should not be promoted into universal vaccine-policy claims by itself

## Vaccine-Immunology Branch Logic

What can be promoted:

- cellular immunity is a real FCV vaccine endpoint family
- vaccine benefit may exceed what humoral cross-neutralisation alone predicts
- challenge-based immune interpretation is richer than simple titre language

What should be held:

- any current-market superiority claim
- any whole-population field-effectiveness claim
- any statement that cellular immunity resolves chronic-carrier or persistence control

This card is best reused as an endpoint-separation and vaccine-immunology source, not as a routine product-ranking source.

Its main value is architectural: it lets the module say that `vaccine benefit can exceed antibody breadth` without slipping into `this product solves FCV` rhetoric. That makes it a control source for downstream endpoint and translation pages, not just another positive vaccine paper.

## Write-Back Implications

- [endpoint handbook](../../topics/fcv/endpoint-handbook.md) should treat this card as the first deep-extracted cellular-immunity anchor.
- [FCV vaccine-persistence boundary memo](../../system/indexes/fcv-vaccine-persistence-boundary-memo.md) can now lean more directly on `benefit beyond titre logic`.
- [translation brief](../../topics/fcv/translation-brief.md) can safely describe vaccine benefit as layered rather than purely humoral.

## Open Follow-Up Questions

- how much protection was explained by cellular immunity versus later induced cross-neutralising antibodies?
- how should this paper be reconciled with cross-neutralisation panels and platform-vaccine studies?

## Linked Entities

- diseases: FCV
- models:
- endpoints: cellular immunity, cross-immunity, challenge response
- mechanisms: IFN-gamma, Th1 response, PBMC response
- regulations:
