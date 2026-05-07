# Compile Checklist

Use this checklist whenever a new source enters the vault.

This is the operating loop that turns the vault from a static folder tree into a continuously compiled research system.

## Stage 1: Ingest

### Goal

Make sure the source exists as a stable object in the system.

### Checklist

- put the original file, clip, or note into the correct `raw/` folder
- create a source card with:
  - id
  - title
  - source kind
  - disease
  - evidence level
  - links
- classify the source using [source hierarchy and claim-fit policy](source-hierarchy-and-claim-fit-policy.md)
- add the source to the relevant source index
- write a one-line summary
- note whether this is:
  - review / guideline
  - primary study
  - regulation / guidance
  - commentary / promo / context-only source

### Exit Condition

The source can be found, identified, and cited.

## Stage 2: Extract

### Goal

Turn the source from “file exists” into “usable knowledge object.”

### Checklist

- extract 3-7 `quoted_fact`
- extract 2-5 `source_supported_conclusion`
- extract 1-3 `uncertainty_or_limit`
- write what this source most safely controls
- write what this source must not control
- decide whether this source is `anchor`, `support`, or `context`
- list candidate entities
- list likely write-back targets

### Rule

Do not fill `llm_inference` just to make the card look complete.

Do not leave the source-family / claim-fit judgment implicit.

### Exit Condition

The source card is rich enough to support topic compilation.

## Stage 3: Link

### Goal

Attach the source to the right part of the vault.

### Checklist

- add / update source ids in relevant topic pages
- link to existing entities where justified
- create a new entity only if:
  - the concept recurs
  - it matters to multiple outputs
  - it is not a one-off detail
- do not let commentary / promo / case-level sources silently control the main topic architecture

### Exit Condition

The source is no longer isolated.

## Stage 4: Compile

### Goal

Promote repeated signals from source cards into topic pages.

### Checklist

- update the topic page's `quoted_fact`
- update the topic page's `source_supported_conclusion`
- add new uncertainty only if the source actually adds ambiguity
- update bridge tables or comparison matrices when needed

### Rule

Do not promote:

- vague impressions
- unsupported synthesis
- a conclusion that only exists in `llm_inference`

### Exit Condition

The topic page becomes denser, not noisier.

## Stage 5: Derive Outputs

### Goal

Turn compiled knowledge into reusable outputs.

### Checklist

- decide whether the new source changes:
  - briefing
  - dossier
  - slides
- if yes, update or derive the relevant output
- preserve evidence layers
- if needed, create an English derivative for output-facing documents

### Exit Condition

Important new knowledge is reflected in at least one reusable output.

## Stage 6: Review And Promote

### Goal

Prevent low-quality synthesis from leaking into core pages.

### Checklist

- ask: is this `quoted_fact`, `source_supported_conclusion`, or `llm_inference`?
- ask: would I still defend this claim if someone opened the source card right now?
- ask: does this change the topic page, or should it stay only in an output?
- if promotion is plausible, apply:
  - [write-back promotion checklist](writeback-promotion-checklist.md)
  - [write-back promotion template](writeback-promotion-template.md)

### Exit Condition

Promotion happens deliberately, not automatically.

## Stage 7: Health Check

### Goal

Keep the system internally consistent as it grows.

### Checklist

- is the source indexed?
- is the frontmatter complete?
- does the topic page cite source ids?
- did a new entity get created without real need?
- did a conclusion become stronger than the underlying evidence?
- did bilingual outputs drift from the original meaning?

### Exit Condition

The new source does not degrade the system.

## Quick Version

If you only have 5 minutes, do this:

1. ingest
2. extract one-line summary + 3 facts
3. add source id to the right topic page
4. decide whether it changes briefing / dossier

## Full Version

If the source is important, run all 7 stages.

## When To Stop

Stop compiling and leave a note if:

- the source is too weak
- the source duplicates what is already captured
- the source only adds noise, not structure

Not every source deserves promotion.

That is part of the discipline.
