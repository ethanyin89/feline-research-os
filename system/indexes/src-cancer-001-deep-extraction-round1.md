---
id: src-cancer-001-deep-extraction-round1
type: system
source_id: src-cancer-001
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-001

**Source:** Feline Oncogenomics: What Do We Know about the Genetics of Cancer in Domestic Cats?
**Journal:** Veterinary Sciences (MDPI, Open Access) (2022)
**DOI:** 10.3390/vetsci9100547
**PMID:** 36288160
**Evidence Level:** review

## Phase 0: Context

**Access status:** Open access via MDPI. Full-text available.

**Source scope:** Comprehensive genetics review covering multiple feline cancer types from cytogenetics to next-generation sequencing.

**Cross-branch value:** This review spans lymphoma, mammary, SCC, sarcoma, mast cell, hemangiosarcoma, pulmonary carcinoma, pancreatic carcinoma, and osteosarcoma — providing genetics context for multiple topic branches.

## Phase 1: Sequential Micro-Analysis

### 1.1 Field Overview

| Claim | Quote | Boundary |
|-------|-------|----------|
| Cancer burden | "Cancer is a significant cause of morbidity and mortality in domestic cats" | General epidemiology framing |
| Genetics importance | "In humans, an understanding of the oncogenome has proven critical and is deeply interwoven into all aspects of patient care" | Human comparison context |
| Field maturity | "Investigations into understanding the genetics of feline cancers started with cytogenetics and was then expanded to studies at a gene-specific level" | Historical progression |
| Enabling technology | "A recently generated high-quality reference genome for cats enables next-generation sequencing studies" | Technical milestone |

### 1.2 Cancer Types Covered

| Cancer Type | Evidence Note |
|-------------|---------------|
| Lymphomas | Genetics context available |
| Mammary tumours | Genetics context available |
| Squamous cell carcinomas | Genetics context available |
| Soft tissue tumours | Genetics context available |
| Mast cell tumours | Genetics context available |
| Hemangiosarcomas | Genetics context available |
| Pulmonary carcinomas | Genetics context available |
| Pancreatic carcinomas | Genetics context available |
| Osteosarcomas | Genetics context available |

**Key insight:** This is a multi-branch reference source. Each cancer type section in the full text would provide specific genetic findings.

### 1.3 Technology Evolution

| Era | Approach |
|-----|----------|
| Early | Cytogenetics (chromosome-level) |
| Intermediate | Gene-specific studies |
| Current | NGS enabled by high-quality reference genome |

**Implication:** The field is transitioning from descriptive cytogenetics to actionable molecular genetics.

### 1.4 Comparative Oncology Theme

| Finding | Boundary |
|---------|----------|
| Human oncogenome understanding informs feline research | Comparative context |
| Feline cancers may serve as models for human cancer | Model direction flagged |
| Shared mutations may enable shared therapeutic approaches | Hypothesis, not proven |

## Phase 2: Theme Reconstruction

### Theme A: Genetics Infrastructure Maturity

The feline cancer genetics field has reached a new phase with the high-quality reference genome. This enables:
- Whole-genome sequencing studies
- Variant identification at scale
- Comparison with human cancer genomics

### Theme B: Multi-Cancer Genetics Map

This review provides a single-source genetics overview across 9 cancer types. This is valuable for:
- Architecture decisions about genetics sections in branch pages
- Identifying which cancer types have most developed genetic understanding
- Cross-branch molecular mechanism references

### Theme C: Translational Potential

The comparative oncology theme suggests:
- Feline cancers share genetic features with human cancers
- Therapeutic approaches may be transferable
- Feline patients may serve as natural disease models

**Boundary:** This is framework/potential, not proven therapeutic guidance.

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/index.md

**Claims to add:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| GEN1 | Feline cancer genetics field has evolved from cytogenetics to NGS-enabled molecular studies | B | historical context |
| GEN2 | High-quality feline reference genome enables modern oncogenomics research | B | technical milestone |
| GEN3 | Genetics evidence exists for lymphomas, mammary tumours, SCCs, soft tissue tumours, mast cell tumours, hemangiosarcomas, pulmonary carcinomas, pancreatic carcinomas, and osteosarcomas | B | scope indicator |

**Section to add:** Genetics Context (or Molecular Biology subsection)

**Boundary rules:**
- Do not recommend genetic testing for owners
- Do not claim specific mutations without full-text verification
- Frame as "research landscape" not "clinical guidance"

### Target: Multiple branch pages

Each branch page (lymphoma.md, mammary-carcinoma.md, oral-squamous-cell-carcinoma.md, etc.) can reference this source for genetics context. Full-text extraction would provide specific claims per cancer type.

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] Cancer is significant cause of morbidity/mortality in cats (general framing)
- [x] Field has evolved from cytogenetics to molecular genetics
- [x] High-quality reference genome enables modern research
- [x] Review covers 9 cancer types from genetics perspective
- [x] Comparative oncology with human cancer is a research theme

### not_safe_to_promote_yet

- [ ] Specific mutations per cancer type (need full-text)
- [ ] Genetic testing recommendations
- [ ] Targeted therapy recommendations
- [ ] Prognosis based on genetics
- [ ] Prevalence of specific mutations

### open_questions

1. What specific mutations are documented for each cancer type?
2. Which cancer types have most robust genetic data?
3. What therapeutic implications are discussed?
4. Are there actionable genetic markers for any feline cancer?
5. How do mutation frequencies compare to human cancers?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 5 framework-level claims |
| Evidence level | review (2022) |
| Key contribution | Cross-branch genetics overview, field maturity map |
| Primary gap | Specific mutations need full-text extraction |
| Topic page targets | cancer/index.md (genetics section), multiple branch pages |
| Cross-branch value | High — spans 9 cancer types |
