---
id: system-diabetes-breed-risk-synthesis-memo
type: system
topic: diabetes
last_compiled_at: 2026-04-24
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# Diabetes Breed-Risk Synthesis Memo

- Date: `2026-04-24`
- Scope: `src-diabetes-009`, `src-diabetes-012`, with secondary context from `src-diabetes-023`

This memo exists because Burmese risk appears in two different population frames and should be synthesized without becoming an individual-cat prediction rule.

## Core Takeaway

`Burmese predisposition is a durable early risk signal across UK and Australian sources, but denominator differences block global prevalence or mechanism claims`

## UK Insured-Population Anchor

Main source:

- [src-diabetes-009 deep extraction round 1](src-diabetes-009-deep-extraction-round1.md)

Current source-supported facts:

- diabetes prevalence was 1 in 230 cats in a UK insured population
- Burmese cats were 3.7 times more likely to develop diabetes than non-pedigree cats in that population
- univariate risk factors included male sex, neuter status, inactivity, weight at least 5 kg, and corticosteroid history
- a multivariate tree model identified gender as the most important overall risk factor

## Australian Feline-Clinic Anchor

Main source:

- [src-diabetes-012 deep extraction round 1](src-diabetes-012-deep-extraction-round1.md)

Current source-supported facts:

- the study included 12,576 cats and 93 diabetes cases over 5 years
- five-year period prevalence was 7.4 per 1000 cats
- Burmese cats had a period prevalence of 22.4 per 1000 cats
- mean age at first diagnosis was higher in Burmese cats than domestic short/longhaired cats

## Secondary Context

`src-diabetes-023` adds cross-species pancreatic disease and DKA context, but it should not lead feline-specific risk synthesis because its framing is broader than feline-only diabetes.

## Current Risk Interpretation

The module can safely say:

- Burmese predisposition appears in both UK and Australian sources
- male sex, neuter status, inactivity, weight, and corticosteroid history are UK risk-factor signals
- population denominators matter
- risk-factor signals are not causality proofs

The module should not say:

- Burmese risk has a proven mechanism
- UK insured prevalence equals Australian clinic period prevalence
- breed risk can be applied as an individual-cat prediction rule
- cross-species diabetes context outranks feline-only epidemiology

## Denominator Rule

Always attach the denominator:

| Claim | Required Denominator |
|---|---|
| UK prevalence | insured cat population |
| UK Burmese odds | Burmese versus non-pedigree within insured-population frame |
| Australian period prevalence | two feline-only clinics over 5 years |
| Australian Burmese prevalence | Burmese cats within that clinic denominator |
| cross-species risk context | background context only |

## Best Write-Back Targets

- [risk and recognition](../../topics/diabetes/risk-and-recognition.md)
- [current state dashboard](../../topics/diabetes/current-state-dashboard.md)
- [synthesis index](../../topics/diabetes/synthesis-index.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for denominator-aware breed-risk synthesis; no, for mechanism or prediction`
- smallest durable home: `memo + recognition write-back + dashboard write-back`

### Decision

- promote
