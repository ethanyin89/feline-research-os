---
id: src-fcv-018
type: source
title: "Identification of prevalent Feline Calicivirus strains and novel antiviral efficacy of CpG49 stimulus in Feline Calicivirus-infected cats"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [clinical recovery, viral shedding, interferon response]
jurisdictions: []
evidence_level: original-study
year: 2025
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, therapy, cpg49, antiviral, in-vivo]
links:
  doi: "10.1016/j.ijbiomac.2025.144105"
  url: "https://pubmed.ncbi.nlm.nih.gov/40350117/"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "PubMed abstract reports the authors established an FCV infection model using the prevalent clinical strain FG24-1."
    - "PubMed abstract reports CpG49 elicited Th1-biased type I and II interferon responses and significantly inhibited FCV replication in vitro and in vivo."
    - "PubMed abstract reports CpG49 reduced serum fSAA by up to 40.38% and increased IFN-gamma by up to 2.14-fold."
    - "PubMed abstract reports the high-dose CpG49 group had 3-day shorter oral-inflammation recovery time and 2-day less fever duration."
    - "PubMed abstract reports viral shedding was 53.4% lower on day 6 and 97.4% lower on day 9 after treatment."
  source_supported_conclusion:
    - This is the strongest in vivo FCV therapeutic signal in the current seed set.
    - The paper supports a distinct immunostimulatory-therapy branch rather than a generic antiviral-screening branch.
    - The paper supports separating clinical recovery, inflammatory moderation, and shedding reduction from vaccine-only endpoint language.
    - The paper supports keeping FCV treatment optimism below routine-care authority while still acknowledging a real therapeutic signal.
  llm_inference:
    - This source now serves as the first deep-extracted in vivo therapeutic anchor in the FCV therapy branch.
    - The safest downstream wording is `promising in vivo therapeutic signal`, not `established FCV treatment standard`.
---

# Identification of prevalent Feline Calicivirus strains and novel antiviral efficacy of CpG49 stimulus in Feline Calicivirus-infected cats

## One-Line Summary

Recent study linking prevalent strain identification to a CpG49 immunostimulatory treatment signal that reduced shedding and improved recovery in FCV-infected cats.

## Why It Matters For FCV

- gives the module a real in vivo therapeutic branch, not just compound screening
- connects interferon-biased immune modulation to measurable recovery and shedding outcomes
- now serves as the first FCV deep-extracted therapy anchor with both clinical and shedding endpoints

## Key Findings

### quoted_fact

- PubMed abstract reports the authors established an FCV infection model using the prevalent clinical strain `FG24-1`.
- PubMed abstract reports CpG49 elicited Th1-biased type I and II interferon responses and significantly inhibited FCV replication in vitro and in vivo.
- PubMed abstract reports CpG49 reduced serum fSAA by up to `40.38%` and increased IFN-gamma by up to `2.14-fold`.
- PubMed abstract reports the high-dose CpG49 group had `3-day` shorter oral-inflammation recovery time and `2-day` less fever duration.
- PubMed abstract reports viral shedding was `53.4%` lower on day 6 and `97.4%` lower on day 9 after treatment.

### source_supported_conclusion

- This source is the current best FCV therapy paper for keeping a real in vivo treatment branch visible without turning that branch into routine-care guidance.
- The paper supports writing FCV treatment effect in three linked layers: immune activation, clinical recovery, and shedding reduction.
- The paper supports a stronger treatment signal than the interferon-sensitivity paper or in vitro screening paper, but still below practice-grade authority.
- The strongest safe read is `promising in vivo immunostimulatory therapy signal with replication pressure still needed`.

### llm_inference

- If the module later builds a fuller FCV treatment-comparison memo, this card should control the first in vivo branch entry rather than remain a generic therapy footnote.

## Limits / Caveats

- a single modern therapeutic paper should not become routine FCV treatment guidance
- confirmation and replication pressure remain high
- the current extraction is abstract-led plus article-summary-led, not a full section-by-section PDF extraction

## Therapy-Branch Logic

What can be promoted:

- FCV now has a real in vivo therapeutic branch, not only supportive-care language plus preclinical screening
- CpG49 produced linked signals across interferon response, inflammatory moderation, clinical recovery, and viral shedding
- treatment endpoints should stay separated from vaccine endpoints rather than flattened into one broad `control` bucket

What should be held:

- any statement that CpG49 is already standard of care
- any claim that one study settles comparative treatment ranking
- any collapse of immune stimulation, supportive care, and vaccine protection into one intervention layer

## Operational Read

This paper matters because it upgrades the FCV therapy branch from assay-stage possibility to
an actual in vivo signal. The preserved abstract facts are structurally stronger than a simple
compound-screening result: the study uses a prevalent clinical strain, shows interferon-biased
immune activation, tracks inflammatory moderation, and reports both symptom recovery and sharply
lower shedding after treatment.

That said, the correct downstream use is still narrow. This source should stabilize the sentence
`FCV has an exploratory but now real in vivo immunostimulatory therapy branch`, while blocking
any leap into routine protocol language, product ranking, or claims that therapeutic benefit has
already solved broader carriage or control problems.

Its main value is architectural: it gives the FCV translation layer one deep-extracted therapy
anchor that is stronger than `in vitro inhibition` but still clearly below standard-of-care
authority.

## Open Follow-Up Questions

- what were the sample sizes and control conditions for the in vivo arm?
- how should this treatment branch be bounded against supportive care and antiviral-screening literature?
- how reproducible are the shedding and recovery gains across other circulating strains or independent cohorts?

## Linked Entities

- diseases: FCV
- models:
- endpoints: clinical recovery, viral shedding, interferon response
- mechanisms: innate immune stimulation, Th1 bias
- regulations:
