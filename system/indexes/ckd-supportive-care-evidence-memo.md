---
id: system-ckd-supportive-care-evidence-memo
type: system
topic: ckd
last_compiled_at: 2026-04-09
owner: codex
status: active
language: en
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
---

# CKD Supportive-Care Evidence Memo

- Date: `2026-04-09`
- Scope: `src-ckd-003`, `src-ckd-007`, `src-ckd-010`

This memo exists to separate supportive-care branches that are clinically important but easy to flatten into one vague “supportive treatment” bucket.

In the current vault, supportive care is real and necessary.
But the evidence strength is uneven across:

1. potassium correction
2. anaemia-directed support
3. appetite / uraemic-gastroenteritis support
4. long-term subcutaneous fluid therapy

## Core Position

1. Supportive care belongs in the CKD treatment map because it affects quality of life, stability, and complication burden.
2. These branches are not all equally supported.
3. Potassium, anaemia, and appetite-support logic are clinically meaningful context-dependent branches.
4. Long-term subcutaneous fluid therapy remains the clearest example of common practice outrunning evidence strength.

## Key-Claim Traceability

| Claim ID | Key Claim | Claim Level | Supporting Source IDs | Notes |
|---|---|---|---|---|
| SC1 | Supportive care in feline CKD mainly targets consequences of reduced renal function rather than the underlying cause | B | src-ckd-003 | broad framing anchor |
| SC2 | Potassium correction is important because hypokalaemia can create serious complications | B | src-ckd-003, src-ckd-007 | supportive branch with clear complication logic |
| SC3 | Anaemia and uraemic-gastroenteritis support become increasingly relevant as CKD progresses | B | src-ckd-003, src-ckd-010 | burden and late-stage support branch |
| SC4 | Long-term subcutaneous fluid therapy is common in practice but weakly supported in the current evidence layer | B | src-ckd-007 | explicit weak-evidence anchor |
| SC5 | Supportive-care importance should not be translated into disease-modification proof | B | src-ckd-003, src-ckd-007 | branch-level boundary |

## Branch 1: Potassium Correction

What current sources support:

- hypokalaemia matters clinically
- potassium correction is important to prevent serious complications
- potassium belongs in the treatment-context endpoint set

What the vault can say safely:

- potassium supplementation is a meaningful supportive intervention when hypokalaemia is present

What the vault should not say:

- do not write potassium correction as a disease-modifying CKD therapy

## Branch 2: Anaemia-Directed Support

What current sources support:

- anaemia becomes more relevant with greater disease burden
- anaemia is tied to later-stage CKD management rather than first-wave diagnosis
- the branch is clinically meaningful, but not yet sharply ranked in the current vault

What the vault can say safely:

- anaemia-directed support belongs in supportive-care logic for more advanced CKD

What the vault should not say:

- do not treat anaemia support as if the current vault already contains a strong feline intervention hierarchy for this branch

## Branch 3: Appetite / Uraemic-Gastroenteritis Support

What current sources support:

- many cats benefit from treatment of uraemic gastroenteritis as CKD progresses
- appetite and clinical wellbeing matter in treatment evaluation
- this branch fits quality-of-life and clinical-stability logic more than progression reversal logic

What the vault can say safely:

- appetite-support and GI-support are real supportive branches with clinical value

What the vault should not say:

- do not confuse symptom relief with proven slowing of structural renal disease

## Branch 4: Long-Term Subcutaneous Fluid Therapy

What current sources support:

- this intervention is widely used in practice
- current evidence review explicitly grades long-term subcutaneous fluid therapy as weak grade IV evidence in cats

What the vault can say safely:

- long-term subcutaneous fluid therapy is operationally common but evidentiary weak

What the vault should not say:

- do not let field familiarity be mistaken for strong proof

## Current Working Hierarchy

| Supportive Branch | Current Position In Vault | Notes |
|---|---|---|
| Potassium correction | meaningful Tier 2 supportive branch | complication-control logic is clear |
| Anaemia-directed support | supportive but less sharply ranked | context-relevant, more advanced disease branch |
| Appetite / GI support | supportive and clinically important | quality-of-life and stability branch |
| Long-term subcutaneous fluids | common but weak-evidence | strongest example of practice outrunning evidence |

## What This Branch Is Not Allowed To Become

- It is not allowed to become a single undifferentiated “supportive care works” claim.
- It is not allowed to upgrade supportive management into disease modification.
- It is not allowed to hide weak-evidence branches behind high-frequency clinical use.
- It is not allowed to flatten quality-of-life support and progression control into the same outcome claim.

## What The Vault Can Now Say More Clearly

1. Supportive care matters, but it is not flat.
2. Potassium, anaemia, and appetite-support are clinically meaningful without needing to be overstated.
3. Long-term subcutaneous fluid therapy remains the clearest weak-evidence supportive branch in the current corpus.
4. Supportive branches mostly improve burden and stability rather than proving structural disease reversal.

## Best Reuse Targets

- [CKD treatment ranking memo](ckd-treatment-ranking-memo.md)
- [translation brief](../../topics/ckd/translation-brief.md)
- [anaemia](../../entities/endpoints/anaemia.md)
- [potassium](../../entities/endpoints/potassium.md)
- [current state dashboard](../../topics/ckd/current-state-dashboard.md)
