---
id: system-hcm-diagnostic-workup-memo
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

# HCM Diagnostic-Workup Memo

- Date: `2026-04-10`
- Scope: `src-hcm-001`, `src-hcm-007`, `src-hcm-008`, `src-hcm-009`, `src-hcm-010`, `src-hcm-013`, `src-hcm-021`, `src-hcm-023`

This memo exists to stop the HCM recognition branch from drifting into one-test or one-tool thinking.

It does four narrower things:

1. separate suspicion, confirmation, and overclaim
2. keep structural phenotype above biomarker shortcuts
3. separate screening augmentation from true confirmation
4. keep genotype and age pressure inside workup interpretation without letting them replace phenotype definition

## Core Takeaway

`feline HCM workup should be modeled as structure-first confirmation plus bounded screening augmentation, not as a flat mix of echo, biomarkers, and algorithms`

## Current Working Architecture

### Layer 1: Clinical Suspicion

This is where workup starts:

- general cardiomyopathy framing
- phenotype suspicion
- age and genotype pressure context

This layer is mainly carried by:

- `src-hcm-001`
- `src-hcm-007`
- `src-hcm-008`

### Layer 2: Structural Confirmation

This is where the workup becomes operationally decisive:

- echocardiographic phenotype definition
- gross morphometric discrimination
- exclusion-aware interpretation of mild to moderate thickening

This layer is mainly carried by:

- `src-hcm-001`
- `src-hcm-009`
- `src-hcm-013`

### Layer 3: Screening Augmentation

This is where additional tools can help route or strengthen suspicion:

- NT-proBNP
- AI or computational detection logic

This layer is mainly carried by:

- `src-hcm-010`
- `src-hcm-023`

### Layer 4: Overclaim Boundary

This is the part the module most needs to defend:

- biomarker support is not the same as structural confirmation
- severe-disease flags are not the same as mild-disease screening competence
- computational augmentation is not the same as routine diagnostic authority
- genotype pressure is not the same as current confirmed phenotype

## Current Diagnostic Branches

### Branch 1: Structural Phenotype

What current sources support:

- echocardiography remains the lead confirmatory branch
- phenotype is heterogeneous, not one uniform wall-thickening pattern
- mild to moderate thickening remains an exclusion-aware zone rather than automatic certainty

What the vault can say safely:

- HCM confirmation should remain structure-first

What the vault should not say:

- do not treat one thickness signal or one nonstructural measure as equivalent to confirmatory phenotype definition

### Branch 2: Screening Augmentation

What current sources support:

- NT-proBNP can help identify severe disease burden
- augmentation tools may help routing or suspicion-building
- these tools are not interchangeable with structural confirmation

What the vault can say safely:

- screening augmentation belongs in the workup, but below confirmation

What the vault should not say:

- do not write NT-proBNP as a reliable mild-to-moderate HCM screen
- do not write AI as if it already outranks structural workup

### Branch 3: Genotype- and Age-Aware Interpretation

What current sources support:

- age-related penetrance matters
- genetic pressure can sharpen suspicion and risk interpretation
- genotype context should modify interpretation, not replace phenotype confirmation

What the vault can say safely:

- workup should remain age-aware and genotype-aware

What the vault should not say:

- do not promote mutation status into standalone diagnostic certainty

## Current Working Hierarchy

| Workup Branch | Current Position In Vault | Notes |
|---|---|---|
| Structural phenotype confirmation | strongest current operational branch | carried by review and echo/morphometry anchors |
| Composite suspicion-building | core framing rule | cardiomyopathy context plus phenotype suspicion |
| Screening augmentation | useful but bounded | severe-disease flags and computational routing, not confirmation |
| Genotype- and age-aware interpretation | contextual modifier | useful, but below structural definition |

## What This Branch Is Not Allowed To Become

- It is not allowed to become a biomarker-first diagnosis story.
- It is not allowed to flatten screening augmentation into confirmatory authority.
- It is not allowed to let genotype context replace structural phenotype definition.
- It is not allowed to treat AI or computational logic as routine first-wave authority.

## What The Vault Can Now Say More Clearly

1. HCM workup is structure-first by design, not by lack of imagination.
2. Screening augmentation belongs in the module, but in a lower branch than confirmation.
3. Mild-to-moderate thickening needs exclusion-aware interpretation.
4. Age and genotype pressure modify workup interpretation without becoming diagnosis by themselves.

## Best Reuse Targets

- [risk and recognition](../../topics/hcm/risk-and-recognition.md)
- [endpoint handbook](../../topics/hcm/endpoint-handbook.md)
- [synthesis index](../../topics/hcm/synthesis-index.md)
- [current state dashboard](../../topics/hcm/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for workup hierarchy; no, for one-test shortcut claims`
- smallest durable home: `memo + topic update + dashboard update`

### Reason

- what is repeating:
  HCM workup questions keep arriving as if echo, biomarkers, and AI sit in one flat diagnostic bucket
- what becomes clearer:
  the branch now separates `clinical suspicion`, `structural confirmation`, `screening augmentation`, and `overclaim boundary`
- what is still too thin, if anything:
  later AI and novel-biomarker ranking is still too thin for stronger hierarchy claims

### Decision

- promote
