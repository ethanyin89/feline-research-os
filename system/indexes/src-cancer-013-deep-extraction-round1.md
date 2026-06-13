---
id: src-cancer-013-deep-extraction-round1
type: system
source_id: src-cancer-013
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-013

**Source:** Spontaneous feline mammary carcinoma is a model of HER2 overexpressing poor prognosis human breast cancer
**Journal:** Cancer Research (2005)
**DOI:** Not specified
**PMID:** 15705889
**Evidence Level:** original-study (molecular characterization)

## Phase 0: Context

**Access status:** Full abstract available in source card. Cancer Research (AACR) journal.

**Source scope:** Molecular characterization of feline HER2 and its expression in feline mammary carcinoma (FMC), establishing FMC as a comparative oncology model.

**Translational importance:** This establishes the molecular basis for using FMC as a model for HER2+ human breast cancer and potentially testing HER2-targeted therapies.

## Phase 1: Sequential Micro-Analysis

### 1.1 Feline HER2 Molecular Characterization

| Parameter | Finding | Significance |
|-----------|---------|--------------|
| Kinase domain homology | 92% similar to human HER2 | High conservation |
| Antibody cross-reactivity | Human anti-HER2 antibody recognizes feline HER2 | Diagnostic/research tool |
| Protein size | Comigrates with human p185HER2 | Similar protein |

**Key insight:** The 92% kinase domain homology means feline HER2 is structurally similar enough that human HER2-targeted agents may have activity against feline HER2.

### 1.2 HER2 Expression in FMC

| Sample Type | HER2 Status | Prevalence |
|-------------|-------------|------------|
| FMC cell lines | 3-18x mRNA increase | 3/3 (100%) |
| Mammary adenomas | mRNA increase | 1/4 (25%) |
| FMC tumor samples | mRNA increase | 6/11 (55%) |
| FMC archival (IHC) | Strongly positive | 13/36 (36%) |

**Key insight:** HER2 overexpression is common in FMC — 36-55% depending on method. This is higher than in human breast cancer (~15-20%), supporting FMC as an enriched model.

### 1.3 FMC Disease Characteristics

| Characteristic | Finding |
|----------------|---------|
| Aggressiveness | "Highly aggressive" |
| Hormone receptor status | "Mainly hormone receptor-negative" |
| Model comparison | Poor prognosis human breast cancer |

**Key insight:** FMC shares key features with aggressive human breast cancer subtypes — hormone receptor negative and often HER2+.

### 1.4 Model Validation

| Criterion | Evidence |
|-----------|----------|
| Genetic heterogeneity | Spontaneous tumors in genetically diverse population |
| Molecular similarity | 92% HER2 kinase homology |
| Phenotypic similarity | HER2+ aggressive cancer |
| Tool availability | Human antibodies cross-react |

**Conclusion from paper:** "FMC qualified as homologous to the subset of HER2 overexpressing, poor prognosis human breast carcinomas"

## Phase 2: Theme Reconstruction

### Theme A: Molecular Basis for Comparative Oncology

The 92% kinase domain homology between feline and human HER2 provides a molecular foundation for using FMC as a model for human HER2+ breast cancer. This is not just phenotypic similarity but structural conservation.

### Theme B: HER2 Prevalence in FMC

HER2 overexpression is found in 36-55% of FMC samples depending on detection method:
- qRT-PCR: 55% (6/11)
- IHC: 36% (13/36)

This is higher than the ~15-20% HER2+ rate in human breast cancer, making FMC an "enriched" population for HER2 research.

### Theme C: Triple-Negative vs HER2+ in FMC

This study notes FMC is "mainly hormone receptor-negative" and often HER2+. Combined with src-cancer-005's note that triple-negative is enriched in cats, this suggests FMC molecular subtypes may differ from human breast cancer distribution:
- Higher HER2+ rate
- Higher hormone receptor-negative rate
- Potentially higher triple-negative (HR-/HER2-)

### Theme D: Therapeutic Implications

The cross-reactivity of human anti-HER2 antibodies with feline HER2 opens potential therapeutic avenues:
- HER2-targeted therapies (trastuzumab-like) could be tested
- FMC patients could potentially benefit from HER2-targeted drugs
- Natural disease model for drug development

**Boundary:** This is translational research potential, not treatment recommendation.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/mammary-carcinoma.md

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| MC-HER2-1 | Feline HER2 kinase domain is 92% similar to human HER2 | B | molecular characterization |
| MC-HER2-2 | 36-55% of FMC samples show HER2 overexpression | B | 2005 study, varies by method |
| MC-HER2-3 | Human anti-HER2 antibodies cross-react with feline HER2 | B | research/diagnostic tool |
| MC-HER2-4 | FMC is validated as a model for HER2+ poor prognosis human breast cancer | B | comparative oncology, not treatment |

**Section to add:** Molecular Subtypes / HER2 Status

**Boundary rules:**
- This is model validation, not treatment guidance
- Do not recommend HER2 testing for FMC patients without additional clinical evidence
- Do not recommend HER2-targeted therapies without feline trial data
- Frame as research finding, not clinical practice

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Feline HER2 is 92% similar to human HER2 kinase domain
- [x] 36-55% of FMC samples show HER2 overexpression
- [x] Human anti-HER2 antibodies recognize feline HER2
- [x] FMC is established as a model for HER2+ human breast cancer
- [x] FMC is mainly hormone receptor-negative

### not_safe_to_promote_yet

- [ ] HER2 testing recommendations for FMC patients
- [ ] HER2-targeted therapy for cats
- [ ] Prognostic significance of HER2 in FMC
- [ ] Comparison of HER2+ vs HER2- FMC outcomes

### open_questions

1. Does HER2 status affect prognosis in FMC?
2. Have HER2-targeted therapies been tested in cats?
3. What is the current recommended HER2 testing method for FMC?
4. How does FMC HER2 expression compare to more recent studies?
5. Is combined HR-/HER2+ status more common in FMC than in humans?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 5 molecular characterization claims |
| Evidence level | original study (2005, Cancer Research) |
| Key contribution | Molecular basis for FMC as HER2+ model |
| Primary gap | Clinical HER2 testing/therapy data for cats |
| Topic page targets | mammary-carcinoma.md (molecular subtypes) |
| Translational value | High — validates comparative oncology model |
