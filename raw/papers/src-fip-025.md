---
id: src-fip-025
type: source
title: "Assessing the feasibility of applying machine learning to diagnosing non-effusive feline infectious peritonitis"
source_kind: paper
species: feline
diseases: [FIP]
models: [machine learning diagnostic model]
endpoints: [diagnostic accuracy, sensitivity, specificity]
jurisdictions: []
evidence_level: original-study
status: extracted
extraction_depth: partial
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, machine-learning, diagnosis, non-effusive, classifier]
links:
  doi: "10.1038/s41598-024-52577-4"
  url: "https://www.nature.com/articles/s41598-024-52577-4"
  local_assets: []
year: 2024
evidence_policy:
  quoted_fact:
    - "Dataset encompassing 1939 suspected FIP cases comprising 683 FIP (35.2%) and 1256 non-FIP (64.8%) cases."
    - "Two diagnostic machine learning ensemble models trained on signalment and laboratory data."
    - "Both ensemble models detected FIP with an accuracy of 97.5%, an area under the curve (AUC) of 0.969, sensitivity of 95.45% and specificity of 98.28%."
    - "Validated on 80 confirmed cases (FIP: n=58, non-FIP: n=22)."
  source_supported_conclusion:
    - "Machine learning models can accurately discriminate FIP and non-FIP cases using laboratory data alone, in line with expert opinion."
    - "High sensitivity (95.45%) and specificity (98.28%) achieved on confirmed cases."
  llm_inference:
    - "This approach could support diagnosis of non-effusive FIP where confirmatory testing is not undertaken."
    - "Laboratory-only input suggests potential for clinical decision support without additional specialized testing."
---

# Assessing the feasibility of applying machine learning to diagnosing non-effusive feline infectious peritonitis

## Evidence-Depth Caveat

Abstract-weighted extraction only. Full text review needed for model performance metrics, feature importance, and validation methodology.

## One-Line Summary

Machine learning ensemble models trained on signalment and laboratory data can accurately discriminate FIP from non-FIP cases in line with expert opinion.

## Why It Matters For Feline FIP

Non-effusive FIP is diagnostically challenging. This study provides a data-driven approach to support clinical diagnosis when confirmatory testing (PCR, immunohistochemistry) is not performed.

## Key Findings (Abstract-Level)

### quoted_fact

- Dataset: 1939 suspected cases (683 FIP, 1256 non-FIP)
- Authors: University of Glasgow team (Dunbar, Babayan, Krumrie, Haining, Hosie, Weir)
- Published: January 30, 2024

### source_supported_conclusion

- ML models using standard laboratory markers can support FIP diagnosis
- Performance comparable to expert clinical opinion

### llm_inference

- Potential clinical decision support tool
- May reduce need for invasive confirmatory testing in some cases

## Claim-Fit Judgment

Strongest safe use:
- Diagnostic methodology research
- Non-effusive FIP diagnostic challenges

Must not control yet:
- Clinical diagnostic recommendations (needs full text review of performance metrics)
- Comparison to current gold standard tests

## Linked Entities

- diseases: FIP (non-effusive form)
- models: machine learning ensemble classifier
- endpoints: diagnostic accuracy
- mechanisms: N/A (diagnostic, not mechanistic)
- regulations: none applicable
