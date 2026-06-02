# Handoff: Ordinary-User Answer Quality Gate — 2026-06-02

## Classification

This was **check + investigation**, not a new feature expansion.

The user compared three answer modes:

1. `Vault Search (free)`
2. API synthesis inside Ask the vault
3. Wikipedia / 維基百科

The important clarification was: **the user cares about answer quality**. Route correctness, zero API calls, and source count are necessary, but they are not enough. An ordinary user asking `解释CKD` expects a compact, useful explanation, not merely a local hit list or a thin citation bundle.

## Finding

The previous fix made API synthesis load a minimum source-card baseline, but the free-mode recurring eval still mostly checked mechanics:

- disease detection
- answer mode
- surface selection
- source count
- no API call
- not hit-list-only

That did not guarantee the answer felt good compared with a normal reference page. For a broad CKD prompt, a good ordinary-user answer needs at least:

- plain-language definition
- how CKD is recognized
- what indicators are monitored
- treatment/management reality
- overclaim boundaries
- next reading path
- a clear value proposition versus Wikipedia

## Fix

Changed:

- `scripts/app.py`
  - Expanded the deterministic CKD overview answer in both Chinese and English.
  - Added sections for recognition/diagnosis, monitoring, treatment reality, and Wikipedia comparison.
  - Follow-up: added researcher-overview handling for phrases like `current understanding of feline CKD` and `what should a researcher know about feline CKD`, plus a `Researcher Lens` section that separates disease model, markers, endpoints, and evidence strength.
  - Follow-up: manually probed nine researcher-style prompts across CKD, HCM, FIP, and IBD. HCM and IBD routed correctly; FIP broad researcher prompts fell back to local retrieval. Added `fip_overview` with risk/recognition/form/diagnostic/treatment-actionability layers.
  - Follow-up: HCM and IBD routed correctly but were thinner than CKD/FIP for researcher use. Added `Researcher Lens` sections to HCM and IBD answers so researcher prompts get disease-model and evidence-layer framing, not only the ordinary overview.
  - Follow-up: manually probed diabetes, FCV, obesity, and cancer researcher prompts. All four fell back to local retrieval. Added bounded overview surfaces: `diabetes_overview`, `fcv_overview`, `obesity_overview`, and `cancer_overview`. Obesity and cancer surfaces carry explicit evidence-depth/architecture caveats to avoid fake certainty.
  - Follow-up: added a source-trace trust gate. Manual probe found CKD overview cited `src-ckd-002`, `src-ckd-006`, `src-ckd-007` without loading them, and IBD cited `src-ibd-014`, `src-ibd-021` without loading them. Builder source lists were corrected.
  - Kept the no-API disclosure and source-tag discipline.

- `scripts/ordinary_user_vault_eval.py`
  - Added `quality_groups` to all six recurring ordinary-user samples.
  - Added `has_quality_groups(...)`.
  - The eval now fails if expected ordinary-user concepts are missing, not only if routing is wrong.
  - Follow-up: added researcher-style CKD overview samples after manually probing eight phrasings.
  - Follow-up: added three FIP researcher overview samples after the cross-disease probe found FIP-specific failures.
  - Follow-up: added four HCM/IBD researcher quality samples to keep the researcher lens recurring.
  - Follow-up: added eight diabetes/FCV/obesity/cancer researcher samples. The recurring eval now covers 24 ordinary-user/researcher prompts.
  - Follow-up: `ordinary_user_vault_eval.py` now fails if any cited source ID is nonexistent, absent from `loaded_source_ids`, or missing entirely on a `local_explanation` surface.

This turns the screenshot lesson into a recurring gate instead of a one-off manual judgment.

## Verification

Ran:

```bash
python3 -m py_compile scripts/app.py scripts/ordinary_user_vault_eval.py
.venv/bin/python scripts/ordinary_user_vault_eval.py
python3 scripts/test_query.py
python3 scripts/health.py
```

Results:

- ordinary-user eval: 6/6 PASS, all `api_calls=0`
- query tests: 108 passed / 0 failed
- health: PASS for `Ordinary-user vault eval`
- health still reports the known thin-source warning unrelated to this patch

## Product Interpretation

The vault should not try to beat Wikipedia by being longer or pretending to be a public encyclopedia. Its value should be:

- source-backed claims
- explicit inference labels
- uncertainty boundaries
- next reading path
- free local mode for “what do we already have?”
- API mode only when synthesis across evidence is worth paying for

For broad ordinary-user questions, local free mode must be good enough that the user understands why this is not just a weaker Google/Wikipedia answer.

## Dirty Worktree Boundary

Only these files belong to this task:

- `scripts/app.py`
- `scripts/ordinary_user_vault_eval.py`
- `HANDOFF.md`
- `HANDOFF-2026-06-02-ANSWER-QUALITY-GATE.md`

Do not include unrelated cancer/material intake files, generated health reports, or pre-existing public-test artifacts in this thread.
