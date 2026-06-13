#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PORT="${PORT:-8502}"
export OPENROUTER_DAILY_BUDGET_USD="${OPENROUTER_DAILY_BUDGET_USD:-1.00}"
export OPENROUTER_MODEL="${OPENROUTER_MODEL:-openai/gpt-4.1-mini}"
export USE_RESULT_PRESENTATION_V2="${USE_RESULT_PRESENTATION_V2:-1}"

cat <<EOF
Starting Ask the vault test page:
  URL: http://localhost:${PORT}
  OPENROUTER_DAILY_BUDGET_USD=${OPENROUTER_DAILY_BUDGET_USD}
  OPENROUTER_MODEL=${OPENROUTER_MODEL}
  USE_RESULT_PRESENTATION_V2=${USE_RESULT_PRESENTATION_V2}

Before live OpenRouter questions, confirm the OpenRouter dashboard has the matching \$1/day cap.
EOF

exec .venv/bin/python -m streamlit run scripts/app.py \
  --server.headless true \
  --server.port "${PORT}"
