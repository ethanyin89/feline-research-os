#!/usr/bin/env bash
set -euo pipefail

url="${1:-}"
if [[ -z "$url" ]]; then
  echo "usage: $0 https://YOUR-TUNNEL.trycloudflare.com" >&2
  exit 2
fi

url="${url%/}"

echo "== health =="
curl -sS --max-time 15 "$url/health"
echo

echo "== presentation =="
curl -sS --max-time 20 "$url/" \
  | rg -n "Feline Research OS|Answer engine|Condition|Advanced settings|Find by keyword|Research Chat|Ask the vault|chat-form"

echo "== real answer =="
curl -sS --max-time 180 \
  -X POST \
  --data-urlencode "backend=local" \
  --data-urlencode "question=FIP怎么识别" \
  --data-urlencode "disease=auto" \
  --data-urlencode "max_hops=2" \
  "$url/ask" \
  | rg -n "local</code>|recognition|FIP怎么识别|立即就医|src-fip-006|Sources|Read path"

echo "== local endpoint surface =="
curl -sS --max-time 60 \
  -X POST \
  --data-urlencode "backend=local" \
  --data-urlencode "question=FIP药效评价指标" \
  --data-urlencode "disease=auto" \
  --data-urlencode "max_hops=2" \
  "$url/ask" \
  | rg -n "local</code>|Key-Claim Traceability|FE1|Endpoint Hierarchy|src-fip-003"
