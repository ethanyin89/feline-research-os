## Design System
Always read DESIGN.md before making any visual or UI decisions.
All font choices, colors, spacing, and aesthetic direction are defined there.
Do not deviate without explicit user approval.
In QA mode, flag any code that doesn't match DESIGN.md.

## Workspace And API Cost Rules

Primary active projects live under `/Users/jiawei/Desktop/insclaude`.

Default work mode: use Claude or ChatGPT subscription products for ordinary coding,
content processing, documentation, and review. Do not connect real paid APIs just to
write code, inspect files, or run non-live checks.

Use a real API only when a real page or live acceptance path genuinely requires it.
For this repo, that means Streamlit `Ask the vault` or acceptance runs that cannot be
verified with local/template checks.

OpenRouter live runs require both safeguards before running:

1. OpenRouter dashboard daily/project budget is set to `$1/day`.
2. The project environment sets `OPENROUTER_DAILY_BUDGET_USD=1.00` or lower.

If either safeguard is missing, report the run as blocked. Do not fake API output,
do not mark acceptance as live, and do not silently switch to another paid backend.
Anthropic API use requires explicit user approval because this repo does not enforce
a project-side daily Anthropic spend cap.

## Model Collaboration Contract

This project uses a strict multi-model division of labor. Do not collapse these
roles unless the user explicitly asks to override the workflow for a specific task.

1. **ChatGPT**
   - Converts rough ideas into task briefs, acceptance criteria, prompts, and
     judgment frameworks.
   - Owns framing, scope, and what "done" means.
   - Does not silently become the implementation agent after writing a plan.

2. **Antigravity**
   - Runs read-only scans, audits, inconsistency checks, and risk identification.
   - Produces critique and findings.
   - Does not perform the main implementation or rewrite the codebase.

3. **Claude**
   - Executes concrete changes from an explicit task brief.
   - Runs tests and reports the resulting diff.
   - Owns primary implementation work when the task has already been specified.

4. **Codex or ChatGPT**
   - Performs final code review, logic review, and copy review.
   - Prioritizes bugs, regressions, hidden assumptions, user-facing leakage, and
     acceptance gaps.
   - Should review against the task brief and acceptance criteria instead of
     inventing new scope.

Default handoff sequence:

`Idea -> ChatGPT task brief -> Antigravity read-only critique -> Claude implementation -> Codex/ChatGPT final review`

If a model receives work outside its assigned role, it should either convert the
request into the correct artifact for its role or explicitly ask whether the user
wants to override the collaboration contract for that turn.

## Skill routing

When the user's request matches an available skill, ALWAYS invoke it using the Skill
tool as your FIRST action. Do NOT answer directly, do NOT use other tools first.
The skill has specialized workflows that produce better results than ad-hoc answers.

Key routing rules:
- Product ideas, "is this worth building", brainstorming → invoke office-hours
- Bugs, errors, "why is this broken", 500 errors → invoke investigate
- Ship, deploy, push, create PR → invoke ship
- QA, test the site, find bugs → invoke qa
- Code review, check my diff → invoke review
- Update docs after shipping → invoke document-release
- Weekly retro → invoke retro
- Design system, brand → invoke design-consultation
- Visual audit, design polish → invoke design-review
- Architecture review → invoke plan-eng-review
- Save progress, checkpoint, resume → invoke checkpoint
- Code quality, health check → invoke health
