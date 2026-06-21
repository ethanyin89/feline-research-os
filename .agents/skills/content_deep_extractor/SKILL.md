---
name: content_deep_extractor
description: Systematic process for performing deep extraction on raw literature cards in Feline Research OS.
---

# Content Deep Extractor Skill

This skill provides a standardized, high-fidelity methodology for extracting full-text or abstract content from literature sources in the Feline Research OS vault. It replaces empty `title_only` placeholders with specific clinical and study parameters (e.g., sample sizes, cohorts, statistical significance).

## Deep Extraction Workflow

Follow these steps when extracting a placeholder card:

### Step 1: Identify Targets
Find candidate source cards in `system/indexes/research-depth-queue.md` or look for files in `raw/papers/` that have:
* `status: ingested`
* `verification_status: title_only` or `abstract_weighted`
* `extraction_depth: partial`

### Step 2: Retrieve Clinical Context & Auto-Scrape Figures
Run the automated fetch script to retrieve abstracts/metadata and download PMC figures for queue candidates:
```bash
.venv/bin/python scripts/fetch_abstracts.py --limit 4
```
This script fetches metadata, resolves PMCIDs via the official converter API, scrapes and downloads PMC figure images to `raw/images/<disease>/`, and saves the structured context to `scratch/fetched_abstracts.json`.

Review the fetched metadata in `scratch/fetched_abstracts.json` and retrieve any missing full-text context. You must locate:
1. Enrolled sample sizes (n) and cohort breakdowns.
2. Concrete quantitative numbers (e.g., median concentration levels, correlation coefficients, p-values).
3. Primary study limitations (lack of control groups, small sample sizes, high dropout rates).
4. Local paths to downloaded figures (under `local_assets` in the JSON) to reference and embed within the deep-extracted markdown cards.

### Step 3: Populate Card Structure
Overwrite the placeholder markdown card under `raw/papers/src-<disease>-<id>.md` using the template below.

#### Template:
```markdown
---
id: src-<disease>-<id>
type: source
title: "Full Paper Title"
source_kind: paper
species: feline
diseases: [<Diseases>]
models: [<Models/Methods>]
endpoints: [<Endpoints Measured>]
evidence_level: <original-study | review | guideline>
year: <Year>
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
decision_grade: <yes | no>
language_qa_status: bilingual_checked
tags: [<tags>]
links:
  doi: "<doi>"
  url: "<url>"
  local_assets: []
abstract: "Complete abstract text here..."
methods_summary: "Detailed methodology description here..."
evidence_policy:
  quoted_fact:
    - "Direct, quantitative facts with sample sizes and p-values."
  source_supported_conclusion:
    - "Welfare, feasibility, or diagnostic conclusions directly supported."
  llm_inference:
    - "Conservative clinical or therapeutic inferences."
  # V2 enhanced fields (required for Research Mode presentation)
  study_design: "研究类型，样本描述，主要方法"
  core_argument: "论文的核心论点——必须是完整主张，不是话题描述"
  implicit_premise: "论点成立需要什么前提条件"
  unexpected_finding: "意外发现或反直觉结果（可选）"
  title_gap: "标题说X，但真正发现是Y——为什么值得读"
  evidence_boundary: "这篇论文明确回答不了什么问题"
---

# Full Paper Title

## Evidence-Depth Caveat

This card is based on complete publication text. It is deep-extracted as a [study type] study.

## One-Line Summary

[Clear, quantitative one-line summary]

## Why It Matters For Feline [Disease]

[Significance of findings, clinical translation]

## Key Findings

### quoted_fact

* [Bullet 1]
* [Bullet 2]

### source_supported_conclusion

* [Bullet 1]

### llm_inference

* [Bullet 1]

## Study Design Details

### Cohort Summary

| Parameter | Value |
|---|---|

## Linked Entities

- diseases: [<Diseases>]
- models: [<Models>]
- endpoints: [<Endpoints>]
- mechanisms: [<Mechanisms>]
```

### Step 4: Recompile & Verify
Once the markdown files have been edited:
1. Recompile the index mappings:
   ```bash
   .venv/bin/python scripts/sync_indexes.py
   ```
2. Verify presentation rendering and routing compliance:
   ```bash
   .venv/bin/python scripts/check_research_mode_presentation.py
   ```
3. Run the Streamlit test page to preview card display formatting:
   ```bash
   ./scripts/run_test_page.sh
   ```

## V2 Enhanced Fields (Required)

All deep-extracted cards MUST include V2 fields for Research Mode presentation.

### Quality Gates

Before finalizing extraction, verify:

1. `core_argument` is > 50 characters and is a complete claim (not a topic label)
   - Wrong: "This paper is about feline HCM"
   - Right: "轻中度左心室肥厚在猫中无法仅靠超声心动图确诊——仍是排除性诊断"

2. `evidence_boundary` is non-empty and specific (not generic like "needs more research")
   - Wrong: "需要更多研究"
   - Right: "综述层面无法提供个体化治疗方案；轻中度肥厚的具体排除标准仍需参考原始研究"

3. At least one `quoted_fact` contains hard data (numbers, p-values, sample sizes)

4. `title_gap` creates specific intellectual tension (not generic praise)
   - Wrong: "这是一篇重要的研究"
   - Right: "标题说prevalence，但真正价值是发现了两个遗传标记的分离模式"

5. `study_design` follows format: "研究类型，样本描述，主要方法"
   - Example: "回顾性横断面研究，91 只猫按 ACVIM 分期，采用常规及斑点追踪超声心动图"

### Mis-ingestion Check

Before extraction, verify the paper is actually about feline species:
- "Feline sarcoma-related protein" (Fer) is a protein name, not species
- "FELINE trial" may be a human study acronym
- "Feline Wolf Net" is an ML algorithm name
- Check abstract/methods for actual cat subjects

If mis-ingested, add to V2 fields:
```yaml
study_design: "**误收录警告**：这是人类研究——[原因]"
core_argument: "N/A——人类研究；[简述]"
```

### Reference

Full V2 extraction methodology: `system/prompts/deep-extraction-prompt-v2.md`

## Batch V2 Field Extraction

For cards that already have deep extraction but lack V2 fields, use the batch script:

```bash
# Dry run to see what would be processed
OPENROUTER_DAILY_BUDGET_USD=1.00 .venv/bin/python scripts/add_v2_fields.py --disease fcv --limit 5 --dry-run

# Process 5 cards
OPENROUTER_DAILY_BUDGET_USD=1.00 .venv/bin/python scripts/add_v2_fields.py --disease fcv --limit 5

# Process a single file
OPENROUTER_DAILY_BUDGET_USD=1.00 .venv/bin/python scripts/add_v2_fields.py --file raw/papers/src-fcv-042.md
```

### Current V2 Coverage (2026-06-21)

| Disease | With V2 | Total | Coverage |
|---------|---------|-------|----------|
| Cancer | 111 | 111 | 100% |
| IBD | 26 | 126 | 21% |
| Diabetes | 25 | 121 | 21% |
| CKD | 38 | 197 | 19% |
| FCV | 58 | 296 | 20% |
| Obesity | 15 | 95 | 16% |
| HCM | 32 | 226 | 14% |
| FIP | 33 | 242 | 14% |
| **Total** | **338** | **1414** | **24%** |

Update counts:
```bash
for d in cancer hcm ckd fip fcv ibd diabetes obesity; do
  echo "$d: $(grep -l 'core_argument:' raw/papers/src-${d}-*.md 2>/dev/null | wc -l)"
done
```
