---
id: src-ibd-011
type: source
title: "Cyclooxygenase-2 immunoexpression in intestinal epithelium and lamina propria of cats with inflammatory bowel disease and low grade alimentary lymphoma"
source_kind: paper
species: feline
diseases: [IBD]
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
tags: [ibd, coX2, lymphoma-boundary]
links:
  doi: "10.1186/s12917-018-1486-0"
  url: "https://link.springer.com/article/10.1186/s12917-018-1486-0"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The abstract states that the study evaluated COX-2 immunoexpression in intestinal epithelium and lamina propria of cats with IBD and low-grade alimentary lymphoma.
    - The abstract reports 11 cats with IBD and 9 cats with low-grade alimentary lymphoma after exclusions.
    - The abstract reports significantly higher epithelial COX-2 intensity in both IBD and lymphoma compared with control cats, but not between the two sick groups.
    - The abstract reports no difference in lamina propria COX-2 expression between groups.
  source_supported_conclusion:
    - This source belongs in the tissue-marker side of the IBD-versus-lymphoma boundary branch.
    - The study supports epithelial COX-2 as a shared inflammatory or reparative signal rather than a clean separator between IBD and lymphoma.
  llm_inference:
    - This paper is best modeled as a shared tissue-response marker page, not as a decisive boundary marker.
---

# One-line Summary

Tissue-expression paper that may sharpen the COX2 side of the IBD-versus-low-grade-lymphoma boundary problem.

## Why It Matters For IBD

- adds immunohistochemical depth to the main diagnostic-boundary branch
- may connect inflammatory signaling with pathology interpretation
- now serves as the first COX-2 tissue-expression anchor in the boundary branch

## Key Findings

- abstract includes 11 cats with IBD and 9 cats with low-grade alimentary lymphoma after exclusions
- abstract reports increased epithelial COX-2 intensity in both IBD and lymphoma relative to controls
- abstract reports no clear epithelial COX-2 difference between the IBD and lymphoma groups
- abstract reports no correlation between COX-2 expression and FCEAI or histologic alterations

## COX-2 Tissue-Marker Role

This source gives the IBD module a tissue-expression counterpart to the MDR1/COX2 mRNA pilot study. It evaluated COX-2 immunoexpression in intestinal epithelium and lamina propria of cats with IBD and low-grade alimentary lymphoma. The result is mainly boundary-setting: epithelial COX-2 intensity was higher in both disease groups than in controls, but not clearly different between IBD and lymphoma.

The branch placement should be precise. COX-2 immunoexpression can be part of shared intestinal response biology, but it is not a clean separator in the current evidence. No difference was found for lamina propria COX-2 expression, and there were no correlations with FCEAI or histologic alterations. That keeps the source below practical workup leaders such as biopsy-site strategy and ultrasound muscularis propria findings.

For wiki reuse, this card should help explain why tissue markers can be biologically meaningful without being diagnostically decisive. It belongs in the lymphoma-boundary memo as a `shared response marker` row. It should also be linked to the endpoint handbook, where it can illustrate why marker class matters: expression intensity is not the same as disease identity, severity, or treatment response.

The source is also useful in combination with `src-ibd-007`. If both mRNA and immunoexpression work fail to cleanly separate IBD from low-grade lymphoma, the module should not let COX2 language drift into clinical decisiveness. The correct compiled statement is that COX-2 appears more useful for explanatory tissue-response context than for current diagnostic discrimination.

Future full-text work should look for staining-scoring details, tissue location definitions, and whether any subgroup analyses suggest narrower reuse. Until then, this remains a support-boundary source.

That support-boundary role is still valuable: it stops the module from promising more than current tissue-marker evidence supports.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- expression differences are not automatically clinically decisive
- do not treat epithelial COX-2 intensity as a validated disease-class marker
- no FCEAI or histologic correlation should stay attached to severity claims

## Open Follow-up Questions

- does COX2 meaningfully separate IBD from lymphoma?
- is the signal stronger in epithelium, lamina propria, or both?
- does full-text scoring reveal any subgroup signal hidden by the abstract?
- should COX-2 be framed mainly as biology, diagnosis support, or therapeutic hypothesis?

## Deep Extraction

- [src-ibd-011 deep extraction round 1](../../system/indexes/src-ibd-011-deep-extraction-round1.md)

## Linked Entities

- COX2
- immunohistochemistry
- alimentary lymphoma
