---
id: src-cancer-003-deep-extraction-round1
type: system
topic: cancer
question_type: deep-extraction
source_ids: [src-cancer-003]
language: zh
last_compiled_at: 2026-05-30
verification_status: deep_extracted
decision_grade: no
owner: codex
status: active
---

# Deep Extraction Worksheet

Source: `src-cancer-003`  
Title: `The role of COX expression in the prognostication of overall survival of canine and feline cancer: A systematic review`  
Method note: Wiley and PMC direct pages returned browser/challenge pages during this run, but Europe PMC full-text XML for `PMC8294401` was accessible and used for this worksheet.

## Phase 0: Sequential Micro-Analysis

#### Unit 1: This is a prognosis-biomarker review, not a treatment protocol

- core_claim: the review asks whether COX-1 or COX-2 expression has prognostic value in canine and feline malignant neoplasms.
- implicit_premise: a biomarker prognostic signal does not automatically become a treatment recommendation.
- relation_to_previous: adds a prognosis-marker layer to the cancer module after molecular branch mapping and mammary/TNBC model extraction.
- hard_details: PubMed was searched using dog/cat/neoplasia/tumour/cancer/cyclooxygenase/COX terms; the last search was performed on 2019-10-20; the final review included 18 studies.
- tension_or_surprise: the title says canine and feline cancer broadly, but the feline reusable signal is narrower: mammary tumours and oral SCC.

#### Unit 2: The evidence pool is mixed-species and methodologically uneven

- core_claim: the review includes many dog studies and fewer cat studies, so feline claims need species-specific filtering.
- implicit_premise: mixed-species review conclusions should not be copied into feline-only topic text without checking which studies were feline.
- relation_to_previous: prevents overgeneralizing broad systematic-review language.
- hard_details: included studies totaled 688 dogs and 145 cats; four studies involved cats; feline tumour types included mammary tumours, transitional cell carcinoma, and oral squamous cell carcinoma.
- tension_or_surprise: the largest evidence body is canine, but the paper is still useful for feline branch boundaries if filtered carefully.

#### Unit 3: COX-2 is the mammary carcinoma signal

- core_claim: the review supports COX-2 as a negative prognostic marker in feline mammary tumours, but the certainty is limited.
- implicit_premise: this source can support biomarker prioritization in the mammary branch, not stand-alone prognosis advice.
- relation_to_previous: complements `src-cancer-019`, which defines TNBC-like / basal-like mammary model logic.
- hard_details: two feline mammary tumour studies were reviewed; one reported significant association between high COX-2 and decreased overall survival, while another trended in the same direction but with higher risk of bias.
- tension_or_surprise: the review's conclusion is positive, but it still calls for stronger multivariate and standardized studies.

#### Unit 4: COX-1, not COX-2, is the oral SCC signal

- core_claim: the review reports that COX-1 distribution pattern was an independent negative prognostic factor in feline oral SCC, while COX-2 was not prognostic in that feline oral SCC study.
- implicit_premise: oral SCC biomarker logic must not default to "COX-2 everywhere."
- relation_to_previous: provides an oral SCC marker bridge while `src-cancer-021` remains access-blocked.
- hard_details: the oral SCC signal comes from Hayes et al. 2007 with 54 cats; the review rates the COX-1 distribution-pattern finding as relevant but method-dependent.
- tension_or_surprise: the feline oral SCC branch points to COX-1 pattern, not the more commonly discussed COX-2.

#### Unit 5: Standardization is the main gate before reader-facing claims

- core_claim: heterogeneity in immunohistochemistry scoring and cutoffs is a central limitation.
- implicit_premise: the module should describe COX as a candidate/prognostic-marker family with method caveats, not a clean owner-facing decision rule.
- relation_to_previous: reinforces the vault-wide rule that biomarkers need method and endpoint boundaries.
- hard_details: most included studies used semi-quantitative immunohistochemistry; scoring systems and cutoffs varied; only three studies were classified as low risk of bias, and those were canine studies.
- tension_or_surprise: the review supports rational use of COX enzymes for prognosis research, but also explains why reproducibility and meta-analysis remain difficult.

## Phase 1: Theme Reconstruction

## Theme: COX belongs in prognosis-marker architecture, not treatment advice

This source gives the cancer module a marker-focused branch: COX-2 for feline mammary carcinoma prognosis research and COX-1 pattern for feline oral SCC. It should not be used to recommend NSAIDs, COX inhibitors, or clinical treatment selection without separate therapeutic evidence.

### Hard Information

- systematic review
- 18 included studies
- 688 dogs and 145 cats across included studies
- four cat-involving studies
- feline mammary tumours and feline oral SCC are the strongest feline-relevant branches

## Theme: Feline claims must be filtered out of mixed-species conclusions

The paper repeatedly discusses canine and feline cancers together, but reusable feline claims are concentrated in a few studies. This makes it useful for branch placement and evidence triage, while still requiring species-specific claim extraction.

### Hard Information

- feline mammary tumour evidence: De Campos et al. 2016 and Millanta et al. 2006
- feline oral SCC evidence: Hayes et al. 2007
- feline TCC evidence: Bommer et al. 2012, but too small for firm prognostic conclusions
- only canine studies were included among the low-risk-of-bias group

## Phase 2: Claim-Evidence Structure

### Prognosis-Marker Key Points

**Claim 1**
- support: the review concludes COX-2 has negative prognostic value in canine and feline mammary tumours.
- details: feline support comes from two mammary tumour studies, one significant and one trending with higher bias.
- implicit_premise: mammary branch pages can list COX-2 as a candidate/prognostic marker with evidence-strength caveats.

**Claim 2**
- support: the review reports COX-1 distribution pattern as a negative prognostic factor in feline oral SCC.
- details: the relevant feline oral SCC study included 54 cats and did not find COX-2 prognostic value.
- implicit_premise: oral SCC marker notes should distinguish COX-1 pattern from COX-2 expression.

### Boundary-Setting Key Points

**Claim 1**
- support: the review highlights subjective COX quantification, variable scoring systems, and variable cutoffs.
- details: most studies used immunohistochemistry; only two used more objective methods such as ELISA or qPCR.
- implicit_premise: do not present COX status as a standardized diagnostic/prognostic test for owners.

**Claim 2**
- support: the feline TCC evidence was too small for firm conclusions.
- details: the TCC study had seven cats and no formal statistical test for the observed survival difference.
- implicit_premise: do not create a feline TCC COX rule from this review.

## Phase 2.5: Write-Back Implications

### For `topics/cancer/index.md`

- add COX prognosis-marker logic as a future cross-branch layer, not a main disease branch.
- mammary carcinoma branch should include COX-2 only with method and evidence-strength caveats.
- oral SCC branch should preserve the COX-1-vs-COX-2 distinction.

### For `system/indexes/cancer-source-index.md`

- `src-cancer-003` should be marked as a deep-extracted systematic review for COX/prognosis marker boundaries.

### For `system/indexes/cancer-source-depth-map.md`

- this becomes the third cancer source with full deep-extraction status.

## Phase 3: Promotion Check

- source_card_updates:
  - promote `src-cancer-003` from `abstract_weighted` to `deep_extracted`
  - capture COX-2 mammary, COX-1 oral SCC, and standardization caveats
- topic_write_back_targets:
  - `topics/cancer/index.md`
  - `topics/cancer/current-state-dashboard.md`
  - `topics/cancer/navigation.md`
  - `system/indexes/cancer-source-index.md`
  - `system/indexes/cancer-source-depth-map.md`
- not_safe_to_promote_yet:
  - COX inhibitor treatment recommendations
  - owner-facing survival predictions
  - universal feline cancer biomarker rules
  - feline TCC prognostic rules
  - COX-2 rules for feline oral SCC
- conflicts_with_existing_vault:
  - none detected; this source adds a cross-branch biomarker/prognosis layer
- new_entities_or_pages_justified:
  - future prognosis-marker subsection
  - future mammary carcinoma biomarker subsection
  - future oral SCC marker caveat subsection
