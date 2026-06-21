---
id: src-fip-017
type: source
title: "The nucleoside analog GS-441524 strongly inhibits feline infectious peritonitis (FIP) virus in tissue culture and experimental cat infection studies"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2018
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, treatment, gs-441524, experimental]
links:
  doi: ""
  url: "https://www.sciencedirect.com/science/article/pii/S0378113518301603?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly reports strong inhibition of FIP virus by GS-441524 in tissue culture and experimental cat infection studies.
    - The abstract reports no toxicity in feline cells at concentrations as high as 100 uM and inhibition of viral replication at concentrations as low as 1 uM.
    - The abstract reports pharmacokinetic work establishing dosing that sustained effective blood levels for 24 hours in cats.
    - The abstract reports rapid reversal of disease signs and return to normality in 10/10 experimentally infected cats with no apparent toxicity.
  source_supported_conclusion:
    - This source belongs in the experimental antiviral-foundation branch below natural-disease treatment evidence.
    - This source provides mechanistic, pharmacokinetic, and experimental-disease support for the later natural-disease GS-441524 treatment branch.
  llm_inference:
    - This paper helps explain why the later natural-disease efficacy branch did not appear from nowhere.
    - This paper should stabilize the lower treatment layer without replacing the natural-disease baseline anchor.
  # V2 enhanced fields
  study_design: "原始研究，GS-441524 在组织培养和实验性猫感染研究中的抗病毒效力"
  core_argument: "GS-441524 有强大的临床前和实验性猫抗病毒基础——10/10 实验感染猫快速逆转疾病体征并恢复正常，无明显毒性"
  implicit_premise: "假设实验感染结果支持后续自然疾病研究的合理性但不能取代它；假设 PK 可行性需要单独验证"
  unexpected_finding: "100 uM 时无毒性，1 uM 时抑制病毒复制——安全窗口支持后续临床开发"
  title_gap: "标题说强效抑制 FIP 病毒，但真正价值是完整的临床前基础：10/10 实验感染猫快速恢复正常、100 倍安全窗口（100 uM 无毒/1 uM 有效）、24 小时 PK 可行性——解释了为什么后续自然疾病研究有合理基础"
  evidence_boundary: "实验基础，非自然疾病临床表现；不应合并为治愈率或现代方案细节"
---

# One-line Summary

Experimental GS-441524 paper that anchors the preclinical antiviral foundation under the modern treatment branch.

## Why It Matters For FIP

- gives the treatment branch mechanistic, pharmacokinetic, and experimental footing
- helps separate preclinical proof from natural-disease clinical proof
- now serves as the first deep-extracted experimental antiviral anchor in the FIP module

## Key Findings

- abstract reports no toxicity up to 100 uM and inhibition at concentrations as low as 1 uM
- naturally infected macrophage systems were included, not only standard cell culture
- abstract reports PK work supporting effective blood levels over 24 hours
- abstract reports rapid reversal of disease signs and return to normality in 10/10 experimentally infected cats
- best reused as a foundation layer rather than the main clinical anchor

## Experimental-Antiviral Role

This paper anchors the experimental foundation under the modern FIP antiviral branch. It is stronger than a simple cell-culture source because it includes tissue culture, naturally infected macrophage systems, pharmacokinetic work in cats, and experimental cat infection studies. But it is still a foundation layer, not the same thing as natural-disease clinical efficacy.

The source explains why later GS-441524 treatment studies were biologically and translationally plausible. The abstract reports no toxicity in feline cells at concentrations as high as 100 uM and inhibition of viral replication at concentrations as low as 1 uM. It also reports pharmacokinetic work establishing dosing capable of sustaining effective blood levels for 24 hours. Those details make the source important for mechanism-to-treatment translation, not just for retrospective treatment history.

The experimental-cat result is dramatic: rapid reversal of disease signs and return to normality in 10/10 experimentally infected cats with no apparent toxicity. The wiki should preserve that strength while keeping the hierarchy visible. Experimental infection and natural spontaneous disease are different evidence objects. `src-fip-017` should sit below natural-disease anchors such as `src-fip-016` and treatment-package data such as `src-fip-019`, and it should sit beside later durability evidence such as `src-fip-013`.

The safe compiled rule is: GS-441524 had a strong preclinical and experimental-cat antiviral foundation before later natural-disease clinical evidence developed. This source can support the lower treatment spine, PK plausibility, and experimental rescue branch. It should not be used alone to define clinical dose protocols, relapse expectations, neurologic dosing complexity, or real-world treatment outcomes.

This distinction is important for readers because `GS works` is too flat. A high-quality treatment page should teach the ladder: in vitro and macrophage inhibition, feline PK feasibility, experimental rescue, natural-disease efficacy, neurologic/ocular complexity, real-world regimen outcomes, and remission durability.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- experimental rescue and tissue-culture success are not the same as naturally occurring clinical treatment performance
- do not collapse experimental efficacy into natural-disease clinical success rates
- do not infer modern protocol details beyond the source's experimental and PK frame

## Open Follow-up Questions

- how directly did the experimental dosing logic map onto later natural-disease protocols?
- which parts of the treatment narrative should remain limited to experimental scope?
- what exact experimental infection model was used, and how comparable is it to field cases?
- which PK assumptions later survived into clinical treatment papers?

## Deep Extraction

- [src-fip-017 deep extraction round 1](../../system/indexes/src-fip-017-deep-extraction-round1.md)

## Linked Entities

- GS-441524
- antiviral treatment
- experimental infection
