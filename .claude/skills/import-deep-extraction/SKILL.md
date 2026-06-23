# import-deep-extraction

Import a Phase 0-3 deep extraction document into the vault with proper preservation and UI-ready highlights.

## Purpose

Transform external deep extraction documents (produced via ChatGPT/Claude with the "Phase 0 Enhanced" template) into:
1. **Preserved full extraction** in `raw/deep-extractions/` with bibliographic header
2. **Updated source card** in `raw/papers/` with researcher-attracting highlights

## Input

A deep extraction document containing:
- Paper bibliographic info (title, DOI, year, authors)
- Phase 0: Paragraph-level microanalysis (optional to preserve)
- Phase 1: Theme reconstruction
- Phase 2: Argument-evidence extraction (论点-论据)
- Phase 3: Self-check findings

## Workflow

### Step 1: Parse Bibliographic Info

Extract from the document:
```
title: "Full paper title"
doi: "10.xxxx/xxxxx"
url: "https://doi.org/10.xxxx/xxxxx"
year: YYYY
authors: ["Author1", "Author2", ...]
```

### Step 2: Determine Source ID

Check existing source cards to find or assign ID:
```bash
# Find existing card by DOI
grep -l "doi.*10.xxxx/xxxxx" raw/papers/src-*.md

# Or get next available ID for disease category
ls raw/papers/src-diabetes-*.md | sort -V | tail -1
```

### Step 3: Preserve Deep Extraction

Create `raw/deep-extractions/ext-{source-id}.md`:

```markdown
---
source_id: src-diabetes-XXX
title: "Paper Title"
doi: "10.xxxx/xxxxx"
url: "https://doi.org/..."
year: YYYY
authors: ["Author1", ...]
extracted_date: YYYY-MM-DD
extraction_source: phase-0-enhanced
---

# [Title]

## Bibliographic Info

- **Title**: ...
- **Authors**: ...
- **Journal**: ...
- **Year**: ...
- **DOI**: ...

---

# Phase 2: Argument-Evidence Extraction

[Preserve full Phase 2 content here]

---

# Phase 3: Self-Check Findings

[Preserve full Phase 3 content here]
```

### Step 4: Generate Source Card Highlights

Transform Phase 2+3 into source card format:

**Extract for `evidence_policy`:**
- `quoted_fact`: Direct data/findings from Phase 2 "论据" sections
- `source_supported_conclusion`: Key "论点" claims with evidence support
- `llm_inference`: Cross-theme insights from Phase 3

**Extract for V2 fields:**
- `study_design`: From Phase 0/1 method description
- `core_argument`: Central thesis from Phase 2
- `implicit_premise`: Unstated assumptions from Phase 0 analysis
- `title_gap`: Gap between title promise and actual contribution
- `evidence_boundary`: What the paper doesn't prove (from Phase 3)
- `unexpected_finding`: Cross-theme tensions or surprises

**Generate researcher highlights:**
- `Why it matters`: Key insight for researchers
- `Takeaway`: Actionable reading guidance
- `Evidence boundary`: What still needs verification

### Step 5: Update Source Card

Edit or create `raw/papers/src-{disease}-{nnn}.md`:
- Update `extraction_depth: full`
- Update `status: deep_extracted`
- Add `evidence_policy` entries
- Add V2 enhanced fields
- Link to deep extraction: `local_assets: ["../../raw/deep-extractions/ext-{id}.md"]`

### Step 6: Verify Integration

```bash
# Check source card is valid
python scripts/health.py --check-card raw/papers/src-diabetes-XXX.md

# Check deep extraction is linked
grep "deep-extractions" raw/papers/src-diabetes-XXX.md
```

## Quality Standards

### Deep Extraction Preservation
- [ ] Bibliographic info complete (title, DOI, year, authors)
- [ ] Phase 2 content preserved verbatim with structure
- [ ] Phase 3 self-check findings preserved
- [ ] Extracted date recorded

### Source Card Quality
- [ ] V2 fields have specific, non-generic content
- [ ] `core_argument` is a falsifiable claim with conditions
- [ ] `title_gap` shows intellectual tension
- [ ] `evidence_boundary` cites specific method limitations
- [ ] `quoted_fact` entries are direct quotes, not paraphrases
- [ ] Deep extraction linked in `local_assets`

## Example Run

```bash
# Input: deep extraction document
INPUT="/Users/jiawei/Desktop/Paper Title.深度提炼.md"

# Parse bibliographic info
TITLE="Feline Diabetes Is Associated with..."
DOI="10.3390/ijms252313195"
YEAR="2024"

# Determine source ID
EXISTING=$(grep -l "10.3390/ijms252313195" raw/papers/src-diabetes-*.md)
if [ -z "$EXISTING" ]; then
  NEXT_ID=$(ls raw/papers/src-diabetes-*.md | sort -V | tail -1 | grep -o '[0-9]\{3\}' | tail -1)
  NEW_ID=$(printf "%03d" $((10#$NEXT_ID + 1)))
  SOURCE_ID="src-diabetes-$NEW_ID"
else
  SOURCE_ID=$(basename "$EXISTING" .md)
fi

# Create deep extraction file
# Create/update source card
# Verify
```

## Trigger

Use when:
- User provides a deep extraction document path
- User says "import deep extraction"
- User mentions "Phase 2" or "Phase 3" preservation

## Output

1. Deep extraction preserved at `raw/deep-extractions/ext-{id}.md`
2. Source card updated at `raw/papers/{id}.md`
3. Report: what was extracted, what's linked, quality check results
