---
id: src-fcv-012
type: source
title: "Use of serologic tests to predict resistance to feline herpesvirus 1, feline calicivirus, and feline parvovirus infection in cats"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [serology, resistance prediction, vaccination interval]
jurisdictions: []
evidence_level: original-study
year: 2002
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, serology, resistance, vaccination, challenge]
links:
  doi: "10.2460/javma.2002.220.38"
  url: "https://avmajournals.avma.org/view/journals/javma/220/1/javma.2002.220.38.xml"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed abstract reports 72 laboratory-reared cats and 276 client-owned cats were studied."
    - "PubMed abstract reports laboratory-reared cats were vaccinated with 1 of 3 commercial vaccines or maintained as unvaccinated controls and then challenged with virulent virus 9 to 36 months after vaccination."
    - "PubMed abstract reports predictive values of positive results in vaccinated laboratory-reared cats were 100% for the FCV ELISA and FPV ELISA and 90% for the FHV-1 ELISA."
    - "PubMed abstract reports results of the FCV ELISA were positive for 255 of 276 client-owned cats, corresponding to 92.4%."
    - "PubMed abstract reports because most client-owned cats had detectable serum antibodies suggestive of resistance to infection, arbitrary booster vaccination intervals were likely to lead to unnecessary vaccination of some cats."
  source_supported_conclusion:
    - This is a serology-resistance boundary paper, not a stand-alone vaccination-policy answer.
    - The study supports caution against arbitrary booster intervals, but not against vaccination itself.
    - The paper supports a bounded endpoint branch where antibody detection can help predict resistance in vaccinated cats.
    - The paper supports separating resistance prediction from universal durable protection or broad booster-policy claims.
  llm_inference:
    - This source now serves as the main FCV serology-resistance prediction anchor in the endpoint branch.
    - The safest downstream wording is `predictive in vaccinated cats, but not a universal no-booster rule`.
---

# Use of serologic tests to predict resistance to feline herpesvirus 1, feline calicivirus, and feline parvovirus infection in cats

## One-Line Summary

Vaccination/challenge study suggesting FCV antibody testing can predict resistance in vaccinated cats, with implications for booster policy.

## Why It Matters For FCV

- gives the module a serology-based resistance-prediction paper
- creates a boundary between antibody positivity and broader control strategy
- now serves as the first FCV deep-extracted serology-resistance anchor

## Key Findings

### quoted_fact

- PubMed abstract reports `72` laboratory-reared cats and `276` client-owned cats were studied.
- PubMed abstract reports laboratory-reared cats were vaccinated with `1 of 3` commercial vaccines or maintained as unvaccinated controls and then challenged with virulent virus `9 to 36 months` after vaccination.
- PubMed abstract reports predictive values of positive results in vaccinated laboratory-reared cats were `100%` for the FCV ELISA and FPV ELISA and `90%` for the FHV-1 ELISA.
- PubMed abstract reports results of the FCV ELISA were positive for `255` of `276` client-owned cats, corresponding to `92.4%`.
- PubMed abstract reports because most client-owned cats had detectable serum antibodies suggestive of resistance to infection, arbitrary booster vaccination intervals were likely to lead to unnecessary vaccination of some cats.

### source_supported_conclusion

- This source is the current best FCV paper for keeping serology inside a bounded resistance-prediction branch rather than letting it drift into stand-alone vaccination policy.
- The paper supports using antibody detection as an endpoint interpretation tool in vaccinated cats.
- The paper supports skepticism toward arbitrary booster timing while still staying below anti-vaccination or no-booster rhetoric.
- The strongest safe read is `predictive in vaccinated cats, but not equivalent to universal durable protection`.

### llm_inference

- If the module later builds a fuller FCV vaccination-policy note, this card should control the serology subsection rather than sit as a generic caveat.

## Limits / Caveats

- resistance prediction in vaccinated cats is not the same thing as sterilising immunity
- this card should not be promoted into a universal no-booster rule
- the current extraction is abstract-led and does not recover all challenge-outcome detail by virus or vaccine product

## Serology-Boundary Logic

What can be promoted:

- positive FCV ELISA results can be meaningfully predictive of resistance in vaccinated cats in this study frame
- most client-owned cats in the sampled population had detectable FCV antibodies
- arbitrary booster intervals deserve scrutiny rather than blind repetition

What should be held:

- any statement that antibody positivity equals universal long-term protection
- any conversion of this paper into a universal no-booster recommendation
- any use of this paper to override broader control, challenge, or persistence branches

## Operational Read

This paper matters because it gives the FCV module a clean serology sentence. The
study does not say `antibodies solve policy`, but it does say that in vaccinated cats,
positive FCV ELISA results can be highly predictive of resistance in the study frame,
and that blindly repeating arbitrary booster intervals may overvaccinate some cats.

That is why this card belongs in the endpoint branch, not at the top of the control
stack. `src-fcv-009` still controls broad diagnosis/control wording, `src-fcv-017`
still blocks overclaim on persistence, and `src-fcv-011` / `src-fcv-022` still own
challenge and immune-benefit logic. `src-fcv-012` is the bounded serology layer that
keeps antibody testing useful without letting it become policy absolutism.

Its main value is architectural: it keeps resistance prediction and vaccination policy
from collapsing into one sentence.

## Open Follow-Up Questions

- how should this paper be reconciled with ABCD guidance that still recommends routine vaccination?
- what exact challenge outcomes were prevented versus not prevented?
- how much does the predictive value hold outside vaccinated laboratory-cat conditions and into mixed real-world populations?

## Linked Entities

- diseases: FCV
- models:
- endpoints: serology, resistance prediction, vaccination interval
- mechanisms: humoral immunity
- regulations:
