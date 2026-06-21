---
id: src-cancer-077
type: source
title: "BNCT of 3 cases of spontaneous head and neck cancer in feline patients"
source_kind: paper
species: feline
diseases: [cancer]
models: []
endpoints: []
jurisdictions: []
evidence_level: case-series
year: 2004
status: deep_extracted
extraction_depth: deep
verification_status: abstract_weighted
decision_grade: no
language_qa_status: not_applicable
pmid: 15308173
tags: [cancer, BNCT, boron-neutron-capture, SCC, head-neck, radiotherapy, investigational]
links:
  doi: "10.1016/j.apradiso.2004.05.016"
  url: "https://www.sciencedirect.com/science/article/abs/pii/S0969804304003045?via%3Dihub"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "BPA-BNCT showed no radiotoxic effects in 3 terminal feline patients."
    - "Results: partial tumor control, impaired growth, partial necrosis."
    - "Improved clinical condition and prolonged survival beyond terminal condition."
  source_supported_conclusion:
    - "BNCT is feasible and safe for spontaneous head/neck tumors in feline patients."
    - "BPA delivered therapeutic boron levels to tumor."
  llm_inference:
    - "Early investigational study; n=3 terminal patients only."
    - "May inform oral-squamous-cell-carcinoma.md experimental therapy section."
  # V2 enhanced fields
  study_design: "病例系列（2004 年 Appl Radiat Isot），3 例终末期猫头颈癌，BPA-BNCT（硼中子俘获治疗）"
  core_argument: "BNCT 在自发性猫头颈癌中可行且安全——BPA 递送治疗性硼浓度到肿瘤——无放射毒性——部分肿瘤控制（生长抑制、部分坏死）——改善临床状况并延长终末期生存"
  implicit_premise: "假设终末期患者的安全性信号可扩展到较早期患者；假设部分肿瘤控制代表有意义的临床获益"
  unexpected_finding: "终末期患者实现了生存延长和临床状况改善——考虑到终末期基线，任何获益都有意义——但 n=3 限制了任何结论"
  title_gap: "标题说 3 例自发性猫头颈癌的 BNCT，但真正发现是可行性：治疗性硼浓度可实现、无放射毒性、部分反应——为更大研究奠定基础但本身不支持临床采用"
  evidence_boundary: "小病例系列（n=3）仅终末期患者；仅支持历史可行性背景，不支持治疗推荐；BNCT 仍为研究性治疗"
---

# BNCT of 3 cases of spontaneous head and neck cancer in feline patients

## Evidence-Depth Caveat

This card has deep extraction based on the full abstract. 2004 Appl Radiat Isot: n=3 terminal feline head/neck cancer; BPA-BNCT (boron neutron capture therapy); no radiotoxicity; partial tumor control and improved survival; investigational therapy; historical feasibility study. [Deep extraction worksheet](../../system/indexes/src-cancer-077-deep-extraction-round1.md).

## Source Check, 2026-06-02

| Field | Value |
|-------|-------|
| PMID | 15308173 |
| DOI | 10.1016/j.apradiso.2004.05.016 |
| Journal | Appl Radiat Isot |
| Year | 2004 |
| Authors | Rao M, Trivillin VA, Heber EM, et al. |

## Abstract Summary

| Category | Finding |
|----------|---------|
| Treatment | BPA-BNCT (boron neutron capture therapy) |
| Population | 3 terminal feline patients with spontaneous head/neck tumors |
| Biodistribution | BPA delivered therapeutic boron levels to tumor |
| Safety | No radiotoxic effects observed |
| Efficacy | Partial tumor control, impaired growth, partial necrosis |
| Clinical outcome | Improved condition, prolonged survival beyond terminal state |

**Boundary:** Abstract-level extraction. Small case series (n=3) of terminal patients. Investigational therapy; not standard of care.

## One-Line Summary

BNCT feasibility study in 3 terminal feline head/neck cancer patients showing partial tumor control and improved survival with no radiotoxicity.

## Why It Matters For Feline Cancer

This source was included in a reviewed feline literature intake sheet and classified as `new-cancer` by the intake workflow.

The safe current use is source ownership:

- preserve the title and locator
- prevent the row from being reprocessed as an unknown reference
- make the row eligible for a later source-check or deep-extraction pass
- keep claims out of topic pages until the source text is actually read

## Key Findings

### quoted_fact

- 3 terminal feline patients with spontaneous head/neck tumors treated with BPA-BNCT
- BPA delivered boron values to tumor in therapeutically useful range
- No radiotoxic effects observed
- Partial tumor control: impaired growth and partial necrosis
- Improved clinical condition and prolonged survival beyond terminal state

### source_supported_conclusion

- BNCT is feasible and safe for spontaneous feline head/neck cancer
- Therapeutic boron concentrations achievable with BPA delivery
- Preclinical context; builds on hamster cheek pouch SCC model work

### llm_inference

- Investigational therapy; n=3 is too small for efficacy conclusions
- Historical interest for FOSCC experimental therapy landscape
- BNCT remains investigational; not standard of care for feline OSCC

## Claim-Fit Judgment

Strongest safe use:

- intake ownership
- source queue placement
- deduplication and future extraction planning

Must not control yet:

- reader-facing medical advice
- numeric claims
- comparative ranking
- guideline-like recommendations
- mechanism closure

## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate until labels are verified

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the cancer module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?

## Linked Entities

- diseases: cancer
- models:
- endpoints:
- mechanisms:
- regulations:
