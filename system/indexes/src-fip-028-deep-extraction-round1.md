---
id: src-fip-028-deep-extraction-round1
type: deep-extraction-worksheet
source_id: src-fip-028
round: 1
last_compiled_at: 2026-06-08
verification_status: compiled
decision_grade: no
language_qa_status: not_applicable
owner: codex
status: active
---

# Deep Extraction: src-fip-028 (GS-441524 vs Molnupiravir Comparison)

## Phase 0: Micro-Analysis Units

### Study Metadata

| Field | Value |
|-------|-------|
| Title | GS-441524 and molnupiravir are similarly effective for the treatment of cats with feline infectious peritonitis |
| Journal | Frontiers in Veterinary Science |
| Year | 2024 |
| DOI | 10.3389/fvets.2024.1422408 |
| Study Type | Prospective comparative cohort |
| Sample Size | 118 cats (59 per group) |

### Hard Numbers

| Metric | GS-441524 | Molnupiravir | P-value |
|--------|-----------|--------------|---------|
| Total cats | 59 | 59 | — |
| Deaths | 12 (20.3%) | 8 (13.6%) | 0.326 |
| Completed treatment | 48 | 52 | — |
| Achieved remission | 48/48 (100%) | 51/52 (98%) | — |
| Effusive FIP (total) | ~38 | ~38 | — |

### Dosing Details

| Drug | Dose Range | Standard Duration |
|------|------------|-------------------|
| GS-441524 (Mutian® Xraphconn) | 12.5–25 mg/kg/day | 84 days |
| Molnupiravir (compounded) | 20–40 mg/kg/day | 84 days |

Dose adjustment: Lower doses for effusive FIP, higher doses for neurological/ocular involvement.

### Timeline

- Most deaths: Within first 10 days
- Lab normalization: 6-7 weeks
- Treatment duration: 84 days (both drugs)

## Phase 1: Key Themes

### Theme 1: Equivalent Efficacy
Both antivirals achieve near-identical outcomes. The mortality difference (20.3% vs 13.6%) is not statistically significant (p = 0.326).

### Theme 2: Early Mortality Window
Deaths cluster in first 10 days, suggesting severe disease at presentation rather than treatment failure.

### Theme 3: Dose-Response by Presentation
Both drugs use lower doses for effusive FIP, higher for neuro/ocular. This reflects the blood-brain barrier challenge.

### Theme 4: Safety Profile
Adverse events similar: transient hepatic enzyme elevation, self-resolving.

## Phase 2: Claim-Evidence Pairs

| Claim | Evidence | Strength |
|-------|----------|----------|
| Molnupiravir equivalent to GS-441524 | 118-cat comparative cohort, p=0.326 | Strong |
| Both achieve ~99% remission in completers | 48/48 vs 51/52 | Strong |
| 84-day protocol standard | Both groups used 84-day duration | Descriptive |
| Early deaths reflect disease severity | Deaths within 10 days | Inferential |
| Neuro/ocular cases need higher doses | Dose adjustment protocol | Descriptive |

## Phase 3: Promotion Boundaries

### Safe to Promote

- Molnupiravir as equivalent alternative to GS-441524
- 84-day treatment duration for both drugs
- Near-complete remission rates
- Similar safety profiles

### Not Safe to Promote

- Specific dose recommendations (individualized to presentation)
- Long-term relapse rates (not studied beyond remission)
- Cost-effectiveness claims
- Preference ranking between drugs

### Design Limitations

- Not randomized (matched groups but potential selection bias)
- Single-center study
- Compounded molnupiravir (not commercial formulation)
- No long-term follow-up data

## Phase 4: Integration Notes

### Module Impact

This source strengthens the FIP treatment branch by validating molnupiravir as an equivalent alternative. The existing GS-441524 evidence base (src-fip-016, src-fip-017, src-fip-013) remains valid; molnupiravir joins as co-equal option.

### Update Candidates

- `topics/fip/index.md` — add molnupiravir as equivalent treatment option
- FIP treatment guidance — note both drugs are viable first-line
- `what-is-fip.md` — mention treatment options include both antivirals

### Cross-References

- src-fip-026: Molnupiravir case series (18 cats) — complementary evidence
- src-fip-027: Molnupiravir clinical trial (10 cats, effusive) — complementary
- src-fip-016: GS-441524 efficacy/safety — original GS-441524 evidence
- src-fip-017: GS-441524 in vitro/in vivo — mechanism support
