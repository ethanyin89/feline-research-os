---
id: out-hcm-dossier-20260410-v1-working-en
type: output
output_kind: dossier
language: en
topic: hcm
question: "What is the first usable internal dossier for feline HCM across disease framing, recognition, endpoint hierarchy, genotype pressure, remodeling depth, and treatment-regulatory boundary?"
source_ids: [src-hcm-001, src-hcm-004, src-hcm-006, src-hcm-007, src-hcm-008, src-hcm-009, src-hcm-010, src-hcm-012, src-hcm-013, src-hcm-015, src-hcm-020, src-hcm-024]
generated_at: 2026-04-10
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

# Feline HCM Internal Dossier V1

## User Question

What is the first usable internal dossier for feline HCM across disease framing, recognition, endpoint hierarchy, genotype pressure, remodeling depth, and treatment-regulatory boundary?

## Executive Answer

Based on the current seed corpus, feline HCM is now usable as an internal research object, but only if it is modeled with the correct hierarchy.

The disease should currently be framed as a `structure-first cardiomyopathy module`, not as a biomarker-led or mutation-only object. The strongest current organizing logic is:

- phenotype confirmation before biomarker enthusiasm
- endpoint hierarchy instead of marker flattening
- genotype pressure without genotype determinism
- remodeling depth beneath visible hypertrophy
- treatment reality constrained by explicit evidence skepticism
- regulatory boundary held back until product type and route fit are clearer

The most important practical consequence is that the system should not ask, “Which single marker diagnoses HCM?” The better question is, “Which combination of structural, biomarker, genotype, and remodeling layers best supports phenotype definition and severity interpretation without overclaiming treatment or route readiness?”

This file is the working-English dossier. It should not be mistaken for a bilingual or Chinese-facing dossier. Paired `-en` and `-zh` files, if created later, are derivative language-facing outputs built on top of this working layer.

## Disease Framing

### quoted_fact

- Broad feline cardiomyopathy and HCM review material supports HCM as one phenotype inside a wider feline cardiomyopathy frame.
- Echocardiographic work reports structurally heterogeneous spontaneous feline HCM rather than one uniform phenotype.
- Comparative framing papers position feline HCM as a spontaneous large-animal model of human HCM.

### source_supported_conclusion

- HCM should be stored as a `core hypertrophic phenotype spine` inside a broader feline cardiomyopathy frame.
- The system should preserve both `HCM core architecture` and `non-HCM cardiomyopathy boundary pressure`.
- Cross-species model relevance belongs in the disease object, but should not replace feline-specific phenotype logic.

### llm_inference

- HCM is valuable for the research OS because it forces the system to integrate recognition, genotype pressure, remodeling, and translational caution in one map rather than one averaged disease summary.

## Recognition And Workup Layer

### quoted_fact

- Echocardiographic assessment shows feline HCM as structurally heterogeneous rather than uniform.
- Morphometry work supports measurable structural phenotype discrimination.
- NT-proBNP screening work fails to reliably screen mild-to-moderate or equivocal HCM in the studied colony.

### source_supported_conclusion

- `Structural confirmation` should remain the lead branch for HCM recognition.
- `Biomarkers` belong below phenotype definition and should not outrank imaging or gross morphometry.
- `Screening augmentation` and `phenotype confirmation` should remain separated in the workup architecture.

### llm_inference

- The recognition layer is already strong enough to support a future more explicit HCM workup protocol page if needed.

## Endpoint Layer

### quoted_fact

- Troponin-I is higher in moderate-to-severe HCM and even higher with active congestive heart failure.
- NT-proBNP has stronger severe-disease signal than mild-disease screening performance.
- Pathology staging and phenotype-depth papers suggest severity is layered rather than one-dimensional.

### source_supported_conclusion

- The endpoint hierarchy should currently be organized into:
  - structural confirmation
  - screening augmentation
  - injury or severity pressure
  - pathology-depth context
- `Troponin I` and `NT-proBNP` should not be treated as interchangeable HCM endpoints.
- Pathology-depth and late-stage remodeling belong in endpoint architecture because they shape severity interpretation.

### llm_inference

- A later HCM endpoint matrix will likely need explicit use-case labeling rather than one global ranking.

## Genotype-Severity Layer

### quoted_fact

- Genetics-focused clinical work reports stronger severity and penetrance pressure in homozygous MYBPC3-mutant cats than in heterozygous cats.
- Genetics review material supports a broader inherited HCM frame rather than a one-mutation story.

### source_supported_conclusion

- The genotype branch should remain `stratified`, not binary.
- `Mutation dosage` and `age-related penetrance` already matter enough to shape the compiled HCM map.
- Genotype should deepen severity interpretation rather than replace phenotype confirmation.

### llm_inference

- HCM is likely to remain one of the clearest modules where genotype pressure matters structurally but does not justify phenotype-only shortcutting.

## Phenotype And Remodeling Depth

### quoted_fact

- Remodeling-focused work supports cardiomyocyte-initiated and macrophage-driven remodeling processes.
- Anatomopathological staging work supports end-stage HCM as a broader remodeled phenotype rather than just more hypertrophy.

### source_supported_conclusion

- `Remodeling` should be a real branch beneath phenotype, not a side note beneath wall-thickening.
- `Fibrosis` and remodeled late-stage structure deepen phenotype interpretation rather than replacing it.
- End-stage HCM should be modeled as deeper structural change rather than simple extension of hypertrophy alone.

### llm_inference

- Remodeling may become the most reusable bridge concept between mechanism and severity depth in later cardiomyopathy work.

## Treatment And Regulatory Boundary

### quoted_fact

- A 2025 review frames feline HCM treatment around controlling clinical signs, slowing progression, and improving quality and life expectancy.
- The seed corpus contains both targeted-therapy work and a paper explicitly questioning whether feline HCM treatment is based more on science or faith.

### source_supported_conclusion

- The current treatment layer should be framed as `real but overclaim-sensitive`.
- The safest current treatment architecture is `bounded management + selective targeted frontier`.
- Current HCM evidence can support translation mapping much earlier than route-level regulatory analysis.
- The regulatory layer should remain a boundary page until product type, assay-versus-drug distinction, and route fit are clearer.
- The current HCM topic layer has no HCM-specific regulatory source pack yet.

### llm_inference

- HCM may later require separate regulatory archetypes for drug-like products, biomarker assays, and device-like or imaging-linked branches before any jurisdiction comparison is serious.

## Uncertainty / Limits

- The current HCM seed corpus contains 24 mapped sources, and all 24 paper cards now have round-1 deep extraction coverage; this dossier still is not full-text line-by-line review or decision-grade guidance.
- The dossier is still built mostly on first-round compiled extraction rather than line-by-line full-text review of the whole corpus.
- Treatment hierarchy remains thinner than recognition and phenotype architecture.
- AI and frontier-marker branches are present but still below first-line authority.
- No HCM-specific regulatory source pack exists yet.

## Suggested Write-Back Targets

- `topics/hcm/index.md`
- `topics/hcm/current-state-dashboard.md`
- `topics/hcm/mechanism-overview.md`
- `topics/hcm/endpoint-handbook.md`
- `topics/hcm/risk-and-recognition.md`
- `topics/hcm/translation-brief.md`
- `topics/hcm/synthesis-index.md`
