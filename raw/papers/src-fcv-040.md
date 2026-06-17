---
id: src-fcv-040
type: source
title: "An Outbreak of Limping Syndrome Associated with Feline Calicivirus"
source_kind: paper
species: feline
diseases: [FCV]
models: [outbreak-investigation, natural-transmission]
endpoints: [limping-syndrome, viral-transmission, genome-sequencing]
jurisdictions: [Italy]
evidence_level: original-study
year: 2023
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
pmid: "37889723"
doi: "10.3390/animals13111778"
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, limping-syndrome, viral-arthritis, household-outbreak, genome-sequencing, respiratory-origin, pathotype-retention]
links:
  doi: "10.3390/animals13111778"
  url: "https://doi.org/10.3390/animals13111778"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "A small outbreak of FCV infection in two household cats, in which limping disease was monitored with a 12-day lag time."
    - "Up to 39 synonymous nucleotide mutations identified between isolates."
    - "Sensitivity to low pH conditions and trypsin treatment, a pattern usually associated with viruses isolated from the upper respiratory tract."
    - "The asynchronous pattern of infections and the results of genome sequencing suggest that a virus of respiratory origin was transmitted between the animals and that the FCV strain was able to retain the limping disease pathotype during the transmission chain."
  source_supported_conclusion:
    - "FCV limping syndrome can transmit naturally between household cats."
    - "Limping pathotype retained during cat-to-cat transmission (not lost)."
    - "Respiratory-origin virus can cause limping syndrome."
    - "12-day lag between sequential infections in household."
    - "Complete genome sequencing showed 39 synonymous mutations during transmission."
  llm_inference:
    - "Natural transmission confirms experimental findings of pathotype persistence."
    - "Household contact is sufficient for limping syndrome spread."
    - "Synonymous mutations suggest ongoing viral evolution without phenotype change."
---

# An Outbreak of Limping Syndrome Associated with Feline Calicivirus

## Evidence-Depth Caveat

**Deep-extracted from PubMed abstract (PMID 37889723).** 2023 Animals: household outbreak (n=2 cats), 12-day lag between infections. Complete genome sequencing (39 synonymous mutations). Respiratory-origin virus retained limping pathotype during natural transmission. Evidence level: outbreak investigation with molecular characterization.

## Source Check, 2026-06-17

PubMed abstract extracted.

- PMID: 37889723
- DOI: 10.3390/animals13111778
- Journal: Animals (MDPI)
- Year: 2023
- Authors: Lanave et al.
- Open access: yes

## Outbreak Details

| Feature | Value |
|---------|-------|
| Setting | Household |
| Cats affected | 2 |
| Transmission lag | 12 days between infections |
| Pattern | Asynchronous (sequential) |
| Clinical signs | Upper respiratory → limping |

## Viral Characterization

| Analysis | Finding |
|----------|---------|
| Genome sequencing | Complete genome obtained |
| Mutations | 39 synonymous nucleotide changes |
| pH sensitivity | Low pH sensitive |
| Trypsin sensitivity | Yes |
| Origin | **Respiratory tract** |

**Quoted:** "Sensitivity to low pH conditions and trypsin treatment, a pattern usually associated with viruses isolated from the upper respiratory tract."

## Key Finding: Pathotype Retention

**Quoted:** "The asynchronous pattern of infections and the results of genome sequencing suggest that a virus of respiratory origin was transmitted between the animals and that the FCV strain was able to retain the limping disease pathotype during the transmission chain, as previously observed in experimental studies."

- Limping pathotype **not lost** during natural transmission
- Confirms experimental observations in real-world setting
- Respiratory-origin virus can cause joint disease

## One-Line Summary

2023 household FCV outbreak (n=2, 12-day lag): genome sequencing (39 mutations) shows respiratory-origin virus retained limping pathotype during natural cat-to-cat transmission.

## Claim-Fit Judgment

**Strongest safe use:**
- FCV limping syndrome natural transmission
- Pathotype retention evidence
- Respiratory-origin virus causing limping
- Household outbreak epidemiology

**May control:**
- FCV mechanism-overview.md limping syndrome section
- Clinical presentation diversity

**Should use with caveats:**
- Small outbreak (n=2)
- Single household

**Must not control:**
- Prevalence estimates
- Treatment protocols

## Deep Extraction Metadata

- **Extraction date:** 2026-06-17
- **Source:** PubMed abstract (PMID 37889723)
- **Full text verified:** Abstract-level
- **Citations in vault topic pages:** 1

## Linked Entities

- diseases: FCV, limping syndrome, viral arthritis
- transmission: household contact, respiratory
- endpoints: limping, joint involvement
- methods: complete genome sequencing
- mechanisms: pathotype retention, viral evolution
