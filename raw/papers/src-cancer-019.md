---
id: src-cancer-019
type: source
title: "Feline mammary basal-like adenocarcinomas: a potential model for human triple-negative breast cancer (TNBC) with basal-like subtype"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: [immunohistochemistry, BRCA, comparative-oncology]
jurisdictions: []
evidence_level: original-study
year: 2013
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [cancer, mammary, basal-like, adenocarcinomas, potential, model, human, triple-negative]
links:
  doi: "10.1186/1471-2407-13-403"
  url: "https://doi.org/10.1186/1471-2407-13-403"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Crossref metadata resolves this DOI and reports abstract availability for source scope checking."
    - "Crossref container: BMC Cancer; year: 2013."
    - "The accessible BMC Cancer / Springer Nature article page was checked in the 2026-05-30 deep extraction pass."
  source_supported_conclusion:
    - "This source supports a mammary carcinoma / TNBC-like comparative oncology branch."
    - "It can define marker and model boundaries, but it should not be used as treatment guidance."
  llm_inference:
    - "Small archival design and partial BRCA amplification limit broad prevalence, prognosis, and mechanism claims."
  # V2 enhanced fields
  study_design: "原始研究，24 例存档猫乳腺腺癌的 IHC 和 BRCA 基因检测"
  core_argument: "猫乳腺腺癌中 14/24 为三阴性，其中 11/14 为基底样亚型——FMC 可作为人类 TNBC 基底样亚型的潜在比较模型"
  implicit_premise: "假设 IHC 标志物（ER、PR、HER2、CK5/6、EGFR）定义的表型与人类 TNBC 分子亚型具有生物学等价性"
  unexpected_finding: "BRCA1/BRCA2 在测试的扩增子集中未发现肿瘤特异性异常——这挑战了人类 TNBC 中 BRCA 驱动假设对猫的直接转化"
  title_gap: "标题说 FMC 基底样腺癌可能是人类 TNBC 的模型，但真正发现是 BRCA 阴性：小样本测试中未发现 BRCA 异常——需谨慎将人类 TNBC 的 BRCA 驱动假设转化到猫"
  evidence_boundary: "24 例存档样本是小型研究；BRCA 阴性发现不能排除更广泛的 BRCA 相关性"
---

# Feline mammary basal-like adenocarcinomas: a potential model for human triple-negative breast cancer (TNBC) with basal-like subtype

## Deep Extraction, 2026-05-30

Worksheet: [src-cancer-019 deep extraction](../../system/indexes/src-cancer-019-deep-extraction-round1.md)

This source was promoted from abstract-weighted triage to deep-extracted after manual full-text review of the accessible BMC Cancer / Springer Nature HTML article page.

Safe promoted role:

- mammary carcinoma comparative oncology branch anchor
- TNBC-like / basal-like phenotype boundary source
- IHC marker framework source for ER, PR, HER2, CK5/6, and EGFR
- BRCA-boundary source, because the tested subset did not show tumor-specific BRCA1/BRCA2 abnormalities

Do not use this source as:

- treatment guidance
- broad prevalence authority
- prognosis authority for all feline mammary carcinoma
- proof that feline TNBC-like mammary tumors are BRCA-driven

## Source Check, 2026-05-30

Crossref metadata was checked as a repeatable second-pass intake step before deep extraction.

- DOI metadata resolved: yes
- Container: BMC Cancer
- Year: 2013
- Abstract available in Crossref: yes
- Full text manually verified: yes, open HTML article page
- Extraction status: deep-extracted

## One-Line Summary

Deep-extracted mammary carcinoma source supporting a TNBC-like / basal-like comparative oncology branch, with explicit BRCA and treatment-translation boundaries.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow. Full-text review confirms that its strongest role is mammary carcinoma branch architecture rather than owner-facing treatment advice.

The safe current use is controlled branch evidence:

- define a feline mammary carcinoma / TNBC-like model branch
- keep basal-like and triple-negative definitions tied to IHC markers
- prevent human TNBC / BRCA assumptions from being overtranslated into cats
- keep treatment, prognosis, and prevalence claims behind stronger clinical or registry sources

## Key Findings

### quoted_fact

- The intake sheet lists this title: Feline mammary basal-like adenocarcinomas: a potential model for human triple-negative breast cancer (TNBC) with basal-like subtype.
- The intake sheet locator is: 10.1186/1471-2407-13-403.
- The study evaluated 24 feline mammary adenocarcinomas from a diagnostic archive.
- The marker panel included ER, PR, HER2, CK5/6, and EGFR.
- The study reported 14/24 tumors as triple negative and 11/14 triple-negative tumors as basal-like.
- BRCA1/BRCA2 genetic testing did not find tumor-specific abnormalities in the amplified subset.

### source_supported_conclusion

- This source supports early separation of mammary carcinoma from the general feline cancer shell.
- It supports a TNBC-like / basal-like comparative oncology branch with marker-defined boundaries.
- It supports caution around BRCA translation: negative findings in a small amplified subset do not prove or exclude broader BRCA relevance.

### llm_inference

- Use this source with `src-cancer-004` to build a mammary carcinoma mechanism/model branch before adding clinical management claims.
- Numeric results should remain study-bound until checked against registry, review, or larger clinical-study sources.

## Claim-Fit Judgment

Strongest safe use:

- mammary carcinoma branch architecture
- TNBC-like / basal-like marker framework
- comparative oncology model boundaries
- BRCA non-translation caution

Must not control yet:

- reader-facing medical advice
- treatment ranking
- broad prevalence
- prognosis estimates outside this archival series
- guideline-like recommendations
- BRCA mechanism closure

## Image Asset TODO

- figures to capture: IHC phenotype figures and BRCA/LOH figure may be useful if a mammary carcinoma branch page is built
- why these matter: marker images can explain branch definitions, but only after asset permissions and labels are checked

## Open Follow-Up Questions

- Which larger registry or review sources should triangulate the 24-case numbers?
- Should mammary carcinoma become the first split-out cancer branch page?
- Which owner-facing claims require separate clinical guideline or treatment outcome sources?
- Are article figures worth capturing under the asset workflow?

## Linked Entities

- diseases: cancer
- models:
- endpoints: immunohistochemistry, BRCA, comparative oncology
- mechanisms: ER/PR/HER2 status, CK5/6, EGFR, basal-like phenotype, TNBC-like phenotype
- regulations:
