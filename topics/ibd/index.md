---
id: topic-ibd-index
type: topic
topic: ibd
species: feline
disease: IBD
question_type: overview
source_ids: [src-ibd-001, src-ibd-002, src-ibd-003, src-ibd-004, src-ibd-005, src-ibd-006, src-ibd-007, src-ibd-008, src-ibd-009, src-ibd-010, src-ibd-011, src-ibd-012, src-ibd-013, src-ibd-014, src-ibd-015, src-ibd-016, src-ibd-017, src-ibd-018, src-ibd-019, src-ibd-020, src-ibd-021, src-ibd-022, src-ibd-023, src-ibd-024]
last_compiled_at: 2026-04-23
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
owner: codex
status: active
---

# Feline IBD Topic Index

## Question This Page Answers

What is the first-pass internal map of feline inflammatory bowel disease across chronic enteropathy framing, microbiota, diagnosis, IBD-versus-lymphoma boundary, treatment, and related extension branches?

## Topic Pages

- [navigation](./navigation.md)
- [current-state-dashboard](./current-state-dashboard.md)
- [current-state-dashboard-bilingual](./current-state-dashboard-bilingual.md)
- [mechanism-overview](./mechanism-overview.md)
- [endpoint-handbook](./endpoint-handbook.md)
- [risk-and-recognition](./risk-and-recognition.md)
- [translation-brief](./translation-brief.md)
- [regulatory-brief](./regulatory-brief.md)
- [synthesis-index](./synthesis-index.md)
- [synthesis-index-bilingual](./synthesis-index-bilingual.md)

## Current Reusable Entities

- [Feline IBD](../../entities/diseases/ibd.md)
- [chronic enteropathy](../../entities/diseases/chronic-enteropathy.md)
- [small-cell alimentary lymphoma](../../entities/diseases/small-cell-alimentary-lymphoma.md)
- [FCEAI](../../entities/endpoints/fceai.md)
- [intestinal fibrosis](../../entities/endpoints/intestinal-fibrosis.md)
- [muscularis thickening](../../entities/endpoints/muscularis-thickening.md)
- [vitamin D](../../entities/endpoints/vitamin-d.md)
- [fecal S100A12](../../entities/endpoints/fecal-s100a12.md)
- [metabolomics](../../entities/endpoints/metabolomics.md)
- [hydrolysed diet response](../../entities/endpoints/hydrolysed-diet-response.md)

## Current Conclusions

Evidence-depth note: this page cites mixed-depth IBD sources, including
`abstract_weighted` extension/context cards. Treat those as cautious branch
orientation, not full-text or decision-grade proof.

### quoted_fact

- The current source set spans microbiota, clinicopathology, imaging, biopsy utility, biomarkers, fibrosis, diet response, and IBD-versus-lymphoma boundary work.
- The current IBD set also includes extension branches such as eosinophilic fibroplasia, granulomatous colitis, and cholangitis.

### source_supported_conclusion

- A first IBD seed corpus of `24` candidate sources has now been mapped into the vault.
- Feline IBD should be modeled inside a wider `chronic enteropathy` frame rather than as one perfectly clean standalone entity.
- The strongest early compile likely needs to keep `IBD`, `small-cell lymphoma boundary`, and `diagnostic-workup architecture` separate from the beginning.
- The current treatment branch is now real enough to anchor with `diet-first logic`, but it still remains thinner and more heterogeneous than the diagnostic and pathology branches.
- Fibrosis now belongs in the structural chronicity branch of the module, not in background pathology residue.
- The extension branches should remain outside the core idiopathic IBD spine.
- The current extension branch is now strong enough to compile, but it should remain an edge-of-module layer rather than a rewrite of the core spine.
- The first product-archetype layer now exists, and it makes later regulatory work safer by separating claim-fit from route-fit before any jurisdiction comparison.

### llm_inference

- IBD is a good third disease module because it stress-tests the system on `boundary disease`, not only on one disease with one biomarker story.
- The best early IBD compile will probably center on `workup architecture and disease-boundary compression`, not on one single mechanistic claim.
- The current top-level compile is now strong enough that the next gains should come from selective bilingual reuse, regulatory interpretation, and better compression of the already-built branches.

## Evidence Map

- broad review / chronic-enteropathy framing: `src-ibd-003`, `src-ibd-008`, `src-ibd-024`
- microbiota / mucosal mechanism branch: `src-ibd-001`, `src-ibd-006`, `src-ibd-019`, `src-ibd-022`
- disease-activity / endpoint branch: `src-ibd-004`, `src-ibd-013`, `src-ibd-017`
- imaging / biopsy / pathology workup branch: `src-ibd-010`, `src-ibd-012`, `src-ibd-015`
- IBD-versus-small-cell-lymphoma boundary: `src-ibd-001`, `src-ibd-002`, `src-ibd-007`, `src-ibd-010`, `src-ibd-011`, `src-ibd-013`, `src-ibd-015`, `src-ibd-016`, `src-ibd-019`
- treatment / translation branch: `src-ibd-005`, `src-ibd-014`, `src-ibd-021`
- fibrosis / chronicity branch: `src-ibd-022`, `src-ibd-018`

## Conflicts / Uncertainty

- The current IBD seed corpus is now source-card full across its core, treatment, extension, and workflow anchors.
- `src-ibd-009` is now deep-extracted with recovered methods, metrics, and label-set details; it can support pathology-report workflow normalization, but not claim-heavy clinical diagnosis.
- The module will need to avoid flattening `IBD`, `chronic enteropathy`, and `small-cell lymphoma` into one continuum too early.
- Several candidate markers may help with support or stratification without becoming lead diagnostic endpoints.

## Gaps

- no jurisdiction-specific regulatory strategy yet

## Next Sources To Read First

- no immediate must-read source remains inside the current seed corpus
