---
id: system-ckd-hypertension-proteinuria-junction-memo
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

# CKD Hypertension-Proteinuria Junction Memo

- Date: `2026-04-09`
- Scope: `src-ckd-003`, `src-ckd-004`, `src-ckd-007`, `src-ckd-009`, `src-ckd-010`, `src-ckd-014`, `src-ckd-017`

This memo exists to keep one important treatment junction from becoming blurry.

In feline CKD, blood pressure and proteinuria belong in the same management conversation.
But they are not the same branch, and they should not be collapsed into one generic renoprotective claim.

## Core Position

1. Hypertension and proteinuria repeatedly converge in feline CKD because both are tied to progression logic, target-organ risk, and treatment choice.
2. This convergence makes them a junction, not a merged endpoint.
3. Hemodynamic management and proteinuria-oriented management partly overlap, but they are still different reasoning branches.
4. The safest current wording is management relevance, not broad proof of survival-level renoprotection.

## Key-Claim Traceability

| Claim ID | Key Claim | Claim Level | Supporting Source IDs | Notes |
|---|---|---|---|---|
| J1 | Systolic blood pressure and proteinuria repeatedly appear together in feline CKD progression and management logic | B | src-ckd-004, src-ckd-009, src-ckd-010 | bridge across endpoint and pathology layers |
| J2 | Hypertension drives or amplifies clinically meaningful proteinuria context in feline CKD | B | src-ckd-009, src-ckd-010 | endpoint coupling matters even when mechanism is not fully resolved |
| J3 | Antihypertensive treatment and proteinuria-oriented RAAS management partially overlap but should not be flattened into one efficacy claim | B | src-ckd-003, src-ckd-009, src-ckd-017 | management branches intersect without becoming identical |
| J4 | Blood-pressure under-measurement weakens real-world execution of this junction | B | src-ckd-014, src-ckd-009 | implementation gap matters here |
| J5 | Proteinuria may also point toward a glomerular subset, so not every proteinuric cat belongs to one diffuse CKD story | B | src-ckd-017 | keeps pathology logic from disappearing inside treatment logic |

## Why This Junction Matters

If blood pressure is discussed without proteinuria, the treatment picture is incomplete.
If proteinuria is discussed without blood pressure, the treatment picture is also incomplete.

That is why this branch matters:

- blood pressure changes management thresholds
- proteinuria changes monitoring and treatment relevance
- together they shape how strong or weak a treatment claim can safely be

In other words, this junction is not only about interpretation.
It changes what kind of management language is defensible.

## What The Current Sources Actually Support

### Stronger Support

- systolic blood pressure belongs in routine CKD workup
- proteinuria is not a minor laboratory detail
- hypertension and proteinuria should be read together when assessing progression and management forks
- antihypertensive treatment has clear management importance when hypertension is present

### Bounded Support

- blood-pressure control does not automatically prove broad renal-outcome benefit
- proteinuria-oriented RAAS logic has management relevance but not broad survival-level proof
- the overlap between these branches should not be written as if one intervention solved the whole junction

## What `src-ckd-017` Adds To The Junction

`src-ckd-017` matters here because it stops proteinuria from being treated as only a hemodynamic severity marker.

It adds a second reminder:

- some proteinuric cats may sit in a glomerular disease subset
- UPC magnitude can sharpen suspicion
- pathology heterogeneity remains real

So the junction is three-layered:

- hemodynamic context
- endpoint / progression context
- pathology-subset context

That is exactly why broad renoprotective language is too loose for the current vault.

## What This Branch Is Not Allowed To Become

- It is not allowed to become “hypertension plus proteinuria equals proven disease modification.”
- It is not allowed to become “RAAS use resolves both branches equally well.”
- It is not allowed to erase the glomerular subset logic in proteinuric cats.
- It is not allowed to treat missing SBP measurement as a minor documentation issue.

## Current Working Use

| Use Case | Safe Current Framing |
|---|---|
| CKD cat with hypertension | hemodynamic management is clinically central |
| CKD cat with proteinuria | proteinuria-oriented management is clinically meaningful but bounded |
| CKD cat with both hypertension and proteinuria | the treatment junction is more important, but not automatically more proven |
| Proteinuric cat with very high UPC | keep glomerular subset logic visible; do not flatten into generic diffuse CKD |

## What The Vault Can Now Say More Clearly

1. Blood pressure and proteinuria belong in one treatment conversation.
2. They are connected branches, not interchangeable branches.
3. Hemodynamic management and proteinuria-oriented management should be kept adjacent but distinct.
4. The current vault supports stronger management logic than broad renoprotective proof at this junction.

## Best Reuse Targets

- [hypertension and comorbidity](../../topics/ckd/hypertension-and-comorbidity.md)
- [translation brief](../../topics/ckd/translation-brief.md)
- [CKD treatment ranking memo](ckd-treatment-ranking-memo.md)
- [CKD proteinuria treatment evidence memo](ckd-proteinuria-treatment-evidence-memo.md)
