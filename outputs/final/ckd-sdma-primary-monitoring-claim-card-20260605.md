---
id: business-ckd-sdma-primary-monitoring-claim-card-20260605
type: business
artifact_kind: claim_card
disease: CKD
created_at: 2026-06-05
owner: claim_evidence_workbench
status: draft
verification_status: compiled
decision_grade: no
---

# Claim Evidence Card

**Disease:** CKD
**Claim:** Feline CKD progression can be monitored primarily with SDMA.

## Verdict

| Field | Value |
|-------|-------|
| Verdict | **PARTIALLY_SUPPORTED** |
| Confidence | low |
| Claim Level | C (Working Inference) |
| Next Action | revise |

## Key Sources

- `src-ckd-004`
- `src-ckd-021`
- `src-ckd-005`
- `src-ckd-001`
- `src-ckd-024`

## Evidence Depth

| Metric | Value |
|--------|-------|
| Sources checked | 24 |
| Matching sources | 10 |
| Matching compiled claims | 0 |
| Level A quoted matches | 8 |
| Level B supported matches | 0 |
| Level C inference matches | 2 |
| Deep extracted source cards | 24 |

## Quoted Facts

- `src-ckd-004`: SDMA is described as more sensitive than creatinine for early CKD detection and less affected by muscle mass.
- `src-ckd-004`: SDMA is not recommended as a single CKD screening test.
- `src-ckd-001`: CKD progression is associated with variables including proteinuria, plasma phosphate, and plasma creatinine.
- `src-ckd-021`: MR-antagonist studies have not yet shown whether mortality or CKD progression is reduced.
- `src-ckd-005`: CKD management remains limited by late diagnosis and limited ability to prevent progression.

## Source-Supported Conclusions

- `src-ckd-004`: Creatinine, USG, UPCR, systolic blood pressure, serum biochemistry, and imaging remain the practical core of first-pass CKD workup even when SDMA or GFR are discussed.

## Boundary

- SDMA can support early detection and staging, but the current evidence does not support using it as the primary or standalone progression-monitoring axis.
- A safer claim is: `SDMA can support feline CKD detection and staging, but progression monitoring should remain multi-variable, including creatinine, urinalysis/USG, UPCR, blood pressure, phosphorus, and clinical trend.`
- This card is not decision-grade for a diagnostic-product claim until the endpoint hierarchy is audited against `topics/ckd/endpoint-handbook.md` and `src-ckd-004`.

## Missing Evidence

- No compiled CKD Key-Claim Traceability row currently supports `SDMA as primary progression monitor`.
- No decision-grade endpoint memo ranks SDMA above creatinine, phosphorus, UPCR, blood pressure, or clinical progression variables.
- A progression-monitoring claim would need longitudinal feline evidence tying SDMA trend to outcome or progression decisions.

## Verification Path

`topics/ckd/synthesis-index.md -> topics/ckd/endpoint-handbook.md -> raw/papers/src-ckd-004.md`

