---
id: expert-answer-review-prototype-20260514
type: system
topic: operating-system
question_type: workflow-prototype
language: bilingual
last_compiled_at: 2026-05-14
verification_status: prototype
decision_grade: no
language_qa_status: light_checked
owner: codex
status: active
---

# Expert Answer Review Prototype, 2026-05-14

## Classification

按 `/autoplan`，这件事属于：

`方案 + 内容处理`

不是想法、检查、排查。

原因：用户给的不是一个单点事实，而是一条可重复操作思路：

`Ask the vault answer -> field expert review -> structured correction -> write-back decision`

## Current Prototype State

**Minimum sample threshold reached.** Ready for codification.

Current status:

- sample target: `3-10` real Ask the vault answers
- completed manual samples: `3` ✓
- finalized skill file: `ready to create`
- cron needed: `no` (judgment-heavy)
- user-facing prompt surface: `yes, Ask the vault renders an Expert review loop under each answer`

## Codification Decision (2026-05-17)

All 5 acceptance criteria met:
1. ✓ Reviews produce more than style feedback
2. ✓ Findings map to stable system homes
3. ✓ Comments convert to claim-level actions
4. ✓ Actions don't treat expert chat as evidence
5. ✓ Future answers improve from changes

**Codify as:** workflow (execution order is the main value)

Primary patterns discovered:
- `wording downgrade` — answer stronger than source support
- `endpoint hierarchy` — distinct outcomes collapsed
- `source gap` — needs evidence not in vault
- `routing miss` — loaded wrong sources

Cron is not appropriate because expert answer review is judgment-heavy. Mechanical follow-ups can later become health checks, but expert selection, claim downgrading, and write-back decisions should not run automatically.

## Samples

| # | Question Area | Answer File | Expert Lens | Review File | Result |
|---|---|---|---|---|---|
| 1 | feline diabetes endpoint comparison | `/Users/jiawei/Downloads/feline-diabetes-ask-the-vault-answer.md` | Jacquie Rand, feline diabetes clinical research and remission/endpoints | `/Users/jiawei/Desktop/问与答.md` | useful; exposed endpoint-layer compression errors |
| 2 | CKD phosphorus control evidence | `inbox/ckd/2026-05-17-treatment-ckd.md` | Jonathan Elliott, feline nephrology, ISFM CKD guidelines | in-session | useful; exposed endpoint hierarchy gaps and source verification needs |
| 3 | FIP GS-441524 treatment protocol | `inbox/fip/2026-05-17-treatment-fipgs441524.md` | Niels Pedersen, FIP treatment research pioneer | in-session | useful; exposed wording downgrade and routing gaps |

**Sample 1** produced one durable signal:
`expert review is most useful when it converts answer wording into a claim hierarchy and write-back decision, not when it simply rewrites the answer`

**Sample 2** confirmed: `endpoint hierarchy` issues (phosphate binder stratification) and `source verification` needs (survival numbers)

**Sample 3** confirmed: `wording downgrade` pattern (dose escalation caveats) and `routing miss` (incomplete source loading)

## Why This Matters

The original answer was directionally useful, but compressed several endpoint families too flatly.

The expert review forced the system to separate:

- ordinary glycemic control
- remission as a conditional high-value endpoint
- insulin independence versus true remission
- SGLT2 drug-control state versus remission
- neuropathy as a complication endpoint, not a universal primary endpoint
- obesity/body-condition as background, mechanism, and endpoint, not a loose prevalence slogan
- cat clinical endpoints versus rodent/primate model endpoints

This is exactly the kind of content pressure that should feed the vault.

## Prototype Workflow

Use this manually for the next `2-9` samples.

### Step 1: Save Inputs

Record:

- original question
- Ask the vault answer
- loaded source IDs if available
- expert-selection prompt and chosen expert
- expert review output

Do not treat the external expert response as source evidence.

### Step 2: Classify The Review

Assign one primary review type:

| Review Type | Meaning | Typical Action |
|---|---|---|
| `wording downgrade` | answer wording is stronger than source support | revise answer prompt, topic wording, or traceability |
| `endpoint hierarchy` | answer collapses distinct outcomes | update endpoint/treatment owner |
| `source gap` | reviewer needs evidence not present in vault | queue source/full-text work |
| `routing miss` | Ask the vault loaded the wrong surface | update routing tests or answer surfaces |
| `scenario specificity` | answer failed to ask what kind of project/use case | add scenario-aware prompt or topic structure |
| `promotion candidate` | review produces durable branch clarity | stage content precision promotion |

### Step 3: Map Findings To System Homes

Every finding must land in one of these homes:

| Finding Destination | Use When |
|---|---|
| `chat-only` | useful rewrite, no durable structure |
| `inbox/` staged audit | likely reusable, needs review |
| `topic page` | canonical wording is too strong or too flat |
| `memo / narrow owner` | a branch boundary needs a control layer |
| `source/deep extraction queue` | full text or source card depth is the blocker |
| `query test` | same bad answer could recur from routing/prompt behavior |
| `health check` | drift is mechanically detectable |

### Step 4: Decide Movement

Use the same promotion states as content precision:

- `promote`
- `partial-promote`
- `hold`
- `needs source access`

Default is `hold` unless the correction is conservative, source-anchored, and structurally clarifying.

### Step 5: Record The Sample

Write one staged note in `inbox/<disease>/` with:

- original answer summary
- expert lens
- findings table
- system action table
- what not to say
- whether the pattern is stable enough to codify

## Acceptance Criteria Before Codification

Do not create a final `expert-answer-review-workflow` or skill until at least `3` samples pass this test:

1. expert review produces more than style feedback
2. at least one finding maps to a stable system home
3. reviewer comments can be converted into claim-level actions
4. action does not require treating the expert chat as primary evidence
5. a future Ask the vault answer would improve because of the change

At `3-10` successful samples, codify as one durable owner:

- workflow if the main value is execution order
- prompt if the main value is how to ask the expert reviewer
- query test if the failure is answer/routing recurrence
- health check if the failure can be detected mechanically

## Current Decision

Sample 1 supports:

- create a staged diabetes review note
- make one conservative endpoint wording downgrade
- expose the review loop in the Ask the vault UI as a manual prompt download
- continue manual sampling before writing a final skill

It does not yet support:

- automatic expert review
- cron
- treating Jacquie Rand persona output as evidence
- broad prompt rewrite across all diseases

## User-Facing Surface

The Streamlit app now exposes this as a manual loop after each answer:

`Expert review loop -> Download review prompt`

The generated prompt includes:

- the original question
- the Ask the vault answer
- disease / question type / confidence metadata
- cited source IDs
- the reviewer-selection prompt
- strict review instructions that force claim-level action

This surface is allowed before final codification because it does not automate judgment.
It only makes the current standard process visible and repeatable for users.

## Related Pages

- [query to write-back](query-to-writeback.md)
- [write-back promotion checklist](writeback-promotion-checklist.md)
- [claim audit protocol](claim-audit-protocol.md)
- [content precision promotion workflow](content-precision-promotion-workflow.md)
- [durable agent codification protocol](durable-agent-codification-protocol.md)
