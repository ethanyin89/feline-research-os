---
id: src-cancer-015-deep-extraction-round1
type: system
source_id: src-cancer-015
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-015

**Source:** Epidemiological features of feline mammary carcinoma
**Journal:** Veterinary Record (1981)
**DOI:** 10.1136/vr.108.22.476
**PMID:** 7257136
**Evidence Level:** original-study (epidemiological survey)

## Phase 0: Context

**Access status:** Full abstract available in source card.

**Source scope:** Classic 1981 multi-center epidemiological survey of 132 cats with mammary neoplasia from 15 North American veterinary teaching hospitals.

**Historical importance:** Foundational epidemiological study establishing the high malignancy rate and Siamese breed predisposition for feline mammary carcinoma.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Characteristics

| Parameter | Value |
|-----------|-------|
| Population | 132 cats with mammary neoplasia |
| Centers | 15 North American VMTHs |
| Design | Epidemiological survey |
| Year | 1981 |

### 1.2 Malignancy Rate

| Finding | Value | Significance |
|---------|-------|--------------|
| Malignant:benign ratio | 9:1 | Very high malignancy |
| Total carcinomas | 113 cases | Including 2 males |
| Predominant histology | Adenocarcinoma | Most common subtype |

**Key insight:** The 9:1 malignant to benign ratio is a foundational finding — feline mammary tumors are overwhelmingly malignant, unlike dogs where ~50% are benign.

### 1.3 Breed Predisposition

| Factor | Finding | P-value |
|--------|---------|---------|
| Siamese breed risk | 2x vs all breeds | P < 0.01 |
| Siamese age at diagnosis | Younger than other breeds | — |

**Key insight:** Siamese cats have significantly elevated risk and present younger. This suggests a genetic predisposition.

### 1.4 Hormone Dependency

| Observation | Interpretation |
|-------------|----------------|
| "Apparent lack of oestrogen dependency" | Differs from many human breast cancers |
| Therapeutic implication | Cat suited for evaluating hormone-independent therapies |

**Connects to:** src-cancer-013 (HER2 prevalence) and src-cancer-005 (triple-negative enrichment) — feline mammary carcinoma tends to be hormone receptor-negative.

### 1.5 Comparative Oncology

| Claim | Context |
|-------|---------|
| Cat is appropriate surrogate for human breast cancer | Clinical and pathological similarities |
| Especially for hormone-independent tumors | Lack of estrogen dependency |

## Phase 2: Theme Reconstruction

### Theme A: High Malignancy Rate

The 9:1 malignant to benign ratio is a defining characteristic of feline mammary neoplasia:
- Almost all mammary tumors in cats are malignant
- Contrasts with dogs (~50% benign)
- Clinical implication: treat all feline mammary masses as potentially malignant

### Theme B: Siamese Genetic Predisposition

Siamese cats have 2x the risk with younger age at diagnosis:
- Suggests genetic/heritable component
- May indicate specific susceptibility pathways
- Potential for breed-specific research

### Theme C: Hormone-Independent Biology

The "apparent lack of oestrogen dependency" aligns with:
- src-cancer-005: triple-negative enrichment
- src-cancer-013: high HER2+ rate

This supports the characterization of FMC as predominantly hormone receptor-negative, which has treatment implications.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-EPI1 | Feline mammary tumors have 9:1 malignant to benign ratio | B | 1981 foundational study, 132 cats |
| MC-EPI2 | Siamese cats have 2x risk for mammary carcinoma (P<0.01) | B | North American population |
| MC-EPI3 | Siamese cats are diagnosed with mammary carcinoma at younger age | B | breed-specific pattern |
| MC-EPI4 | Feline mammary carcinoma shows apparent lack of estrogen dependency | B | hormone biology |
| MC-EPI5 | Adenocarcinoma is the predominant histologic subtype | B | histopathology |

**Section to add/update:** Epidemiology, Breed Predisposition, Hormone Biology

**Boundary rules:**
- Note 1981 study date for breed demographics
- Frame 9:1 ratio as foundational/widely cited finding
- Connect hormone independence to molecular subtype discussion

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] 9:1 malignant to benign ratio
- [x] Siamese breed 2x risk (P<0.01)
- [x] Siamese diagnosed younger
- [x] Adenocarcinoma predominant histology
- [x] Apparent lack of estrogen dependency
- [x] Cat as model for human breast cancer

### not_safe_to_promote_yet

- [ ] Current breed risk in different populations
- [ ] Specific genetic mutations in Siamese
- [ ] Treatment recommendations based on hormone status
- [ ] Modern malignancy ratios (may have changed)

### open_questions

1. Have breed risk profiles changed with population demographics?
2. What genetic variants underlie Siamese predisposition?
3. Is the 9:1 ratio confirmed in modern studies?
4. How does spay status affect risk in Siamese vs other breeds?
5. Are there other high-risk breeds identified since 1981?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 6 epidemiological claims |
| Evidence level | epidemiological survey (1981, 132 cats, 15 VMTHs) |
| Key contribution | Foundational malignancy rate, Siamese predisposition |
| Primary gap | 40+ year old study, modern validation needed |
| Topic page targets | mammary-carcinoma.md (epidemiology, breed risk) |
| Historical value | High — foundational epidemiology |
