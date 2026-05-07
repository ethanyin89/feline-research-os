# Health Check Report

Date: 2026-04-08  
Scope: `feline-research-os/` round 1 CKD vault

## Structural Checks

### Passed

- vault directories exist for raw, entities, topics, outputs, and system
- source, topic, and output templates exist
- CKD topic index exists
- briefing, dossier, and slides outputs exist

### Findings

1. `topics/ckd/model-summary.md` and `topics/ckd/translation-brief.md` were missing before this round.
Severity: medium  
Status: fixed in this round

2. bilingual policy existed in the plan, but templates and schema do not yet expose a `language` field.
Severity: medium  
Status: open

## Traceability Checks

### Passed

- key topic pages now declare `source_ids`
- outputs declare `source_ids`

### Findings

3. some source cards remain abstract-weighted rather than full-text extracted.
Severity: medium  
Impact: topic confidence can be overstated if not monitored  
Status: open

4. `regulatory-brief.md` is route-level solid, but still lacks a comparison table and indication-specific evidence requirements.
Severity: medium  
Impact: cannot yet support serious registration recommendation  
Status: open

## Entity Checks

### Findings

5. original V1 plan still treated `ugt1a6` as effectively required even though current CKD evidence more strongly supports `tgf-beta`.
Severity: medium  
Status: fixed in this round

6. endpoint set now clearly includes USG, UPCR, phosphorus, and systolic blood pressure, but not all of these had dedicated cards before this round.
Severity: medium  
Status: fixed in this round

## Write-Back Safety Checks

### Passed

- topic pages distinguish `quoted_fact`, `source_supported_conclusion`, and `llm_inference`
- outputs preserve evidence layers

### Findings

7. no formal bilingual output derivation rule exists yet, so future English outputs may drift from Chinese source wording.
Severity: medium  
Status: open

8. no executed promotion checklist exists yet for “when can output content be promoted into topic pages”.
Severity: high  
Impact: risk of premature write-back from draft output  
Status: open

## Recommended Fix Order

1. add `language` field to output and topic schema
2. create a promotion checklist for write-back safety
3. build a regulatory comparison table
4. continue full-text extraction on highest-value source cards

## Overall Status

Round 1 vault is usable.

Main risk is no longer missing structure.  
Main risk is maintenance discipline and promotion safety.
