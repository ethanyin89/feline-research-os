# Feline Research OS Workspace Rules

These guidelines are automatically applied to coding work in this project.

## Repeatable Tasks → Skills

If a task will be done more than once, it MUST be codified:
1. Run 3-10 samples manually first
2. After approval, create a skill file or script
3. If automatic running needed, set cron

Test: If the user asks for the same thing twice, you failed.

### Available Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/add_v2_fields.py` | Add V2 enhanced fields to source cards | `OPENROUTER_DAILY_BUDGET_USD=1.00 .venv/bin/python scripts/add_v2_fields.py --disease fcv --limit 5` |
| `scripts/fetch_abstracts.py` | Fetch abstracts and PMC figures | `.venv/bin/python scripts/fetch_abstracts.py --limit 4` |
| `scripts/auto_extract_literature.py` | Auto-extract placeholder papers | `.venv/bin/python scripts/auto_extract_literature.py` |
| `scripts/health.py` | Generate vault health report | `.venv/bin/python scripts/health.py` |
| `scripts/setup_cron.sh` | Set up daily health check automation | `./scripts/setup_cron.sh` |

### Automation Setup

```bash
# Install daily health check (runs at 9:00 AM)
./scripts/setup_cron.sh

# Check if running
launchctl list | grep feline

# Remove automation
./scripts/setup_cron.sh --remove
```

## Streamlit Development Constraints

To prevent duplicate widget key exceptions (`StreamlitDuplicateElementKey`) in multi-turn conversation logs:

1. **Mandatory Dynamic Keys in Loops & Chat Blocks**: Any widget rendered inside the chat log rendering loop (such as `render_answer_block`, `render_answer_block_v2`, `render_translatable_content`, `render_source_card_v2`, and their helper routines) **MUST** accept and incorporate a `key_prefix` or dynamic iteration index.
2. **Exclusion / Separation**: Top-level UI panels that render exactly once (e.g. sidebar parameters or tab selectors) may use static keys. Form widgets on static pages (like Case Workspace) may rely on form namespaces or record IDs.
3. **Verification**: After modifying any files rendering Streamlit widgets, run the AST linter:
   ```bash
   .venv/bin/python .agents/skills/streamlit_key_guard/scripts/lint_streamlit_keys.py
   ```
   Ensure no new duplicate key violations or static widget key hazards are introduced.
