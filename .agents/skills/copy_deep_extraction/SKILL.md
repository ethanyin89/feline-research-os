---
name: copy_deep_extraction
description: Automates copying deep‑extraction markdown drafts from the desktop into the project's raw/deep‑extractions folder.
---

# Overview
This skill provides a repeatable workflow for the *copy‑draft* task used in the Feline Research OS project. It replaces the manual copy‑paste steps with a small Python script that:
1. Scans the user's Desktop for `*.deep extract.md` files.
2. Copies each file to `raw/deep-extractions/` under a standardized name `ext-src-<slug>.md`.
3. Logs successes and failures to a `copy_deep_extraction.log` file.

# Usage
```bash
agy run copy_deep_extraction --source "~/Desktop" --target "raw/deep-extractions"
```
The script will:
- Preserve the original file content.
- Generate a slug from the original filename (lower‑case, alphanumeric, hyphens).
- Overwrite only if the target does not already exist (prevent accidental data loss).

# Implementation Details
- Implemented in Python 3.9+.
- Relies on the standard library (`os`, `shutil`, `re`, `logging`).
- Idempotent: running multiple times safely skips already‑copied files.
- Can be scheduled via the existing `setup_cron.sh` script for automated runs.

# Files
- `scripts/copy_deep_extraction.py` – core logic.
- `README.md` – short usage guide (auto‑generated).

# Testing
Run `python -m unittest discover -s scripts` after adding unit tests (optional).

# Next Steps
1. Review the generated script.
2. Optionally add unit tests under `scripts/tests/`.
3. If automated runs are desired, add a cron entry using `schedule` tool.

# Disclaimer
This skill follows the workspace rule: manual copies have been performed 4 ×; now this skill will handle future copies automatically.
