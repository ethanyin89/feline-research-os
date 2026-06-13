# Feline Research OS Architecture

**Version:** 0.1 (Draft)
**Last Updated:** 2026-06-09
**Status:** MVP implemented; repeated workflow validation remains
**Branch:** idea-chatacademia-research-workbench

## Product Definition

Feline Research OS is a **research workspace for feline medicine**, not a chatbot.

It transforms feline disease research, drug efficacy evaluation, PK/PD studies, and protocol design from scattered chat sessions into a **retrievable, verifiable, and inheritable research system**.

### What It Is

- A sovereign research workspace you own and control
- A system that saves research records, not just answers
- A platform where every conclusion can be traced to evidence
- A tool that distinguishes cat evidence from dog/human/mouse extrapolation

### What It Is Not

- A cute cat + AI chatbox interface
- A generic knowledge Q&A tool
- A black-box answer engine
- A single-model dependency

## Six-Layer Architecture

Based on analysis of II (Intelligent Internet) design principles:

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1: Human-in-the-Loop Research Workspace                 │
│  ├── User is not a spectator but an active reviewer            │
│  ├── Every decision point is visible and modifiable            │
│  └── Professional judgment stays in the loop                   │
├─────────────────────────────────────────────────────────────────┤
│  Layer 2: Professional Team Mode                               │
│  ├── Strategist: clarify goals, define scope                   │
│  ├── Coordinator: decompose into work modules                  │
│  ├── Associates: execute specific research tasks               │
│  └── Verifier: review evidence, species, completeness          │
├─────────────────────────────────────────────────────────────────┤
│  Layer 3: Research Pipeline                                    │
│  ├── Query evaluation → Search depth assignment                │
│  ├── Subquery generation → Multi-source retrieval              │
│  ├── Evidence compression → Gap reflection                     │
│  ├── Follow-up retrieval → Draft synthesis                     │
│  └── Verification → Final report → Save record                 │
├─────────────────────────────────────────────────────────────────┤
│  Layer 4: Research Record                                      │
│  ├── request, scope, sources, decisions                        │
│  ├── outputs, uncertainties, handoff, next_steps               │
│  └── Durable work records, not ephemeral chat                  │
├─────────────────────────────────────────────────────────────────┤
│  Layer 5: Retrieval Memory                                     │
│  ├── Evidence cards, model cards, protocol versions            │
│  ├── Correction history, verifier rules                        │
│  └── Low-cost retrieval of accumulated state                   │
├─────────────────────────────────────────────────────────────────┤
│  Layer 6: Data Quality & Verification                          │
│  ├── Intake: deduplication, quality filtering, structuring     │
│  ├── Output: species verification, evidence grounding          │
│  └── Prevent cat/dog mixing, over-extrapolation                │
└─────────────────────────────────────────────────────────────────┘
```

## Core Data Objects

### Research Record Schema

Every research task generates a durable record:

```yaml
record_id: string                    # unique identifier
timestamp: datetime                  # when task was created
user_request: string                 # original user question
task_type: enum                      # literature_review | protocol_design | evidence_check |
                                     # biomarker_mapping | model_evaluation | pk_design | other
species: cat                         # always feline for this system
disease: enum                        # FIP | CKD | HCM | FCGS | obesity | dermatology | other
scope: string                        # task boundary description
retrieval_sources:
  - pubmed
  - pmc
  - internal_knowledge_base
  - guideline
  - uploaded_file
selected_evidence:
  - evidence_card_id                 # cards used in answer
excluded_evidence:
  - reason                           # why certain sources were excluded
key_decisions:
  - decision                         # important choices made
uncertainties:
  - uncertainty                      # acknowledged gaps
output_path: string                  # where final output is saved
verifier_status: enum                # passed | failed | needs_human_review
next_steps:
  - action                           # recommended follow-up
handoff_summary: string              # for next agent/session
```

### Evidence Card Schema

Structured knowledge units, not raw text:

```yaml
evidence_card_id: string             # unique identifier
title: string                        # source title
source_type: enum                    # pubmed | pmc | guideline | internal_note |
                                     # protocol | uploaded_file
source_id: string                    # PMID/PMCID/DOI/file_path/url
species: enum                        # cat | dog | human | mouse | mixed | unknown
disease: string                      # specific disease
study_type: enum                     # guideline | review | original_research |
                                     # case_series | internal_protocol | other
biomarkers:
  - string                           # relevant biomarkers mentioned
use_case:
  - diagnosis
  - enrollment
  - efficacy_endpoint
  - safety_monitoring
  - prognosis
  - model_validation
key_finding: string                  # main takeaway
limitations: string                  # acknowledged limitations
evidence_strength: enum              # high | medium | low
last_reviewed: date                  # when last verified
```

## Harness Loop (Feline-RALPH)

Prevents premature completion on complex tasks:

```
user_request
  → task_evaluation          # What type of task? What depth needed?
  → initial_answer / draft   # First attempt at answer
  → gap_check               # Compare draft against original requirement
  → revision                # Fill identified gaps
  → independent_verification # Species check, evidence check, completeness
  → final_answer            # Verified output
  → save_research_record    # Preserve procedural context
```

### Verifier Checkpoints

- Species boundary: Is evidence directly from cats?
- Cross-species mixing: Any dog/human/mouse extrapolation unmarked?
- Evidence sources: Are PubMed/guideline/internal sources cited?
- Endpoint clarity: Diagnosis vs enrollment vs efficacy vs safety distinguished?
- Evidence level: High/medium/low labeled?
- Uncertainty disclosure: Gaps and extrapolation risks noted?
- Protocol completeness (for design tasks):
  - Purpose, animals, grouping, endpoints, timepoints
  - Statistics, ethics, humane endpoints, limitations

## Search Depth Controller

Based on II-Search principles, prevent "tool laziness":

| Task Type | Min Searches | Source Types Required | Gap Reflection |
|-----------|-------------|----------------------|----------------|
| Quick (explanation) | 0-1 | Any | Optional |
| Standard (literature/biomarker) | 2-3 | At least 2 types | Recommended |
| Deep (protocol/endpoint selection) | 2+ rounds | Guideline + review + original research | Required |
| Evidence Audit | Multiple | Must include limiting/contrary evidence | Required |

## Query Evaluation Dimensions

Before processing any research question:

| Dimension | Question to Answer |
|-----------|-------------------|
| Freshness | Does this need latest literature? (new biomarkers, new drugs) |
| Plurality | Does this need multiple sources? (most protocol questions do) |
| Completeness | Does this need full protocol structure or just explanation? |
| Species-specificity | Must be cat-only? Flag extrapolation risk? |
| Evidence type | Need guideline? Review? Original research? Internal record? |
| Output type | Literature cards? Report? Protocol? Table? Prompt template? |

## Agent Roles (YAML-configurable)

### feline_research_strategist
- Faces user directly
- Clarifies: Is this literature review? Protocol design? Evidence check?
- Defines task boundary before execution

### research_coordinator
- Decomposes task into work modules
- Assigns: retrieve literature, extract biomarkers, draft protocol, verify species

### literature_search_associate
- PubMed/PMC search execution
- Evidence card generation
- Evidence level annotation

### feline_disease_model_associate
- Disease model expertise: FIP, CKD, HCM, FCGS, obesity, dermatology
- Model suitability assessment
- Limitation disclosure

### protocol_design_associate
- Converts evidence into protocol structure
- Covers: purpose, animals, grouping, dosing, endpoints, timepoints, statistics, ethics

### evidence_verifier
- Checks source reliability
- Confirms evidence supports conclusions
- Verifies PubMed/guideline/internal record backing

### species_specific_reviewer
- Cat vs dog/human/mouse mixing detection
- Feline-specific considerations
- Veterinary terminology accuracy

### research_record_writer
- Saves: request, scope, sources, decisions, uncertainties, next_steps
- Generates handoff summary for continuity

## MVP Implementation Path

### Phase 1: Core Infrastructure

```
/pages
  1_Research_Console.py      # Main research interface
  2_Evidence_Cards.py        # Browse/search evidence cards
  3_Research_Records.py      # View past research tasks
  4_Verifier_Dashboard.py    # Verification status overview

/core
  task_evaluator.py          # Query evaluation & depth assignment
  search_depth_controller.py # Enforce minimum search behavior
  retrieval.py               # PubMed/internal search wrapper
  evidence_card.py           # Evidence card CRUD
  gap_checker.py             # Gap detection after draft
  verifier.py                # Species/evidence/completeness checks
  record_store.py            # Research record persistence
  synthesis.py               # LLM synthesis with evidence grounding

/data
  research_records/          # JSON/Markdown records
  evidence_cards/            # Structured evidence units
  verifier_rules/            # Configurable verification rules

/prompts
  strategist.md              # Strategist agent prompt
  evidence_extractor.md      # Evidence extraction prompt
  gap_checker.md             # Gap detection prompt
  verifier.md                # Verification prompt
  final_synthesizer.md       # Final answer synthesis prompt
```

### Phase 2: Harness Loop Integration

- Implement draft → gap_check → revision → verification cycle
- Add verifier checkpoints to Research Console
- Show verification status in Research Records

### Phase 3: Retrieval Memory

- Index historical research records for retrieval
- Enable "what did we conclude about X before?" queries
- Cross-reference evidence cards across tasks

### Phase 4: Data Quality Pipeline

- Intake validation for new sources
- Deduplication detection
- Species/evidence type auto-tagging
- Quality scoring for evidence cards

## Benchmark Questions (Initial 20)

For regression testing improvements:

1. 猫 FIP 药效评价有哪些核心指标？
2. 猫 CKD 研究中 SDMA 的用途和限制是什么？
3. 猫 HCM 研究中超声心动图终点如何选择？
4. 猫 PK 研究采血设计有哪些约束？
5. 猫 FCGS 临床研究评分体系如何构建？
6. 猫皮肤真菌模型适合评价哪些产品？
7. 猫肥胖模型中体重、BCS、代谢指标如何组合？
8. 猫研究方案中哪些地方最容易犬猫混用？
9. FIP 造模成功率如何评价？
10. CKD 自然病例 vs 造模的优劣势？
11. SAA 在猫炎症评价中的边界是什么？
12. A/G ratio 在 FIP 诊断和疗效评价中分别承担什么角色？
13. 猫药物 PK 采样时间点如何设计？
14. 猫临床前研究中人道终点如何设定？
15. IRIS 分期在 CKD 药效评价中的应用？
16. 猫呼吸道感染模型的主要读数指标？
17. 猫皮肤病模型中瘙痒评分体系的选择？
18. 猫心肌病研究中 NT-proBNP 的用途？
19. 猫糖尿病模型的血糖控制目标？
20. 猫研究中转化医学的边界和风险？

## Visual Direction

**NOT:** Cute cats + AI chatbox
**YES:** Research infrastructure / veterinary research blueprint

Style keywords:
- Warm parchment background
- Navy ink line art
- Engraved architectural drawings
- Archival scientific illustration
- Research infrastructure aesthetic
- Evidence record visual language

## Relationship to Existing Code

### Current State (scripts/)

| File | Role | Architecture Layer |
|------|------|-------------------|
| app.py | Streamlit main app | Layer 1 (Workspace) |
| query.py | Query processing | Layer 3 (Pipeline) |
| search.py | Source search | Layer 5 (Retrieval) |
| health.py | System health checks | Layer 6 (Quality) |
| claim_evidence.py | Evidence management | Layer 4 (Record) |
| endpoint_decision.py | Endpoint logic | Layer 2 (Team Mode) |
| research_case_store.py | Case persistence | Layer 4 (Record) |
| structured_abstract_extraction.py | Source extraction | Layer 6 (Quality) |

### Integration Path

1. **No breaking changes** - new architecture layers extend, not replace
2. **Gradual migration** - existing query.py becomes part of Layer 3 pipeline
3. **Research Record** wraps existing output mechanisms
4. **Evidence Card** schema aligns with existing source card frontmatter

## Design Principles

From II materials analysis:

1. **Model replaceable** - GPT/DeepSeek/Claude are interchangeable; records and rules persist
2. **Knowledge auditable** - Every conclusion traceable to source + evidence level
3. **Work inheritable** - Each task becomes foundation for future tasks
4. **Species boundaries** - Cat evidence distinguished from extrapolation
5. **Premature completion prevention** - Complex tasks require harness loop
6. **Tool laziness prevention** - Complex questions require multiple search rounds

## Next Steps

1. [x] Review and approve this architecture with user
2. [x] Create `core/` directory structure
3. [x] Implement Research Record schema in `record_store.py`
4. [x] Implement Evidence Card schema extending existing source cards
5. [x] Add Harness Loop to Research Console
6. [x] Integrate Verifier checkpoints
7. [x] Build benchmark question evaluation
8. [x] Enforce observable search-depth contracts in the Harness Loop

The architecture MVP is implemented. The next gate is repeated workflow
validation, not adding more framework layers.
