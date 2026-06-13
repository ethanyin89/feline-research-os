# Feline Research OS — Takeover Audit Report (260613)

**Audit Date:** 2026-06-13  
**Current Branch:** `idea-chatacademia-research-workbench`  
**Current HEAD Commit:** `2cc2a84 feat: add Expert Review Loop and External Search integration` (June 13, 2026)  

---

## 1. Scope Inspected & Evidence Base

### Scope Inspected
* Core python architecture packages located in `core/`.
* Operational scripts, CLI utilities, and UI layout in `scripts/`.
* Vault documentation, handoffs, and planning files in the root workspace and `system/`.
* Virtual environment and dependency configurations.

### Commands Run
* `git status` (and concise `--short --branch` variants) to evaluate workspace index status.
* `git log` and `git diff` stats to check codebase modification logs and file change sizes.
* Diagnostic import compilation tests on system Python and local `.venv` Python.
* Link integrity checks (`scripts/check_markdown_links.py`).
* Core unit test suites (`scripts/test_query.py` and `core/test_harness_loop.py`).
* Configuration budget guard checks (`scripts/check_openrouter_budget_guard.py`).

### Files Read
* **Read in full:**
  * [CLAUDE.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/CLAUDE.md)
  * [ARCHITECTURE.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/ARCHITECTURE.md)
  * [DESIGN.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/DESIGN.md)
  * [HANDOFF.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/HANDOFF.md)
  * [HANDOFF-2026-06-11-WORKTREE-STATE.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/HANDOFF-2026-06-11-WORKTREE-STATE.md)
  * [HANDOFF-2026-06-13-SESSION-CONTINUATION.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/HANDOFF-2026-06-13-SESSION-CONTINUATION.md)
  * [TODOS.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/TODOS.md)
  * [requirements.txt](file:///Users/jiawei/Desktop/insclaude/feline-research-os/requirements.txt)
  * [system/health-checks/health-report-20260613.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/system/health-checks/health-report-20260613.md)
  * [README.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/README.md)
* **Sampled (Partially read):**
  * [core/schemas.py](file:///Users/jiawei/Desktop/insclaude/feline-research-os/core/schemas.py) (sections on ResearchRecord and Schema version definitions)
  * [scripts/app.py](file:///Users/jiawei/Desktop/insclaude/feline-research-os/scripts/app.py) (import headers)
  * [scripts/query.py](file:///Users/jiawei/Desktop/insclaude/feline-research-os/scripts/query.py) (budget validation helpers)

---

## 2. Verified Project Progress

* `[CONFIRMED FACT]` The vault contains 603 strict disease paper cards located in [raw/papers/](file:///Users/jiawei/Desktop/insclaude/feline-research-os/raw/papers) and 14 regulation cards.
* `[CONFIRMED FACT]` Core Q&A parsing, token estimations, and regex-based routing pass $113$ pure unit tests in [scripts/test_query.py](file:///Users/jiawei/Desktop/insclaude/feline-research-os/scripts/test_query.py).
* `[CONFIRMED FACT]` A Presentation V2 adapter layer is implemented in [core/result_presentation.py](file:///Users/jiawei/Desktop/insclaude/feline-research-os/core/result_presentation.py) mapping source attributes (PMID, DOI, Author lists) to user-facing results.
* `[CONFIRMED FACT]` The OpenRouter budget check logic successfully blocks query runs when the environment cap variable `OPENROUTER_DAILY_BUDGET_USD` is missing or greater than $1.00.

---

## 3. Documentation-vs-Implementation Gaps

* `[CONFIRMED FACT]` **Bilingual Context Bypassed:** Although [README.md](file:///Users/jiawei/Desktop/insclaude/feline-research-os/README.md#L197) details a bilingual compiled content strategy, the active routing and loading functions in [scripts/query.py:949](file:///Users/jiawei/Desktop/insclaude/feline-research-os/scripts/query.py#L949) hardcode English-only paths, completely ignoring bilingual counterparts (`*-bilingual.md`).
* `[INFERENCE]` The bilingual files are legacy assets from a previous project scope that have since been bypassed by the newer automated Q&A pipeline.
* `[CONFIRMED FACT]` **Stale Handoff Claims:** Chronological handoffs in the root directory state that "all tests pass" and the vault is "production-ready," which is contradicted by the current broken dataclass imports and uncommitted worktree changes.

---

## 4. Technical Risks

* `[CONFIRMED FACT]` **Critical Dataclass TypeError:** In the uncommitted changes of [core/schemas.py:475](file:///Users/jiawei/Desktop/insclaude/feline-research-os/core/schemas.py#L475), the field `schema_version` (with default value) is defined before `task_type` (non-default value) in the `ResearchRecord` dataclass. This throws `TypeError: non-default argument 'task_type' follows default argument 'schema_version'` at import time, preventing the Streamlit UI from starting.
* `[CONFIRMED FACT]` **Dirty Worktree Git Risk:** The working tree contains $180$ modified tracked files and $474$ untracked files. Standard git branch resets or checkouts run in this state present an extreme risk of local session data loss.
* `[CONFIRMED FACT]` **Test Environment Package Mismatch:** The system Python contains `pytest` but lacks `streamlit`, while the virtual environment `.venv` has `streamlit` but lacks `pytest`. This prevents running case test runners inside the standard `.venv` shell.
* `[CONFIRMED FACT]` **Broken Link Warnings:** 6 broken Markdown links (placeholder names and absolute user-directory paths) exist in root handoff documents.

---

## 5. Research OS Gaps

* `[CONFIRMED FACT]` **Lexical Matcher Constraints:** Evidence card validation is lexical rather than semantic, which creates a risk of false-positive matches (e.g., matching negated terms).
* `[CONFIRMED FACT]` **Signatures are Plaintext:** Reviewer identities and case sign-offs are entered as unverified text strings in the UI with no cryptographic verification or user authentication channels.
* `[INFERENCE]` Because research records are kept as individual local JSON files, concurrent multi-user execution will likely lead to file write contention and data loss.

---

## 6. Priorities & Contained Next Steps

### Prioritized Roadmap
1. **Phase 0 (Stabilization):** Solve the dataclass import error, batch-commit dirty worktree files, and add missing dependencies.
2. **Phase 1 (Clarity):** Archive old handoffs, resolve bilingual path conflicts, and fix broken markdown links.
3. **Phase 2 (Workflow Integration):** Test the Gate 6A/6B transient Research Record saving and Claim Promotion paths inside the running UI.

### Open Questions
* **Bilingual Policy:** Should `*-bilingual.md` files be integrated into the automated query pipeline or pruned?
* **Authentication Details:** How should Streamlit session logins be structured for secure reviewer sign-offs?

### Recommended First Task for Next Agent
* **Task Title:** Fix Dataclass Parameter Ordering in core/schemas.py
* **Rationale:** Resolves the critical import error crashing UI startup.
* **Scope:** Reorder fields in `ResearchRecord` in [core/schemas.py](file:///Users/jiawei/Desktop/insclaude/feline-research-os/core/schemas.py) so that all fields with default values follow fields without default values.
* **Validation Method:** Execute `.venv/bin/python -c "import scripts.app"`.
* **Completion Criteria:** Script runs without raising TypeErrors.
* **Preferred Executor:** **Codex** (for localized syntax fix).
