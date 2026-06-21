# Deep Extraction Prompt V2

Use this prompt when a source is important enough to justify deeper extraction beyond first-pass ingest.

This prompt is designed for the current `feline-research-os` workflow.
It is not a generic summarization prompt.
Its job is to turn one high-value source into:

- denser source-card content
- cleaner topic write-back
- safer evidence promotion
- **card-level synthesis fields that make Research Mode recommendations compelling**

## Best Use Cases

- guideline papers
- major review papers
- primary studies that connect mechanism and endpoints
- regulatory documents that shape route selection
- industry reports or interviews worth preserving at source depth

## Not The Right Use Case

- low-value clipping
- duplicate source coverage
- materials that only need title/abstract ingest

## Operating Principle

`first-pass ingest` answers:
what is this source roughly about?

`deep extraction` answers:
what exactly does this source say, how does it build its case, and what can safely be promoted into the vault?

## Required Output Discipline

Always preserve the vault's evidence policy:

- `quoted_fact`
- `source_supported_conclusion`
- `llm_inference`
- `core_argument` (new in v2)
- `study_design` (new in v2)
- `implicit_premise` (new in v2)
- `title_gap` (new in v2)
- `evidence_boundary` (new in v2)
- `tension_with` (new in v2)

Do not collapse these layers.

## Workflow

### Phase 0: Sequential Micro-Analysis

Work through the source in natural order.
Split it into paragraph units or content units by topic shift, not by arbitrary token count.
For each unit, answer:

1. `core_claim`
What is this unit really saying?

2. `implicit_premise`
What assumptions must be true for this claim to hold?

3. `relation_to_previous`
Is this a continuation, turn, qualification, contradiction, or new branch?

4. `hard_details`
Capture all hard information:
- numbers
- dates
- names
- compounds
- endpoints
- products
- studies
- organizations
- routes
- guidance references

5. `tension_or_surprise`
Optional, but include when useful.
Note contradictions, overclaims, or friction with other parts of the same source.

#### Output Template

```md
#### Unit [N]: [one-line label]

- core_claim:
- implicit_premise:
- relation_to_previous:
- hard_details:
- tension_or_surprise:
```

### Phase 0.5: Card-Level Synthesis (NEW in V2)

After completing Phase 0 micro-analysis, synthesize into card-level fields.
These fields power Research Mode's "为什么值得读" and "关键发现" sections.

**The goal: make a researcher want to open this paper without having seen the abstract.**

1. `core_argument` (required)
   - The paper's central thesis in one complete sentence
   - Must be a specific claim, not a topic description
   - Wrong: "This paper is about feline HCM"
   - Wrong: "This study investigates biomarkers"
   - Right: "Mild-to-moderate LV hypertrophy in cats cannot be diagnosed by echocardiography alone and remains a diagnosis of exclusion"
   - Right: "LACI-ED reflects disease severity but lacks discriminative power for thromboembolism prediction"

2. `study_design` (optional, include when available)
   - Brief description of the research method and cohort
   - Format: "研究类型，样本描述，主要方法"
   - Examples:
     - "回顾性横断面研究，91 只猫按 ACVIM 分期，采用常规及斑点追踪超声心动图"
     - "前瞻性病例对照研究，21 只 HCM 猫 vs 26 只对照，采用 TMAD"
     - "多中心回顾性研究，273 张腹背位胸片，5 种 CNN 架构"
   - Skip if the paper does not disclose sufficient methodological detail

3. `implicit_premise` (required)
   - What must be true for the core argument to hold?
   - Usually an unstated methodological or theoretical assumption
   - Examples:
     - "Assumes the echocardiographic cutoffs validated in other populations apply to this cohort"
     - "Assumes proteomic differences reflect pathophysiology rather than confounding"
     - "Assumes retrospective staging accuracy is equivalent to prospective assessment"

4. `title_gap` (required for compelling recommendations)
   - Why this paper is worth reading beyond what the title/abstract suggests
   - This is what makes a researcher WANT to open the paper
   - Three patterns:
     a) Hidden finding: the paper contains a discovery the title doesn't mention
     b) Title contradiction: data in the paper challenges what the title claims
     c) Value shift: the title says A, but the real value is in B
   - Examples:
     - "标题说prevalence，但真正价值是发现了两个遗传标记的分离模式——ALMS1纯合子全部健康，A31P仅在HCM组出现"
     - "标题是诊断准确性研究，但图5揭示了临床决策的困境：66%阳性预测值意味着每3个阳性结果只有2个真病例"
     - "摘要强调治疗有效，但表3显示脱落率40%——这不是有效性问题而是可行性警告"
   - Wrong: Generic statements like "interesting findings" or "important study"
   - Wrong: Simply rephrasing the abstract
   - Right: Specific insight that creates intellectual tension or curiosity

5. `evidence_boundary` (required)
   - What questions does this paper explicitly NOT answer?
   - What would you need to look elsewhere for?
   - Examples:
     - "Does not establish whether LACI-ED changes predict future events (cross-sectional only)"
     - "Cannot determine if coagulation changes precede or follow HCM development"
     - "Sample size insufficient for subgroup analysis by breed"

6. `tension_with` (optional, include when you can identify specific sources)
   - Does this paper contradict, extend, or qualify findings from other vault sources?
   - Format:
     ```yaml
     tension_with:
       - source_id: "src-hcm-002"
         type: "contradicts|extends|qualifies"
         description: "Brief description of the tension"
     ```
   - Examples:
     - contradicts: "Reports different NT-proBNP cutoffs than src-hcm-015"
     - extends: "Adds TMAD to the biomarker panel described in src-hcm-045"
     - qualifies: "Shows the correlation from src-hcm-023 only holds for stage C cats"

#### Output Template

```yaml
evidence_policy:
  # Existing fields
  quoted_fact:
    - "..."
  source_supported_conclusion:
    - "..."
  llm_inference:
    - "..."

  # New V2 fields
  study_design: "研究类型，样本描述，主要方法（可选）"
  core_argument: "One-sentence thesis statement"
  implicit_premise: "Unstated assumption the argument depends on"
  title_gap: "Why this paper is worth reading beyond what the title suggests"
  evidence_boundary: "What this paper does not/cannot answer"
  tension_with:
    - source_id: "src-xxx-nnn"
      type: "contradicts|extends|qualifies"
      description: "Description of the tension"
```

### Phase 1: Topic Reconstruction

After Phase 0 and 0.5, regroup the source by naturally emerging themes.

Do not force common categories if the source itself does not support them.

For each theme:

- rewrite the content in fluent prose
- preserve all important hard information
- keep speaker/author attribution clear
- do not flatten disagreements

#### Output Template

```md
## Theme: [name]

[full reconstruction]

### Key Quote
> "..."

### Hard Information
- ...
```

### Phase 2: Claim-Evidence Structure

For each theme, extract:

- `claim`
- `support`
- `details`
- `implicit_premise`

#### Output Template

```md
### [Theme] Key Points

**Claim 1**
- support:
- details:
- implicit_premise:
```

### Phase 3: Vault Promotion Check

Before producing final write-back, answer:

1. what belongs in the source card only?
2. what can be promoted into topic pages now?
3. what should remain provisional?
4. what conflicts with current vault content?
5. what new entities, topic pages, or output updates become justified?

#### Output Template

```md
## Promotion Check

- source_card_updates:
- topic_write_back_targets:
- not_safe_to_promote_yet:
- conflicts_with_existing_vault:
- new_entities_or_pages_justified:
```

## Current Project Adaptation

When using this prompt in `feline-research-os`, prefer these write-back targets:

- `raw/papers/*.md`
- `topics/ckd/*.md`
- `entities/endpoints/*.md`
- `entities/mechanisms/*.md`
- `entities/regulations/*.md`
- `entities/symptoms/*.md`

Raw source material should remain in its original language.
Do not translate the raw layer just to make the vault look uniform.

## Domain-Specific Translation Layer

If the source is Chinese and the write-back target is English, or vice versa:

- keep raw source material in its original language
- apply translation only to compiled write-back or derived output layers
- preserve drug names, disease names, endpoint terms, and regulatory references exactly
- prefer industry-standard veterinary phrasing over literal translation
- keep tone aligned to source type:
  - guideline: precise
  - review: analytical
  - marketing/industry interview: readable but still exact
- never smooth over uncertainty in the original

For current project use, accuracy beats style.
Especially protect:

- compounds
- dose units
- route names
- agencies
- regulatory pathways
- disease names
- endpoint names

For full project policy, follow:

- [bilingual content policy](bilingual-content-policy.md)

## Quality Gates for V2 Fields

Before finalizing extraction, verify:

1. `core_argument` is > 50 characters and is a complete claim (not a topic label)
2. `evidence_boundary` is non-empty and specific (not generic like "needs more research")
3. At least one `quoted_fact` contains hard data (numbers, p-values, sample sizes)
4. `title_gap` creates specific intellectual tension (not generic praise)
5. If this paper engages with vault sources you know, `tension_with` is populated

See [V2 Quality Rubric](../schemas/v2-quality-rubric.md) for A/B/C/F grading standards.

---

## Good vs Bad Examples

### core_argument

**Grade A (specific claim with conditions):**
```
"轻中度左心室肥厚在猫中无法仅靠超声心动图确诊——仍是排除性诊断；生物标志物不应独立用于诊断"
```
Why it works: Contains stance verb (无法), specific condition (轻中度), and falsifiable structure.

**Grade C (topic description):**
```
"这篇论文研究了 HCM 生物标志物的相关研究进展"
```
Why it fails: Describes what the paper is about, not what it argues. No stance.

**Grade F (generic):**
```
"这是一篇关于猫疾病的重要研究"
```
Why it fails: Empty of content, pure placeholder.

---

### title_gap

**Grade A (specific contrast with evidence):**
```
"标题说 prevalence，但真正价值是发现了表3中40%脱落率数据——这不是有效性问题而是可行性警告"
```
Why it works: Clear "标题说X，但Y" pattern, references specific data (表3, 40%), explains impact.

**Grade B (contrast without specifics):**
```
"标题强调机制研究，但本文也包含临床数据分析"
```
Why it's B: Has contrast marker (但), but no specific evidence reference.

**Grade F (praise only):**
```
"这是一篇非常重要的有价值的研究"
```
Why it fails: No contrast, just generic praise.

---

### evidence_boundary

**Grade A (methodology-grounded):**
```
"横断面设计无法确定 LACI-ED 变化是否预测临床恶化；样本量（n=91）不支持按品种分亚组"
```
Why it works: Names design type (横断面), names specific variable (LACI-ED), specifies impact.

**Grade B (limitation without design link):**
```
"本研究未涉及长期预后和生存率分析，未评估治疗持久性"
```
Why it's B: States limitation clearly but doesn't ground it in methodology.

**Grade F (boilerplate):**
```
"需要更多研究来进一步验证"
```
Why it fails: Pure boilerplate, says nothing specific.

---

### quoted_fact Discipline

**Good (hard data):**
```
- "n=91 cats staged by ACVIM criteria"
- "Sensitivity 78%, specificity 92%, AUC 0.89"
- "Median survival 14 months (range 3-48)"
```

**Bad (contains interpretation):**
```
- "This source supports keeping the biomarker branch separate"
- "Dietary management should be considered alongside pharmacotherapy"
```
Why bad: Contains "supports", "should" — interpretation belongs in `source_supported_conclusion` or `llm_inference`.

## Recommended Current Use

This prompt is especially useful right now for:

1. HCM papers with detailed echocardiographic or biomarker data
2. High-evidence-level papers (guidelines, systematic reviews, meta-analyses)
3. Papers that conflict with or extend existing vault content
4. Recent (2020+) original studies with clinical endpoints

## What Success Looks Like

A good V2 deep extraction should let a later reader:

- understand the source without reopening it
- know exactly what is defensible
- see where the source is weak
- **want to read the original paper based on the "为什么值得读" hook**
- **understand the paper's contribution and limits from the "关键发现" section**
- update source cards and topic pages with low hallucination risk
