---
id: src-ibd-010
type: source
title: "Ultrasonographic Evaluation of the Muscularis Propria in Cats with Diffuse Small Intestinal Lymphoma or Inflammatory Bowel Disease"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2010
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, ultrasound, lymphoma-boundary]
links:
  doi: "10.1111/j.1939-1676.2009.0457.x"
  url: "https://academic.oup.com/jvim/article/24/2/289/8447309"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source evaluates ultrasonographic muscularis propria thickening and lymphadenopathy in cats with diffuse small intestinal lymphoma or IBD.
    - The abstract reports 142 cats with histologic diagnosis of normal small intestine, lymphoma, or IBD.
    - The abstract reports that cats with muscularis propria thickening were more likely to have lymphoma than normal small intestine cats and more likely to have lymphoma than IBD cats.
    - The abstract reports that lymphadenopathy was associated with both lymphoma and IBD compared with normal small intestine.
  source_supported_conclusion:
    - This source belongs in the imaging-support side of the IBD-versus-lymphoma workup branch.
    - The study supports muscularis thickening as a bounded lymphoma-leaning signal rather than a stand-alone diagnostic separator.
  llm_inference:
    - This was the correct next deep-extraction target because it turns the boundary branch into a multimodal workup story instead of a biopsy-only story.
  # V2 enhanced fields
  study_design: "回顾性队列研究，142 只经组织学确诊为正常小肠、弥漫性小肠淋巴瘤或炎症性肠病的猫，采用超声评估肌层增厚及淋巴结肿大"
  core_argument: "猫的弥漫性小肠淋巴瘤患者相比正常小肠和炎症性肠病患者更可能表现为肌层增厚，肌层增厚是倾向于淋巴瘤的超声信号，但不足以单独用于诊断区分"
  implicit_premise: "超声检查的肌层厚度和淋巴结状态可以反映猫肠道病理变化的类型和严重程度"
  title_gap: "标题说是超声评估肌层变化，但真正发现是肌层增厚虽倾向淋巴瘤却非单独诊断指标——提示诊断需结合更多信息"
  evidence_boundary: "该研究未评估肌层厚度是否能区分其他类型肠道肿瘤，亦未验证超声以外的诊断方法准确性和预后相关性"
  unexpected_finding: "淋巴结肿大不仅与淋巴瘤相关，也存在于炎症性肠病猫中，提示该超声表现非特异性"
---

# One-line Summary

Ultrasound boundary paper that likely helps position muscularis propria thickening as a useful workup signal without turning it into a definitive separator.

## Why It Matters For IBD

- gives the module a practical imaging branch
- likely helps define what ultrasound can and cannot do in the IBD-versus-lymphoma problem
- now serves as the first imaging-boundary anchor in the IBD module

## Key Findings

- abstract includes 142 cats with normal, IBD, or lymphoma histology
- abstract reports that muscularis propria thickening was more strongly associated with lymphoma than with IBD
- abstract reports that lymphadenopathy was associated with both lymphoma and IBD relative to normal intestine
- abstract conclusion states that older cats with muscularis layer thickening are more likely to have T-cell lymphoma than IBD

## Imaging-Boundary Role

This source gives the IBD module its first strong imaging-boundary anchor. It evaluates ultrasonographic muscularis propria thickening and lymphadenopathy in cats with normal small intestine, IBD, or diffuse small intestinal lymphoma. The point is not that ultrasound can replace tissue diagnosis. The point is that imaging can change the level and direction of lymphoma suspicion before or alongside biopsy planning.

The source is especially useful because it separates two ultrasound signals. Muscularis propria thickening leaned toward lymphoma: the abstract reports that cats with muscularis thickening were more likely to have lymphoma than normal cats and more likely to have lymphoma than IBD cats. The worksheet records an odds ratio of 18.8 for lymphoma versus IBD when muscularis propria thickening was present. Lymphadenopathy behaved differently: it was associated with both lymphoma and IBD compared with normal intestine, making it a weaker discriminator.

For wiki reuse, this card should sit beside `src-ibd-015`, not beneath it as a minor imaging note. Biopsy-site selection remains central, but ultrasound can pressure the workup toward stronger lymphoma concern and can help justify more complete sampling or stronger pathology review. The safe phrase is `lymphoma-leaning signal`, not `lymphoma diagnosis`.

This source also protects against a common compression error: treating all abnormal intestinal ultrasound findings as equivalent. Thickened muscularis and lymphadenopathy do different jobs. The endpoint handbook should preserve that difference, because it affects how the workup is explained to non-specialist readers.

The claim ceiling is firm. Older cats with muscularis thickening may be more likely to have T-cell lymphoma than IBD, but not every older cat with thickening has lymphoma. Histopathology, biopsy location, and clinical context remain necessary.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- ultrasound support should not outrun biopsy utility or histopathology
- do not treat muscularis thickening as standalone diagnostic proof
- lymphadenopathy should not be overread because it appears in both lymphoma and IBD contexts

## Open Follow-up Questions

- how discriminative is muscularis thickening in practice?
- is the value mainly suspicion-raising or truly boundary-separating?
- how should ultrasound findings alter duodenal versus ileal biopsy planning?
- what ultrasound thresholds or measurement methods were used in the full paper?

## Deep Extraction

- [src-ibd-010 deep extraction round 1](../../system/indexes/src-ibd-010-deep-extraction-round1.md)

## Linked Entities

- ultrasonography
- muscularis propria
- small intestinal lymphoma
