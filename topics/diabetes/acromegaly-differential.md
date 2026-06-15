---
id: topic-diabetes-acromegaly-differential
type: topic
topic: diabetes
species: feline
disease: diabetes mellitus
question_type: comorbidities
source_ids: [src-diabetes-013, src-diabetes-020, src-diabetes-036, src-diabetes-061, src-diabetes-075, src-diabetes-090, src-diabetes-092, src-diabetes-114]
last_compiled_at: 2026-06-15
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline Acromegaly (Hypersomatotropism) Differential Diagnosis and Management

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| ACR1 | Hypersomatotropism (acromegaly) is caused by a growth hormone-secreting pituitary adenoma and is present in up to 25-30% of diabetic cats | B | src-diabetes-061, src-diabetes-020 | Prevalence anchor, not screening mandate |
| ACR2 | Acromegalic cats exhibit severe insulin resistance, requiring high insulin doses ($>1.5 \text{ U/cat/dose}$) | B | src-diabetes-075 | Clinical feature predictor |
| ACR3 | Diagnostics require checking serum insulin-like growth factor 1 (IGF-1) levels, with values $>1000 \text{ ng/mL}$ strongly suggestive | B | src-diabetes-075, src-diabetes-061 | Diagnostic threshold |
| ACR4 | Medical management options include pasireotide (somatostatin analogue) or cabergoline (dopamine agonist) | B | src-diabetes-090, src-diabetes-092, src-diabetes-114 | Treatment options |

## Evidence-Depth Caveat

This page compiles differential diagnosis and management rules for feline acromegaly from endocrinology studies and clinical trials, including investigations of pasireotide (`src-diabetes-090`) and cabergoline (`src-diabetes-092`, `src-diabetes-114`). This page cites abstract-weighted sources and is not decision-grade clinical guidance. Clinical presentation varies, and diagnosis must combine endocrine testing with pituitary imaging (CT/MRI) where possible.

---

## 1. Clinical Presentation & Screen Timing

Feline acromegaly (hypersomatotropism) is an underdiagnosed comorbidity. Growth hormone (GH) excess induces high levels of insulin-like growth factor-1 (IGF-1), leading to anabolic tissue changes and profound insulin resistance.

### 1.1 When to Screen (Red Flags)
Veterinarians should suspect acromegaly and perform screening in diabetic cats exhibiting:
* **Insulin Resistance:** Poor glycemic control despite insulin doses exceeding $1.5 \text{ to } 2.0 \text{ U/kg/dose}$ (or $>6.0 \text{ U/cat/dose}$).
* **Atypical Weight Patterns:** Maintenance of body weight, or active weight gain (anabolic effect), despite persistent hyperglycemia and polyuria.
* **Physical Alterations:** Broad facial features (due to bone expansion), prognathia inferior (lower jaw protrusion), organomegaly (renomegaly, hepatomegaly), or a new systolic heart murmur.

---

## 2. Diagnostic Workup Protocol

```
         [Diabetic Cat with Insulin Resistance]
                           │
                           ▼
                  [Step 1: Serum IGF-1]
         Measure serum IGF-1 (radioimmunoassay)
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
   [< 800 ng/mL]     [800-1000 ng/mL]  [> 1000 ng/mL]
    Unlikely          Grey Zone         Highly Likely
                      (Re-test)              │
                                             ▼
                                    [Step 2: Imaging]
                                   Pituitary CT or MRI
                                   Detect tumor mass
                                             │
                                             ▼
                                 [Diagnosed Acromegaly]
```

### 2.1 Laboratory Diagnostics
* **Serum IGF-1:** The primary screening test. 
  * $\text{IGF-1} < 800 \text{ ng/mL}$: Acromegaly is highly unlikely.
  * $\text{IGF-1 } 800 \text{ to } 1000 \text{ ng/mL}$: Grey zone; re-test in 2-3 months or proceed to imaging.
  * $\text{IGF-1} > 1000 \text{ ng/mL}$: Strongly diagnostic of hypersomatotropism in a diabetic cat.
* *Note:* Retest IGF-1 at least 6-8 weeks after starting insulin, as insulin therapy is required for hepatic IGF-1 synthesis; untreated diabetics may show false-low IGF-1.

### 2.2 Advanced Imaging
* **Pituitary CT or MRI:** Essential to visualize the pituitary adenoma, assess tumor size, and rule out neurological compression risk.

---

## 3. Therapeutic Management Options

Managing acromegaly aims to control insulin resistance, reduce GH/IGF-1 levels, and manage tumor growth.

### 3.1 Medical Therapies
* **Pasireotide (SOM230):** A multi-receptor somatostatin analogue.
  * *Efficacy:* Highly effective at reducing IGF-1 and insulin resistance ([src-diabetes-090]).
  * *Limitation:* High cost, and subcutaneous injection is required (monthly depot or daily short-acting).
* **Cabergoline:** A dopamine agonist.
  * *Efficacy:* Reduces insulin requirement and IGF-1 in a subset of cats ([src-diabetes-092], [src-diabetes-114]).
  * *Advantage:* Orally administered, affordable, and safe.

### 3.2 Definitive Therapies
* **Hypophysectomy:** Surgical removal of the pituitary gland. Offers the highest rate of diabetic remission, but requires lifelong hormone replacement (thyroxine, cortisone, DDAVP) and advanced surgical teams.
* **Radiation Therapy:** Stereotactic radiosurgery (SRS) to shrink the adenoma. Slow reduction in insulin resistance over months.

---

## What the Module Can Say Safely
* Acromegaly is a common cause of refractory diabetes and severe insulin resistance in cats.
* Serum IGF-1 $>1000 \text{ ng/mL}$ is the primary screening indicator.
* Medical treatments like cabergoline or pasireotide can reduce insulin needs, but surgical hypophysectomy offers the best cure rate.

## What the Module Should Not Say Yet
* Do not diagnose acromegaly based on insulin resistance alone without checking IGF-1 or imaging.
* Do not assume all acromegalic cats will exhibit physical enlargement or prognathism (early cases present with diabetes only).
* Do not guarantee complete tumor control with cabergoline.
