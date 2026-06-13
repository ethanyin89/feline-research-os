# /structured-abstract-extract

Structured abstract extraction skill for feline disease source cards. Upgrades title-only cards to abstract-weighted level with Crossref metadata.

## Trigger

- `/structured-abstract-extract <source-id>` — e.g., `/structured-abstract-extract src-ckd-027`
- `/structured-abstract-extract batch --disease <disease>` — process all title_only sources for a disease
- `/structured-abstract-extract list --disease <disease>` — show candidates

## Input

- `source-id`: A source card ID like `src-ckd-027` or `src-cancer-045`
- `disease`: Disease code (ckd, cancer, diabetes, fip, fcv, hcm, ibd, obesity)

## Prerequisites

The script uses Crossref API to fetch abstracts. Sources without DOI or without Crossref abstract will be skipped.

## Workflow

### Step 1: Validate Source

```bash
# Single source check
ls raw/papers/$SOURCE_ID.md
grep "verification_status:" raw/papers/$SOURCE_ID.md
```

Abort if:
- Source doesn't exist
- Already at `abstract_weighted`, `source_checked`, or `deep_extracted`

### Step 2: Run Extraction Script

For single source:
```bash
python3 scripts/structured_abstract_extraction.py \
  --source-ids "$SOURCE_ID" \
  --source-label "manual extraction $(date +%Y-%m-%d)" \
  --write
```

For batch (disease-specific):
```bash
python3 scripts/structured_abstract_extraction.py \
  --source-glob "raw/papers/src-${DISEASE}-*.md" \
  --status title_only \
  --source-label "$DISEASE structured abstract batch $(date +%Y-%m-%d)" \
  --index-id "feline-${DISEASE}-structured-abstract-$(date +%Y%m%d)" \
  --index-out "system/indexes/feline-${DISEASE}-structured-abstract-$(date +%Y%m%d).md" \
  --write
```

### Step 3: Update Source Card Status

For each successfully processed source, update the source card frontmatter:

```yaml
verification_status: abstract_weighted
```

### Step 4: Report Summary

Output table of processed sources:

| Source | Abstract Available | Worksheet | Signals |
|--------|-------------------|-----------|---------|
| src-ckd-027 | yes | src-ckd-027-structured-abstract-round1.md | {signals} |
| src-ckd-028 | no (skipped) | — | — |

## Output Files

| Item | Path |
|------|------|
| Worksheet | `system/indexes/{source-id}-structured-abstract-round1.md` |
| Index | `system/indexes/feline-{disease}-structured-abstract-{date}.md` |
| Source card | `raw/papers/{source-id}.md` (status updated) |

## Promotion Rules

### Safe uses of abstract-weighted sources:
- Extraction priority and branch placement
- Mechanical signal detection (endpoints, population, study type)
- Deduplication checking

### Not safe:
- Numeric effect sizes, protocol selection, prevalence values
- Risk ranking or owner-facing advice
- Topic page write-back

### Requires source_checked or deep_extracted:
- Any clinical decision-relevant claim
- Quantified findings for business artifacts
- Claim cards or opportunity briefs

## List Candidates

```bash
# Find title_only sources for a disease
grep -l "verification_status: title_only" raw/papers/src-${DISEASE}-*.md | \
  while read f; do
    id=$(basename "$f" .md)
    title=$(grep "^title:" "$f" | head -1 | sed 's/^title: //' | tr -d '"' | cut -c1-60)
    doi=$(grep "^doi:" "$f" | head -1 | sed 's/^doi: //' | tr -d '"')
    echo "$id|$doi|$title"
  done | column -t -s'|'
```

## Sample Sessions

### CKD extension batch (8 samples completed 2026-06-05):
- src-ckd-025, src-ckd-026, src-ckd-033, src-ckd-034, src-ckd-035, src-ckd-043, src-ckd-045, src-ckd-046
- Index: `system/indexes/feline-ckd-extension-structured-abstract-20260605.md`
- 2 promoted to source_checked: src-ckd-026 (FGF-23), src-ckd-034 (risk factors)

## Related Skills

- `/cancer-deep-extract` — full-text deep extraction for cancer sources
- `/source-check` — verify source metadata before extraction
- `/claim-evidence` — create claim cards from extracted sources

## Batch Processing Notes

When processing large batches:
1. Run in batches of 10-20 sources (Crossref rate limits)
2. Review skipped sources (no DOI or no abstract)
3. Generate index file for tracking
4. Update source-depth-map after batch completes
