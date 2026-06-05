---
id: topic-cancer-registry-and-prevalence
type: topic
topic: cancer
species: feline
disease: cancer
question_type: synthesis
source_ids: [src-cancer-002, src-cancer-007, src-cancer-024, src-cancer-064]
last_compiled_at: 2026-05-30
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Registry And Prevalence

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| RP1 | Registry and prevalence claims must state the denominator before using numeric tumor-frequency language | B | src-cancer-002 | pathology registry proportions, not population incidence |
| RP2 | Tumor type and anatomic location should both shape cancer navigation | B | src-cancer-002 | branch priority, not clinical ranking |
| RP3 | Regional comparator sources may change tumor-mix expectations, but blocked full text cannot control synthesis yet | C | src-cancer-007 | abstract-weighted only |
| RP4 | Pediatric feline oncology needs a separate denominator from all-age registry or hospital-admission datasets | B | src-cancer-064 | cats <=12 months, UK biopsy submissions |
| RP5 | In the pediatric biopsy-submission dataset, lymphoma, soft-tissue sarcoma, mast cell tumor, and SCC were the most frequent tumors | B | src-cancer-064 | pediatric pathology-submission proportions only |
| RP6 | 17.0% of feline patients at UC Davis VMTH (2000-2019) were diagnosed with cancer; older age is the strongest predictor | B | src-cancer-024 | referral hospital population, not general incidence |

## Current Synthesis

`src-cancer-002` is the controlling source for registry denominator discipline. It uses the Swiss Feline Cancer Registry, spanning 1965-2008, with 51,322 feline patient records and 18,375 tumours. Because Switzerland lacked obligatory cat registration, the paper used proportional calculations. That boundary must travel with any frequency statement.

The safe reuse is structural:

- label numbers as registry or pathology-submission proportions
- keep tumor type and anatomic site as separate axes
- use registry prominence to prioritize branch extraction
- keep time trends as hypothesis-generating until branch-specific sources verify mechanism

## US Referral Hospital Epidemiology

`src-cancer-024` provides the largest US companion animal cancer epidemiology dataset from UC Davis VMTH (2000-2019). Deep-extracted findings:

- 150,063 total patients (20.1% cats = ~30,163 feline patients)
- 17.0% of feline patients diagnosed with cancer (vs 18.1% dogs)
- Older age is the strongest predictor of cancer in both species
- Nine cancer types analyzed: sarcoma, carcinoma, lymphoid neoplasia, MCT, melanoma, plus four others
- Authors explicitly call for California-wide registry

**Boundary:** This is a referral hospital population with inherent selection bias. The 17.0% cancer rate reflects referral patterns, not general feline cancer incidence. Feline-specific odds ratios for breed/sex/neuter status are not reported in the abstract; full-text extraction needed.

## South Africa Comparator Lead

`src-cancer-007` is important but not yet deep-extracted. The publisher abstract identifies a South African hospital-admissions dataset from 1998-2005 and reports a high squamous cell carcinoma share. Because direct PDF access was not verified in this run, the source can guide the reading queue but should not control topic-page claims.

## Pediatric Oncology Denominator

`src-cancer-064` is a pediatric-cat pathology-submission dataset from Idexx Laboratories, Wetherby, UK. It screened 4196 biopsy submissions from cats 12 months old or younger between September 1993 and March 2008; 233 biopsies were neoplastic and met search criteria.

Study-bound findings:

- 233/4196 submissions (6%) were neoplastic and met criteria.
- Tumor categories included hematopoietic, malignant epithelial, malignant mesenchymal, benign epithelial, benign mesenchymal, and miscellaneous groups.
- The most frequent tumors were lymphoma, soft-tissue sarcoma, mast cell tumor, and squamous cell carcinoma.
- Skin and soft tissues were the most common tumor site.
- 164 neoplasms were malignant or had malignant potential.

**Boundary:** This is a pediatric-cat biopsy-submission denominator. Do not merge it with all-age registry, hospital-admission, or population incidence claims.

## Boundaries

- Do not convert registry proportions into population incidence.
- Do not merge Swiss pathology registry data with South African hospital-admissions data as one pooled prevalence estimate.
- Do not present fibrosarcoma time trends as vaccine causality without FISS-specific sources.
- Do not present lymphoma time trends as FeLV causality without FeLV / lymphoma sources.
- Do not convert pediatric biopsy-submission proportions into all-age feline cancer rankings.
- Do not present US referral hospital rates (17.0%) as general population cancer incidence.
- Do not rank treatments, prognosis, or diagnostic pathways from registry frequency data.

## Next Sources Needed

- the paired Swiss registry overview paper for occurrence of tumours in cats in Switzerland
- FISS-specific epidemiology / pathology source
- FeLV-era lymphoma source
- full-text readable copy of the South Africa prevalence article
- full-text review of `src-cancer-064` if pediatric oncology becomes its own branch
