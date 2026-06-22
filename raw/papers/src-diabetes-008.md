---
id: src-diabetes-008
type: source
title: "Treatment of feline diabetes mellitus using an alpha-glucosidase inhibitor and a low-carbohydrate diet"
source_kind: paper
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [glycemic-control]
jurisdictions: []
evidence_level: original-study
year: 2003
status: deep_extracted
verification_status: deep_extracted
extraction_depth: full
decision_grade: no
language_qa_status: not_applicable
tags: [diabetes, treatment, diet, alpha-glucosidase-inhibitor]
links:
  doi: "10.1016/S1098-612X(03)00006-8"
  url: "https://doi.org/10.1016/S1098-612X(03)00006-8"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Study enrolled 18 client-owned diabetic cats."
    - "Cats received low-carbohydrate canned diet plus acarbose every 12 hours with meals."
    - "Acarbose is an alpha-glucosidase inhibitor that slows carbohydrate absorption."
    - "Most cats in the study also received concurrent insulin therapy."
    - "Responders were classified as cats in which insulin therapy was discontinued."
    - "Serum fructosamine decreased in both responder and non-responder groups."
    - "Blood glucose levels decreased over the 4-month study period in both groups."
  source_supported_conclusion:
    - "This 2003 JFMS study provides early evidence for alpha-glucosidase inhibitor use in feline diabetes."
    - "The 18-cat cohort and combination therapy design limits attribution of effects to acarbose alone."
    - "Responder classification (insulin discontinuation) is not equivalent to formal remission criteria."
    - "Fructosamine and glucose improvements occurred but cannot be attributed to any single intervention."
    - "The study supports adjunct therapy exploration but does not establish acarbose as first-line treatment."
  llm_inference:
    - "Acarbose belongs in the adjunct/historical treatment branch, not as a current first-line recommendation."
    - "Combination interventions require careful attribution; this study cannot isolate drug effect."
    - "Responder status should be distinguished from durable remission in diabetes module architecture."
  # V2 enhanced fields
  study_design: "前瞻性临床干预研究，纳入18只患有糖尿病的宠物猫，采用低碳水化合物罐装饮食联合每12小时餐时口服α-葡萄糖苷酶抑制剂阿卡波糖治疗方案"
  core_argument: "阿卡波糖的独立疗效无法确定——该联合治疗研究（n=18）表明部分猫可停用胰岛素，但效果难以归因于单一干预"
  implicit_premise: "阿卡波糖通过减缓碳水化合物的吸收能够有效改善糖尿病猫的血糖控制，从而使部分猫咪能够停止胰岛素治疗"
  title_gap: "标题强调α-葡萄糖苷酶抑制剂和低碳水化合物饮食的治疗作用，但实际研究发现其效果难以单独归因于阿卡波糖，且停用胰岛素并不等同于疾病完全缓解"
  evidence_boundary: "小样本前瞻性研究（n=18，2003年），联合干预设计无法分离阿卡波糖效果；停用胰岛素不等同于正式缓解标准"
  unexpected_finding: "尽管大多数猫接受胰岛素治疗，仍有部分猫通过联合治疗方案成功停止胰岛素使用"
---

# Treatment of feline diabetes mellitus using an alpha-glucosidase inhibitor and a low-carbohydrate diet

## One-Line Summary

Original treatment source combining alpha-glucosidase inhibition with low-carbohydrate diet.

## Why It Matters For Feline Diabetes

- gives the treatment branch an older non-insulin adjunct example
- should be compared against diet-only and insulin-based treatment anchors

## Key Findings

- first-pass metadata confirms this as a 2003 Journal of Feline Medicine and Surgery article
- the study involved 18 cats treated with an alpha-glucosidase inhibitor and low-carbohydrate canned diet
- most cats were also managed with insulin, so this is not a clean diet-only or drug-only experiment
- abstract-level outcome structure separates responders and nonresponders and reports insulin discontinuation more often among responders
- intervention design involves drug, diet, and insulin changes, so attribution needs care
- the source helps keep older adjunct approaches visible without making them current first-line treatment
- it is best read beside diet-study and remission-boundary cards

## Limits / Caveats

- full text not reviewed; this is an abstract-weighted extraction
- do not infer independent drug effect until study design and comparator are checked
- do not treat responder status as identical to durable remission
- do not compare acarbose directly with SGLT2 or insulin protocols without modern comparator evidence

## Adjunct Treatment Logic

What can be promoted:

- acarbose plus low-carbohydrate diet was tested in client-owned cats
- most cats also received insulin
- glucose and fructosamine improved across response groups
- responder classification centered on insulin discontinuation

What should be held:

- independent acarbose effect
- first-line protocol status
- durable remission claims
- comparative superiority over diet-only, insulin, or SGLT2 branches

## Write-Back Implications

- [translation brief](../../topics/diabetes/translation-brief.md) should keep acarbose as an adjunct/historical branch.
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md) should separate fructosamine/glucose change from insulin discontinuation and remission.
- [synthesis index](../../topics/diabetes/synthesis-index.md) should preserve attribution caution.

## Full-Text Target If Needed

Extract comparator design, dose, insulin-adjustment rules, adverse effects, adherence, and response definitions before using this source for treatment hierarchy.

## Current Safe Role

Use this source as an older adjunct-treatment example. It is useful because it shows that diet, adjunct drug, and insulin adjustment can be bundled in practice, which makes attribution hard. It should sit below clearer diet-study, insulin, SGLT2, and remission-boundary owners when ranking evidence strength.

This card is most helpful when the translation page needs to show why combination interventions require caution. A positive responder pattern does not automatically identify the active ingredient when acarbose, diet composition, and insulin changes move together.
That makes it a branch-separation source rather than a recommendation source for current outputs or practical treatment hierarchy decisions now safely.

## Open Follow-Up Questions

- what comparator or baseline design was used?
- what glycemic endpoints were measured?
- were remission or adverse events reported?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: glycemic control
- mechanisms: carbohydrate absorption
- regulations:
