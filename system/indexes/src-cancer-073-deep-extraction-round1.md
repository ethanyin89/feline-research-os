---
id: src-cancer-073-deep-extraction-round1
type: system
source_id: src-cancer-073
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-073

**Source:** Expression of mPGES1 and p16 in feline and human oral squamous cell carcinoma: A comparative oncology approach
**Journal:** Veterinary and Comparative Oncology (2024)
**DOI:** 10.1111/vco.12967
**PMID:** 38378135
**Evidence Level:** original-study (comparative pathology)

## Phase 0: Context

**Access status:** Abstract available from PubMed.

**Source scope:** 2024 comparative study of mPGES1 and p16 expression in 45 FOSCC vs 42 HOSCC cases, examining species-specific expression patterns.

**Key contribution:** Highlights both similarities and differences between FOSCC and HOSCC, informing comparative oncology model validity.

**Critical boundary:** Pathological characterization. Different risk factors between species.

## Phase 1: Sequential Micro-Analysis

### 1.1 Study Design

| Parameter | Value |
|-----------|-------|
| FOSCC samples | 45 |
| HOSCC samples | 42 |
| Markers | mPGES1, p16, COX-2, CD147 |
| Goal | Compare expression patterns between species |

### 1.2 p16 Expression

| Species | Finding |
|---------|---------|
| HOSCC | High p16 in tumor cells vs adjacent stroma/epithelium |
| FOSCC | Similar trend but not statistically significant |

**Context:** p16 is a marker of HPV-driven cancer in humans. HPV causation not demonstrated in cats.

### 1.3 mPGES1 Expression

| Species | Pattern |
|---------|---------|
| FOSCC | Higher in adjacent epithelium than tumor/stroma |
| HOSCC | More similar between compartments |

**mPGES1:** Microsomal prostaglandin E synthase 1, downstream of COX-2 in inflammation pathway.

### 1.4 CD147 Correlation

| Finding | Detail |
|---------|--------|
| HOSCC | High CD147 more common in high mPGES1 group |
| Implication | Inflammation and invasion pathways linked |

## Phase 2: Theme Reconstruction

### Theme A: Species Differences

FOSCC vs HOSCC differ:
- p16 patterns differ (HPV-relevant in humans, not cats)
- mPGES1 compartment distribution differs
- Risk factors likely different
- Model has limitations

### Theme B: Inflammation Pathways

Shared inflammation features:
- COX-2 expressed in both
- mPGES1 (downstream of COX-2) expressed
- Inflammation relevant to pathogenesis
- Potential therapeutic target

### Theme C: Comparative Model Nuance

FOSCC as HOSCC model:
- Some pathway similarities
- But different etiologies
- HPV-driven HOSCC not paralleled in cats
- Must specify which human OSCC subtype is modeled

### Theme D: p16 and HPV

HPV-related differences:
- p16 overexpression = HPV marker in humans
- HPV-positive HOSCC has better prognosis
- HPV role in FOSCC not established
- Different clinical implications

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/oral-squamous-cell-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| OSCC-COMP1 | FOSCC and HOSCC show different p16 expression patterns | A | comparative pathology |
| OSCC-COMP2 | mPGES1 expression differs between FOSCC tumor and adjacent epithelium | A | n=45 |
| OSCC-COMP3 | HPV-driven HOSCC has different biology than FOSCC | B | model limitation |
| OSCC-PATH1 | mPGES1 (COX-2 pathway) is expressed in FOSCC | A | inflammation marker |

**Section to update:** Comparative Oncology / Pathogenesis

**Boundary rules:**
- Comparative study highlights differences
- FOSCC may model HPV-negative HOSCC better than HPV-positive
- Inflammation pathways shared
- Not treatment guidance

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FOSCC and HOSCC differ in p16 expression patterns
- [x] mPGES1 is expressed in FOSCC
- [x] Species-specific risk factors likely contribute to differences
- [x] FOSCC model has limitations for HPV-driven HOSCC

### not_safe_to_promote_yet

- [ ] Treatment implications of expression patterns
- [ ] Prognostic value of mPGES1 or p16 in FOSCC
- [ ] COX-2/mPGES1 inhibitor efficacy in FOSCC
- [ ] HPV role in FOSCC (not established)

### open_questions

1. Does FOSCC better model HPV-negative human OSCC?
2. Is mPGES1 a therapeutic target in FOSCC?
3. What are the actual risk factors for FOSCC (not HPV)?
4. Does COX-2/mPGES1 inhibition help FOSCC?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 4 comparative pathology claims |
| Evidence level | original-study (comparative, n=45+42) |
| Key contribution | Species-specific expression patterns documented |
| Primary gap | Therapeutic implications |
| Topic page targets | oral-squamous-cell-carcinoma.md (comparative) |
| Cross-reference | Complements src-cancer-061 (comparative oncology review) |
