# Handoff

If you are a new model taking over this repo because of token loss, model switch, or usage limit, do this first.

## Latest Session Handoff

Read the latest session handoff first:

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

1. `120-source content pipeline`
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

## 30-Second Reality

- The repo has `120` paper source cards total as of the 2026-04-21 reality check: CKD / FIP / HCM / IBD / Diabetes each have `24/24` cards and `24/24` round-1 deep-extraction worksheets.
- Content work now has a fixed Karpathy-style workflow and should not require reconfirmation on every repeated step.
- CKD is already the mature template.
- FIP source cards are no longer the main extraction backlog: `24/24` round-1 worksheets already exist and `24/24` cards are now explicit `full`.
- IBD source cards are also no longer a real extraction backlog: `24/24` round-1 worksheets exist and `24/24` cards are now explicit `full`.
- FIP / IBD dashboard, synthesis, and unresolved trackers have now had a first state-sync pass from those worksheets.
- HCM is also clean at the source-card level: `24/24` cards are `extracted`, and `24/24` are now explicit `full` after the 2026-04-22 remaining-partial promotion pass.
- The user-facing legacy `96` scope means CKD / FIP / HCM / IBD. That scope is processed at source-card + worksheet level and is now `96/96` explicit full at source-card depth.
- Diabetes is now present as a fifth source-card module: `24/24` cards are `extracted`, `24/24` are explicit `full`, narrow owner memos exist, U.S. SGLT2 regulatory/label controls exist, and the first briefing/dossier/slides output set now exists across `working-en / en / zh`.
- The ordinary-user surface in `scripts/app.py` is already materially better, but the remaining gap is still "ask-native product feel", not raw frontend absence.
- The current shell still does not have `ANTHROPIC_API_KEY`, and live Streamlit smoke test still needs a shell with `streamlit` installed.

## Verify In 4 Commands

```bash
python3 scripts/test_query.py
python3 -m py_compile scripts/app.py scripts/search.py scripts/query.py
find raw/images -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) | sort
python3 - <<'PY'
from pathlib import Path
import re
root = Path('raw/papers')
for disease in ['ckd', 'fip', 'hcm', 'ibd', 'diabetes']:
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
2. continue only full-text / official-source / image-table / output-specific precision; do not reopen generic source-card thickening for any of the five disease modules
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
