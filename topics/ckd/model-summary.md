---
id: topic-ckd-model-summary
type: topic
topic: ckd
species: feline
disease: CKD
question_type: model
source_ids: [src-ckd-010, src-ckd-012, src-ckd-022]
last_compiled_at: 2026-04-08
confidence: low
owner: ""
status: active
---

# Feline CKD Model Summary

## Question This Page Answers

What model or model-like evidence currently supports feline CKD interpretation, and what can it actually answer?

## Current Conclusions

### quoted_fact

- The current seed corpus contains a pathology-linked primary study that correlates renal lesions with measurable dysfunction markers.
- The current seed corpus also contains a comparative case-control study that captures owner-observed symptom patterns before formal diagnosis.
- Treatment-oriented review material is largely built on cats with naturally occurring CKD rather than challenge-model logic.
- Fibrosis review material says most feline CKD has unknown underlying aetiology and is discussed through lesion and mediator framing.
- The experimental-model paper `src-ckd-022` followed 6 cats for 6 months after a unilateral 90-minute ischemic event and found persistent functional decline plus chronic structural renal lesions.

### source_supported_conclusion

- The current V1 “model layer” is not a strong induced-model landscape. It is primarily supported by:
  - natural-disease observational evidence
  - clinicopathology correlation evidence
- The model layer is now stronger than before because it includes one explicit feline experimental-model anchor, not only observational logic.
- The current vault is stronger on `evidence archetypes` than on classic `model taxonomy`.
- The fibrosis review material is better read as lesion and mediator framing than as formal experimental model architecture.
- For feline CKD, the most useful current translational bridge is not an experimental challenge model, but the relationship between structural kidney lesions and clinically observable markers.
- This means the CKD system should explicitly label the current model layer as `natural disease / observational evidence dominant`.
- The most defensible model split in the current corpus is:
  - natural-disease clinical management evidence
  - observational recognition/risk evidence
  - clinicopathology correlation evidence
  - mechanism review framing
  - experimental ischemic injury evidence

### llm_inference

- If the project later needs stronger preclinical model reasoning, a dedicated search for feline CKD interventional, longitudinal, or model-design literature should be run as a separate workstream.
- For now, the model layer should answer `what kind of evidence are we actually using?` before it tries to answer `which experimental model is best?`
- The next model-layer milestone should be comparing this ischemia model against spontaneous disease relevance, not simply collecting model papers for volume.

## Evidence Map

- `src-ckd-010` gives pathology-marker correlation evidence
- `src-ckd-012` gives symptom-recognition and case-control framing
- `src-ckd-003` gives naturally occurring disease treatment-management framing
- `src-ckd-011` gives fibrosis-centered lesion/mediator framing
- `src-ckd-022` gives an explicit ischemic experimental-model anchor

## Conflicts / Uncertainty

- We now have one experimental-model anchor, but not a developed taxonomy.
- The current page is stronger on “what evidence exists in practice” than on “formal model architecture.”
- It remains unclear how much of the current translational reasoning can be called `model-based` versus simply `natural clinical evidence`.

## Gaps

- no dedicated natural-history page yet
- no explicit observational-study index yet
- no intervention-model summary yet
- no explicit distinction yet between `model` and `evidence archetype` in system-wide vocabulary
- only one experimental-model paper is currently anchored

## Next Sources To Ingest

- feline CKD longitudinal observational studies
- any study explicitly designed as a feline CKD intervention model
- biomarker-validation papers with stronger prospective design

## Current Model Stack

| Evidence / Model Type | What It Looks Like In This Vault | What It Can Answer | What It Cannot Yet Answer | Key Source IDs |
|---|---|---|---|---|
| Natural-disease clinical management evidence | reviews and treatment logic from cats with naturally occurring CKD | what is done in practice, which endpoints matter operationally, where evidence is stronger or weaker | formal preclinical model selection or controlled challenge-model comparison | src-ckd-003, src-ckd-004, src-ckd-007 |
| Observational recognition / risk evidence | case-control and risk-oriented recognition logic | which cats get recognized late, what symptom or risk context should trigger workup | causal disease-mechanism proof or intervention efficacy | src-ckd-012, src-ckd-005 |
| Clinicopathology correlation evidence | lesion-marker linkage in naturally diseased cats | how structural lesions connect to endpoints such as phosphorus, proteinuria, blood pressure, anaemia | prospective treatment-response modeling | src-ckd-010 |
| Mechanism review framing | fibrosis-centered mediator and lesion synthesis | which mechanistic story is most defensible, which mediators deserve deeper extraction | direct cat-specific intervention effect sizes | src-ckd-001, src-ckd-011 |
| Experimental ischemic injury model | unilateral ischemia followed over 6 months | whether a single acute insult can lead to lasting functional and structural renal disease in cats | broad spontaneous-disease generalization or model selection for product programs | src-ckd-022 |

## What This Page Now Says Clearly

1. The current CKD model layer is mostly an evidence-stack problem, not an induced-model catalog.
2. Naturally occurring feline disease is the main substrate of the current vault.
3. The best translational bridge currently available is clinicopathology correlation, not challenge-model design.
4. If a future project requires stronger preclinical planning, model-specific literature must be ingested as a separate track.
5. The vault is no longer entirely without experimental-model evidence, but it still has only one clear anchor.
