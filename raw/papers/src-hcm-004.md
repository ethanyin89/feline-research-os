---
id: src-hcm-004
type: source
title: "Genetics of feline hypertrophic cardiomyopathy"
source_kind: paper
species: feline
diseases: [HCM]
models: []
endpoints: []
jurisdictions: []
evidence_level: review
year: 2020
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [hcm, genetics, review]
links:
  doi: "10.1111/cge.13743"
  url: "https://onlinelibrary.wiley.com/doi/10.1111/cge.13743"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The abstract describes HCM as an abnormal increase in myocardial mass that affects cardiac structure and function.
    - The abstract identifies HCM as the most common inherited cardiovascular disease in humans and the most common cardiovascular disease in cats.
    - The abstract states that feline HCM phenotype is very similar to human HCM, while feline disease develops on a shorter time frame.
    - The abstract says feline genetic studies have been limited to fragment analysis of two sarcomeric genes, with two MYBPC3 variants and one MYH7 variant identified.
    - The abstract warns that high prevalence of reported variants in unaffected cats hinders pathogenicity assumptions in heterozygotes.
  source_supported_conclusion:
    - Genetics is already a first-class branch in the HCM seed corpus; this 2020 dedicated genetics review is its primary anchor.
    - This source should anchor the genotype branch before severity and phenotype language are overcompressed.
    - The current evidence available in-tool supports architectural promotion of a genotype branch, but not a confident variant-level hierarchy.
    - This source is still important because it prevents the HCM module from collapsing into phenotype-only language.
    - This card can support the existence of a dedicated genetics branch, human-cat genotype/phenotype analogy, and a strong caution against overconfident variant-level interpretation.
    - The source supports a bounded genetics frame: feline HCM is plausibly inherited and sarcomere-linked in some settings, but known variants do not settle broad disease causation or prognosis.
  llm_inference:
    - This is one of the strongest early deep-extraction targets after the broad review anchor.
    - The safer current compiled move is `keep genetics first-class, keep variant compression bounded`.
  # V2 enhanced fields
  study_design: "综述，专门讨论猫肥厚型心肌病的遗传学（2020 年）"
  core_argument: "猫 HCM 在表型上与人类 HCM 高度相似，但猫的遗传研究局限于少数肌节基因——已知变异在健康猫中的高流行率阻碍了致病性判定"
  implicit_premise: "假设人-猫表型相似性可以支持比较病理生理学；假设已知变异的流行率问题是系统性的而非偶然"
  unexpected_finding: "报告的变异在未受影响猫中的高流行率——这阻止了简单的「变异阳性=疾病」诊断逻辑"
  title_gap: "标题说遗传学，但真正发现是基因检测的局限：已知变异在健康猫中流行率也高——'变异阳性≠疾病'阻止了简单的遗传筛查逻辑"
  evidence_boundary: "不提供变异级别的致病性层级；品种相关变异解读应保持谨慎；不能用于临床遗传咨询的具体建议"
---

# One-line Summary

Genetics review that should anchor the genotype branch of the HCM module.

## Why It Matters For HCM

- keeps the module from flattening HCM into phenotype alone
- likely shapes genotype-severity and breed-associated interpretation

## Key Findings

- dedicated genetics anchor
- feline HCM phenotype is close enough to human HCM to matter for comparative pathophysiology
- known feline genetic studies are much narrower than the human HCM genetics literature
- reported feline variants include MYBPC3 and MYH7 signals, but variant pathogenicity is constrained by prevalence in unaffected cats
- best first-pass genetics overview in the current seed set

## Why This Review Matters

This source matters because HCM becomes unstable very quickly if genetics is treated as either everything or nothing.

At one extreme, the module can collapse into phenotype-only language and lose genotype pressure entirely. At the other, it can pretend that one or two familiar breed-associated variants already explain the whole disease. This review is useful because it gives the genetics branch a legitimate anchor before either error takes over.

The abstract makes the source more than a title-level anchor. It gives the module three reusable facts. First, feline HCM is framed as a close phenotypic analog of human HCM. Second, cats differ from humans in the depth of available genetic discovery: humans have thousands of implicated variants, while feline studies remain concentrated around a small number of sarcomeric candidates. Third, the known feline variant story is not clean enough to turn into a simple pathogenicity hierarchy, because variants reported in cats can also appear at high prevalence in unaffected cats.

That combination is exactly what the HCM module needs. Genetics should not be hidden behind echocardiographic phenotype, but it also should not become a deterministic mutation story. The safest compression is not "test one variant and rank the cat"; it is "keep genotype pressure visible, especially in breed and family contexts, while treating variant interpretation as bounded and incomplete."

This source also helps explain why the human-cat comparison is useful but dangerous. Similar phenotype, shared sarcomeric logic, and overlapping complications justify comparative framing. The shorter feline disease time frame and much smaller feline variant literature prevent direct transfer of human genetic certainty into feline clinical guidance.

## Current Safe Promotion

The safest promotion from this source is:

- genetics remains a first-class HCM branch
- genotype pressure should stay visible before phenotype and severity are overcompressed
- breed and variant language should remain bounded until fuller extraction is available
- known feline genetic findings belong in a `candidate / breed-associated / interpretation-limited` frame rather than a broad deterministic frame
- human-cat analogy is useful for pathophysiology and model thinking, but not for importing human variant hierarchy wholesale

That makes this card `architecturally important` even though it is not yet a full-depth genetics synthesis source.

## Limits / Caveats

- abstract-weighted rather than full-text compressed
- does not provide enough extracted detail here for variant-by-variant tables, breed penetrance estimates, or clinical testing recommendations
- the card supports branch architecture and overclaim prevention more strongly than operational genetic counseling
- later 2025 multiomics evidence may sharpen the genetics story, but it should be handled as a separate source rather than silently merged into this 2020 review

## Open Follow-up Questions

- which variants or breed signals are operationally important?
- how strongly does the review connect genetics to severity or prognosis?
- does it mainly stabilize known breed variants, or also discuss broader polygenic uncertainty?
- does the paper support a narrow mutation story or a broader genotype-risk framing across feline populations?
- how should the 2020 review be reconciled with newer large-cohort sequencing and transcriptomics work?

## Linked Entities

- HCM
- genetics
