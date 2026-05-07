---
id: src-ibd-007
type: source
title: "Pilot study: duodenal MDR1 and COX2 gene expression in cats with inflammatory bowel disease and low-grade alimentary lymphoma"
source_kind: paper
species: feline
diseases: [IBD]
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
tags: [ibd, lymphoma-boundary, molecular-expression]
links:
  doi: "10.1177/1098612X17730708"
  url: "https://journals.sagepub.com/doi/10.1177/1098612X17730708"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The abstract states that the study aimed to determine duodenal mRNA levels of MDR1 and COX2 in cats with IBD and low-grade alimentary lymphoma.
    - The abstract reports 20 cats with IBD, 9 with low-grade alimentary lymphoma, and 3 healthy controls.
    - The abstract reports lower MDR1 expression in cats with IBD and lymphoma than in healthy controls.
    - The abstract reports no difference in COX2 mRNA levels between groups.
  source_supported_conclusion:
    - This source belongs in the molecular side of the IBD-versus-lymphoma boundary branch.
    - The study supports MDR1 as a shared chronic-enteropathy disturbance signal rather than a clean IBD-versus-lymphoma separator.
  llm_inference:
    - This paper is best used as a bounded molecular-layer note, not as a lead diagnostic page.
---

# One-line Summary

Pilot molecular-expression paper that may help map the IBD-to-low-grade-lymphoma boundary without becoming a routine front-door test.

## Why It Matters For IBD

- adds gene-expression depth to the main disease-boundary branch
- may clarify whether COX2 and MDR1 are explanation markers, stratification markers, or practical diagnostics
- now serves as the first duodenal gene-expression anchor in the boundary branch

## Key Findings

- abstract includes 20 cats with IBD, 9 with low-grade alimentary lymphoma, and 3 healthy controls
- abstract reports lower MDR1 expression in both disease groups relative to controls
- abstract reports no significant difference in COX2 mRNA levels between IBD and lymphoma groups
- abstract reports no correlation between gene expression and clinical signs or histologic severity

## Molecular-Boundary Role

This pilot study belongs in the molecular side of the IBD-versus-low-grade-lymphoma boundary branch. Its main lesson is negative or boundary-setting: shared molecular disturbance is not the same thing as disease-class separation. The study included 20 cats with IBD, 9 with low-grade alimentary lymphoma, and 3 healthy controls. MDR1 expression was lower in both disease groups than in healthy cats, while COX2 mRNA did not differ usefully between groups.

For wiki reuse, this source should sit below biopsy-site strategy and imaging support. It can explain that duodenal gene-expression changes exist in chronic enteropathy, but it does not justify a practical MDR1/COX2 diagnostic shortcut. The absence of correlation between gene expression, clinical signs, histologic severity, or between genes further supports a cautious role.

The card should also be paired with `src-ibd-011`, which evaluates COX-2 immunoexpression at the tissue level. Together these two COX-related sources point in the same broad direction: COX biology may be part of intestinal response, but current seed-corpus evidence does not make COX2 a clean IBD-versus-lymphoma separator.

This is useful because it prevents the module from overvaluing any molecular-sounding marker. A marker can be mechanistically interesting, shared across disease states, and still clinically weak for classification. The endpoint handbook should therefore include molecular-expression evidence as subordinate boundary texture rather than as lead workup.

The future extraction question is whether MDR1 has treatment-response or drug-handling relevance that is separate from diagnosis. That possibility should be kept open, but not promoted without full-text support.

For now, the card's best use is negative discipline. It tells the module not to treat a molecular marker as useful just because it sounds precise. The observed MDR1 pattern is shared across IBD and lymphoma, and the COX2 mRNA result does not rescue the boundary.

## Limits / Caveats

- current card is abstract-checked, not full-text reviewed
- pilot molecular studies should not outrun biopsy and histopathology utility
- very small healthy-control group limits strong clinical translation
- do not convert shared MDR1 downregulation into a disease-class discriminator

## Open Follow-up Questions

- do these markers separate groups well enough to matter clinically?
- is the signal mechanistic, diagnostic, or both?
- does MDR1 have more relevance to drug response than to diagnosis?
- how does mRNA expression compare with COX-2 immunoexpression in `src-ibd-011`?

## Deep Extraction

- [src-ibd-007 deep extraction round 1](../../system/indexes/src-ibd-007-deep-extraction-round1.md)

## Linked Entities

- MDR1
- COX2
- low-grade alimentary lymphoma
