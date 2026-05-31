---
id: topic-cancer-registry-and-prevalence
type: topic
topic: cancer
species: feline
disease: cancer
question_type: synthesis
source_ids: [src-cancer-002, src-cancer-007]
last_compiled_at: 2026-05-30
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: not_checked
owner: codex
status: active
---

# Registry And Prevalence

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| RP1 | Registry and prevalence claims must state the denominator before using numeric tumor-frequency language | B | src-cancer-002 | pathology registry proportions, not population incidence |
| RP2 | Tumor type and anatomic location should both shape cancer navigation | B | src-cancer-002 | branch priority, not clinical ranking |
| RP3 | Regional comparator sources may change tumor-mix expectations, but blocked full text cannot control synthesis yet | C | src-cancer-007 | abstract-weighted only |

## Current Synthesis

`src-cancer-002` is the controlling source for registry denominator discipline. It uses the Swiss Feline Cancer Registry, spanning 1965-2008, with 51,322 feline patient records and 18,375 tumours. Because Switzerland lacked obligatory cat registration, the paper used proportional calculations. That boundary must travel with any frequency statement.

The safe reuse is structural:

- label numbers as registry or pathology-submission proportions
- keep tumor type and anatomic site as separate axes
- use registry prominence to prioritize branch extraction
- keep time trends as hypothesis-generating until branch-specific sources verify mechanism

## South Africa Comparator Lead

`src-cancer-007` is important but not yet deep-extracted. The publisher abstract identifies a South African hospital-admissions dataset from 1998-2005 and reports a high squamous cell carcinoma share. Because direct PDF access was not verified in this run, the source can guide the reading queue but should not control topic-page claims.

## Boundaries

- Do not convert registry proportions into population incidence.
- Do not merge Swiss pathology registry data with South African hospital-admissions data as one pooled prevalence estimate.
- Do not present fibrosarcoma time trends as vaccine causality without FISS-specific sources.
- Do not present lymphoma time trends as FeLV causality without FeLV / lymphoma sources.
- Do not rank treatments, prognosis, or diagnostic pathways from registry frequency data.

## Next Sources Needed

- the paired Swiss registry overview paper for occurrence of tumours in cats in Switzerland
- FISS-specific epidemiology / pathology source
- FeLV-era lymphoma source
- full-text readable copy of the South Africa prevalence article
