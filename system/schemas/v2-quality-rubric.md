# V2 Field Quality Rubric

This document defines the grading standards for V2 enhanced fields in source cards.
Use this rubric for:

1. **Automated quality gates** — `scripts/v2_quality_gates.py` implements programmable checks
2. **Manual auditing** — human reviewers use this rubric for calibration
3. **LLM prompt guidance** — examples inform extraction prompts

---

## Grading Scale

| Grade | Meaning | Action |
|-------|---------|--------|
| A | High-quality, defensible content | Write to card |
| B | Complete but imprecise | Write to card |
| C | Weak but salvageable | Write with `needs_review: true` flag |
| F | Empty, generic, or wrong | Block write, queue for re-extraction |

---

## 1. core_argument

The paper's central thesis in one complete sentence. Must be a **specific, falsifiable claim**, not a topic description.

### Grade A — Specific claim with conditions

Contains:
- Stance verb (是、无法、需要、不能、优于、导致、remains、cannot、requires)
- Specific entity, threshold, or condition
- Falsifiable structure

**Examples:**
- "轻中度左心室肥厚在猫中无法仅靠超声心动图确诊——仍是排除性诊断"
- "LACI-ED reflects disease severity but lacks discriminative power for thromboembolism prediction"
- "NT-proBNP combined with cardiac troponin I provides better prognostic stratification than either marker alone in cats with HCM"

### Grade B — Complete claim, imprecise conditions

Contains a complete claim but:
- Conditions are vague (e.g., "some cats", "certain conditions")
- Missing specific thresholds or entities
- Still falsifiable but less sharply

**Examples:**
- "猫肥胖症是最常见的多因素营养障碍" (true claim, but "多因素" is vague)
- "Biomarkers are useful but have limitations" (claim present, but which biomarkers?)

### Grade C — Topic description, not a claim

Describes what the paper is about rather than what it argues.

**Examples:**
- "这篇论文研究了 HCM 生物标志物"
- "This study investigates the relationship between obesity and diabetes"
- "The review covers feline CKD pathophysiology"

### Grade F — Empty, generic, or factually wrong

**Examples:**
- "这是一篇关于猫疾病的重要研究"
- "This is a comprehensive study"
- "" (empty)
- Factually incorrect statements

### Programmable Checks

```python
STANCE_VERBS_ZH = ["是", "无法", "需要", "不能", "优于", "导致", "仍是", "表明", "证明", "支持"]
STANCE_VERBS_EN = ["is", "are", "cannot", "remains", "requires", "demonstrates", "shows", "proves", "fails", "lacks", "provides"]
TOPIC_MARKERS = ["这篇论文", "这项研究", "本研究", "本文", "this paper", "this study", "the study", "this review"]

def check_core_argument(text: str) -> tuple[str, str]:
    """Returns (grade, reason)"""
    if not text or len(text) < 30:
        return ("F", "empty or too short")

    text_lower = text.lower()

    # F: Topic description pattern
    for marker in TOPIC_MARKERS:
        if text_lower.startswith(marker.lower()):
            return ("C", "topic description, not a claim")

    # Check for stance verbs
    has_stance = any(v in text for v in STANCE_VERBS_ZH) or \
                 any(v in text_lower for v in STANCE_VERBS_EN)

    # Check for specific entities (numbers, thresholds, named entities)
    has_specifics = bool(re.search(r'\d+|%|mg|kg|ACVIM|HCM|CKD|FIP|NT-proBNP|SDMA', text))

    if has_stance and has_specifics:
        return ("A", "specific claim with conditions")
    elif has_stance:
        return ("B", "complete claim, imprecise conditions")
    else:
        return ("C", "no clear stance or claim")
```

---

## 2. title_gap

Why this paper is worth reading beyond what the title suggests. Must create **specific intellectual tension or curiosity**.

### Grade A — Specific contrast with intellectual tension

Pattern: "标题说X，但真正发现是Y——[原因/影响]"

Contains:
- Contrast marker (但、然而、而不是、相反、真正、but、however、actually)
- Specific X and specific Y
- Explains why the gap matters

**Examples:**
- "标题说 prevalence，但真正价值是发现了两个遗传标记的分离模式——ALMS1 纯合子全部健康，A31P 仅在 HCM 组出现"
- "摘要强调治疗有效，但表 3 显示脱落率 40%——这不是有效性问题而是可行性警告"
- "标题是诊断准确性研究，但图 5 揭示了临床决策的困境：66% 阳性预测值意味着每 3 个阳性结果只有 2 个真病例"

### Grade B — Points out hidden value, weak tension

Indicates something beyond the title but:
- Contrast is soft ("also includes", "additionally")
- Gap is mentioned but impact unclear

**Examples:**
- "标题强调机制，但本文也包含临床数据"
- "Title focuses on diagnosis but the discussion has treatment implications"

### Grade C — Restates abstract, no real contrast

**Examples:**
- "标题概括主题，内容更详细"
- "The title captures the main finding accurately"
- "This paper covers what the title suggests and more"

### Grade F — Generic praise or title repetition

**Examples:**
- "这是一篇重要的研究"
- "This is a valuable paper"
- "Worth reading" (no specifics)
- "" (empty)

### Programmable Checks

```python
CONTRAST_MARKERS_ZH = ["但", "然而", "而不是", "相反", "真正", "实际上", "事实上"]
CONTRAST_MARKERS_EN = ["but", "however", "actually", "instead", "contrary", "real value", "truly"]
PRAISE_ONLY_MARKERS = ["重要", "有价值", "全面", "comprehensive", "important", "valuable", "worth reading"]

def check_title_gap(text: str) -> tuple[str, str]:
    """Returns (grade, reason)"""
    if not text or len(text) < 20:
        return ("F", "empty or too short")

    text_lower = text.lower()

    # Check for contrast markers
    has_contrast = any(m in text for m in CONTRAST_MARKERS_ZH) or \
                   any(m in text_lower for m in CONTRAST_MARKERS_EN)

    # Check for praise-only (bad sign if no contrast)
    is_praise_only = any(m in text for m in PRAISE_ONLY_MARKERS) and not has_contrast

    if is_praise_only:
        return ("F", "generic praise without specific contrast")

    # Check for specific references (figures, tables, numbers)
    has_specifics = bool(re.search(r'图|表|Figure|Table|Fig\.|Tab\.|数据|data|\d+%|\d+/\d+', text))

    if has_contrast and has_specifics:
        return ("A", "specific contrast with evidence reference")
    elif has_contrast:
        return ("B", "contrast present but lacks specific evidence")
    else:
        return ("C", "no clear contrast or intellectual tension")
```

---

## 3. evidence_boundary

What questions this paper explicitly cannot answer. Must be **specific and methodology-grounded**.

### Grade A — Methodology-based specific limitation

Contains:
- Research design term (横断面、回顾性、单中心、cross-sectional, retrospective, single-center)
- Specific unanswered question linked to design

**Examples:**
- "横断面设计无法确定 LACI-ED 变化是否预测临床恶化"
- "Retrospective design cannot establish causality between treatment and outcome"
- "Sample size insufficient for subgroup analysis by breed (n=3 per breed)"

### Grade B — States limitation without methodology link

Identifies what's missing but doesn't ground it in design:
- "未涉及具体治疗方案的效果评估"
- "Does not address long-term outcomes"

### Grade C — Vague limitation

**Examples:**
- "样本量小" (how small? what's the impact?)
- "Limited generalizability"
- "More research needed in this area"

### Grade F — Empty or pure boilerplate

**Examples:**
- "需要更多研究"
- "Limitations exist"
- "Further research is warranted"
- "" (empty)

### Programmable Checks

```python
DESIGN_TERMS_ZH = ["横断面", "回顾性", "前瞻性", "单中心", "多中心", "随机", "对照", "队列", "病例系列"]
DESIGN_TERMS_EN = ["cross-sectional", "retrospective", "prospective", "single-center", "multi-center",
                   "randomized", "controlled", "cohort", "case series", "case-control"]
BOILERPLATE_PHRASES = [
    "需要更多研究", "进一步研究", "更多研究", "样本量有限",
    "more research needed", "further research", "limitations exist", "future studies"
]

def check_evidence_boundary(text: str) -> tuple[str, str]:
    """Returns (grade, reason)"""
    if not text or len(text) < 20:
        return ("F", "empty or too short")

    text_lower = text.lower()

    # Check for pure boilerplate
    for phrase in BOILERPLATE_PHRASES:
        if phrase in text_lower and len(text) < 50:
            return ("F", "pure boilerplate")

    # Check for design terms
    has_design = any(t in text for t in DESIGN_TERMS_ZH) or \
                 any(t in text_lower for t in DESIGN_TERMS_EN)

    # Check for specific impact (numbers, named variables)
    has_specifics = bool(re.search(r'\d+|LACI|NT-proBNP|SDMA|纤维化|thromboembolism|mortality', text))

    if has_design and has_specifics:
        return ("A", "methodology-grounded specific limitation")
    elif has_design or has_specifics:
        return ("B", "limitation stated, partial grounding")
    else:
        return ("C", "vague limitation")
```

---

## 4. Composite Scoring

The overall V2 extraction quality uses weighted scoring:

| Field | Max Points |
|-------|-----------|
| core_argument | 3 (A=3, B=2, C=1, F=0) |
| title_gap | 3 |
| evidence_boundary | 3 |
| hard_data presence | 2 (has quoted_fact with numbers) |
| coherence check | 1 (fields don't contradict each other) |
| **Total** | **12** |

### Grade Thresholds

| Total Score | Grade | Action |
|-------------|-------|--------|
| 10-12 | A | Write to card |
| 7-9 | B | Write to card |
| 4-6 | C | Write with `needs_review: true` |
| 0-3 | F | Block write, queue re-extraction |

---

## 5. Special Checks

### Mis-ingestion Detection

If `study_design` starts with "**误收录警告**" or contains non-feline species as primary subject:
- Grade: F
- Action: Block and flag for manual review

### quoted_fact Discipline

`quoted_fact` items should not contain:
- Interpretation words: "支持", "表明这意味着", "suggests that"
- Vault routing language: "branch", "module", "should be placed"
- Future speculation: "可能会", "might lead to"

Violation → deduct 1 point from coherence score.

---

## 6. Audit Sampling Strategy

For the 338 V2 cards, stratified sampling:

| Stratum | Sample Size | Selection Criteria |
|---------|-------------|---------------------|
| High auto-score (10+) | 10 | Verify A quality holds |
| Medium auto-score (6-9) | 20 | Calibrate B/C boundary |
| Low auto-score (<6) | 20 | Confirm F cards need rework |

Per-disease target: 6-8 cards minimum to ensure coverage.

---

## 7. Reference Examples

### A-Grade Card Example (src-hcm-001)

```yaml
core_argument: "轻中度左心室肥厚在猫中无法仅靠超声心动图确诊——仍是排除性诊断；生物标志物不应独立用于诊断；目前没有治疗能逆转或减缓心肌病进程"
# Grade: A — specific falsifiable claim with conditions

title_gap: "标题是 HCM 综述系列，但真正警告是诊断边界：轻中度肥厚仍是排除性诊断，生物标志物不能独立使用，没有治疗能逆转——这直接限制了筛查策略的过度自信"
# Grade: A — specific contrast with methodology impact

evidence_boundary: "综述层面无法提供个体化治疗方案；轻中度肥厚的具体排除标准仍需参考原始研究"
# Grade: B — limitation stated, partial methodology grounding
```

### C-Grade Card Example (needs improvement)

```yaml
core_argument: "这篇论文研究了猫糖尿病的治疗选择"
# Grade: C — topic description, not a claim

title_gap: "内容比标题更详细"
# Grade: C — no specific contrast

evidence_boundary: "需要更多研究"
# Grade: F — pure boilerplate
```

---

## 8. Implementation Files

| File | Purpose |
|------|---------|
| `scripts/v2_quality_gates.py` | Automated quality checks |
| `scripts/audit_v2_cards.py` | Audit sampling and reporting |
| `scripts/add_v2_fields.py` | Integration point for gate pipeline |
| `scripts/health.py` | Quality distribution in health reports |
| `system/prompts/deep-extraction-prompt-v2.md` | LLM prompt with quality examples |
