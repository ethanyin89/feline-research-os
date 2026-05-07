---
id: system-fcv-recognition-architecture-memo
type: system
topic: fcv
last_compiled_at: 2026-04-24
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# FCV Recognition Architecture Memo

- Date: `2026-04-24`
- Scope: `src-fcv-004`, `src-fcv-005`, `src-fcv-006`, `src-fcv-009`, `src-fcv-020`, `src-fcv-021`

This memo exists to stop FCV recognition from shrinking into:

`oral ulcers plus respiratory signs means FCV`

That is too small for the current source pack.

## Core Takeaway

`the current FCV recognition architecture is syndrome-first and composite: oral/upper-respiratory disease leads suspicion, healthy shedding and co-pathogens block symptom-only diagnosis, and ocular or enteric findings remain extension branches`

## Current Recognition Layers

### Layer 1: Core Suspicion Frame

This layer is mainly carried by:

- `src-fcv-004`
- `src-fcv-009`

Current meaning:

- FCV belongs in the oral plus upper-respiratory syndrome frame
- typical FCV language should keep oral ulceration, salivation, and URTD signs visible
- severe systemic disease exists, but it should not replace the common first recognition frame

Boundary:

- positive virologic detection still needs context because carrier-state shedding remains real
- generic `cat flu` shorthand is too blunt for FCV recognition

### Layer 2: Epidemiology / Healthy-Shedding Control

This layer is mainly carried by:

- `src-fcv-005`
- `src-fcv-006`

Current meaning:

- healthy cats can carry or shed FCV
- respiratory presentations need co-pathogen-aware interpretation
- geographic strain structure may matter when reading prevalence or vaccine-fit claims
- oral-disease-heavy findings may discriminate better than a flat classical-URTD list

Boundary:

- symptom cluster does not equal etiologic closure
- local epidemiology does not automatically generalize everywhere

### Layer 3: Ocular Extension

This layer is mainly carried by:

- `src-fcv-021`

Current meaning:

- ocular-surface disease is a real FCV recognition extension branch
- ocular findings can enrich FCV suspicion inside the right clinical context
- one deep-extracted ocular anchor now supports this branch directly

Boundary:

- ocular disease does not displace FHV-1 or other pathogen differentials
- this is an extension branch, not the whole recognition core

### Layer 4: Enteric Extension

This layer is mainly carried by:

- `src-fcv-020`

Current meaning:

- FCV-enteric association should stay visible as a possible extension branch
- one deep-extracted enteric anchor now supports this branch directly
- the enteric branch is still thinner than the oral/respiratory branch

Boundary:

- do not promote FCV into a routine feline-enteritis lead cause from the current compiled layer

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| FCR1 | FCV suspicion should start with oral and upper-respiratory syndrome recognition | B | src-fcv-004, src-fcv-009 | not confirmation logic |
| FCR2 | Healthy shedding and co-pathogens make FCV recognition a composite interpretation problem | B | src-fcv-005, src-fcv-006 | not whole-population prevalence claim |
| FCR2a | Oral-disease-heavy findings are more discriminating than a flat classical-URTD symptom list in the current field anchor | B | src-fcv-006 | not universal symptom rule |
| FCR3 | Ocular disease is a real FCV extension branch | B | src-fcv-021 | not sole-cause claim |
| FCR4 | Enteric association should remain visible but subordinate to the respiratory/oral recognition core | B | src-fcv-020 | not primary-enteritis framing |

## What The Module Can Say Safely

- FCV recognition should start with syndrome awareness, not with one test or one lesion
- oral/respiratory disease remains the core FCV frame
- healthy shedding and co-pathogens are central controls against overdiagnosis
- the current best field anchor gives extra weight to oral-disease-heavy findings over a flat URTD list
- one deep-extracted ocular-recognition anchor now supports keeping ocular-surface disease visible without turning it into a shortcut
- one deep-extracted enteric-recognition anchor now supports keeping enteric FCV visible without promoting it into a front-door shortcut
- ocular and enteric signals belong in extension routing rather than being erased

## What The Module Should Not Say Yet

- do not equate FCV-compatible signs with FCV confirmation
- do not erase co-pathogen structure in feline respiratory disease
- do not turn ocular or enteric signals into new FCV front-door shortcuts
- do not write one prevalence number as if it applies across regions and settings

## Best Reuse Targets

- [risk and recognition](../../topics/fcv/risk-and-recognition.md)
- [current state dashboard](../../topics/fcv/current-state-dashboard.md)
- [index](../../topics/fcv/index.md)
- [navigation](../../topics/fcv/navigation.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for recognition architecture; no, for final diagnostic workup claims`
- smallest durable home: `memo + recognition write-back + dashboard write-back`

### Decision

- promote
