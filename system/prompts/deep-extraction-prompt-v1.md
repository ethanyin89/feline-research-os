# Deep Extraction Prompt V1

Use this prompt when a source is important enough to justify deeper extraction beyond first-pass ingest.

This prompt is designed for the current `feline-research-os` workflow.
It is not a generic summarization prompt.
Its job is to turn one high-value source into:

- denser source-card content
- cleaner topic write-back
- safer evidence promotion

## Best Use Cases

- guideline papers
- major review papers
- primary studies that connect mechanism and endpoints
- regulatory documents that shape route selection
- industry reports or interviews worth preserving at source depth

## Not The Right Use Case

- low-value clipping
- duplicate source coverage
- materials that only need title/abstract ingest

## Operating Principle

`first-pass ingest` answers:
what is this source roughly about?

`deep extraction` answers:
what exactly does this source say, how does it build its case, and what can safely be promoted into the vault?

## Required Output Discipline

Always preserve the vault's evidence policy:

- `quoted_fact`
- `source_supported_conclusion`
- `llm_inference`

Do not collapse these layers.

## Workflow

### Phase 0: Sequential Micro-Analysis

Work through the source in natural order.
Split it into paragraph units or content units by topic shift, not by arbitrary token count.
For each unit, answer:

1. `core_claim`
What is this unit really saying?

2. `implicit_premise`
What assumptions must be true for this claim to hold?

3. `relation_to_previous`
Is this a continuation, turn, qualification, contradiction, or new branch?

4. `hard_details`
Capture all hard information:
- numbers
- dates
- names
- compounds
- endpoints
- products
- studies
- organizations
- routes
- guidance references

5. `tension_or_surprise`
Optional, but include when useful.
Note contradictions, overclaims, or friction with other parts of the same source.

#### Output Template

```md
#### Unit [N]: [one-line label]

- core_claim:
- implicit_premise:
- relation_to_previous:
- hard_details:
- tension_or_surprise:
```

### Phase 1: Topic Reconstruction

After Phase 0, regroup the source by naturally emerging themes.

Do not force common categories if the source itself does not support them.

For each theme:

- rewrite the content in fluent prose
- preserve all important hard information
- keep speaker/author attribution clear
- do not flatten disagreements

#### Output Template

```md
## Theme: [name]

[full reconstruction]

### Key Quote
> "..."

### Hard Information
- ...
```

### Phase 2: Claim-Evidence Structure

For each theme, extract:

- `claim`
- `support`
- `details`
- `implicit_premise`

#### Output Template

```md
### [Theme] Key Points

**Claim 1**
- support:
- details:
- implicit_premise:
```

### Phase 3: Vault Promotion Check

Before producing final write-back, answer:

1. what belongs in the source card only?
2. what can be promoted into topic pages now?
3. what should remain provisional?
4. what conflicts with current vault content?
5. what new entities, topic pages, or output updates become justified?

#### Output Template

```md
## Promotion Check

- source_card_updates:
- topic_write_back_targets:
- not_safe_to_promote_yet:
- conflicts_with_existing_vault:
- new_entities_or_pages_justified:
```

## Current Project Adaptation

When using this prompt in `feline-research-os`, prefer these write-back targets:

- `raw/papers/*.md`
- `topics/ckd/*.md`
- `entities/endpoints/*.md`
- `entities/mechanisms/*.md`
- `entities/regulations/*.md`
- `entities/symptoms/*.md`

Raw source material should remain in its original language.
Do not translate the raw layer just to make the vault look uniform.

## Domain-Specific Translation Layer

If the source is Chinese and the write-back target is English, or vice versa:

- keep raw source material in its original language
- apply translation only to compiled write-back or derived output layers
- preserve drug names, disease names, endpoint terms, and regulatory references exactly
- prefer industry-standard veterinary phrasing over literal translation
- keep tone aligned to source type:
  - guideline: precise
  - review: analytical
  - marketing/industry interview: readable but still exact
- never smooth over uncertainty in the original

For current project use, accuracy beats style.
Especially protect:

- compounds
- dose units
- route names
- agencies
- regulatory pathways
- disease names
- endpoint names

For full project policy, follow:

- [bilingual content policy](bilingual-content-policy.md)

## Recommended Current Use

This prompt is especially useful right now for:

1. `src-ckd-004`
2. `src-ckd-010`
3. `src-ckd-011`
4. high-value regulatory sources

## What Success Looks Like

A good deep extraction should let a later reader:

- understand the source without reopening it
- know exactly what is defensible
- see where the source is weak
- update source cards and topic pages with low hallucination risk
