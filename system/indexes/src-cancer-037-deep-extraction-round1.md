---
id: src-cancer-037-deep-extraction-round1
type: system
source_id: src-cancer-037
extraction_round: 1
created_at: 2026-06-05
owner: claude
status: deep_extracted
---

# Deep Extraction Worksheet: src-cancer-037

**Source:** A new detection method for canine and feline cancer using the olfactory system of nematodes
**Journal:** Biochemical and Biophysical Research Communications Reports (2022, Open Access)
**DOI:** 10.1016/j.bbrep.2022.101332
**PMID:** 36111250
**Evidence Level:** original-study

## Phase 0: Context

**Access status:** Open access. Full abstract available.

**Source scope:** 2022 validation study of N-NOSE (nematode-based cancer screening) for dogs and cats using C. elegans chemotaxis to urine samples.

**Key contribution:** Demonstrates proof-of-concept for non-invasive cancer screening using nematode olfactory system.

**Conflict of interest:** Authors are employees of Hirotsu Bio Science Inc. (test developer). Requires independent validation.

## Phase 1: Sequential Micro-Analysis

### 1.1 Technology Overview

| Component | Description |
|-----------|-------------|
| Test name | N-NOSE (Nematode-NOSE) |
| Organism | C. elegans |
| Sample type | Urine |
| Principle | Chemotaxis — nematodes move toward or away from cancer-associated odors |
| Human status | Commercially available for 15 cancer types |

### 1.2 Study Design

| Parameter | Value |
|-----------|-------|
| Species | Canine + Feline |
| Sample type | Urine |
| Comparison | Cancer patients vs healthy controls |
| Analysis | ROC analysis with AUC |

### 1.3 Results — Feline

| Metric | Dilution 1 | Dilution 2 |
|--------|-----------|-----------|
| AUC | 0.7667 | 0.9000 |
| p-value | < 0.04 | — |

**Interpretation:**
- AUC 0.77-0.90 indicates moderate to good discrimination
- Dilution 2 performed better (AUC 0.90)
- Statistically significant difference from healthy controls

### 1.4 Comparison to Canine

| Metric | Dogs | Cats |
|--------|------|------|
| AUC range | 0.79-0.81 | 0.77-0.90 |
| p-value | < 0.01 | < 0.04 |
| Best dilution | Similar | Dilution 2 better |

## Phase 2: Theme Reconstruction

### Theme A: Non-Invasive Cancer Screening

N-NOSE represents a paradigm shift:
- **Current screening:** Requires imaging, blood draws, or biopsies
- **N-NOSE:** Urine collection only (non-invasive)
- **Potential use:** Annual wellness screening
- **Early detection:** May catch cancers before symptoms

### Theme B: Pan-Cancer Detection

Unlike specific biomarkers:
- N-NOSE detects "cancer odor" generally
- May detect multiple cancer types simultaneously
- Does not specify cancer location (requires follow-up)
- Could serve as initial triage

### Theme C: Evidence Limitations

Must interpret with caution:
1. **Conflict of interest:** Company-funded research
2. **Small sample:** Not specified in abstract
3. **Single study:** No independent replication yet
4. **Specificity unknown:** False positive rate?
5. **Cancer types:** Which feline cancers detected?

### Theme D: Comparative Diagnostics

| Test | Sample | Invasiveness | AUC | Status |
|------|--------|--------------|-----|--------|
| N-NOSE | Urine | None | 0.77-0.90 | Research |
| Liquid biopsy | Blood | Low | Variable | Emerging |
| Imaging | — | Moderate | High | Standard |
| Biopsy | Tissue | High | Reference | Standard |

## Phase 2.5: Write-Back Implications

### Target: topics/cancer/index.md (diagnostics section)

**Claims to add/update:**

| ID | Claim | Level | Boundary |
|----|-------|-------|----------|
| DX-EXP1 | N-NOSE nematode-based urine test shows AUC 0.77-0.90 for feline cancer | B | single study, COI |
| DX-EXP2 | Non-invasive cancer screening using C. elegans chemotaxis is under development | C | research direction |

**Section to update:** Emerging Diagnostics / Cancer Screening

**Boundary rules:**
- Single study with conflict of interest
- Not a clinical recommendation
- Research/emerging technology only
- Needs independent validation

## Phase 3: Promotion Check

### safe_to_promote_now

- [x] N-NOSE uses C. elegans chemotaxis to urine
- [x] AUC 0.77-0.90 reported for feline cancer detection
- [x] Test is non-invasive (urine only)
- [x] Already commercially available for human use

### not_safe_to_promote_yet

- [ ] Clinical recommendation for cancer screening
- [ ] Specific cancer type detection claims
- [ ] Sensitivity/specificity for clinical use
- [ ] Cost-effectiveness comparison
- [ ] Independent validation results

### open_questions

1. Which feline cancer types can N-NOSE detect?
2. What is the false positive rate (specificity)?
3. Has independent validation been performed?
4. Is N-NOSE commercially available for veterinary use?
5. What is the cost compared to standard screening?
6. What is the optimal screening protocol (annual? risk-based?)?

## Extraction Summary

| Metric | Value |
|--------|-------|
| Claims extracted | 2 diagnostic technology claims |
| Evidence level | original-study (2022) |
| Key contribution | Non-invasive screening proof-of-concept |
| Primary gap | Independent validation, specificity data |
| Topic page targets | index.md (emerging diagnostics) |
| Commercial status | Human: available; Veterinary: research stage |
| Conflict of interest | Yes — company employees authored |
