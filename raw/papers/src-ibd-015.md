---
id: src-ibd-015
type: source
title: "Utility of Endoscopic Biopsies of the Duodenum and Ileum for Diagnosis of Inflammatory Bowel Disease and Small Cell Lymphoma in Cats"
source_kind: paper
species: feline
diseases: [IBD]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2011
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [ibd, biopsy, lymphoma-boundary]
links:
  doi: "10.1111/j.1939-1676.2011.00831.x"
  url: "https://academic.oup.com/jvim/article/25/6/1253/8451361"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source evaluates agreement between endoscopic duodenal and ileal biopsies in cats with IBD and small-cell lymphoma.
    - The abstract reports 70 client-owned cats with gastrointestinal disease and adequate duodenal and ileal tissue biopsies.
    - The abstract reports poor agreement between duodenal and ileal diagnoses with kappa = 0.23.
    - The abstract reports that among 18 cats diagnosed with small-cell lymphoma, 7 were diagnosed only in duodenum, 8 only in ileum, and 3 in both sites.
  source_supported_conclusion:
    - This source anchors the practical diagnostic-boundary branch of the module.
    - The study supports modeling ileal biopsy as a branch-critical addition rather than an optional afterthought in some cats.
  llm_inference:
    - This was the correct next IBD deep extraction target because it materially changes how the workup branch should be compressed.
---

# One-line Summary

Biopsy-utility paper that likely becomes the central workup anchor for separating feline IBD from small-cell lymphoma.

## Why It Matters For IBD

- sits directly at the main diagnostic compression problem
- likely shapes how much confidence to place in duodenal and ileal endoscopic sampling
- now serves as the first major biopsy-site selection anchor in the IBD module

## Key Findings

- abstract included 70 cats with gastrointestinal disease and adequate paired duodenal and ileal endoscopic biopsies
- abstract states there was poor agreement between duodenal and ileal diagnosis for IBD and small-cell lymphoma
- abstract reports that many small-cell lymphoma diagnoses were site-specific rather than duplicated across both sites
- abstract conclusion supports the existence of a cat population in which diagnosis of small-cell lymphoma can be found only by evaluating ileal biopsies

## Biopsy-Site Boundary Role

This is one of the most important operational sources in the IBD module because it turns the IBD-versus-small-cell-lymphoma problem into a sampling problem, not only an interpretation problem. The study evaluated paired duodenal and ileal endoscopic biopsies in 70 client-owned cats with gastrointestinal disease. Poor agreement between sites, with kappa = 0.23, means the workup cannot safely pretend that one intestinal site represents the whole boundary.

The small-cell lymphoma numbers are the key reusable facts. Among 18 cats diagnosed with small-cell lymphoma, 7 were diagnosed only in duodenum, 8 only in ileum, and 3 in both sites. That pattern supports a strong practical rule: ileal biopsy can be branch-critical when lymphoma exclusion is a real goal. It should not be reduced to an optional extra in every compressed workup diagram.

For wiki architecture, this source belongs above most biomarker and imaging-support papers. Ultrasound, molecular expression, metabolomics, microbiota, and vitamin D findings can pressure suspicion, but tissue-site selection remains central when the question is whether the cat has IBD or small-cell lymphoma. The card should be linked from risk/recognition, endpoint handbook, and diagnostic-boundary memos.

The claim ceiling should be visible. The source does not prove every cat needs ileal biopsy, and it does not eliminate pathologist variability or residual gray zones once tissue is obtained. It does prove that diagnostic completeness and procedural convenience are not the same thing. A duodenal-only path can be easier, but this paper shows why it can be incomplete for lymphoma detection.

The future table asset is high priority because the duodenum-versus-ileum pattern is easy to misremember in prose. The site-specific detection summary should become a stable visual if verified.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- biopsy utility is not the same thing as perfect diagnostic resolution
- retrospective design and single-pathologist review limit certainty even while the site-selection signal remains important
- do not imply paired biopsies remove all IBD-versus-lymphoma ambiguity
- do not make ileal biopsy universal without clinical-context framing

## Image Asset TODO

- figures to capture:
  - duodenal-versus-ileal diagnostic agreement table
  - site-specific lymphoma detection summary figure or table
  - any biopsy-site workflow diagram
- why these matter:
  - this paper sits at the center of the IBD-versus-small-cell-lymphoma boundary and should preserve the site-selection logic directly
  - the numerical disagreement signal is much safer to carry as a table than as compressed prose
  - if a workflow figure exists, it would help keep ileal biopsy as a branch-critical addition rather than an afterthought

## Open Follow-up Questions

- how much incremental value comes from ileal biopsy beyond duodenal biopsy?
- what diagnostic misses remain even with both sites?
- which clinical features should trigger ileal sampling as a stronger requirement?
- how should this source be paired with ultrasound and molecular-boundary papers in a practical algorithm?

## Deep Extraction

- [src-ibd-015 deep extraction round 1](../../system/indexes/src-ibd-015-deep-extraction-round1.md)

## Linked Entities

- endoscopic biopsy
- duodenum
- ileum
