---
id: topic-fip-translation-brief
type: topic
topic: fip
species: feline
disease: FIP
question_type: translation
source_ids: [src-fip-003, src-fip-013, src-fip-016, src-fip-017, src-fip-019, src-fip-024]
last_compiled_at: 2026-04-11
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-04-22 checked for wording drift; translation page remains source-bounded and not universal efficacy guidance."
owner: codex
status: active
---

# Feline FIP Translation Brief

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FT1 | FIP treatment has materially transformed in the GS/remdesivir era | B | src-fip-003, src-fip-013, src-fip-016, src-fip-019 | treatment transformation, not universal cure |
| FT2 | Neurologic rescue and package-logic evidence should not be collapsed into baseline GS efficacy | B | src-fip-017, src-fip-019, src-fip-024 | branch separation |
| FT3 | Translation should remain below diagnostic and regulatory certainty boundaries | C | src-fip-003, src-reg-014 | not decision-grade |

## Quick Helpers

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)

## Question This Page Answers

From disease biology to clinical use, where are the strongest translational bridges in FIP and where are the easiest overclaims?

## Current Safe Reading

- The current translational center of gravity is no longer only diagnosis; it is also `antiviral treatment transformation`
- GS-441524-era papers should be modeled as a distinct treatment branch, not mixed back into older fatalism-era review language
- neurologic FIP should be treated as an important treatment-complexity branch, not just a severity footnote
- treatment transformation should not erase the fact that diagnosis remains supportive and composite
- the antiviral layer is now better read as a branch-comparison problem than as a one-line efficacy story

## Current Conclusions

### quoted_fact

- The current source set includes efficacy and safety work on GS-441524 in naturally occurring FIP.
- The current source set includes tissue-culture and experimental-infection work on GS-441524.
- The current source set includes long-term remission follow-up after oral GS-441524 treatment.
- The current source set includes remdesivir and GS-441524 combination treatment in effusive and non-effusive FIP.
- The current source set includes dedicated antiviral treatment material for neurologic FIP.

### source_supported_conclusion

- The modern FIP treatment branch is already strong enough to justify a dedicated translational layer from day one.
- It is important to separate `proof of antiviral activity`, `clinical remission data`, and `real-world treatment package logic`.
- Neurologic FIP and long-term remission are likely to become two of the most decision-relevant translation subbranches.
- The first deep-extracted broad review supports modeling FIP translation as `diagnostic ambiguity plus treatment transformation`, not as treatment only.
- The first deep-extracted experimental GS paper now supports a true `preclinical antiviral foundation` layer below natural-disease treatment evidence.
- The first deep-extracted natural-disease treatment anchor supports real treatment transformation, but does not justify universal efficacy claims across severe neurologic and ocular disease.
- The first deep-extracted remdesivir-plus-GS series now supports a distinct `real-world treatment package` layer beyond the baseline GS anchor.
- The first deep-extracted neurologic-treatment paper now supports a distinct `neurologic rescue / high-complexity treatment` layer beyond both baseline efficacy and package logic.
- The neurologic rescue branch is now clearer as a treatment-category shift rather than an intensified version of ordinary baseline antiviral treatment.
- The first deep-extracted remission follow-up paper now supports a distinct `post-treatment durability` layer beyond initial response.
- The treatment layer is now strong enough to support a dedicated antiviral-branch comparison memo even though final protocol hierarchy is still unresolved.

### llm_inference

- FIP may be the first disease in this vault where the treatment branch rapidly outruns the regulatory branch in practical importance.

## Evidence Map

- broad review anchor: `src-fip-003`
- remission / follow-up branch: `src-fip-013`
- natural-disease treatment anchor: `src-fip-016`
- experimental antiviral anchor: `src-fip-017`
- remdesivir plus GS real-world branch: `src-fip-019`
- neurologic treatment branch: `src-fip-024`

Related working page:

- [src-fip-003 deep extraction round 1](../../system/indexes/src-fip-003-deep-extraction-round1.md)
- [src-fip-013 deep extraction round 1](../../system/indexes/src-fip-013-deep-extraction-round1.md)
- [src-fip-017 deep extraction round 1](../../system/indexes/src-fip-017-deep-extraction-round1.md)
- [src-fip-016 deep extraction round 1](../../system/indexes/src-fip-016-deep-extraction-round1.md)
- [src-fip-019 deep extraction round 1](../../system/indexes/src-fip-019-deep-extraction-round1.md)
- [src-fip-024 deep extraction round 1](../../system/indexes/src-fip-024-deep-extraction-round1.md)
- [FIP treatment evidence memo](../../system/indexes/fip-treatment-evidence-memo.md)
- [FIP antiviral-branch comparison memo](../../system/indexes/fip-antiviral-branch-comparison-memo.md)
- [FIP neurologic rescue boundary memo](../../system/indexes/fip-neurologic-rescue-boundary-memo.md)
- [FIP diagnostic-workup memo](../../system/indexes/fip-diagnostic-workup-memo.md)
- [FIP briefing round 1 working-en](../../outputs/briefings/out-fip-briefing-20260410-round1-working-en.md)
- [FIP dossier v1 working-en](../../outputs/dossiers/out-fip-dossier-20260410-v1-working-en.md)
- [FIP output language matrix](../../system/indexes/fip-output-language-matrix.md)

## Conflicts / Uncertainty

- We have not yet separated clinical efficacy, access pathway, and regulatory legitimacy.
- The current vault should not yet flatten all GS/remdesivir-era material into one outcome claim.
- The current strongest treatment anchor still excludes severe neurologic and ocular cases, so the branch must stay form-sensitive.
- The experimental antiviral anchor is strong enough to stabilize the lower treatment layer, but still does not replace natural-disease treatment evidence.
- The real-world package anchor is broader and more practice-like, but still remains retrospective case-series evidence.
- The neurologic-treatment anchor is clinically decisive for branch structure, but still rests on only four cases.
- The remission-durability anchor follows only successfully treated cats, so it should not be reused as a whole-branch cure-rate estimate.

## Gaps

- no treatment ranking memo yet
- no outcome architecture yet
- no access / implementation memo yet
- no final protocol hierarchy yet across baseline GS-441524 efficacy, neurologic FIP treatment, and remdesivir-plus-GS package logic
