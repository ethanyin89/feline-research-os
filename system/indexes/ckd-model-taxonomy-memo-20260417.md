---
id: system-ckd-model-taxonomy-memo-20260417
type: system
topic: ckd
species: feline
disease: CKD
question_type: model
language: en
last_compiled_at: 2026-04-17
confidence: medium
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
source_ids:
  - src-ckd-001
  - src-ckd-003
  - src-ckd-004
  - src-ckd-007
  - src-ckd-009
  - src-ckd-010
  - src-ckd-011
  - src-ckd-012
  - src-ckd-016
  - src-ckd-022
---

# CKD Model Taxonomy Memo, 2026-04-17

## Purpose

This memo addresses the P4 densification gap:

> model taxonomy 更明确

The existing `model-map.md` correctly lists what evidence archetypes exist. The gap is that it does not organize them by PURPOSE — what each model type can and cannot answer when the question changes. A research question about disease mechanism needs a different model than a question about endpoint validation or drug efficacy.

This memo converts the existing evidence map into a true model taxonomy: organized first by model TYPE, then by what each type can answer for each intended purpose.

---

## The Taxonomy Frame

Three axes define whether a model evidence source is useful for a given question:

1. **Model TYPE** — what kind of evidence is it? (natural disease / experimental / computational / correlative)
2. **Intended PURPOSE** — what is the question? (mechanism characterization / endpoint validation / drug efficacy / regulatory translation)
3. **Validity** — how directly does this model type answer that purpose?

The current vault has strong TYPE coverage but uneven PURPOSE coverage. That's the real shape of the gap.

---

## Type 1: Naturally Occurring Clinical Disease

**Vault presence:** Strong (src-ckd-003, src-ckd-004, src-ckd-007, src-ckd-009)

**What this type is:**
Clinical studies, guidelines, case series, and cohort observations from cats with spontaneous CKD. No investigator-controlled induction. Disease process is real and complete.

**What it can answer well:**

| Purpose | Validity | Notes |
|---|---|---|
| Natural history characterization | High | Direct — this IS the natural history |
| Endpoint selection (operational) | High | Real endpoints from real cats in real conditions |
| Risk-factor recognition | High | Case-control and cohort work (src-ckd-012) |
| Management logic | Medium-high | Guideline-level evidence with variable proof depth |
| Mechanism characterization | Low-to-medium | Mechanism is inferred from clinical findings, not controlled |
| Drug efficacy (controlled) | Low | Observational; confounded; cannot isolate intervention effect |
| Regulatory translation | Medium | Regulators accept naturally occurring disease, but efficacy claims are harder to support without controlled trials |

**What it cannot answer:**
- Causal mechanism isolation (no control over initiating insult)
- Clean single-drug efficacy (real-world polypharmacy and management variation)
- Early-disease biology (by the time clinical CKD is diagnosed, early stages are past)

---

## Type 2: Experimental Model (Induced Disease)

**Vault presence:** Thin but real — one source (src-ckd-022: unilateral 90-minute ischemic injury)

**What this type is:**
Investigator-controlled disease induction in a defined animal model. Allows causal inference, time-course control, and tissue collection.

**What it can answer well:**

| Purpose | Validity | Notes |
|---|---|---|
| Mechanism characterization (post-injury) | Medium-high | Controlled induction allows causal inference |
| Lesion progression timeline | Medium | src-ckd-022 shows 6-month persistence of structural lesions and functional decline |
| Function-structure linkage | Medium | Direct histological and functional readouts from same animals |
| Drug efficacy testing | Medium (potential) | Currently not represented in vault — the ischemia paper is observational of injury, not drug testing |
| Regulatory translation | Low-to-medium | Induced ischemia ≠ spontaneous CKD; regulators require bridging argument |
| Natural history characterization | Low | Induced acute injury has different initiation logic from spontaneous CKD |

**What it cannot answer:**
- Spontaneous CKD initiation (different biology from ischemic induction)
- Chronic heterogeneous progression as seen in clinical cats
- Final drug efficacy claims without additional controlled intervention studies

**Current vault state for this type:**
One paper (src-ckd-022) provides an experimental foundation. It is real and useful. It is not yet a rich experimental model layer. Future expansion would require additional induced-model or interventional studies.

---

## Type 3: Clinicopathology Correlation

**Vault presence:** Strong and distinctive (src-ckd-010)

**What this type is:**
Structural (histological, morphometric) findings linked to functional measurements in the same cats. Bridges lesion biology with measurable clinical endpoints.

**What it can answer well:**

| Purpose | Validity | Notes |
|---|---|---|
| Mechanism-endpoint bridge | High — best current vault source for this | Links structural lesions directly to clinical markers |
| Endpoint interpretation | High | Grounds marker validity in tissue reality |
| Lesion characterization | High | Direct histological read |
| Drug efficacy | Low | Observational; not an intervention design |
| Regulatory translation | Medium | Endpoint grounding is useful; efficacy claim still requires controlled evidence |

**What it cannot answer:**
- Causal interventional claims
- Early-disease biology (requires clinical-stage tissue samples)
- Treatment ranking

---

## Type 4: Aged-Cat Natural History and Morphology Review

**Vault presence:** Moderate and rising (src-ckd-001, src-ckd-016)

**What this type is:**
Review-level synthesis of geriatric renal biology, lesion types, aging-versus-disease distinction, and pathogenesis framing in naturally aging cats.

**What it can answer well:**

| Purpose | Validity | Notes |
|---|---|---|
| Natural history framing | Medium-high | Organizes the initiation-vs-progression distinction |
| Geriatric context | High | Specifically addresses aged-cat renal biology |
| Mechanism framing (lesion level) | Medium | Fibrosis-centered architecture; partly extrapolated beyond cats |
| Initiation hypothesis | Medium | Useful framing, review-level confidence |
| Drug efficacy | Low | Review-only; no intervention evidence |

**What it cannot answer:**
- Initiating-cause identification (heterogeneous in spontaneous CKD)
- Definitive mechanism causality
- Drug-efficacy claims

---

## Type 5: Computational / Machine-Learning Model

**Vault presence:** Real frontier (src-ckd-018)

**What this type is:**
Statistical and ML models trained on metabolomic or multi-parameter datasets. Not an animal model — a predictive algorithm. Belongs here because it represents a distinct model archetype for answering specific questions about early detection.

**What it can answer well:**

| Purpose | Validity | Notes |
|---|---|---|
| Early biomarker discrimination | Medium-high (in study conditions) | AUC 0.929 for ML panel at T-6 in one longitudinal study |
| Panel-over-single-marker logic | High for this vault | Shows why single-marker shortcuts are weaker than panel models |
| Biomarker discovery | Medium | Identifies 3-hydroxykynurenine S/U as strongest individual signal |
| Mechanism characterization | Low | Statistical association, not causal mechanism |
| Drug efficacy | None | No intervention design |
| Regulatory translation | Low | Computational models require separate regulatory pathway (e.g., Software as Medical Device) |

**What it cannot answer:**
- Why the biomarkers are predictive (mechanism is not addressed)
- Whether the discrimination holds in routine clinical populations (limited sample, CKD2 only)
- Drug-level efficacy questions

---

## Purpose-Oriented Read: What Each Research Question Needs

| Research question | Best current vault model type | What is missing |
|---|---|---|
| What lesion drives CKD progression? | Clinicopathology correlation (src-ckd-010) + mechanism review (src-ckd-001, src-ckd-011) | Causal intervention studies |
| What endpoints should a CKD trial use? | Naturally occurring disease (src-ckd-004, src-ckd-007) + trial outcome logic (src-ckd-013) | Validated prospective endpoints in controlled feline trials |
| Can a drug slow CKD progression? | Naturally occurring management evidence (src-ckd-003, src-ckd-004, src-ckd-007) | Controlled intervention studies with agreed endpoints |
| What is the best early biomarker? | Computational/ML model (src-ckd-018) + adjunctive SDMA evidence (src-ckd-004, src-ckd-024) | Routine-scale clinical validation of metabolomic panel |
| How do we isolate a mechanism in a clean model? | Experimental ischemia (src-ckd-022) | Additional induced-model coverage for non-ischemic initiation |

---

## What This Taxonomy Changes

| Prior framing | After this memo |
|---|---|
| "model thin but real" | Specific: Type 2 (experimental) is thin; Types 1, 3, 4 are moderate-to-strong |
| All evidence types treated as equivalent | Separated by what each can answer for a given research question |
| "one ischemic experimental anchor" | Positioned correctly: useful for post-injury mechanism, not for spontaneous CKD initiation or drug efficacy |
| Computational model bundled with "newer biomarkers" | Separated as its own type — answers different questions than clinical biomarker papers |

## What This Taxonomy Does Not Resolve

- The vault still lacks controlled interventional studies (Type 2 drug-testing)
- Spontaneous CKD initiation remains mechanistically underspecified regardless of model type
- Computational models need routine-scale validation before regulatory translation

## Best Write-Back Targets

- [model map](../../topics/ckd/model-map.md) — update the matrix to reflect purpose-oriented framing
- [current state dashboard](../../topics/ckd/current-state-dashboard.md) — upgrade "model thin but real" to "model taxonomy explicit"
- [translation brief](../../topics/ckd/translation-brief.md)
