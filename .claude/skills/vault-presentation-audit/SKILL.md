# vault-presentation-audit

Audit the vault UI for internal structure exposure and presentation quality issues.

## Purpose

This skill ensures the "Ask the Vault" UI never exposes internal file structure
(like `src-ckd-001` IDs) to end users, and that outputs meet presentation standards.

## When to Use

- After adding new source cards
- After modifying `app.py` or `research_mode.py`
- Before shipping UI changes
- When user reports seeing internal IDs or truncated outputs

## Audit Checklist

### 1. Internal ID Exposure (Critical)

Search for patterns that might expose internal source IDs:

```bash
# Check for src-xxx patterns in user-facing strings
grep -rn "src-[a-z]*-[0-9]" scripts/app.py scripts/research_mode.py | grep -v "def\|#\|is_internal\|humanize\|_source_id\|get_source"
```

Verify:
- [ ] All `src-xxx` IDs are converted to paper titles before display
- [ ] `_humanize_source_ids()` is called on all provenance badge content
- [ ] Research mode output uses paper titles, not file IDs
- [ ] Sidebar saved answers show paper titles

### 2. Output Completeness

Test research mode with sample queries:

```python
# In Python REPL or test script
from research_mode import handle_research_query
result = handle_research_query("find recent diabetes papers with clinical relevance")
print(f"Output length: {len(result)} chars")
print(f"Paper count: {result.count('##')}")  # Count section headers
```

Expected:
- [ ] Output length > 5000 chars for typical queries
- [ ] At least 5 papers returned for broad queries
- [ ] No truncation mid-sentence

### 3. Badge Rendering

Verify provenance badges render correctly:

```bash
# Check badge patterns have consistent styling
grep -A2 "quoted_fact\|source_supported_conclusion\|llm_inference" scripts/app.py | grep "span style"
```

Verify:
- [ ] All three badge types use JetBrains Mono font
- [ ] Colors match DESIGN.md (green: #10b981, amber: #d97706, gray: #6b7280)
- [ ] Badges have consistent padding (3px 10px) and border-radius (5px)

### 4. Typography Consistency

Check font loading and application:

```bash
# Verify Google Fonts import
grep -n "@import url" scripts/app.py
```

Verify:
- [ ] Inter, JetBrains Mono, and Source Serif 4 are loaded
- [ ] Serif font (Source Serif 4) is used for body prose
- [ ] Sans-serif (Inter) is used for UI elements
- [ ] Monospace (JetBrains Mono) is used for metadata and badges

### 5. Color Consistency

Check CSS variables match DESIGN.md:

```bash
grep -A10 ":root {" scripts/app.py
```

Verify:
- [ ] `--bg: #0a0c10`
- [ ] `--surface: #12151c`
- [ ] `--text: #eceff4`
- [ ] Accent colors match provenance badge colors

## Manual QA Steps

1. **Run the app locally:**
   ```bash
   cd /Users/jiawei/Desktop/insclaude/feline-research-os
   .venv/bin/python -m streamlit run scripts/app.py
   ```

2. **Test Ask the Vault:**
   - Query: "what is CKD"
   - Verify no `src-ckd-xxx` IDs visible
   - Check provenance badges show paper titles

3. **Test Research Mode:**
   - Query: "搜索HCM最新文献"
   - Verify output has 5+ papers
   - Check paper entries have titles, not IDs

4. **Test Sidebar:**
   - Save an answer
   - Check saved answer list shows paper titles, not IDs

## Auto-Fix Actions

If issues found:

### Fix 1: Internal ID Exposure

Ensure all provenance badge rendering uses `_humanize_source_ids()`:

```python
# In app.py render_provenance()
humanized = _humanize_source_ids(match.group(1))
return f'<span...>{badge_label}: {html.escape(humanized)}</span>'
```

### Fix 2: Missing Font

Add to Google Fonts import:

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400&display=swap');
```

### Fix 3: Color Mismatch

Update DESIGN.md and app.py to match:
- Background: `#0a0c10`
- Surface: `#12151c`
- Text: `#eceff4`
- Green accent: `#10b981`
- Amber accent: `#d97706`

## Exit Criteria

All checkboxes marked. If any fail:
- Report which checks failed
- Apply auto-fix if available
- Re-run audit
