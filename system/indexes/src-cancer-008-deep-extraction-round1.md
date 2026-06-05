---
id: src-cancer-008-deep-extraction-round1
type: system
topic: cancer
question_type: deep-extraction
source_ids: [src-cancer-008]
language: zh
last_compiled_at: 2026-05-30
verification_status: deep_extracted
decision_grade: no
owner: codex
status: active
---

# Deep Extraction Worksheet

Source: `src-cancer-008`  
Title: `The Histologic Classification of 602 Cases of Feline Lymphoproliferative Disease using the National Cancer Institute Working Formulation`  
Method note: local direct fetch of SAGE links returned HTTP 403 during availability probing, but the SAGE PDF was readable through the browser layer and was used for this worksheet.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This is a pathology classification anchor, not a treatment outcomes paper

- core_claim: the study classifies feline lymphoproliferative disease histologically using the National Cancer Institute Working Formulation.
- implicit_premise: lymphoma branch architecture should begin with pathology and topography, not treatment ranking.
- relation_to_previous: adds the first lymphoma / lymphoproliferative disease branch-control source after broad cancer architecture.
- hard_details: 688 admissions from 12 veterinary institutions were reviewed; 86 were excluded; 602 cases were used for analysis.
- tension_or_surprise: the source is large and branch-controlling, but it is mostly pre-1989 material and predates modern routine immunophenotyping.

#### Unit 2: The study supports low/intermediate/high grade architecture

- core_claim: the NCI Working Formulation gave a practical grade-based classification frame for feline lymphoma.
- implicit_premise: grade and morphology should remain visible in lymphoma synthesis before treatment or prognosis claims.
- relation_to_previous: converts the broad lymphoma branch from `src-cancer-004` into a pathology-controlled branch.
- hard_details: 69/602 cases were low-grade, 210/602 intermediate-grade, and 323/602 high-grade lymphomas.
- tension_or_surprise: more than half of analyzed cases were high-grade in this historical series.

#### Unit 3: Topography is not interchangeable with histologic subtype

- core_claim: diagnosis correlated with tumor topography, mitotic frequency, necrosis, sclerosis, and age.
- implicit_premise: lymphoma pages should separate anatomic site from histologic class.
- relation_to_previous: adds structure to future alimentary, mediastinal, multicentric, renal, cutaneous, and other lymphoma branches.
- hard_details: alimentary lymphomas were more often associated with lower mitotic categories, while mediastinal and renal lymphomas appeared more often in higher mitotic categories.
- tension_or_surprise: site-specific patterns exist, but they are not treatment protocols or prognosis estimates by themselves.

#### Unit 4: FeLV status is visible but incompletely measured

- core_claim: FeLV antigen status was collected, but was unknown or untested in most cases.
- implicit_premise: do not use this paper alone to make modern FeLV-era causal claims.
- relation_to_previous: links lymphoma to viral-history logic introduced by `src-cancer-004`.
- hard_details: FeLV antigen was positive in 84 cases, negative in 82, and unknown or untested in 522.
- tension_or_surprise: FeLV-positive cases were associated with higher mitotic categories, but the missingness limits generalization.

#### Unit 5: Alimentary lymphoma receives an early branch signal

- core_claim: primary alimentary lymphomas were common and often lower-grade/indolent compared with thoracic high-mitotic patterns.
- implicit_premise: alimentary lymphoma deserves its own later branch, but treatment claims require newer clinical sources.
- relation_to_previous: sharpens the GI-shift branch from `src-cancer-004`.
- hard_details: primary lymphomas in the alimentary tract numbered 164 cases in this study.
- tension_or_surprise: the paper gives a surgical-localization anecdote, but that should not become a general surgical recommendation.

## Phase 1: Theme Reconstruction

## Theme: Lymphoma needs pathology-first branch architecture

This source is useful because it prevents lymphoma from becoming one generic branch. It provides a large historical pathology base, grade grouping, topography correlations, and a bridge from NCI Working Formulation categories toward more pragmatic diagnostic groupings.

### Hard Information

- 602 analyzed feline lymphoproliferative disease cases
- 12 veterinary institutions contributed cases
- low-grade: 69 cases
- intermediate-grade: 210 cases
- high-grade: 323 cases
- topography and mitotic activity were key analytic dimensions

## Theme: Historical classification must be bounded against modern lymphoma work

The study predates broad routine immunophenotyping and uses mostly pre-1989 material. It is still valuable for morphology and topography architecture, but modern lymphoma pages should not stop here.

### Hard Information

- paraffin-embedded tissue was not generally available for the full archive
- immunophenotyping was not in general use for most home-institution cases
- FeLV status was unknown or untested in most cases

## Phase 2: Claim-Evidence Structure

### Lymphoma Branch Key Points

**Claim 1**
- support: the paper analyzed 602 feline lymphoproliferative disease cases with NCI Working Formulation categories.
- details: low/intermediate/high grade categories were tabulated and correlated with histologic and topographic variables.
- implicit_premise: lymphoma branch architecture should include morphology and grade before treatment discussion.

**Claim 2**
- support: the paper identified significant correlations among diagnosis, topography, mitotic frequency, necrosis, sclerosis, and age.
- details: alimentary lymphoma and mediastinal/renal patterns differed in mitotic-category associations.
- implicit_premise: anatomic lymphoma pages need pathology context.

### Boundary-Setting Key Points

**Claim 1**
- support: the material is historical and mostly pre-immunophenotyping.
- details: the authors used the WF system because the archive lacked broad paraffin-block and immunophenotype availability.
- implicit_premise: later lymphoma pages need newer immunophenotype and treatment outcome sources.

**Claim 2**
- support: FeLV data were largely missing.
- details: 522/688 admissions were unknown or untested for FeLV antigen status.
- implicit_premise: do not build modern FeLV lymphoma risk guidance from this source alone.

## Phase 2.5: Write-Back Implications

### For `topics/cancer/lymphoma.md`

- create lymphoma as an early branch.
- split branch structure by pathology/grade and topography.
- mark alimentary lymphoma as a high-priority future branch requiring newer clinical sources.

### For `system/indexes/cancer-source-index.md`

- `src-cancer-008` should be marked as a deep-extracted lymphoma pathology classification anchor.

### For `system/indexes/cancer-source-depth-map.md`

- this becomes the fifth cancer source with full deep-extraction status.

## Phase 3: Promotion Check

- source_card_updates:
  - promote `src-cancer-008` from `abstract_weighted` to `deep_extracted`
  - capture lymphoma pathology, topography, grade, mitosis, and FeLV-missingness boundaries
- topic_write_back_targets:
  - `topics/cancer/lymphoma.md`
  - `topics/cancer/index.md`
  - `topics/cancer/current-state-dashboard.md`
  - `topics/cancer/navigation.md`
  - `system/indexes/cancer-source-index.md`
  - `system/indexes/cancer-source-depth-map.md`
- not_safe_to_promote_yet:
  - treatment protocols
  - modern FeLV risk guidance
  - survival prediction
  - immunophenotype-based modern classification closure
  - surgical recommendations for alimentary lymphoma
- conflicts_with_existing_vault:
  - none detected; this source adds the first lymphoma-specific branch anchor
- new_entities_or_pages_justified:
  - lymphoma branch page
  - future alimentary lymphoma page
  - future FeLV/lymphoma boundary page after newer sources
