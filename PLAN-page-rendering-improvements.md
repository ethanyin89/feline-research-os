# Plan: Reusable Research Result Presentation

<!-- /autoplan restore point: /Users/jiawei/.gstack/projects/feline-research-os/idea-chatacademia-research-workbench-autoplan-restore-20260612-100546.md -->

**Status:** Phase 6 approved direction: transparent research output + selective knowledge promotion
**Branch:** `idea-chatacademia-research-workbench`
**Base branch:** `main`
**Date:** 2026-06-12
**Scope:** Presentation logic for research results, not a visual rebrand

## Problem

The vault already produces sourced answers, topic pages, evidence rankings, research
traces, and source metadata. The missing layer is a stable contract for what users see
first, what they can inspect next, and how evidence limits are explained without exposing
repository internals.

Today the result experience is inconsistent:

- `render_answer_block()` shows the answer before confidence and source context.
- source titles are readable, but source links and evidence depth are not modeled as a
  reusable presentation object.
- internal terms such as `src-ckd-003`, `abstract_weighted`, and `llm_inference` can leak
  into ordinary-user surfaces.
- topic pages, ranked treatment pages, and Ask the Vault answers use related evidence
  concepts but do not share a presentation contract.
- loading, empty, partial-evidence, unavailable-link, and degraded-source states are not
  specified as user experiences.

This matters because the user must be able to answer four questions in order:

1. What is the answer?
2. How much should I trust it?
3. What evidence can I inspect?
4. What should I do next, and where are the limits?

## Confirmed Premises

These premises come from the current user instruction and the supplied handoff documents:

1. Content presentation logic has higher priority than visual restyling.
2. ii.inc is a reference for information hierarchy, concise result cards, and multiple
   research exits, not a visual template to copy.
3. The existing Geist, dark, industrial design system remains authoritative.
4. Repeated work must become a reusable skill after 3-10 manual samples.
5. User-facing citations use paper titles plus canonical links such as DOI or PubMed,
   never internal source IDs.
6. This phase improves how existing research is presented and selectively preserved. It
   does not replace the source-card evidence base or let generated text become evidence.
7. Research Records preserve task context and user-selected outputs. Only source-traced,
   human-selected, validated material may later be promoted into topic, index, or synthesis
   pages.

## CEO Premise Challenge

Two independent reviewers agreed on a product-safety problem in the current draft:

1. `high | medium | low` is not a defensible answer-level trust signal. The current
   `compute_confidence()` function measures only the proportion of provenance tags; it
   does not measure study quality, contradiction, recency, claim coverage, source
   independence, or human review.
2. Moving that label above the answer would amplify authority without improving its basis.
3. The product's defensible unit is not a generic result card. It is:

```text
claim
  → supporting or challenging evidence
  → evidence depth
  → safe boundary
  → unresolved gap
  → decision implication
  → human authority state
```

4. A canonical DOI or PubMed link proves source identity, not that the paper supports every
   claim in the answer. Consequential claims must retain claim-to-source mapping.
5. The first pilot should prove that the presentation helps users detect unsupported
   claims and move toward a defensible decision, not merely that the page looks cleaner.

### User Challenge

**Original direction:** improve result presentation, with trust signals prominent and
the Ask the Vault response as the first integration target.

**Both reviewers recommend:** keep the presentation-layer project, but remove global
`high | medium | low` trust badges from V1; use a factual evidence profile and pilot the
contract on one claim/decision workflow before generalizing it.

**What the reviewers may be missing:** Ask the Vault may be the most practical current
surface for user feedback, and the user may intentionally want a coarse navigational
signal rather than a decision-grade label.

**Cost if the reviewers are wrong:** the plan starts narrower and delays the visible
Ask the Vault improvement and reusable skill.

## User Outcomes

After this work:

- an ordinary reader gets a short answer before technical detail;
- a professional reader can inspect claim provenance, source depth, and research trace;
- evidence limitations are visible before a result is used for a clinical or research
  decision;
- every result surface offers clear next research moves;
- new result pages can reuse one documented presentation contract and one skill instead
  of inventing hierarchy again.

## What Already Exists

| Need | Existing asset | Reuse decision |
|---|---|---|
| answer provenance | `render_provenance()` and provenance tags | keep as internal input; translate labels for the user |
| confidence summary | `render_trust_block()` | split calculation from rendering; place summary before answer |
| source titles | `readable_source_titles()` | extend into structured source display data |
| source list | `render_sources_section()` | replace title-only rows with canonical linked cards |
| audit trail | `render_research_trace()` | keep collapsed by default |
| answer composition | `render_answer_block()` | migrate incrementally behind a feature flag |
| design language | `DESIGN.md` | preserve Geist, dark surfaces, restrained provenance colors |
| manual samples | `content-presentation-logic-samples-20260611.md` | use as the first three fixtures |
| visual prototype | `presentation-logic-test-page.html` | use for hierarchy review, not as production code |
| ordinary-user precedent | learning `research-lite-output-mode` | titles over IDs, technical footers hidden, audit trail optional |

## Chosen Approach

### Approach A: Patch each page independently

- **Effort:** S
- **Risk:** High
- **Completeness:** 4/10
- **Advantage:** smallest immediate diff
- **Problem:** repeats hierarchy decisions and fails the "do not do it twice" rule

### Approach B: One generic renderer for every result

- **Effort:** L
- **Risk:** High
- **Completeness:** 8/10
- **Advantage:** maximum reuse
- **Problem:** topic pages, ranked evidence, and conversational answers have different
  reading jobs; one renderer would become a large conditional tree

### Approach C: Shared presentation contract plus three surface adapters

- **Effort:** M
- **Risk:** Medium-Low
- **Completeness:** 10/10
- **Advantage:** shares evidence semantics and state handling while preserving the
  correct anatomy for overview, ranked decision, and query-response surfaces

**Decision:** Use Approach C. It is explicit, reuses existing code, and avoids both
page-by-page duplication and a universal component with dozens of branches.

## Presentation Contract

Every result surface consumes a structured presentation model:

```text
ResultPresentation
├── context
│   ├── title
│   ├── subtitle
│   ├── audience: ordinary | professional
│   └── language: zh | en
├── evidence_profile
│   ├── authority_state: automated | human_reviewed
│   ├── direct_support_count
│   ├── supported_synthesis_count
│   ├── inference_count
│   ├── limited_source_count
│   ├── contradiction_count
│   └── unresolved_gap_count
├── primary_answer
│   ├── lead
│   ├── sections[]
│   └── inline_citations[]
├── evidence
│   ├── source_cards[]
│   ├── boundary_notice
│   └── research_trace[]
└── next_actions[]
```

`source_cards[]` use user-facing fields:

```text
SourceDisplay
├── title
├── canonical_url
├── publication_year
├── source_type_label
├── evidence_depth_label
└── limitations[]
```

Internal values are translated:

| Internal value | Ordinary-user label | Professional detail |
|---|---|---|
| `deep_extracted`, `audited` | 已核查全文 | exact verification status in expanded metadata |
| `source_checked` | 已核查来源 | exact verification status in expanded metadata |
| `abstract_weighted` | 基于摘要 | abstract-only limitation |
| `title_only` | 仅题录信息 | cannot support a substantive claim |
| `quoted_fact` | 直接来源 | original provenance type in expanded metadata |
| `source_supported_conclusion` | 来源支持 | original provenance type in expanded metadata |
| `llm_inference` | 分析推断 | original provenance type in expanded metadata |

Internal source IDs remain available only in expert metadata, logs, and research trace.

## Surface Anatomy

### 1. Overview / What-Is

```text
Title + plain subtitle
  ↓
Quick answer
  ↓
Key facts
  ↓
Explore next
  ↓
Sources and update status
  ↓
Boundary notice
```

Trust is concise and does not interrupt the first explanation. English is collapsed by
default when Chinese is the selected language.

### 2. Ranked Evidence / Decision Support

```text
Title + task context
  ↓
Evidence legend
  ↓
Top-ranked interventions, fully expanded
  ↓
Conditional and thin-evidence items, collapsed
  ↓
Comparison table
  ↓
Sources, limitations, and decision boundary
```

Every intervention must state both "supported use" and "do not overclaim."

### 3. Ask the Vault Response

```text
Question
  ↓
Trust summary
  ↓
Answer with linked citations
  ↓
Evidence limitations, when decision-relevant
  ↓
Source cards
  ↓
Research trace, collapsed
  ↓
Next research moves
  ↓
Expert review loop, when applicable
```

The trust summary appears before the answer because this surface can be generated from a
mix of direct sources and inference. The summary must remain one compact line plus an
optional explanation.

## State Matrix

| State | Trigger | User sees | Recovery |
|---|---|---|---|
| loading | retrieval or synthesis running | named current step, not a generic spinner | wait or cancel where supported |
| supported-profile | direct, sufficiently deep support | direct/support/inference profile with linked claims | inspect sources or continue |
| mixed-profile | supported synthesis or mixed depth | evidence profile and concise caveat | inspect limitations |
| sparse-profile | sparse sources or material inference | starter answer label, prominent limits | run deeper research |
| partial-sources | some source metadata/link lookup fails | answer remains, affected source marked unavailable | retry metadata lookup |
| title-only | source has no usable abstract/full text | source listed as discovery only | do not count toward claim support |
| no-direct-evidence | no relevant source cards | explicit abstention, no generated efficacy conclusion | start literature intake |
| empty-answer | synthesis returns blank content | named failure, no fake success state | retry or use local answer |
| malformed-provenance | unknown or broken provenance tags | safe plain text plus warning in trace | log and test parser fallback |
| source-link-missing | no DOI/PMID/canonical URL | title and "link unavailable" | expert metadata may show source ID |
| research-trace-missing | trace absent | trace section omitted | no user-facing error |
| bilingual-missing | translation absent | selected language only | no empty language expander |
| long-answer | answer exceeds reading budget | lead and first section expanded, remainder structured | expand sections |
| mobile-320px | narrow viewport | one-column cards, no horizontal table overflow | table becomes stacked rows |

## Interaction Rules

1. **Progressive disclosure:** primary answer is open; source metadata, research trace,
   and lower-ranked evidence are collapsed.
2. **Citation behavior:** citations display a shortened paper title and open the canonical
   URL in a new tab. Missing URLs are not rendered as fake links.
3. **Copy behavior:** "copy answer" copies readable answer text plus linked source titles,
   excluding UI labels and internal IDs.
4. **Next actions:** offer 2-4 task-specific research moves. Generic "ask anything" copy is
   not acceptable.
5. **Accessibility:** semantic headings, keyboard-operable expanders, visible focus,
   44px touch targets, color never carries meaning alone.
6. **Responsive behavior:** 720px maximum reading width; cards collapse to one column;
   comparison tables provide a stacked mobile representation.

## Architecture

```text
answer payload + source IDs + research trace
                    │
                    ▼
       build_result_presentation()
          │        │         │
          │        │         └── source display resolver
          │        └──────────── evidence profile builder
          └───────────────────── provenance parser
                    │
                    ▼
          ResultPresentation model
             │        │        │
             ▼        ▼        ▼
        overview   ranking   query response
         adapter    adapter      adapter
             │        │        │
             └────────┴────────┘
                    │
                    ▼
              Streamlit renderers
```

The model-building functions remain pure Python so they can be unit tested without
starting Streamlit. Streamlit functions only render validated presentation data.

## Implementation Phases

### Phase 1: Finalize and approve the manual samples

1. Replace all internal source IDs in the samples with paper titles and canonical links.
2. Replace raw evidence-depth vocabulary with the user-facing labels in this plan.
3. Add the missing states from the State Matrix to the HTML prototype.
4. Verify the three surface anatomies at 320px, 768px, and 1440px.
5. Record approval decisions for bilingual handling, trust placement, technical detail,
   and default collapse behavior.

### Phase 2: Codify the reusable skill

Create `.claude/skills/render-result-page.md` containing:

- when to use each surface type;
- the `ResultPresentation` and `SourceDisplay` contracts;
- user-facing evidence vocabulary;
- anatomy and progressive disclosure rules;
- state matrix;
- accessibility and responsive checks;
- three approved examples;
- anti-patterns, including internal IDs and raw verification statuses.

The skill is a design and content-generation contract. It does not execute paid APIs.

### Phase 3: Build pure presentation helpers

Add one focused module, preferably `core/result_presentation.py`, with:

- `build_evidence_profile()`
- `build_source_displays()`
- `build_result_presentation()`
- evidence-depth and provenance label maps
- validation and safe fallbacks

Do not create a general UI framework or move unrelated renderers.

### Phase 4: Integrate Ask the Vault first

1. Add a feature flag for the new query-response presentation.
2. Change `render_answer_block()` to consume `ResultPresentation`.
3. Preserve figures and the expert review loop.
4. Keep the old renderer available for rollback until acceptance tests pass.
5. Remove the flag and old branch only after the new path passes ordinary-user and
   professional-reader checks.

### Phase 5: Apply adapters to two static surfaces

1. Migrate one What-Is page.
2. Migrate one ranked treatment evidence page.
3. Compare the result against the approved samples.
4. Expand to other pages only after the first two are accepted.

## Phase Completion Notes

### Phase 1: Complete (2026-06-11)

- Replaced all internal source IDs with paper titles and DOI/PubMed links
- Updated HTML prototype with factual evidence profiles (removed confidence badges)
- Added State Matrix visual examples (loading, sparse, empty, error states)
- Translated all raw labels to user-facing Chinese vocabulary
- Applied CEO review decision: no global high/medium/low badges in V1

### Phase 2: Complete (2026-06-11)

- Created `.claude/skills/render-result-page.md` with complete presentation contract
- Documented surface types, vocabulary tables, state matrix, interaction rules
- Added 6 approved examples covering headers, profiles, source cards, provenance
- Listed anti-patterns and validation checklist

### Phase 3: Complete (2026-06-11)

- Created `core/result_presentation.py` with 450+ lines
- Implemented data models: ResultPresentation, SourceDisplay, EvidenceProfile, etc.
- Implemented label maps: EVIDENCE_DEPTH_LABELS, PROVENANCE_LABELS, SOURCE_TYPE_LABELS
- Implemented builder functions:
  - `build_evidence_profile()` - builds profile from sources and claims
  - `build_source_displays()` - builds user-facing source cards
  - `build_result_presentation()` - main entry point for full presentation
  - `build_next_actions()` - generates task-specific next actions
- Added state detection and validation helpers
- Module imports and basic verification passed

### Phase 4: Complete (2026-06-11)

- Added feature flag `USE_RESULT_PRESENTATION_V2` (env var)
- Added `load_full_source_metadata()` to extract DOI, PMID, verification_status from frontmatter
- Created v2 rendering functions in `scripts/app.py`:
  - `render_evidence_profile_v2()` - factual evidence profile (replaces confidence badges)
  - `render_source_card_v2()` - single source card with canonical DOI/PubMed link
  - `render_sources_section_v2()` - sources list with expandable overflow
  - `render_next_actions_v2()` - task-specific next research moves
  - `build_presentation_from_answer()` - bridges old query output to ResultPresentation
  - `render_answer_block_v2()` - complete v2 renderer
- Updated both call sites (chat history and live query) to check feature flag
- Old renderer preserved for rollback
- Code compiles and imports verified

**To test:** `USE_RESULT_PRESENTATION_V2=1 streamlit run scripts/app.py`

### Phase 5: Static Adapters Complete (2026-06-12)

- Corrected `EvidenceProfile` so unique source counts and claim provenance counts are
  separate facts.
- Added explicit `unknown_source_count`; missing or unrecognized verification metadata
  is no longer promoted to abstract-level evidence.
- Added `core/source_metadata.py` as the shared pure metadata resolver for DOI, PMID,
  canonical URL, source type, and verification state.
- Updated Ask the Vault V2 to use the shared resolver and translate provenance tags to
  paper titles plus Chinese labels in both visible output and downloads.
- Added strict static adapters:
  - overview adapter for `topics/ckd/what-is-ckd.md`
  - ranked adapter for `system/indexes/ckd-treatment-ranking-memo.md`
- Added a dependency-free deterministic HTML renderer and CLI:
  `scripts/render_static_result_page.py`.
- Generated accepted fixtures:
  - `outputs/presentation/ckd-what-is.html`
  - `outputs/presentation/ckd-treatment-ranking.html`
- Normalized every ranked intervention to include both `Supported use` and
  `Do not overclaim`.
- Added 7 regression tests covering source/claim count separation, unknown metadata,
  safe URL fallback, missing metadata, title-based provenance, visible-token leakage,
  tier order, and ranked boundaries.
- Browser acceptance passed at 375x812, 768x1024, and 1280x720 with no console errors.
  At 375px, document width equals viewport width and all tables use stacked mobile rows.

**Remaining gate:** do not remove `USE_RESULT_PRESENTATION_V2` or the legacy renderer
until a protected live Ask the Vault run passes ordinary-user and professional-reader
acceptance. That run requires the documented OpenRouter `$1/day` dashboard limit and
`OPENROUTER_DAILY_BUDGET_USD=1.00`, or explicit approval for another paid backend.

### Phase 6: Transparent Research Flywheel (2026-06-12)

**References:**

- `/Users/jiawei/Desktop/raw-2.md`, for the II-Commons Research Agent Answer Pattern
- Karpathy LLM Wiki, for a maintained, linked, reusable knowledge substrate
- the existing source-card, source-depth, claim-fit, Research Record, and harness-loop
  implementation in this repository

**Confirmed product model:**

The disease modules and curated paper sets are the bottom layer. Their purpose is to
provide real, traceable literature with explicit quality differences. The runtime
research flow operates above that base:

```text
real source cards + source quality / claim-fit controls
                         │
                         ▼
user research question
  → choose knowledge sources
  → retrieve evidence
  → organize structured context
  → LLM synthesis
  → reviewable research judgment
                         │
                         ▼
user chooses whether this run is worth preserving
  → save Research Record
  → source trace + human selection + validation
  → promote approved knowledge into topic / index / synthesis
                         │
                         └──────────────► richer knowledge base for future research
```

Detailed presentation is part of the research method. It helps the user inspect what
was searched, why sources were used, how evidence differs, what the answer does not
establish, and which research branch should come next.

#### Two Distinct Truth Layers

1. **Evidence base:** source cards and validated topic/index/synthesis content. This layer
   controls factual and decision-bearing claims.
2. **Research work layer:** Research Records containing the question, retrieval trace,
   selected evidence, generated answer, decisions, uncertainties, and next moves.

A Research Record is durable work context, not automatically validated knowledge.

The shared promotion unit is a claim, not an answer section:

```text
ResearchClaim
├── claim_id
├── text
├── original_answer_span
├── ordinal
├── source_ids[]
├── provenance: quoted_fact | source_supported_conclusion | inference
├── supported_use
├── boundary
├── selected_by_human
├── promotion_validation_results[]
├── promotion_status
└── target
```

`ResearchRecord.verifier_status` describes the quality checks run on the research
answer. It never grants promotion eligibility. Promotion uses a separate claim-level
validation result.

Claim IDs are stable within a record and generated at the synthesis/presentation
boundary. Original claim text is immutable after save; later edits create a new claim
version. Inference-only claims and claims without exact source mapping cannot be selected
for promotion.

#### Two-Stage Preservation Policy

**Stage 1, Consolidate the research run**

- The user explicitly chooses "沉淀这次研究".
- The system previews the record before save.
- The saved record includes the original question, interpreted task, actual retrieval
  scope, selected and excluded evidence, answer, key decisions, uncertainties,
  verification status, next moves, and handoff.
- Saving never edits source cards, topic pages, indexes, or synthesis pages.

**Stage 2, Promote validated knowledge**

- Promotion is a separate explicit action available only from a saved Research Record.
- The user selects the exact claims or sections worth promoting and the target page.
- Every promoted item must retain source IDs and claim-to-source provenance.
- Validation checks source existence, acceptable evidence depth, claim-fit, species
  boundary, and verifier status.
- Validation is claim-level and independent from the answer-level harness verifier.
- Promotion produces a reviewable draft or patch. It never silently publishes generated
  text into the evidence base.
- Rejected or unverified content remains in the Research Record and cannot affect future
  evidence retrieval as established knowledge.

#### Existing Capability Reuse

| Need | Existing capability | Phase 6 action |
|---|---|---|
| real literature substrate | `raw/papers/`, source schemas, source-depth maps | preserve as authoritative base |
| source quality distinction | source family, claim-fit, extraction depth, verification, decision grade, species boundary | expose relevant dimensions, do not invent one composite score |
| query evaluation | `TaskEvaluator` | show interpreted task and intended depth |
| actual retrieval trace | query result `research_trace`, loaded paths and source IDs | render factual scope from observed events |
| durable record model | `core.schemas.ResearchRecord` | extend compatibly only where observed fields are missing |
| JSON/Markdown persistence | `core.record_store.RecordStore` | retain dual-write behavior |
| automatic run capture | `HarnessLoop.process_query_result()` | change product behavior to explicit user consolidation |
| record browser | `scripts/research_record_ui.py` | add preview, status, continuation, and promotion entry |
| source presentation | `SourceDisplay`, shared metadata resolver | add optional metadata without requiring unavailable fields |
| existing promotion precedent | deep-extraction promotion checks, write-back template, artifact review queue | reuse status and review concepts without reusing business-artifact semantics blindly |

The shared metadata resolver produces one raw `SourceSnapshot`:

```text
SourceSnapshot
├── source_id + content_fingerprint
├── title + canonical identifiers
├── source_family + study_type
├── species + applicability boundary
├── extraction_depth + verification_status
├── safe_claim_types + prohibited_claim_types
├── decision_grade + limitations
└── supersession state
```

Presentation translates the snapshot into user-facing labels. Promotion validation,
fingerprinting, and stale detection consume the same raw snapshot.

#### Source Quality Presentation

The interface must not flatten source quality into one badge. It should expose the
dimensions already present in the repository:

1. source family / study type;
2. species and applicability boundary;
3. extraction depth;
4. verification status;
5. claim-fit / safest use;
6. decision grade and known limitations.

Publication year, DOI, PMID, PMCID, authors, journal, and tags are metadata, not quality
scores. Missing metadata remains explicitly unavailable.

#### Research Answer Pattern

```text
Query interpretation
  ↓
Actual retrieval scope
  ↓
Primary answer with claim-linked citations
  ↓
Evidence cards with metadata + quality dimensions + safest use
  ↓
Quick take: evidence branches, agreements, tensions, and gaps
  ↓
Specific next research moves
  ↓
Optional "沉淀这次研究"
```

The Quick Take is built deterministically from source tags, evidence family, provenance,
limitations, and retrieval trace in V1. LLM-authored clustering or value judgments may be
added later only when they are labeled as generated interpretation and covered by tests.

#### Phase 6 Information Hierarchy

The answer remains the primary object. Research mechanics are available without forcing
the user through an audit screen before reading:

```text
1. direct answer and decision boundary
2. claim-linked evidence
3. Quick Take: branches, tensions, gaps
4. specific next research moves
5. collapsed retrieval scope and full source metadata
6. optional consolidation command
```

Each source row shows title, safest use, and evidence depth by default. Source family,
species boundary, verification, claim-fit details, decision grade, identifiers, and
limitations remain keyboard-expandable. This preserves the six dimensions without
turning every answer into a metadata wall.

#### Consolidation Interaction

The command appears after next research moves only when the run contains substantive
research work. It uses an inline preview, not a modal:

```text
[沉淀这次研究]
        │
        ▼
inline preview
├── question and editable record title
├── actual retrieval scope
├── evidence selected and excluded
├── answer summary
├── decisions and uncertainties
├── next research objective
├── duplicate / existing-version notice
└── "仅保存研究记录，不写入知识库"
        │
        ├── Save Research Record
        ├── Continue Existing
        ├── Save New Version
        └── Cancel
```

Saving shows the record ID and two next actions: View Record and Continue Research. It
does not immediately present a promotion action. Promotion starts from the saved record
after the user has reviewed what was preserved.

#### Promotion Interaction

```text
saved Research Record
  → select individual claims
  → inspect linked sources and boundaries
  → choose target page
  → run promotion validation
      ├── blocked: show exact failed checks and recovery action
      └── passed: show read-only patch preview
  → explicit Apply Patch confirmation
  → promoted or stale-review state
```

Answer verification and promotion validation use separate labels and separate sections.
The UI must never imply that "Answer passed" means "Safe to publish."

#### Phase 6 Interaction States

| State | Trigger | User sees | Recovery |
|---|---|---|---|
| consolidation unavailable | quick or empty run with no user-added value | no save prompt | add decision, annotation, or follow-up |
| preview ready | user chooses consolidate | inline complete preview and knowledge-boundary notice | save, continue existing, new version, cancel |
| duplicate detected | equivalent question, evidence, and answer hash | existing record and timestamp | continue existing or explicitly save version |
| unsaved navigation | preview has edits and user changes workspace | unsaved-state warning | stay or discard |
| save in progress | write started | disabled primary command and named status | wait; no double submit |
| JSON written, Markdown failed | partial dual-write failure | save reported incomplete, record not shown as healthy | retry reconciliation |
| saved | both representations committed | record ID, View and Continue actions | open record |
| claim not selectable | inference-only or missing source mapping | disabled selection with reason | improve evidence mapping |
| validation running | claim checks executing | per-check progress | wait or cancel before patch generation |
| validation blocked | source/depth/species/claim-fit check fails | failed checks, no Apply action | repair source or edit claim |
| draft ready | all promotion checks pass | read-only target diff | apply or reject |
| source changed | manifest fingerprint differs | stale label and affected claim list | revalidate |
| promoted | patch applied and recorded | target reference and timestamp | inspect target or continue research |

At 320px, source dimensions use stacked label-value rows and commands remain full-width.
The claim text appears before check results. No horizontal comparison table is required
for the save or promotion flows.

#### Phase 6 Implementation Steps

**6.1. Make retrieval scope truthful**

- Add a versioned `RetrievalEvent` schema derived only from actual search and load events:
  engine, query, scope, candidate count, retained IDs, excluded IDs and reasons, filters,
  load outcome, and timestamp.
- Show source families searched, result counts, retained counts, exclusions, filters,
  and retrieval depth when observed.
- Use "not recorded" for unknown fields. Never claim PubMed or external search occurred
  when the run used only the local vault.
- Persist the raw events in the Research Record and derive the visible scope summary from
  those events. Do not parse human-readable trace strings back into data.

**6.2. Extend source presentation compatibly**

- Add optional `authors`, `journal`, `pmcid`, `pmid`, `doi`, `publish_date`, and tags.
- Display only available metadata.
- Add the six existing quality/claim-fit dimensions where data exists.
- Add a deterministic "safest use" annotation from source family and claim-fit policy.
- Keep generated, question-specific research value judgment out of V1.
- Run a metadata consistency audit before allowing promotion. Conflicting depth,
  verification, species, claim-fit, or decision-grade states block promotion and enter
  a review queue.

**6.3. Build deterministic Quick Take and next moves**

- Group sources by evidence family, disease branch, use case, and limitations.
- Report convergence only when multiple source cards support the same explicit branch.
- Report tensions from existing conflict/boundary data, not semantic invention.
- Generate next moves from missing evidence families, shallow extraction, unresolved
  verifier findings, and unexplored retrieval branches.

**6.4. Convert automatic capture into explicit consolidation**

- Stop treating every completed query as user-approved knowledge work.
- Refactor `HarnessLoop.process_query_result()` into a pure finalization step that returns
  a fully populated transient Research Record without file I/O.
- Keep that transient record in `st.session_state`.
- Add a preview with Save, Edit title/summary, and Cancel actions.
- Only the confirmed Save action may call `RecordStore.save()`.
- Preserve verification failures and uncertainties in the saved record.
- Detect equivalent records by normalized question, selected evidence, and answer hash.
  Offer Continue Existing or Save New Version instead of silently duplicating records.
- Do not prompt to preserve routine quick explanations unless the user adds a decision,
  annotation, unresolved question, or follow-up objective.

**6.5. Add the promotion gate**

- Add promotion status: `record_only | candidate | validated | promoted | rejected`.
- Add independent freshness status: `current | stale | superseded`.
- Add selected `ResearchClaim` objects with source provenance and target page.
- Validate source existence, evidence depth, claim-fit, species boundary, and verifier
  results before generating a patch. Answer-level `verifier_status` is context only.
- Require human confirmation before applying the patch.
- Record promotion timestamp, target, and resulting commit or file reference.
- Write a promotion manifest containing claim ID, source IDs, source fingerprints,
  target location, validation-policy version, and timestamp.
- When a source changes or becomes superseded, mark dependent promoted claims stale and
  add them to a review queue.
- Compare canonical SHA-256 source fingerprints before every promotion view and every
  validated-claim retrieval. Stale claims leave synthesis results immediately.

**6.6. Reuse validated records in future research**

- Search saved records as prior-work context, not as primary evidence.
- Only `validated` or `promoted` claims may enter synthesis context as reusable findings.
- `record_only` and `candidate` records may be shown as prior work with a clear unverified
  label, but cannot control factual conclusions.
- Source cards cited by prior records are reloaded from the current evidence base so
  later corrections and supersession remain effective.
- Keep two retrieval channels: whole Research Records for workflow continuity, and a
  validated-claim index for factual synthesis. Never inject an entire saved answer as
  evidence.
- Existing `RecordStore.search()` and `get_related()` are workflow-context APIs only.
  Add a separate `ValidatedClaimStore.query_validated_claims()` for synthesis.

#### Phase 6 Delivery Gates

**6A, truthful presentation and explicit consolidation**

- versioned retrieval events and visible scope;
- compatible source metadata and six-dimension display;
- deterministic Quick Take and gap-specific next moves;
- transient record preview, duplicate handling, explicit Save or Cancel;
- no promotion or factual reuse yet.

**6B, claim selection and validation drafts**

- structured `ResearchClaim`;
- claim selection from saved records;
- independent promotion validation;
- target selection and reviewable draft generation;
- no automatic file changes.

**6C, promotion and validated reuse**

- human-confirmed patch application;
- promotion manifest and stale-dependency queue;
- validated-claim retrieval channel;
- later-run reuse with current source-card revalidation.

6B starts only after three distinct 6A tasks are saved and at least one is reopened or
continued. 6C starts only after claim-validation fixtures pass and a human approves at
least one generated promotion draft.

#### Persistence And Compatibility

- Add `schema_version` to Research Record JSON.
- New fields use additive defaults so the three existing v1 records remain readable.
- Add `title`, `parent_record_id`, `record_version`, `retrieval_events`,
  `research_claims`, and persistence health metadata without changing the meaning of
  `verifier_status`.
- Save JSON and Markdown to temporary files, flush and fsync both, atomically replace
  both destinations, then atomically write a commit manifest containing both hashes.
- Record listing and retrieval trust only records whose commit manifest validates.
- Interrupted saves appear in a reconciliation queue and never as healthy records.
- Reuse the locking, path containment, schema migration, and atomic-write patterns from
  `scripts/research_case_store.py`.

#### Minimal Implementation Order

```text
1. schema version + backward-compatible migrations
2. RetrievalEvent and SourceSnapshot
3. pure harness finalization with zero persistence
4. atomic RecordStore + commit manifest + reconciliation
5. explicit-save UI + duplicate/version handling
6. ResearchClaim creation and serialization
7. claim-level promotion validator + draft generation
8. source fingerprints + stale queue
9. ValidatedClaimStore + synthesis channel isolation
10. human-confirmed patch application
```

No step may depend on a later step for correctness. In particular, 6A ships without
promotion code, and 6B produces drafts without applying them.

#### Adoption Metrics

- substantive-run save rate;
- duplicate avoidance rate;
- saved-record reopen or continue rate;
- promotion-candidate rate;
- validated promotion rate;
- later research runs that reuse a validated claim;
- time saved compared with reconstructing the same context.

#### Phase 6 Success Criteria

1. A user can inspect the actual query interpretation, retrieval scope, selected evidence,
   quality dimensions, limitations, and next moves.
2. Local-only runs never claim external database retrieval.
3. Missing metadata is omitted or labeled unavailable, never fabricated.
4. Completing a query does not silently publish it into the durable knowledge base.
5. A user can preview and explicitly save a Research Record.
6. Saving a record cannot modify source, topic, index, or synthesis files.
7. Promotion requires source-linked claims, validation, target selection, and explicit
   human confirmation.
8. Only validated or promoted claims can be reused as knowledge in later synthesis.
9. A roundtrip test proves question → result → saved record → promotion candidate →
   validated draft → later retrieval with current source cards.
10. Three distinct research tasks complete the flow: quick explanation, evidence check,
    and deep protocol/endpoint task.
11. Quick-answer `verifier_status=passed` never makes a claim promotion-eligible.
12. Duplicate runs do not create duplicate records without an explicit Save New Version
    choice.
13. A changed or superseded source marks dependent promoted claims stale.
14. Whole saved answers are never injected into factual synthesis as evidence.

#### Phase 6 Architecture

```text
query result
    │
    ├── answer + exact provenance spans
    ├── RetrievalEvent[]
    └── SourceSnapshot[]
            │
            ▼
pure HarnessLoop.finalize_record()
            │
            ▼
transient ResearchRecord in session
    │                    │
    │ Cancel             │ explicit Save
    ▼                    ▼
discard             atomic RecordStore
                          │
                          ▼
              workflow-context retrieval
                          │
                          ▼
                claim selection in 6B
                          │
                          ▼
              PromotionValidator
                │               │
                │ blocked       │ passed
                ▼               ▼
          repair guidance   reviewable draft
                                  │
                                  ▼ human confirm
                         promotion manifest
                                  │
                                  ▼
                        ValidatedClaimStore
                                  │
                                  ▼
                     factual synthesis context
```

#### Phase 6 Test Diagram

```text
SCHEMA AND STORE
├── legacy v1 record → migrate with additive defaults
├── future schema version → reject explicitly
├── save JSON + Markdown + manifest → all hashes valid
├── crash after one temp write → no healthy record listed
├── crash between replacements → reconciliation entry
├── concurrent save/version attempt → lock or version conflict
└── path outside record root → reject

EXPLICIT CONSOLIDATION
├── query completes → zero record files written
├── transient preview → exact question, trace, evidence, checks
├── Cancel → session draft cleared, zero persistence
├── double-click Save → one record/version
├── equivalent record → Continue Existing / Save New Version
└── successful Save → record ID + valid dual representation

CLAIM PROMOTION
├── supported claim + exact sources → selectable
├── inference-only claim → disabled
├── missing source mapping → disabled
├── title-only or conflicting source state → validation blocked
├── answer verifier passed but claim validator failed → no draft
├── valid claim → read-only target diff
├── target outside allowlist → reject
├── no human confirmation → no file mutation
└── confirmed patch → manifest records claim, sources, target, hashes

STALE AND RETRIEVAL
├── current fingerprints → validated claim returned
├── source content changed → claim stale and excluded
├── source superseded → claim superseded and excluded
├── workflow record search → labeled context only
└── factual synthesis → ValidatedClaimStore only

PRESENTATION
├── local-only trace → no external-search claim
├── unknown trace field → "not recorded"
├── partial source metadata → available fields only
├── six dimensions → compact default + keyboard expansion
└── 320px → stacked metadata and full-width commands
```

Required test files:

- extend `core/test_harness_loop.py` for pure finalization and verifier separation;
- add `scripts/test_research_record_store.py` for migrations, atomic writes, manifests,
  reconciliation, locking, duplicate versions, and path containment;
- extend `scripts/test_result_presentation.py` for truthful retrieval scope, source
  snapshots, six-dimension disclosure, and responsive visible-token checks;
- add `scripts/test_research_claim_promotion.py` for selection, validation, target
  allowlisting, draft-only behavior, fingerprints, stale exclusion, and channel isolation;
- add one Streamlit integration fixture for preview, Cancel, Save, duplicate, and
  validation-blocked user flows.

## Test Diagram

```text
NEW UX FLOWS
├── query → evidence profile → answer → claim-linked source → next action
├── overview → quick answer → explore card → source details
└── ranking → tier legend → intervention → comparison → boundary

NEW DATA FLOWS
├── source ID → source card → canonical link → SourceDisplay
├── provenance tags + source depth → factual evidence profile
└── answer payload → validated ResultPresentation → Streamlit adapter

NEW BRANCHES
├── automated / human-reviewed authority
├── direct / synthesis / inference evidence profile
├── direct / limited / title-only source depth
├── linked / unlinked source
├── trace present / absent
├── Chinese / English / missing translation
└── feature flag old / new renderer

ERROR PATHS
├── unknown source ID
├── malformed frontmatter
├── missing DOI and PMID
├── empty answer
├── malformed provenance tag
└── partial source metadata
```

### Required Tests

| Area | Test type | Required coverage |
|---|---|---|
| label translation | unit | every known and unknown internal status |
| evidence profile | unit | zero claims, mixed inference, thin sources, contradictions |
| source resolver | unit | DOI, PMID, URL fallback, no-link fallback, duplicates |
| presentation validation | unit | nil, empty, malformed and partial inputs |
| three adapters | unit/snapshot | correct section order and default visibility |
| Streamlit query path | integration | old/new flag, figures, review loop, trace |
| responsive prototype | visual | 320px, 768px, 1440px |
| accessibility | automated/manual | headings, focus order, contrast, keyboard use |
| ordinary-user language | acceptance | no internal IDs or raw statuses in default view |
| professional inspection | acceptance | exact metadata remains reachable in expanded view |

Test commands should use the repository's existing `unittest` pattern unless a test
runner is added separately. No new framework is required.

## Error And Rescue Registry

| Codepath | Failure | Rescue | User sees |
|---|---|---|---|
| source display resolver | source card not found | keep title if available; mark metadata unavailable | readable source row, no broken link |
| canonical link resolver | DOI/PMID malformed | omit anchor and log source ID | "link unavailable" |
| provenance parser | unknown tag | render safe plain text and record warning | answer remains readable |
| evidence profile builder | zero valid claims | return empty factual profile | "evidence profile unavailable" |
| presentation builder | answer empty | return named error state | retry/deeper research action |
| adapter | optional section absent | omit section, preserve order | no blank card |
| new renderer | unexpected exception | feature-flag fallback to legacy renderer with log | answer still appears |

## Failure Modes Registry

| Failure mode | Severity | Prevention |
|---|---|---|
| evidence profile is mistaken for human review | critical | explicit automated/human-reviewed authority state |
| title-only records appear as supporting evidence | critical | discovery-only label and exclusion from support count |
| internal IDs leak to ordinary users | high | acceptance test scans rendered default view |
| missing source link renders a dead control | medium | explicit unlinked source state |
| long answers hide the actual conclusion | high | lead required before detail sections |
| mobile comparison table overflows | medium | stacked mobile representation |
| color-only tier meaning fails accessibility | high | text labels and icons accompany color |
| feature flag produces two inconsistent contracts | medium | same pure presentation model feeds both paths during rollout |

## Rollout And Rollback

- Roll out only the Ask the Vault adapter first.
- Keep the legacy rendering branch behind a local feature flag.
- Capture before/after screenshots for the three approved fixtures.
- Roll back by disabling the flag; no data migration is involved.
- Remove the legacy branch only after acceptance tests and manual review pass.

## Success Criteria

1. The three manual samples are approved and represented in the reusable skill.
2. Default user views contain zero `src-*` identifiers and zero raw verification-status
   values.
3. Every displayed source has a paper title and either a canonical link or an explicit
   unavailable-link state.
4. No global answer-level confidence is shown without validated grading semantics.
5. Evidence profiles expose provenance, source depth, contradiction, gaps, and authority
   state as separate facts.
6. All State Matrix rows have an implementation path and test.
7. The first pilot passes unit, integration, responsive, accessibility,
   ordinary-user, and professional-reader acceptance checks.
8. Rollback requires only disabling the feature flag.

## Not In Scope

- visual rebrand, light mode, serif typography, illustrations, or ii.inc cloning;
- consolidating all 30+ render functions;
- changing evidence grading or source verification semantics;
- changing retrieval, LLM prompts, or paid API behavior;
- migrating all topic pages in one pass;
- new database or frontend framework;
- redesigning Research Cases (Research Records ARE in scope for Phase 6).

## Deferred

- analytics comparing expansion behavior and source-card clicks;
- saved user preferences for collapsed sections;
- a component gallery beyond the three approved fixtures;
- automated screenshot regression infrastructure for every topic page.

## Decision Audit Trail

| # | Phase | Decision | Classification | Principle | Rationale | Rejected |
|---|---|---|---|---|---|---|
| 1 | Intake | presentation logic over visual rebrand | user-confirmed | explicit over clever | current instruction and handoffs state the priority | ii.inc visual clone |
| 2 | Intake | shared contract plus three adapters | auto-decided | DRY + completeness | reuse evidence semantics without forcing different reading jobs into one renderer | independent patches; universal renderer |
| 3 | Intake | keep existing design system | user-confirmed | reuse existing | `DESIGN.md` is authoritative | light/serif redesign |
| 4 | Intake | titles and canonical links in default UI | user-confirmed | user outcome | internal IDs are not meaningful to readers | `src-*` citations |
| 5 | Intake | pure model builders before Streamlit rendering | auto-decided | testability | enables complete branch testing without browser automation | render-only logic |
| 6 | Intake | Ask the Vault first, static pages second | auto-decided | reversible rollout | highest-value dynamic surface with feature-flag rollback | global migration |
| 7 | CEO | reject global answer-level confidence in V1 | user challenge | authority safety | both independent reviewers found current semantics insufficient | prominent high/medium/low badge |
| 8 | CEO | center claim-to-evidence boundaries | user challenge | product differentiation | claim traceability is the repository's defensible capability | generic answer card hierarchy |
| 9 | Design | trust summary position inconsistent | auto-decided | explicit over clever | Overview buries trust, Ask the Vault leads with it; pick one principle | inconsistent placement |
| 10 | Design | missing claim-level structure in contract | taste | completeness | Codex recommends claims[] as central unit; Claude agrees boundaries should be claim-adjacent | aggregate-only evidence_profile |
| 11 | Design | state matrix shallow not designed | auto-decided | completeness | both reviewers found states named but interactions undefined | aspirational states |
| 12 | Design | accessibility aspirational not measurable | auto-decided | completeness | need contrast ratios, focus order, live regions as acceptance criteria | principle-only a11y |
| 13 | Eng | nil vs empty handling undefined | auto-decided | completeness | evidence=None vs evidence={source_cards:[]} not distinguished | implicit handling |
| 14 | Eng | contradiction_count is new AI feature | auto-decided | scope control | detection logic does not exist; remove from V1 | scope creep |
| 15 | Eng | source resolution O(n) network latency | auto-decided | performance | 100+ sources causes timeout; cap to 20 with show-more | unbounded resolution |
| 16 | Eng | acceptance test for internal ID leakage | auto-decided | completeness | most important test; regex scan rendered HTML | missing critical test |
| 17 | Phase 5 | separate source counts from claim provenance counts | auto-decided | explicit over clever | factual profile cannot label claim tags as papers | overloaded count fields |
| 18 | Phase 5 | preserve unknown verification as unknown | auto-decided | authority safety | missing metadata cannot be upgraded to abstract evidence | abstract fallback |
| 19 | Phase 5 | use one pure source metadata resolver | auto-decided | DRY | Ask the Vault and static pages must resolve DOI, PMID, and URL identically | duplicate loaders |
| 20 | Phase 5 | build two strict static adapters | auto-decided | explicit over clever | overview and ranked pages have different required shapes | generic Markdown parser |
| 21 | Phase 5 | require supported-use and overclaim boundaries for every ranked item | auto-decided | completeness | ranking without both boundaries is unsafe to reuse | optional boundaries |
| 22 | Phase 5 | render deterministic standalone HTML through a CLI | auto-decided | bias toward action | adapters need an actual invocation path and reviewable artifact | dead library code |
| 23 | Phase 5 | retain feature flag until protected live acceptance | auto-decided | reversible rollout | static acceptance does not prove the paid dynamic path | premature legacy removal |
| 24 | Phase 6 | adopt II-Commons detailed presentation pattern | user-confirmed | completeness | raw-2.md reference shows fuller metadata, research value judgments, and domain maps build professional trust | minimal presentation |
| 25 | Phase 6 | add Research Record consolidation | user-confirmed | knowledge accumulation | CommonGround Kernel pattern preserves request, scope, sources, decision, output, next_moves, handoff | ephemeral sessions |
| 26 | Phase 6 | treat presentation, research execution, and knowledge accumulation as one flywheel | user-confirmed | product coherence | detailed evidence presentation guides research and produces better candidates for later reuse | presentation-only framing |
| 27 | Phase 6 | use two-stage preservation: save record, then validate and promote selected knowledge | user-confirmed | authority safety + knowledge compounding | preserves useful work without allowing generated text to become evidence automatically | direct write-back; record-only archive |
| 28 | Phase 6 | reuse the existing Research Record model and store | auto-decided | DRY | the repository already has schema, JSON/Markdown persistence, browser UI, and three saved records | create a second record system |
| 29 | Phase 6 | expose six existing quality and claim-fit dimensions instead of one composite score | auto-decided | explicit over clever | source family, species, depth, verification, claim-fit, and decision boundary answer different questions | single quality badge |
| 30 | Phase 6 | keep question-specific LLM value judgments out of V1 | auto-decided | authority safety | deterministic safest-use annotations already follow source policy and do not require paid generation | unvalidated generated annotations |
| 31 | Phase 6 | build V1 Quick Take from explicit tags, source families, boundaries, and trace | auto-decided | explicit over clever | existing structured data can support a truthful map without an unspecified clustering model | aspirational LLM domain map |
| 32 | Phase 6 CEO re-review | make `ResearchClaim` the unit of selection, validation, promotion, and factual reuse | auto-decided | authority safety | whole answers and sections can mix supported and unsupported statements | section-level promotion |
| 33 | Phase 6 CEO re-review | separate answer verification from promotion validation | auto-decided | explicit over clever | current quick answers can pass without claim-level entailment checks | reuse `verifier_status` as promotion permission |
| 34 | Phase 6 CEO re-review | split delivery into 6A, 6B, and 6C gates | auto-decided | pragmatic + reversibility | isolates presentation adoption from claim promotion and retrieval-memory risks | one large Phase 6 release |
| 35 | Phase 6 CEO re-review | maintain separate workflow-record and validated-claim retrieval channels | auto-decided | authority safety | whole generated answers are useful context but are not evidence | one mixed memory index |
| 36 | Phase 6 Eng re-review | make harness finalization pure and persistence user-triggered | auto-decided | explicit over clever | a UI button is not a real save boundary while `process_query_result()` still writes | automatic persistence behind explicit-looking UI |
| 37 | Phase 6 Eng re-review | use atomic dual-write plus a commit manifest | auto-decided | completeness | JSON-first writes can expose records whose Markdown representation failed | best-effort sequential writes |
| 38 | Phase 6 Eng re-review | add schema versioning and v1 migration before new record fields | auto-decided | reversibility | three existing records must remain readable as the model grows | unversioned additive assumptions |
| 39 | Phase 6 Eng re-review | derive display and validation from one raw `SourceSnapshot` | auto-decided | DRY | separate metadata interpretations create authority drift | translated presentation model as validation input |
| 40 | Phase 6 Eng re-review | track promotion state and freshness state independently | auto-decided | explicit over clever | a promoted claim can later become stale without ceasing to have promotion history | one overloaded status enum |

## GSTACK REVIEW REPORT

| Review | Status | Notes |
|---|---|---|
| CEO Review | USER_CHALLENGE | both voices reject global confidence and recommend a claim/decision pilot |
| Design Review | ISSUES_FOUND | Claude: 18 findings, Codex: 7 findings; 7/7 consensus on structural issues |
| Eng Review | ISSUES_FOUND | Claude: 15 findings (4 critical); Codex unavailable (usage limit) |

### Design Review Consensus (2026-06-11)

Both reviewers independently identified:
1. **Trust summary should be removed from V1** - renamed confidence badge still present
2. **Missing claim-level structure** - `claims[]` should be central, not aggregate counts
3. **State matrix is shallow** - states named but interactions undefined
4. **Responsive/accessibility aspirational** - need measurable criteria

### Eng Review Summary (2026-06-11, subagent-only)

Critical blockers before implementation:
1. Define explicit None vs empty handling with validate() method
2. Add acceptance test scanning for `src-*` patterns in rendered output
3. Remove contradiction_count and unresolved_gap_count from V1 (no detection logic)
4. Cap source_cards resolution to 20 with "show more" action

### Phase 6 /autoplan Review (2026-06-12, subagent-only)

**CEO Review (8 findings):**

| # | Finding | Severity | Recommended Fix |
|---|---------|----------|-----------------|
| 1 | Presentation polish on unused system | Critical | Require 5 complete research cases before Phase 6 |
| 2 | II-Commons is retrieval, not presentation | High | Gate presentation on retrieval quality |
| 3 | Research Record has no adoption path | High | Define save trigger, staleness, re-retrieval |
| 4 | 6-month regret scenario is obvious | High | Define user success metric |
| 5 | Claim Evidence Workbench was dismissed | High | Reconsider narrow wedge first |
| 6 | Competitive risk misframed | Medium | Name scenario where GPT-5 obsoletes this |
| 7 | More metadata is not better judgment | Medium | Cut cosmetic fields |
| 8 | No acceptance criteria for Phase 6 | Medium | Define 3 test queries |

**Design Review (18 findings, 4 critical):**

| # | Finding | Severity |
|---|---------|----------|
| 1 | Hierarchy collision between existing and Phase 6 patterns | Critical |
| 4 | Research Record save flow has no state definitions | Critical |
| 10 | Source card layout unspecified | Critical |
| 15 | "Saved records appear in retrieval" is ambiguous | Critical |
| 2 | Research value judgment placement undefined | High |
| 7 | Domain map generation states missing | High |
| 8 | No emotional arc for Research Record flow | High |
| 9 | Ordinary vs professional audience rules missing | High |
| 12 | Research Record preview content unspecified | High |
| 17 | Mobile treatment of enhanced source cards | High |
| 18 | Research value judgment generation prompt undefined | High |

**Eng Review (18 findings, 4 critical):**

| # | Finding | Severity |
|---|---------|----------|
| A-1 | Research Record index consistency | Critical |
| A-3 | Research value judgment generation undefined | Critical |
| T-1 | No Research Record roundtrip test | Critical |
| H-1 | ResearchRecord schema incomplete | Critical |
| A-2 | SourceDisplay breaking schema change | High |
| A-4 | Domain map aspirational (no algorithm) | High |
| E-1 | O(N) file reads at scale | High |
| T-2 | Retrieval scope accuracy untested | High |
| H-2 | Bilingual handling for new fields | High |

**Cross-Phase Themes:**

Both CEO and Eng independently flagged:
- **Research Record has no adoption path** (CEO #3, Eng A-1, H-1)
- **Research value judgment undefined** (Eng A-3, Design #18)
- **Domain map is aspirational** (Eng A-4, Design #7)

All three reviews converge: Phase 6 as specified is too ambitious. Recommend scoping down.

### Phase 6 /autoplan Re-review After Product Confirmation (2026-06-12)

This section supersedes the Phase 6 conclusion immediately above without deleting its
audit history. The earlier conclusion assumed that Research Record did not yet exist and
treated detailed presentation as an isolated UI project. Repository inspection and the
user-confirmed product model changed both premises:

- `ResearchRecord`, `RecordStore`, the record browser, automatic harness persistence,
  and saved fixtures already exist;
- the product is an evidence-to-judgment-to-validated-knowledge flywheel, not a
  presentation-only surface;
- the approved preservation model is A: save a work record first, then separately
  validate and promote selected claims.

#### Final Review Consensus

| Review | Revised status | Resolution |
|---|---|---|
| CEO | APPROVED_WITH_GATES | make `ResearchClaim` the reusable unit; never promote whole generated answers |
| Design | APPROVED_WITH_FALLBACK | answer first, six dimensions on demand, explicit save and promotion states |
| Engineering | APPROVED_WITH_GATES | pure finalization, atomic persistence, schema migration, separate retrieval channels |
| Product | USER_CONFIRMED | two-stage preservation is the intended compounding mechanism |

The executable scope is therefore not "all of Phase 6 at once." It is the gated sequence
6A -> 6B -> 6C. Each gate has its own adoption and safety proof, and later gates do not
ship merely because earlier presentation work is complete.

#### Cross-Phase Themes

1. **Evidence is the authority layer.** A generated answer or saved record never becomes
   a source merely by being useful or verified as an answer.
2. **Claims are the reuse boundary.** Selection, provenance, validation, promotion,
   freshness, and retrieval all operate on `ResearchClaim`.
3. **Presentation is part of research control.** The six dimensions explain what a
   source can support and where it must not be used.
4. **Accumulation must remain deliberate.** Saving preserves work context; promotion
   changes the validated knowledge layer and therefore requires a separate human action.
5. **Unknown stays unknown.** Missing publication metadata and unresolved quality fields
   are shown as unavailable, never inferred into higher authority.
6. **Adoption precedes automation.** Generated research-value judgments and semantic
   domain clustering remain deferred until saved records and reopen/continue behavior
   demonstrate actual use.

#### Design Litmus Scorecard

Scores describe plan readiness after the revisions above, not implemented UI quality.

| Dimension | Score | Basis |
|---|---:|---|
| information hierarchy | 5/5 | answer first; audit and six dimensions progressively disclosed |
| workflow clarity | 5/5 | save and promotion are separate, named actions |
| interaction states | 5/5 | duplicate, partial write, blocked validation, stale, and recovery states specified |
| domain fit | 5/5 | evidence depth, species boundary, claim-fit, and limitations remain visible |
| responsive behavior | 4/5 | 320px stacking specified; visual implementation still requires screenshot QA |
| accessibility | 4/5 | keyboard expansion and non-color semantics specified; implementation audit remains |
| visual-system consistency | 4/5 | existing `DESIGN.md` remains authoritative; AI mockup was unavailable |

#### Completion Summaries

**CEO:** The revised plan protects the core product thesis: real literature remains the
authority layer, while useful research work can compound through deliberate
consolidation and claim-level promotion. The critical product risk, generated answers
quietly becoming evidence, is blocked by separate stores, validators, and retrieval
channels.

**Design:** The experience now leads with the answer, exposes source quality only as
needed, and gives explicit save, duplicate, validation, promotion, and stale states. The
failed AI mockup call does not leave an interaction-design gap, but responsive and
accessibility scores cannot reach 5/5 before implementation QA.

**Engineering:** The plan reuses the existing Research Record system and adds the missing
boundaries: pure finalization, schema migration, atomic dual representation, exact-span
claims, source fingerprints, target containment, and validated-only factual retrieval.
The implementation can start at 6A without depending on unfinished 6B or 6C code.

#### Phase 6 Error And Rescue Registry

| Codepath | Failure | Rescue | User-visible result |
|---|---|---|---|
| session finalization | transient record lost after rerun | retain serializable draft in session and expose retry | unsaved state remains explicit |
| harness | record written before user chooses save | remove persistence from finalization; save only through store command | no hidden archive entry |
| record store | JSON succeeds but Markdown or manifest fails | temp writes, `fsync`, atomic replace, reconciliation on next open | record remains pending or recoverable |
| record save | duplicate task saved repeatedly | fingerprint request, scope, source set, and answer; offer reopen or new version | no silent duplicate |
| promotion target | invalid namespace or path traversal | target allowlist plus path-containment validation | promotion blocked with named validation error |
| source refresh | promoted claim references changed source | compare SHA-256 fingerprints and queue stale review | claim remains historically promoted but excluded from fresh retrieval |
| retrieval | whole generated answer enters factual context | physically separate workflow-record and validated-claim APIs | only validated claims enter factual synthesis |
| claim selection | claim mixes sourced statement and inference | require exact answer span and source mapping; disable promotion until split | user is asked to narrow the claim |
| metadata resolver | source card and identifier metadata conflict | retain raw values, flag conflict, do not auto-upgrade quality | conflict shown as unresolved |
| promotion validation | validator errors or times out | keep draft and validation log; no status advancement | retry remains available without data loss |

#### Phase 6 Failure Modes Registry

| Failure mode | Severity | Prevention |
|---|---|---|
| answer verification is treated as promotion approval | critical | separate validator, status field, API, and tests |
| saved generated text is retrieved as evidence | critical | separate stores and retrieval channels |
| unsupported clause is hidden inside a promoted paragraph | critical | exact-span `ResearchClaim` and one-claim validation |
| stale source silently continues supporting decisions | critical | source fingerprints, freshness state, stale exclusion |
| explicit Save UI still triggers automatic background writes | high | pure `process_query_result()` contract and zero-write test |
| interrupted dual-write creates mismatched record views | high | atomic JSON/Markdown/manifest commit and reconciliation |
| six dimensions collapse into a misleading score | high | preserve dimensions independently and disclose unknowns |
| duplicate records create false evidence of adoption | medium | deterministic duplicate detection and version relationship |
| missing author, journal, or date is fabricated | high | optional metadata contract and unavailable state |
| a promoted target escapes its approved namespace | critical | allowlist and path-containment checks |

#### Final Autoplan Decision

`READY_FOR_GATED_IMPLEMENTATION`.

- Start with Gate 6A only.
- Enter Gate 6B after three distinct saved research tasks and one successful
  reopen/continue workflow.
- Enter Gate 6C only after claim-validation fixtures pass and a human explicitly
  approves at least one promotion draft.
- The protected live Ask the Vault acceptance remains a separate operational blocker:
  do not incur paid OpenRouter usage until the dashboard `$1/day` cap is confirmed.
- The unavailable AI design mockup is not a planning blocker; the textual hierarchy,
  interaction states, responsive rules, and acceptance criteria are authoritative.

Test-plan artifact:
`/Users/jiawei/.gstack/projects/feline-research-os/jiawei-idea-chatacademia-research-workbench-test-plan-20260612-101522.md`
