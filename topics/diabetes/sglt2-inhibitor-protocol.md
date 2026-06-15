---
id: topic-diabetes-sglt2-inhibitor-protocol
type: topic
topic: diabetes
species: feline
disease: diabetes mellitus
question_type: treatment
source_ids: [src-diabetes-011, src-diabetes-035, src-reg-010, src-reg-011, src-reg-012, src-reg-013]
last_compiled_at: 2026-06-15
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Feline SGLT2 Inhibitor Clinical Screening and Monitoring Protocol

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| SGLT1 | Oral SGLT2 inhibitors (e.g., velagliflozin, bexagliflozin) are effective stand-alone therapies for feline diabetes mellitus | B | src-diabetes-035, src-diabetes-011 | Must be insulin-naive and otherwise healthy |
| SGLT2 | Pre-treatment screening must rule out pancreatitis, renal dysfunction, and insulin-dependent state | B | src-reg-012, src-reg-013 | Diagnostic boundary, not clinical suggestion |
| SGLT3 | SGLT2 inhibitors carry a critical risk of diabetic ketoacidosis (DKA) or euglycemic DKA | A | src-diabetes-035, src-reg-012, src-reg-013 | Key safety guardrail |
| SGLT4 | Daily monitoring of ketones is essential during the initial initiation period | B | src-reg-012, src-reg-013 | Monitoring protocol standard |

## Evidence-Depth Caveat

This page is compiled from U.S. FDA regulatory labels and clinical trials, including the SENSATION study (`src-diabetes-035`) which evaluated velagliflozin in 190 diabetic cats. This page cites abstract-weighted sources and is not decision-grade clinical guidance. It provides a structured synthesis of screening and monitoring rules, but it does not replace professional veterinary consultation or individual patient assessment.

---

## 1. Patient Selection Criteria

SGLT2 inhibitors represent a paradigm shift in feline diabetes management, offering oral, once-daily dosing. However, patient selection is narrow and critical.

### 1.1 Indications / Inclusion
* **Insulin-Naive Cats:** Cats newly diagnosed with diabetes mellitus that have not yet received insulin therapy.
* **Otherwise Healthy:** No concurrent systemic illnesses such as chronic kidney disease (IRIS Stage 3 or 4), active pancreatitis, or hepatic dysfunction.
* **Clinically Stable:** Capable of eating, drinking, and showing no signs of systemic dehydration or ketoacidosis.

### 1.2 Absolute Contraindications
* **Prior Insulin Therapy:** Cats currently receiving or previously treated with insulin must not be transitioned to SGLT2 inhibitors.
* **Insulin-Dependent Diabetes:** Cats with chronic beta-cell failure or secondary diabetes that absolutely require exogenous insulin.
* **Ketoacidosis:** Active diabetic ketoacidosis (DKA) or history of recurrent DKA.
* **Pancreatitis comorbidity:** Cats with clinical signs of acute or chronic active pancreatitis.

---

## 2. Pre-Treatment Screening Protocol

Before administering the first dose of velagliflozin or bexagliflozin, veterinarians must execute a strict screening protocol to ensure safety.

```
       [Newly Diagnosed Diabetic Cat]
                     │
                     ▼
          [Step 1: Clinical History]
     Is the cat insulin-naive & active?
        ├── No ──────► [DO NOT USE SGLT2]
        └── Yes
             │
             ▼
          [Step 2: Lab Screening]
     Perform CBC, Chemistry, fPLI, UA
     Are ketones present in blood/urine?
        ├── Yes ─────► [DO NOT USE SGLT2]
        └── No
             │
             ▼
     Is fPLI elevated or liver/renal impaired?
        ├── Yes ─────► [DO NOT USE SGLT2]
        └── No ──────► [Approved for SGLT2 Therapy]
```

### 2.1 Laboratory Workup
1. **Complete Blood Count (CBC) & Chemistry Profile:** Evaluate renal parameters (SDMA, Creatinine) and liver enzymes.
2. **Pancreatic Specific Lipase (fPLI):** Must be performed to rule out subclinical pancreatitis.
3. **Urinalysis (UA) & Urine/Blood Ketone Test:** Ketones must be completely absent. If blood $\beta$-hydroxybutyrate ($\beta$-HB) is $>1.5 \text{ mmol/L}$, SGLT2 inhibitors are contraindicated.

---

## 3. Monitoring & Safety Guardrails

The governing risk of SGLT2 inhibitor therapy is **Euglycemic Diabetic Ketoacidosis (DKA)**—a condition where the cat develops ketoacidosis but maintains normal or only mildly elevated blood glucose levels (under $14 \text{ mmol/L}$ or $250 \text{ mg/dL}$), masking the severity of the illness.

### 3.1 Daily Monitoring Protocol (Weeks 1 - 2)
* **Ketone Monitoring:** The owner must check blood or urine ketones daily for the first 14 days. 
  * If blood ketones ($\beta$-HB) rise above $1.5 \text{ mmol/L}$, or urine ketones are $>1+$, stop SGLT2 immediately and evaluate for DKA.
* **Appetite & Activity Check:** SGLT2 inhibitors must be discontinued immediately if the cat develops anorexia, lethargy, vomiting, or diarrhea.

### 3.2 Long-Term Follow-up (Week 2, 4, and monthly)
* **Clinical Assessments:** Monitor body weight, hydration status, and clinical signs of polyuria/polydipsia.
* **Fructosamine / Glycemic Control:** Assess glycemic response using fructosamine levels. SGLT2 inhibitors typically reduce fructosamine within 2 to 4 weeks.

---

## 4. Emergency Management of Euglycemic DKA

If a cat on SGLT2 therapy presents with anorexia, vomiting, or lethargy:

1. **Stop SGLT2 Inhibitor:** Immediately discontinue the oral medication.
2. **Check Blood Ketones:** Measure $\beta$-HB. If elevated, initiate DKA treatment.
3. **Aggressive Fluid Therapy:** Administer IV fluids containing dextrose to prevent hypoglycemia while treating acidosis.
4. **Regular Insulin Therapy:** Administer low-dose regular insulin infusions or intermittent IM/SC injections to suppress ketogenesis, even if blood glucose is not markedly elevated.

---

## What the Module Can Say Safely
* SGLT2 inhibitors (Bexacat/Senvelgo) provide convenient oral once-daily dosing.
* Pre-treatment laboratory screening is mandatory to rule out renal failure, pancreatitis, and DKA.
* Euglycemic DKA is a life-threatening risk; ketones must be checked frequently.
* Appetite loss or lethargy requires immediate discontinuation of SGLT2 inhibitors.

## What the Module Should Not Say Yet
* Do not recommend SGLT2 inhibitors for cats that have failed insulin therapy (contraindicated).
* Do not claim SGLT2 inhibitors are safer or more effective than insulin (treatment superiority is not established).
* Do not bypass pre-treatment laboratory workups.
