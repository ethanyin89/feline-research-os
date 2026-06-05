---
id: src-cancer-004-deep-extraction-round1
type: system
topic: cancer
question_type: deep-extraction
source_ids: [src-cancer-004]
language: zh
last_compiled_at: 2026-05-30
verification_status: deep_extracted
decision_grade: no
owner: codex
status: active
---

# Deep Extraction Worksheet

Source: `src-cancer-004`  
Title: `Molecular Mechanisms of Feline Cancers`  
Method note: this worksheet is based on the accessible open HTML article page at LIDSEN / OBM Genetics. The XML endpoint listed by Crossref returned CloudFront 503 during this run, so this is not an XML/PDF extraction.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This is a broad molecular oncology map, not a treatment guideline

- core_claim: the review frames feline cancers as under-studied compared with canine cancers but useful for comparative oncology because cats are immunocompetent companion animals exposed to human-like environments.
- implicit_premise: comparative oncology value does not automatically make a source clinically prescriptive for cats.
- relation_to_previous: establishes the source's shell role for the cancer module.
- hard_details: article published in `OBM Genetics` in 2021; open-access CC BY; reviewed lymphoma, squamous cell carcinoma, sarcoma, mammary tumors, and mast cell tumors.
- tension_or_surprise: the paper is branch-rich, but its strongest role is taxonomy and mechanism placement, not owner-facing advice.

#### Unit 2: Lymphoma is treated as a shifting viral and gastrointestinal branch

- core_claim: lymphoma is positioned as a major feline cancer branch historically linked to FeLV/FIV, but the review emphasizes a shift toward gastrointestinal lymphoma as FeLV-associated cases declined.
- implicit_premise: the cancer module should separate older retrovirus-linked lymphoma logic from newer alimentary/GI lymphoma logic.
- relation_to_previous: first disease branch under the broad molecular map.
- hard_details: review states lymphoma is about one third of feline tumors; in one 163-cat lymphoma study, alimentary lymphoma was 52%, nasal 15%, mediastinal 12%, multicentric 9%, and other locations 12%; FeLV-positive and FIV-positive cats are reported as much more likely to develop lymphoma in cited work.
- tension_or_surprise: declining FeLV does not mean declining lymphoma, because GI lymphoma becomes a separate modern control problem.

#### Unit 3: Oral squamous cell carcinoma is a comparative model with unresolved mechanism boundaries

- core_claim: feline oral squamous cell carcinoma is presented as a model for human head and neck SCC because of similar behavior, but viral association, EGFR, p53, COX, and other pathways remain unsettled.
- implicit_premise: model similarity is useful but should not erase feline-specific uncertainty.
- relation_to_previous: moves from lymphoma to a second branch with model-organism implications.
- hard_details: FOSCC is described as the most common oral cancer in cats, affecting older cats and often the sublingual area; the review discusses papillomavirus uncertainty, TP53/p53 dysregulation, COX-1/COX-2 overexpression, EGFR expression, BCL11B/VEGF/SRC pathway work, dasatinib, and CK2 as a candidate target.
- tension_or_surprise: the paper repeatedly identifies candidate pathways, but often ends with "needs further study" rather than settled prognostic or therapeutic rules.

#### Unit 4: Sarcoma is split into injection-site associated and spontaneous disease

- core_claim: feline sarcoma should be split into injection-site associated sarcoma and spontaneous sarcoma because the causal frame, behavior, and treatment logic differ.
- implicit_premise: a cancer module that groups all sarcoma together will overcompress a high-risk boundary.
- relation_to_previous: third major branch, with the clearest inflammatory-origin story.
- hard_details: the review states FISS occurrence as 1 to 10 per 10,000 vaccinated cats; commonly associated with FeLV/rabies vaccination sites; recurrence can be high without radical excision plus radiotherapy; review discusses TP53 staining, FAP/WT1/PRAME upregulation, TP63/EPHA1/DUSP26 downregulation, chromosomal instability, metformin, liposomal doxorubicin/hyperthermia, IL-2 poxvirus vectors, electrochemotherapy, and tyrosine kinase inhibitor work.
- tension_or_surprise: the treatment section contains many experimental or adjunctive leads; these are not the same as practice standards.

#### Unit 5: Mammary carcinoma is a comparative oncology anchor, especially for TNBC-like biology

- core_claim: feline mammary carcinoma is presented as aggressive and translationally important, with model relevance to hormone-independent and triple-negative human breast cancer.
- implicit_premise: comparative model value should be separated from direct feline treatment recommendations.
- relation_to_previous: fourth branch and probably one of the strongest module anchors.
- hard_details: review discusses HER2, TOP2A, E-cadherin/beta-catenin, ER-alpha splice variants, TWIST1, STAT3, f-STK/RON, p-AKT/PTEN, TP53, ERBB2, HSPB1, and cyclin-related mechanisms; a cited study found overexpression of feline HER2 orthologue and 92% similarity between feline HER2 and human HER2 exons 17 and 23.
- tension_or_surprise: feline HER2 expression may not map cleanly onto human HER2 gene amplification logic, so model language must stay bounded.

#### Unit 6: Mast cell tumors are c-KIT rich but still clinically unsettled

- core_claim: feline mast cell tumors are organized by organ system, with c-KIT mutation biology visible but not fully predictive.
- implicit_premise: molecular marker presence is not automatically a validated clinical decision rule.
- relation_to_previous: fifth major branch and a cautionary example for overreading biomarkers.
- hard_details: splenic, intestinal, and cutaneous MCT categories are discussed; splenic MCTs occur in older cats, with mean age range of 9 to 13 years in cited work; anemia is reported in roughly 14-70% in splenic MCT sources; one cited comparison reports median survival of 856 days with splenectomy versus 342 days without splenectomy; c-KIT mutations are common, mainly in exons 8-11.
- tension_or_surprise: the review notes c-KIT mutation frequency but also says correlation with survival, mitotic activity, or differentiation is not clearly established.

## Phase 1: Theme Reconstruction

## Theme: Feline cancer needs a branch map before advice

This source is valuable because it supplies a first molecular branch map for the cancer module. It covers lymphoma, FOSCC, sarcoma, mammary tumors, and mast cell tumors in one place, while repeatedly showing that each branch has its own mechanism and claim ceiling. This makes it a shell-setting review.

### Hard Information

- 2021 OBM Genetics review
- five main branches: lymphoma, SCC, sarcoma, mammary tumors, mast cell tumors
- article is open access under CC BY
- comparative oncology is a repeated theme, but not a clinical-guideline frame

## Theme: Comparative oncology claims need boundaries

The paper repeatedly compares feline cancers with human cancers, especially FOSCC with human head and neck SCC and feline mammary carcinoma with breast cancer/TNBC. These analogies are useful for model logic and mechanism discovery, but the paper does not make them sufficient for treatment translation.

### Hard Information

- FOSCC is compared with HNSCC
- feline mammary carcinoma is compared with human breast cancer and TNBC
- HER2, TOP2A, E-cadherin, TWIST1, STAT3, p-AKT/PTEN, and TP53 appear in mammary branch discussion
- FOSCC pathway discussion includes TP53/p53, COX-1/COX-2, EGFR, BCL11B/VEGF/SRC, and CK2

## Theme: Viral, inflammatory, and molecular mechanisms split the module

The source helps prevent a flat "cancer" page. Lymphoma has retrovirus and GI-shift logic. Sarcoma has injection-site inflammation versus spontaneous disease. Mast cell tumors have c-KIT biology but unresolved prognostic translation. Mammary carcinoma and FOSCC sit closer to comparative oncology model branches.

### Hard Information

- lymphoma: FeLV/FIV history plus rising GI lymphoma emphasis
- sarcoma: FISS versus spontaneous sarcoma split
- mast cell tumors: splenic, intestinal, cutaneous categories
- mammary carcinoma: HER2/TNBC model language needs boundary control

## Phase 2: Claim-Evidence Structure

### Cancer-Shell Key Points

**Claim 1**
- support: the article explicitly reviews five major feline cancer families.
- details: lymphoma, SCC, sarcoma, mammary tumors, mast cell tumors.
- implicit_premise: cancer module architecture should branch by tumor family rather than compile a single generic oncology page.

**Claim 2**
- support: several branches are framed through molecular markers and comparative oncology models.
- details: FOSCC/HNSCC; mammary carcinoma/breast cancer/TNBC; c-KIT in MCT; FeLV/FIV and lymphoma.
- implicit_premise: comparative model logic is a separate evidence family from feline clinical guidance.

### Boundary-Setting Key Points

**Claim 1**
- support: treatment leads are mixed with cell-line, molecular, and review-level material.
- details: dasatinib, CK2 targeting, metformin, IL-2 vectors, electrochemotherapy, tyrosine kinase inhibitors, chemotherapy examples.
- implicit_premise: do not convert molecular treatment leads into practice recommendations without source-specific clinical evidence.

**Claim 2**
- support: the review often reports marker associations while preserving unresolved prognostic meaning.
- details: EGFR prognosis in FOSCC unclear; c-KIT mutation relationship in MCT still needs study; HER2 gene amplification differs from human pattern.
- implicit_premise: marker presence is not claim permission for diagnostic or treatment decisions.

## Phase 2.5: Write-Back Implications

### For `topics/cancer/index.md`

- cancer shell should split early into lymphoma, oral SCC, sarcoma/FISS, mammary carcinoma, and mast cell tumor branches.
- this source can serve as the first molecular branch-map anchor, not a treatment guide.

### For `system/indexes/cancer-source-index.md`

- `src-cancer-004` should be marked as a deep-extracted molecular mechanism review and prioritized above title-only mechanism/cell-line sources.

### For `system/indexes/cancer-source-depth-map.md`

- this becomes the first cancer source with full deep-extraction status.

## Phase 3: Promotion Check

- source_card_updates:
  - promote `src-cancer-004` from `abstract_weighted` to `deep_extracted`
  - preserve branch map role and open-access HTML method note
  - capture lymphoma, FOSCC, sarcoma, mammary carcinoma, and MCT boundaries
- topic_write_back_targets:
  - `topics/cancer/index.md`
  - `topics/cancer/current-state-dashboard.md`
  - `system/indexes/cancer-source-index.md`
  - `system/indexes/cancer-source-depth-map.md`
- not_safe_to_promote_yet:
  - treatment rankings
  - owner-facing prognosis statements
  - biomarker decision rules
  - human-to-cat therapy translation claims
  - numeric risk claims outside the specific review context
- conflicts_with_existing_vault:
  - none detected; this source adds a cancer molecular branch map
- new_entities_or_pages_justified:
  - future branch pages for lymphoma, oral SCC, sarcoma/FISS, mammary carcinoma, and mast cell tumors
