---
id: topic-ckd-index
type: topic
topic: ckd
species: feline
disease: CKD
question_type: overview
source_ids: [src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-005, src-ckd-006, src-ckd-007, src-ckd-008, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-012, src-ckd-013, src-ckd-014, src-ckd-015, src-ckd-016, src-ckd-017, src-ckd-018, src-ckd-019, src-ckd-020, src-ckd-021, src-ckd-022, src-ckd-023, src-ckd-024, src-ckd-026, src-ckd-027, src-ckd-029, src-ckd-030, src-ckd-034, src-ckd-050, src-ckd-051, src-ckd-053, src-ckd-054]
last_compiled_at: 2026-06-11
confidence: high
verification_status: compiled
decision_grade: yes
language_qa_status: light_checked
language_qa_notes: "2026-06-11 expanded to 33 sources including FGF-23 biomarker (src-ckd-026), gut-uremic toxins (src-ckd-027), phosphate binders (src-ckd-029), and TGF-beta fibrosis (src-ckd-050)."
owner: codex
status: active
---

# Feline CKD Topic Index

## Question This Page Answers

What is the current internal map of feline CKD across mechanism, model, translation, and regulatory layers?

## Topic Pages

- [navigation](./navigation.md)
- [mechanism-overview](./mechanism-overview.md)
- [model-map](./model-map.md)
- [model-summary](./model-summary.md)
- [endpoint-handbook](./endpoint-handbook.md)
- [pathology-correlations](./pathology-correlations.md)
- [early-detection](./early-detection.md)
- [risk-and-recognition](./risk-and-recognition.md)
- [hypertension-and-comorbidity](./hypertension-and-comorbidity.md)
- [translation-brief](./translation-brief.md)
- [regulatory-brief](./regulatory-brief.md)

## Current Conclusions

### quoted_fact

- CKD is the first disease selected for V1 system build.
- Current seed corpus now includes guideline, review, and primary-study material spanning mechanism, diagnosis, therapy, fibrosis, hypertension, risk-factor recognition, biomarker studies, and experimental-model material.
- The CKD corpus now also includes newer CKD-MBD, metabolomic early-detection, comorbidity-interpretation, imaging-workup, practice-pattern, and aging-senescence sources.

### source_supported_conclusion

- Initial CKD seed corpus is in place and the first compiled evidence map now supports a usable V1 topic structure.
- Renal fibrosis is the clearest current mechanism backbone for feline CKD in this corpus.
- Core first-wave CKD endpoints should include creatinine, USG, UPCR or proteinuria, systolic blood pressure, phosphorus, and SDMA.
- Hypertension is not a side issue in feline CKD, it is part of the core disease-management and progression picture.
- Treatment content in this corpus supports renal diet most clearly, while several other commonly used interventions need explicit evidence-strength labeling.
- Imaging and practice-pattern layers are now explicit enough to support more realistic workup and implementation framing.

### llm_inference

- CKD is likely a strong first wedge because it naturally touches all four system layers.
- Early detection is now strong enough to stand as its own compiled subpage, but still not strong enough to be treated as solved.
- Risk and recognition logic is now strong enough to justify a separate page, especially around older/high-risk cats and owner-observed polyuria/polydipsia.
- Hypertension and proteinuria now justify their own CKD comorbidity page because they materially change interpretation and management.
- Pathology-correlation logic is now strong enough to stand alone, especially around fibrosis, proteinuria, phosphorus, anaemia, and blood pressure.

## Evidence Map

- mechanism-heavy sources: src-ckd-001, src-ckd-010, src-ckd-011, src-ckd-012, src-ckd-016, src-ckd-050
- CKD-MBD / mineral branch: src-ckd-015, src-ckd-026 (FGF-23), src-ckd-029 (phosphate binders)
- microbiome-kidney axis: src-ckd-027 (gut-uremic toxins: indoxyl sulfate, p-cresyl sulfate, TMAO)
- endpoint / diagnosis sources: src-ckd-002, src-ckd-004
- therapy / translation sources: src-ckd-003, src-ckd-005, src-ckd-006, src-ckd-007, src-ckd-008, src-ckd-009
- early recognition / symptom signal: src-ckd-012
- fibrosis pathway: src-ckd-050 (TGF-beta), src-ckd-051, src-ckd-053, src-ckd-054
- senescence / aging: src-ckd-022, src-ckd-023

## Conflicts / Uncertainty

- exact role of SDMA within the first-pass endpoint hierarchy still needs fuller extraction
- regulatory comparison depth is still not established
- many treatment claims still need explicit evidence-strength ranking
- the main remaining gaps are no longer about ingest only, but about intervention ranking and product-specific regulatory precision

## Gaps

- no dedicated owner-observed symptom entity layer yet
- no dedicated hypertension-treatment decision note yet
- no dedicated lesion entity layer yet beyond fibrosis-centered summaries

## Next Sources To Ingest

- higher-density feline CKD treatment primary studies
- stronger natural-history / longitudinal observational studies
- deeper intervention-response studies
- China veterinary registration source
- FDA CVM renal indication source

## Reading Priority

Round 1 reading plan:

- [ckd-reading-plan-round-1](../../system/indexes/ckd-reading-plan-round-1.md)
- [ckd-deep-read-checklists-round-1](../../system/indexes/ckd-deep-read-checklists-round-1.md)

Tier A read-first sources:

- src-ckd-004
- src-ckd-001
- src-ckd-002
- src-ckd-003
- src-ckd-010

## First-Pass CKD Map

### Mechanism Backbone

- renal fibrosis / tubulointerstitial fibrosis
- glomerulosclerosis
- progression-linked variables: proteinuria, phosphorus, blood pressure

### Core Endpoints

- creatinine
- USG
- UPCR or proteinuria
- systolic blood pressure
- phosphorus
- SDMA

### Important Context Endpoints

- anaemia
- potassium
- PTH
- appetite or uraemic clinical signs

### Translation Baseline

- renal diet has the clearest support in the current seed set
- several adjunct treatments are used despite weaker or mixed evidence
- hypertension management is central, not optional

## Evidence-Depth Caveat

This page cites abstract-weighted and title-only sources (such as src-ckd-051, src-ckd-053, and src-ckd-054) for extended pathogenetic and staging context. These details do not provide clinical or veterinary medical guidance and should be verified against full-text source files for high-priority clinical decisions.
