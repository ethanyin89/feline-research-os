---
id: feline-ckd-extension-claim-fit-queue-20260605
type: system
topic: ckd
question_type: claim-fit-queue
language: zh
last_compiled_at: 2026-06-05
verification_status: abstract_weighted
decision_grade: no
owner: codex
status: active
---

# CKD Extension Claim-Fit Queue, 2026-06-05

## Boundary

This queue is built from abstract-only worksheets for CKD Google Sheet extension sources. It can decide extraction priority and branch placement, but it cannot support reader-facing clinical claims yet.

Source index:

- `system/indexes/feline-ckd-extension-structured-abstract-20260605.md`

## Priority Queue

| Priority | Source | Abstract Signal | Likely Branch | Why Next | Current Limit |
|---:|---|---|---|---|---|
| 1 | `src-ckd-026` | FGF-23, hyperphosphatemia, phosphate/phosphorus, staging; 304 cats | phosphorus / mineral-burden endpoint | Could refine the phosphorus-control artifact beyond diet-vs-binder hierarchy into staging/endocrine burden. | Abstract-only; no numeric thresholds or staging rule can be reused yet. |
| 2 | `src-ckd-034` | risk factor, CKD; 101 cats; methods/results/conclusions detected | risk architecture | Could add modern risk/protective-factor nuance without reopening the mature seed bootstrap. | Abstract-only; risk ranking and causality remain blocked. |
| 3 | `src-ckd-033` | urinary tract infection, survival/risk factor; 25 cats | comorbidity / UTI boundary | Could create a narrow CKD + UTI boundary card for screening vs overgeneralized infection claims. | Small population signal; no prevalence or treatment rule should be lifted. |
| 4 | `src-ckd-045` | proteinuria, albuminuria; methods/results/conclusions detected | proteinuria endpoint | Could strengthen UPC/proteinuria branch if a claim artifact needs subtyping beyond existing seed coverage. | Abstract-only; electrophoretic pattern details require source review. |
| 5 | `src-ckd-043` | carbonyl stress, uraemic toxin, biomarker | uremic toxin / mechanism endpoint | Useful if the product needs a mechanistic biomarker watchlist, not routine monitoring advice. | Abstract-only; no biomarker recommendation should be inferred. |
| 6 | `src-ckd-035` | cytokine; 26 cats | inflammation endpoint | Could support an inflammation-marker watchlist or research-gap artifact. | Abstract-only and likely exploratory. |
| 7 | `src-ckd-046` | ultrasonography; practical relevance | imaging boundary | May refine ultrasound branch boundaries, especially normal/abnormal kidney wording. | Review-level but abstract-only; no imaging protocol details yet. |
| 8 | `src-ckd-025` | resistivity/pulsatility, ultrasonography | imaging endpoint | Systematic-review title makes it a candidate for imaging endpoint extraction. | Abstract-only; no diagnostic ranking or threshold claims yet. |

## Suggested Content Moves

1. Drafted a non-promotable claim card around `src-ckd-026`: `outputs/business/ckd-fgf23-phosphorus-staging-claim-card-20260605.md`.
2. Build a revised CKD phosphorus/staging claim card around `src-ckd-026`, but only after a real abstract extraction or source worksheet captures the actual results.
3. Drafted a non-promotable risk-architecture claim card around `src-ckd-034`: `outputs/business/ckd-risk-protective-factors-architecture-claim-card-20260605.md`.
4. Build a narrow CKD comorbidity boundary card around `src-ckd-033` if the product needs to answer “should CKD cats be routinely urine-cultured?” with appropriate caveats.
5. Keep `src-ckd-030` and other intervention/product-like extension sources outside claim generation until source text is reviewed.

## PubMed Fallback Additions, 2026-06-06

Six previously title-only sources now have PubMed-backed structured abstract worksheets:

| Source | Branch signal | Safe next use |
|---|---|---|
| `src-ckd-027` | metabolomics / uremic toxins | Mechanism and biomarker extraction candidate; no clinical biomarker recommendation yet. |
| `src-ckd-029` | phosphate binder supplementation / renal diet | High-risk intervention candidate; requires full abstract or full text before treatment claims. |
| `src-ckd-039` | peritubular capillary change | Mechanism branch candidate; canine/feline population boundaries must remain explicit. |
| `src-ckd-044` | homocysteine / proteinuria | Exploratory metabolic endpoint candidate; no routine-monitoring recommendation. |
| `src-ckd-047` | progressive CKD pathogenesis | Broad mechanism-review candidate and likely high-reuse deep-extraction target. |
| `src-ckd-049` | feeding-tube management | Management-boundary candidate; requires source review before practical recommendations. |

`src-ckd-032` remains title-only because PMID `24783628` has no PubMed abstract.

## Full-Text Promotions, 2026-06-06

- `src-ckd-027` is now `deep_extracted`. Use it for metabolomics and gut-derived uremic-toxin branch architecture, not diagnostic thresholds or treatment recommendations.
- `src-ckd-029` is now `deep_extracted`. Use it as a guarded source-specific phosphorus-control signal with explicit nonrandomized, small-sample, multi-ingredient, and manufacturer-conflict limits.
- `src-ckd-030` is now `deep_extracted`. Use it for probiotic trial design and failure-mode mapping only: 12 enrolled, 6 completed, no control group, nonsignificant toxin endpoints, and increased serum phosphate.
- `src-ckd-050` is now `deep_extracted`. Use it for direct feline in-vitro TGF-beta/fibroblast evidence, with treatment implications explicitly out of scope.
- The cross-source owner is `system/indexes/ckd-uremic-toxin-microbiome-bridge-memo-20260606.md`.
- None of these sources independently justifies reader-facing treatment changes.

## Do Not Do Yet

- Do not update CKD topic pages from these worksheets alone.
- Do not turn abstract signals into numeric thresholds, prevalence claims, treatment rankings, or owner advice.
- Do not treat `abstract_weighted` as `source_checked`.
