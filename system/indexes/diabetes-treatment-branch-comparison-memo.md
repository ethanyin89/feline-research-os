---
id: system-diabetes-treatment-branch-comparison-memo
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

# Diabetes Treatment Branch Comparison Memo

- Date: `2026-04-24`
- Scope: `src-diabetes-006`, `src-diabetes-007`, `src-diabetes-008`, `src-diabetes-011`, `src-diabetes-015`, `src-diabetes-016`, `src-diabetes-017`, `src-diabetes-022`, `src-diabetes-024`, `src-reg-010`, `src-reg-011`

This memo exists to stop feline diabetes treatment from becoming a flat list of interventions.

## Core Takeaway

`the current diabetes treatment map has no safe single winner; the right structure is branch separation by role, evidence type, candidate selection, endpoint, and safety boundary`

## Current Treatment Branches

### Branch 1: Diet Architecture

Current owner:

- [diabetes diet architecture memo](diabetes-diet-architecture-memo.md)

Current role:

- foundational management branch
- affects glycemic control, insulin requirement, body condition, and remission-related endpoints
- strongest direct diet-comparison signal comes from `src-diabetes-015`

Boundary:

- not a universal diet prescription
- low carbohydrate, fiber, protein, and calorie restriction must remain separated

### Branch 2: Insulin Protocol / Glargine U300

Current owner:

- [src-diabetes-024 deep extraction round 1](src-diabetes-024-deep-extraction-round1.md)

Current role:

- insulin remains a core treatment branch
- glargine U300 has a promising short-term prospective-study signal
- hypoglycemia interpretation needs both biochemical and clinical-sign layers

Boundary:

- no superiority claim over other insulin protocols
- suspected hypersomatotropism exclusions make endocrine-secondary screening relevant to interpretation

### Branch 3: SGLT2 Inhibitors

Current owners:

- [diabetes SGLT2 safety/regulatory boundary memo](diabetes-sglt2-safety-regulatory-boundary-memo.md)
- [diabetes SGLT2 primary FDA source memo](diabetes-sglt2-primary-fda-source-memo.md)
- [Bexacat FDA FOI source](../../raw/regulations/src-reg-010-bexacat-fda-foi.md)
- [Senvelgo FDA FOI source](../../raw/regulations/src-reg-011-senvelgo-fda-foi.md)

Current role:

- real U.S. FDA-approved product branch for otherwise healthy cats with diabetes mellitus not previously treated with insulin
- oral route changes operational workflow
- candidate selection and ketoacidosis monitoring dominate the branch

Boundary:

- not for complicated or insulin-dependent diabetes by default
- not a route-convenience winner
- not a global regulatory map

### Branch 4: Alpha-Glucosidase Inhibitor Plus Low-Carbohydrate Diet

Current owner:

- [src-diabetes-008 deep extraction round 1](src-diabetes-008-deep-extraction-round1.md)

Current role:

- older adjunct-plus-diet treatment signal
- useful for non-insulin adjunct history

Boundary:

- intervention attribution is confounded by diet, drug, and insulin adjustment
- should not become an independent acarbose efficacy claim without full-text review

### Branch 5: Incretin / GLP-1 / DPP-4 Frontier

Current owner:

- [src-diabetes-017 deep extraction round 1](src-diabetes-017-deep-extraction-round1.md)

Current role:

- innovation map before the SGLT2 era
- GLP-1-related mechanisms include satiety, gastric emptying, glucose-dependent insulin support, and glucagon suppression

Boundary:

- not a mature feline treatment protocol owner
- should remain frontier/transition logic until stronger feline clinical evidence is ingested

### Branch 6: Remission Endpoint Control

Current owner:

- [diabetes remission boundary memo](diabetes-remission-boundary-memo.md)

Current role:

- controls treatment-enthusiasm language
- keeps remission visible but evidence-bounded

Boundary:

- no single factor predicts remission
- no treatment branch can claim universal remission authority from current seed evidence

## Branch Comparison Table

| Branch | Current Role | Strongest Safe Claim | Main Boundary |
|---|---|---|---|
| diet architecture | foundational management | diet affects glycemic and insulin-requirement endpoints | not a universal prescription |
| insulin / glargine U300 | core pharmacologic branch | promising short-term glargine U300 signal | no comparative superiority |
| SGLT2 inhibitors | FDA-approved oral product branch | approved U.S. options for selected otherwise healthy insulin-naive cats | ketoacidosis risk and candidate selection |
| alpha-glucosidase inhibitor adjunct | historical adjunct-plus-diet branch | combined intervention signal | independent drug effect not isolated |
| incretin / GLP-1 frontier | innovation branch | plausible metabolic mechanisms | not routine protocol authority |
| remission | endpoint/control branch | real but evidence-fragile endpoint | no single predictor or protocol |

## What The Module Can Say Now

- diet, insulin, SGLT2 inhibitors, and adjunct/frontier branches should be separated
- SGLT2 products now have primary U.S. regulatory source cards
- remission language should sit above treatment branches as a boundary, not inside one preferred protocol
- treatment comparisons should include endocrine-secondary and pancreatitis comorbidity checks

## What The Module Should Not Say Yet

- do not rank treatments by superiority
- do not promote oral route as inherently better
- do not compare Bexacat and Senvelgo as winners
- do not collapse non-insulin-dependence into standardized remission without definition checks
- do not write owner-facing clinical instructions from the current compiled layer alone

## Best Write-Back Targets

- [translation brief](../../topics/diabetes/translation-brief.md)
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md)
- [regulatory brief](../../topics/diabetes/regulatory-brief.md)
- [synthesis index](../../topics/diabetes/synthesis-index.md)
- [current state dashboard](../../topics/diabetes/current-state-dashboard.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for branch comparison; no, for final treatment ranking`
- smallest durable home: `memo + translation write-back + regulatory write-back`

### Decision

- promote
