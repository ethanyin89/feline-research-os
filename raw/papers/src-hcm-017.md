---
id: src-hcm-017
type: source
title: "Evaluation of Potential Novel Biomarkers for Feline Hypertrophic Cardiomyopathy"
source_kind: paper
species: feline
diseases: [HCM]
models: []
endpoints: [novel-biomarkers]
jurisdictions: []
evidence_level: original-study
year: 2024
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [hcm, biomarkers, frontier]
links:
  doi: "10.1016/j.rvsc.2024.105430"
  url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4873577"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "The abstract states that NT-proBNP and cardiac troponin I have several limitations when used for HCM screening."
    - "The abstract identifies IL-18, IGFBP-2, PYGB, and WNT5A as candidate myocardial genes or circulating biomarker targets under evaluation."
    - "The abstract reports serum RT-qPCR and ELISA evaluation in eight healthy controls, eight cats with subclinical HCM, and six cats with HCM plus CHF."
    - "The abstract reports that serum IGFBP-2 RNA differed among groups and was highest in subclinical HCM."
    - "The abstract reports higher IL-18 and WNT5A gene expression in HCM plus CHF versus controls, and higher WNT5A in subclinical HCM versus controls."
    - "The abstract reports no observed group differences for PYGB."
  source_supported_conclusion:
    - Frontier biomarker work already exists in the HCM seed set and should be kept separate from routine markers.
    - The safest current use of this source is to widen the endpoint map without altering routine authority.
    - Novel-biomarker work should remain below structural confirmation and established marker use-case separation.
    - IGFBP-2, WNT5A, and IL-18 are the reusable frontier markers from this abstract; PYGB should be treated as negative or unsupported in this small dataset.
    - The source supports future large-scale evaluation rather than routine screening replacement.
  llm_inference:
    - This belongs in a frontier-marker branch, not in first-pass operational authority.
    - Endpoint pages should keep novelty and confidence ranked together, especially because this source is SSRN-hosted.
  # V2 enhanced fields
  study_design: "探索性三组研究，8 只健康对照 + 8 只亚临床 HCM + 6 只 HCM 伴 CHF，采用血清 RT-qPCR 和 ELISA"
  core_argument: "NT-proBNP 和 cTnI 用于猫 HCM 筛查存在局限，IGFBP-2、WNT5A 和 IL-18 可能是值得进一步评估的潜在新型生物标志物"
  implicit_premise: "假设心肌组织中差异表达的基因可以通过血清 RNA/蛋白检测反映并用于临床诊断；假设小样本探索性研究的信号方向在大规模验证中可重复"
  unexpected_finding: "PYGB 在三组间无显著差异，尽管它在之前的心肌组织研究中被识别为差异表达基因——这提示组织水平与循环水平的表达可能不一致"
  title_gap: "标题说新型生物标志物评估，但真正发现是负面结果的价值：PYGB 在组织中差异表达，但在循环中无法区分——这挑战了'组织信号=循环信号'的假设"
  evidence_boundary: "样本量极小（8 对照 + 8 亚临床 + 6 CHF），仅为探索性研究；不能确定这些标志物的临床诊断阈值、敏感性/特异性或预后价值；不能替代现有的 NT-proBNP/cTnI"
---

# One-line Summary

Novel-biomarker study that widens the frontier branch of HCM without yet defining the routine layer.

## Why It Matters For HCM

- prevents the biomarker branch from stopping at troponin and NT-proBNP
- may later support a frontier-versus-routine endpoint split

## Key Findings

- novel biomarker focus
- small three-group serum study: healthy controls, subclinical HCM, and HCM plus CHF
- IGFBP-2 RNA, WNT5A, and IL-18 signals are the main positive frontier findings
- PYGB did not separate groups in the abstract
- likely stratification or screening-augmentation depth rather than lead diagnosis

## Why This Study Matters

This paper matters because it stops the HCM biomarker branch from looking finished once troponin and NT-proBNP have been placed. A module that only carries routine markers becomes too clean and can miss where the frontier pressure is actually coming from.

At the same time, novelty is exactly where overclaim risk rises. This source is useful not because it should outrank established markers, but because it sharpens the hierarchy. It gives the endpoint branch a clearer frontier layer beneath routine structure-first confirmation and beneath better-established marker use cases.

The abstract gives enough structure to make that frontier layer concrete. The study compared serum RNA/protein measures across eight healthy controls, eight cats with subclinical HCM, and six cats with HCM plus CHF. It evaluated IL-18, IGFBP-2, PYGB, and WNT5A because prior work had identified those genes as differentially expressed in myocardium. The reusable result is split: IGFBP-2 RNA was highest in subclinical HCM, WNT5A and IL-18 signals were stronger in HCM plus CHF, WNT5A was also higher in subclinical HCM, and PYGB did not show group differences.

That is especially important here because the title itself is cautious. It says `potential novel biomarkers`, which already signals that exploratory maturity belongs in the interpretation. The paper is now peer-reviewed in Research in Veterinary Science, so the older SSRN caution should not be treated as a permanent dismissal. The correct caution is now sample size and validation maturity, not merely preprint status.

## Frontier-Marker Boundary

The strongest write-back rule from this source is:

- HCM endpoint architecture needs a frontier-biomarker layer
- novel markers should widen the hierarchy, not flatten it
- screening augmentation or stratification depth is a safer landing zone than diagnosis leadership
- novelty and confidence should remain explicitly linked in the page layer
- positive candidates and negative candidate signals should be separated so the module does not list all four as equally promising
- large-scale clinical validation is the next threshold before routine use-case promotion

That keeps the biomarker branch broad enough to be realistic and narrow enough to stay trustworthy.

## Limits / Caveats

- current card is abstract-weighted rather than full-text reviewed
- small sample size: eight controls, eight subclinical HCM cats, and six HCM plus CHF cats in the abstract
- this card currently supports frontier placement and trust-boundary caution more strongly than any particular marker ranking
- candidate biomarker differences are not yet clinical decision thresholds

## Open Follow-up Questions

- how robust are IGFBP-2, WNT5A, and IL-18 in larger clinical cohorts?
- are they framed as diagnosis, severity, or monitoring tools?
- how much of the paper is screening-oriented versus severity-oriented?
- does later peer-reviewed publication exist, and if so, does it shift confidence materially?

## Linked Entities

- HCM
- biomarkers
