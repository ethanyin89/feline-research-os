#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

BACKEND="${BACKEND:-anthropic}"
OPENROUTER_MODEL_DEFAULT="${OPENROUTER_MODEL:-openai/gpt-5-mini}"

if [[ "$BACKEND" == "openrouter" && -z "${OPENROUTER_API_KEY:-}" ]]; then
  echo "Missing OPENROUTER_API_KEY" >&2
  exit 1
fi
if [[ "$BACKEND" == "openrouter" && -z "${OPENROUTER_DAILY_BUDGET_USD:-}" ]]; then
  echo "Missing OPENROUTER_DAILY_BUDGET_USD. Set it to 1.00 after setting the OpenRouter dashboard limit to $1/day." >&2
  exit 1
fi
if [[ "$BACKEND" == "openrouter" ]]; then
  python3 - <<'PY'
import os
import sys
budget = os.environ.get("OPENROUTER_DAILY_BUDGET_USD", "")
try:
    value = float(budget)
except ValueError:
    print("OPENROUTER_DAILY_BUDGET_USD must be numeric", file=sys.stderr)
    raise SystemExit(1)
if value <= 0 or value > 1.00:
    print("OPENROUTER_DAILY_BUDGET_USD must be greater than 0 and no more than 1.00", file=sys.stderr)
    raise SystemExit(1)
PY
fi

echo "[day1] Backend: $BACKEND"
if [[ "$BACKEND" == "openrouter" ]]; then
  echo "[day1] Model: $OPENROUTER_MODEL_DEFAULT"
  echo "[day1] Project daily budget guard: \$${OPENROUTER_DAILY_BUDGET_USD}"
fi

echo "[day1] Step 1/4: local sanity"
python3 scripts/test_query.py
python3 -m py_compile scripts/query.py scripts/run_acceptance_checklist.py scripts/app.py

echo "[day1] Step 2/4: smoke question 1"
python3 scripts/query.py "CKD 的核心机制主线是什么？" --backend "$BACKEND"

echo "[day1] Step 3/4: smoke question 2"
python3 scripts/query.py "Compare CKD and HCM on the maturity of their endpoint architecture." --backend "$BACKEND"

echo "[day1] Step 4/4: acceptance template + full run"
python3 scripts/run_acceptance_checklist.py --template-only
python3 scripts/run_acceptance_checklist.py --backend "$BACKEND"

echo "[day1] Done"
echo "[day1] Report: system/health-checks/ask-the-vault-acceptance-report-$(date +%Y%m%d).md"
