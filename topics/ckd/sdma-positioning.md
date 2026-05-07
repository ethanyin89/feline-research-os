---
id: topic-ckd-sdma-positioning
type: topic
topic: ckd
species: feline
disease: CKD
question_type: endpoint
source_ids: [src-ckd-002, src-ckd-004, src-ckd-024]
last_compiled_at: 2026-04-09
confidence: medium
owner: codex
status: active
---

# Feline CKD SDMA Positioning

## Question This Page Answers

What can this vault currently say, and not say, about SDMA in feline CKD?

## Current Conclusions

### quoted_fact

- The diagnosis and staging review treats GFR as ideal for detecting early renal dysfunction, but notes practical routine-use limitations.
- The ISFM guideline states that serial annual or bi-annual assessment of serum creatinine or SDMA together with USG may facilitate earlier or more certain diagnosis in older cats.
- The same guideline states that SDMA appears to offer greater sensitivity than creatinine for early CKD detection and does not appear to be affected by muscle mass.
- The guideline also states that SDMA cannot currently be recommended as a single screening test for CKD, but may support diagnosis or staging, especially in cats with marked muscle loss.
- The 2022 biomarker review states that serum creatinine has important limitations for early CKD detection and that SDMA was introduced as a novel GFR biomarker for earlier detection in cats.
- The same review states that SDMA specificity data are still limited.

### source_supported_conclusion

- In the current vault, SDMA belongs in the endpoint map as an adjunctive early-detection and staging aid.
- SDMA should currently sit below the classic practical core of serial creatinine interpretation plus USG, not above it.
- The strongest current use-case for SDMA is reducing over-reliance on a creatinine-only mindset, especially where muscle loss complicates interpretation.
- The current corpus supports SDMA as a support marker, not as a replacement marker.
- The new biomarker review reduces uncertainty about whether SDMA matters at all, but it does not eliminate uncertainty about how heavily it should be weighted in routine workflows.
- The metabolomic-plus-ML paper strengthens SDMA's role as one ingredient in a broader frontier, but weakens any SDMA-alone shortcut story.

### llm_inference

- The current bottleneck is no longer whether SDMA matters at all. It does.
- The real unresolved question is how strongly it should be weighted relative to creatinine trend, USG, and broader serial surveillance logic.

## Evidence Map

- `src-ckd-002`: diagnosis/staging framing, GFR ideal-reference logic
- `src-ckd-004`: strongest current SDMA wording in the vault
- `src-ckd-018`: metabolomic-plus-ML frontier paper that weakens any SDMA-alone shortcut story
- `src-ckd-024`: biomarker-review framing that supports SDMA relevance while preserving caution

## What We Can Say Safely

1. SDMA is relevant to earlier recognition of feline CKD.
2. SDMA is especially useful where creatinine interpretation may be distorted by reduced muscle mass.
3. SDMA should be interpreted inside a serial and multi-marker workflow.
4. SDMA does not justify a one-test screening story.
5. In the current frontier literature, SDMA is better read as one component inside a broader augmentation layer than as the single dominant answer.

## What We Should Not Say Yet

1. SDMA replaces creatinine.
2. SDMA replaces USG.
3. SDMA is already the best single early CKD marker in routine practice.
4. The current vault has enough evidence to rank SDMA definitively against all traditional markers.

## Working Position In V1

| Marker | Current V1 Position | Why |
|---|---|---|
| Creatinine | core operational anchor | serial change remains practical and central in the current corpus |
| USG | core operational anchor | essential context for renal azotemia and CKD confirmation |
| SDMA | adjunctive provisional core | helps with earlier recognition and muscle-mass edge cases, but is not a standalone shortcut |
| GFR | reference-standard concept | ideal in theory, limited in routine working use |

## Operational Rule

If a CKD note, memo, or output mentions SDMA, it should usually also mention at least one of:

- serial creatinine trend
- USG
- older-cat surveillance logic
- muscle-loss context

That keeps SDMA inside the right interpretive frame.

## Current Gaps

- no stable SDMA threshold or ranking logic should be assumed from the current corpus
- no routine-clinic implementation source yet for metabolomic or machine-learning augmentation
- no definitive rank order can yet be claimed across SDMA, creatinine, USG, and frontier panel approaches

## New Best Linked Memo

- [CKD SDMA frontier memo](../../system/indexes/ckd-sdma-frontier-memo.md)

## Recommended Next Sources To Ingest

- feline CKD papers with SDMA-focused diagnostic-performance detail
- studies that compare SDMA with creatinine and USG in earlier CKD detection
- any source clarifying how SDMA should be used in older cats with low muscle mass

## Best Linked Pages

- [endpoint handbook](endpoint-handbook.md)
- [early detection](early-detection.md)
- [synthesis index](synthesis-index.md)
- [SDMA entity card](../../entities/endpoints/sdma.md)
