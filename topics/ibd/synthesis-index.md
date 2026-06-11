---
id: topic-ibd-synthesis-index
type: topic
topic: ibd
species: feline
disease: IBD
question_type: synthesis
source_ids: [src-ibd-001, src-ibd-002, src-ibd-003, src-ibd-004, src-ibd-005, src-ibd-006, src-ibd-007, src-ibd-008, src-ibd-009, src-ibd-010, src-ibd-011, src-ibd-012, src-ibd-013, src-ibd-014, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-018, src-ibd-019, src-ibd-020, src-ibd-021, src-ibd-022, src-ibd-023, src-ibd-024]
last_compiled_at: 2026-06-11
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Feline IBD Synthesis Index

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| IS1 | IBD synthesis should center diagnostic boundary compression and workup sequencing, not treatment ranking | B | src-ibd-003, src-ibd-010, src-ibd-011, src-ibd-015, src-ibd-016, src-ibd-019 | compiled synthesis |
| IS2 | Marker and frontier-omics branches add support but do not lead routine workup | B | src-ibd-004, src-ibd-013, src-ibd-017 | no one-marker workup claim |
| IS3 | Diet-first treatment logic is useful but remains inside chronic-enteropathy / food-response boundaries | B | src-ibd-014, src-ibd-021 | not idiopathic-IBD-specific efficacy |
| IS4 | `src-ibd-009` is deep-extracted workflow support for pathology-report normalization, not decision-grade diagnosis | C | src-ibd-009 | keep below biopsy, imaging, and pathologist interpretation |

## Quick Helpers

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)

## Current Synthesis Spine

- feline IBD currently sits inside a wider `chronic enteropathy` frame
- the first broad review anchor already frames feline IBD as a diagnosis of exclusion
- the first major compression problem is not treatment ranking but `IBD versus small-cell lymphoma` boundary handling
- `diagnostic workup`, `multimodal boundary`, `tissue-marker boundary`, and `support/frontier marker hierarchy` are now distinct compiled layers
- current marker-level evidence adds depth, but still does not support one-marker workup leadership
- muscularis thickening is lymphoma-leaning and ileal sampling can be diagnosis-changing, so the boundary is partly a sequencing and sampling problem rather than only a pathology-reading problem
- the practical boundary sequence is now: chronic-enteropathy suspicion -> imaging pressure -> biopsy-site strategy -> integrated pathology -> bounded marker support
- tissue-marker depth is now stratified: Bcl-2 is stronger than the shared COX-2 signal, but still not a stand-alone separator
- support-marker and frontier-marker branches are now distinct layers rather than one generic biomarker bucket
- vitamin D and fecal S100A12 now sit in the shared support-marker layer, while metabolomics is the strongest current frontier-separation signal without becoming routine-ready workup leadership
- clinicopathology, imaging, biopsy utility, and disease-activity indexing are currently more operationally important than frontier omics signals
- microbiota and fibrosis matter, but they currently deepen explanation, chronicity modeling, and boundary pressure more than they settle routine workup
- the fibrosis branch now has a concrete feline chronic-enteropathy anchor: `src-ibd-022` reports 65 client-owned cats and links intestinal fibrosis with lower body weight and serum albumin, so fibrosis should be read as burden/chronicity architecture rather than a minor histology footnote
- extension branches such as eosinophilic fibroplasia, granulomatous colitis, and cholangitis now help define the module edge without changing the core idiopathic IBD spine
- diet-first treatment logic is now the cleanest practical intervention anchor, but it still sits inside a mixed chronic-enteropathy and food-response frame
- the treatment layer is now also clearer as a branch-comparison problem: `direct practical anchor`, `broad overview context`, and `exploratory translational branch` are adjacent but not equivalent
- idiopathic-IBD immunopathology now gives the inflammatory side of the module its own depth without changing the exclusion-first workup order
- 24 of 24 IBD seed source cards are explicit full-depth cards; `src-ibd-009` now has recovered methods, label set, and classifier metrics, but should still stay in workflow-support territory rather than claim-heavy clinical diagnosis

## Best First Compiled Questions

- what should lead first-pass clinical suspicion in feline chronic enteropathy?
- how should the module separate IBD from low-grade or small-cell alimentary lymphoma?
- which markers belong to lead workup, support workup, or frontier stratification?
- how much practical treatment signal is already strong enough to compile without overclaim?
- how should fibrosis and idiopathic-pathology depth be integrated without flattening them into the same layer as activity or biomarkers?
- how should structural chronicity endpoints such as fibrosis be kept separate from support biomarkers and frontier class-separation markers?

## Current Working Hypothesis

IBD should become the first disease module where `diagnostic boundary compression and workup sequencing` are at least as important as `treatment compression`.

## What This Module Most Needs Next

1. treat dashboard / synthesis / unresolved state-sync as promoted, and shift the next batch to full-text / image-table / regulatory precision where branch order or output claims require it
2. keep the practical workup sequence explicit: clinical suspicion, imaging pressure, biopsy-site choice, histology / integrated pathology, then bounded marker support
3. keep diet-first management inside the mixed chronic-enteropathy and food-response frame rather than treating it as pure idiopathic-IBD certainty
4. keep fibrosis and extension-branch remodeling near chronicity / module-edge logic without flattening them into activity scoring, support biomarkers, or a ready treatment route

## Source-Card Depth State

- IBD source cards: `24/24` explicit `full` and `24/24` `deep_extracted`; `src-ibd-009` is workflow support, not decision-grade diagnosis
- IBD round-1 worksheets: `24/24`
- card-level map: [IBD source depth map](../../system/indexes/ibd-source-depth-map.md)
- remaining source-side work: biopsy-site tables, FCEAI component scoring, fibrosis detection-method tables, ultrasound thresholds, marker validation details, treatment claim-fit, and regulatory route-fit checks
