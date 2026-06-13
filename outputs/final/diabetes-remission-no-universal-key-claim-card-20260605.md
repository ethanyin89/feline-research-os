---
id: business-diabetes-remission-no-universal-key-claim-card-20260605
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
**Claim:** Feline diabetic remission is real, but no single diet, insulin type, or protocol is a universal remission key.

## Verdict

| Field | Value |
|-------|-------|
| Verdict | **SUPPORTED** |
| Confidence | medium |
| Claim Level | B (Source-Supported) |
| Next Action | promote |

## Key Sources

- `src-diabetes-007`
- `src-diabetes-015`
- `src-diabetes-022`
- `src-diabetes-024`
- `system/indexes/diabetes-remission-boundary-memo.md`

## Evidence Depth

| Metric | Value |
|--------|-------|
| Sources checked | 118 diabetes source cards |
| Matching sources | 2 |
| Matching compiled claims | 1 |
| Deep extracted source cards | 24 |
| Compiled memo support | `DREM2` in `diabetes-remission-boundary-memo.md` |

## Quoted Facts

- `src-diabetes-007`: remission is possible in cats across multiple insulin types and protocols.
- `src-diabetes-007`: no single factor reliably predicts remission in diabetic cats.
- `src-diabetes-007`: overall evidence level was judged moderate to poor.
- `src-diabetes-015`: a low-carbohydrate/low-fiber diet arm had more cats revert to a non-insulin-dependent state in a 16-week canned-diet comparison.
- `src-diabetes-024`: glargine U300 was studied with concurrent low-carbohydrate diet, blocking clean isolation of insulin contribution.

## Source-Supported Conclusions

- `src-diabetes-007`: remission is real and documented, but no single predictor or protocol has strong evidence support.
- `system/indexes/diabetes-remission-boundary-memo.md`: `DREM2` states that current seed evidence does not support a single predictor, diet, insulin type, or protocol as the universal remission key.
- `system/indexes/diabetes-remission-boundary-memo.md`: `DREM4` separates non-insulin-dependent state, insulin-dose reduction, glycemic improvement, and rigorously defined remission.

## Boundary

- This supports remission-boundary discipline, not pessimism about remission.
- Low-carbohydrate diet and insulin protocol choices can matter, but they should not be presented as a universal remission recipe.
- Non-insulin-dependent state, insulin-dose reduction, glycemic improvement, and rigorously defined remission should not be treated as interchangeable endpoints.
- Diabetes corpus maturity is uneven: the 24 seed cards are deep-extracted, but many extension cards are partial and should not drive final protocol ranking yet.

## Missing Evidence

- Full-text extraction of the remission systematic review is needed before exact remission-rate comparisons or predictor tables.
- Extension sources on glargine, remission, and survival/QoL should be source-checked before they change the remission hierarchy.
- A decision-grade treatment protocol comparison would need consistent remission definitions, insulin adjustment rules, diet context, and endocrine-secondary exclusion criteria.

## Verification Path

`system/indexes/diabetes-remission-boundary-memo.md -> raw/papers/src-diabetes-007.md, raw/papers/src-diabetes-015.md, raw/papers/src-diabetes-022.md, raw/papers/src-diabetes-024.md`

