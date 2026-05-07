# Deep Extraction Workflow

This page defines how deep extraction works inside `feline-research-os`.

Use it when first-pass ingest is no longer enough and a source needs to become a reusable knowledge asset.

## What This Workflow Is For

Deep extraction is the bridge between:

- `raw source exists`
and
- `the source is safe to reuse across topic pages, entity cards, and outputs`

It is not a default step for every paper.
It is for high-value sources only.

## When To Use It

Use deep extraction when a source is one of the following:

- a practice-defining guideline
- a high-value review that shapes mechanism or regulatory logic
- a primary study that bridges structure and endpoints
- a source likely to be cited repeatedly across the vault

Do not use it for routine clipping or low-value duplicates.

## Current Prompt

- [deep extraction prompt v1](../prompts/deep-extraction-prompt-v1.md)
- [bilingual content policy](../prompts/bilingual-content-policy.md)

This prompt replaces vague “summarize the paper” behavior with a staged workflow:

1. Phase 0: sequential micro-analysis
2. Phase 1: topic reconstruction
3. Phase 2: claim-evidence structure
4. Phase 3: promotion check

## Current Demonstration Set

The workflow has already been run on three core CKD sources:

- [src-ckd-004 deep extraction](src-ckd-004-deep-extraction-round1.md)
- [src-ckd-010 deep extraction](src-ckd-010-deep-extraction-round1.md)
- [src-ckd-011 deep extraction](src-ckd-011-deep-extraction-round1.md)

And the result has already been compressed once into:

- [core paper synthesis memo](core-paper-synthesis-memo-ckd-round1.md)

## Actual Working Sequence

### Step 1: Select A Worthy Source

Ask:

- will this source be reused often?
- does it support a backbone claim?
- is the current source card still too thin?

If no, stay at first-pass ingest.

### Step 2: Run The Prompt

Create a worksheet in `system/indexes/` using this naming pattern:

- `src-xxxx-deep-extraction-round1.md`

The worksheet should preserve all four phases.

### Step 3: Update The Source Card

Only after the worksheet is done:

- thicken `quoted_fact`
- sharpen `source_supported_conclusion`
- tighten `llm_inference`
- expand `open follow-up questions`

Do not write back claims that the worksheet itself marked as unsafe.
Do not translate the raw source card into another language unless there is a specific exception.

### Step 4: Promote Conservatively

Use Phase 3 `Promotion Check` to decide what belongs in:

- topic pages
- entity cards
- output documents

If a claim is:

- source-specific but useful later -> keep in source card
- stable enough for repeated reuse -> promote to topic/entity
- promising but not well bounded -> keep provisional

If you are about to promote, use:

- [write-back promotion checklist](writeback-promotion-checklist.md)
- [write-back promotion template](writeback-promotion-template.md)

### Step 5: Compress Across Sources

After two or more deep extractions exist on a shared question, create a synthesis layer such as:

- memo
- bridge table
- consensus summary

This is how the vault moves from source depth to compiled knowledge.

### Step 6: Derive Bilingual Assets Selectively

If the source cluster is high-value and reused often:

- derive bilingual memo or output at the compiled layer
- keep raw source language unchanged
- preserve evidence boundaries during translation

Good candidates:

- synthesis memo
- briefing
- dossier
- slide deck

## What Good Output Looks Like

A successful deep extraction should produce:

- one denser source card
- one or more safer topic write-backs
- a clearer statement of what cannot yet be claimed

The value is not “more text.”
The value is:

- more precise boundaries
- better cross-page reuse
- lower hallucination risk
- higher bilingual reuse without corrupting the raw layer

## Current Best Example

The strongest current example is the three-paper CKD backbone:

- `src-ckd-004` operational clinical logic
- `src-ckd-010` clinicopathology bridge
- `src-ckd-011` fibrosis and mediator framing

That set now supports:

- [core paper synthesis memo](core-paper-synthesis-memo-ckd-round1.md)
- [synthesis index](../../topics/ckd/synthesis-index.md)

## Recommended Next Uses

If this workflow continues, the next best targets are:

1. higher-value regulatory sources
2. newer SDMA-specific studies
3. stronger feline treatment primary studies
