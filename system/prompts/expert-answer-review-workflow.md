---
id: expert-answer-review-workflow
type: workflow
topic: operating-system
status: active
verified_samples: 3
last_updated: 2026-05-17
---

# Expert Answer Review Workflow

## When To Use

After receiving an Ask the Vault answer that:
- Will be used for decision-making
- Will be written back to the vault
- Has medium or low confidence
- Covers treatment, endpoints, or regulatory topics

## Prerequisites

- Original question
- Ask the Vault answer with provenance tags
- Source IDs cited
- Disease and question type metadata

## Workflow

### Step 1: Select Expert

Choose a domain expert for the specific field and scene. Criteria:
- Top-tier in the exact subspecialty
- Can be living or historical
- Must have published or practiced in the specific area
- If uncertain, ask 2 clarifying questions first

**Prompt template:**
```
我想探讨【{disease}】里的【{question_type}】。先别回答。请你先选一位最适合的领域顶尖名人专家来思考它。

输出：
1. 你选谁，他对应的细分领域
2. 为啥选他，三句话
```

### Step 2: Request Strict Review

From the selected expert's perspective, evaluate:

1. Which statements should be downgraded
2. Which endpoints, scenarios, or subjects are conflated
3. Which claims need source card or original text verification
4. Which content should remain as inference only
5. If writing back, what's the minimum target layer (topic, memo, source queue, query test, health check)

**Prompt template:**
```
请以你刚才选择的专家视角，严格审核下面这个 Ask the vault 回答是否准确、严谨、证据分层是否正确。不要只润色。

最后给出：
- 保留
- 修改
- 删除或降级
- 需要补证据
- 不应写回，只保留聊天
```

### Step 3: Classify Findings

Assign primary review type:

| Review Type | Meaning | Typical Action |
|---|---|---|
| `wording downgrade` | Answer wording stronger than source support | Revise answer/topic wording |
| `endpoint hierarchy` | Answer collapses distinct outcomes | Update endpoint owner |
| `source gap` | Reviewer needs evidence not in vault | Queue source/fulltext work |
| `routing miss` | Ask the vault loaded wrong sources | Add query test |
| `scenario specificity` | Answer failed to ask what kind of use case | Add scenario-aware prompt |
| `promotion candidate` | Review produces durable branch clarity | Stage content precision promotion |

### Step 4: Map to System Homes

Every finding must land in exactly one home:

| Destination | Use When |
|---|---|
| `chat-only` | Useful rewrite, no durable structure |
| `inbox/` staged | Likely reusable, needs review |
| `topic page` | Canonical wording too strong or flat |
| `memo / narrow owner` | Branch boundary needs control layer |
| `source/deep extraction queue` | Full text or source depth is blocker |
| `query test` | Same bad answer could recur |
| `health check` | Drift is mechanically detectable |

### Step 5: Decide Movement

Use promotion states:

- `promote` — conservative, source-anchored, structurally clarifying
- `partial-promote` — some findings actionable, others need verification
- `hold` — needs more evidence or source access
- `needs source access` — blocked on original text

**Default is `hold`** unless correction is conservative and source-anchored.

### Step 6: Record Sample

Write to `inbox/{disease}/` with:
- Original answer summary
- Expert lens
- Findings table
- System action table
- What not to say
- Pattern stability notes

## Constraints

- **Never treat expert chat as source evidence**
- **Never auto-run** — expert selection and claim evaluation require judgment
- **Never promote without source verification** for quantitative claims
- **Always preserve provenance tags** in revised answers

## Verified Patterns (from 3 samples)

1. **Endpoint hierarchy collapse** — answers conflate distinct intervention types or outcome measures
2. **Wording stronger than sources** — answer presents preliminary findings as definitive
3. **Routing gaps** — query loads incomplete source set for the question type
4. **Source verification queue** — specific numbers need original text confirmation

## Related

- [Expert review prototype](../indexes/expert-answer-review-prototype-20260514.md)
- [Content precision promotion workflow](../indexes/content-precision-promotion-workflow.md)
- [Query to writeback](../indexes/query-to-writeback.md)
