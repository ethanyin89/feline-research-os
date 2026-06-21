---
id: src-ibd-016
type: source
title: "Expression of the Bcl-2 apoptotic marker in cats diagnosed with inflammatory bowel disease and gastrointestinal lymphoma"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2012
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, bcl2, lymphoma-boundary]
links:
  doi: "10.1177/1098612X12451404"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X12451404"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The abstract reports Bcl-2 immunolabeling in small-intestinal biopsy sections from 55 cats with histologic evidence of IBD or gastrointestinal lymphoma.
    - The abstract reports 8 cats with IBD and 47 cats with gastrointestinal lymphoma.
    - The abstract reports a significantly higher percentage of Bcl-2-positive cells in cats with GI lymphoma than in cats with IBD.
    - The abstract states that the overall degree of positive immunolabeling tended to be high in both groups.
  source_supported_conclusion:
    - This source belongs in the apoptotic-marker side of the IBD-versus-lymphoma boundary branch.
    - The study supports Bcl-2 as a lymphoma-leaning tissue marker, but not a clean standalone separator because expression remains high in both groups.
  llm_inference:
    - This paper is useful as a stronger tissue-marker boundary signal than COX-2, while still requiring bounded interpretation.
  # V2 enhanced fields
  study_design: "原始观察性研究，包含55只经组织学诊断为炎症性肠病（8只）或胃肠道淋巴瘤（47只）的猫，采用小肠活检组织的Bcl-2免疫标记检测"
  core_argument: "Bcl-2蛋白在胃肠道淋巴瘤组猫的免疫阳性细胞比例显著高于炎症性肠病组，但两组均表现出较高的Bcl-2表达，表明其并非能单独区分两种疾病的特异性标记"
  implicit_premise: "Bcl-2蛋白表达水平与细胞抗凋亡功能相关，且其免疫标记强度可以反映组织病理状态的差异"
  title_gap: "标题指出Bcl-2表达于IBD和胃肠淋巴瘤中，但真正发现是两者均有较高表达，且淋巴瘤组虽更高，却不能通过Bcl-2单独明确区分这两种疾病"
  evidence_boundary: "该研究未涉及Bcl-2表达与临床预后、治疗反应或其他分子标记物联合诊断的相关性，亦未扩展至其他猫种疾病病理状态的比较"
  unexpected_finding: "尽管预期淋巴瘤组Bcl-2表达明显高于IBD组，但IBD组同样显示整体较高的Bcl-2免疫阳性，提示抗凋亡机制可能在炎症状态中亦活跃"
---

# One-line Summary

Bcl-2 marker paper that likely deepens the tissue-level boundary between feline IBD and gastrointestinal lymphoma.

## Why It Matters For IBD

- adds another pathology-support angle to the core boundary problem
- may help show whether apoptotic signaling contributes practical discrimination
- now serves as the first Bcl-2 tissue-marker anchor in the boundary branch

## Key Findings

- abstract includes 55 biopsy specimens, with 8 IBD and 47 GI lymphoma cases
- abstract reports higher median Bcl-2 labeling in lymphoma than in IBD
- abstract also states that positive labeling tended to be high in both groups
- abstract suggests Bcl-2 overexpression may be relevant as a therapeutic target as well as a pathology marker

## Bcl-2 Boundary Role

This source provides a stronger tissue-marker boundary signal than the COX-2 expression papers, but it still has to stay bounded. The abstract reports Bcl-2 immunolabeling in small-intestinal biopsy sections from 55 cats with histologic evidence of IBD or gastrointestinal lymphoma: 8 cats with IBD and 47 cats with lymphoma. A significantly higher percentage of Bcl-2-positive cells was found in lymphoma than in IBD.

The important caveat is also in the abstract: the overall degree of positive immunolabeling tended to be high in both groups. That means Bcl-2 should be described as lymphoma-leaning, not as a standalone separator. It may add tissue-marker pressure when the workup already includes morphology, biopsy-site strategy, and pathology review, but it should not replace those layers.

For wiki reuse, this card belongs in the IBD-versus-lymphoma boundary memo as one of the more useful tissue-marker rows. It should be contrasted with `src-ibd-011`, where COX-2 behaves more like a shared response signal. Bcl-2 appears more class-informative, but overlap and group imbalance keep it below diagnostic certainty.

The source also opens a treatment-hypothesis note because the abstract suggests Bcl-2 overexpression may be therapeutically relevant. That should remain a hypothesis or translational note, not a current treatment recommendation for feline GI lymphoma or IBD.

The safe compiled statement is: Bcl-2 immunolabeling supports lymphoma-leaning pathology interpretation, but high labeling in both groups prevents clean solo classification.

This source should be placed higher than shared COX-2 markers but still below integrated pathology. It is one of the few tissue-marker cards in the current IBD set that leans toward lymphoma rather than merely separating disease from health or showing shared response. That makes it useful for a boundary table, provided the table explicitly marks overlap and group imbalance.

The IBD wiki should use Bcl-2 as an example of calibrated evidence. It is stronger than a marker that shows no between-group difference, but it is weaker than a complete diagnostic rule. That middle position is exactly where many pathology adjuncts live.

If future full-text work recovers thresholds, staining distribution, or associations with lymphoma subtype, this card may become more operational. Until then, it should remain a supportive pathology marker rather than a decision endpoint.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- marker-expression differences may not translate into stand-alone diagnostic authority
- lymphoma cases greatly outnumber IBD cases in this source
- do not convert therapeutic-target language into treatment guidance

## Open Follow-up Questions

- how strong is the Bcl-2 separation signal?
- does it add independent value beyond routine histopathology?
- are there practical thresholds, or only group-level differences?
- how does Bcl-2 interact with clonality, immunophenotype, and site-selection evidence?

## Deep Extraction

- [src-ibd-016 deep extraction round 1](../../system/indexes/src-ibd-016-deep-extraction-round1.md)

## Linked Entities

- Bcl-2
- gastrointestinal lymphoma
- pathology support
- apoptosis marker
