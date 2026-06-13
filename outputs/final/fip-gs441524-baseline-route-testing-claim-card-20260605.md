---
id: business-fip-gs441524-baseline-route-testing-claim-card-20260605
type: business
artifact_kind: claim_card
disease: FIP
created_at: 2026-06-05
owner: claim_evidence_workbench
status: draft
verification_status: compiled
decision_grade: no
---

# Claim Evidence Card

**Disease:** FIP
**Claim:** Baseline GS-441524 has enough natural-disease efficacy and safety signal for internal route testing in non-neurologic FIP.

## Verdict

| Field | Value |
|-------|-------|
| Verdict | **SUPPORTED** |
| Confidence | medium |
| Claim Level | B (Source-Supported) |
| Next Action | promote |

## Key Sources

- `src-fip-016`
- `src-fip-017`
- `src-fip-024`
- `system/indexes/fip-baseline-gs-us-conditional-approval-eligibility-memo.md`

## Evidence Depth

| Metric | Value |
|--------|-------|
| Sources checked | 24 FIP source cards |
| Matching sources | 2 |
| Matching compiled claims | 1 |
| Deep extracted source cards | 24 |
| Compiled memo support | `FIP-US-CA3` in `fip-baseline-gs-us-conditional-approval-eligibility-memo.md` |

## Quoted Facts

- `src-fip-016`: this source is an efficacy and safety study of GS-441524 in cats with naturally occurring FIP.
- `src-fip-016`: the enrolled case mix included effusive, dry-to-effusive, and non-effusive disease, while severe neurologic and ocular FIP were not recruited.
- `src-fip-017`: GS-441524 has experimental antiviral foundation in tissue culture and experimental cat infection studies.

## Source-Supported Conclusions

- `src-fip-016`: the study supports clinical efficacy of GS-441524 in naturally occurring FIP, but does not justify overgeneralizing to severe neurologic and ocular disease.
- `system/indexes/fip-baseline-gs-us-conditional-approval-eligibility-memo.md`: `FIP-US-CA3` states that baseline GS-441524 has enough natural-disease efficacy and safety signal for internal route testing.
- `src-fip-024`: neurologic FIP remains a separate treatment object because dose, monitoring, relapse, and response interpretation differ from baseline non-neurologic disease.

## Boundary

- This supports internal route testing, not a legal marketing-status claim.
- This supports a narrow baseline non-neurologic product object first, not broad all-form FIP cure language.
- Neurologic and ocular FIP should remain separate label-extension or rescue-complexity branches.
- This card is not decision-grade for FDA strategy until the official-source route pack and current Animal Drugs @ FDA / Green Book status are rechecked.

## Missing Evidence

- Sponsor-grade endpoint definitions, monitoring rules, and statistical package are not present in this card.
- Current regulatory status needs a fresh official-source check before external use.
- Comparator logic remains separate and should be read through `fip-baseline-gs-us-comparator-boundary-memo.md`.

## Verification Path

`system/indexes/fip-baseline-gs-us-conditional-approval-eligibility-memo.md -> raw/papers/src-fip-016.md, raw/papers/src-fip-017.md, raw/papers/src-fip-024.md`

