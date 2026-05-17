---
id: topic-obesity-current-state-dashboard
type: topic
topic: obesity
species: feline
disease: obesity
question_type: dashboard
source_ids: [src-obesity-001, src-obesity-004, src-obesity-005, src-obesity-008, src-diabetes-005]
last_compiled_at: 2026-05-17
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-05-17 upgraded after Tier 1 complete (4/87 deep-extracted) and first architecture page written."
owner: codex
status: active
---

# Feline Obesity Current State Dashboard

## State

`compiled starter — Tier 1 complete`

The obesity module now has 4 deep-extracted Tier 1 source cards and its first architecture page. The module can support bounded 5-branch architecture claims: prevalence ranges, risk factor categories, associated condition visibility, diabetes-bridge mechanism, and prevention target framing.

## What Exists

| Layer | Status | Read |
|---|---|---|
| Google Sheet intake | done | 227 non-empty rows classified |
| Obesity candidate set | done | 87 obesity source cards now exist |
| Shared-source control | done | 10 shared existing rows marked for cross-linking after bootstrap |
| Obesity source cards | Tier 1 complete | 4 deep-extracted (001, 004, 005, 008), 40 abstract-weighted, 43 title-only |
| Obesity source index | active | depth map tracks all 87 cards; Tier 1 priorities complete |
| Obesity topic pages | first architecture page | mechanism-overview, index, navigation, dashboard |

## Deep-Extracted Anchors (Tier 1)

| Source | Role | Key Finding |
|---|---|---|
| src-obesity-001 | broad shell | prevalence 11.5-63%, 5-branch architecture, J.S. Rand co-author |
| src-obesity-004 | risk factors | extrinsic (lifestyle/diet) vs intrinsic (genetics/sex/breed) framework |
| src-obesity-005 | prevention | target population: post-gonadectomy kittens 5-12 months |
| src-obesity-008 | diabetes bridge | insulin sensitivity decreases with increasing adiposity |

## 5-Branch Architecture

The module now supports bounded claims across all 5 branches:

| Branch | Anchor | Can Say | Cannot Say Yet |
|--------|--------|---------|----------------|
| Prevalence | src-obesity-001 | range 11.5-63%, geographic variation | specific population estimates |
| Risk Factors | src-obesity-001, 004 | intrinsic vs extrinsic categories | effect-size ranking |
| Pathogenesis | src-obesity-008 | insulin sensitivity decline | other mechanisms |
| Associated Conditions | src-obesity-001, 004 | T2D, musculoskeletal, skin, urinary visibility | causal proof |
| Assessment | src-obesity-001 | body condition evaluation is essential | specific scoring thresholds |

**Prevention layer:** src-obesity-005 identifies post-gonadectomy kittens 5-12 months as the target population. Prevention is framed as preferable to treatment.

## Do Not Say Yet

- do not rank risk factors by effect size
- do not give specific prevalence for any single population
- do not rank weight-loss interventions
- do not make owner-facing feeding or treatment recommendations
- do not cite specific body condition scoring thresholds
- do not use screening or intervention thresholds

## Next Exit Condition

The module has reached `compiled starter` status. Next moves:

1. Write additional architecture pages (risk-and-recognition, prevention, diabetes-bridge) if question density justifies
2. Deep-extract Tier 2 management sources (002, 003, 006, 007, 080) if intervention detail is needed
3. Compile bilingual versions of mechanism-overview
4. Address remaining year metadata gaps (6 cards without DOI)
