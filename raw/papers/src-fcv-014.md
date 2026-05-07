---
id: src-fcv-014
type: source
title: "Potential Therapeutic Agents for Feline Calicivirus Infection"
source_kind: paper
species: feline
diseases: [FCV]
models: []
endpoints: [antiviral screening, in vitro inhibition]
jurisdictions: []
evidence_level: original-study
year: 2018
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: no
language_qa_status: not_applicable
tags: [fcv, therapy, antivirals, screening, in-vitro]
links:
  doi: "10.3390/v10080433"
  url: "https://www.mdpi.com/1999-4915/10/8/433"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "MDPI abstract reports 15 compounds from different antiviral classes were tested against FCV using in vitro protein and cell culture assays."
    - "MDPI abstract reports two in vitro assays were established to assess inhibitory activity directly against the FCV protease or polymerase."
    - "MDPI abstract reports quercetagetin and PPNDS inhibited FCV polymerase activity with IC50 values of 2.8 uM and 2.7 uM, respectively."
    - "MDPI abstract reports GC376 inhibited FCV protease activity with an IC50 of 18 uM."
    - "MDPI abstract reports nitazoxanide and 2'-C-methylcytidine inhibited FCV replication in cell culture with EC50 values of 0.6 uM and 2.5 uM, respectively."
  source_supported_conclusion:
    - This is a therapy-frontier methods paper, not a clinical treatment guideline.
    - The paper supports a distinct FCV antiviral-discovery branch below clinical translation.
    - The paper supports separating enzyme-inhibition hits from cell-culture replication hits instead of collapsing them into one candidate list.
    - The paper supports using assay-stage FCV therapy language as discovery infrastructure, not practice-grade intervention evidence.
  llm_inference:
    - This source now serves as the main FCV assay-stage therapy anchor beneath the interferon and in vivo branches.
    - The safest downstream wording is `screening and assay infrastructure with selective hits`, not `candidate treatment recommendations`.
---

# Potential Therapeutic Agents for Feline Calicivirus Infection

## One-Line Summary

In vitro antiviral-screening paper building assay infrastructure for FCV therapeutic discovery and surveying candidate compounds.

## Why It Matters For FCV

- gives the module a therapy-discovery anchor instead of only supportive-care discussion
- helps keep antiviral claims tied to assay stage rather than clinical efficacy
- now serves as the first FCV deep-extracted assay-stage therapy anchor

## Key Findings

### quoted_fact

- MDPI abstract reports `15` compounds from different antiviral classes were tested against FCV using in vitro protein and cell culture assays.
- MDPI abstract reports two in vitro assays were established to assess inhibitory activity directly against the FCV protease or polymerase.
- MDPI abstract reports quercetagetin and PPNDS inhibited FCV polymerase activity with `IC50` values of `2.8 uM` and `2.7 uM`, respectively.
- MDPI abstract reports GC376 inhibited FCV protease activity with an `IC50` of `18 uM`.
- MDPI abstract reports nitazoxanide and `2'-C-methylcytidine` inhibited FCV replication in cell culture with `EC50` values of `0.6 uM` and `2.5 uM`, respectively.

### source_supported_conclusion

- This source is the current best FCV paper for keeping assay-stage antiviral discovery separate from in vivo treatment language.
- The paper supports a three-layer read inside the therapy branch: enzyme hits, cell-culture replication hits, and later in vivo translation.
- The paper supports nitazoxanide and 2CMC as the strongest cell-culture candidates in this study, while blocking overpromotion of polymerase or protease hits that did not translate into cell-culture antiviral effect.
- The strongest safe read is `discovery infrastructure plus selective cell-culture leads`, not `finished FCV therapeutic shortlist`.

### llm_inference

- If the module later builds a therapy-comparison memo, this card should control the assay-stage subsection rather than remain a generic antiviral-frontier citation.

## Limits / Caveats

- the paper is preclinical and not an in vivo treatment answer
- compound signals should not be promoted into owner-facing therapy recommendations
- the current extraction is abstract-led and section-sampled rather than a full line-by-line PDF extraction

## Therapy-Discovery Logic

What can be promoted:

- FCV now has a real assay-stage antiviral-discovery branch rather than only supportive-care prose
- enzyme-target inhibition and cell-culture inhibition should be kept as separate endpoint families
- nitazoxanide and 2CMC are the main cell-culture leads in this paper

What should be held:

- any statement that polymerase/protease inhibition automatically means useful antiviral effect in infected cells
- any promotion of this paper into clinical treatment guidance
- any flattening of quercetagetin, PPNDS, GC376, nitazoxanide, and 2CMC into one equivalent candidate bucket

## Operational Read

This paper matters because it organizes the bottom layer of the FCV therapy branch. It does
not answer which treatment works in cats, but it does tell the module how to read early
therapeutic evidence: first ask whether a compound hits a viral enzyme, then ask whether that
signal survives in infected cells, and only after that ask whether an in vivo study exists.

That structure is why this card belongs beneath `src-fcv-008` and `src-fcv-018`. `src-fcv-014`
provides the assay and screening scaffold, `src-fcv-008` adds strain-sensitive interferon
caution, and `src-fcv-018` adds the first bounded in vivo treatment signal. The correct
downstream sentence is therefore narrow: FCV therapy now has a structured frontier, but its
lowest layer is still discovery infrastructure rather than routine intervention evidence.

Its main value is architectural: it stops the therapy branch from jumping directly from
supportive care to in vivo optimism without preserving the assay-stage middle.

## Open Follow-Up Questions

- which compounds looked strongest and by what assay logic?
- how should this paper be reconciled with newer CpG49 in vivo work?
- which assay-stage hits remained promising once enzyme and cell-culture results were compared head to head?

## Linked Entities

- diseases: FCV
- models:
- endpoints: antiviral screening, in vitro inhibition
- mechanisms: replication inhibition
- regulations:
