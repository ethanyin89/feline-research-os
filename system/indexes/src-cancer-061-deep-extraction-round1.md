---
id: src-cancer-061-deep-extraction-round1
type: system
source_id: src-cancer-061
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-061

**Source:** Companion Animal Model in Translational Oncology; Feline Oral Squamous Cell Carcinoma and Canine Oral Melanoma
**Journal:** Biology (MDPI) (2021)
**DOI:** 10.3390/biology11010054
**PMID:** 35053051
**Evidence Level:** review (narrative)

## Phase 0: Context

**Access status:** Open access via MDPI (PMC8773126).

**Source scope:** 2021 review discussing companion animal cancer models for translational oncology, with FOSCC as example for human HNSCC.

**Key contribution:** Summarizes rationale for using companion animal cancers as translational models.

**Critical boundary:** Review/rationale only. Does not validate specific bidirectional translation.

## Phase 1: Sequential Micro-Analysis

### 1.1 Review Scope

| Focus | Example |
|-------|---------|
| Feline | FOSCC as human HNSCC model |
| Canine | Oral melanoma as mucosal melanoma/immunotherapy model |
| Purpose | Advantages/disadvantages of companion animal models |

### 1.2 Model Advantages

| Advantage | Detail |
|-----------|--------|
| Spontaneous | Naturally occurring vs artificially induced |
| Phylogenetic | Closer to humans than mice |
| Body size | More similar to humans |
| Genome | Organization resembles humans |
| Pathology | Shares features with human cancers |
| Drug response | Toxicity/efficacy similar to humans |
| Environment | Shared owner/household exposures |
| Timeline | Shorter lifespan, faster progression |

### 1.3 Model Limitations (implied)

| Limitation | Note |
|------------|------|
| Species differences | Not identical to human |
| Bidirectional translation | Not automatically valid |
| Model selection | Must match specific questions |
| Regulatory | Different approval pathways |

## Phase 2: Theme Reconstruction

### Theme A: Comparative Oncology Rationale

Why companion animals matter:
- Fill gap between mouse models and human trials
- Spontaneous tumor biology
- Immune system intact
- Tumor microenvironment preserved
- More realistic drug exposure

### Theme B: FOSCC as HNSCC Model

FOSCC advantages for HNSCC research:
- Similar anatomic location
- Similar aggressive behavior
- Similar treatment challenges
- May share molecular features
- Faster trial timelines possible

### Theme C: Translation Caveats

What doesn't transfer:
- Exact molecular targets may differ
- Drug metabolism variations
- Regulatory pathways distinct
- Not proof of human efficacy

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/oral-squamous-cell-carcinoma.md

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| OSCC-MODEL2 | FOSCC is used as a translational model for human HNSCC | B | review-level |
| OSCC-MODEL3 | Companion animal cancers offer advantages over mouse models (spontaneous, intact immunity, realistic exposure) | B | general principle |

**Section to update:** Comparative Oncology / Research Models

**Boundary rules:**
- Review-level evidence
- Rationale, not validation
- Does not establish specific molecular parallels
- Does not prove treatment translation

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] FOSCC is discussed as a HNSCC translational model
- [x] Companion animal cancers are spontaneous (not induced)
- [x] Cats/dogs closer to humans than mice phylogenetically
- [x] Shared environments may share risk factors

### not_safe_to_promote_yet

- [ ] Specific FOSCC-HNSCC molecular parallels
- [ ] Treatment response correlations
- [ ] Drug development success rate
- [ ] Regulatory acceptance of companion animal data

### open_questions

1. What specific molecular parallels exist between FOSCC and HNSCC?
2. How often do FOSCC trials predict human HNSCC outcomes?
3. Are there successful bidirectional drug developments?
4. What are the specific limitations for each cancer type?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 2 comparative oncology claims |
| Evidence level | review (narrative) |
| Key contribution | Summarizes companion animal model rationale |
| Primary gap | Specific molecular validation |
| Topic page targets | oral-squamous-cell-carcinoma.md (models) |
| Cross-reference | Complements src-cancer-055 (CK2 trial using FOSCC model) |
