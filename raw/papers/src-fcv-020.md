---
id: src-fcv-020
type: source
title: "Identification of feline calicivirus in cats with enteritis"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [enteric detection, pathotype extension]
jurisdictions: []
evidence_level: original-study
year: 2020
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, enteritis, extension, pathotype, enteric]
links:
  doi: "10.1111/tbed.13605"
  url: "https://onlinelibrary.wiley.com/doi/10.1111/tbed.13605"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Accessible abstract/card extraction reports FCV RNA was identified in 25.9% of stools from cats with enteritis and in 0% of controls without diarrhea."
    - "Accessible abstract/card extraction reports enteric isolates were more resistant to low pH, trypsin, and bile treatment than respiratory isolates."
    - "Accessible abstract/card extraction reports the authors suggested FCV should be considered in enteric diagnostic algorithms."
  source_supported_conclusion:
    - This is the current main FCV enteric-extension anchor in the seed set.
    - The paper supports treating enteric tropism as a real extension branch rather than a casual aside.
    - The paper supports bounded enteric-differential visibility rather than routine enteritis leadership.
    - The paper should control the enteric extension branch, not core-disease or prevalence language.
  llm_inference:
    - This source now serves as the first deep-extracted enteric-extension anchor in the FCV recognition branch.
    - The safest downstream wording is `bounded enteric extension`, not `FCV as a routine enteritis lead cause`.
---

# Identification of feline calicivirus in cats with enteritis

## One-Line Summary

Enteric-pathotype paper showing FCV can remain visible as a bounded enteric-recognition extension branch, with some isolates showing adaptation features beyond classic respiratory framing.

## Why It Matters For FCV

- creates a non-respiratory extension branch with phenotype and stability implications
- helps stop the module from assuming all FCV biology is only oral/upper respiratory
- now serves as the first FCV deep-extracted enteric-extension anchor

## Key Findings

### quoted_fact

- Accessible abstract/card extraction reports FCV RNA was identified in 25.9% of stools from cats with enteritis and in 0% of controls without diarrhea.
- Accessible abstract/card extraction reports enteric isolates were more resistant to low pH, trypsin, and bile treatment than respiratory isolates.
- Accessible abstract/card extraction reports the authors suggested FCV should be considered in enteric diagnostic algorithms.

### source_supported_conclusion

- This source is the current best FCV enteric-extension paper for keeping the enteric branch visible without replacing the core oral/respiratory frame.
- The paper supports enteric FCV as a bounded extension branch with pathotype-adaptation pressure.
- The strongest safe read is `consider in differential, not promote to lead cause`.

### llm_inference

- If the module later builds a fuller FCV workup page, this card should control the enteric branch entry rather than a generic extension footnote.

## Limits / Caveats

- this is not a stand-alone enteritis-screening paper
- this is a branch-extension paper, not a new FCV core-disease owner
- broader replication is needed before enteric FCV becomes routine clinical framing
- current card is deep-extracted at worksheet level, but still not full-text reviewed section by section

## Enteric-Extension Branch Logic

What can be promoted:

- FCV-enteric association is a real extension branch
- enteric isolates may carry adaptation-relevant phenotype signals
- FCV can remain visible in enteric differential thinking

What should be held:

- any routine feline-enteritis lead-cause claim
- any front-door FCV suspicion shortcut from diarrhea alone
- any whole-population enteric prevalence claim

## Operational Read

This paper is strongest when reused as a branch-order control source rather than as a
generic prevalence citation. The preserved `25.9%` versus `0%` contrast keeps the
enteric signal visible, while the acid/trypsin/bile-resistance result explains why the
paper matters beyond a single stool-detection observation.

That combination supports one narrow downstream sentence: enteric FCV deserves a place
in differential thinking when syndrome context fits, but it still sits below the main
oral/respiratory FCV recognition shell.

This card is best reused as an enteric-extension recognition source rather than as a new core-disease framing source.

Its main value is architectural: it lets the module say `enteric FCV remains visible but bounded` without collapsing the oral/respiratory shell.

## Write-Back Implications

- [risk and recognition](../../topics/fcv/risk-and-recognition.md) should treat this card as the first deep-extracted enteric-extension anchor.
- [FCV recognition architecture memo](../../system/indexes/fcv-recognition-architecture-memo.md) can now lean more directly on `bounded enteric extension`.
- [current state dashboard](../../topics/fcv/current-state-dashboard.md) should treat the extension branch as having both ocular and enteric deep-extracted anchors.

## Open Follow-Up Questions

- how stable is the enteric tropism over time and passage?
- does enteric adaptation trade off against classic respiratory or VS-FCV behavior?
- how often should FCV meaningfully enter chronic-enteritis differential language outside this source context?

## Linked Entities

- diseases: FCV
- models:
- endpoints: enteric detection, pathotype extension
- mechanisms: enteric tropism, environmental stability
- regulations:
