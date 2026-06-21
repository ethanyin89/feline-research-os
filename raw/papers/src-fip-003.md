---
id: src-fip-003
type: source
title: "A review of feline infectious peritonitis virus infection"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, review, mechanism, translation]
links:
  doi: ""
  url: "https://veterinaryworld.org/Vol.17/November-2024/1.php"
  local_assets:
    - raw/images/fip/src-fip-003-figure-2-ascites-radiograph-kidney-ihc-panel.png
evidence_policy:
  quoted_fact:
    - The source is a 2024 review article focused on FIP virus infection.
    - The abstract states that FIP has non-specific laboratory changes and clinical signs and that supportive diagnosis is needed because there are no specific symptoms.
    - The abstract states that feline coronaviruses can be classified into two serotypes and two pathotypes, including feline enteric coronavirus and FIP virus.
  source_supported_conclusion:
    - This source is the best current broad modern review anchor in the FIP seed set.
    - The review supports treating diagnostic uncertainty as a central part of the FIP map, not as a minor caveat.
    - The review should sit above narrow mutation, assay, and antiviral papers because it preserves whole-disease branch architecture.
    - The source supports a central distinction between coronavirus exposure/background and FIP disease emergence.
  llm_inference:
    - This is the best candidate for the first FIP deep extraction pass.
  # V2 enhanced fields
  core_argument: "FIP 的临床表现和实验室检查均为非特异性，诊断必须基于多维度支持性证据的综合判断，而非任何单一「金标准」检测"
  implicit_premise: "假设综述能够准确整合不同时代、不同样本来源、不同研究设计的证据；假设 GS-441524 时代的治疗转型不改变诊断框架的基本逻辑"
  evidence_boundary: "综述性质无法提供原始诊断性能数据；不能用于评估具体检测方法的敏感性/特异性；治疗方案的证据等级需回溯原始研究"
---

# One-line Summary

Modern broad FIP review that should anchor the first full compile of the disease module.

## Why It Matters For FIP

- likely provides the cleanest recent overview before we split into mutation, diagnosis, and treatment branches
- should be the main overview source for early synthesis work
- now has a round-1 deep extraction worksheet to stabilize the first-pass FIP branch architecture

## Key Findings

- published in November 2024, making it a useful post-GS-era framing source
- abstract explicitly emphasizes non-specific clinical and laboratory findings
- abstract explicitly distinguishes feline enteric coronavirus from FIP virus pathotypes
- abstract supports the need for supportive, multi-input diagnosis rather than one definitive symptom pattern
- strongest current role is whole-module framing before narrower mutation, assay, and treatment sources are compressed

## Disease-Architecture Contribution

This review matters because it holds together three truths that can easily drift apart. First, FIP remains diagnostically difficult: clinical signs and routine laboratory changes are non-specific, so recognition has to remain composite and support-based. Second, feline coronavirus background and FIP disease are not the same layer; the review distinguishes serotypes and pathotypes and keeps feline enteric coronavirus separate from FIP virus disease logic. Third, the modern treatment era does not erase either of those facts. A post-GS-era module still needs diagnostic humility.

That makes this source a cross-branch anchor rather than a single mechanism citation. It should stabilize vocabulary for exposure, pathotype, disease emergence, recognition, and treatment context before the module narrows into mutation testing or antiviral protocols. If this paper is overfiled under `mechanism` only, the compiled FIP module risks fragmenting too early.

The safest reusable compression is: FIP is a systems problem involving coronavirus ecology, host/disease emergence, non-specific recognition, and modern antiviral transformation. The review supports that architecture, but it should not be used alone to rank diagnostic assays or treatment protocols.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- broad reviews can blur evidence strength across older and newer treatment eras
- do not use this broad review as substitute evidence for primary-treatment efficacy, mutation-diagnostic performance, or assay sensitivity/specificity
- candidate image references remain unverified until figure/table labels are checked against the source

## Image Asset TODO

- verified assets:
  - `raw/images/fip/src-fip-003-figure-2-ascites-radiograph-kidney-ihc-panel.png` — article PDF Figure-2; ascites ultrasound, abdominal-effusion radiograph, kidney necrotic foci / lymph-node enlargement gross panels, interstitial nephritis histology, and kidney macrophage immunohistochemistry panel
- figures to capture:
  - broad overview or mechanism summary figure
  - diagnostic support or workup summary table
  - any treatment-era comparison figure that separates old from current antiviral logic
- why these matter:
  - this is the broadest modern FIP review anchor and should eventually carry the visual backbone for the disease shell
  - diagnosis in FIP is currently described as multi-input and non-specific, so a review summary table would preserve that structure better than prose alone
  - if the review contains a treatment-era comparison graphic, it would help keep overview pages from flattening historical and current antiviral logic

## Open Follow-up Questions

- how strongly does it separate diagnosis from treatment transformation?
- does it clearly bound mutation-based diagnosis claims?
- how much of the review is modern treatment synthesis versus broad background summary?

## Deep Extraction

- [src-fip-003 deep extraction round 1](../../system/indexes/src-fip-003-deep-extraction-round1.md)

## Linked Entities

- FIP
- feline coronavirus
- GS-441524
- diagnosis
