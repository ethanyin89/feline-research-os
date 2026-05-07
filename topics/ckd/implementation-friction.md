---
id: topic-ckd-implementation-friction
type: topic
topic: ckd
species: feline
disease: CKD
question_type: translation
source_ids: [src-ckd-014, src-ckd-019]
last_compiled_at: 2026-04-08
confidence: medium
owner: codex
status: active
---

# Feline CKD Implementation Friction

## Question This Page Answers

Where does feline CKD management break down between guideline-aware intent and real-world execution?

## Quantified Claim Traceability

| Claim | Source IDs | Boundary |
|---|---|---|
| 92.7% of respondents reported using IRIS guidance, but only 19.1% systematically measured SBP in all CKD cats. | src-ckd-014 | Portugal questionnaire data; use as practice-friction evidence, not global behavior. |
| 99.3% advised renal diet, while 36.9% reported renal diet represented less than 75% of daily intake for most patients. | src-ckd-014 | Implementation/adherence signal; not renal-diet efficacy proof. |
| 70.9% recommended reassessment every 2-3 months or more often, but only 35.7% could comply because of owner constraints. | src-ckd-014 | Owner-constraint signal from survey reporting; not a controlled outcome comparison. |

## Current Conclusions

### quoted_fact

- In the Portugal questionnaire study, 92.7% of respondents reported using IRIS guidance, but only 19.1% systematically measured systolic blood pressure in all CKD cats.
- A renal diet was advised by 99.3% of respondents, but 36.9% reported that it represented less than 75% of daily intake for most patients.
- Renal diet was often prescribed regardless of stage and without a proper gradual transition.
- Appetite stimulants, phosphate binders, ACE inhibitors, and calcium channel blockers were all commonly prescribed in practice.
- 70.9% recommended stable-patient reassessment every 2-3 months or more frequently, but only 35.7% could comply because of owner constraints.
- The hyperthyroidism review states that concurrent disease can mask CKD and that renal reassessment is required when euthyroidism is restored.

### source_supported_conclusion

- The main translational bottleneck in feline CKD is not only evidence scarcity. It is also implementation inconsistency.
- Blood-pressure substaging is one of the clearest current implementation failures in practice.
- Renal diet remains the strongest baseline-supported intervention, but real-world adherence and rollout quality are major limiting factors.
- Owner constraints should be treated as part of CKD care design, not as an afterthought.
- Concurrent hyperthyroidism adds another kind of implementation friction because interpretation and follow-up have to change over time rather than remain static.

### llm_inference

- A practical translational rule for the vault is:
  if a CKD plan depends on perfect monitoring cadence, perfect diet adherence, or one-time interpretation,
  it is probably less realistic than it looks.

## Friction Matrix

| Friction Type | What It Looks Like | Why It Matters | Current Best Interpretation | Key Source IDs |
|---|---|---|---|---|
| Guideline-to-execution gap | IRIS awareness high, SBP measurement low | substaging and hypertension detection fail if BP is not measured consistently | this is an implementation problem, not a theory problem | src-ckd-014 |
| Diet adoption gap | renal diet recommended, but intake often partial and rollout imperfect | even strongest intervention weakens if adherence is poor | recommendation rate is not the same as effective implementation | src-ckd-014 |
| Owner-constraint gap | ideal follow-up cadence not maintained | monitoring strategy may fail even when clinicians recommend it | owner-side feasibility must shape plan design | src-ckd-014 |
| Practice-evidence gap | common adjunct prescriptions exceed strongest-evidence anchors | routine use can look stronger than actual evidence | common use must be labeled separately from evidence strength | src-ckd-014 |
| Dynamic comorbidity interpretation | thyroid treatment changes renal interpretation window | one-time assessment can miss important post-treatment renal change | euthyroidism restoration is a reassessment checkpoint | src-ckd-019 |

## What This Page Says Clearly

1. Real-world feline CKD care has implementation friction even when guideline awareness is high.
2. Blood pressure under-measurement is one of the most actionable current gaps.
3. Renal diet is still the clearest baseline-supported intervention, but adherence is a major limiting reality.
4. Owner constraints materially shape whether recommended monitoring plans can actually happen.
5. Concurrent hyperthyroidism adds interpretation friction, not just diagnostic complexity.

## What We Should Not Overstate

- that reported common practice proves treatment efficacy
- that guideline familiarity means guideline-quality execution
- that translational planning can ignore owner adherence and follow-up constraints

## Reuse Targets

- [translation brief](translation-brief.md)
- [hypertension and comorbidity](hypertension-and-comorbidity.md)
- [current state dashboard](current-state-dashboard.md)
