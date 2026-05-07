# Health Check Report

Date: 2026-04-08  
Scope: `feline-research-os/` round 2 CKD vault consistency check

## Structural Checks

### Passed

- CKD topic layer now includes dedicated pages for early detection, risk recognition, hypertension/comorbidity, and pathology correlations
- endpoint entity coverage is substantially denser than round 1
- symptom entity coverage now exists for `polyuria` and `polydipsia`

### Findings

1. `entities/regulations/china-veterinary-registration.md` and `entities/regulations/fda-cvm.md` were still seed-only cards before this round.
Severity: low  
Status: fixed in this round

2. `entities/mechanisms/ugt1a6.md` still carried a misleading `seed` state even though the plan already downgraded it to provisional.
Severity: medium  
Status: fixed in this round

## Consistency Checks

### Passed

- `navigation.md`, `synthesis-index.md`, and the Chinese briefing now reflect the newer early-detection and recognition pages
- symptom entities are now linked back into the CKD recognition page

### Findings

3. `out-ckd-dossier-20260408-v1-working-en.md` still described early-detection content as a future subpage.
Severity: medium  
Status: fixed in this round

4. `out-ckd-briefing-20260408-round1-en.md` still contained an outdated future write-back target.
Severity: low  
Status: fixed in this round

5. `topics/ckd/mechanism-overview.md` still referred to missing TGF-beta/PTH cards even after entity-layer progress.
Severity: low  
Status: fixed in this round

## Residual Open Issues

6. `topics/ckd/model-summary.md` still says there is no dedicated natural-history page.
Severity: low  
Impact: the model layer remains the thinnest part of the vault  
Status: open

7. Several source cards are still abstract-weighted and not yet full-text extracted.
Severity: medium  
Impact: topic confidence can still outrun evidence density if left unchecked  
Status: open

8. Regulatory entity coverage is now active, but still route-level rather than product-specific.
Severity: medium  
Impact: not enough yet for product-specific registration recommendations  
Status: open

## Recommended Fix Order

1. deepen the model layer, likely via a natural-history or model-taxonomy page
2. continue full-text extraction on highest-reused source cards
3. build product-specific regulatory decision notes only after more evidence-package detail is ingested

## Overall Status

Round 2 vault consistency is better than round 1.

The main risk has shifted again:
it is no longer stale structure, but uneven evidence density across layers, especially the model layer and source-depth layer.
