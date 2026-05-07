---
id: src-fcv-010
type: source
title: "Neutralizing Feature of Commercially Available Feline Calicivirus (FCV) Vaccine Immune Sera against FCV Field Isolates"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [neutralisation, field isolates, vaccine breadth]
jurisdictions: [Japan]
evidence_level: original-study
year: 1999
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, vaccine, neutralisation, field-isolates, japan]
links:
  doi: "10.1292/jvms.61.299"
  url: "https://www.jstage.jst.go.jp/article/jvms/61/3/61_3_299/_article"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "J-STAGE abstract reports four commercially available FCV vaccines were compared using sera from specific-pathogen-free cats immunized by two injections of each vaccine."
    - "J-STAGE abstract reports each vaccine immune serum neutralized laboratory strains F4, F9, and 255 relatively well."
    - "J-STAGE abstract reports that across 36 field isolates, vaccine A sera failed to neutralize 18-20 strains, vaccine B 19-22 strains, vaccine C 22-25 strains, and vaccine D 8-16 strains."
    - "J-STAGE full text reports there were eight field isolates that were not neutralized by any immune serum."
    - "J-STAGE abstract reports the results suggested much difference in neutralizing antigenicity between existing vaccine strains and FCV strains prevalent in Japan."
  source_supported_conclusion:
    - This is an early warning paper against assuming uniform vaccine breadth.
    - The paper belongs under vaccine-breadth boundary, not clinical efficacy ranking.
    - The paper supports separating laboratory-strain neutralization from field-isolate coverage.
    - The paper supports writing FCV vaccine breadth as product-variable and incomplete rather than flatly broad.
  llm_inference:
    - This source now serves as the early field-fit stress-test anchor beneath later UK breadth and challenge papers.
    - The safest downstream wording is `laboratory neutralization can look much cleaner than field-isolate coverage`.
---

# Neutralizing Feature of Commercially Available Feline Calicivirus (FCV) Vaccine Immune Sera against FCV Field Isolates

## One-Line Summary

Early field-isolate neutralisation paper showing commercial FCV vaccines could leave many field strains insufficiently neutralised.

## Why It Matters For FCV

- provides an older but sharp vaccine-limit anchor
- helps explain why cross-neutralisation remains a recurring FCV control problem
- now serves as the first FCV deep-extracted early field-fit stress-test anchor

## Key Findings

### quoted_fact

- J-STAGE abstract reports four commercially available FCV vaccines were compared using sera from specific-pathogen-free cats immunized by two injections of each vaccine.
- J-STAGE abstract reports each vaccine immune serum neutralized laboratory strains `F4`, `F9`, and `255` relatively well.
- J-STAGE abstract reports that across `36` field isolates, vaccine A sera failed to neutralize `18-20` strains, vaccine B `19-22` strains, vaccine C `22-25` strains, and vaccine D `8-16` strains.
- J-STAGE full text reports there were `8` field isolates that were not neutralized by any immune serum.
- J-STAGE abstract reports the results suggested much difference in neutralizing antigenicity between existing vaccine strains and FCV strains prevalent in Japan.

### source_supported_conclusion

- This source is the current best FCV paper for showing that laboratory-strain neutralization can materially overstate field-isolate coverage.
- The paper supports product-variable and geography-sensitive vaccine-breadth language rather than one generic `vaccines neutralize FCV` sentence.
- The paper supports a stronger early warning about field-fit instability than the broader review layer can provide on its own.
- The strongest safe read is `breadth is partial and field-fit can be much weaker than laboratory readouts suggest`.

### llm_inference

- If the module later builds a fuller vaccine-comparison memo, this card should control the early historical stress-test subsection rather than remain a background citation.

## Limits / Caveats

- old field-isolate data should not be promoted as current vaccine performance
- in vitro neutralisation does not equal full clinical protection or failure
- the current extraction is abstract-led plus limited full-text sampling, not a full line-by-line extraction of the entire article

## Breadth-Boundary Logic

What can be promoted:

- vaccine sera can look strong against laboratory strains while remaining incomplete against real field isolates
- breadth differs materially across commercial vaccine products in this paper
- some field isolates escaped all tested immune sera in this dataset

What should be held:

- any statement that this 1999 Japanese dataset defines current global vaccine performance
- any direct conversion from neutralization gaps to clinical inefficacy
- any flat sentence suggesting all commercial vaccines had the same field-isolate profile

## Operational Read

This paper matters because it makes the FCV vaccine-breadth problem concrete. It does
not merely say `variants matter`; it shows a specific pattern the module needs to keep
visible: vaccine sera can neutralize laboratory strains relatively well while leaving a
large fraction of field isolates uncovered, and some isolates may escape all tested sera.

That is why this card belongs under the vaccine-breadth boundary layer, not under final
clinical ranking. `src-fcv-003` still carries the newer `broad but incomplete` UK-style
message, and `src-fcv-011` still carries challenge protection, but `src-fcv-010` is the
older stress-test that explains why broad review language should never drift into uniform
field-coverage rhetoric.

Its main value is architectural: it keeps early field-fit instability explicit in the
FCV vaccine branch.

## Open Follow-Up Questions

- how should this older Japanese signal be weighed against later UK work?
- which products or strains were most divergent?
- how often do later datasets reproduce the `lab strains good, field isolates weaker` pattern across jurisdictions?

## Linked Entities

- diseases: FCV
- models:
- endpoints: neutralisation, field isolates, vaccine breadth
- mechanisms: antigenic diversity
- regulations:
