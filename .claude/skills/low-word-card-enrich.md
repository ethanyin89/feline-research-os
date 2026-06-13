# /low-word-card-enrich

Enrichment skill for source cards that are `extraction_depth: full` but below 700 words. Adds structured details from deep extraction worksheets to meet health check threshold.

## Trigger

- `/low-word-card-enrich <source-id>` — e.g., `/low-word-card-enrich src-ckd-027`
- `/low-word-card-enrich list` — show candidates (full-extraction cards below 700 words)
- `/low-word-card-enrich all` — process all candidates

## Input

- `source-id`: A source card ID like `src-ckd-027`
- Must have `extraction_depth: full` and word count < 700

## Why This Exists

The health check flags cards with `extraction_depth: full` that are below 700 words. These cards have complete deep extraction worksheets but the source card itself is too concise. This skill enriches the card with structured information from the worksheet.

## Workflow

### Step 1: Find Candidates

```bash
for f in raw/papers/*.md; do
  depth=$(grep -m1 "^extraction_depth:" "$f" 2>/dev/null | sed 's/extraction_depth: *//')
  if [ "$depth" = "full" ]; then
    words=$(wc -w < "$f")
    if [ "$words" -lt 700 ]; then
      id=$(basename "$f" .md)
      echo "$words $id"
    fi
  fi
done | sort -n
```

### Step 2: Read Deep Extraction Worksheet

For source `{source-id}`, read:
```
system/indexes/{source-id}-deep-extraction-round1.md
```

Extract:
- Phase 0 micro-analysis units (study details, hard numbers)
- Phase 1 themes (key findings)
- Phase 2 claim-evidence structure
- Phase 3 promotion boundaries

### Step 3: Enrich Source Card

Add or expand these sections in `raw/papers/{source-id}.md`:

#### A. Study Design Details

Create structured tables from worksheet:

```markdown
## Study Design Details

### Population
| Metric | Value |
|--------|-------|
| Sample size | N |
| Groups | description |
| Stages/grades | breakdown |

### Methods
- Key methodology points from worksheet

### Key Limitations
- Design boundary items from Phase 0
```

#### B. Detailed Findings

Add specific pathway/mechanism findings:

```markdown
## Detailed Pathway Findings

### {Topic 1}
- Bullet points from worksheet hard_details

### {Topic 2}
- More specifics
```

#### C. Clean Up Template Sections

Replace boilerplate with actual content:

**Before:**
```markdown
## Image Asset TODO

- figures to capture: unknown until source text is read
- why these matter: tables or figures should remain behind the candidate gate

## Open Follow-Up Questions

- What source family is confirmed by the abstract or article body?
- Which claims, if any, are reusable for the ckd module?
- Does this source deserve deep extraction, or should it remain queue context?
- Are there tables or figures that change the module structure?
```

**After:**
```markdown
## Image Assets

No figures captured. [Specific reason from worksheet about why no figures warranted promotion].
```

Remove "Open Follow-Up Questions" section entirely (already answered by deep extraction).

#### D. Fill In Linked Entities

Replace empty values:

**Before:**
```markdown
## Linked Entities

- diseases: CKD
- models:
- endpoints:
- mechanisms:
- regulations:
```

**After:**
```markdown
## Linked Entities

- diseases: CKD (stages X-Y)
- models: {model type from worksheet}
- endpoints: {specific endpoints measured}
- mechanisms: {pathways involved}
- regulations: none applicable
```

### Step 4: Verify Word Count

```bash
wc -w raw/papers/{source-id}.md
```

Target: ≥700 words

### Step 5: Run Health Check

```bash
python3 scripts/health.py 2>&1 | grep "Low-word"
```

## Samples Processed (2026-06-08)

| Source | Before | After | Key Additions |
|--------|--------|-------|---------------|
| src-ckd-050 | 383 | 721 | TGF-beta pathway context, evidence gap analysis, study design table |
| src-ckd-030 | 544 | 726 | Population/attrition table, uremic toxin results, limitations |
| src-cancer-093 | 648 | 789 | Molecular subtypes table, phosphoprotein details, study composition |
| src-ckd-029 | 649 | 775 | Intervention composition, monitoring parameters table, design limits |
| src-ckd-027 | 666 | 751 | Detailed pathway findings, validation analysis, mechanism context |

## Content Guidelines

### What to Add

- Structured tables (population, methods, results)
- Specific numbers from worksheet (sample sizes, p-values, percentages)
- Mechanism details (pathways, genes, markers)
- Clear limitation statements
- Filled-in Linked Entities

### What NOT to Add

- Padding or filler text
- Claims beyond worksheet scope
- Clinical recommendations
- Content not supported by the deep extraction

### Word Count Targets

- Minimum: 700 words (health check threshold)
- Typical: 700-900 words
- If under 700 after enrichment: source may legitimately be concise, consider if extraction_depth should remain "full"

## Output Summary

After completion, report:

| Item | Value |
|------|-------|
| Source | `{source-id}` |
| Words before | N |
| Words after | M |
| Key additions | {brief description} |

## Batch Mode

```
/low-word-card-enrich all
```

Process all candidates, report summary table at end.

## Related Skills

- `/cancer-deep-extract` — creates deep extraction worksheet (prerequisite)
- `/structured-abstract-extract` — abstract-level extraction
