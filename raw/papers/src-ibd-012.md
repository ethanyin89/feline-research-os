---
id: src-ibd-012
type: source
title: "Immunohistochemical Findings in Idiopathic Inflammatory Bowel Disease in Nine Cats"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2020
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, immunohistochemistry, pathology]
links:
  doi: "10.1155/2020/6209185"
  url: "https://onlinelibrary.wiley.com/doi/10.1155/2020/6209185"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The abstract states that feline inflammatory bowel disease is an elimination diagnosis and cannot be diagnosed only through histologic findings.
    - The study included nine cats referred for chronic gastrointestinal signs and compared them with healthy control samples.
    - The abstract reports that TNF-alpha, IL-1beta, IL-12, and CD3-positive expression were significantly different between cats with IBD and controls.
    - The abstract reports no differences for TGF-beta, IL-10, and FOXP3.
  source_supported_conclusion:
    - This source belongs in the pathology-deepening side of the IBD workup branch.
    - The study supports an inflammatory-imbalance interpretation for idiopathic feline IBD, but not an operational diagnostic shortcut.
  llm_inference:
    - This paper is most useful as an idiopathic-IBD-side pathology depth page rather than a boundary-separation page.
  # V2 enhanced fields
  study_design: "前瞻性病例对照研究，纳入9只患有特发性炎症性肠病的猫及健康对照样本，采用免疫组织化学方法检测多种炎症及免疫标志物表达差异"
  core_argument: "特发性猫炎症性肠病患者肠组织中TNF-α、IL-1β、IL-12及CD3阳性表达显著不同于健康猫，提示该病存在炎症失衡机制，但单凭组织学无法确诊"
  implicit_premise: "不同炎症因子和免疫细胞的表达差异直接反映了炎症性肠病的病理生理状态，且这些标志物的检测足以揭示疾病机制"
  title_gap: "标题强调免疫组织化学发现，但实际揭示的是组织学检查不足以独立诊断特发性炎症性肠病，强调需综合诊断思路——这一点常被忽视"
  evidence_boundary: "该研究未评估临床治疗效果、病因学机制及长期预后，也未系统验证免疫标志物的诊断敏感性与特异性"
  unexpected_finding: "TGF-β、IL-10和FOXP3等免疫调节相关因子的表达在患病猫与健康猫间无显著差异，挑战了其作为免疫抑制标志物的作用假设"
---

# One-line Summary

Small immunohistochemistry study that likely deepens the pathology profile of idiopathic feline IBD.

## Why It Matters For IBD

- gives the module pathology depth on the IBD side rather than only on the lymphoma-comparison side
- may help clarify what `idiopathic IBD` means histologically in this corpus
- now serves as the first idiopathic-IBD immunopathology anchor in the module

## Key Findings

- abstract includes nine clinical IBD cats and healthy controls
- abstract reports higher TNF-alpha, IL-1beta, IL-12, and CD3-positive expression in IBD than controls
- abstract reports no significant difference for TGF-beta, IL-10, and FOXP3
- abstract concludes that an imbalance in immune response may play a role in the etiopathogenesis of feline IBD

## Idiopathic-IBD Immunopathology Role

This source gives the IBD side of the module its own immunopathology depth. The abstract states that feline IBD is an elimination diagnosis and cannot be diagnosed only through histologic findings. That statement should travel with every marker claim from this paper because it keeps the source inside exclusion-first architecture.

The study included nine cats with chronic gastrointestinal signs and healthy control samples. TNF-alpha, IL-1beta, IL-12, and CD3-positive expression were significantly different between cats with IBD and controls, while TGF-beta, IL-10, and FOXP3 were not. The source therefore supports an inflammatory-imbalance interpretation, not a complete diagnostic panel.

For wiki reuse, this card should be placed on the idiopathic-IBD side rather than the lymphoma-boundary side. It explains what inflammatory IBD tissue may look like immunologically, while other papers handle lymphoma comparison, biopsy-site selection, Bcl-2, COX-2, and metabolomics. Keeping those roles separate reduces overclaim risk.

The card is also useful because it reinforces the gap between mechanism depth and workup leadership. A cytokine or immune-cell pattern can make the pathogenesis page richer without becoming the next clinical test. The nine-cat size supports cautious explanatory use and argues against broad operational certainty.

The safe compiled rule is: idiopathic feline IBD may involve measurable mucosal immune imbalance, but the diagnosis remains exclusion-based and cannot rest on immunohistochemistry alone.

This card should also help prevent the IBD module from becoming only a negative-exclusion page. Exclusion is the architecture, but the disease still needs positive biologic depth once mimics are ruled down. Cytokine and CD3 expression differences give the idiopathic-IBD side a tissue-level inflammatory story, even if that story is not enough for standalone diagnosis.

The source should be cross-linked to microbiota and fibrosis pages because mucosal immune imbalance, dysbiosis, and remodeling are likely adjacent mechanism layers. However, it should remain separated from lymphoma-boundary marker papers. It compares IBD with healthy controls, so it explains IBD biology more than it resolves the small-cell lymphoma problem.

For future output, the phrasing should be: `IBD is exclusion-defined clinically, but not biologically empty; small immunohistochemistry studies support inflammatory-imbalance mechanisms`.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- nine-cat size suggests depth rather than wide operational certainty
- do not treat the cytokine pattern as a routine diagnostic panel
- do not use this IBD-versus-control source to claim lymphoma separation

## Open Follow-up Questions

- which immune-cell markers dominate?
- does this paper materially improve everyday diagnostic discrimination?
- how reproducible are TNF-alpha, IL-1beta, IL-12, and CD3 findings in larger cohorts?
- should this source feed an immunopathology subsection rather than an endpoint table?

## Deep Extraction

- [src-ibd-012 deep extraction round 1](../../system/indexes/src-ibd-012-deep-extraction-round1.md)

## Linked Entities

- idiopathic IBD
- immunohistochemistry
- mucosal pathology
- immune imbalance
