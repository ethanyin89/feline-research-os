---
id: business-diabetes-sglt2-label-boundary-claim-card-20260605
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
**Claim:** Current label control preserves the otherwise-healthy, insulin-naive indication boundary for both Bexacat and Senvelgo.

## Verdict

| Field | Value |
|-------|-------|
| Verdict | **SUPPORTED** |
| Confidence | medium |
| Claim Level | B (Source-Supported) |
| Next Action | promote |

## Key Sources

- `src-reg-012`
- `src-reg-013`
- `src-reg-010`
- `src-reg-011`
- `system/indexes/diabetes-sglt2-current-label-control-memo.md`

## Evidence Depth

| Metric | Value |
|--------|-------|
| Sources checked | 122 diabetes-relevant source cards, including regulations |
| Matching sources | 4 |
| Matching compiled claims | 1 |
| Deep extracted paper cards | 24 |
| Regulatory source cards | 4 |
| Compiled memo support | `DSG2` in `diabetes-sglt2-current-label-control-memo.md` |

## Quoted Facts

- `src-reg-012`: DailyMed lists Bexacat as approved under NADA #141-566.
- `src-reg-013`: DailyMed lists Senvelgo as approved under NADA #141-568.

## Source-Supported Conclusions

- `src-reg-012`: the current Bexacat label preserves the otherwise-healthy, insulin-naive indication boundary.
- `src-reg-013`: the current Senvelgo label preserves the otherwise-healthy, insulin-naive indication boundary.
- `src-reg-012`: the Bexacat label foregrounds diabetic ketoacidosis/euglycemic diabetic ketoacidosis risk, insulin-related contraindications, and pre-treatment screening.
- `src-reg-013`: the Senvelgo label foregrounds diabetic ketoacidosis/euglycemic ketoacidosis risk and insulin-related contraindications.
- `system/indexes/diabetes-sglt2-current-label-control-memo.md`: `DSG2` states that current label control preserves the otherwise-healthy, insulin-naive indication boundary for both products.

## Boundary

- This supports U.S. label-control language, not global approval or availability.
- This does not support ranking Bexacat versus Senvelgo.
- This does not support ranking SGLT2 treatment against insulin from current-label evidence alone.
- This does not support use in insulin-treated, previously insulin-treated, insulin-dependent, complicated, or DKA-risk cats.
- DKA/euglycemic DKA warnings should govern any treatment, product, or owner-facing output.

## Missing Evidence

- Comparative efficacy evidence is not established by current labels.
- Product-specific monitoring gates need full label-section extraction before external-facing text.
- Current DailyMed/FDA label status should be rechecked before partner-facing or regulatory-facing use.

## Verification Path

`system/indexes/diabetes-sglt2-current-label-control-memo.md -> raw/regulations/src-reg-012-bexacat-current-label.md, raw/regulations/src-reg-013-senvelgo-current-label.md, raw/regulations/src-reg-010-bexacat-fda-foi.md, raw/regulations/src-reg-011-senvelgo-fda-foi.md`

