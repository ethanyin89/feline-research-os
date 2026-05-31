---
id: topic-cancer-suspected-cancer-workflow
type: topic
topic: cancer
species: feline
disease: cancer
question_type: workflow
source_ids: [src-cancer-040, src-cancer-004]
last_compiled_at: 2026-05-30
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: not_checked
owner: codex
status: active
---

# Suspected Cancer Workflow

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| CW1 | Cancer in cats should be approached as a workflow: recognize possible presentations, confirm diagnosis, stage disease, then consider treatment options | B | src-cancer-040 | workflow, not remote diagnosis |
| CW2 | Diagnosis and staging should be separated; treatment discussion should not precede tumor typing and extent assessment | B | src-cancer-040 | clinical sequence, not test prescription |
| CW3 | Feline cancer branches should be separated by tumor family because mechanism, behavior, and treatment evidence differ | B | src-cancer-004 | branch map, not complete clinical guide |

## Evidence-Depth Caveat

This page sits on two deep-extracted sources. `src-cancer-040` is the workflow anchor and `src-cancer-004` is the molecular branch-map anchor. It is not a diagnostic manual and not a treatment protocol.

## Core Takeaway

The safest first cancer page is not a list of treatments. It is a sequence:

1. possible presentation
2. veterinary diagnostic confirmation
3. staging and extent assessment
4. branch-specific treatment planning
5. evidence-bound prognosis discussion

## Workflow Architecture

### 1. Presentation

Cancer may present as an obvious mass, but it may also appear through non-specific signs. The safe reader-facing framing is: possible cancer requires veterinary assessment and differential diagnosis, not symptom-based certainty.

**Lead source:** `src-cancer-040`

### 2. Diagnosis

Cytology and biopsy are different tools. Histopathology is often needed for definitive classification, and the sampling choice can affect later treatment options.

**Guardrail:** do not imply that a visible mass equals a known tumor type.

**Lead source:** `src-cancer-040`

### 3. Staging

Staging should assess the primary tumor, regional lymph nodes, and distant disease where relevant. Imaging and sampling choices depend on tumor site and management implications.

**Guardrail:** do not jump from diagnosis to treatment without staging context.

**Lead source:** `src-cancer-040`

### 4. Branch-Specific Planning

The current branch map separates:

- lymphoma / lymphoproliferative disease
- oral squamous cell carcinoma
- sarcoma / injection-site sarcoma
- mammary carcinoma
- mast cell tumor

**Lead source:** `src-cancer-004`

## What The Module Can Say Safely

- Suspected cancer needs diagnostic confirmation.
- Diagnosis and staging are separate steps.
- Treatment modality discussion depends on tumor type, stage, feasibility, and patient constraints.
- Cancer content should split by tumor family early.

## What The Module Should Not Say Yet

- Do not provide remote diagnosis from signs.
- Do not rank surgery, chemotherapy, or radiotherapy globally.
- Do not give tumor-specific protocols from this workflow source.
- Do not state survival expectations without tumor-specific sources.

## Current Role

Use this as the cancer front-door workflow. Tumor-family pages should link back here whenever they discuss diagnosis, staging, or treatment planning.
