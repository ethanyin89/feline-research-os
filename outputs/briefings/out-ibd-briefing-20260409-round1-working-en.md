---
id: out-ibd-briefing-20260409-round1-working-en
type: output
output_kind: briefing
language: en
topic: ibd
question: "Based on the current seed corpus, what is the first usable internal view of feline IBD across workup, disease-boundary, markers, and early treatment?"
source_ids: [src-ibd-001, src-ibd-003, src-ibd-004, src-ibd-007, src-ibd-009, src-ibd-010, src-ibd-011, src-ibd-012, src-ibd-013, src-ibd-014, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-019, src-ibd-022]
generated_at: 2026-04-09
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-04-22 checked for wording drift; working-English layer only, not decision-grade diagnostic or treatment guidance."
owner: codex
status: draft
evidence_policy:
  quoted_fact: []
  source_supported_conclusion: []
  llm_inference: []
---

# Internal Briefing: Feline IBD Round 1

## User Question

Based on the current seed corpus, what is the first usable internal view of feline IBD across workup, disease-boundary, markers, and early treatment?

## Executive Answer

Current evidence supports treating feline IBD inside a wider `chronic enteropathy` frame, not as a one-test, one-marker, or one-diagnosis object.

The strongest current architectural conclusion is that feline IBD should be modeled through `diagnosis of exclusion` plus a persistent `IBD-versus-small-cell-lymphoma boundary` problem.

That boundary is not solved by one layer alone. In the current corpus it is shaped by:

- clinical activity logic through `FCEAI`
- imaging support, especially `muscularis thickening`
- biopsy-site strategy, especially `duodenum versus ileum`
- tissue-marker and molecular-marker pressure
- frontier metabolomic separation work

The current corpus also says three other operational things clearly.

First, `FCEAI` is useful, but it belongs to chronic-enteropathy activity and response tracking, not to disease-class separation.

Second, `fibrosis` is now strong enough to be treated as a structural chronicity branch, not as background histology.

Third, the treatment branch is still thinner than the diagnostic branch, but `hydrolysed diet response` is now the clearest early practical anchor. Even so, that anchor still overlaps with food-responsive disease and should not be flattened into idiopathic-IBD-specific proof.

This file is the working-English briefing. It should not be mistaken for a bilingual or Chinese-facing summary. Paired `-en` and `-zh` files, if created later, will be derivative language-facing outputs built on top of this working layer.

## Evidence-Backed Points

### quoted_fact

- Broad review material frames feline IBD as a diagnosis of exclusion.
- The same review notes that dietary intolerance or allergy and well-differentiated alimentary lymphosarcoma can mimic IBD clinically and histologically.
- The FCEAI study reports a multivariable chronic-enteropathy activity index that tracks response to treatment.
- The duodenal and ileal biopsy study reports poor agreement between sites and shows that some small-cell lymphoma cases are identified only in the ileum.
- The ultrasound study reports that muscularis propria thickening is more strongly associated with lymphoma than with IBD.
- The metabolomic study reports discriminatory signal between IBD and small-cell lymphoma, especially among polyunsaturated fatty acids, but only at a frontier-research level.
- The vitamin D and fecal S100A12 studies both report disease-associated abnormality without clean separation between IBD and lymphoma.
- The fibrosis study reports that intestinal fibrosis is common in feline chronic inflammatory enteropathy and is associated with lower body weight and lower albumin.
- The hydrolysed-diet study reports rapid clinical improvement in a small chronic-enteropathy cohort treated with diet as sole therapy.

### source_supported_conclusion

- The primary organizing principle for the current IBD module should be `exclusion-first workup`, not biomarker-first diagnosis.
- `Small-cell alimentary lymphoma` should be treated as a core boundary branch inside the IBD module, not as a remote differential.
- `FCEAI` should be used as an activity-and-response endpoint, not as a discriminator between inflammatory and neoplastic disease.
- `Muscularis thickening` is a lymphoma-leaning imaging signal, but it is not a stand-alone diagnosis.
- `Biopsy-site choice` is part of the diagnosis, not just part of the procedure.
- `Vitamin D` and `fecal S100A12` belong in support-marker layers, while `metabolomics` belongs in a stronger but still non-routine frontier layer.
- `Fibrosis` should be modeled as a structural chronicity branch above support markers and below treatment-route thinking.
- `Hydrolysed diet response` is the cleanest current early treatment anchor, but it must stay inside a mixed chronic-enteropathy and food-response frame.

### llm_inference

- The best next compiled milestone is probably an IBD output matrix that separates:
  1. workup-leading layers
  2. boundary-pressure layers
  3. support-marker layers
  4. frontier-marker layers
  5. early treatment anchors
- The current IBD module is now strong enough to support outward-facing internal outputs, but not yet strong enough for strong treatment-hierarchy claims.

## Uncertainty / Limits

- This briefing is built from first-round extraction, not full-text line-by-line review of every paper.
- All 24 IBD paper cards are now deep-extracted; `src-ibd-009` adds pathology-report workflow support but remains non-decision-grade.
- Treatment evidence remains much thinner than diagnostic and pathology evidence.
- The entity layer is growing, but it is still incomplete.
- This briefing should not be used as a submission-grade or guideline-grade decision document.

## Suggested Write-Back Targets

- `topics/ibd/index.md`
- `topics/ibd/mechanism-overview.md`
- `topics/ibd/endpoint-handbook.md`
- `topics/ibd/risk-and-recognition.md`
- `topics/ibd/translation-brief.md`
- `topics/ibd/synthesis-index.md`

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `partly`
- smallest durable home: `topic update + synthesis update; stay chat-only for any stronger treatment wording`

### Reason

- what is repeating:
  the same IBD questions keep converging on exclusion-first workup, lymphoma boundary, marker hierarchy, and diet-first early treatment framing
- what becomes clearer:
  this briefing compresses the module into reusable architecture instead of isolated paper summaries
- what is still too thin, if anything:
  treatment hierarchy remains thinner than diagnostic architecture, so stronger intervention claims should not be promoted from this output alone

### Decision

- promote selected structure only; hold stronger treatment claims

## Source IDs

- src-ibd-001
- src-ibd-003
- src-ibd-004
- src-ibd-007
- src-ibd-010
- src-ibd-011
- src-ibd-012
- src-ibd-013
- src-ibd-014
- src-ibd-015
- src-ibd-016
- src-ibd-017
- src-ibd-019
- src-ibd-022
