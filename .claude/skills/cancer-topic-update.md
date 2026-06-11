# /cancer-topic-update

Topic page update skill for feline cancer module. Pushes deep extraction findings to topic pages.

## Trigger

- `/cancer-topic-update <source-id>` — push findings from deep extraction to topic pages
- `/cancer-topic-update check` — list sources with deep extraction but pending topic write-back

## Input

- `source-id`: A deep-extracted source card like `src-cancer-093`
- Must have corresponding worksheet in `system/indexes/{source-id}-deep-extraction-round1.md`

## Workflow

### Step 1: Read Deep Extraction Worksheet

```bash
cat system/indexes/${SOURCE_ID}-deep-extraction-round1.md
```

Focus on **Phase 2.5: Write-Back Implications** section which lists:
- Target topic pages
- Specific claims to add
- Boundary rules

### Step 2: Identify Target Topic Pages

Common targets for cancer module:
- `topics/cancer/mammary-carcinoma.md`
- `topics/cancer/lymphoma.md`
- `topics/cancer/oral-squamous-cell-carcinoma.md`
- `topics/cancer/registry-and-prevalence.md`
- `topics/cancer/synthesis-index.md`

### Step 3: Update Key-Claim Traceability Table

For each target page, add claim to the table:

```markdown
| {ID} | {Specific claim with numbers/stats} | {Level} | {source-id} | {boundary caveat} |
```

Claim ID format:
- Mammary carcinoma: MC{N}
- Lymphoma: LY{N}
- OSCC: OSCC{N}
- Registry: RP{N}

Level codes:
- A = quoted fact
- B = source-supported conclusion
- C = inference

### Step 4: Add or Update Section

If new findings warrant a dedicated section:

```markdown
### {Topic Name} ({Extraction Status})

`{source-id}` ({year} {journal}) {one-line description}. See `system/indexes/{source-id}-deep-extraction-round1.md`.

**Key findings:**

| Finding | Detail |
|---------|--------|
| {metric} | {value} |

**Boundary:** {limitations from Phase 3 not_safe_to_promote_yet}
```

Extraction status options:
- `(Deep-Extracted)` — full worksheet available
- `(Abstract-Level)` — abstract only
- `(Title-Only)` — minimal extraction

### Step 5: Update Frontmatter

Add source to `source_ids` list if not present:

```yaml
source_ids: [...existing..., {source-id}]
```

### Step 6: Add Boundary Rules

If new boundary applies, add to page's Boundaries section:

```markdown
- Do not {specific overclaim to avoid}.
```

## Claim Guidelines

### What to include:
- Quantified findings (OR, CI, p-values, percentages)
- Sample sizes and study design
- Novel mechanisms or biomarkers
- Comparisons with existing claims

### What to exclude:
- Treatment recommendations (unless guideline source)
- Causal claims without mechanism evidence
- Generalizations beyond study population

### Boundary language patterns:
- "n={X} study, requires replication"
- "{population} population, may not generalize"
- "in vitro/abstract-level evidence only"
- "first study, validation needed"

## Output Summary

After completion, report:

| Item | Update |
|------|--------|
| Topic page | `{path}` |
| Claims added | {IDs} |
| Section | {new/updated} |
| Boundary | {added rule} |

## Check Mode

Find deep-extracted sources without topic write-back:

```bash
# List deep-extracted cancer sources
grep -l "status: deep_extracted" raw/papers/src-cancer-*.md | while read f; do
  id=$(basename "$f" .md)
  # Check if worksheet exists
  if [ -f "system/indexes/${id}-deep-extraction-round1.md" ]; then
    # Check if Phase 2.5 targets are in topic pages
    targets=$(grep -A10 "Phase 2.5" "system/indexes/${id}-deep-extraction-round1.md" | grep "topics/cancer" | head -3)
    echo "$id: $targets"
  fi
done
```

## Related Skills

- `/cancer-deep-extract` — create deep extraction worksheets
- `/source-check` — verify source metadata
