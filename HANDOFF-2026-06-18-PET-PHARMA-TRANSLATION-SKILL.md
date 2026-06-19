# HANDOFF: Pet Pharma Scientific Translation Skill

Date: 2026-06-18
Branch: idea-chatacademia-research-workbench
Status: COMPLETE

## Summary

The user provided an existing skill folder:

```text
/Users/jiawei/Downloads/pet-pharma-scientific-translation
```

It was reviewed and installed into the current project as a project-level Agent Skill:

```text
.claude/skills/pet-pharma-scientific-translation/
```

## Why This Location

The project already uses `.claude/skills` for project-level agent workflows, including both single-file and directory-style skills. Because the provided material already had a `SKILL.md`, `references/`, `scripts/`, and `templates/`, `.claude/skills/pet-pharma-scientific-translation` is the most consistent location.

`system/skills` was not used because this is intended to be a triggerable translation workflow, not only internal project documentation.

## Files Installed

- `SKILL.md`
- `references/evidence-language-map.md`
- `references/glossary_seed.csv`
- `references/preferred-examples.md`
- `references/prohibited-patterns.md`
- `references/scientific-style-guide.md`
- `references/source-type-rules.md`
- `references/terminology-governance.md`
- `scripts/check_numbers.py`
- `scripts/check_terms.py`
- `templates/qa-checklist.md`
- `templates/terminology-sheet.csv`
- `templates/translation-output-template.md`

The source `README.md` was intentionally not copied. The Codex `skill-creator` guidance says a final skill should avoid auxiliary README / installation / changelog files unless they are directly required for execution.

## Skill Scope

Use this skill for professional English-Chinese translation and editing of veterinary medicine, companion-animal health, pet-pharma R&D, pharmacology, toxicology, diagnostics, biomarkers, clinical research, abstracts, methods, results, discussions, study reports, and literature reviews.

Do not use it for popular-science rewriting, marketing copy, regulatory news, or general consumer-facing content unless the user explicitly asks for a scientific-professional version.

## Key Rules Preserved

- Translate meaning first, then reconstruct professional Chinese.
- Preserve study design, sample, endpoints, statistics, time points, and limitations.
- Do not amplify causality, efficacy, safety, clinical applicability, or certainty.
- Maintain consistent terminology through a per-document terminology sheet.
- Preserve numbers, units, P values, confidence intervals, comparison directions, and subgroup boundaries.
- Separate translation from translator notes unless annotations are requested.

## Verification

Commands run:

```bash
python3 -m py_compile .claude/skills/pet-pharma-scientific-translation/scripts/check_terms.py .claude/skills/pet-pharma-scientific-translation/scripts/check_numbers.py
```

Result: pass.

Additional checks:

- Installed file list reviewed.
- `SKILL.md` frontmatter contains valid `name` and `description`.
- `README.md` is absent from the installed skill directory.

