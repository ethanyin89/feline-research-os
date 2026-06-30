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
home_html="$(curl -sS --max-time 20 "$url/")"
printf "%s" "$home_html" \
  | rg -n "Feline Research OS|Answer engine|Condition|Advanced settings|Find by keyword|Research Chat|Ask the vault|chat-form|Evidence-backed feline health answers"
if printf "%s" "$home_html" | rg -q "src-[a-z0-9-]+-[0-9]{3}|source cards|vault index|local vault|来源清单|title-only|deep [0-9]+|abstract [0-9]+"; then
  echo "public page leaked internal vault details" >&2
  exit 1
fi

echo "== real answer =="
answer_html="$(curl -sS --max-time 180 \
  -X POST \
  --data-urlencode "backend=local" \
  --data-urlencode "question=FIP怎么识别" \
  --data-urlencode "disease=auto" \
  --data-urlencode "max_hops=2" \
  "$url/ask")"
printf "%s" "$answer_html" \
  | rg -n "recognition|FIP怎么识别|立即就医|来源支持|Sources|Read path|A review of feline infectious peritonitis virus infection"
if printf "%s" "$answer_html" | rg -q "src-[a-z0-9-]+-[0-9]{3}|source cards|local vault|Readings loaded|local</code>|raw/papers|topics/|来源清单|title-only|deep [0-9]+|abstract [0-9]+|文献 \\[\\]"; then
  echo "answer leaked internal vault details" >&2
  exit 1
fi

echo "== ckd ordinary answer =="
ckd_html="$(curl -sS --max-time 120 \
  -X POST \
  --data-urlencode "backend=local" \
  --data-urlencode "question=解释CKD" \
  --data-urlencode "disease=auto" \
  --data-urlencode "max_hops=2" \
  "$url/ask")"
printf "%s" "$ckd_html" \
  | rg -n "解释CKD|什么是猫慢性肾病|来源支持|Sources|ISFM Consensus Guidelines"
if printf "%s" "$ckd_html" | rg -q "src-[a-z0-9-]+-[0-9]{3}|source cards|local vault|Readings loaded|local</code>|raw/papers|topics/|来源清单|title-only|deep [0-9]+|abstract [0-9]+|文献 \\[\\]|\\.md\\b|Source IDs"; then
  echo "ckd answer leaked internal vault details" >&2
  exit 1
fi

echo "== local endpoint surface =="
endpoint_html="$(curl -sS --max-time 60 \
  -X POST \
  --data-urlencode "backend=local" \
  --data-urlencode "question=FIP药效评价指标" \
  --data-urlencode "disease=auto" \
  --data-urlencode "max_hops=2" \
  "$url/ask")"
printf "%s" "$endpoint_html" \
  | rg -n "Key-Claim Traceability|FE1|Endpoint Hierarchy|来源支持|Sources"
if printf "%s" "$endpoint_html" | rg -q "src-[a-z0-9-]+-[0-9]{3}|source cards|local vault|Readings loaded|local</code>|raw/papers|topics/|来源清单|title-only|deep [0-9]+|abstract [0-9]+|文献 \\[\\]"; then
  echo "endpoint surface leaked internal vault details" >&2
  exit 1
fi
