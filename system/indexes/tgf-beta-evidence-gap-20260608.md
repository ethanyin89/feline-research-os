---
id: system-tgf-beta-evidence-gap-20260608
type: system
topic: ckd
question_type: evidence-gap
source_ids: [src-ckd-011, src-ckd-050, src-ckd-021, src-ckd-024]
language: en
last_compiled_at: 2026-06-08
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# TGF-beta Evidence Gap Analysis, 2026-06-08

## Purpose

Document the current TGF-beta evidence state in the CKD corpus and define search targets for future material acquisition.

This memo was triggered by the 2026-06-06 handoff instruction:

> For TGF-beta, prioritize CKD-derived or in-vivo feline validation rather than another general fibrosis review.

## Current Evidence Inventory

| Source | Year | Type | TGF-beta Content | Limitation |
|--------|------|------|------------------|------------|
| src-ckd-011 | - | review | Fibrosis mediator framing, TGF-beta as pathway | Not feline-specific data |
| src-ckd-050 | 2024 | original study | Feline renal fibroblasts respond to TGF-beta1 | In vitro, normal cat kidneys, not CKD-derived |
| src-ckd-021 | 2021 | review | Mentions TGF-beta in growth-factor signaling | Focus is RAAS/MR, not TGF-beta primary |
| src-ckd-024 | 2022 | review | Lists TGF-beta1 as a biomarker keyword | No substantial TGF-beta evidence |

## Current TGF-beta Entity State

The `mechanism-tgf-beta` entity correctly states:

> The next evidence gap is CKD-derived or in-vivo feline validation.

Current boundaries:
- TGF-beta is positioned as a mediator-level mechanism, not the primary backbone (fibrosis holds that)
- src-ckd-050 adds in-vitro pathway plausibility but does not establish CKD causation or treatment efficacy
- The entity is correctly bounded as "not a validated feline CKD intervention target"

## Evidence Gap Definition

### What Is Missing

1. **CKD-derived feline tissue evidence**
   - TGF-beta expression or pathway activation measured in kidneys from cats with spontaneous CKD
   - Comparison between CKD and normal cat kidneys

2. **In-vivo feline CKD study**
   - TGF-beta pathway measurement during CKD progression in live cats
   - Association between TGF-beta levels and disease stage, progression rate, or outcomes

3. **Feline intervention data**
   - Any therapeutic targeting of TGF-beta pathway in cats with CKD
   - Would require at minimum safety data, ideally efficacy signal

### What Would NOT Address This Gap

- Another general fibrosis review citing non-feline species
- Additional in-vitro studies from normal cat kidneys
- Human or rodent TGF-beta CKD data (already covered indirectly)

## Search Priority Criteria

When acquiring new CKD material, prioritize sources that provide:

| Priority | Source Type | Example Criteria |
|----------|-------------|------------------|
| High | Feline CKD tissue study | "TGF-beta" + "feline" + "chronic kidney disease" + "tissue" or "biopsy" |
| High | Feline CKD progression study | TGF-beta measurement in longitudinal feline CKD cohort |
| Medium | Cross-species review with feline data | Must include actual feline CKD TGF-beta measurements |
| Low | Additional in-vitro | Only if using CKD-derived feline cells |

## Decision

**No TGF-beta entity or treatment page upgrade is justified until CKD-derived or in-vivo feline evidence becomes available.**

Current TGF-beta position is correctly bounded:
- Mediator-level mechanism
- Pathway plausibility established (src-ckd-050)
- Not validated as intervention target
- Below fibrosis in the mechanism hierarchy

## Future Material Check

When processing new CKD sources, flag for TGF-beta gap review if the source contains:
- Feline kidney tissue/biopsy with TGF-beta measurement
- Feline CKD cohort with TGF-beta biomarker data
- Any feline CKD intervention targeting TGF-beta pathway

## One-Sentence Summary

TGF-beta has in-vitro feline pathway support but requires CKD-derived or in-vivo feline validation before any mechanism or treatment page upgrade.
