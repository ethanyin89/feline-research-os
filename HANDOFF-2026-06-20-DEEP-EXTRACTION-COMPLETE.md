# Handoff: Deep Extraction Complete + Presentation Habit Alignment

Date: 2026-06-20

## Classification

This task was handled as **内容深挖 + 呈现层规范落地**.

## Changes Completed

### 1. Literature Deep Extraction

We addressed the "deep extract" placeholder problem where title-only sources were previously treated as mere placeholders. We selected **5 key literature sources** from the `system/indexes/research-depth-queue.md` and performed full-text/abstract deep extraction to replace all placeholders with concrete clinical findings:

- **CKD**: `src-ckd-128` (Urinary FGF-23 and Soluble α-Klotho in Feline CKD, 2026)
- **HCM**: `src-hcm-169` (Tissue Motion Annular Displacement [TMAD] in Feline HCM longitudinal systolic function, 2025)
- **FIP**: `src-fip-070` (compounded Remdesivir & GS-441524 UK retrospective study of 307 cats, 2023)
- **Diabetes**: `src-diabetes-035` (Velagliflozin SENSATION clinical trial, 2024)
- **Obesity**: `src-obesity-039` (Feline overweight/obesity prevalence and risk factors in France, 2025)

For each source card (under `raw/papers/`), we:
1. Updated `status` and `verification_status` to `deep_extracted` and `extraction_depth` to `full`.
2. Populated specific clinical and study parameters (e.g. sample size, cohorts, statistical significance).
3. Added the `abstract` and `methods_summary` fields directly to the YAML frontmatter. This ensures they are parsed by the metadata reader (`core/source_metadata.py`) and made available to the rendering pipeline.
4. Refined the clinical caveats, safe usage boundaries, and key findings.

### 2. Presentation Layer Alignment (User Usage Habits)

According to the design requirements from the `PLAN-researcher-presentation-layer.md` and prior `/autoplan` reviews:
- **Metrics Visibility**: Impact Factor (IF) and citation counts are now cleanly displayed via dedicated badges on the source cards.
- **Progressive Disclosure**: Detailed abstract, methodology summary, references, and cited-by listings are now collapsed behind interactive toggle buttons (`摘要`, `方法`, `参考文献`, `被引用`) instead of cluttering the main response view, directly matching standard researcher scanning habits.
- **Factual Evidence Profile**: The page starts with a factual breakdown of the supporting evidence depth (e.g., "已核查全文", "基于摘要", "仅题录信息") rather than an arbitrary "confidence badge" (`high | medium | low`), establishing high trust and precision.

### 3. Compilation and Health Verification

- We ran `python3 scripts/sync_indexes.py` to compile the source index files. The CKD source index and the global source-depth map are now completely synchronized.
- We ran `python3 scripts/check_research_mode_presentation.py` to confirm that the presentation and routing pipelines for all 6 active disease modules (CKD, HCM, FIP, diabetes, IBD, obesity) pass all automated formatting checks.

## Files Changed

- `raw/papers/src-ckd-128.md`
- `raw/papers/src-hcm-169.md`
- `raw/papers/src-fip-070.md`
- `raw/papers/src-diabetes-035.md`
- `raw/papers/src-obesity-039.md`
- `system/indexes/ckd-source-index.md`
- `system/indexes/source-depth-map.md`

## Verification Command Output

```bash
=== Research Mode Presentation Check ===
PASS CKD
PASS HCM
PASS FIP
PASS diabetes
PASS IBD
PASS obesity
```

## Next Steps

1. Run the local Streamlit application using `./scripts/run_test_page.sh` to preview the updated cards in action under the `USE_RESULT_PRESENTATION_V2=1` rendering path.
2. Pick additional literature cards from the `research-depth-queue.md` for subsequent extraction rounds as needed, using the newly updated `deep_extracted` cards as formatting exemplars.
