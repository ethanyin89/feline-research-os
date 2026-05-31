---
id: topic-cancer-cox-prognosis-markers
type: topic
topic: cancer
species: feline
disease: cancer
question_type: biomarker
source_ids: [src-cancer-003]
last_compiled_at: 2026-05-30
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: not_checked
owner: codex
status: active
---

# COX And Prognosis Marker Caveats

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| CP1 | COX markers belong in a prognosis-marker caveat layer, not a treatment recommendation layer | B | src-cancer-003 | marker architecture, not therapy guidance |
| CP2 | Feline mammary carcinoma is the main feline branch where COX-2 can be carried as a prognosis-marker candidate | B | src-cancer-003 | candidate marker, not survival prediction |
| CP3 | Feline oral SCC has a COX-1 distribution-pattern signal, while COX-2 was not prognostic in the reviewed oral SCC study | B | src-cancer-003 | source-specific, not complete oral SCC guide |
| CP4 | Immunohistochemistry scoring heterogeneity and cutoff variation block clean generalization | B | src-cancer-003 | method caveat |

## Evidence-Depth Caveat

This page is based on one deep-extracted systematic review. It can define marker caveats and extraction priorities. It cannot create biomarker-based treatment rules or prognosis calculators.

## Core Takeaway

COX evidence should be represented as a cautious prognosis-marker layer. In the feline subset of the reviewed literature, the reusable signals are narrow:

- COX-2: feline mammary carcinoma candidate prognosis marker
- COX-1 distribution pattern: feline oral SCC signal
- COX-2: not supported as the oral SCC prognostic marker in this review

## Marker Map

| Branch | Marker Signal | Safe Use | Boundary |
|---|---|---|---|
| mammary carcinoma | COX-2 | candidate prognosis-marker caveat | not treatment guidance |
| oral SCC | COX-1 distribution pattern | extraction priority and marker note | not complete oral SCC prognosis guide |
| transitional cell carcinoma | COX-1 / COX-2 evidence too small | do not promote | seven-cat study too small for rule |

## Method Caveats

`src-cancer-003` emphasizes that most included studies used semi-quantitative immunohistochemistry. Scoring systems, cutoffs, observers, antibodies, and tissue processing differed across studies.

This matters because:

- marker positivity may not mean the same thing across studies
- survival associations can be confounded
- branch pages should not imply standardized clinical test thresholds

## What The Module Can Say Safely

- COX markers have prognosis-marker relevance in selected feline cancer branches.
- COX-2 should be treated as a feline mammary carcinoma candidate marker with caveats.
- COX-1 distribution pattern is the relevant oral SCC signal in this review.
- More standardized, feline-specific studies are needed before strong clinical use.

## What The Module Should Not Say Yet

- Do not recommend COX inhibitors.
- Do not predict survival from COX status.
- Do not rank biomarkers.
- Do not make a TCC rule.
- Do not treat mixed canine/feline conclusions as automatically feline-specific.

## Current Role

Use this page as the cancer module's biomarker caution layer. It should link out to mammary carcinoma and future oral SCC pages, but not serve as a treatment page.
