---
id: topic-ckd-synthesis-index
type: topic
topic: ckd
species: feline
disease: CKD
question_type: overview
source_ids: [src-ckd-001, src-ckd-002, src-ckd-003, src-ckd-004, src-ckd-005, src-ckd-006, src-ckd-007, src-ckd-008, src-ckd-009, src-ckd-010, src-ckd-011, src-ckd-012, src-reg-001, src-reg-002, src-reg-003, src-reg-004, src-reg-005, src-reg-006, src-reg-007, src-reg-008, src-reg-009]
last_compiled_at: 2026-04-08
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline CKD Synthesis Index

## Quick Helpers

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want to see real `promote / hold / partial promotion` examples:
  [promotion examples index](../../system/indexes/promotion-examples-index.md)

This page is the best “compiled state of the vault” summary.

Use it when you want to know:

- what we think we know
- what still feels weak
- what is actually worth reading next

## 1. Strongest Current Conclusions

### Core-Paper Backbone

- The current strongest internal backbone comes from three papers used together:
  - `src-ckd-004` for operational clinical logic
  - `src-ckd-010` for clinicopathology correlation
  - `src-ckd-011` for fibrosis-centered mechanism framing
- The value of this trio is that they answer different layers of the same disease rather than repeating each other.

### Mechanism

- `Renal fibrosis / tubulointerstitial fibrosis` is the strongest current mechanism backbone.
- The current vault supports treating fibrosis as the most stable anchor connecting structure, progression, and measurable disease burden.
- `TGF-beta` is now the strongest current mediator-level expansion target, but it still sits below fibrosis in certainty.

### Endpoint

- The strongest first-wave endpoint shortlist is:
  - creatinine
  - USG
  - UPCR / proteinuria
  - systolic blood pressure
  - phosphorus
  - SDMA
- Among these, `proteinuria`, `phosphorus`, and `systolic blood pressure` are especially valuable because they bridge mechanism, prognosis, and treatment.
- The current core papers also support reading these endpoints on multiple lesion axes rather than as one undifferentiated renal-severity scale.

### Translation

- `Renal diet` is the clearest baseline-supported intervention in the current vault.
- Several interventions are clinically common but do not yet have equally strong supporting evidence in this corpus.
- The easiest overclaim is to confuse common use with strong efficacy evidence.
- The treatment layer is now also clearer at a disease-modification boundary: management and progression-control language are stronger than structural-reversal language.
- Early detection, risk recognition, and prevention-oriented thinking are now explicit parts of the vault, but still not strong enough to be treated as solved.
- The current core papers jointly support framing early detection as `serial surveillance`, not as a one-test biomarker problem.

### Regulatory

- There is no single generic “regulatory path.”
- China, FDA, EMA, and VMD each require different early strategic questions.
- FDA and EMA each contain a high-leverage special-route question that should be tested early rather than assumed.

## Key-Claim Traceability

| Claim ID | Key Claim | Claim Level | Supporting Source IDs | Notes |
|---|---|---|---|---|
| S1 | The strongest current internal backbone comes from `src-ckd-004`, `src-ckd-010`, and `src-ckd-011` used together | B | src-ckd-004, src-ckd-010, src-ckd-011 | compiled cross-source backbone claim |
| S2 | Renal fibrosis / tubulointerstitial fibrosis is the strongest current mechanism backbone | B | src-ckd-010, src-ckd-011, src-ckd-016 | stable compiled mechanism judgment, still not sentence-level citation to source text |
| S3 | The first-wave endpoint shortlist is creatinine, USG, UPCR/proteinuria, systolic blood pressure, phosphorus, and SDMA | B | src-ckd-004, src-ckd-009, src-ckd-010, src-ckd-024 | operational compiled shortlist, not decision-grade |
| S4 | Renal diet is the clearest baseline-supported intervention in the current vault | B | src-ckd-003, src-ckd-006, src-ckd-007 | review-led treatment hierarchy |
| S5 | The current best early-detection framing remains serial surveillance, not a one-test biomarker story | B | src-ckd-004, src-ckd-018, src-ckd-024 | compiled early-detection judgment |
| S6 | There is no single generic regulatory path; China, FDA, EMA, and VMD require different early strategic questions | B | src-reg-001, src-reg-004, src-reg-007, src-reg-008 | route-level only, not product-specific |

## 2. What Still Feels Weak

### Weak Layer 1: Model Architecture

- The current “model layer” is still mostly natural-disease and observational logic.
- It is no longer purely observational, because the vault now has one explicit ischemic experimental anchor:
  [src-ckd-022](../../raw/papers/src-ckd-022.md)
- The real weakness now is not total absence, but lack of model density and taxonomy.

### Weak Layer 2: SDMA Positioning

- SDMA is now more clearly supportable as a useful adjunctive biomarker linked to GFR-oriented early recognition logic.
- The remaining weakness is not whether SDMA matters at all, but how strongly to rank it against creatinine and USG across concrete use cases.
- This is now being collected into a dedicated working page:
  [sdma positioning](sdma-positioning.md)

### Weak Layer 3: Treatment Ranking

- We now have a treatment evidence matrix and a better minimum trial-outcome frame.
- What is still missing is a deeper intervention-by-intervention primary-study map.

### Weak Layer 4: Indication-Specific Regulatory Detail

- Current regulatory pages are route-level solid.
- They are not yet strong enough for a product-specific or submission-grade recommendation.

### Weak Layer 5: Prevention Logic

- The vault now has enough material to say prevention matters.
- It does not yet have enough material to say what a true prevention strategy should look like in practice.

### Weak Layer 6: Symptom-To-Workup Operationalization

- The vault now has a clearer risk-and-recognition layer.
- It still does not define exactly when owner-observed change should trigger a standardized renal workup.

### Weak Layer 7: Hypertension Treatment Granularity

- The vault now has a clearer hypertension/comorbidity layer.
- It is still stronger on why hypertension matters than on exact treatment-fork and monitoring-cadence detail.

### Weak Layer 8: Machine-Learning Early Detection Claims

- The next likely pressure point is newer biomarker-plus-model literature.
- The vault now has one real metabolomics-plus-ML source:
  [src-ckd-018](../../raw/papers/src-ckd-018.md)
- That paper strengthens the idea of future panel-based augmentation, but it still does not justify replacing serial surveillance with a routine ML workflow.

## 3. Most Important Cross-Layer Bridges

### Bridge 1

`renal fibrosis -> phosphorus`

Why it matters:

- this is not just a treatment issue
- it is a progression and mechanism issue too

### Bridge 2

`structural injury -> proteinuria`

Why it matters:

- proteinuria belongs at the center of interpretation, not as a minor staging detail

### Bridge 3

`vascular / glomerular injury context -> systolic blood pressure`

Why it matters:

- blood pressure is a core disease signal and management lever

### Bridge 4

`route selection -> evidence package`

Why it matters:

- regulatory choice depends less on geography alone and more on product type + claim + feasible evidence package

## 4. Current Arguments We Can Defend

These are strong enough for internal discussion now:

- feline CKD is best framed as fibrosis-centered in the current vault
- endpoint choice should not be flattened into a single “kidney marker” mindset
- treatment summaries must label evidence strength
- hypertension is central, not peripheral
- owner-observed polyuria and polydipsia are meaningful recognition prompts in the current corpus
- regulatory path is a branching decision problem
- treatment-trial outcomes are broader than routine clinical monitoring
- spontaneous feline CKD should still default to an aged-cat, fibrosis-centered tubulointerstitial framing
- the current best early-detection framing remains serial surveillance, but emerging metabolomic panels may become a meaningful augmentation layer
- senescence now has direct feline support as a mechanism-enrichment branch, but not as a replacement backbone

## 5. Current Arguments We Should Not Overstate

These are not yet strong enough:

- exact SDMA ranking against traditional markers
- strong disease-modification claims for multiple interventions
- a finished feline CKD model landscape
- a final preferred jurisdiction for registration strategy
- any “human drug to pet” shortcut conclusion
- machine-learning early-detection superiority claims
- any claim that senescence has already become the primary organizing mechanism of feline CKD

## 6. Best Pages To Reuse Right Now

### For a quick internal discussion

- [briefing working en](../../outputs/briefings/out-ckd-briefing-20260408-round1-working-en.md)
- [briefing en](../../outputs/briefings/out-ckd-briefing-20260408-round1-en.md)

### For deeper reading

- [dossier working en](../../outputs/dossiers/out-ckd-dossier-20260408-v1-working-en.md)
- [core paper synthesis memo](../../system/indexes/core-paper-synthesis-memo-ckd-round1.md)
- [round 2 tier A synthesis memo](../../system/indexes/ckd-round-2-tier-a-synthesis-memo.md)
- [CKD disease-modification boundary memo](../../system/indexes/ckd-disease-modification-boundary-memo.md)

### For mechanism

- [mechanism overview](mechanism-overview.md)
- [pathology correlations](pathology-correlations.md)

### For endpoints

- [endpoint handbook](endpoint-handbook.md)
- [sdma positioning](sdma-positioning.md)

### For early detection

- [early detection](early-detection.md)

### For risk recognition

- [risk and recognition](risk-and-recognition.md)

### For hypertension and comorbidity

- [hypertension and comorbidity](hypertension-and-comorbidity.md)

### For translation

- [translation brief](translation-brief.md)

### For regulatory

- [regulatory brief](regulatory-brief.md)

## 7. Best Next Reading Moves

If the goal is to densify the vault rather than expand scope, the next reading priorities are:

1. the next bounded early-detection read, especially machine-learning-plus-biomarker material
2. more feline CKD primary treatment studies
3. better model / observational study mapping
4. more indication-specific regulatory and dossier-detail sources
5. stronger prevention-oriented feline studies beyond recognition logic

## 8. Best Next Build Moves

### Highest-value next asset

- an `intervention -> endpoint -> evidence-strength -> product archetype` comparison that goes deeper than the current first-pass ranking memo

### Highest-value next densification move

- full-text extraction on the most reused source cards

### Highest-value next regulatory move

- a tighter decision memo for one specific product archetype

## 9. One-Sentence State Of The Vault

This vault is no longer just a framework. It is a usable compiled CKD research system with a denser Round 2 backbone, stronger on SDMA boundaries, trial-outcome logic, model realism, pathology-aware proteinuria interpretation, and a first-pass treatment ranking, while still remaining weaker in treatment primary-study density, model density, and product-specific regulatory precision.
