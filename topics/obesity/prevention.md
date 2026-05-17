---
id: topic-obesity-prevention
type: topic
topic: obesity
species: feline
disease: obesity
question_type: prevention
source_ids: [src-obesity-001, src-obesity-005]
last_compiled_at: 2026-05-17
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: not_checked
owner: codex
status: active
---

# Feline Obesity Prevention

## Key-Claim Traceability

| ID | Claim | Level | Source IDs | Boundary |
|---|---|---|---|---|
| OP1 | Post-gonadectomy kittens aged 5-12 months are the primary target population for obesity prevention | B | src-obesity-005 | target population, not universal screening mandate |
| OP2 | Treatment for feline obesity is slow, often unsuccessful, and not without consequences | B | src-obesity-005 | treatment limitation framing, not treatment rejection |
| OP3 | Prevention is preferable to treatment because of treatment limitations | B | src-obesity-005 | strategic priority, not efficacy claim |
| OP4 | Dietary and feeding management strategies are the primary prevention approaches | B | src-obesity-005 | strategy categories, not specific protocols |
| OP5 | Identifying high-risk populations is crucial for developing preventive strategies | B | src-obesity-005 | targeting logic, not population-specific success rates |

## Evidence-Depth Caveat

This page sits on 4 deep-extracted obesity source cards (001, 004, 005, 008). The primary anchor for prevention is src-obesity-005, a 2024 JFMS research review with 118 citations. The abstract was extracted via Crossref API; full-text extraction would add specific dietary protocols and feeding recommendations.

## Core Takeaway

Prevention is strategically preferable to treatment for feline obesity because treatment is slow, often unsuccessful, and carries its own consequences. The primary target population for prevention is post-gonadectomy kittens aged 5-12 months. Prevention strategies focus on dietary and feeding management, though specific protocols require full-text verification.

## Prevention Architecture

### Strategic Priority: Prevention Over Treatment

Most research currently focuses on obesity treatment. However, treatment outcomes suggest prevention should be the priority:

| Aspect | Treatment Reality | Prevention Advantage |
|--------|-------------------|---------------------|
| Research focus | Majority of current research | Underrepresented but more strategic |
| Success rate | Often unsuccessful | More effective when targeted |
| Speed | Slow | Proactive intervention |
| Consequences | Not without consequences | Lower overall burden |

**Key framing:** Prevention is not just "treatment done earlier" — it is a different strategic orientation that avoids the burden of treatment limitations.

**Lead sources:** `src-obesity-005`

### Target Population

The primary target population for obesity prevention is:

| Population | Age Range | Context |
|------------|-----------|---------|
| **Post-gonadectomy kittens** | **5-12 months** | Primary prevention target |

**Why this population:**
- Gonadectomy is a known risk factor for obesity
- The 5-12 month window follows typical neutering timing
- This is when metabolic changes from neutering intersect with growth completion
- Targeted prevention at this stage can prevent obesity onset rather than requiring later treatment

**Lead sources:** `src-obesity-005`

### Prevention Strategy Categories

The review highlights two main strategy categories:

1. **Dietary management strategies**
   - Specific protocols need full-text verification
   - Focus is on preventing excessive energy intake

2. **Feeding management strategies**
   - Specific protocols need full-text verification
   - Focus is on feeding patterns and behaviors

**Current limitation:** The abstract identifies strategy categories but not specific protocols. Full-text extraction would add actionable detail.

**Lead sources:** `src-obesity-005`

### Risk Factor Awareness in Prevention

Prevention requires awareness of modifiable risk factors (from risk-and-recognition page):

**Modifiable extrinsic factors:**
- Sedentary indoor lifestyle
- Low environmental stimulation
- Ad-lib feeding patterns
- Commercial processed food reliance
- Owner feeding behaviors

**Post-neuter timing:** The neutering event is a modifiable timing point — prevention efforts can be initiated at this known transition.

**Lead sources:** `src-obesity-001`, `src-obesity-005`

## Source-Layer Reality

| Source | Role | Status |
|---|---|---|
| src-obesity-001 | comprehensive review: risk factors relevant to prevention targeting | deep_extracted |
| src-obesity-005 | prevention review: target population, treatment limitations, strategy categories | deep_extracted |

## Prevention Targeting Matrix

| Target Population | Why Target | Prevention Window | Strategy Focus | Key Source IDs |
|---|---|---|---|---|
| Post-gonadectomy kittens 5-12mo | Highest risk window after known trigger event | At or shortly after neutering | Dietary and feeding management | src-obesity-005 |
| Indoor cats with limited enrichment | Lifestyle risk factors are modifiable | Ongoing | Environmental enrichment | src-obesity-001 |
| Cats on ad-lib feeding | Feeding pattern is modifiable | Ongoing | Feeding management | src-obesity-001, src-obesity-005 |

## Guardrail

Do not conflate prevention with early treatment. The safe architecture is:

1. **Strategic orientation:** Prevention is preferable to treatment because treatment has limitations
2. **Target population:** Post-gonadectomy kittens 5-12 months as primary focus
3. **Strategy categories:** Dietary and feeding management (specific protocols pending)
4. **Timing:** Prevention efforts should initiate at known risk transitions (neutering)
5. **Modifiable factors:** Focus on lifestyle and feeding factors that can be changed

## What The Module Can Say Safely

- Prevention is strategically preferable to treatment for feline obesity
- Treatment is slow, often unsuccessful, and not without consequences
- Post-gonadectomy kittens aged 5-12 months are the primary target population
- Prevention strategies include dietary and feeding management
- Identifying high-risk populations is crucial for developing preventive strategies
- The post-neutering period is a key intervention window

## What The Module Should Not Say Yet

- Do not recommend specific dietary protocols (need full-text)
- Do not recommend specific feeding schedules or portions
- Do not provide owner-facing prevention checklists
- Do not claim specific prevention success rates
- Do not state how much prevention reduces obesity risk quantitatively

## Current Role

Use this page as the obesity prevention handbook. The source-card layer has 4/87 deep-extracted papers, with src-obesity-005 as the primary prevention anchor. Next gains come from:
- Full-text extraction of specific dietary protocols
- Full-text extraction of feeding management recommendations
- Evidence for prevention program effectiveness
- Owner intervention study data from Tier 2 sources
