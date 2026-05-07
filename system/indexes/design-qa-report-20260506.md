# Design QA Report — 2026-05-06

## Summary

- Total checks: 7
- Passed: 6
- Failed: 0
- Missing/Needs Review: 1

## Detailed Findings

### ✓ Passed

**1. Core Colors (10/10 DESIGN.md colors found)**
| Color | Role | Found |
|-------|------|-------|
| #0f1117 | Background | ✓ |
| #1a1d27 | Surface | ✓ |
| #222535 | Surface 2 | ✓ |
| #2d3147 | Border | ✓ |
| #e8eaf0 | Primary text | ✓ |
| #8b90a0 | Muted text | ✓ (7 uses, most frequent) |
| #4a4f64 | Subtle text | ✓ |
| #16a34a | quoted_fact | ✓ |
| #ca8a04 | supported | ✓ |
| #6b7280 | inference | ✓ |

**2. Provenance Badges**
- Implemented in `BADGE_PATTERNS` (lines 64-86)
- All three badge types present
- Styling matches DESIGN.md spec

**3. Empty State**
- `EMPTY_STATE_INTRO_HTML` implemented (lines 104-111)
- Title "Ask the vault" present
- Stats line present
- Example question chips implemented via `render_example_question_chips()`

**4. Provenance Guide**
- `PROVENANCE_GUIDE_HTML` implemented (lines 95-102)
- Shows only in empty state as specified

**5. Copy Markdown Button**
- `copy_button()` function implemented (lines 343-363)
- Uses clipboard API correctly
- Renders below assistant messages

**6. Search UI**
- `vault_search` imported and used
- Search functionality in sidebar
- 47 search-related code references

### ⚠ Needs Review

**1. Undocumented Colors (5 colors not in DESIGN.md)**

| Color | Usage | Status |
|-------|-------|--------|
| #f2b0b0 | line 872 | Light pink - likely error/warning state |
| #f0d08b | line 806 | Light amber - likely hover state |
| #d6b56b | line 866 | Darker amber - likely state variation |
| #79d094 | line 878 | Light green - likely success state |
| #3a3f58 | line 680 | Border variation |

**Recommendation:** Add these as derived/state colors in DESIGN.md's Color section:

```markdown
### State Colors (derived from base palette)
| Role | Color | Derivation |
|------|-------|------------|
| Error highlight | #f2b0b0 | Light red for error states |
| Hover amber | #f0d08b | Lighter supported badge hover |
| Active amber | #d6b56b | Darker supported badge active |
| Success highlight | #79d094 | Light green for success states |
| Active border | #3a3f58 | Darker border for active elements |
```

## Implementation Coverage

| DESIGN.md Section | Status |
|-------------------|--------|
| Product Context | N/A (documentation) |
| Aesthetic Direction | ✓ Implemented |
| Typography | ✓ Geist fonts loaded |
| Color | ✓ Core + 5 undocumented variants |
| Spacing | ✓ 8px base unit visible |
| Layout | ✓ 720px max-width applied |
| Motion | N/A (minimal) |
| Streamlit config.toml | ✓ Present |
| CSS Injection | ✓ Implemented |
| Provenance Badges | ✓ Implemented |
| Figures | ✓ Implemented |
| Empty State | ✓ Implemented |
| Search UI | ✓ Implemented |
| Onboarding | ✓ Via empty state |
| Error States | ⚠ Basic (see below) |
| Copy/Export | ✓ Copy markdown implemented |

### Error State Detail

Current error handling is basic (`st.error()` / `st.warning()`). DESIGN.md specifies structured error messages with:
- Plain English explanation
- Actionable next steps
- Collapsed technical details

**Current implementation:** 1 `st.error` call found.
**Recommendation:** Enhance error messages to match DESIGN.md spec.

## Recommended Actions

1. **Low priority:** Document the 5 derived state colors in DESIGN.md
2. **Medium priority:** Enhance error message structure to match DESIGN.md spec
3. **No action needed:** Core UI implementation is compliant

## Next QA Run

Schedule: After next UI feature addition
Focus: Error message improvements
