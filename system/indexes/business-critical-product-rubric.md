---
id: system-business-critical-product-rubric
type: system
topic: all
last_compiled_at: 2026-06-04
owner: codex
status: active
language: en
---

# Business-Critical Product Rubric

This page defines what makes `feline-research-os` business-critical.

It is not a feature list. It is a decision contract.

## One-Line Definition

A business-critical product surface is one where:

`question -> evidence map -> decision artifact -> business action`

If a weekly user session does not produce a clearer decision, it failed.

## User Segments

### Segment 1: Internal R&D / BD Operator

| Field | Value |
|-------|-------|
| Job | Decide which disease branch to pursue, compare endpoint maturity, identify evidence gaps, prepare partner memos |
| Why they care | Saves analyst time, reduces overclaim risk, faster opportunity review |
| Primary surface | Opportunity Brief Workbench |
| Success signal | Brief used in prioritization meeting |

### Segment 2: Companion Animal Therapeutics / Diagnostics Team

| Field | Value |
|-------|-------|
| Job | Evaluate product archetypes, understand endpoint fit, map regulatory path, identify next evidence needed |
| Why they care | Supports product strategy, reduces wasted preclinical effort, decides if indication is investable |
| Primary surface | Indication Evidence Dossier |
| Success signal | Go/no-go decision made using dossier |

### Segment 3: Veterinary KOL / Research Collaborator

| Field | Value |
|-------|-------|
| Job | Verify claims are source-supported, understand vault boundaries, co-author briefings |
| Why they care | Faster literature orientation, traceable evidence, fewer hallucinations |
| Primary surface | Claim Evidence Workbench |
| Success signal | Claim promoted, revised, or killed based on verdict |

### Segment 4: Educated Ordinary Reader

| Field | Value |
|-------|-------|
| Job | Understand disease, know questions to ask vet, distinguish strong vs weak advice |
| Why they care | Trust, clarity, no fake medical advice |
| Primary surface | Ask the Vault |
| Success signal | User trusts answer, returns for next question |

Note: Segment 4 is the trust and distribution layer, not the monetization wedge.

## Decision Types

Each decision type has a required artifact.

| Decision | Required Artifact | Success Signal |
|----------|-------------------|----------------|
| Which disease area to pursue next? | Cross-disease opportunity brief | Leadership uses it in prioritization |
| Is this claim defensible? | Claim evidence card | Claim is promoted, revised, or killed |
| What endpoint should a study use? | Endpoint decision memo | Endpoint shortlist changes study design |
| Is this treatment branch investable? | Indication evidence dossier | Go/no-go or diligence action taken |
| What evidence is missing? | Gap-to-source intake queue | New source search or extraction starts |
| What can we say publicly? | Source-bounded owner answer | Communication avoids overclaim |

## Required Artifact Contracts

### Claim Evidence Card

Input:
- disease
- claim text
- optional source IDs

Required output fields:

| Field | Description | Required |
|-------|-------------|----------|
| verdict | supported / partially supported / not supported / absent | Yes |
| key_sources | Source IDs supporting the claim | Yes |
| evidence_depth | Number of sources, extraction level | Yes |
| quoted_facts | Direct quotes if available | No |
| source_supported_conclusion | Synthesized conclusion from sources | Yes |
| boundary | What the claim does NOT cover | Yes |
| next_action | promote / revise / kill / search more | Yes |

Failure modes:
- verdict without sources = FAIL
- boundary section missing = FAIL
- next_action missing = FAIL

### Opportunity Brief

Required sections:

| Section | Description | Required |
|---------|-------------|----------|
| disease_branch | Which disease and sub-branch | Yes |
| business_question | What decision this brief supports | Yes |
| evidence_backbone | Key sources and compiled pages | Yes |
| endpoint_maturity | Which endpoints are measurable, evidence level | Yes |
| treatment_opportunity | What interventions are viable | Yes |
| regulatory_path_notes | Known regulatory considerations | Yes |
| missing_evidence | Gaps that weaken the case | Yes |
| go_no_go_implication | Clear decision implication | Yes |
| source_appendix | Source IDs and verification paths | Yes |

Failure modes:
- missing_evidence section absent = FAIL
- go_no_go_implication absent = FAIL
- source_appendix absent = FAIL

### Endpoint Decision Memo

Required sections:

| Section | Description | Required |
|---------|-------------|----------|
| disease | Which disease | Yes |
| endpoint_hierarchy | Ranked list of endpoints with evidence level | Yes |
| primary_endpoint_recommendation | Recommended primary endpoint | Yes |
| secondary_endpoints | Supporting endpoints | Yes |
| measurement_protocol_notes | How to measure each endpoint | No |
| regulatory_precedent | Prior approvals using these endpoints | No |
| boundary | What these endpoints do NOT measure | Yes |
| source_appendix | Source IDs | Yes |

Failure modes:
- endpoint_hierarchy without evidence levels = FAIL
- boundary section missing = FAIL

### Gap-to-Intake Queue Item

Required fields:

| Field | Description | Required |
|-------|-------------|----------|
| gap_id | Unique identifier | Yes |
| disease | Which disease | Yes |
| gap_description | What evidence is missing | Yes |
| impact | How this gap weakens current claims | Yes |
| suggested_search | Keywords or sources to find | Yes |
| priority | P0 / P1 / P2 | Yes |
| created_from | Which artifact exposed this gap | Yes |

Failure modes:
- gap without impact assessment = FAIL
- gap without suggested_search = FAIL

## Satisfaction Metrics

Track these, not vanity metrics.

| KPI | Target | Measurement |
|-----|--------|-------------|
| Decision artifacts produced per week | 1-3 | Count of claim cards + briefs + memos |
| Claims killed or revised due to evidence boundary | >0 | Count of verdict=not_supported leading to action |
| Gap-to-intake tasks generated from real questions | >0 | Count of gaps created from user sessions |
| Meeting-ready briefs exported | >0 | Count of briefs used in actual meetings |
| Time from question to defensible brief | <30 min | Measured from query to artifact export |
| Unsupported claim rate in artifacts | 0 | Audit of artifacts for missing source IDs |

## Unacceptable Failure Modes

These are hard failures. If any occur, the product is not business-critical.

### Content Failures

| Failure | Why unacceptable | Mitigation |
|---------|------------------|------------|
| Verdict without source IDs | No traceability | Require source_ids in every verdict |
| Boundary section missing | User doesn't know limits | Mandatory boundary field |
| Generic summary instead of decision | Remains optional | Every artifact must have decision implication |
| Overclaim (C-level claim presented as A/B) | Credibility damage | Claim-audit-protocol enforcement |
| Missing evidence hidden | Bad business decision | Mandatory missing_evidence section |

### Product Failures

| Failure | Why unacceptable | Mitigation |
|---------|------------------|------------|
| Only chat UI visible | User misses business value | Add Decide and Verify entry points |
| Disease maturity not shown | False confidence | Show maturity level per disease |
| Artifacts bypass health checks | Truth layer rots | Route outputs through inbox/promotion/health |
| Paid mode produces random better prose | No contract | Paid mode must obey same artifact contract |

### Anti-Slop Rules

These outputs are banned from business surfaces:

1. Generic disease summaries without decision implication
2. Unranked source lists
3. "Consult a vet" endings for research workflows
4. No boundary section
5. No go/no-go implication
6. Citations without loaded source trace
7. Artifact that cannot be copied into a meeting doc

## Verification Checklist

Before any business artifact is exported:

- [ ] Verdict or recommendation is present
- [ ] All claims have source_ids
- [ ] Boundary section exists
- [ ] Missing evidence section exists (if opportunity brief)
- [ ] Next action is specified
- [ ] No Level C claims presented as Level A/B
- [ ] Artifact can be copy-pasted into a meeting doc

## Disease Maturity Labels

Each disease should show its evidence maturity.

| Label | Meaning |
|-------|---------|
| Mature | 20+ sources, deep extraction complete, topic pages compiled |
| Developing | 10-20 sources, partial extraction, topic pages exist |
| Thin | <10 sources, minimal extraction, gaps prominent |

Current status:

| Disease | Sources | Extraction | Maturity |
|---------|---------|------------|----------|
| CKD | 24 | Full | Mature |
| FIP | 24 | Full | Mature |
| HCM | 24 | Full | Mature |
| IBD | 24 | Full | Mature |
| Diabetes | 118 | Partial | Developing |
| FCV | 24 | Full | Mature |
| Obesity | 87 | Partial | Developing |
| Cancer | 102 | Partial | Developing |

## What This Rubric Does NOT Cover

This rubric does not:
- Define source card format (see source card template)
- Define claim audit rules (see claim-audit-protocol.md)
- Define ordinary-user answer format (see ordinary-user-usage-guide.md)
- Define language QA rules (see language-qa-protocol.md)

This rubric only defines what makes a product surface business-critical.
