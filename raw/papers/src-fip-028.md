---
id: src-fip-028
type: source
title: "GS-441524 and molnupiravir are similarly effective for the treatment of cats with feline infectious peritonitis"
source_kind: paper
species: feline
diseases: [FIP]
models: [prospective comparative cohort]
endpoints: [mortality, remission, clinical resolution, adverse events]
jurisdictions: []
evidence_level: original-study
status: extracted
extraction_depth: full
year: 2024
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fip, gs-441524, molnupiravir, antiviral, comparison, treatment, head-to-head]
links:
  doi: "10.3389/fvets.2024.1422408"
  url: "https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2024.1422408/full"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "118 cats with FIP: 59 received GS-441524 and 59 received molnupiravir."
    - "GS-441524: 12/59 deaths (20.3%); Molnupiravir: 8/59 deaths (13.6%); p = 0.326."
    - "Remission: GS-441524 48/48 (100%); Molnupiravir 51/52 (98%) among treatment completers."
    - "Most deaths occurred within the first 10 days of treatment."
    - "Parameters normalized within 6 to 7 weeks of treatment initiation."
  source_supported_conclusion:
    - "GS-441524 and molnupiravir show similar effects and safety in cats with FIP."
    - "No statistically significant difference in mortality between treatments."
    - "Both achieve near-complete remission in cats that survive initial treatment phase."
  llm_inference:
    - "Treatment choice can be guided by availability, cost, or formulation preference rather than efficacy."
    - "Early mortality (first 10 days) may reflect disease severity at presentation rather than treatment failure."
---

# GS-441524 and molnupiravir are similarly effective for treatment of cats with FIP

## Evidence-Depth Caveat

Full text reviewed. This is a prospective comparative cohort study with matched groups. It supports comparative efficacy claims but is not a randomized controlled trial.

## One-Line Summary

Head-to-head comparison of 118 cats showed GS-441524 and molnupiravir achieve equivalent remission rates (~99%) with no significant difference in mortality.

## Why It Matters For Feline FIP

First direct comparison of the two main FIP antivirals with sufficient sample size. Establishes that molnupiravir is a viable alternative when GS-441524 is unavailable or cost-prohibitive.

## Study Design Details

### Population

| Parameter | GS-441524 | Molnupiravir |
|-----------|-----------|--------------|
| Total cats | 59 | 59 |
| Effusive FIP | ~38 | ~38 |
| Non-effusive FIP | ~21 | ~21 |
| Completed treatment | 48 | 52 |

76 of 118 cats had effusive FIP (fluid accumulation).

### Treatment Protocols

| Drug | Dose Range | Duration | Dose Adjustment |
|------|------------|----------|-----------------|
| GS-441524 (Mutian® Xraphconn) | 12.5–25 mg/kg/day | 84 days | Lower for effusive, higher for neuro/ocular |
| Molnupiravir (compounded) | 20–40 mg/kg/day | 84 days | Lower for effusive, higher for neuro/ocular |

## Key Findings

### quoted_fact

- **Mortality:** GS-441524 20.3% (12/59) vs Molnupiravir 13.6% (8/59), p = 0.326
- **Remission:** GS-441524 100% (48/48) vs Molnupiravir 98% (51/52) among completers
- **Timing:** Most deaths within first 10 days
- **Clinical resolution:** Neurological and ocular signs resolved in all but one cat (persistent seizures)
- **Lab normalization:** Within 6-7 weeks of treatment initiation

### source_supported_conclusion

- No significant efficacy difference between GS-441524 and molnupiravir
- Both achieve near-complete remission in treatment completers
- Adverse events similar: transient hepatic abnormalities resolving without intervention
- Early mortality reflects disease severity, not treatment failure

### llm_inference

- Molnupiravir validated as equivalent alternative to GS-441524
- Treatment selection can prioritize availability/cost/formulation
- 84-day protocol standard for both drugs
- Higher doses needed for neurological/ocular involvement (both drugs)

## Claim-Fit Judgment

Strongest safe use:
- Comparative antiviral efficacy between GS-441524 and molnupiravir
- Molnupiravir as viable first-line FIP treatment
- Remission rates for both drugs
- 84-day treatment duration standard

Must not control yet:
- Optimal dosing within ranges (individualized based on presentation)
- Long-term relapse rates (study reports remission, not long-term follow-up)
- Cost-effectiveness (not studied)
- Drug-resistant case management

## Deep Extraction

- Round 1 worksheet: [system/indexes/src-fip-028-deep-extraction-round1.md](../../system/indexes/src-fip-028-deep-extraction-round1.md)

## Clinical Context

This study addresses a critical clinical question: are the two available FIP antivirals truly interchangeable? GS-441524 became the first effective FIP treatment in 2019, but availability and cost issues drove interest in alternatives. Molnupiravir, originally developed for influenza and later used against COVID-19, emerged as a potential option. This head-to-head comparison provides the evidence base for treating either drug as a first-line option, with selection guided by availability, cost, and formulation preferences rather than efficacy differences.

The use of dose adjustment by disease severity (lower for effusive, higher for neurological or ocular involvement) reflects clinical experience that central nervous system penetration requires higher plasma concentrations for both drugs. This dosing strategy is now standard practice in FIP treatment protocols.

## Linked Entities

- diseases: FIP (effusive and non-effusive)
- models: prospective comparative cohort
- endpoints: mortality, remission, clinical resolution, hepatic function
- mechanisms: antiviral (nucleoside analogs - both are adenosine analogs)
- regulations: none applicable
