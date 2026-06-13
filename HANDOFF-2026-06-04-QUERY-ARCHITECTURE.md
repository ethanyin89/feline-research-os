# Handoff: Query Architecture Implementation

**Date:** 2026-06-04
**Branch:** idea-chatacademia-research-workbench
**Status:** Implementation Complete, Public Local-Mode Testing Added

---

## What Was Done

### Goal
Implement the two-tier query architecture for the vault:
1. **Goal 1 (Knowledge queries):** Wikipedia-style plain-language explanations with source citations
2. **Goal 2 (Research queries):** Structured Key-Claim Traceability tables for endpoint/treatment evaluation

### Changes Made

| File | Line(s) | Change |
|------|---------|--------|
| `scripts/app.py` | 1691-1692 | Added `fip_endpoint` and `fip_treatment_evidence` to builders dictionary |
| `scripts/app.py` | 316 | Added "什么是" to explanation markers |
| `scripts/app.py` | 271 | Added "gs-441524", "gs441524", "remdesivir" to FIP disease detection patterns |
| `scripts/public_test_app.py` | public HTTP path | Added `Vault Search (free)` / `OpenRouter (API)` selector and local-mode routing |
| `scripts/local_answer_surfaces.py` | new | Added deterministic no-API public surfaces for FIP recognition, endpoint/treatment evidence pages for CKD/FIP/HCM/IBD/diabetes/FCV, and what-is pages |
| `scripts/check_local_answer_surfaces.py` | new | Added no-server regression checks for deterministic local surfaces |
| `scripts/check_public_test_page.sh` | public checker | Forces `backend=local` and checks recognition + endpoint surfaces through the real HTTP form path |

### New Query Surfaces

| Surface | Trigger Keywords | Content Type |
|---------|------------------|--------------|
| `fip_endpoint` | 评价, 指标, 药效, endpoint, efficacy | Key-Claim Traceability + Endpoint Hierarchy |
| `fip_treatment_evidence` | 治疗证据, 疗效证据, GS-441524, remdesivir | Treatment evidence layers + Key-Claim table |

### Test Results: 15/15 Passed

```
✓ obesity explanation  | 什么是猫肥胖                    → obesity_overview
✓ obesity explanation  | feline obesity explanation → obesity_overview
✓ obesity explanation  | 解释一下猫肥胖                   → obesity_overview
✓ CKD explanation      | 什么是CKD                    → ckd_overview
✓ CKD explanation      | 解释猫慢性肾病                   → ckd_overview
✓ CKD endpoint         | CKD endpoint              → ckd_endpoint
✓ FIP explanation      | 什么是FIP                    → fip_overview
✓ FIP recognition      | FIP怎么识别                   → fip_recognition
✓ FIP endpoint         | FIP药效评价指标                 → fip_endpoint
✓ FIP treatment        | GS-441524疗效证据             → fip_treatment_evidence
✓ FIP treatment        | FIP treatment evidence    → fip_treatment_evidence
✓ HCM explanation      | 什么是HCM                    → hcm_overview
✓ IBD lymphoma         | IBD和淋巴瘤怎么区分               → ibd_lymphoma
✓ diabetes explanation | 什么是糖尿病                    → diabetes_overview
✓ cancer explanation   | 什么是猫癌症                    → cancer_overview
```

### Public HTTP Local-Mode Test Results

```
✓ local surface check  | FIP怎么识别                    → fip_recognition, 3 sources
✓ local surface check  | FIP药效评价指标                 → fip_endpoint, 13 sources
✓ local surface check  | GS-441524疗效证据             → fip_treatment_evidence, 6 sources
✓ local surface check  | 什么是FIP                    → fip_what_is, 3 sources
✓ local surface check  | CKD endpoint                 → ckd_endpoint, 13 sources
✓ local surface check  | CKD治疗证据                    → ckd_treatment_evidence, 12 sources
✓ local surface check  | HCM评价指标                    → hcm_endpoint, 8 sources
✓ local surface check  | IBD endpoint                 → ibd_endpoint, 7 sources
✓ local surface check  | 糖尿病疗效评价指标                → diabetes_endpoint, 11 sources
✓ local surface check  | FCV治疗证据                    → fcv_treatment_evidence, 15 sources
✓ public HTTP checker  | FIP怎么识别                    → local recognition surface
✓ public HTTP checker  | FIP药效评价指标                 → local endpoint surface
```

---

## How to Test

### Local Testing

1. Start the Streamlit app:
   ```bash
   source .venv/bin/activate
   python -m streamlit run scripts/app.py --server.port 8501
   ```

2. Open http://localhost:8501

3. **Select "Vault Search (free)"** in the sidebar dropdown

4. Test queries:
   - `什么是猫肥胖` → Plain-language obesity explanation
   - `FIP药效评价指标` → Key-Claim Traceability + Endpoint Hierarchy
   - `GS-441524疗效证据` → Treatment evidence with Key-Claim table
   - `什么是FIP` → Plain-language FIP explanation

### Public HTTP Testing

```bash
python3 scripts/check_local_answer_surfaces.py

python3 scripts/public_test_app.py --host 127.0.0.1 --port 8510
bash scripts/check_public_test_page.sh http://127.0.0.1:8510
```

The public HTTP app now defaults to `Vault Search (free)` and does not call OpenRouter unless `OpenRouter (API)` is explicitly selected.

### What to Verify

- [ ] Obesity explanation returns plain-language content, not jargon
- [ ] FIP endpoint query returns structured Key-Claim table with evidence levels (B/C)
- [ ] FIP treatment query returns treatment layers with source citations
- [ ] All answers include `[source_supported_conclusion: src-xxx]` tags
- [ ] Verification paths point to source cards and topic pages

---

## Architecture Summary

### Query Flow (Local/Free Mode)

```
User Query
    ↓
infer_local_disease() → Detect disease from keywords
    ↓
is_local_explanation_question() → Check if "什么是", "解释", "explain" etc.
    ↓
choose_local_explanation_surface() → Route to specific surface
    ↓
build_local_explanation() → Call the builder function
    ↓
Return structured answer with source tags
```

### Evidence Levels

| Tag | Meaning |
|-----|---------|
| `[quoted_fact: src-xxx]` | Direct quote from source |
| `[source_supported_conclusion: src-xxx]` | Conclusion supported by sources |
| `[llm_inference]` | LLM reasoning beyond source support |

### Key-Claim Traceability (Research Queries)

| Column | Purpose |
|--------|---------|
| ID | Claim identifier (FE1, FT1, etc.) |
| Claim | The specific claim being made |
| Level | Evidence strength (A=strong, B=moderate, C=weak) |
| Sources | Source card IDs supporting the claim |
| Boundary | What the claim does NOT cover |

---

## Files Reference

### Builder Functions (app.py)

| Function | Line | Purpose |
|----------|------|---------|
| `build_obesity_local_explanation` | 1330 | Plain-language obesity explanation |
| `build_fip_endpoint_explanation` | 618 | FIP endpoint hierarchy + Key-Claim table |
| `build_fip_treatment_evidence_explanation` | 716 | FIP treatment evidence layers |
| `build_fip_local_explanation` | 379 | Plain-language FIP explanation |
| `build_ckd_local_explanation` | 458 | Plain-language CKD explanation |

### Topic Pages (what-is-*.md)

| File | Content |
|------|---------|
| `topics/obesity/what-is-obesity.md` | Bilingual obesity explanation |
| `topics/ckd/what-is-ckd.md` | Bilingual CKD explanation |
| `topics/fip/what-is-fip.md` | FIP explanation |
| `topics/cancer/what-is-cancer.md` | Cancer explanation |

### Plan Document

`PLAN-query-architecture.md` — Original plan with Karpathy Wiki LLM concept

---

## Known Limitations

1. **API mode** uses different path (`run_query_core`) that doesn't use these builders
2. **Public test app** local mode now uses deterministic surfaces for FIP recognition, CKD/FIP/HCM/IBD/diabetes/FCV endpoint and treatment-evidence pages, and what-is pages, then falls back to generic local retrieval
3. Some diseases don't have endpoint/treatment builders yet in the Streamlit app path (public helper exposes broader compiled topic-page surfaces)

---

## Next Steps (Optional)

1. Add endpoint builders for other diseases (HCM, IBD, diabetes)
2. Add treatment evidence builders for other diseases
3. Extend `scripts/local_answer_surfaces.py` to cancer/obesity endpoint-like branch pages if public testing needs those research paths
4. Add more "什么是" aliases if detection gaps found

---

## Session Commands

```bash
# Start app
source .venv/bin/activate
python -m streamlit run scripts/app.py --server.port 8501

# Run routing tests
.venv/bin/python -c "
import sys; sys.path.insert(0, 'scripts')
from app import infer_local_disease, choose_local_explanation_surface
print(choose_local_explanation_surface('什么是猫肥胖', infer_local_disease('什么是猫肥胖')))
"

# Check syntax
python3 -m py_compile scripts/app.py && echo "Syntax OK"

# Check public local surfaces without API calls
python3 -m py_compile scripts/public_test_app.py scripts/local_answer_surfaces.py scripts/check_local_answer_surfaces.py
python3 scripts/check_local_answer_surfaces.py
```

---

## One-Line Summary

Query architecture now routes "什么是X" to plain-language explanations and "X药效评价/疗效证据" to structured Key-Claim Traceability tables, with all answers including source citations and verification paths.
