---
id: system-ckd-early-detection-frontier-branch-memo-20260417
type: system
topic: ckd
species: feline
disease: CKD
question_type: diagnosis
language: en
last_compiled_at: 2026-04-17
confidence: medium
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
source_ids:
  - src-ckd-018
  - src-ckd-024
  - src-ckd-004
---

# CKD Early-Detection Frontier Branch Memo, 2026-04-17

## Purpose

This memo addresses the P4 densification gap:

> early-detection literature 不再只是 support branch

The existing `early-detection.md` correctly frames serial surveillance as the operational backbone and positions metabolomics/ML work as "frontier augmentation." That framing was right in round 1. It is now understating what src-ckd-018 actually adds.

This memo carves out a distinct **early-detection frontier branch** — a named category with its own evidence base, its own evidence standards, its own use cases, and its own boundaries. It is not folded under serial surveillance. It runs parallel to it.

---

## Why This Branch Earns Its Own Category

Serial surveillance branch and the frontier branch answer DIFFERENT questions.

| | Serial Surveillance Branch | Early-Detection Frontier Branch |
|---|---|---|
| Core question | When should we screen? How often? What to track? | Can we detect CKD before clinical diagnosis is possible? |
| Evidence type | Guidelines, clinical management evidence | Longitudinal metabolomics + ML modeling |
| Output | Operational workflow | Prediction model / biomarker panel |
| Clinical readiness | High — this is what vets do now | Low — research stage, requires assay development |
| What it changes | Timing and frequency of existing clinical workflow | Potentially pre-empts the current clinical trigger entirely |

These are parallel branches. Neither is support for the other.

---

## What the Frontier Branch Contains

### Primary anchor: src-ckd-018

**Study design (important — read before citing):**
- Baseline: 61 healthy cats vs 63 CKD2 cats (cross-sectional separation)
- Longitudinal: 26 cats remaining healthy vs 22 cats developing CKD2 within one year
- Primary outcome: discrimination of future CKD2 diagnosis up to 6 months before traditional diagnosis
- Method: untargeted urine metabolomics; both single-marker and ML panel models tested

**What this study found — stated precisely:**

| Finding | Metric | Claim level |
|---|---|---|
| Best individual metabolite (T-6) | S/U 3-hydroxykynurenine: AUC 0.844, accuracy 0.804 | quoted_fact: src-ckd-018 |
| Best ML panel (T-6) | Linear SVM + metabolites + clinical parameters: AUC 0.929, accuracy 0.862 | quoted_fact: src-ckd-018 |
| SDMA ranking in this dataset | 14th individual metabolite at T-6; poor individual sensitivity | quoted_fact: src-ckd-018 |
| Study population | CKD2 cats only; no GFR; no ultrasound; limited N | quoted_fact: src-ckd-018 |

**Why this is a genuinely distinct branch, not just "a better SDMA paper":**
The study tested whether CKD can be predicted from urine metabolomics before azotemia becomes diagnostic. The answer is: yes, at AUC 0.929 using a panel. That is different in kind from "SDMA is a useful adjunct to creatinine." It is testing a pre-clinical prediction horizon that serial surveillance does not address.

### Supporting context: src-ckd-024, src-ckd-004

These sources establish the contrast — they define what the serial surveillance branch can do, which sharpens what the frontier branch adds beyond it.

- src-ckd-024: SDMA is a useful adjunctive marker, GFR is the reference concept, specificity remains limited
- src-ckd-004: serial creatinine + USG + persistence remains the practical backbone; SDMA supplements rather than replaces

---

## The Frontier Branch Has Its Own Evidence Standards

Because this branch answers a different question, it should be evaluated on different criteria.

**Questions to ask when evaluating frontier branch claims:**

1. **Pre-clinical horizon:** Does the study test prediction before clinical diagnosis, or just at/near diagnosis?
2. **Prospective validation:** Is the longitudinal validation independent from the training set?
3. **Model type:** Single-marker vs. multi-marker panel — the performance difference is large and should be stated
4. **Population scope:** CKD2 only, or does it cover CKD1 and subclinical stages?
5. **Assay practicality:** Is this a routine clinical assay or a research metabolomics platform?
6. **Sample size:** N=22/26 in the longitudinal arm of src-ckd-018 is real but small

**Frontier branch confidence ceiling:**
Even strong performance metrics (AUC 0.929) do not automatically translate to routine clinical readiness. The frontier branch earns high innovation confidence but low deployment confidence until:
- Larger prospective validation exists
- Assay is practical in clinical settings
- True CKD1/subclinical prediction (not just CKD2 six-month foreshadowing) is addressed

---

## How the Two Branches Coexist

They are not competitors. They operate at different time horizons and serve different stakeholders.

```
TIME AXIS ──────────────────────────────────────────────────────▶

Frontier branch:
  [research-stage metabolomics/ML panel]
         │
         ▼ discriminates 6 months before clinical CKD2 diagnosis
         │
         ▼ (pre-clinical research context)
         ╔═══════════════════════════════════════════════╗
         ║  Clinical CKD2 trigger (azotemia + USG)       ║
         ╚═══════════════════════════════════════════════╝
         │
         ▼ (serial surveillance starts here or earlier in high-risk cats)
Serial branch:
  [older/high-risk cats → repeat surveillance → creatinine trend + USG + proteinuria]
         │
         ▼ escalate on persistent abnormalities
```

The frontier branch potentially extends detection into a pre-clinical window the serial branch cannot reach. The serial branch is the operational reality for clinical practice now.

---

## What the Frontier Branch Can Support Right Now

**Supportable conclusions:**
- A pre-clinical metabolomic detection horizon for feline CKD exists in at least one study `[quoted_fact: src-ckd-018]`
- Multi-metabolite ML panels outperform single-marker approaches in early discrimination `[source_supported_conclusion: src-ckd-018]`
- SDMA alone is not the strongest individual metabolite in the current frontier evidence `[quoted_fact: src-ckd-018]`
- The frontier branch represents a different research question than serial surveillance optimization `[source_supported_conclusion: src-ckd-018, src-ckd-024, src-ckd-004]`

**Not supportable yet:**
- That metabolomic early detection is ready for clinical deployment
- That the ML panel generalizes to routine clinical populations
- That this addresses CKD1 or truly pre-GFR-impaired detection (CKD2 is still azotemic)
- That this replaces any current clinical workflow

---

## Minimum Completion Standard: Met

This memo fulfills the P4 requirement for this sub-gap:
- ✓ Early-detection literature now has a named frontier branch
- ✓ The frontier branch has its own evidence standards
- ✓ It is no longer permanently subordinated to serial surveillance
- ✓ What makes it a distinct branch (different question, different horizon) is explicit
- ✓ The limits are as clearly stated as the findings

---

## Best Write-Back Targets

- [early detection](../../topics/ckd/early-detection.md) — add frontier-branch-as-distinct-category framing
- [CKD SDMA frontier memo](ckd-sdma-frontier-memo.md) — cross-reference: frontier branch supersedes SDMA-centered framing of src-ckd-018
- [endpoint handbook](../../topics/ckd/endpoint-handbook.md) — frontier biomarkers now have a clearer tier
- [current state dashboard](../../topics/ckd/current-state-dashboard.md) — update "Early detection" row state
