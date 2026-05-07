---
id: system-diabetes-neuropathy-boundary-memo
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

# Diabetes Neuropathy Boundary Memo

- Date: `2026-04-24`
- Scope: `src-diabetes-004`, `src-diabetes-018`

This memo exists to make diabetic neuropathy a real complication branch rather than a loose clinical-sign aside.

## Core Takeaway

`feline diabetic neuropathy should be represented as a complication mechanism and endpoint branch, not as a treatment claim or a simple plantigrade-posture label`

## Clinical And Pathology Anchor

Main source:

- [src-diabetes-004 deep extraction round 1](src-diabetes-004-deep-extraction-round1.md)

Current source-supported facts:

- 19 diabetic cats were compared with 28 nondiabetic cats
- physical/neurologic exams, electrophysiology, biochemical testing, and nerve/muscle biopsy analysis were used
- diabetic cats showed functional, structural, and biochemical defects
- plantigrade posture was the most notable severe impairment
- sensorimotor neuropathy affected pelvic and thoracic limbs
- Schwann-cell injury and demyelination were prevalent
- axonal degeneration appeared in severe cases

## Microvascular Anchor

Main source:

- [src-diabetes-018 deep extraction round 1](src-diabetes-018-deep-extraction-round1.md)

Current source-supported facts:

- 12 diabetic cats were compared with 7 nondiabetic cats
- diabetic cats had elevated long-term glycemic markers, impaired motor nerve conduction, and decreased myelinated nerve fiber density
- capillary size and luminal area were significantly increased
- vasoconstriction index was significantly decreased

## What Neuropathy Is Allowed To Do In The Module

Neuropathy can:

- anchor chronic complication language
- add motor conduction and tissue-pathology endpoints
- keep diabetes pages from over-focusing on remission and glycemic control alone
- connect clinical signs to electrophysiologic, myelin, Schwann-cell, axonal, and microvascular findings

## What Neuropathy Must Not Do Yet

Neuropathy should not:

- become a routine screening recommendation without fuller evidence
- imply a specific treatment or reversibility claim
- be treated as only plantigrade posture
- be used to rank diabetes treatments by complication prevention

## Operational Rule

When neuropathy is mentioned, label the claim as one of:

- `clinical sign`: plantigrade posture or gait abnormality
- `neurophysiology`: conduction or sensorimotor dysfunction
- `tissue pathology`: myelin, Schwann-cell, axonal, or microvascular change
- `unknown`: reversibility, screening, or treatment effect not yet established

## Best Write-Back Targets

- [mechanism overview](../../topics/diabetes/mechanism-overview.md)
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md)
- [synthesis index](../../topics/diabetes/synthesis-index.md)
- [current state dashboard](../../topics/diabetes/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for complication branch; no, for treatment or reversibility`
- smallest durable home: `memo + endpoint write-back + synthesis write-back`

### Decision

- promote
