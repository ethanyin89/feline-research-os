---
id: feline-source-metadata-check-20260513
type: system
topic: content-pipeline
question_type: source-check-report
language: zh
last_compiled_at: 2026-05-13
verification_status: generated
decision_grade: no
owner: codex
status: active
---

# Feline Source Metadata Check, 2026-05-13

Source set: `diabetes/obesity priority sample 2026-05-13`

## Rule

This report is a second-pass sample check. It does not make clinical claims.

- DOI metadata alone does not upgrade a card.
- Abstract availability can justify `abstract_weighted` only for navigation and extraction priority.
- Full-text or structured worksheet review is still required before `source_checked` or `deep_extracted`.

## Summary

- Cards checked: `10`
- Crossref metadata found: `10`
- Abstract available: `8`

## Check Table

| Source | Current | Recommended | DOI | Year | Container | Abstract | Error |
|---|---|---|---|---:|---|---|---|
| `src-diabetes-050` | `abstract_weighted` | `abstract_weighted` | `10.1177/1098612x15571880` | 2015 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-diabetes-087` | `abstract_weighted` | `abstract_weighted` | `10.5326/jaaha-ms-6822` | 2018 | Journal of the American Animal Hospital Association | `yes` |  |
| `src-diabetes-046` | `title_only` | `title_only` | `10.1016/j.cvsm.2023.02.001` | 2023 | Veterinary Clinics of North America: Small Animal Practice | `no` |  |
| `src-diabetes-035` | `abstract_weighted` | `abstract_weighted` | `10.2460/javma.24.03.0174` | 2024 | Journal of the American Veterinary Medical Association | `yes` |  |
| `src-diabetes-091` | `abstract_weighted` | `abstract_weighted` | `10.1111/jvim.16625` | 2023 | Journal of Veterinary Internal Medicine | `yes` |  |
| `src-obesity-001` | `title_only` | `title_only` | `10.17221/145/2015-vetmed` | 2016 | Veterinární medicína | `no` |  |
| `src-obesity-004` | `abstract_weighted` | `abstract_weighted` | `10.1177/1098612x241285519` | 2024 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-obesity-005` | `abstract_weighted` | `abstract_weighted` | `10.1177/1098612x241228042` | 2024 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-obesity-008` | `abstract_weighted` | `abstract_weighted` | `10.1053/jfms.2001.0138` | 2001 | Journal of Feline Medicine and Surgery | `yes` |  |
| `src-obesity-080` | `abstract_weighted` | `abstract_weighted` | `10.2460/ajvr.79.2.181` | 2018 | American Journal of Veterinary Research | `yes` |  |

## Abstract Availability Notes

### `src-diabetes-050`

- Crossref title: ISFM Consensus Guidelines on the Practical Management of Diabetes Mellitus in Cats
- Abstract lead for scope check only: Practical relevance: Diabetes mellitus (DM) is a common endocrinopathy in cats that appears to be increasing in prevalence. The prognosis for affected cats can be good when the di...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-diabetes-087`

- Crossref title: 2018 AAHA Diabetes Management Guidelines for Dogs and Cats*
- Abstract lead for scope check only: ABSTRACT Diabetes mellitus (DM) is a common disease encountered in canine and feline medicine. The 2018 AAHA Diabetes Management Guidelines for Dogs and Cats revise and update ear...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-diabetes-046`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-diabetes-035`

- Crossref title: Velagliflozin, a once-daily, liquid, oral SGLT2 inhibitor, is effective as a stand-alone therapy for feline diabetes mellitus: the SENSATION study
- Abstract lead for scope check only: Abstract OBJECTIVE To investigate safety and effectiveness of velagliflozin oral solution as sole therapy in naïve and previously insulin-treated diabetic cats. ANIMALS 252 client...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-diabetes-091`

- Crossref title: Survival, remission, and quality of life in diabetic cats
- Abstract lead for scope check only: Abstract Background Remission is documented in a substantial proportion of cats with diabetes. The effects of diabetes mellitus (DM) on the lives of cats and their owners should b...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-obesity-001`

- Crossref metadata resolved, but no abstract was available from Crossref.
- Keep the card at its current status until abstract or full text is read.

### `src-obesity-004`

- Crossref title: Overweight and obesity in domestic cats: epidemiological risk factors and associated pathologies
- Abstract lead for scope check only: The domestic cat has evolved in various aspects in its journey from original domestication to the present day. Many domestic cats today lead a sedentary indoor lifestyle with low...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-obesity-005`

- Crossref title: Identifying the target population and preventive strategies to combat feline obesity
- Abstract lead for scope check only: Feline obesity continues to be a priority health and welfare issue. Most research surrounding obesity currently focuses on obesity treatment. However, treatment for feline obesity...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-obesity-008`

- Crossref title: Insulin Sensitivity Decreases with Obesity, and Lean Cats with Low Insulin Sensitivity are at Greatest Risk of Glucose Intolerance with Weight Gain
- Abstract lead for scope check only: This study quantifies the effects of marked weight gain on glucose and insulin metabolism in 16 cats which increased their weight by an average of 44.2% over 10 months. Significan...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.

### `src-obesity-080`

- Crossref title: Effects of weight loss with a moderate-protein, high-fiber diet on body composition, voluntary physical activity, and fecal microbiota of obese cats
- Abstract lead for scope check only: Abstract OBJECTIVE To determine effects of restriction feeding of a moderate-protein, high-fiber diet on loss of body weight (BW), voluntary physical activity, body composition, a...
- Card can be upgraded only to abstract-weighted; do not promote clinical claims from this note.
