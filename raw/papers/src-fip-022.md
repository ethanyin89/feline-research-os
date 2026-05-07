---
id: src-fip-022
type: source
title: "Detection of feline coronavirus spike gene mutations as a tool to diagnose feline infectious peritonitis"
source_kind: paper
species: feline
diseases: [FIP]
models: []
endpoints: []
jurisdictions: []
evidence_level: original-study
year: 2015
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, diagnosis, mutation]
links:
  doi: ""
  url: "https://journals.sagepub.com/doi/10.1177/1098612X15623824"
  local_assets: []
evidence_policy:
  quoted_fact:
    - The source explicitly studies detection of feline coronavirus spike-gene mutations as a diagnostic tool for FIP.
  source_supported_conclusion:
    - This source belongs in the mutation-based diagnostic branch, not in the primary mechanism-origin branch.
    - This source is best used as the positive utility side of the mutation-diagnostics branch, but only in bounded comparison with the limitation papers.
    - The source prevents the mutation branch from becoming only cautionary; bounded diagnostic support is still real.
    - It should be used as a workup-strengthening source, not as a standalone definitive test source.
  llm_inference:
    - This paper should be read directly beside `src-fip-010` to keep utility and limitation claims from drifting apart.
---

# One-line Summary

Mutation-detection paper that likely represents the `tool` side of the mutation-diagnostics branch.

## Why It Matters For FIP

- provides the positive/utility side of mutation-based diagnostic reasoning
- helps prevent the diagnostic branch from being represented only by cautionary papers

## Key Findings

- title frames spike-gene mutation detection as a diagnostic tool
- likely important for balancing later limitation-focused work

## Mutation-Utility Role

This source represents the positive side of the mutation-diagnostics branch. Without it, the FIP module would be biased toward origin theory and caution papers and might understate why mutation testing became clinically interesting in the first place.

The value is bounded utility. The title frames spike-gene mutation detection as a tool to diagnose FIP, so the paper belongs in diagnostic workup and endpoint pages. But it should not be used alone. Its safe role is comparative: place it beside `src-fip-010`, which names limitations, and `src-fip-018`, which separates systemic spread from FIP disease identity.

The safe compiled rule is: mutation detection can be a support tool, but support is not certainty. This paper can justify a mutation-utility row in the diagnostic boundary memo, while the limitation and spread-correlation sources set the ceiling on claim strength.

For wiki reuse, this card should be the positive half of the mutation-diagnostics pair. It prevents the module from overcorrecting into a purely cautionary stance after reading `src-fip-010` and `src-fip-018`. The balanced page should say that mutation detection became clinically relevant for a reason, while still forcing the result through sample context, performance limits, and composite diagnosis.

The comparison structure should be explicit. `src-fip-022` supports a utility claim: spike-gene mutation detection can be discussed as a diagnostic tool. `src-fip-010` limits that claim: using such mutations for diagnosis has boundaries. `src-fip-018` explains one biological reason for caution: some spike changes may correlate with systemic spread rather than FIP disease identity. Together these sources should produce a middle-tier workup rule, not a binary endorsement or rejection.

In the future endpoint handbook, this paper belongs in bounded support below clinicopathology-led suspicion and disease-form recognition. It may help strengthen a suspected case when interpreted in the right sample and clinical context, but the card should not be used to write a standalone definitive-test pathway until full methods, tissue/sample details, and performance metrics are extracted.

This makes the card valuable even before full-text metric recovery. It establishes that the wiki needs a utility branch, then leaves the exact claim strength open until the assay context is verified.

## Limits / Caveats

- current card is deep-extracted at worksheet level, but still not full-text reviewed
- title alone does not reveal sensitivity, specificity, or sample-context limits
- do not promote a definitive diagnostic-test claim without exact methods, sample context, and performance metrics
- utility language should stay below clinicopathology-led suspicion and composite workup logic

## Open Follow-up Questions

- what tissue or sample context was used?
- how strong was the claimed diagnostic utility?
- how directly does this paper conflict with `src-fip-010`?
- should mutation detection sit in Tier 2 support beneath clinicopathology and effusion/CSF context?

## Deep Extraction

- [src-fip-022 deep extraction round 1](../../system/indexes/src-fip-022-deep-extraction-round1.md)

## Linked Entities

- spike gene
- mutation testing
- diagnosis
