---
id: diabetes-extension-source-queue-20260513
type: system
topic: diabetes
question_type: source-queue
language: zh
last_compiled_at: 2026-05-13
verification_status: compiled
decision_grade: no
owner: codex
status: active
---

# Diabetes Extension Source Queue, 2026-05-13

This queue is derived from [feline diabetes / obesity intake manifest](feline-diabetes-obesity-intake-manifest-20260513.md).

It does not replace the current 24-source diabetes corpus. The current corpus remains the canonical diabetes module until new rows are first-pass ingested and reviewed.

## Current Intake Read

| Class | Count | Handling |
|---|---:|---|
| existing diabetes seed / duplicate-to-seed rows | 35 | no new source card |
| new diabetes candidates | 94 | queue for first-pass ingest |
| shared diabetes-obesity existing rows | 5 | cross-link / owner note, not duplicate evidence text |
| duplicate-in-sheet rows | 5 | hold behind first occurrence |

## Tier A — Read First

These rows are most likely to change branch order, treatment boundaries, or output-facing answers.

| Sheet Row | Proposed Role | Title | Locator |
|---:|---|---|---|
| 62 | practice-guideline control | ISFM Consensus Guidelines on the Practical Management of Diabetes Mellitus in Cats | `10.1177/1098612X15571880` |
| 99 | practice-guideline control | 2018 AAHA Diabetes Management Guidelines for Dogs and Cats | `10.5326/JAAHA-MS-6822` |
| 58 | remission / prediabetes mechanism update | Pathophysiology of Prediabetes, Diabetes, and Diabetic Remission in Cats | `10.1016/J.CVSM.2023.02.001` |
| 47 | SGLT2 treatment-control study | Velagliflozin, a once-daily, liquid, oral SGLT2 inhibitor, is effective as a stand-alone therapy for feline diabetes mellitus: the SENSATION study | `10.2460/JAVMA.24.03.0174` |
| 68 | incretin frontier review | Incretin therapy in feline diabetes mellitus - a review of the current state of research | `10.1016/J.DOMANIEND.2024.106869` |
| 103 | outcome / quality-of-life anchor | Survival, remission, and quality of life in diabetic cats | `10.1111/JVIM.16625` |
| 79 | large epidemiology anchor | Epidemiology of Diabetes Mellitus among 193,435 Cats Attending Primary-Care Veterinary Practices in England | `10.1111/JVIM.14365` |
| 115 | environmental risk anchor | Environmental Risk Factors for Diabetes Mellitus in Cats | `10.1111/JVIM.14618` |
| 123 | insulin remission comparison | Treatment of newly diagnosed diabetic cats with glargine insulin improves glycaemic control and results in higher probability of remission than protamine zinc and lente insulins | `10.1016/J.JFMS.2009.05.016` |
| 81 | DKA diagnostic endpoint | Point-of-care beta-hydroxybutyrate measurement for the diagnosis of feline diabetic ketoacidaemia | `10.1111/J.1748-5827.2012.01204.X` |

## Tier B — Read Next

These should be first-pass ingested after Tier A because they deepen already-existing branches.

| Branch | Candidate Rows |
|---|---|
| insulin / protocol / monitoring | 33, 45, 84, 85, 94, 110, 111, 122, 124 |
| endocrine-secondary diabetes | 46, 48, 60, 61, 73, 87, 102, 104, 107, 120, 126 |
| remission / quality of life / owner burden | 66, 90, 93, 97, 103, 108, 109, 116 |
| obesity / insulin resistance / adipokines | 27, 35, 52, 67, 77, 119, 125 |
| pancreatitis / DKA / exocrine pancreas | 57, 63, 70, 101, 129, 130 |
| epidemiology / risk factors | 42, 49, 72, 79, 88, 91, 92, 106, 115, 118, 128 |
| complications / neuropathy / cataract / kidney overlap | 43, 69, 74, 78, 98, 112 |

## Tier C — Hold Or Context

Do not prioritize these until a specific output needs them:

- broad cross-species chapters or human-animal comparison rows
- older personal-experience or broad treatment commentary rows
- case reports unless they expose a rescue/failure mode
- duplicate DOI rows that appear again in the obesity segment

## First-Pass Ingest Rule

When creating `src-diabetes-025+` cards:

1. Use source cards only after verifying at least title, locator, year, source family, and claim-fit.
2. Leave `quoted_fact` empty unless exact source text has been read.
3. Use `verification_status: title_only`, `abstract_weighted`, `source_checked`, or stricter only when true. Do not invent new verification labels.
4. Do not promote claims to topic pages in the same pass unless the card has enough source support.
5. Run markdown link checks and source-card required-field checks after writes.

## Deep Extraction Candidates

Start with:

1. row 62, ISFM consensus guideline
2. row 99, 2018 AAHA guideline
3. row 58, prediabetes / remission pathophysiology review
4. row 47, velagliflozin SENSATION study, paired with existing SGLT2 label/FOI controls
5. row 103, survival/remission/QoL study

These are the only rows currently strong enough to pre-commit as likely deep-extraction candidates.
