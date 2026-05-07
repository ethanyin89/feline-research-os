# Bilingual Content Policy

This file defines where bilingual handling belongs in `feline-research-os`.

## Core Rule

`raw data stays in its original language`

That means:

- English source stays English
- Chinese source stays Chinese
- clipped material is not normalized into another language at the raw layer

Do not translate raw source cards just to make the vault look uniform.

## Where Bilingual Support Belongs

Bilingual support belongs in:

- compiled topic outputs
- briefings
- dossiers
- slides
- synthesis memos
- selected high-value workflow artifacts

It does **not** belong in:

- `raw/`
- first-pass ingest as a default requirement
- evidence-layer rewriting inside source cards

## Why

Keeping raw data in the original language protects:

- traceability
- auditability
- terminology precision
- low-friction ingest

If raw data is translated too early, the vault becomes harder to trust.

## Practical Rule Set

### Source Layer

- preserve original title, wording, and language
- extract evidence in the source card language that best preserves accuracy
- do not rewrite the source card into bilingual form by default

### Topic Layer

- default to one primary working language per page
- bilingual topic variants are allowed only for high-reuse pages
- if a page has a bilingual derivative, make that explicit

### Output Layer

- bilingual derivation is encouraged
- the derivative must preserve the same evidence boundaries as the original
- translation must not strengthen claims

## Translation Rules

When bilingual derivation is needed, follow:

- [bilingual output rules](bilingual-output-rules.md)

And also preserve domain-specific accuracy for:

- drug names
- disease names
- endpoint names
- regulatory route names
- doses and units
- agency names

## Current Recommended Pattern

For this project, the preferred pattern is:

1. ingest source in original language
2. compile topic in one working language
3. derive bilingual or English/Chinese outputs only where reuse value is high

## Current Good Candidates For Bilingual Derivation

- core paper synthesis memo
- briefing
- dossier
- slides

## Current Non-Candidates

- routine source cards
- low-value clips
- provisional notes
