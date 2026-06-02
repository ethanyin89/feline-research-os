# Handoff

If you are a new model taking over this repo because of token loss, model switch, or usage limit, do this first.

## Latest Session Handoff

Read the latest session handoff first:

- [HANDOFF-2026-06-02-CKD-ANSWER-MODE-COMPARISON.md](HANDOFF-2026-06-02-CKD-ANSWER-MODE-COMPARISON.md)

For the prior cancer abstract extraction sample handoff, read:

- [HANDOFF-2026-06-02-CANCER-ABSTRACT-SAMPLE.md](HANDOFF-2026-06-02-CANCER-ABSTRACT-SAMPLE.md)

For the prior Streamlit/API-cost guard handoff, read:

- [HANDOFF-2026-06-01-STREAMLIT-API-COST-GUARD.md](HANDOFF-2026-06-01-STREAMLIT-API-COST-GUARD.md)

For the prior public-test link refresh handoff, read:

- [HANDOFF-2026-05-25-PUBLIC-TEST-LINK-REFRESH.md](HANDOFF-2026-05-25-PUBLIC-TEST-LINK-REFRESH.md)

For the prior ordinary-user HTTP public test handoff, read:

- [HANDOFF-2026-05-22-ORDINARY-USER-HTTP-PUBLIC-TEST.md](HANDOFF-2026-05-22-ORDINARY-USER-HTTP-PUBLIC-TEST.md)

For the prior Streamlit public-tunnel investigation, read:

- [HANDOFF-2026-05-21-ORDINARY-USER-PUBLIC-TEST.md](HANDOFF-2026-05-21-ORDINARY-USER-PUBLIC-TEST.md)

For the prior public-test recovery step, read:

- [HANDOFF-2026-05-20-ORDINARY-USER-PUBLIC-TEST.md](HANDOFF-2026-05-20-ORDINARY-USER-PUBLIC-TEST.md)

For the prior Karpathy gap-analysis / ordinary-user prep session, read:

- [HANDOFF-2026-05-17-KARPATHY-GAP-ANALYSIS.md](HANDOFF-2026-05-17-KARPATHY-GAP-ANALYSIS.md)

For the prior obesity Tier 1 completion, read:

- [HANDOFF-2026-05-17-OBESITY-TIER1-COMPLETE.md](HANDOFF-2026-05-17-OBESITY-TIER1-COMPLETE.md)

For the prior autoplan gap analysis, read:

- [HANDOFF-2026-05-17-AUTOPLAN-KARPATHY-GAP.md](HANDOFF-2026-05-17-AUTOPLAN-KARPATHY-GAP.md)

For the prior expert-review / obesity-gate handoff, read:

- [HANDOFF-2026-05-16-EXPERT-REVIEW-OBESITY-GATE.md](HANDOFF-2026-05-16-EXPERT-REVIEW-OBESITY-GATE.md)

For the prior expert-review / source-depth handoff, read:

- [HANDOFF-2026-05-15-EXPERT-REVIEW-SOURCE-DEPTH.md](HANDOFF-2026-05-15-EXPERT-REVIEW-SOURCE-DEPTH.md)

For the previous ordinary-user presentation handoff, read:

- [HANDOFF-2026-05-07-CONTENT-PRESENTATION.md](HANDOFF-2026-05-07-CONTENT-PRESENTATION.md)

For the longer session log behind it, read:

- [HANDOFF-2026-05-06-SESSION-2.md](HANDOFF-2026-05-06-SESSION-2.md)

## Task Type

This is a `plan`, not a narrow blocker check.

The current repo-level job is no longer "continue only the CKD image gate".
The current job is to hold two tracks at once:

1. `325-source content pipeline` (7 disease modules)
2. `ordinary-user usage surface`

## Read These 4 Files

1. [Two-track operating plan, 2026-04-18](system/indexes/two-track-operating-plan-20260418.md)
2. [Karpathy alignment handoff, 2026-04-18](system/indexes/karpathy-alignment-handoff-20260418.md)
3. [UX improvement handoff, 2026-04-18](system/indexes/ux-improvement-handoff-20260418.md)
4. [Content vs frontend collaboration plan](system/indexes/content-vs-frontend-collaboration-plan.md)

If you are continuing the content line specifically, also read:

5. [Content-side densification queue](system/indexes/content-side-densification-queue.md)
6. [120 source processing ledger, 2026-04-21](system/indexes/source-processing-ledger-120-20260421.md)
7. [Legacy 96 source processing ledger, 2026-04-21](system/indexes/legacy-96-source-processing-ledger-20260421.md)
8. [Cross-disease source depth map](system/indexes/source-depth-map.md)

If you are continuing the ordinary-user line specifically, also read:

9. [Ordinary-user LLM wiki usability audit, 2026-04-10](system/indexes/ordinary-user-llm-wiki-usability-audit-20260410.md)

## 30-Second Reality (Updated 2026-05-17)

- The repo has `325` paper source cards across 7 disease modules: CKD, FIP, HCM, IBD, Diabetes, FCV, and Obesity.
- **Year metadata coverage**: 325/325 (100%) — all cards have year field.
- **CKD/FIP/HCM/IBD/FCV**: 24/24 cards each, all `deep_extracted` and `full`.
- **Diabetes**: 118 cards (24 seed + 94 extension), seed corpus is `full`, extension is `partial`.
- **Obesity**: 87 cards, 4 deep-extracted (Tier 1 complete), 4 architecture pages + 4 bilingual versions.
- Content work now has a fixed Karpathy-style workflow and should not require reconfirmation on every repeated step.
- The ordinary-user surface in `scripts/app.py` is already materially better, but the remaining gap is still "ask-native product feel", not raw frontend absence.
- Health check: 107 tests passing, all checks PASS.

## Verify In 4 Commands

```bash
python3 scripts/test_query.py
python3 -m py_compile scripts/app.py scripts/search.py scripts/query.py
find raw/images -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) | sort
python3 - <<'PY'
from pathlib import Path
import re
root = Path('raw/papers')
for disease in ['ckd', 'fip', 'hcm', 'ibd', 'diabetes', 'fcv', 'obesity']:
    cards = sorted(root.glob(f'src-{disease}-*.md'))
    statuses = {}
    for p in cards:
        text = p.read_text(encoding='utf-8')
        m = re.search(r'^status:\s*(.+)$', text, re.M)
        s = m.group(1).strip() if m else 'missing'
        statuses[s] = statuses.get(s, 0) + 1
    print(disease.upper(), len(cards), statuses)
PY
```

## Default Owner Split

- content side owns truth, evidence, write-back, queue reality, and system state
- frontend side owns presentation, interaction, and ordinary-user polish

Do not silently let frontend edits rewrite truth claims.
Do not let content work drift back into presentation-only cleanup unless the user asks.

## Default Next Move

If no one has given a narrower instruction, the safest default is:

1. continue the content line
2. continue only full-text / official-source / image-table / output-specific precision; do not reopen generic source-card thickening for any of the seven disease modules
3. stage write-back through `inbox/`
4. refresh broader system owners like `source-depth-map` only after this batch is coherent

## Do Not Regress To

- "continue only the CKD image gate"
- treating presentation polish as the content-side default
- re-opening architecture decisions that are already locked
- re-asking the user for confirmation on repeated source-card processing steps

## One Line

Do not continue "the old blocker".
Continue `the two-track repo plan`.
