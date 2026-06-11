---
id: topic-diabetes-synthesis-index
type: topic
topic: diabetes
species: feline
disease: diabetes mellitus
question_type: synthesis
source_ids: [src-diabetes-001, src-diabetes-002, src-diabetes-003, src-diabetes-004, src-diabetes-005, src-diabetes-006, src-diabetes-007, src-diabetes-008, src-diabetes-009, src-diabetes-010, src-diabetes-011, src-diabetes-012, src-diabetes-013, src-diabetes-014, src-diabetes-015, src-diabetes-016, src-diabetes-017, src-diabetes-018, src-diabetes-019, src-diabetes-020, src-diabetes-021, src-diabetes-022, src-diabetes-023, src-diabetes-024, src-diabetes-025, src-diabetes-085, src-diabetes-118, src-diabetes-119, src-diabetes-120, src-diabetes-121, src-reg-010, src-reg-011, src-reg-012, src-reg-013]
last_compiled_at: 2026-06-11
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
language_qa_notes: "2026-06-11 expanded to 30 diabetes sources + 4 regulatory sources; added insulin signaling deficits, pancreatitis bidirectionality, and comparative model evidence."
owner: codex
status: active
---

# Feline Diabetes Synthesis Index

## Key-Claim Traceability

| ID | Claim | Level | Source ids | Boundary |
|---|---|---|---|---|
| DS1 | Feline diabetes should be treated as a mixed metabolic/endocrine syndrome, not a single remission-protocol story | B | src-diabetes-001, src-diabetes-005, src-diabetes-010, src-diabetes-013, src-diabetes-020, src-diabetes-023 | compiled synthesis; not decision-grade |
| DS2 | Remission is real but current evidence blocks simple protocol ranking | B | src-diabetes-007, src-diabetes-015, src-diabetes-024, src-diabetes-085 | not decision-grade clinical guidance |
| DS3 | SGLT2 is now primary-source anchored for U.S. label/regulatory discussion, but not a treatment winner | B | src-diabetes-011, src-reg-010, src-reg-011, src-reg-012, src-reg-013 | no product superiority claim |
| DS4 | Strong clinical recommendations still require tighter topic/output-level compression and, where needed, official-label precision | C | src-diabetes-001, src-diabetes-024 | not decision-grade |
| DS5 | Feline diabetes is associated with ectopic lipid deposition in liver and skeletal muscle | A | src-diabetes-025 | quoted_fact from 54-cat insulin signaling study |
| DS6 | GLUT-4 and PI3K protein abundance decrease in muscle of diabetic cats, indicating peripheral insulin resistance | A | src-diabetes-025 | molecular mechanism; parallels human T2DM |
| DS7 | Incretin signaling (GLP-1R, GIP-R) is deficient in untreated diabetic cats | B | src-diabetes-025 | therapeutic target implication; not treatment recommendation |
| DS8 | Diabetes-pancreatitis relationship is bidirectional; "brittle" glycemic control indicates concurrent pancreatic inflammation | B | src-diabetes-118 | comorbidity screening rationale |
| DS9 | Feline diabetes has strong comparative value as human T2DM model but model value should not translate directly to cat management | B | src-diabetes-003, src-diabetes-121 | comparative architecture |
| DS10 | Obese diabetic cats require dual-condition management approach (weight loss + glycemic control) | B | src-diabetes-119 | management architecture; full text needed for protocols |

## Current Synthesis

Feline diabetes is best started as a reversible-potential disease with chronic metabolic and endocrine constraints. The expanded 30-source synthesis sharpens the evidence base:

**Core Mechanism (expanded):**
- `src-diabetes-025` (2024): First comprehensive insulin signaling study showing GLUT-4/PI3K deficits in muscle, ectopic lipid deposition, and incretin signaling deficits (GLP-1R, GIP-R)
- Molecular parallels to human T2DM now documented at receptor/signaling level
- Incretin-based therapies (GLP-1 agonists) emerge as potential therapeutic avenue

**Comorbidity Expansion:**
- `src-diabetes-118`: Pancreatitis-diabetes bidirectionality with "brittle" glycemic control phenotype
- `src-diabetes-119`: Obese diabetic cat management review
- `src-diabetes-120`, `src-diabetes-121`: Comparative model value and species-specific corrections

**Synthesis Status:**
- 30 diabetes sources + 4 regulatory sources (34 total)
- Mechanism-overview at HIGH confidence with molecular mechanism evidence
- Treatment ranking and clinical protocols remain gated pending tighter compression
- SGLT2 regulatory layer complete (Bexacat/Senvelgo primary FDA sources)

## First Synthesis Questions

1. What disease model best explains feline diabetes: type-2-like metabolic disease, endocrine-secondary disease, or a mixed clinical syndrome?
2. Which remission claims survive systematic review, given moderate-to-poor evidence quality and no single predictor?
3. How should obesity, hypersomatotropism, and pancreatitis be positioned relative to primary diabetes management?
4. Which diet variables matter most: carbohydrate, fiber, protein, calorie restriction, or palatability/adherence?
5. How should newer SGLT2 and glargine U300 treatment sources be bounded against older insulin/diet evidence?
6. How should UK and Australian Burmese risk signals be combined without overclaiming mechanism or universal prevalence?
7. How should neuropathy and microvascular pathology be represented without turning complication endpoints into treatment claims?
8. Which diet signals are really carbohydrate, fiber, protein, calorie, or adherence signals?

## First Narrow Owner Memos

- [remission boundary memo](../../system/indexes/diabetes-remission-boundary-memo.md)
- [diet architecture memo](../../system/indexes/diabetes-diet-architecture-memo.md)
- [endocrine-secondary diabetes memo](../../system/indexes/diabetes-endocrine-secondary-diabetes-memo.md)
- [pancreatitis comorbidity memo](../../system/indexes/diabetes-pancreatitis-comorbidity-memo.md)
- [SGLT2 safety/regulatory boundary memo](../../system/indexes/diabetes-sglt2-safety-regulatory-boundary-memo.md)
- [SGLT2 primary FDA source memo](../../system/indexes/diabetes-sglt2-primary-fda-source-memo.md)
- [SGLT2 current label control memo](../../system/indexes/diabetes-sglt2-current-label-control-memo.md)
- [SGLT2 label-section comparison memo](../../system/indexes/diabetes-sglt2-label-section-comparison-memo.md)
- [treatment branch comparison memo](../../system/indexes/diabetes-treatment-branch-comparison-memo.md)
- [diagnostic monitoring workup memo](../../system/indexes/diabetes-diagnostic-monitoring-workup-memo.md)
- [obesity body-condition memo](../../system/indexes/diabetes-obesity-body-condition-memo.md)
- [feline diabetic neuropathy boundary memo](../../system/indexes/diabetes-neuropathy-boundary-memo.md)
- [breed-risk synthesis memo](../../system/indexes/diabetes-breed-risk-synthesis-memo.md)

## Promoted Topic Branches

- [diagnostic and monitoring workup](diagnostic-monitoring-workup.md)
- [diet architecture](diet-architecture.md)
- [remission boundaries](remission-boundaries.md)
- [treatment branch map](treatment-branch-map.md)
- [obesity and body condition](obesity-and-body-condition.md)
- [endocrine-secondary diabetes](endocrine-secondary-diabetes.md)
- [pancreatitis comorbidity](pancreatitis-comorbidity.md)
- [neuropathy and complication endpoints](complications-neuropathy.md)
- [epidemiology and breed risk](epidemiology-and-breed-risk.md)
- [SGLT2 label control](sglt2-label-control.md)

## Current Verdict

The first narrow memo layer is now in place and has been extended with treatment comparison, obesity/body-condition, diagnostic/workup, primary FDA SGLT2 source control, current-label control, and label-section comparison. The module has complete seed-scope worksheets, four U.S. SGLT2 regulatory/label source cards, two label-section worksheets, thirteen narrow owners, ten memo-derived topic branches, a first briefing/dossier/slides output set across `working-en / en / zh`, and all 24 paper source cards at explicit full source-card depth with `24/24 deep_extracted` paper-card status.

Next densification should target stronger topic/output-level clinical compression, local label/source-PDF archiving, or non-U.S. regulatory checks only where external output requires it. Strong clinical recommendations still need tighter compression and, where relevant, label-level precision.

## First Output Layer

- [Diabetes briefing round 1 working-en](../../outputs/briefings/out-diabetes-briefing-20260421-round1-working-en.md)
- [Diabetes dossier v1 working-en](../../outputs/dossiers/out-diabetes-dossier-20260421-v1-working-en.md)
- [Diabetes slides v1 working-en](../../outputs/slides/out-diabetes-slides-20260421-v1-working-en.md)
- [Diabetes output language matrix](../../system/indexes/diabetes-output-language-matrix.md)
- [Diabetes source depth map](../../system/indexes/diabetes-source-depth-map.md)
