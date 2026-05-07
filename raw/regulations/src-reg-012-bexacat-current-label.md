---
id: src-reg-012
type: source
title: "DailyMed Current Label: Bexacat (bexagliflozin tablets)"
source_kind: regulation
species: feline
diseases: [diabetes mellitus]
models: []
endpoints: [glycemic-control, safety, ketoacidosis, monitoring]
jurisdictions: [USA]
evidence_level: regulation
year: 2023
status: extracted
extraction_depth: partial
verification_status: source_checked
decision_grade: no
language_qa_status: not_applicable
tags: [dailymed, fda, bexacat, bexagliflozin, sglt2, diabetes, current-label]
links:
  doi: ""
  url: "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f918583d-0337-40da-8da1-1e1320b8d027"
  local_assets: []
evidence_policy:
  quoted_fact:
    - "DailyMed lists Bexacat as approved under NADA #141-566."
  source_supported_conclusion:
    - "The current Bexacat label preserves the otherwise-healthy, insulin-naive indication boundary."
    - "The current Bexacat label foregrounds diabetic ketoacidosis/euglycemic diabetic ketoacidosis risk, insulin-related contraindications, and pre-treatment screening."
    - "Bexacat label control should govern owner-facing SGLT2 language more strongly than review abstracts."
  llm_inference: []
---

# DailyMed Current Label: Bexacat (bexagliflozin tablets)

## One-Line Summary

Current DailyMed animal-drug label for Bexacat, used to control indication, warning, dosing, and monitoring language for the feline diabetes SGLT2 branch.

## Why It Matters For Feline Diabetes

- upgrades Bexacat from FDA FOI source control to current-label source control
- captures current warning and monitoring language in a label-oriented source card
- prevents treatment pages from treating oral administration as the main SGLT2 message

## Key Findings

- DailyMed lists Bexacat as a prescription animal drug label with NADA 141-566.
- The label is for bexagliflozin 15 mg flavored tablets for oral use in cats only.
- The indication is to improve glycemic control in otherwise healthy cats with diabetes mellitus not previously treated with insulin.
- Dosing is one tablet by mouth once daily for cats weighing at least 3.0 kg, with or without food and regardless of blood glucose level.
- The label contains a diabetic ketoacidosis/euglycemic diabetic ketoacidosis warning.
- The label says not to use Bexacat in cats previously treated with insulin, receiving insulin, or with insulin-dependent diabetes mellitus.
- The label says Bexacat should not be initiated in cats with anorexia, dehydration, or lethargy at diagnosis or without appropriate screening tests.
- Sudden hyporexia/anorexia, lethargy, dehydration, or weight loss while receiving Bexacat should trigger discontinuation and assessment for diabetic ketoacidosis regardless of blood glucose level.

## Limits / Caveats

- this is U.S. label control, not global approval status
- this source does not compare Bexacat with Senvelgo or insulin
- use current DailyMed/FDA label access dates when producing external-facing regulatory text

## Open Follow-Up Questions

- which exact current-label contraindication and adverse-reaction sections need full extraction?
- should the Animal Drugs @ FDA labeling PDF be stored as a local asset for audit stability?
- how should owner-facing warnings be phrased without becoming clinical advice?

## Linked Entities

- diseases: diabetes mellitus
- models:
- endpoints: glycemic control, ketoacidosis, euglycemic ketoacidosis, monitoring
- mechanisms: SGLT2 inhibition, renal glucosuria
- regulations: FDA CVM, NADA 141-566, DailyMed label
