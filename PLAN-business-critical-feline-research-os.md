<!-- /autoplan restore point: /Users/jiawei/.gstack/projects/feline-research-os/idea-chatacademia-research-workbench-autoplan-restore-20260606-154819.md -->

# Business-Critical Plan: Feline Research OS

Date: 2026-06-04
Branch: idea-chatacademia-research-workbench
Status: reviewed plan, not yet implemented

## Trigger

The user clarified that the goal is not just better CKD answers.

The goal is for `feline-research-os` to materially advance the business, not become a nice-to-have research toy.

## One-Line Strategy

Turn `feline-research-os` from an evidence vault into a decision workbench for feline therapeutics, diagnostics, nutrition, and regulatory strategy.

If a weekly user session does not produce a clearer decision, it failed.

## External Signal

Current market/research signals support the direction, but also warn against generic AI chat:

- FDA CVM emphasizes animal drugs still need safety/effectiveness evidence, while allowing different evidence routes, including literature/meta-analysis in some cases. Source: https://www.fda.gov/animal-veterinary/animal-health-literacy/innovation-animal-drug-development
- Veterinary oncology AI reviews point to data readiness, clinical translation, and annotated datasets as bottlenecks, not just model generation. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12817679/
- Veterinary oncology data-management literature explicitly frames AI value around data synthesis, decision support, and treatment planning, while noting fragmented clinical data and workflow complexity. Source: https://veterinaryoncology.biomedcentral.com/articles/10.1186/s44356-025-00043-2
- Veterinary software market growth is driven by AI, telehealth, imaging, and rising animal disease volume, but this is a crowded broad-software category. Source: https://www.grandviewresearch.com/industry-analysis/veterinary-software-market

Conclusion:

Do not build another broad pet health chatbot.

Build the boring thing that actually matters: evidence-to-decision infrastructure for companion animal R&D and translational strategy.

## Business User Segments

### Segment 1: Internal R&D / BD Operator

Job:

- decide which disease branch is worth pursuing,
- compare endpoint maturity,
- identify evidence gaps before a meeting,
- prepare a partner-facing memo.

Why they care:

- saves analyst time,
- reduces overclaim risk,
- makes opportunity review faster.

Primary product surface:

`Opportunity Brief Workbench`

### Segment 2: Companion Animal Therapeutics / Diagnostics Team

Job:

- evaluate product archetypes,
- understand endpoint and evidence package fit,
- map regulatory path questions,
- identify next evidence needed.

Why they care:

- supports product strategy,
- reduces wasted preclinical/clinical design effort,
- helps decide whether an indication is investable.

Primary product surface:

`Indication Evidence Dossier`

### Segment 3: Veterinary KOL / Research Collaborator

Job:

- verify whether claims are source-supported,
- understand what the vault says and does not say,
- co-author briefing or study rationale.

Why they care:

- faster literature orientation,
- traceable evidence,
- fewer hallucinated summaries.

Primary product surface:

`Claim Evidence Workbench`

### Segment 4: Educated Ordinary Reader

Job:

- understand disease,
- know what questions to ask a vet,
- distinguish strong evidence from weak advice.

Why they care:

- trust,
- clarity,
- no fake medical advice.

Primary product surface:

`Ask the Vault`

This is not the first monetization wedge. It is the trust and distribution surface.

## What Makes This Business-Critical

The project becomes business-critical when it powers one of these decisions:

| Decision | Product Output | Success Signal |
|---|---|---|
| Which feline disease area should we pursue next? | cross-disease opportunity brief | leadership uses it in prioritization |
| Is this claim defensible? | claim evidence card | claim is promoted, revised, or killed |
| What endpoint should a study use? | endpoint decision memo | endpoint shortlist changes study design |
| Is this treatment branch investable? | indication evidence dossier | go/no-go or diligence action |
| What evidence is missing? | gap-to-source intake queue | new source search or extraction starts |
| What can we say publicly? | source-bounded owner-facing answer | communication avoids overclaim |

If a feature does not feed one of these decisions, it is probably not business-critical.

## Product Thesis

The product is not:

- a generic AI vet,
- a generic academic search engine,
- a prettier Obsidian vault,
- an agent menu,
- a chatbot that happens to cite papers.

The product is:

`a claim-traceable feline evidence workbench that compresses literature into business decisions.`

## CEO Review

### Premise Challenge

Original premise:

`Make the project useful and not optional.`

Sharper premise:

`Make the project the default decision substrate for feline evidence work.`

That means the value metric is not answer quality alone.

The value metric is decision conversion:

```text
question -> evidence map -> decision artifact -> business action
```

### 10-Star Version

A 10-star `feline-research-os` session looks like this:

1. User asks: "Is feline CKD phosphorus control an investable branch?"
2. System returns:
   - current evidence backbone,
   - treatment ranking,
   - endpoint fit,
   - regulatory route questions,
   - missing primary studies,
   - claim boundaries,
   - next diligence checklist.
3. User exports:
   - one-page opportunity brief,
   - evidence table,
   - source verification appendix.
4. This goes into a business meeting.
5. A go/no-go or next-source-intake decision happens.

That is the product.

### CEO Findings

| Finding | Severity | Decision |
|---|---:|---|
| The current repo has strong truth infrastructure but weak business artifact focus. | High | Promote decision artifacts to first-class product surfaces. |
| Ordinary-user Ask is useful, but not the monetization wedge. | High | Keep it as front door, prioritize research/BD workflows. |
| Disease modules are mature enough to support opportunity briefs now. | High | Start with CKD/FIP/diabetes/cancer branch briefs. |
| Generic "AI research workbench" scope is too broad. | High | Narrow to feline evidence-to-decision workflows. |
| The strongest defensibility is claim traceability, not model cleverness. | High | Make Key-Claim Traceability visible in every business artifact. |

## Design Review

UI scope exists. The product experience must communicate decision readiness.

### Design Completeness Score

Current product direction: 5/10.

Why:

- strong evidence system,
- usable Ask surface,
- but business users still have to infer what to do next.

Target: 9/10.

### Required Product Surfaces

| Surface | User question | Output |
|---|---|---|
| Ask the Vault | What does the vault know? | source-bounded answer |
| Claim Evidence Workbench | Can we defend this claim? | claim verdict card |
| Opportunity Brief Workbench | Is this branch worth pursuing? | business-facing brief |
| Endpoint Decision Workbench | What should we measure? | endpoint shortlist + boundary |
| Gap-to-Intake Queue | What evidence is missing? | source search/extraction queue |

### Information Architecture

```text
Home
├── Ask
│   ├── plain explanation
│   ├── researcher map
│   └── source trace
├── Decide
│   ├── Opportunity Brief
│   ├── Endpoint Decision
│   └── Treatment Evidence
├── Verify
│   ├── Claim Evidence
│   ├── Source Card
│   └── Key-Claim Traceability
└── Build
    ├── Gap Queue
    ├── Source Intake
    └── Health Check
```

The current UI leans too much toward Ask. Business value needs Decide and Verify.

### 5-Second User Test

After landing in the app, a business user should know:

1. I can ask a disease question.
2. I can verify a claim.
3. I can generate a decision artifact.
4. I can see what evidence is missing.

If they only see a chat box, the product undersells itself.

### Anti-Slop Rules

Ban these outputs from business surfaces:

- generic disease summaries,
- unranked source lists,
- "consult a vet" endings for research workflows,
- no boundary section,
- no go/no-go implication,
- citations without loaded source trace,
- artifact that cannot be copied into a meeting doc.

## Engineering Review

### Scope

Do not rewrite the vault.

Do not rebuild the whole UI.

Add a business decision layer on top of existing source cards, topic pages, and local surfaces.

### Architecture

```text
Source Cards
  |
  v
Topic Pages / Compiled Memos
  |
  v
Decision Surface Builders
  |-----------------------------|
  | claim evidence card         |
  | opportunity brief           |
  | endpoint decision memo      |
  | treatment evidence summary  |
  | gap-to-intake queue         |
  |-----------------------------|
  |
  v
Exportable Business Artifact
  |
  v
Inbox / Promotion / Health Check
```

### Implementation Cuts

#### Cut 1: Business Rubric

Create:

`system/indexes/business-critical-product-rubric.md`

Define:

- user segment,
- decision type,
- required output,
- satisfaction metric,
- unacceptable failure modes.

#### Cut 2: Claim Evidence Workbench

Start here.

Reason: smallest wedge, highest defensibility, direct fit with current source IDs.

Input:

- disease,
- claim text,
- optional source IDs.

Output:

- verdict: supported / partially supported / not supported / absent,
- key sources,
- evidence depth,
- quoted facts if available,
- source-supported conclusion,
- boundary,
- next action.

Files likely involved:

- `scripts/app.py`
- `scripts/query.py`
- `scripts/search.py`
- new helper: `scripts/claim_evidence.py`
- tests/evals

#### Cut 3: Opportunity Brief Template

Create:

`system/templates/opportunity-brief-template.md`

Sections:

- disease branch,
- business question,
- evidence backbone,
- endpoint maturity,
- treatment/diagnostic opportunity,
- regulatory path notes,
- missing evidence,
- go/no-go implication,
- source appendix.

#### Cut 4: First Business Artifact

Generate one real artifact:

`outputs/business/ckd-phosphorus-control-opportunity-brief-20260604.md`

or:

`outputs/business/fip-gs441524-regulatory-opportunity-brief-20260604.md`

Do not make this a demo. Make it something that could be used in a meeting.

#### Cut 5: Eval

Add an eval script:

`scripts/business_value_eval.py`

It should test:

- claim evidence card has verdict,
- opportunity brief has go/no-go implication,
- source IDs exist,
- boundaries exist,
- next action exists,
- no unsupported claims.

### Test Diagram

```text
Business query
├── claim verification
│   ├── supported claim -> verdict + sources + boundary
│   ├── partial claim -> split claim + missing evidence
│   └── absent claim -> no support + intake suggestion
├── opportunity brief
│   ├── mature disease branch -> artifact + decision implication
│   ├── thin disease branch -> artifact + gap warning
│   └── mixed evidence -> artifact + branch-specific caveats
├── endpoint decision
│   ├── compiled endpoint page exists -> shortlist + hierarchy
│   └── missing endpoint page -> gap-to-intake queue
└── ordinary ask
    └── answer + trace, no business artifact unless requested
```

### Failure Modes

| Failure | Business impact | Mitigation |
|---|---|---|
| System produces nice summaries but no decisions | remains optional | every business surface must include decision implication |
| It tries to serve all pet owners first | weak monetization | keep ordinary Ask, but prioritize R&D/BD workflows |
| Claim verifier overstates evidence | credibility damage | strict verdict categories and source trace gate |
| Opportunity brief hides gaps | bad business decision | mandatory "missing evidence" section |
| UI only exposes chat | user misses value | add Decide and Verify entry points |
| Disease coverage is uneven | false product confidence | show maturity level per disease |
| New artifacts bypass health checks | truth layer rots | route business outputs through inbox/promotion/health |

## Business KPI

Do not track only:

- number of sources,
- number of answers,
- number of pages,
- source card count.

Track:

| KPI | Target |
|---|---|
| Decision artifacts produced per week | 1-3 |
| Claims killed or revised due to evidence boundary | >0 |
| Gap-to-intake tasks generated from real questions | >0 |
| Meeting-ready briefs exported | >0 |
| Time from question to defensible brief | <30 minutes |
| Unsupported claim rate in artifacts | 0 |

## Priority Roadmap

### P0: Make It Decision-Critical

1. Create business-critical rubric.
2. Build Claim Evidence Workbench.
3. Generate first meeting-ready opportunity brief.
4. Add business-value eval.

### P1: Make It Repeatable

1. Add endpoint decision memo generator.
2. Add opportunity brief generator.
3. Add gap-to-intake queue.
4. Add disease maturity labels to answer surfaces.

### P2: Make It Presentable

1. Add `Decide` and `Verify` UI entry points.
2. Add export buttons for business artifacts.
3. Add source appendix view.
4. Add weekly decision dashboard.

### P3: Make It Scalable

1. External source search only when explicitly requested.
2. PubMed/Crossref intake for gaps.
3. Partner-specific dossier generation.
4. Human review and promotion workflow for business outputs.

## What Not To Build Yet

Do not build:

- 20 research agents,
- generic pet owner symptom checker,
- broad academic search clone,
- fancy graph UI before claim evidence works,
- large paid API workflows before local decision surfaces work,
- cancer-style clinical recommendation tool.

## Decision Audit Trail

| # | Phase | Decision | Classification | Rationale |
|---|---|---|---|
| 1 | CEO | Reframe from answer quality to business decision conversion | Mechanical | user's concern is business impact |
| 2 | CEO | Prioritize R&D/BD/research workflows over ordinary-user monetization | User Challenge | ordinary-user surface is trust layer, not strongest wedge |
| 3 | Design | Add Decide and Verify as first-class product surfaces | Mechanical | chat-only hides business value |
| 4 | Eng | Build Claim Evidence Workbench first | Mechanical | smallest high-value slice using current source cards |
| 5 | Eng | Require business-value evals | Mechanical | prevents "nice but optional" drift |

## Final Approval Gate

### Recommendation

Approve the pivot from `auditable research vault + Ask UI` to:

`feline evidence decision workbench`

Start with Claim Evidence Workbench and one real Opportunity Brief.

### User Challenge

This plan changes the center of gravity.

It says ordinary-user chat is not the business wedge. It is the trust/distribution layer.

The business wedge is research/BD/translation decision support.

If your intended business is direct-to-consumer pet health education, this is wrong. If your intended business is companion-animal therapeutics, diagnostics, nutrition, regulatory intelligence, or research collaboration, this is the right move.

## Completion Summary

| Review | Status | Findings |
|---|---|---|
| CEO Review | PASS_WITH_USER_CHALLENGE | reframe project around decision artifacts |
| Design Review | PASS_WITH_REQUIREMENTS | add Decide and Verify surfaces |
| Eng Review | PASS_WITH_TEST_PLAN | build claim evidence wedge, eval business artifacts |

## GSTACK REVIEW REPORT

| Review | Trigger | Why | Runs | Status | Findings |
|--------|---------|-----|------|--------|----------|
| CEO Review | `/plan-ceo-review` via `/autoplan` | Scope & strategy | 1 | PASS_WITH_USER_CHALLENGE | project must drive decisions, not just answer questions |
| Design Review | `/plan-design-review` via `/autoplan` | Product surface | 1 | PASS_WITH_REQUIREMENTS | chat alone undersells business value |
| Eng Review | `/plan-eng-review` via `/autoplan` | Architecture & tests | 1 | PASS_WITH_TEST_PLAN | claim evidence workbench is first implementation slice |

## Autoplan Re-Review: 2026-06-06

Status: `PREMISE_GATE_PASSED`

### Classification

The June 6 materials started as an idea about a vertical Research OS, but the
repository now contains a concrete plan and working product slices. This review
therefore treats the task as a plan revision, not idea generation, QA, or bug
investigation.

### What Already Exists

The original roadmap is substantially implemented:

- Claim Evidence backend and Verify UI.
- Opportunity Brief generator and Decide UI.
- Endpoint Decision Memo generator.
- Gap-to-Intake queue and dashboard.
- Research Trace.
- Artifact review and promotion workflow.
- CKD researcher overview.
- Partner dossier generator.
- Eleven promoted business artifacts.

The next plan must not rebuild these surfaces.

### Verified CEO Findings

1. The current claim verifier is lexical matching, not semantic entailment.
   Opposing SDMA claims produced the same verdict, sources, confidence, and next
   action.
2. Opportunity Brief converts lexical verdict counts and source counts into
   `CONDITIONAL GO`, `HOLD`, or `NO GO`. The UI can invoke it with
   `branch="general"`, producing malformed claims such as "general improves
   outcomes."
3. `business_value_eval.py` validates artifact structure and source-ID presence,
   not whether evidence entails the claim or whether a recommendation is
   commercially justified.
4. The review queue records eleven promoted artifacts, mostly submitted and
   approved by `cli`; this is workflow metadata, not independent scientific and
   business review.
5. CKD maturity is stale in several static maps: the current corpus contains 50
   source cards, while product surfaces still report 24 and "full" extraction.

### CEO Dual Voices: Consensus

| Dimension | Independent reviewer | Codex reviewer | Consensus |
|---|---|---|---|
| Premises valid? | Evidence-to-decision overstates system authority | Same | CHANGE REQUIRED |
| Right problem? | Prove real adoption and accountable decisions | Build evidence-controlled diligence | CONFIRMED |
| Scope calibration? | Stop adding generators | Stop adding generators and disease modules | CONFIRMED |
| Alternatives explored? | Research Case / Decision Record | Sponsor Diligence Workspace | CONFIRMED |
| Competitive risk covered? | Generic synthesis is copyable | Retrieval and summaries are weak moats | CONFIRMED |
| Six-month trajectory? | Risk of many artifacts and no weekly user | Same | CONFIRMED |

Consensus: `5/6 confirmed`, with the product premise itself pending user
confirmation.

### Premise Gate

Recommended revised premise:

`Feline Research OS is an evidence-controlled diligence and research-case
workspace. It assembles traceable evidence, counterevidence, assumptions, gaps,
and artifacts; a named human owner makes and signs the final decision.`

Recommended next product layer:

`Research Case Workspace / Research Kernel`

Minimum durable record:

- research or business question;
- asset, indication, sponsor/client, owner, and deadline;
- decision criteria and alternatives;
- sources searched, included, and excluded;
- claim cards, counterevidence, and artifact versions;
- assumptions, dissent, and unresolved risks;
- human recommendation and approval;
- final action and later outcome.

Until semantic reliability is demonstrated, automated output should report
`evidence readiness`, not `GO`, `NO GO`, `invest`, `promote`, or `kill`.

User confirmation: `A`, received 2026-06-06.

The remaining design and engineering review will use the revised premise as the
source of truth.

<!-- AUTONOMOUS DECISION LOG -->
## Autoplan Decision Audit Trail

| # | Phase | Decision | Classification | Principle | Rationale | Rejected |
|---|---|---|---|---|---|---|
| 1 | Intake | Use this file as the main plan; treat the CKD plan and June 6 handoffs as supporting input | Mechanical | Explicit over clever | It is the repo-level product plan on the active branch | Create another overlapping plan |
| 2 | CEO | Treat the original roadmap as substantially implemented | Mechanical | DRY | Existing code already contains the planned decision surfaces | Rebuild Claim/Opportunity/Endpoint/Gap tools |
| 3 | CEO | Stop before changing the evidence-to-decision premise | User Challenge | User sovereignty | Both independent reviewers recommend changing the product's authority boundary | Silently rewrite the product thesis |
| 4 | CEO | Adopt evidence-controlled Research Case Workspace with human-signed decisions | User Confirmed | User sovereignty | User selected option A at the premise gate | Keep automatic investment decisions as the product center |

## Design Re-Review: 2026-06-06

Status: `PASS_WITH_REQUIRED_CONTRACTS`

Design completeness moved from `4/10` to `9/10`. The remaining point depends on
engineering the durable record and validating the workflow with a real CKD case.

### Superseding Design Decision

This section supersedes earlier requirements for first-class `Decide`, one-click
Opportunity Brief generation, automatic `GO / HOLD / NO GO`, and system-authored
investment recommendations.

The primary product surface is:

`Research Cases`

The system may assemble evidence and draft bounded research artifacts. It must
not present those artifacts as a final decision. Legacy decision artifacts are
labelled `unreviewed legacy output` until a named reviewer admits them into a
case.

### Selected Direction

Use:

- Variant B for the stage-gated workflow.
- Variant A for the persistent case identity and blocker header.
- Variant C for the claim-centric Evidence workspace.

Comparison artifact:

`/Users/jiawei/.gstack/projects/feline-research-os/designs/research-case-workspace-20260606/comparison.html`

### Information Architecture

```text
Research Cases
├── Case list
│   ├── owner / reviewer / due date
│   ├── current stage and state
│   └── blockers / stale / superseded indicators
└── Case workspace
    ├── Persistent case header
    │   ├── case ID / atomic question / version
    │   ├── asset / indication / jurisdiction
    │   ├── owner / reviewer / due date
    │   └── authority notice / blockers / dissent
    ├── Frame
    ├── Criteria
    ├── Evidence
    │   └── claim cards with support and counterevidence together
    ├── Challenge
    ├── Recommendation contract, unavailable in release 1
    ├── Sign contract, unavailable in release 1
    └── Search trace / assumptions / gaps / history / snapshots
```

### Stage and Gate Contract

Every stage has one of:

`not_started`, `in_progress`, `blocked`, `complete`, `stale`

Every transition records actor, timestamp, prior version, resulting version,
reason, and affected dependencies.

| Stage | Required inputs | Completion condition | Invalidation |
|---|---|---|---|
| Frame | atomic question, scope, alternatives, asset/indication, jurisdiction, owner, reviewer, deadline | reviewer confirms the question is decision-bounded | editing Frame makes all downstream stages stale |
| Criteria | criterion, threshold, applicability, required/optional flag, owner, rationale | criteria version is frozen | editing frozen Criteria makes Evidence and Challenge stale |
| Evidence | search trace, included/excluded sources, exclusion reasons, atomic claims, polarity, directness, species, depth, linked criterion | each required criterion has reviewed evidence status or an explicit gap | new, removed, or downgraded evidence invalidates affected claim and Challenge dispositions |
| Challenge | counterclaim/dissent, independent reviewer, disposition, rationale, unresolved blockers | all claims are challenged or explicitly blocked | claim split/merge or evidence change reopens affected challenges |
| Recommend | human-authored recommendation bound to a case snapshot | contract defined, UI unavailable in release 1 | any upstream stale state invalidates recommendation |
| Sign | authenticated attestation bound to case, evidence, and recommendation versions | identity, role separation, immutable snapshot, dissent and declaration are recorded | any signed-record edit creates a new revision and supersedes the prior case |

Gate overrides require a named actor, reason, timestamp, and audit entry. Prior
snapshots are preserved rather than overwritten.

### Evidence Workspace Contract

Evidence is organized around atomic claims, not a free-form Kanban board.

Each claim shows:

- support;
- counterevidence;
- applicability boundary;
- linked decision criterion;
- source verification depth;
- reviewer and disposition;
- assumptions with owner and expiry;
- unresolved gaps convertible to intake tasks.

Search accounting shows searched, included, excluded, and unresolved sources.
Exclusion reason is mandatory. Claim split and merge operations preserve
lineage.

### Interaction States

| State | Required behavior |
|---|---|
| Empty | explain required fields and expose only the next valid action |
| Loading | name the operation, preserve navigation, disable invalid advancement |
| Error | retain entered data, scope the error to its panel, expose retry |
| Partial | show successful/failed counts and the last valid snapshot |
| Stale | name the invalidating change and affected gates |
| Blocked | show blocker, owner, age, and resolution requirement |
| Signed | immutable snapshot with signer, role, version, and timestamp |
| Superseded | read-only with bidirectional link to the replacement |
| Source unavailable | retain citation metadata but prohibit verified status |

Do not show unexplained percentages such as `Readiness 58%`. Use categorical,
checklist-backed states such as `insufficient`, `reviewable`, and
`challenge-complete`.

### Seven-Pass Design Review

| Pass | Score | Resolution |
|---|---:|---|
| Information architecture | 9/10 | case-first hierarchy with persistent identity and blockers |
| Interaction and states | 9/10 | explicit gate, stale, blocked, signed, and superseded states |
| User journey | 9/10 | stage progression plus controlled reopening and invalidation |
| AI-slop resistance | 10/10 | no fake precision, generic verdict, decorative dashboard, or autonomous decision |
| Design-system fit | 9/10 | retains the dark utilitarian research-instrument language |
| Responsive/accessibility | 8/10 | requirements defined; implementation validation remains |
| Decision clarity | 9/10 | system authority and human authority are visibly separated |

### Responsive and Accessibility Requirements

- Minimum 13px control text, 15px body text, and 44px touch targets.
- Status always uses text plus icon/shape, never color alone.
- Workflow severity gets a separate semantic taxonomy from provenance colors.
- Visible keyboard focus, semantic headings/buttons/navigation, labelled
  controls, and live status announcements.
- At narrow widths, replace the six-stage row with a stage selector, move
  secondary rails into drawers, stack claim details, and keep blockers above
  content.
- Acceptance checks at 320px, 768px, desktop, keyboard-only, and 200% zoom.

### Release Boundary

Release 1 exposes only:

`Frame -> Criteria -> Evidence -> Challenge`

Recommendation and Sign are fully specified in the domain model now, but are
not rendered as available workflow stages. The UI states plainly that human
recommendation and signing remain outside this release until authentication,
role separation, immutable snapshots, and invalidation are implemented.

### Design Dual Voices: Consensus

| Dimension | Independent reviewer | Codex reviewer | Consensus |
|---|---|---|---|
| Selected composition | B workflow + A blockers + C evidence | Same | CONFIRMED |
| Automatic decision UI | Remove from primary flow | Same | CONFIRMED |
| Stage gates | Add explicit contracts and invalidation | Same | CONFIRMED |
| Evidence organization | Claim-centric, support and counterevidence together | Same | CONFIRMED |
| Recommend / Sign | Define now, delay interactive release | Same | CONFIRMED |
| Trust model | Durable versions and audit history required | Same | CONFIRMED |

### Not In Scope

- another disease knowledge module;
- generic academic search UI;
- automated commercial or clinical recommendation;
- cryptographic or legally compliant electronic signature in release 1;
- multi-tenant permissions;
- decorative graph or agent orchestration UI.

| 5 | Design | Replace Decide/Verify with Research Cases as the primary surface | Mechanical | Match revised authority boundary | Current top-level generators imply unsupported system authority | Keep one-click business decisions |
| 6 | Design | Select B workflow + A persistent blockers + C claim workspace | Mechanical | Combine the strongest tested hierarchy | Both design reviewers converged on the same composition | Choose one mockup unchanged |
| 7 | Design | Ship only Frame through Challenge in release 1 | Mechanical | Do not imply unavailable trust guarantees | Recommend and Sign require reliable evidence evaluation, identity, and immutable snapshots | Show locked but apparently imminent decision stages |

## Engineering Re-Review: 2026-06-06

Status: `PASS_WITH_IMPLEMENTATION_SEQUENCE`

### Scope Challenge

Do not add another generator, database service, vector store, background worker,
agent framework, or disease module. Release 1 is a local, single-repository case
workflow that makes evidence work durable and reviewable.

The first pilot is the CKD phosphorus-control case because the repository already
has a 50-card CKD corpus, a promoted legacy brief, endpoint material, and known
gaps. FIP follows only after the CKD workflow is used end to end.

### What Already Exists

Reuse:

- source cards and compiled topic/memo material as evidence inputs;
- Gap Queue as an external work queue;
- artifact files as read-only legacy attachments;
- current provenance and source appendix rendering;
- the existing custom Python test runner pattern;
- the Streamlit visual system and local-only operating model.

Do not reuse as trust signals:

- lexical claim verdicts;
- `promote`, `kill`, or GO/HOLD/NO-GO output;
- artifact queue `approved` or `promoted` status;
- typed CLI actor names as verified identities;
- static disease-maturity constants.

### Architecture Decision

Use one JSON record per case for release 1. This matches the repository's
file-based operating model and is sufficient for a local pilot. SQLite is
deferred until concurrent multi-user or remote deployment is a demonstrated
requirement.

```text
Streamlit Research Cases
        |
        v
research_case_ui.py
        |
        v
research_cases.py
  schema + invariants + transitions + invalidation + errors
        |
        v
research_case_store.py
  containment + migration + per-case lock + optimistic revision
        |
        v
system/research-cases/<case-id>.json
  current projection + immutable revisions + audit events
```

Each commit:

```text
submit(expected_revision, draft)
  -> acquire per-case advisory lock
  -> reload and validate stored revision
  -> reject mismatch with CASE_VERSION_CONFLICT
  -> validate transition and derive invalidation
  -> append immutable revision + audit event
  -> serialize canonical JSON
  -> write temp file in same directory
  -> flush + fsync temp file
  -> os.replace(temp, case file)
  -> fsync containing directory
  -> release lock
```

Corrupt or unsupported files fail closed. They must never become an empty case.
Ephemeral/public deployments default to read-only.

### File Boundaries

| File | Responsibility |
|---|---|
| `scripts/research_cases.py` | dataclasses/enums, validation, derived stage state, transitions, invalidation, stable errors |
| `scripts/research_case_store.py` | path containment, serialization, migrations, lock, atomic write, optimistic concurrency |
| `scripts/research_case_ui.py` | case list and Frame/Criteria/Evidence/Challenge forms |
| `scripts/app.py` | navigation and composition; remove primary Decide/Verify actions |
| `scripts/test_research_cases.py` | domain, store, migration, concurrency, security tests |
| `scripts/test_research_case_ui.py` | Streamlit interaction and rerun tests |
| `system/schemas/research-case-schema.md` | human-readable schema and invariants |
| `system/research-cases/<case-id>.json` | durable case records |

Keep the domain logic outside `app.py`. Do not split into a package with many
small modules until the model becomes difficult to navigate.

### Record Schema and Invariants

Top-level fields:

- `schema_version`;
- `case_id`, `revision`, `created_at`, `updated_at`;
- `status: active | superseded`;
- `current`, the current case projection;
- `revisions`, immutable canonical snapshots with content hashes;
- `events`, append-only actor/time/reason/change records.

Stable IDs are required for criteria, claims, evidence links, challenges,
assumptions, blockers, gaps, and legacy attachments. List position and display
text are never identity.

Evidence links bind:

- source ID and repository-relative path;
- SHA-256 content hash and observed timestamp;
- exact excerpt or structured fact;
- polarity, directness, species/applicability, and extraction depth;
- linked claim and criterion IDs;
- reviewer disposition and self-asserted actor label.

`progress` and `freshness` are separate:

```text
progress  = not_started | in_progress | blocked | complete
freshness = current | stale
```

A stage may therefore be both `blocked` and `stale`. The values are derived from
record invariants, not freely editable status fields.

### Invalidation Rules

- Semantic Frame edits to question, alternatives, scope, asset, indication, or
  jurisdiction stale Criteria, Evidence, and Challenge.
- Administrative Frame edits to owner, reviewer, or deadline create audit
  events but do not stale evidence.
- Editing frozen Criteria creates a new criteria revision and stales linked
  Evidence and Challenge.
- Evidence add/remove/edit, source-hash change, polarity change, or depth
  downgrade stales the affected claim and challenges.
- Claim edits create a new claim version.
- Claim split/merge supersedes parents, records predecessor/successor lineage,
  and requires fresh challenge.
- Challenge edits reopen Challenge without invalidating Evidence.
- Completion requires human-reviewed evidence status or an explicit gap for
  every required criterion. Lexical candidate matches never count.
- Gate overrides are excluded from release 1 because identity is unverified.

### Legacy Containment

- Remove Opportunity Brief, Endpoint Memo, and Verify actions from primary
  navigation.
- Preserve existing Markdown and JSON queues unchanged and read-only.
- Do not dual-write Research Case state back to those queues.
- Manual admission records original relative path, SHA-256, import timestamp,
  and label `legacy_unreviewed`.
- Existing `approved` and `promoted` values grant no gate completion.
- `claim_evidence.py` becomes candidate evidence retrieval only. Its verdict,
  confidence, `promote`, `revise`, and `kill` fields cannot populate reviewed
  dispositions.

### Identity Boundary

Release 1 stores:

`actor_label` and `identity_assurance: self_asserted`

The UI says:

`Typed attestation; identity not verified.`

It does not claim independent identity, nonrepudiation, secure signature, or
legal e-signature. Recommend and Sign remain absent.

### Streamlit Transaction Contract

- One `st.form` per stage.
- Widget keys include case ID, stage, and stable entity ID.
- Unsaved drafts remain in session state.
- A submit reloads the case, compares `expected_revision`, and commits once.
- Rerun happens only after a successful write.
- Conflict and write errors preserve entered data and offer reload/reconcile.
- Rapid double-submit is idempotent by operation ID.

### Security Boundaries

- Case IDs and source IDs use strict allowlist patterns.
- All paths are resolved and required to remain under approved repository roots.
- Reject absolute paths, `..`, separators in IDs, and symlink escapes.
- Escape case/user text before any `unsafe_allow_html` rendering.
- Limit field lengths, evidence attachment size, and total revisions per case
  with explicit validation errors.
- Do not expose arbitrary output paths in the case workflow.

### Error Registry

| Code | Retry | User-visible recovery |
|---|---|---|
| `WRITE_MODE_DISABLED` | no | open locally on persistent storage |
| `CASE_NOT_FOUND` | no | return to case list |
| `SCHEMA_UNSUPPORTED` | no | open read-only and run supported migration |
| `CORRUPT_CASE` | no | preserve file and restore from prior snapshot/backup |
| `VALIDATION_FAILED` | after edit | retain form and highlight invalid fields |
| `INVALID_TRANSITION` | after edit | show unmet gate requirements |
| `GATE_BLOCKED` | after resolution | show blocker owner and required resolution |
| `CASE_VERSION_CONFLICT` | yes | retain draft, reload, and reconcile |
| `WRITE_FAILED` | yes | retain draft and retry after storage check |
| `SOURCE_UNAVAILABLE` | yes | keep citation metadata, remove verified status |
| `SOURCE_CHANGED` | after review | mark linked claim stale and re-review |
| `PATH_OUTSIDE_ROOT` | no | reject path and log safe diagnostic |
| `LEGACY_IMPORT_BLOCKED` | after review | show parsing/admission requirement |
| `UNEXPECTED_ERROR` | maybe | retain input, show redacted diagnostic |

### Migration Contract

- `schema_version` is mandatory.
- Migrations are pure, sequential, idempotent transforms.
- Test every supported starting version.
- Unknown future versions open read-only.
- Initial CKD case creation is an explicit import command/report, never an
  app-startup mutation.
- Rollback uses the untouched pre-migration backup.

### Implementation Cuts

#### Cut 0: Contain Unsafe Authority

1. Remove Decide/Verify and the decision dashboard from primary navigation.
2. Mark legacy generated artifacts `unreviewed legacy output`.
3. Stop `branch="general"` Opportunity Brief generation.
4. Change claim-verifier product language to candidate retrieval/abstention.
5. Replace static disease maturity display with computed inventory or remove it.

#### Cut 1: Durable Case Kernel

1. Add schema and stable IDs.
2. Add validation, progress/freshness derivation, transitions, and invalidation.
3. Add per-case lock, atomic write, revision conflict, migrations, and errors.
4. Add complete domain/store tests before UI composition.

#### Cut 2: Four-Stage Workspace

1. Case list and persistent header.
2. Frame and Criteria forms.
3. Claim-centric Evidence workspace.
4. Challenge workflow and blockers.
5. Empty/loading/error/partial/stale/blocked states.

#### Cut 3: CKD Pilot

1. Explicitly import the CKD phosphorus-control legacy brief as unreviewed.
2. Build the case from Frame through Challenge.
3. Convert real gaps to external intake tasks.
4. Record task completion time, claims revised/killed by a human, unresolved
   blockers, and user return within seven days.

### Test Coverage Diagram

```text
DOMAIN / STORE
├── schema
│   ├── valid/invalid required fields, enums, IDs, UTC timestamps
│   ├── canonical hash and immutable revision history
│   └── old/current/future schema migration branches
├── transitions
│   ├── every permitted and forbidden stage transition
│   ├── progress + freshness combinations
│   └── completion rejected for missing requirements
├── invalidation
│   ├── semantic vs administrative Frame changes
│   ├── frozen Criteria edits
│   ├── evidence add/remove/downgrade/source-hash change
│   └── claim edit/split/merge and Challenge reopen
├── persistence
│   ├── create/read/update/history
│   ├── interrupted temp write and replace failure
│   ├── corrupt/truncated/unsupported file fails closed
│   └── same-revision race -> one success + one conflict
├── security
│   ├── absolute/traversal/separator/symlink path attacks
│   ├── field and attachment limits
│   └── HTML/script content rendered as text
└── legacy
    ├── inventory and malformed artifact
    ├── admission with checksum
    └── no legacy status or lexical verdict grants gate credit

USER FLOW [-> Streamlit AppTest / QA]
├── create case -> Frame -> freeze Criteria -> add Evidence -> Challenge
├── empty/partial/blocked/stale and source-unavailable states
├── rapid double-submit and two-tab version conflict retain draft
├── refresh/restart restores case and history
├── no GO/HOLD/NO GO or Sign action in primary UI
├── keyboard-only, 320px, 768px, desktop, and 200% zoom
└── every registered error shows a specific recovery action

EVAL [-> golden cases]
├── positive and negated SDMA claims never receive identical reviewed status
├── candidate retrieval is clearly labelled and cannot complete Evidence
└── generated text never authors a final recommendation or attestation
```

Current coverage for new paths is `0%`; all branches above are implementation
requirements. Use `scripts/test_research_cases.py` with temporary directories and
processes. Use `streamlit.testing.v1.AppTest` where feasible, then `/qa` for
responsive and keyboard checks.

### Performance Budget

- Case list: under 200 ms for 100 cases.
- Case open: under 300 ms for a 1,000-revision case.
- Stage commit: under 200 ms excluding source hashing.
- Evidence view: paginate or collapse after 100 claims.
- Build one request-level source metadata snapshot keyed by path, size, and
  modification time; do not reread every source for every claim.
- Test 100 cases, 1,000 revisions, and 10,000 evidence links before considering
  a database migration.

### Failure Modes

| Failure | Handling | Test | User experience |
|---|---|---|---|
| two sessions write same revision | lock + optimistic conflict | required | draft retained; reconcile prompt |
| process stops during write | same-directory atomic replace | required | prior valid revision remains |
| case JSON is corrupt | fail closed | required | read-only recovery message |
| source file changes | hash mismatch stales claim | required | re-review required |
| legacy file malformed | reject admission | required | source file remains untouched |
| Streamlit reruns during submit | operation ID + commit-once | required | no duplicate revision |
| candidate matcher overclaims | no gate-credit invariant | golden eval | visible candidate-only label |

No silent failure is acceptable for a case write, migration, source change, or
legacy admission.

### Parallelization

```text
Lane A: Cut 0 legacy containment
Lane B: schema + domain model -> store + migrations -> domain/store tests
After Lane B: UI composition -> UI tests
After A + UI: CKD pilot -> QA
```

Lane A and the initial schema/domain portion of Lane B can run in parallel in
separate worktrees. UI and pilot remain sequential because they depend on the
kernel.

### NOT In Scope

- SQLite or a remote database before measured file-store limits;
- authentication and verified role separation;
- legal or cryptographic signing;
- multi-tenancy and remote collaboration;
- semantic entailment automation as a gate authority;
- vector database or background indexing service;
- automatic migration of promoted artifacts;
- Recommend and Sign UI.

### Engineering Dual Voices

| Dimension | Independent reviewer | Codex reviewer | Decision |
|---|---|---|---|
| Durable revisions required | Yes | Yes | CONFIRMED |
| Atomic writes and version conflicts | Yes | Yes | CONFIRMED |
| Progress/freshness separation | Explicit | Derived-state warning | ADOPT |
| Legacy outputs grant no trust | Yes | Yes | CONFIRMED |
| Typed actors are unverified | Yes | Yes | CONFIRMED |
| Storage | SQLite snapshots | JSON per case | JSON for local release 1; measure migration trigger |
| Database/vector infrastructure now | No vector; SQLite | Neither | DEFER |

### Engineering Completion Summary

- Scope Challenge: scope reduced to authority containment + durable four-stage
  case workflow.
- Architecture Review: 6 critical contracts fixed.
- Code Quality Review: exact boundaries, invariants, typed errors, and path
  containment defined.
- Test Review: branch diagram produced; all new paths are currently gaps and
  required before release.
- Performance Review: source reread and file-store budgets defined.
- NOT in scope: written.
- What already exists: written.
- Failure modes: no accepted silent critical gaps.
- Outside voice: independent subagent and Codex completed.
- Parallelization: 2 initial lanes, then sequential UI/pilot.
- DX Review: skipped because no external developer-facing API, SDK, or CLI is
  introduced; internal scripts are implementation details.

| 8 | Eng | Use JSON-per-case with immutable revisions and atomic locked writes for release 1 | Mechanical | Minimal architecture with measured migration trigger | Fits the local file-first repository while preventing lost updates | Add SQLite before multi-user need |
| 9 | Eng | Split stage progress from freshness | Mechanical | Model independent facts independently | A stage can be blocked and stale simultaneously | Single five-value status enum |
| 10 | Eng | Treat all release-1 actor labels as self-asserted attestations | Mechanical | Do not claim security properties that do not exist | The app has no authentication | Implement Sign with typed names |
| 11 | Eng | Make CKD phosphorus control the first real case | Taste | Maximize learning from existing assets | It has the deepest current material and known legacy defects | Start another disease module |

## Final Autoplan Gate: 2026-06-06

Status: `AWAITING_FINAL_APPROVAL`

### Cross-Phase Themes

1. The moat is not another answer generator. It is the durable, inspectable
   record of how evidence was searched, admitted, challenged, revised, and used.
2. The system owns evidence organization and readiness reporting. A named human
   owns recommendations and decisions.
3. Existing business generators are useful historical material but unsafe as
   decision authority. They must be contained before new workflow UI ships.
4. Trust depends on revision identity, source content hashes, explicit gaps,
   counterevidence, and visible invalidation, not on confidence labels.
5. Release 1 must prove one repeated research workflow before expanding disease
   breadth, agents, databases, or commercial recommendation features.

### Final Implementation Roadmap

```text
Cut 0: Authority containment
  -> remove primary automatic decision actions
  -> relabel lexical outputs and legacy artifacts
  -> remove stale/fake maturity claims

Cut 1: Durable Research Case kernel
  -> schema + stable IDs
  -> progress/freshness + invalidation
  -> locked atomic revision store
  -> migrations + errors + complete tests

Cut 2: Research Case workspace
  -> case list/header
  -> Frame -> Criteria -> Evidence -> Challenge
  -> blockers, gaps, history, stale states

Cut 3: CKD phosphorus-control pilot
  -> admit legacy brief as unreviewed
  -> complete a real case
  -> QA and measure repeat use
```

### Release Acceptance Criteria

- No primary UI action emits or implies automatic GO/HOLD/NO-GO.
- Positive and negated candidate claims cannot silently acquire the same
  reviewed disposition.
- Every case survives refresh/restart with complete revision history.
- Concurrent same-revision writes cannot overwrite each other.
- Every required criterion has reviewed evidence or an explicit gap.
- Support and counterevidence are visible on the same atomic claim.
- Source changes visibly stale affected work.
- Legacy approval metadata grants no gate credit.
- Actor labels are visibly self-asserted; Recommend and Sign are absent.
- The CKD pilot reaches Challenge with no silent write or migration failure.

### Approval Choices

- `A` Approve this plan and begin implementation with Cut 0.
- `B` Revise the final plan before implementation.
- `C` Stop after planning; preserve the artifacts only.

### Final Decision Audit

| # | Phase | Decision | Classification | Rationale |
|---|---|---|---|---|
| 12 | Final | Implement authority containment before the case UI | Mechanical | New UI must not coexist with unsafe automatic decision authority |
| 13 | Final | Use CKD phosphorus control as the first adoption test | Taste | Highest evidence depth and clearest existing defects produce the fastest learning |
| 14 | Final | Gate implementation on explicit user approval | User Challenge | The plan changes product authority, navigation, and persistence architecture |

## GSTACK REVIEW REPORT

| Review | Trigger | Runs | Status | Findings |
|---|---|---:|---|---|
| CEO Review | `/plan-ceo-review` via `/autoplan` | 2 | PASS_AFTER_USER_GATE | revised product from automated decision workbench to evidence-controlled Research Cases |
| Design Review | `/plan-design-review` via `/autoplan` | 2 | PASS_WITH_CONTRACTS | selected B workflow + A blockers + C claim evidence; delayed Recommend/Sign |
| Eng Review | `/plan-eng-review` via `/autoplan` | 2 | PASS_WITH_TEST_PLAN | durable revisions, locked atomic writes, invalidation, errors, security, and tests defined |
| DX Review | scope check | 1 | SKIPPED | no external developer-facing API, SDK, or CLI is introduced |
| Final Gate | cross-phase synthesis | 1 | AWAITING_USER | implementation begins only after final approval |

Overall verdict: `READY_FOR_IMPLEMENTATION_AFTER_FINAL_APPROVAL`

Artifacts:

- Restore point:
  `/Users/jiawei/.gstack/projects/feline-research-os/idea-chatacademia-research-workbench-autoplan-restore-20260606-154819.md`
- Design comparison:
  `/Users/jiawei/.gstack/projects/feline-research-os/designs/research-case-workspace-20260606/comparison.html`
- Engineering QA plan:
  `/Users/jiawei/.gstack/projects/feline-research-os/jiawei-idea-chatacademia-research-workbench-eng-review-test-plan-20260606-212531.md`

## Implementation Progress

### Cut 0: Authority Containment

Completed: `2026-06-07`

- Removed Opportunity Brief, Endpoint Memo, Verify Claim, and Decision Dashboard
  from the primary Streamlit UI.
- Removed their session-state handlers and direct artifact-save workflow.
- Changed claim evaluation output to candidate evidence retrieval with
  `not_assessed` semantic confidence and mandatory human review.
- Disabled automatic claims and the `general` branch in the legacy Opportunity
  Brief generator.
- Replaced automatic GO/HOLD/NO-GO output with an explicit
  `AUTOMATED DECISION DISABLED` notice.
- Prevented Partner Dossier from generating a hidden general Opportunity Brief.
- Replaced static maturity labels with factual source-card inventory counts.
- Updated artifact evaluation to reward authority containment rather than
  automatic decision language.

Verification:

- `scripts/test_authority_containment.py`: 5 passed.
- `scripts/test_query.py`: 111 passed.
- Streamlit `AppTest`: 0 exceptions; no forbidden decision buttons.
- Python compile check: passed.
- Existing `check_local_answer_surfaces.py` still reports six pre-existing
  unsupported route cases outside Cut 0; FIP surfaces and the CKD researcher
  overview pass.

Next implementation cut: `Cut 1: Durable Case Kernel`.

### Cut 1: Durable Case Kernel

Completed: `2026-06-07`

- Added schema version 1, stable case/entity IDs, validation, canonical hashes,
  typed error registry, and self-asserted identity metadata.
- Split stage `progress` from `freshness`.
- Implemented semantic versus administrative Frame invalidation.
- Implemented Criteria, Evidence, Challenge, blocker, and legacy-attachment
  operations.
- Added per-case advisory locking, optimistic revision checks, idempotent
  operation IDs, same-directory atomic replacement, fsync, migrations, and
  fail-closed corruption handling.
- Added source-path containment and SHA-256 requirements.

Verification:

- `scripts/test_research_cases.py`: 11 passed.
- Includes same-revision concurrency, duplicate submit, failed replace,
  corrupt/future schema, migration backup, path traversal, and legacy no-credit
  tests.

### Cut 2: Four-Stage Workspace

Completed: `2026-06-07`

- Added isolated `Ask` and `Research Cases` workspaces.
- Added durable case creation and reload.
- Added persistent case identity, revision, owner/reviewer/deadline, authority
  notice, and stage progress/freshness.
- Added structured Frame, Criteria, Evidence, and Challenge forms.
- Added revision history and unreviewed legacy attachment display.
- Recommend and Sign remain absent.

Verification:

- `scripts/test_research_case_ui.py`: case creation/reload passed.
- Streamlit AppTest: isolated Research Cases navigation passed.
- Pilot case visibility: passed.

### Cut 3: CKD Phosphorus-Control Pilot

Status: `BLOCKED_ON_NAMED_HUMAN_CRITERIA_REVIEW`

- Created `case-ckd-phosphorus-control`.
- Imported the June 4 legacy brief with SHA-256 as `legacy_unreviewed`.
- Granted no Criteria, Evidence, or Challenge completion credit.
- Added visible blocker `blocker-human-criteria-review`.
- The blocker requires a named human to define and freeze Criteria before
  evidence review proceeds. Automation must not fabricate that attestation.

Current pilot revision: `3`.
