---
id: topic-ckd-model
type: topic
topic: ckd
species: feline
disease: CKD
question_type: model
source_ids: [src-ckd-001, src-ckd-003, src-ckd-004, src-ckd-007, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-012, src-ckd-016, src-ckd-022, src-ckd-050]
last_compiled_at: 2026-06-06
confidence: medium
verification_status: compiled
owner: codex
status: active
---

# Feline CKD Model Map

## Question This Page Answers

What model evidence exists for feline CKD, and what can each model answer?

## Quantified Claim Traceability

| Claim | Source IDs | Boundary |
|---|---|---|
| An experimental model followed cats for 6 months after a unilateral 90-minute ischemic event and found persistent function-plus-lesion changes. | src-ckd-022 | Induced, unilateral, small experimental-model evidence; not spontaneous-disease generality. |
| Primary renal cortical fibroblasts from four normal cats responded to TGF-beta1 with a profibrotic transcriptional program. | src-ckd-050 | Healthy-donor, in-vitro evidence; not spontaneous CKD or whole-organism efficacy. |

## Current Conclusions

### quoted_fact

- The current seed corpus is still dominated by naturally occurring feline CKD evidence rather than induced-disease model literature.
- Treatment and guideline sources organize CKD around serial monitoring, substaging, proteinuria, blood pressure, phosphorus control, and supportive management in cats with clinical disease.
- Evidence-grading review material shows that many commonly used interventions remain weakly or unevenly supported despite their real-world use.
- Clinicopathology correlation evidence links structural renal lesions with measurable dysfunction markers.
- Comparative case-control evidence exists for recognition and symptom timing before diagnosis.
- Aged-cat morphology review material now provides a stronger natural-history and pathogenesis scaffold for the naturally occurring disease layer.
- An experimental-model paper exists showing persistent functional decline and chronic structural renal lesions 6 months after a unilateral 90-minute ischemic event in cats.
- A primary feline renal cortical fibroblast culture model now provides direct cell-level TGF-beta response evidence.

### source_supported_conclusion

- The current vault still does not support a classic dense `experimental model menu` for feline CKD.
- A more accurate V1 map remains a `model-like evidence map` built from natural disease management, recognition studies, clinicopathology correlation, review synthesis, and one ischemic injury model.
- Naturally occurring clinical disease remains the strongest model-like substrate because it carries the practical diagnostic, endpoint, and translational logic used across the vault.
- Evidence-grading material now strengthens the claim that the natural-disease layer is valuable not only for realism, but also for exposing where routine management outruns proof.
- Blood-pressure and proteinuria comorbidity material supports treating subgroup structure inside natural disease as important evidence architecture, not as background noise.
- Fibrosis-centered mechanism synthesis makes the natural-disease layer more reusable by giving it a stable lesion backbone even when initiating causes remain heterogeneous.
- The model map is now stronger because aged-cat natural-history review and experimental ischemia work can be read together without collapsing them into the same evidence type.
- The fibroblast model supports mediator and target-engagement experiments but cannot substitute for CKD-derived tissue or in-vivo efficacy evidence.

### llm_inference

- If future work expands into drug-development planning, this page should split into natural disease, longitudinal observational evidence, intervention studies, and true experimental model evidence.

## Model-Like Evidence Matrix

| Model / Evidence Archetype | Current Presence In Vault | Best Use | Main Weakness | Key Source IDs |
|---|---|---|---|---|
| Naturally occurring clinical disease | strong | real-world management logic, endpoint selection, translational caution, subgroup framing | weaker for causal isolation and formal model design | src-ckd-003, src-ckd-004, src-ckd-007, src-ckd-009 |
| Aged-cat natural-history / morphology review | moderate and rising | organizes lesion identity, geriatric framing, and initiation-versus-progression logic in spontaneous disease | review-level and partly hypothesis-led | src-ckd-001, src-ckd-016 |
| Case-control recognition evidence | moderate | early-recognition framing, symptom timing, risk-context suspicion | limited for mechanism and treatment efficacy | src-ckd-012 |
| Clinicopathology correlation | strong and distinctive | mechanism-endpoint bridge, structural interpretation of markers | not a prospective intervention model | src-ckd-010 |
| Mechanism review synthesis | moderate | fibrosis-centered lesion and mediator framing | review-level, partly extrapolated beyond cats | src-ckd-001, src-ckd-011, src-ckd-016 |
| Experimental ischemia model | now present but thin | lesion progression, function-structure linkage after discrete injury, mechanistic anchoring | unilateral and induced, so translational relevance to spontaneous CKD remains bounded | src-ckd-022 |
| Primary feline renal cortical fibroblast culture | one direct anchor | cell-level TGF-beta mechanism and receptor target-engagement testing | four healthy-kidney donors; in vitro; no whole-organism outcome | src-ckd-050 |

## What This Page Says Clearly

1. The current model layer is real, but it is still not a dense classic experimental-model layer.
2. The vault is strongest when it uses naturally occurring disease plus clinicopathology correlation together.
3. Evidence-grading and comorbidity sources make the natural-disease layer more structured than a simple "clinical background" bucket.
4. The vault now has an induced ischemia anchor and a primary fibroblast culture anchor, but users should still be careful not to overstate model strength.
5. **Model type ≠ evidence sufficiency for any purpose.** Different research questions require different model types — see the purpose-oriented taxonomy.

## Model Taxonomy (Purpose-Oriented)

For a full taxonomy of model types organized by what each can answer for different research purposes (mechanism, endpoint validation, drug efficacy, regulatory translation), see:

- [CKD model taxonomy memo, 2026-04-17](../../system/indexes/ckd-model-taxonomy-memo-20260417.md)

Key insight from that memo: the vault's gap is not "not enough model evidence" in general — it is specifically **Type 2 (controlled intervention) coverage** for drug-efficacy questions. Natural disease, clinicopathology correlation, and aged-cat morphology are reasonably strong for the purposes they can serve.
