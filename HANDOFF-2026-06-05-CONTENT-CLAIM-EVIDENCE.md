# Handoff: Content Claim Evidence Workbench Pass

Date: 2026-06-05
Branch: `idea-chatacademia-research-workbench`
Status: content-side execution after `/autoplan` business-critical plan

## What Happened

The business-critical plan already had a completed `/autoplan` review in:

- `PLAN-business-critical-feline-research-os.md`

So this pass did not re-run the full plan review. It executed the approved content-side P0 direction:

```text
question -> evidence map -> decision artifact -> business action
```

## Files Changed

### Claim Evidence Logic

- `scripts/claim_evidence.py`

Changes:

- Claim verification now reads disease-specific compiled Key-Claim Traceability tables from:
  - `topics/{disease}/synthesis-index.md`
  - `system/indexes/{disease}-*.md`
- Claim verification now also loads disease-relevant regulatory source cards from `raw/regulations/src-reg-*.md`.
- Matching compiled claims are included in:
  - verdict calculation,
  - key sources,
  - source-supported conclusions,
  - evidence depth.
- Boundary extraction was tightened:
  - source-card limits and cautionary evidence become business-use boundaries,
  - direct contradictions can downgrade verdicts,
  - generic “no explicit boundary” fallback was replaced with a non-decision-grade warning.

Why it matters:

The verifier now uses the repo’s actual content architecture, not just fuzzy source-card matching.

`scripts/business_value_eval.py` now validates `src-reg-*` source IDs against `raw/regulations/` using prefix matching, because regulation source filenames include descriptive suffixes.

### New Business Artifacts

Added:

- `outputs/business/ckd-sdma-primary-monitoring-claim-card-20260605.md`
- `outputs/business/ckd-phosphorus-diet-vs-binder-claim-card-20260605.md`
- `outputs/business/fip-gs441524-baseline-route-testing-claim-card-20260605.md`
- `outputs/business/diabetes-remission-no-universal-key-claim-card-20260605.md`
- `outputs/business/diabetes-sglt2-label-boundary-claim-card-20260605.md`
- `outputs/business/diabetes-diet-architecture-no-low-carb-slogan-claim-card-20260605.md`

Artifact decisions:

| Artifact | Verdict | Next Action |
|---|---|---|
| CKD SDMA primary monitoring claim | partially supported | revise |
| CKD phosphorus diet vs binder hierarchy claim | supported | promote |
| FIP baseline GS-441524 route-testing claim | supported | promote |
| Diabetes remission no-universal-key claim | supported | promote |
| Diabetes SGLT2 label-boundary claim | supported | promote |
| Diabetes diet architecture / no low-carb slogan claim | supported | promote |

The SDMA card is intentionally a “revise” example. It shows how the workbench should kill or narrow overclaims rather than making every claim sound useful.

The FIP card is the first cross-disease reuse test. It confirms that compiled disease memos under `system/indexes/fip-*.md` can feed the same claim-card workflow.

The diabetes card is the first uneven-corpus test. It required adding a Key-Claim Traceability table to `system/indexes/diabetes-remission-boundary-memo.md` before the verifier could treat the memo as compiled evidence. That is the content architecture lesson: memos with strong Core Takeaways should also expose machine-usable Key-Claim rows.

The SGLT2 card is the first regulatory-source test. It required:

- adding Key-Claim rows to `system/indexes/diabetes-sglt2-current-label-control-memo.md`
- loading `raw/regulations/src-reg-*.md` inside `scripts/claim_evidence.py`
- updating business eval source validation for regulation filenames

The diet card adds the next diabetes content boundary: low-carbohydrate evidence is important, but the product should preserve fiber, protein, body condition, remission-definition, and evidence-quality boundaries. `system/indexes/diabetes-diet-architecture-memo.md` now has machine-usable Key-Claim rows.

### Review Queue

The new claim cards were submitted to:

- `system/indexes/artifact-review-queue.json`

They were then reviewed and promoted to:

- `outputs/final/ckd-sdma-primary-monitoring-claim-card-20260605.md`
- `outputs/final/ckd-phosphorus-diet-vs-binder-claim-card-20260605.md`
- `outputs/final/fip-gs441524-baseline-route-testing-claim-card-20260605.md`
- `outputs/final/diabetes-remission-no-universal-key-claim-card-20260605.md`
- `outputs/final/diabetes-sglt2-label-boundary-claim-card-20260605.md`
- `outputs/final/diabetes-diet-architecture-no-low-carb-slogan-claim-card-20260605.md`

## Verification Run

```bash
python3 -m py_compile scripts/claim_evidence.py scripts/business_value_eval.py
python3 scripts/business_value_eval.py --verbose
```

Result:

```text
Total artifacts: 7
Passed: 7
Failed: 0
Overall score: 100.00%
```

## Current Content State

The business artifact layer now has:

1. one promoted opportunity brief:
   - `outputs/business/ckd-phosphorus-control-opportunity-brief-20260604.md`
2. six promoted claim evidence cards:
   - CKD phosphorus hierarchy, promote
   - CKD SDMA primary-monitoring overclaim, revise
   - FIP baseline GS-441524 route-testing claim, promote
   - diabetes remission no-universal-key boundary, promote
   - diabetes SGLT2 current-label boundary, promote
   - diabetes diet architecture no-low-carb-slogan boundary, promote

This is a better wedge than only improving `Ask the Vault` prose because it can change claims, briefs, and next-source intake.

## Suggested Next Move

Use the SDMA card to create the safer revised claim:

```text
SDMA supports early CKD detection and staging, but progression monitoring should remain multi-variable.
```

Next useful move: add Key-Claim Traceability tables to the remaining high-value diabetes memos that currently have strong Core Takeaways but weak machine-usable claim rows, especially:

- `system/indexes/diabetes-obesity-body-condition-memo.md`

Then generate a diabetes obesity/body-condition sequencing card. That would test whether the workbench can preserve risk-factor nuance without moralizing obesity or recommending unsafe immediate caloric restriction.
