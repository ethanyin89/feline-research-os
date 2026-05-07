---
id: out-ibd-dossier-20260409-v1-working-en
type: output
output_kind: dossier
language: en
topic: ibd
question: "What is the first usable internal dossier for feline IBD across disease framing, workup, marker hierarchy, pathology depth, and early treatment?"
source_ids: [src-ibd-001, src-ibd-003, src-ibd-004, src-ibd-007, src-ibd-009, src-ibd-010, src-ibd-011, src-ibd-012, src-ibd-013, src-ibd-014, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-019, src-ibd-022]
generated_at: 2026-04-09
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-04-22 checked for wording drift; working-English dossier layer only, not decision-grade diagnostic or treatment guidance."
owner: codex
status: draft
evidence_policy:
  quoted_fact: []
  source_supported_conclusion: []
  llm_inference: []
---

# Feline IBD Internal Dossier V1

## User Question

What is the first usable internal dossier for feline IBD across disease framing, workup, marker hierarchy, pathology depth, and early treatment?

## Executive Answer

Based on the current seed corpus, feline IBD is now usable as an internal research object, but only if it is modeled with the right architecture.

The module should currently be framed inside `feline chronic enteropathy`, not as an isolated, perfectly self-contained disease. The strongest current organizing logic is:

- diagnosis of exclusion
- IBD-versus-small-cell-lymphoma boundary handling
- activity versus identity separation
- marker hierarchy instead of biomarker flattening
- diet-first but bounded treatment framing

The most important practical consequence is that the system should not ask, “Which biomarker diagnoses IBD?” The better question is, “Which combination of workup layers most defensibly distinguishes inflammatory chronic enteropathy from nearby disease states?”

This file is the working-English dossier. It should not be mistaken for a bilingual or Chinese-facing dossier. The paired `-en` and `-zh` files, if created later, will be derivative language-facing outputs built on top of this working layer.

## Disease Framing

### quoted_fact

- Broad review material states that feline IBD is a diagnosis of exclusion.
- Dietary intolerance or allergy and well-differentiated alimentary lymphosarcoma can mimic IBD clinically and histologically.
- Later chronic-enteropathy studies continue to use the wider chronic-enteropathy frame rather than a narrow one-marker IBD frame.

### source_supported_conclusion

- The disease object should currently be stored as `IBD within chronic enteropathy`, not as a clean standalone syndrome.
- The system should preserve both `idiopathic IBD depth` and `boundary disease pressure` at the same time.

### llm_inference

- IBD is valuable for the research OS because it forces the system to distinguish `activity`, `pathology`, `boundary`, and `treatment` rather than storing one averaged disease summary.

## Workup Layer

### quoted_fact

- FCEAI combines clinical signs, endoscopic abnormalities, serum total protein, ALT or ALP activity, and serum phosphorus concentration.
- FCEAI scores decrease with positive treatment response.
- Paired duodenal and ileal biopsy study found poor agreement between sites.
- Some small-cell lymphoma diagnoses were made only in ileal specimens.
- Muscularis thickening on ultrasound is more strongly associated with lymphoma than with IBD.

### source_supported_conclusion

- `FCEAI` belongs to activity and response tracking, not to disease-class discrimination.
- `Biopsy-site selection` belongs in the core workup branch.
- `Muscularis thickening` is a meaningful suspicion-shaping signal, but should not outrank tissue diagnosis.

### llm_inference

- The workup architecture is already strong enough to support a formal future `IBD workup protocol` page if needed.

## Boundary Layer

### quoted_fact

- Microbiota differences exist between IBD and small-cell lymphoma.
- COX-2 mRNA does not cleanly separate IBD from low-grade alimentary lymphoma.
- Epithelial COX-2 immunoexpression is increased in both IBD and lymphoma relative to controls.
- Bcl-2 expression is higher in lymphoma than in IBD, but remains substantially positive in both groups.
- Metabolomics shows the strongest current frontier separation signal, including discriminatory power from polyunsaturated fatty acids.

### source_supported_conclusion

- The boundary branch is now clearly `multimodal`.
- Tissue and molecular markers add boundary pressure, but none currently justify one-marker workup leadership.
- `Metabolomics` is the strongest current frontier-separation branch, but it remains below routine-ready status.

### llm_inference

- The next useful boundary densification may come from integrating frontier markers with biopsy-site and imaging logic rather than deepening isolated marker pages one by one.

## Pathology And Chronicity Layer

### quoted_fact

- Idiopathic-IBD immunopathology study reports higher TNF-alpha, IL-1beta, IL-12, and CD3-positive expression in IBD than controls.
- The same study also states that feline IBD cannot be diagnosed only through histologic findings.
- Fibrosis study reports frequent fibrosis in chronic inflammatory enteropathy and association with lower body weight and lower albumin.

### source_supported_conclusion

- `Idiopathic IBD` now has its own pathology-depth branch.
- `Fibrosis` should be treated as structural chronicity and burden, not as background histology.
- Pathology depth should remain subordinate to exclusion-first workup for practical diagnosis.

### llm_inference

- Structural chronicity may become one of the more reusable cross-disease concepts in later feline GI modules.

## Marker Hierarchy

### quoted_fact

- Vitamin D is reduced in cats with IBD or small-cell lymphoma compared with healthy and nongastrointestinal ill controls.
- Fecal S100A12 is elevated in disease versus health, but does not separate IBD from lymphoma.
- Metabolomics offers stronger separation than either vitamin D or fecal S100A12.

### source_supported_conclusion

- `Vitamin D` belongs to a burden or complication-context layer.
- `Fecal S100A12` belongs to a noninvasive disease-versus-health support layer.
- `Metabolomics` belongs to a frontier separation layer.

### llm_inference

- Later outputs should avoid generic “biomarker summary” language and instead preserve this hierarchy explicitly.

## Early Treatment Layer

### quoted_fact

- Hydrolysed diet as sole therapy produced rapid clinical improvement in a small chronic-enteropathy cohort.
- Clinical relapse after re-challenge and response after reintroduction support true diet sensitivity in at least part of that group.

### source_supported_conclusion

- `Hydrolysed diet response` is the cleanest current direct treatment anchor.
- The best current practical treatment frame is `diet-first chronic-enteropathy management`.
- Current treatment evidence does not yet justify strong idiopathic-IBD-specific efficacy language.

### llm_inference

- Before any later treatment ranking page is built, the system should first separate `food-responsive overlap` from stricter idiopathic-IBD logic more cleanly.

## Uncertainty / Limits

- Several relevant sources remain ingested but not yet deep-extracted.
- The current dossier still rests mostly on abstract-checked extraction rather than line-by-line full-text review.
- No jurisdiction-specific regulatory layer exists yet for IBD.
- Output-facing English exists now, but derivative `-en` and `-zh` layers do not yet exist.

## Suggested Write-Back Targets

- `topics/ibd/index.md`
- `topics/ibd/current-state-dashboard.md`
- `topics/ibd/mechanism-overview.md`
- `topics/ibd/endpoint-handbook.md`
- `topics/ibd/translation-brief.md`
- `topics/ibd/synthesis-index.md`
