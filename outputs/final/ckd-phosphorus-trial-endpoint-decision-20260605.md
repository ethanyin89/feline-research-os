---
id: business-ckd-phosphorus-trial-endpoint-decision-20260605
type: business
artifact_kind: endpoint_decision_memo
disease: CKD
use_case: trial_design
created_at: 2026-06-05
updated_at: 2026-06-05
owner: endpoint_decision_workbench
status: pending_review
verification_status: compiled
decision_grade: yes
---

# Endpoint Decision Memo: CKD

**Disease:** CKD
**Use Case:** trial_design
**Disease Maturity:** Mature

---

## Primary Recommendation

Use survival/progression as primary if feasible; otherwise, composite of core endpoints

## Secondary Recommendations

- Creatinine stability or reduction
- Proteinuria reduction (UPCR)
- Blood pressure control

---

## Endpoint Hierarchy

### Core Tier (Operational Endpoints)

| Endpoint | Primary Use | Boundary | Sources |
|----------|-------------|----------|---------|
| Creatinine | diagnosis, staging, longitudinal monitoring. In pr... | Rises relatively late, influenced by mus... | src-ckd-002, src-ckd-004, src-ckd-010 |
| USG (Urine Specific Gravity) | diagnostic confirmation, context for azotemia. Ina... | Essential but not sufficient by itself f... | src-ckd-002, src-ckd-004 |
| UPCR / Proteinuria | prognosis, substaging, progression interpretation,... | Interpretation requires compartment awar... | src-ckd-001, src-ckd-004, src-ckd-010 |
| Systolic Blood Pressure | substaging, risk management, target-organ protecti... | Under-measured in practice. Should be in... | src-ckd-004, src-ckd-007, src-ckd-009 |
| Phosphorus | monitoring, prognosis, progression control, treatm... | May stay normal early despite phosphate ... | src-ckd-003, src-ckd-004, src-ckd-006 |

### Support Tier (Early Detection / Adjunctive)

| Endpoint | Primary Use | Boundary | Sources |
|----------|-------------|----------|---------|
| SDMA | early detection support, adjunct monitoring. Appea... | Cannot currently be recommended as a sin... | src-ckd-002, src-ckd-004, src-ckd-018 |
| GFR | ideal early dysfunction detection reference. Gold ... | Practical limitations prevent routine us... | src-ckd-002, src-ckd-004, src-ckd-024 |

### Context Tier (Interpretation Markers)

| Endpoint | Primary Use | Boundary | Sources |
|----------|-------------|----------|---------|
| PTH | secondary hyperparathyroidism context, phosphate-r... | Important biologically; better as contex... | src-ckd-006, src-ckd-015 |
| Calcium / CKD-MBD Markers (FGF23) | mineral-management caution, calcification context.... | Clinically relevant branch, but not yet ... | src-ckd-015 |
| Anaemia | burden/progression context, treatment context. Int... | Important but currently context variable... | src-ckd-003, src-ckd-010 |
| Imaging (Renal Ultrasonography) | structural workup context, renal differential supp... | Important for structural context; diffus... | src-ckd-004, src-ckd-020 |

---

## Key-Claim Traceability

| ID | Claim | Level | Sources |
|-----|-------|-------|---------|
| CE1 | Core operational CKD endpoints are creatinine, USG, UPCR, sy... | B | src-ckd-004, src-ckd-010... |
| CE2 | Different endpoints map to different structural lesion patte... | B | src-ckd-010... |
| CE3 | Serial surveillance and creatinine trend from baseline are p... | B | src-ckd-004... |
| CE4 | SDMA is an adjunctive early-detection aid, not a standalone ... | B | src-ckd-004, src-ckd-024... |
| CE5 | Phosphorus may stay normal early despite phosphate retention... | B | src-ckd-006, src-ckd-015... |
| CE6 | Trial outcomes should minimally cover 29 parameters grouped ... | C | src-ckd-013... |

---

## Boundary

- [Creatinine] Rises relatively late, influenced by muscle mass. Not ideal for earliest detection.
- [USG (Urine Specific Gravity)] Essential but not sufficient by itself for earliest detection.
- [UPCR / Proteinuria] Interpretation requires compartment awareness (primary glomerular vs broader CKD), blood-pressure context, and non-renal confounder exclusion.
- [Systolic Blood Pressure] Under-measured in practice. Should be interpreted as repeated hemodynamic signal, not one-visit snapshot. Target <160 mmHg to minimize TOD risk.
- [Phosphorus] May stay normal early despite phosphate retention (PTH compensation). Should not be read in isolation from PTH context.

---

## Source Appendix

- `src-ckd-001`
- `src-ckd-002`
- `src-ckd-003`
- `src-ckd-004`
- `src-ckd-006`
- `src-ckd-007`
- `src-ckd-009`
- `src-ckd-010`
- `src-ckd-013`
- `src-ckd-015`
- _... and 4 more_