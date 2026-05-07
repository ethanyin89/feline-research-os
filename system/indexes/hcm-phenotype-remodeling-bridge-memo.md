---
id: system-hcm-phenotype-remodeling-bridge-memo
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

# HCM Phenotype-Remodeling Bridge Memo

- Date: `2026-04-10`
- Scope: `src-hcm-001`, `src-hcm-009`, `src-hcm-020`, `src-hcm-024`

This memo exists to answer a narrower question than the mechanism overview:

`how should the HCM module connect visible structural phenotype to deeper remodeling logic without flattening them into the same thing?`

## Core Takeaway

`feline HCM should be modeled as structural phenotype first, but that phenotype sits on top of an active remodeling branch rather than a static wall-thickening story`

## Current Bridge Architecture

### Layer 1: Structural Phenotype Front Door

This layer is mainly carried by:

- `src-hcm-001`
- `src-hcm-009`

Current meaning:

- echocardiographic structure is the lead operational entry point
- the phenotype is heterogeneous rather than one uniform hypertrophy pattern
- small-cavity and variable hypertrophy patterns matter before deeper tissue interpretation begins

### Layer 2: Remodeling Biology Beneath The Phenotype

This layer is mainly carried by:

- `src-hcm-020`

Current meaning:

- remodeling is not a passive after-effect
- cardiomyocyte disarray, fibrosis, macrophage-rich interstitial change, and profibrotic signaling belong to the core mechanism branch
- phenotype should be read as the visible surface of deeper biologic remodeling

### Layer 3: End-Stage Remodeled Phenotype

This layer is mainly carried by:

- `src-hcm-024`

Current meaning:

- advanced HCM should not be modeled as simply “more hypertrophy”
- end-stage architecture is characterized by fibrosis, chamber dilation, and vascular change
- pathology-depth belongs in the module because it shows how phenotype evolves

## What The Module Can Already Say

- structural phenotype still leads recognition
- remodeling logic deepens phenotype interpretation rather than replacing it
- end-stage HCM is a remodeled phenotype, not just a more extreme thickness state
- fibrosis now functions as a bridge variable between mechanism and severity architecture

## What The Module Should Not Yet Say

- there is no safe claim that remodeling outranks phenotype in first-pass diagnosis
- there is no safe one-cause story where macrophage biology alone explains all HCM heterogeneity
- pathology-depth should not be mistaken for routine first-wave recognition authority

## Best Write-Back Targets

- [mechanism overview](../../topics/hcm/mechanism-overview.md)
- [endpoint handbook](../../topics/hcm/endpoint-handbook.md)
- [synthesis index](../../topics/hcm/synthesis-index.md)
- [current state dashboard](../../topics/hcm/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for phenotype-remodeling bridge architecture; no, for full causal hierarchy`
- smallest durable home: `memo + topic update + dashboard update`

### Reason

- what is repeating:
  HCM keeps wanting to split into either a pure phenotype story or a pure remodeling story
- what becomes clearer:
  the module now separates `structural phenotype front door`, `remodeling biology beneath it`, and `end-stage remodeled phenotype`
- what is still too thin, if anything:
  full-text remodeling depth and later RV integration are still too thin for stronger mechanistic ranking

### Decision

- promote
