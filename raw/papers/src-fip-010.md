---
id: src-fip-010
type: source
title: "Limitations of using feline coronavirus spike protein gene mutations to diagnose feline infectious peritonitis"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2017
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, diagnosis, mutation]
links:
  doi: ""
  url: "https://link.springer.com/article/10.1186/s13567-017-0467-9"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly focuses on limitations of using spike-gene mutations for FIP diagnosis.
  source_supported_conclusion:
    - This source belongs at the center of the `diagnostic caution` branch.
    - This source should be used as the main limitation anchor inside the mutation-testing branch, not as a dismissal of the whole branch.
    - The source separates diagnostic use from mechanism-origin logic: the same mutation vocabulary does not carry the same claim class.
    - The safest use is comparative: pair it with mutation-utility and spread-boundary papers.
  llm_inference:
    - This paper should be read alongside mutation-origin and systemic-spread papers to prevent diagnostic overclaim.
    - This paper likely matters most when compared directly against mutation-utility papers such as `src-fip-022`.
  # V2 enhanced fields
  core_argument: "刺突蛋白基因突变检测用于 FIP 诊断存在根本性局限，不应作为确诊依据使用"
  implicit_premise: "假设「突变检测阳性」被临床医生解读为诊断性证据而非仅支持性证据；假设 FIP 病毒与肠道冠状病毒的突变边界是可检测且具有诊断意义的"
  evidence_boundary: "具体局限性（敏感性/特异性/样本类型/假阳性来源）需阅读全文才能确定；不否定突变检测的全部价值，仅限定其诊断角色上限"
  tension_with:
    - source_id: "src-fip-022"
      type: "qualifies"
      description: "src-fip-022 报告突变检测的诊断效用，本研究限定其适用边界"
---

# One-line Summary

Diagnostic-limits paper that keeps the FIP mutation branch from being overread as a definitive test pathway.

## Why It Matters For FIP

- creates the first explicit brake on naive mutation-based diagnosis
- likely prevents the mechanism branch from being misused as a clinical-certainty branch
- now serves as the first deep-extracted limitation anchor in the mutation-testing branch

## Key Findings

- title directly frames spike-mutation diagnosis as limited
- likely important for any future diagnostic-workup memo
- best reused as the caution anchor paired directly against mutation-utility papers

## Mutation-Diagnostics Role

This paper is one of the trust-boundary anchors in the whole FIP module. It exists to keep spike-mutation testing from being overread as a definitive pathway. That does not mean mutation testing is useless. It means utility and limitation need to be modeled together.

The branch placement is important. This source belongs in diagnosis and endpoint/workup architecture, not in the origin branch. Mutation-origin evidence explains disease emergence; mutation-detection evidence and mutation-limitation evidence determine whether a clinical sample can strengthen diagnosis. Those are different claim classes even when the biological vocabulary overlaps.

The safe compiled rule is: `src-fip-010` is the caution anchor for spike-mutation diagnosis. It should be read beside `src-fip-022` for positive utility and `src-fip-018` for the spread-not-FIP boundary. The paper should block certainty language but should not erase the whole mutation-testing branch.

For wiki reuse, this card should appear as the explicit `claim ceiling` beside every mutation-testing paragraph. Its role is not to say that spike-gene testing has no value. Its role is to make the model ask: what sample was tested, what exactly was detected, what comparator was used, and whether the result is being interpreted as supportive evidence or as disease definition. Until the full methods and performance details are recovered, those questions should remain visible instead of being hidden behind a simple positive/negative test framing.

This source also prevents a different category error. Mutation-origin papers and mutation-detection papers may share the same vocabulary, but they answer different questions. Origin papers help explain how virulence or tissue tropism may emerge from enteric coronavirus backgrounds. Diagnostic papers ask whether a clinical sample can strengthen a diagnosis in a sick cat. `src-fip-010` belongs to the second question and should not be used to rewrite the first.

The future diagnostic-workup page should therefore place this paper in a comparative row: `src-fip-022` for utility, `src-fip-018` for spread-versus-FIP boundary, and this source for diagnostic limitation. That row can teach the useful middle position: mutation testing may support a case, but it should not outrank clinical form, clinicopathology, sample context, and composite judgment.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- without reading the paper, the exact nature of the limitation is still unknown
- do not invent sensitivity, specificity, tissue, or sample-context metrics from the title alone
- limitation language should remain bounded caution, not broad anti-mutation rhetoric

## Open Follow-up Questions

- are the main problems sensitivity, specificity, tissue context, or interpretation?
- does this paper conflict with later mutation-detection utility studies or mainly bound them?
- how should the endpoint handbook rank mutation testing after pairing this source with `src-fip-018` and `src-fip-022`?

## Deep Extraction

- [src-fip-010 deep extraction round 1](../../system/indexes/src-fip-010-deep-extraction-round1.md)

## Linked Entities

- spike gene
- diagnosis
- mutation testing
