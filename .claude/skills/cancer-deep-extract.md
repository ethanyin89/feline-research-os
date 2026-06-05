# /cancer-deep-extract

Deep extraction skill for feline cancer source cards. Upgrades abstract-level cards to full extraction with structured analysis.

## Trigger

- `/cancer-deep-extract <source-id>` — e.g., `/cancer-deep-extract src-cancer-045`
- `/cancer-deep-extract list` — show candidates (abstract-level cancer sources)

## Input

- `source-id`: A source card ID like `src-cancer-045`
- Must exist in `raw/papers/` with `extraction_depth: abstract`

## Workflow

### Step 1: Validate Source

```bash
# Check source exists and is at abstract level
grep -l "^id: $SOURCE_ID" raw/papers/*.md
grep "extraction_depth:" raw/papers/$SOURCE_ID.md
```

Abort if:
- Source doesn't exist
- Already at `extraction_depth: full`

### Step 2: Fetch Full Text

Priority order:
1. DOI → journal website (PLoS One, MDPI, Elsevier open access)
2. PMID → PubMed abstract + eutils
3. PMC → full text if available

Use WebFetch with prompt:
```
Extract the full research content including:
1) Study design and population (sample size, methods)
2) Results (key findings, numbers, statistics, odds ratios)
3) Discussion/Conclusions
Focus on feline-specific findings for the cancer module.
```

### Step 3: Create Deep Extraction Worksheet

Output: `system/indexes/{source-id}-deep-extraction-round1.md`

Required sections:

```markdown
---
id: {source-id}-deep-extraction-round1
type: system
topic: cancer
question_type: deep-extraction
source_ids: [{source-id}]
language: en
last_compiled_at: {today}
verification_status: deep_extracted
decision_grade: no
owner: claude
status: active
---

# Deep Extraction Worksheet

Source: `{source-id}`
Title: `{title}`
Method note: {access method and DOI}

## Phase 0: Sequential Micro-Analysis

#### Unit 1: {main claim}
- core_claim:
- implicit_premise:
- relation_to_previous:
- hard_details:
- tension_or_surprise:

[3-5 units total]

## Phase 1: Theme Reconstruction

## Theme: {theme 1}
{description}
### Hard Information
- {bullet points}

## Phase 2: Claim-Evidence Structure

### {Category} Key Points

**Claim 1**
- support:
- details:
- implicit_premise:

## Phase 2.5: Write-Back Implications

### For `topics/cancer/{relevant-page}.md`
- {specific updates}

### For `raw/papers/{source-id}.md`
- Update status to `deep_extracted`
- Update extraction_depth to `full`

## Phase 3: Promotion Check

- source_card_updates:
- topic_write_back_targets:
- not_safe_to_promote_yet:
- conflicts_with_existing_vault:
- new_entities_or_pages_justified:
- follow_up_needed:
```

### Step 4: Update Source Card

Edit `raw/papers/{source-id}.md`:

1. Update frontmatter:
```yaml
status: deep_extracted
extraction_depth: full
verification_status: deep_extracted
```

2. Add Deep Extraction section after title:
```markdown
## Deep Extraction, {today}

[Deep extraction worksheet](../../system/indexes/{source-id}-deep-extraction-round1.md)

Safe promoted role:
- {bullet points from Phase 3}

Do not use this source as:
- {bullet points from not_safe_to_promote_yet}
```

3. Update DOI if missing

## Promotion Rules

### Safe to promote:
- Quantified findings with statistics (OR, CI, p-values)
- Sample sizes and methodology
- Study limitations acknowledged by authors
- Comparisons with existing vault sources

### Not safe to promote:
- Clinical diagnostic/treatment recommendations (unless guideline source)
- Causal claims without mechanism evidence
- Generalization beyond study population
- Numeric claims without denominator context

### Requires caveats:
- Single-study findings (need replication)
- Small sample sizes (n<50)
- Abstract-only extraction (full text unavailable)
- Regional/population-specific findings

## Output Summary

After completion, report:

| Item | Path |
|------|------|
| Worksheet | `system/indexes/{source-id}-deep-extraction-round1.md` |
| Source card | `raw/papers/{source-id}.md` (updated) |
| Status | `deep_extracted` |

## Batch Mode

For multiple extractions:
```
/cancer-deep-extract src-cancer-045 src-cancer-052 src-cancer-063
```

Process sequentially, report summary table at end.

## List Candidates

```bash
# Find abstract-level cancer sources eligible for deep extraction
grep -l "extraction_depth: abstract" raw/papers/src-cancer-*.md | \
  while read f; do
    id=$(basename "$f" .md)
    title=$(grep "^title:" "$f" | head -1 | sed 's/^title: //' | tr -d '"' | cut -c1-60)
    year=$(grep "^year:" "$f" | head -1 | sed 's/^year: //')
    echo "$id|$year|$title"
  done | sort -t'|' -k2 -rn | head -20
```

## Related Skills

- `/cancer-topic-update` — write extracted findings to topic pages
- `/source-check` — verify source metadata before extraction
