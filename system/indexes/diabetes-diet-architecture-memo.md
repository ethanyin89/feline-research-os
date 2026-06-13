---
id: system-diabetes-diet-architecture-memo
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

# Diabetes Diet Architecture Memo

- Date: `2026-04-24`
- Scope: `src-diabetes-006`, `src-diabetes-015`, `src-diabetes-016`, `src-diabetes-022`, with remission boundary from `src-diabetes-007`

This memo exists because the diet branch is already too complex for one sentence like:

`low carbohydrate diet helps diabetic cats`

That sentence is directionally useful.

It is not specific enough for this vault.

## Core Takeaway

`the safest diet architecture is stage-and-variable separation: prevention versus management, carbohydrate versus fiber versus protein, glycemic control versus insulin independence, and evidence-backed trial findings versus physiology/experience-based guidance`

## Current Diet Layers

### Layer 1: Diet As Cross-Stage Risk And Management Branch

Main source:

- [src-diabetes-006 deep extraction round 1](src-diabetes-006-deep-extraction-round1.md)

Current meaning:

- diet belongs in prevention/risk framing and management framing
- the source explicitly mixes published evidence with clinical experience and physiologic reasoning where direct evidence is thin
- therefore diet claims need evidence labels

### Layer 2: Direct Low-Carbohydrate / Low-Fiber Trial Signal

Main source:

- [src-diabetes-015 deep extraction round 1](src-diabetes-015-deep-extraction-round1.md)

Current meaning:

- 63 diabetic cats were assigned to two canned diet arms over 16 weeks
- both diet groups improved serum glucose and fructosamine
- 22/31 cats in the low-carbohydrate/low-fiber group and 13/32 cats in the moderate-carbohydrate/high-fiber group reverted to a non-insulin-dependent state
- this is the strongest current original-study diet-comparison anchor

Boundary:

- it does not isolate carbohydrate from fiber
- it does not replace the remission systematic review
- non-insulin-dependent state should be tracked separately from final remission definitions

### Layer 3: Low-Carbohydrate Versus High-Fiber Review Boundary

Main source:

- [src-diabetes-016 deep extraction round 1](src-diabetes-016-deep-extraction-round1.md)

Current meaning:

- low-carbohydrate food is treated as remission-favorable
- high-fiber response is not eliminated
- individual clinical judgment remains part of the branch

Boundary:

- do not turn low carbohydrate into a universal rule
- do not erase possible high-fiber responders

### Layer 4: Protein-Emphasis Signal

Main source:

- [src-diabetes-022 deep extraction round 1](src-diabetes-022-deep-extraction-round1.md)

Current meaning:

- 9 cats completed transition to a high-protein low-carbohydrate canned diet
- insulin requirements decreased in 8/9 cats
- insulin injections stopped in 3 cats
- fructosamine-based control was not lost in the current compiled signal

Boundary:

- protein effect and carbohydrate reduction are not isolated
- small completed sample blocks broad diet-rule status

## Working Diet Hierarchy

| Diet question | Current best owner | Safe current read | Boundary |
|---|---|---|---|
| diet across prevention and management | `src-diabetes-006` | diet is cross-stage and evidence-labeled | not all guidance is trial-backed |
| low-carb/low-fiber versus moderate-carb/high-fiber | `src-diabetes-015` | strongest direct diet-comparison signal | not universal remission rule |
| low-carb versus high-fiber debate | `src-diabetes-016` | low-carb favored, high-fiber subgroup preserved | no one-slogan diet page |
| high-protein / low-carb | `src-diabetes-022` | insulin-requirement reduction signal | small sample; protein not isolated |
| remission claims | `src-diabetes-007` | remission real but predictor-weak | diet findings defer to remission boundary |

## What This Memo Changes

The diet branch should no longer be read as:

`low carbohydrate wins`

It should be read as:

`low-carbohydrate evidence is important, but the branch must preserve fiber, protein, body condition, remission-definition, and evidence-quality boundaries`

## Key-Claim Traceability

| Claim ID | Key Claim | Claim Level | Supporting Source IDs | Notes |
|---|---|---|---|---|
| DDIET1 | Diet belongs across feline diabetes prevention, risk, management, glycemic-control, and remission-support framing, not in one treatment slogan. | B | src-diabetes-006 | broad diet architecture |
| DDIET2 | The strongest current direct diet-comparison signal favors low-carbohydrate/low-fiber over moderate-carbohydrate/high-fiber for non-insulin-dependent outcome in one 16-week canned-diet design. | B | src-diabetes-015 | study-design-specific claim |
| DDIET3 | The low-carbohydrate branch should not become a universal diet rule because high-fiber responders, body condition, insulin context, monitoring, and evidence grade remain relevant. | B | src-diabetes-006, src-diabetes-016, src-diabetes-007 | slogan-prevention boundary |
| DDIET4 | High-protein / low-carbohydrate diet has a small insulin-requirement reduction signal, but protein and carbohydrate effects are not isolated. | B | src-diabetes-022 | small-sample diet-variable boundary |
| DDIET5 | Non-insulin-dependent state, insulin-dose reduction, glycemic control, and remission should remain separate endpoints in diet claims. | B | src-diabetes-007, src-diabetes-015, src-diabetes-022 | endpoint-definition boundary |
| DDIET6 | Diet architecture is evidence-safe for branch separation, but not decision-grade for final diet prescription or protocol ranking. | C | src-diabetes-006, src-diabetes-007, src-diabetes-015, src-diabetes-016, src-diabetes-022 | compiled architecture judgment |

## Best Write-Back Targets

- [translation brief](../../topics/diabetes/translation-brief.md)
- [endpoint handbook](../../topics/diabetes/endpoint-handbook.md)
- [risk and recognition](../../topics/diabetes/risk-and-recognition.md)
- [synthesis index](../../topics/diabetes/synthesis-index.md)

## Promotion Judgment

- repeated? `yes`
- structurally clarifying? `yes`
- evidence-safe enough for this layer? `yes, for diet-architecture separation; no, for final diet prescription`
- smallest durable home: `memo + endpoint write-back + translation write-back`

### Decision

- promote
