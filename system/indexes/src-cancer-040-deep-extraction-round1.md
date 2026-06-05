---
id: src-cancer-040-deep-extraction-round1
type: system
topic: cancer
question_type: deep-extraction
source_ids: [src-cancer-040]
language: zh
last_compiled_at: 2026-05-30
verification_status: deep_extracted
decision_grade: no
owner: codex
status: active
---

# Deep Extraction Worksheet

Source: `src-cancer-040`  
Title: `Cats with Cancer: Where to start`  
Method note: direct local fetch of SAGE XML returned a browser/challenge page, but the SAGE full article page was readable through the browser layer and was used for this worksheet.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This is a practitioner orientation article, not a tumor-specific guideline

- core_claim: the article provides a starting framework for approaching cats with cancer across presentation, diagnosis, staging, and treatment modalities.
- implicit_premise: broad orientation should become workflow architecture, not disease-specific treatment rules.
- relation_to_previous: complements the molecular, mammary, and biomarker deep extractions with a practical clinical workflow source.
- hard_details: the article is aimed at veterinary practitioners; it frames itself as an overview and starting point for a special issue on feline oncology.
- tension_or_surprise: it is clinically practical, but deliberately broad, so it should not outrank tumor-specific sources.

#### Unit 2: The first reusable branch is presentation and differential diagnosis

- core_claim: cancer in cats can present as mass lesions or non-specific signs, and neoplasia should remain a differential across many clinical presentations.
- implicit_premise: owner-facing navigation should avoid implying that cancer always appears as an obvious lump.
- relation_to_previous: gives the cancer module a front-door triage frame.
- hard_details: the article lists common tumor families and differentials, including lymphoma, squamous cell carcinoma, mammary carcinoma, soft tissue sarcoma, mast cell tumor, and primary lung tumors.
- tension_or_surprise: several clinical signs overlap with inflammatory, infectious, endocrine, renal, or other non-neoplastic conditions.

#### Unit 3: Diagnosis requires sampling, and sampling choice affects future treatment

- core_claim: cytology and histopathology have complementary roles, but histopathology remains the stronger definitive route for many tumors.
- implicit_premise: the module should distinguish "suspect cancer" from "confirmed tumor type."
- relation_to_previous: supplies a diagnostic workflow layer.
- hard_details: the article discusses cytology, biopsy, incisional biopsy, excisional biopsy, and special pitfalls for lymph nodes, oral masses, nasal tumors, intestinal disease, mammary tumors, and soft tissue sarcomas.
- tension_or_surprise: inappropriate excisional biopsy can compromise later definitive treatment, especially for soft tissue sarcoma.

#### Unit 4: Staging is decision infrastructure, not a decorative step

- core_claim: staging assesses primary tumor extent, regional nodes, and distant metastasis to inform clinical decisions.
- implicit_premise: branch pages should separate diagnosis from staging and should not skip staging before treatment discussion.
- relation_to_previous: links the broad workflow to treatment boundaries.
- hard_details: the article discusses lymph node evaluation, thoracic radiographs, abdominal ultrasound, advanced imaging, and blood tests; it notes that cat pulmonary metastases may not look like classic canine "cannon ball" metastases.
- tension_or_surprise: diagnostic test selection should consider both information value and downstream management cost.

#### Unit 5: Treatment modality summaries must stay conditional

- core_claim: surgery, radiotherapy, and chemotherapy have different roles depending on disease extent and tumor biology.
- implicit_premise: the module should not produce one-size-fits-all treatment ranking.
- relation_to_previous: provides the practical treatment-shell boundary that `src-cancer-004` and `src-cancer-003` deliberately lacked.
- hard_details: surgery is framed as a mainstay for solid tumors; chemotherapy is framed for disseminated or high-metastatic-risk disease; radiotherapy and chemotherapy are described as evolving areas in feline medicine.
- tension_or_surprise: the article provides concrete examples, but repeatedly keeps treatment decisions tied to tumor type, stage, feasibility, and patient/owner constraints.

## Phase 1: Theme Reconstruction

## Theme: Cancer module should begin with workflow, not treatment lists

This source is valuable because it gives a high-level clinical workflow: presentation, diagnosis, staging, then treatment considerations. It is the first deep-extracted source that can organize the reader journey before branch-specific disease pages are written.

### Hard Information

- practitioner-oriented review
- sections include clinical signs, diagnosis, staging, and treatment options
- covers common feline tumor families and differentials
- emphasizes limited evidence base for many feline tumors

## Theme: Diagnosis and staging protect against premature advice

The article repeatedly shows that clinical suspicion, tumor typing, and staging are separate steps. This supports the vault rule that owner-facing content should not jump from a symptom or mass to a treatment recommendation.

### Hard Information

- cytology and biopsy are both discussed
- histopathology remains important for definitive classification
- clinical staging includes tumor extent, nodes, and distant metastasis
- imaging and sampling choices depend on tumor site and management implications

## Phase 2: Claim-Evidence Structure

### Workflow Key Points

**Claim 1**
- support: the article is explicitly written as a starting point for general feline oncology practice.
- details: it introduces presentation, diagnosis, staging, and treatment considerations.
- implicit_premise: the cancer module needs a general workflow shell before tumor-specific recommendations.

**Claim 2**
- support: the article's key points emphasize cancer as a differential and the importance of diagnosis/staging.
- details: non-specific signs and mass lesions both appear in the clinical frame.
- implicit_premise: reader-facing pages should encourage veterinary evaluation, not remote diagnosis.

### Boundary-Setting Key Points

**Claim 1**
- support: treatment modalities are described conditionally.
- details: local therapies for local disease, chemotherapy for disseminated or high-risk microscopic disease, radiotherapy as an evolving option.
- implicit_premise: treatment lists should be gated by diagnosis, stage, tumor family, and individual case constraints.

**Claim 2**
- support: the article warns that inappropriate excisional biopsy can jeopardize future treatment.
- details: soft tissue sarcoma is the most explicit high-risk example.
- implicit_premise: diagnostic-procedure content needs strong "do not self-manage" and referral boundaries.

## Phase 2.5: Write-Back Implications

### For `topics/cancer/index.md`

- add a workflow layer: presentation -> diagnosis -> staging -> branch-specific treatment discussion.
- keep broad treatment modality descriptions below diagnosis and staging gates.

### For `system/indexes/cancer-source-index.md`

- `src-cancer-040` should be marked as a deep-extracted practitioner workflow anchor.

### For `system/indexes/cancer-source-depth-map.md`

- this becomes the fourth cancer source with full deep-extraction status.

## Phase 3: Promotion Check

- source_card_updates:
  - promote `src-cancer-040` from `abstract_weighted` to `deep_extracted`
  - capture presentation, diagnosis, staging, and treatment-modality workflow roles
- topic_write_back_targets:
  - `topics/cancer/index.md`
  - `topics/cancer/current-state-dashboard.md`
  - `topics/cancer/navigation.md`
  - `system/indexes/cancer-source-index.md`
  - `system/indexes/cancer-source-depth-map.md`
- not_safe_to_promote_yet:
  - tumor-specific treatment protocols
  - survival promises
  - remote diagnosis from signs
  - generalized radiation or chemotherapy recommendations
  - broad recurrence/prognosis claims without tumor-specific sources
- conflicts_with_existing_vault:
  - none detected; this source adds a practical workflow shell
- new_entities_or_pages_justified:
  - future "approach to suspected cancer" page
  - future diagnosis/staging workflow section
  - future treatment-modality overview with branch gates
