---
id: business-diabetes-diet-architecture-no-low-carb-slogan-claim-card-20260605
type: business
artifact_kind: claim_card
disease: diabetes
created_at: 2026-06-05
owner: claim_evidence_workbench
status: draft
verification_status: compiled
decision_grade: no
---

# Claim Evidence Card

**Disease:** Diabetes
**Claim:** Low-carbohydrate evidence is important in feline diabetes, but diet claims must preserve fiber, protein, body condition, remission-definition, and evidence-quality boundaries.

## Verdict

| Field | Value |
|-------|-------|
| Verdict | **SUPPORTED** |
| Confidence | medium |
| Claim Level | B (Source-Supported) |
| Next Action | promote |

## Key Sources

- `src-diabetes-006`
- `src-diabetes-015`
- `src-diabetes-016`
- `src-diabetes-022`
- `src-diabetes-007`
- `system/indexes/diabetes-diet-architecture-memo.md`

## Evidence Depth

| Metric | Value |
|--------|-------|
| Sources checked | 122 diabetes-relevant source cards, including regulations |
| Matching source-card branch | diet seed cards |
| Matching compiled claims | `DDIET3`, `DDIET5`, `DDIET6` |
| Deep extracted paper cards | 24 |
| Compiled memo support | `diabetes-diet-architecture-memo.md` |

## Quoted Facts

- `src-diabetes-006`: diet can lower or increase diabetes risk in cats and plays a role in established diabetes management.
- `src-diabetes-006`: some dietary guidance is based on clinical experience and physiologic principles where direct research evidence is lacking.
- `src-diabetes-015`: in one 16-week canned-diet comparison, more low-carbohydrate/low-fiber cats reverted to a non-insulin-dependent state than moderate-carbohydrate/high-fiber cats.
- `src-diabetes-016`: low-carbohydrate foods are remission-favorable in abstract-level framing, while some cats may respond better to high-fiber food.
- `src-diabetes-022`: high-protein / low-carbohydrate diet has a small insulin-requirement reduction signal, but protein and carbohydrate effects are not isolated.

## Source-Supported Conclusions

- `system/indexes/diabetes-diet-architecture-memo.md`: `DDIET3` states that the low-carbohydrate branch should not become a universal diet rule because high-fiber responders, body condition, insulin context, monitoring, and evidence grade remain relevant.
- `system/indexes/diabetes-diet-architecture-memo.md`: `DDIET5` separates non-insulin-dependent state, insulin-dose reduction, glycemic control, and remission.
- `src-diabetes-015`: the direct low-carbohydrate/low-fiber signal is study-design-specific, not a universal diet prescription.
- `src-diabetes-007`: remission claims defer to systematic-review boundary control.

## Boundary

- This supports layered diet architecture, not the slogan `low carbohydrate wins`.
- Low-carbohydrate/low-fiber has a meaningful direct comparison signal, but carbohydrate and fiber are not isolated as single causal variables.
- High-fiber response subgroups should not be erased.
- High-protein / low-carbohydrate evidence should not be generalized beyond small-sample and combined-variable limits.
- Diet claims should not treat non-insulin-dependent state, insulin-dose reduction, glycemic control, and remission as interchangeable endpoints.

## Missing Evidence

- Full-text diet-composition details are needed before protocol-level or product-level diet ranking.
- The diabetes extension corpus contains many partial cards; extension sources should be source-checked before changing the diet hierarchy.
- A decision-grade diet claim would need consistent diet composition, insulin-adjustment rules, body-condition context, remission definitions, and follow-up duration.

## Verification Path

`system/indexes/diabetes-diet-architecture-memo.md -> raw/papers/src-diabetes-006.md, raw/papers/src-diabetes-015.md, raw/papers/src-diabetes-016.md, raw/papers/src-diabetes-022.md, raw/papers/src-diabetes-007.md`

