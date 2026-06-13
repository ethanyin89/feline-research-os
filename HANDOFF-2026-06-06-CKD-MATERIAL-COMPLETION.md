# Handoff: CKD Material Completion

**Date:** 2026-06-06
**Status:** CKD extension abstract processing complete; four selective full-text extensions deep-extracted

## Completed

- Replaced heuristic PubMed text parsing with XML extraction in `scripts/source_metadata_check.py`.
- Added PubMed fallback by DOI and direct PMID-only support.
- Added metadata-provider provenance to source-check reports and structured abstract worksheets.
- Processed the seven remaining title-only CKD extension cards.
- Upgraded six cards to `abstract_weighted`: `src-ckd-027`, `029`, `039`, `044`, `047`, and `049`.
- Created six round-1 structured abstract worksheets and two batch indexes.
- Deep-extracted `src-ckd-027` from complete PMC article text.
- Deep-extracted `src-ckd-029` from a complete eight-page article PDF.
- Deep-extracted `src-ckd-030` from complete MDPI publisher HTML.
- Deep-extracted `src-ckd-050` from complete PMC/BMC full text.
- Updated the TGF-beta entity, mechanism handbook, and model map with bounded direct feline in-vitro evidence.
- Reviewed `src-ckd-036` and held it for a paired senescence synthesis because it substantially overlaps the existing `src-ckd-023` anchor.
- Created `system/indexes/ckd-uremic-toxin-microbiome-bridge-memo-20260606.md` to separate disease association from unproven probiotic efficacy.

## Current CKD State

- 50 source cards total
- 28 `deep_extracted`
- 2 `source_checked`
- 19 `abstract_weighted`
- 1 `title_only`

The sole title-only extension card is `src-ckd-032`. PMID `24783628` resolves to the JAVMA record, but PubMed provides no abstract and no DOI was recovered. Keep it blocked until full text or another legitimate abstract source is available.

## New Owners

- `system/indexes/feline-ckd-extension-pubmed-fallback-20260606.md`
- `system/indexes/feline-ckd-extension-structured-abstract-pubmed-20260606.md`
- `system/indexes/ckd-source-index.md`
- `system/indexes/source-depth-map.md`

## Next Content Priority

Do not repeat metadata or abstract-availability checks across the CKD extension. Select full-text/deep-extraction candidates by branch value. The strongest new candidates are:

1. `src-ckd-047` for progressive CKD pathogenesis architecture, after the open repository manuscript becomes directly accessible.
2. `src-ckd-049` for feeding-tube management boundaries, after full text becomes accessible.
3. Use the completed uremic-toxin/microbiome memo as a research boundary, not treatment guidance.
4. Compare `src-ckd-029` against stronger independent phosphate-binder evidence before any treatment write-back.
5. Any probiotic continuation requires a controlled feline trial; do not broaden from `src-ckd-030`.
6. For TGF-beta, prioritize CKD-derived or in-vivo feline validation rather than another general fibrosis review.

The mechanism and model pages now include the bounded `src-ckd-050` in-vitro claim. No clinical treatment claim was promoted.
