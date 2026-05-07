---
id: src-fcv-021
type: source
title: "Feline calicivirus: a neglected cause of feline ocular surface infections?"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [ocular lesions, urtd association]
jurisdictions: []
evidence_level: original-study
year: 2012
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, ocular, urtd, recognition, extension]
links:
  doi: "10.1111/j.1463-5224.2011.00957.x"
  url: "https://onlinelibrary.wiley.com/doi/10.1111/j.1463-5224.2011.00957.x"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "Accessible abstract/card extraction reports FCV was detected in 30 of 63 pathogen-positive cats with ocular surface infection and URTD history or symptoms."
    - "Accessible abstract/card extraction reports erosive conjunctivitis was highlighted as an important ocular finding."
    - "Accessible abstract/card extraction reports oral ulcers were detected in all FCV-infected cats."
    - "Accessible worksheet extraction reports FCV appeared both alone and with other infectious agents in the ocular-disease context."
  source_supported_conclusion:
    - This is the current main FCV ocular-extension anchor in the seed set.
    - The paper supports keeping ocular-surface disease visible in FCV recognition architecture.
    - The paper supports syndrome-context reading of ocular FCV rather than stand-alone ocular shortcut logic.
    - The paper should control the ocular extension branch, not whole-population prevalence or sole-cause language.
  llm_inference:
    - This source now serves as the first deep-extracted ocular-extension anchor in the FCV recognition branch.
    - The safest downstream wording is `ocular extension with co-pathogen caution`, not `FCV front-door ocular diagnosis`.
---

# Feline calicivirus: a neglected cause of feline ocular surface infections?

## One-Line Summary

Ocular-surface study showing FCV is a meaningful ocular-recognition extension branch when ocular disease appears inside a FCV-compatible respiratory/oral syndrome context.

## Why It Matters For FCV

- creates a specific recognition-extension branch for ocular surface disease
- helps resist collapsing FCV signs to only oral ulcers and mild respiratory signs
- now serves as the first FCV deep-extracted ocular-extension anchor

## Key Findings

### quoted_fact

- Accessible abstract/card extraction reports FCV was detected in 30 of 63 pathogen-positive cats with ocular surface infection and URTD history or symptoms.
- Accessible abstract/card extraction reports erosive conjunctivitis was highlighted as an important ocular finding.
- Accessible abstract/card extraction reports oral ulcers were detected in all FCV-infected cats.

### source_supported_conclusion

- This source is the current best FCV ocular-extension paper for keeping ocular-surface disease visible without replacing the core oral/respiratory recognition frame.
- The paper supports ocular FCV as a syndrome-context enrichment branch, not a stand-alone front door.
- The strongest safe read is `ocular extension with co-pathogen caution`.

### llm_inference

- If the module later builds a fuller FCV workup page, this card should control the ocular branch entry rather than a generic caveat sentence.

## Limits / Caveats

- this is not a stand-alone ocular-screening paper
- this is not a whole-population prevalence study
- FCV ocular association should not erase the role of FHV-1, Chlamydophila, or Mycoplasma
- current card is deep-extracted at worksheet level, but still not full-text reviewed section by section

## Ocular-Extension Branch Logic

What can be promoted:

- ocular-surface disease is a real FCV extension branch
- erosive conjunctivitis belongs in the FCV ocular-recognition vocabulary
- ocular findings are stronger when they remain inside broader FCV-compatible syndrome context

What should be held:

- any whole-population ocular prevalence claim
- any sole-cause claim that displaces FHV-1 or other pathogens
- any promotion of ocular findings into a new FCV front-door shortcut

## Operational Read

This paper should be reused as a syndrome-context control source, not as a shortcut
from conjunctivitis to FCV diagnosis. Its preserved value is the combination of ocular
surface disease, URTD context, oral-ulcer overlap, and explicit co-pathogen caution.

That is why the safest downstream sentence stays narrow: ocular disease belongs in FCV
extension routing when the broader syndrome fits, but it should not erase competing
infectious differentials or become a stand-alone prevalence claim.

This card is best reused as an ocular-extension recognition source rather than as a general ocular-disease prevalence source.

Its main value is architectural: it lets the module say `ocular disease belongs in FCV extension routing` without breaking co-pathogen discipline.

## Write-Back Implications

- [risk and recognition](../../topics/fcv/risk-and-recognition.md) should treat this card as the first deep-extracted ocular-extension anchor.
- [FCV recognition architecture memo](../../system/indexes/fcv-recognition-architecture-memo.md) can now lean more directly on `ocular extension with co-pathogen caution`.
- [current state dashboard](../../topics/fcv/current-state-dashboard.md) should treat the extension branch as having at least one deep-extracted ocular-recognition anchor.

## Open Follow-Up Questions

- which ocular lesions were most FCV-associated after controlling for co-infections?
- how should ocular disease fit under a broader FCV recognition page?
- how often does ocular FCV suspicion remain useful once broader respiratory/oral syndrome context is missing?

## Linked Entities

- diseases: FCV
- models:
- endpoints: ocular lesions, urtd association
- mechanisms: tissue tropism, co-infection
- regulations:
