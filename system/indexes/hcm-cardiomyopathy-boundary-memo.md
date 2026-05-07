---
id: system-hcm-cardiomyopathy-boundary-memo
type: system
topic: hcm
last_compiled_at: 2026-04-10
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# HCM Cardiomyopathy-Boundary Memo

- Date: `2026-04-10`
- Scope: `src-hcm-005`, `src-hcm-007`, `src-hcm-021`, `src-hcm-018`

This memo exists to stop the HCM module from quietly becoming:

`the whole feline cardiomyopathy story`

It should not become that.

## Core Takeaway

`HCM is the dominant current feline cardiomyopathy branch, but it should stay visible inside a wider myocardial-disease map rather than absorbing the entire cardiomyopathy module`

## Current Boundary Architecture

### Branch 1: Broad Cardiomyopathy Frame

This branch is mainly carried by:

- `src-hcm-007`
- `src-hcm-021`

Current meaning:

- feline cardiomyopathies are a broader disease family
- HCM is the most common form, but not the only relevant phenotype
- recognition should retain myocardial-disease classification context

### Branch 2: HCM Core Spine

This branch is mainly carried by:

- `src-hcm-001`
- `src-hcm-009`

Current meaning:

- HCM deserves its own core disease module
- phenotype recognition, genetics, remodeling, endpoint hierarchy, and treatment skepticism justify that depth

### Branch 3: Non-HCM Cardiomyopathy Extension

This branch is mainly carried by:

- `src-hcm-005`
- `src-hcm-018`

Current meaning:

- non-HCM cardiomyopathies should remain visible as adjacent disease forms
- extension logic matters because clinical recognition can otherwise be over-HCM-centered
- broader myocardial disease context helps prevent overcompression of feline cardiology into one phenotype

## What The Module Can Already Say

- HCM is the strongest current cardiomyopathy branch in the vault
- HCM should still be modeled as one branch inside a broader feline cardiomyopathy frame
- broader cardiomyopathy classification belongs in recognition and synthesis architecture
- non-HCM cardiomyopathy material is best treated as an extension branch, not merged into the HCM core spine

## What The Module Should Not Yet Say

- there is no safe reason to collapse all feline cardiomyopathy logic into HCM
- there is no safe claim that HCM recognition automatically resolves other feline myocardial phenotypes
- extension branches should not be erased just because HCM is the richest current source cluster

## Best Write-Back Targets

- [risk and recognition](../../topics/hcm/risk-and-recognition.md)
- [synthesis index](../../topics/hcm/synthesis-index.md)
- [navigation](../../topics/hcm/navigation.md)
- [current state dashboard](../../topics/hcm/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for boundary architecture; no, for full cardiomyopathy-classification map`
- smallest durable home: `memo + topic update + dashboard update`

### Reason

- what is repeating:
  HCM keeps pulling the cardiomyopathy module toward one-phenotype centralization
- what becomes clearer:
  the module now separates `broad cardiomyopathy frame`, `HCM core spine`, and `non-HCM extension`
- what is still too thin, if anything:
  non-HCM phenotype depth is still too thin for a full separate cardiomyopathy classification handbook

### Decision

- promote
