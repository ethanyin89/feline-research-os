---
id: src-ckd-038
type: source
title: "Feline Polycystic Kidney Disease: An Update"
source_kind: paper
species: feline
diseases: [CKD, PKD]
models: [human-ADPKD]
endpoints: [cyst-progression, kidney-failure, genetic-testing]
jurisdictions: []
evidence_level: review
year: 2021
status: ingested
extraction_depth: partial
verification_status: abstract_weighted
pmid: "34822642"
doi: "10.3390/vetsci8110269"
decision_grade: no
language_qa_status: not_applicable
tags: [ckd, pkd, polycystic, ADPKD, PKD1, persian, genetic, hereditary, ultrasound, cysts]
links:
  doi: "10.3390/vetsci8110269"
  url: "https://www.mdpi.com/2306-7381/8/11/269"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "In cats, this disease also has a high prevalence, mainly in the Persian breed, being one of the most common feline genetic diseases."
    - "The formation and growth of cysts progress slowly, causing deterioration of kidney tissue and a gradual decrease in kidney function, leading to irreversible kidney failure."
    - "Imaging tests seem to be the most reliable method for diagnosis of the disease."
  source_supported_conclusion:
    - "Feline PKD is autosomal dominant (ADPKD), caused by PKD1 gene mutations."
    - "Highest prevalence in Persian breed; one of most common feline genetic diseases."
    - "Progressive cyst formation leads to irreversible kidney failure."
    - "Cysts may also form in liver and pancreas."
    - "Imaging (ultrasound) is primary diagnostic method; genetic testing expanding."
    - "Breeding selection programs can reduce/eliminate PKD in affected breeds."
  llm_inference:
    - "Early genetic testing enables preventive breeding strategies."
    - "No curative treatment; management is supportive as CKD progresses."
    - "Human ADPKD parallels support translational relevance."
  # V2 enhanced fields
  study_design: "综述，猫多囊肾病（PKD）的遗传学、诊断和管理更新"
  core_argument: "猫 PKD 是常染色体显性遗传病（ADPKD），由 PKD1 基因突变引起——波斯猫患病率最高，是最常见的猫遗传病之一"
  implicit_premise: "假设早期基因检测可以支持预防性繁殖策略；假设人类 ADPKD 平行关系支持转化相关性"
  unexpected_finding: "囊肿可能在肝脏和胰腺形成而不仅仅是肾脏——多器官累及扩展了疾病理解"
  title_gap: "标题说多囊肾病更新，但真正发现是多器官累及：囊肿可能在肝脏和胰腺形成而不仅仅是肾脏——疾病理解从单器官扩展到系统性，早期基因检测可支持繁殖策略"
  evidence_boundary: "叙述性综述；诊断主要靠影像学，基因检测正在扩展；无治愈性治疗，管理为支持性"
---

# Feline Polycystic Kidney Disease: An Update

## Evidence-Depth Caveat

**Deep-extracted from PubMed abstract (PMID 34822642).** 2021 Vet Sci review of feline ADPKD: PKD1 gene mutation, highest prevalence in Persian breed, progressive cyst formation leading to irreversible kidney failure. Diagnosis via imaging; genetic testing expanding. Evidence level: narrative review.

## Source Check, 2026-06-17

PubMed abstract extracted.

- PMID: 34822642
- DOI: 10.3390/vetsci8110269
- Journal: Veterinary Sciences (MDPI)
- Year: 2021
- Open access: yes

## Genetics

| Feature | Value |
|---------|-------|
| Gene | PKD1 |
| Inheritance | Autosomal dominant (ADPKD) |
| Breed predisposition | Persian (highest prevalence) |
| Status | One of most common feline genetic diseases |

## Disease Progression

**Quoted:** "The formation and growth of cysts progress slowly, causing deterioration of kidney tissue and a gradual decrease in kidney function, leading to irreversible kidney failure."

- Cysts form in kidneys
- May also affect liver and pancreas
- Slow progression → organ failure

## Diagnosis

**Quoted:** "Imaging tests seem to be the most reliable method for diagnosis of the disease."

| Method | Status |
|--------|--------|
| Ultrasound | Primary diagnostic tool |
| Genetic testing | Expanding availability |
| Histology | Confirmatory |

## Prevention

Early genetic mutation detection enables "selection programs to reduce or eliminate this pathology in feline breeds."

## One-Line Summary

2021 review of feline ADPKD: PKD1 mutation, Persian breed predisposition, progressive cyst formation → irreversible kidney failure; diagnosis via imaging, genetic testing for breeding programs.

## Claim-Fit Judgment

**Strongest safe use:**
- PKD genetics and inheritance pattern
- Persian breed prevalence
- Diagnostic approach (imaging, genetic testing)
- Breeding program rationale

**May control:**
- CKD index PKD/hereditary section
- mechanism-overview cyst formation
- Breed-specific risk pages

**Should use with caveats:**
- Specific prevalence numbers (not in abstract)
- Treatment outcomes (not detailed)

**Must not control:**
- Treatment protocols
- Prognosis predictions
- Screening recommendations

## Deep Extraction Metadata

- **Extraction date:** 2026-06-17
- **Source:** PubMed abstract (PMID 34822642)
- **Full text verified:** Abstract-level
- **Citations in vault topic pages:** 8 (branch-controlling)

## Linked Entities

- diseases: CKD, PKD, ADPKD
- genes: PKD1
- breeds: Persian
- endpoints: cyst progression, kidney failure
- mechanisms: cyst formation, hereditary transmission
- diagnostics: ultrasound, genetic testing
