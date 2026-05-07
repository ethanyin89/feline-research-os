---
id: topic-ckd-pathology-correlations
type: topic
topic: ckd
species: feline
disease: CKD
question_type: mechanism
source_ids: [src-ckd-010, src-ckd-016, src-ckd-017]
last_compiled_at: 2026-04-09
confidence: medium
owner: codex
status: active
---

# Feline CKD Pathology Correlations

## Question This Page Answers

Which renal lesions in feline CKD are most clearly tied to commonly used clinical markers?

## Quantified Claim Traceability

| Claim | Source IDs | Boundary |
|---|---|---|
| The histomorphometry study included kidneys from 80 cats with plasma biochemical data from the last 2 months of life. | src-ckd-010 | Necropsy-linked pathology-correlation design; not early-screening evidence. |
| CKD entry in that study required creatinine above 2.0 mg/dl plus compatible history and clinical signs. | src-ckd-010 | Study inclusion criterion; not a universal diagnostic rule replacing guidelines. |
| Proteinuric-kidney-disease data reported 58% ICGN in proteinuric cats and higher median UPC in non-ICGN glomerular diseases than ICGN (14.5 vs 6.5; P <0.001). | src-ckd-017 | Proteinuric subset evidence; not whole-population CKD prevalence. |

## Current Conclusions

### quoted_fact

- The histomorphometry study included kidneys from 80 cats with plasma biochemical data from the last 2 months of life.
- Cats were recruited through 2 London first-opinion practices between 1992 and 2010.
- CKD entry required creatinine above 2.0 mg/dl plus history and clinical signs compatible with chronic disease.
- Renal sections were scored semiquantitatively for glomerulosclerosis, interstitial inflammation, and fibrosis.
- Systolic blood pressure in the study was measured as the mean of 5 Doppler readings per visit, and time-averaged systolic blood pressure was used for analysis.
- Interstitial fibrosis was the lesion best correlated with severity of azotemia, hyperphosphatemia, and anaemia.
- Proteinuria was associated with interstitial fibrosis and glomerular hypertrophy.
- Higher time-averaged systolic blood pressure was associated with glomerulosclerosis and hyperplastic arteriolosclerosis.
- The proteinuric-kidney-disease study found that 58% of proteinuric cats had immune-complex glomerulonephritis and that cats with glomerular diseases other than ICGN had a higher median UPC than ICGN cats (14.5 vs 6.5; P <0.001).
- The aged-cat CKD review describes typical histologic features as interstitial inflammation, tubular atrophy, and fibrosis with secondary glomerulosclerosis.

### source_supported_conclusion

- `Interstitial fibrosis` is the strongest pathology anchor in the current vault because it links structural disease to multiple routine clinical markers.
- The aged-cat review strengthens the view that spontaneous feline CKD is mostly a tubulointerstitial and fibrosis-centered lesion pattern, not a heavily proteinuric primary glomerular disease by default.
- `Proteinuria` and `systolic blood pressure` should not be treated as free-floating monitoring variables; this study ties them to specific structural lesions.
- The new proteinuric-kidney-disease study sharpens that point further by showing that proteinuria in cats can reflect distinct glomerular disease compartments, not just general CKD severity.
- This source supports a multi-axis reading of CKD markers: fibrosis-linked markers are not identical to glomerulo-vascular injury-linked markers.
- This source is one of the best primary-study anchors for defending the fibrosis-centered framing of feline CKD.
- This page should now be read as a consequence-mapping page, not only a correlation page, because different endpoints point toward different structural injury patterns.

### llm_inference

- When the vault talks about mechanism-endpoint linkage, this page should be treated as the main primary-study evidence bridge rather than relying only on review language.

## Pathology-Marker Matrix

| Lesion / Structural Change | Correlated Marker | Why This Matters | Current Role In Vault | Main Limit |
|---|---|---|---|---|
| Interstitial fibrosis | azotemia / creatinine context | links structural injury to renal dysfunction severity | primary mechanism anchor | exact coefficient ranking still not extracted |
| Interstitial fibrosis | hyperphosphatemia | links structural disease to a clinically actionable progression marker | mechanism-endpoint bridge | serum phosphorus may lag early retention biology |
| Interstitial fibrosis | anaemia | shows advanced structural disease has systemic downstream context | pathology-linked context marker | not a first-wave screening variable |
| Interstitial fibrosis + glomerular hypertrophy | proteinuria / UPCR context | supports proteinuria as more than simple substaging paperwork | core bridge endpoint | correlation does not by itself define treatment response |
| Glomerulosclerosis + hyperplastic arteriolosclerosis | time-averaged systolic blood pressure | ties hemodynamic signal to structural vascular and glomerular injury | core CKD comorbidity bridge | monitoring cadence and treatment effect detail still need more sources |
| Immune-complex and other glomerular diseases | UPC magnitude / protein-losing nephropathy context | shows that proteinuria may reflect different glomerular compartments and not just generic CKD severity | pathology-aware proteinuria interpretation | subset paper, not whole-population CKD map |
| Tubulointerstitial lesion pattern in aged cats | fibrosis-centered spontaneous CKD frame | helps anchor the default lesion identity of broad feline CKD | broad disease-framing anchor | review-level and not a quantitative correlation study |

## What This Page Says Clearly

1. The fibrosis-centered framing of feline CKD is not just review-level opinion in this vault.
2. Phosphorus, proteinuria, blood pressure, and anaemia all become more interpretable once structural lesion data are considered.
3. Proteinuria is now better grounded as a compartment-aware signal, not only a staging number.
4. Pathology correlation is one of the strongest reasons not to flatten CKD into a single “kidney number” mindset.
5. Different endpoints matter not only because they correlate with disease, but because they appear to carry different structural-consequence meaning.

## What We Should Not Overstate

- that this one study fully resolves lesion hierarchy in feline CKD
- that correlation alone proves causal treatment-response pathways
- that pathology-linked markers automatically become the best practical screening markers

## Write-Back Targets

- [mechanism overview](mechanism-overview.md)
- [endpoint handbook](endpoint-handbook.md)
- [synthesis index](synthesis-index.md)
