# /what-is-page

Creates or upgrades bilingual "what-is" explanation pages for disease modules. These are simple, accessible pages for ordinary users explaining what a disease is.

## Trigger

- `/what-is-page create <disease>` — create new what-is page
- `/what-is-page upgrade <disease>` — upgrade Chinese-only to bilingual
- `/what-is-page list` — show which diseases have/need what-is pages

## Input

- `disease`: Disease module name (ckd, fip, hcm, ibd, diabetes, fcv, obesity, cancer)

## Prerequisites

- Source cards must exist in `raw/papers/src-{disease}-*.md`
- At least 3-4 deep-extracted sources with clinical overview content

## Template Structure

```markdown
---
id: topic-{disease}-what-is
type: topic
topic: {disease}
species: feline
disease: {disease name}
question_type: what-is
source_ids: [{source list}]
last_compiled_at: {today}
confidence: medium
verification_status: compiled
decision_grade: no
language_qa_status: not_checked
owner: codex
status: active
---

# 什么是猫{disease-zh}？ / What is Feline {Disease}?

## Quantified Claim Traceability

| Claim | Source IDs | Boundary |
|---|---|---|
| {quantified claim} | {sources} | {limitation} |

## 简单回答 / Simple Answer

**{Chinese answer - 1-2 sentences}**

{English answer - 1-2 sentences}

[source_supported_conclusion: {source-id}]

## 有多常见？ / How Common Is It?

{Prevalence info in Chinese}

{Prevalence info in English}

[source_supported_conclusion: {sources}]

## 有什么症状？ / What Are the Signs?

{Symptoms section with bilingual tables}

### 常见症状 / Common Signs

| 症状 | Sign |
|------|------|
| {Chinese} | {English} |

[source_supported_conclusion: {sources}]

## 如何诊断？ / How Is It Diagnosed?

{Diagnosis info with bilingual tables}

[source_supported_conclusion: {sources}]

## 可以治疗吗？ / Can It Be Treated?

{Treatment/management info}

[source_supported_conclusion: {sources}]

## 本页边界 / Page Boundary

本页提供猫{disease-zh}的基础解释。如需了解更多：
- {link to related pages}

This page provides a basic explanation. For more details:
- {link to related pages}

**本页不提供：** 具体用药建议、治疗方案选择、预后预测。这些需要兽医根据个体情况评估。

**This page does not provide:** Specific medication advice, treatment protocol selection, or prognosis predictions. These require veterinary assessment based on individual circumstances.
```

## Workflow

### Step 1: Check Existing State

```bash
# Check if page exists
ls topics/{disease}/what-is-{disease}.md 2>/dev/null

# Check source coverage
grep -l "diseases:.*{disease}" raw/papers/*.md | wc -l

# Find best source candidates
grep -l "verification_status: deep_extracted" raw/papers/src-{disease}-*.md | head -5
```

### Step 2: Select Sources

Choose 3-5 sources that cover:
- Disease definition/mechanism (1-2)
- Epidemiology/prevalence (1)
- Clinical signs/diagnosis (1-2)
- Treatment/management (1)

Prefer `deep_extracted` sources over `abstract_weighted`.

### Step 3: Extract Key Information

For each source, extract:
- Quantified claims (prevalence, thresholds, timeframes)
- Clinical signs lists
- Diagnostic markers
- Treatment options

### Step 4: Create/Update Page

Write bilingual content following the template structure.

Key requirements:
- Every section has Chinese followed by English
- Tables use bilingual format: `| 症状 | Sign |`
- All claims have `[source_supported_conclusion: src-xxx]` tags
- Quantified claims have traceability table entries

### Step 5: Update Best-Answer-Surfaces

Edit `system/indexes/best-answer-surfaces.md`:
- Add page to Simple Explanation surface
- Update last_compiled_at

### Step 6: Run Health Check

```bash
python3 scripts/health.py 2>&1 | grep -E "Reader page|Quantified claim"
```

## Quantified Claim Traceability

Any numeric claim needs an entry in the traceability table:

| Claim Type | Example | Needs Traceability |
|------------|---------|-------------------|
| Prevalence | "30-40% of cats over 10 years" | YES |
| Staging cutoffs | "Stage 2: 1.6-2.8 mg/dL" | YES |
| Treatment duration | "84 days (12 weeks)" | YES |
| Age groups | "more common in older cats" | NO (qualitative) |

## Samples Processed (2026-06-08)

| Disease | Action | Sources Used |
|---------|--------|--------------|
| IBD | Created | src-ibd-001, src-ibd-003, src-ibd-010, src-ibd-015 |
| HCM | Created | src-hcm-001, src-hcm-002, src-hcm-003, src-hcm-009, src-hcm-024 |
| Diabetes | Created | src-diabetes-001, src-diabetes-005, src-diabetes-010, src-diabetes-020 |
| FCV | Created | src-fcv-001, src-fcv-002, src-fcv-004, src-fcv-009 |
| FIP | Upgraded to bilingual | src-fip-003, src-fip-005, src-fip-006 |

## Bilingual Upgrade Pattern

For Chinese-only pages needing English:

1. Keep all Chinese content intact
2. Add English parallel after each Chinese section
3. Convert single-language tables to bilingual format:

**Before:**
```markdown
| 症状 | 表现 |
|------|------|
| 肚子变大 | 腹部积液 |
```

**After:**
```markdown
| 症状 | Sign | 表现 / Presentation |
|------|------|---------------------|
| 肚子变大 | Abdominal distension | 腹部积液 / Fluid buildup |
```

## Content Guidelines

### Include:
- Simple, accessible language (not technical jargon)
- Common signs that owners would notice
- When to seek veterinary care
- Treatment options at high level

### Do NOT Include:
- Specific drug names/dosages
- Detailed diagnostic protocols
- Prognosis predictions
- Survival statistics

### Page Boundary Disclaimer

Always include the "本页不提供/This page does not provide" disclaimer to prevent overreach.

## Output Summary

After completion, report:

| Item | Value |
|------|-------|
| Disease | {disease} |
| Action | created / upgraded |
| Sources | {source count} |
| Traceability claims | {count} |

## Related Skills

- `/cancer-deep-extract` — deep extract sources for what-is content
- `/low-word-card-enrich` — enrich source cards if needed
- `/topic-recompile` — recompile topic pages after changes
