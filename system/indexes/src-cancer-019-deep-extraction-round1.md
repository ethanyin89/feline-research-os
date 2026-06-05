---
id: src-cancer-019-deep-extraction-round1
type: system
topic: cancer
question_type: deep-extraction
source_ids: [src-cancer-019]
language: zh
last_compiled_at: 2026-05-30
verification_status: deep_extracted
decision_grade: no
owner: codex
status: active
---

# Deep Extraction Worksheet

Source: `src-cancer-019`  
Title: `Feline mammary basal-like adenocarcinomas: a potential model for human triple-negative breast cancer (TNBC) with basal-like subtype`  
Method note: this worksheet is based on the accessible open HTML article page at Springer Nature / BMC Cancer. `src-cancer-021` was checked in the same continuation sample but the Hindawi page returned a Cloudflare challenge, so it was not extracted.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: The paper is a mammary carcinoma model study, not a treatment guide

- core_claim: the article evaluates feline mammary adenocarcinomas as a natural model for human triple-negative breast cancer with basal-like subtype.
- implicit_premise: translational model value should be kept separate from feline clinical treatment authority.
- relation_to_previous: deepens the mammary carcinoma branch introduced by `src-cancer-004`.
- hard_details: 24 archival feline mammary adenocarcinomas from Michigan State University were studied; cases were submitted from 2004-01-01 through 2007-12-12; mean age was 12 years, range 6 to 19 years.
- tension_or_surprise: the paper supports a strong model analogy but does not establish practice recommendations for cats.

#### Unit 2: The phenotype screen uses human breast-cancer classification markers

- core_claim: the study applies ER, PR, HER2, CK5/6, and EGFR immunohistochemistry to classify feline mammary adenocarcinomas.
- implicit_premise: the branch should track marker definitions and not treat "basal-like" as a casual synonym for aggressive cancer.
- relation_to_previous: converts the broad mammary/TNBC signal into a concrete marker framework.
- hard_details: ER/PR/HER2 were used for triple-negative status; CK5/6 and EGFR were used as basal-like markers; HER2 was interpreted with a HercepTest-style scoring boundary.
- tension_or_surprise: basal-like assignment depends on marker combinations, so title-level intake is insufficient for claim promotion.

#### Unit 3: Triple-negative and basal-like results are the branch-controlling finding

- core_claim: most tumors in this series were aggressive, and triple-negative tumors commonly overlapped with basal-like marker expression.
- implicit_premise: the module can use this source to justify a mammary carcinoma / TNBC-like comparative branch, not a universal feline cancer claim.
- relation_to_previous: supplies the first extracted numeric anchor for the mammary comparative oncology branch.
- hard_details: 14/24 tumors were triple negative; 11/14 triple-negative tumors had basal-like subtype; 19/24 tumors were classified as basal-like when CK5/6 and/or EGFR positivity was considered.
- tension_or_surprise: basal-like positivity can appear outside strict triple-negative status, so the module should keep "basal-like FMA" and "triple-negative basal-like FMA" distinct.

#### Unit 4: BRCA findings are negative and method-limited

- core_claim: BRCA1/BRCA2 sequencing and LOH analysis did not find tumor-specific abnormalities in the tested subset.
- implicit_premise: absence of detected BRCA changes is not proof that BRCA biology is irrelevant in cats.
- relation_to_previous: constrains the human TNBC analogy.
- hard_details: only 5 of 11 DNA samples from triple-negative basal-like tumors amplified for genetic analysis; no BRCA1/BRCA2 allelic loss was detected in the tested material.
- tension_or_surprise: the model similarity is strong at histology and IHC level, but weaker and unresolved at the BRCA mechanism level.

#### Unit 5: The source can shape branch architecture but not owner-facing advice

- core_claim: this article is useful for structuring mammary carcinoma evidence around comparative oncology, marker phenotype, and model limits.
- implicit_premise: numeric findings from 24 archival cases should remain tied to this study context unless corroborated by larger clinical or registry sources.
- relation_to_previous: gives `src-cancer-004` a concrete mammary-branch companion.
- hard_details: the paper reports high mitotic rates, frequent necrosis, ER positivity in 2/24, PR positivity in 7/24, HER2 overexpression in 4/24, and tumor necrosis in 21/24.
- tension_or_surprise: the study is mechanistically useful, but its small archival design limits broad prevalence or prognosis generalization.

## Phase 1: Theme Reconstruction

## Theme: Mammary carcinoma needs its own comparative oncology branch

This source gives the cancer module a reason to split feline mammary carcinoma from generic cancer content. It shows a concrete marker framework for a TNBC-like / basal-like branch and links the feline disease to human comparative oncology without turning that analogy into treatment guidance.

### Hard Information

- 24 feline mammary adenocarcinoma cases
- ER, PR, HER2, CK5/6, and EGFR immunohistochemistry
- 14/24 triple negative
- 11/14 triple-negative tumors basal-like
- 19/24 basal-like by CK5/6 and/or EGFR marker logic

## Theme: BRCA is a boundary, not a bridge

The paper tests BRCA1/BRCA2 because human TNBC and basal-like breast cancers are often discussed through BRCA biology. In this feline series, the tested BRCA region did not provide a positive bridge. That makes the source especially useful for preventing overtranslation from human TNBC.

### Hard Information

- BRCA1/BRCA2 sequencing and LOH analysis were attempted in the triple-negative basal-like subset
- only 5/11 DNA samples amplified for genetic analysis
- no tumor-specific BRCA abnormality or allelic loss was detected in the tested material

## Phase 2: Claim-Evidence Structure

### Mammary Branch Key Points

**Claim 1**
- support: the article applies breast-cancer molecular classification markers to feline mammary adenocarcinomas.
- details: ER, PR, HER2, CK5/6, EGFR.
- implicit_premise: mammary carcinoma branch pages need marker definitions before claim synthesis.

**Claim 2**
- support: triple-negative tumors frequently overlapped with basal-like marker expression in this series.
- details: 14/24 triple negative; 11/14 triple-negative tumors basal-like.
- implicit_premise: this source supports a TNBC-like model branch, not a general cancer prevalence statement.

### Boundary-Setting Key Points

**Claim 1**
- support: BRCA testing was negative in the amplified subset.
- details: 5/11 tested-subset samples amplified; no tumor-specific BRCA abnormality or LOH.
- implicit_premise: do not claim feline TNBC-like mammary tumors are BRCA-driven from this source.

**Claim 2**
- support: the design is archival and small.
- details: 24 cases from one diagnostic archive and a defined 2004-2007 window.
- implicit_premise: numeric results should be study-bound unless triangulated with registry or larger clinical sources.

## Phase 2.5: Write-Back Implications

### For `topics/cancer/index.md`

- mammary carcinoma should be an early split, with a sub-branch for TNBC-like / basal-like comparative oncology.
- the branch should explicitly separate feline clinical management from human-model relevance.

### For `system/indexes/cancer-source-index.md`

- `src-cancer-019` should be marked as a deep-extracted mammary carcinoma / TNBC model anchor.

### For `system/indexes/cancer-source-depth-map.md`

- this becomes the second cancer deep-extracted source after `src-cancer-004`.

## Phase 3: Promotion Check

- source_card_updates:
  - promote `src-cancer-019` from `abstract_weighted` to `deep_extracted`
  - capture mammary carcinoma, TNBC-like, basal-like, IHC marker, and BRCA boundary roles
- topic_write_back_targets:
  - `topics/cancer/index.md`
  - `topics/cancer/current-state-dashboard.md`
  - `topics/cancer/navigation.md`
  - `system/indexes/cancer-source-index.md`
  - `system/indexes/cancer-source-depth-map.md`
- not_safe_to_promote_yet:
  - feline treatment recommendations
  - broad prevalence claims
  - prognosis estimates for all feline mammary cancer
  - BRCA-driven mechanism claims
  - direct human-to-cat therapy translation
- conflicts_with_existing_vault:
  - none detected; this source strengthens the mammary carcinoma comparative oncology branch
- new_entities_or_pages_justified:
  - future mammary carcinoma branch page
  - future TNBC-like / basal-like evidence subsection
