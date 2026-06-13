#!/usr/bin/env python3
"""
Minimal public HTTP test page for Ask the Vault.

This intentionally avoids Streamlit/websockets so temporary public tunnels can
serve ordinary-user smoke tests over plain HTTP.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from query import (  # noqa: E402
    OPENROUTER_MODEL,
    build_source_index,
    build_source_titles,
    build_source_weights,
    make_client,
    parse_source_ids_from_answer,
    run_local_query_core,
    run_query_core,
)
from local_answer_surfaces import build_local_surface_answer  # noqa: E402

EXAMPLE_QUESTIONS = [
    "解释CKD",
    "FIP怎么识别",
    "HCM是什么，为什么危险",
    "IBD和淋巴瘤怎么区分",
    "糖尿病猫为什么会缓解",
    "我的猫肌酐升高，这个库能告诉我什么",
]


def vault_counts() -> tuple[int, int, int]:
    source_count = len(PublicTestHandler.source_index)
    topic_count = len(list((VAULT_ROOT / "topics").rglob("*.md")))
    disease_count = len([p for p in (VAULT_ROOT / "topics").iterdir() if p.is_dir()])
    return source_count, topic_count, disease_count


def render_provenance(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(
        r"\[quoted_fact: ([^\]]+)\]",
        r'<span class="prov-badge prov-quoted">直接来源: \1</span>',
        escaped,
    )
    escaped = re.sub(
        r"\[source_supported_conclusion: ([^\]]+)\]",
        r'<span class="prov-badge prov-supported">来源支持: \1</span>',
        escaped,
    )
    escaped = re.sub(
        r"\[llm_inference\]",
        r'<span class="prov-badge prov-inference">分析推断</span>',
        escaped,
    )
    return escaped


def provenance_counts(answer: str) -> dict[str, int]:
    return {
        "quoted": len(re.findall(r"\[quoted_fact:\s*[^\]]+\]", answer)),
        "supported": len(re.findall(r"\[source_supported_conclusion:\s*[^\]]+\]", answer)),
        "inference": len(re.findall(r"\[llm_inference\]", answer)),
    }


def confidence_for_answer(answer: str) -> str:
    counts = provenance_counts(answer)
    if counts["inference"] == 0 and (counts["quoted"] + counts["supported"]) >= 2:
        return "high"
    if counts["quoted"] + counts["supported"]:
        return "medium"
    return "low"


def render_source_titles(source_ids: list[str], limit: int = 6) -> str:
    titles = PublicTestHandler.source_titles
    rows: list[str] = []
    for sid in source_ids[:limit]:
        title = titles.get(sid, sid)
        rows.append(f"<div class='source-row'>· {html.escape(title)}</div>")
    if len(source_ids) > limit:
        rows.append(f"<div class='source-more'>+ {len(source_ids) - limit} more source ids loaded</div>")
    return "\n".join(rows)


def render_page(
    answer_html: str = "",
    question: str = "",
    status_html: str = "",
    backend_choice: str = "local",
    disease_choice: str = "auto",
    max_hops: int = 3,
) -> bytes:
    source_count, topic_count, disease_count = vault_counts()
    examples = "\n".join(
        f"<button class='chip' name='question' value='{html.escape(q, quote=True)}'>{html.escape(q)}</button>"
        for q in EXAMPLE_QUESTIONS
    )
    escaped_question = html.escape(question, quote=True)
    disease_options = [
        ("auto", "Auto-detect"),
        ("ckd", "CKD"),
        ("hcm", "HCM"),
        ("fip", "FIP"),
        ("ibd", "IBD"),
        ("diabetes", "Diabetes"),
        ("fcv", "FCV"),
    ]
    disease_select = "\n".join(
        "<option value='{value}'{selected}>{label}</option>".format(
            value=html.escape(value, quote=True),
            label=html.escape(label),
            selected=" selected" if value == disease_choice else "",
        )
        for value, label in disease_options
    )
    backend_options = [
        ("local", "Vault Search (free)"),
        ("openrouter", "OpenRouter (API)"),
    ]
    backend_select = "\n".join(
        "<option value='{value}'{selected}>{label}</option>".format(
            value=html.escape(value, quote=True),
            label=html.escape(label),
            selected=" selected" if value == backend_choice else "",
        )
        for value, label in backend_options
    )
    engine_label = "local vault search" if backend_choice == "local" else OPENROUTER_MODEL
    engine_notice = (
        "Free local mode is selected. No API call will be made."
        if backend_choice == "local"
        else "OpenRouter API mode is selected. This may spend project API budget."
    )
    body = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ask the Vault Public Test</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #0f1117;
      --surface: #1a1d27;
      --surface-2: #222535;
      --border: #2d3147;
      --text: #e8eaf0;
      --muted: #8b90a0;
      --subtle: #4a4f64;
      --accent: #ef4444;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font: 15px/1.7 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    .app {{ min-height: 100vh; display: grid; grid-template-columns: 356px minmax(0, 1fr); }}
    aside {{
      border-right: 1px solid var(--border);
      background: #11151f;
      padding: 72px 24px 28px;
    }}
    main {{ min-width: 0; padding: 48px clamp(24px, 12vw, 250px) 128px; }}
    .vault-panel {{
      background: rgba(26,29,39,0.72);
      border: 1px solid rgba(45,49,71,0.9);
      border-radius: 10px;
      padding: 16px;
    }}
    .vault-kicker, .vault-panel-label {{
      color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 11px;
      letter-spacing: .08em;
      text-transform: uppercase;
      margin-bottom: 8px;
    }}
    h1 {{ margin: 0; font-size: 32px; line-height: 1.08; font-weight: 600; }}
    p {{ color: var(--muted); margin: 8px 0 0; }}
    .divider {{ height: 1px; background: var(--border); margin: 52px 0 36px; }}
    .field {{ margin: 0 0 18px; }}
    select, input, textarea {{
      width: 100%;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 11px 14px;
      background: var(--surface);
      color: var(--text);
      font: inherit;
    }}
    .notice {{
      margin: 12px 0;
      padding: 10px 12px;
      border-radius: 8px;
      border: 1px solid rgba(22,163,74,0.22);
      background: rgba(22,163,74,0.08);
      color: #79d094;
      font-size: 13px;
    }}
    details {{
      border: 1px solid var(--border);
      border-radius: 10px;
      background: rgba(26,29,39,0.44);
      overflow: hidden;
      margin: 18px 0 34px;
    }}
    summary {{ padding: 13px 16px; background: rgba(26,29,39,0.84); cursor: pointer; }}
    .details-body {{ padding: 14px 16px; }}
    .meta-row {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      margin-top: 8px;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 11px;
      color: var(--muted);
    }}
    .meta-row strong {{ color: var(--text); font-weight: 500; }}
    .main-header {{ padding: 4px 0 18px; }}
    .statline {{
      margin-top: 14px;
      color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 11px;
    }}
    .try-panel {{ margin: 24px 0 10px; }}
    .examples {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 10px; }}
    button {{
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 10px 13px;
      background: var(--surface);
      color: var(--text);
      cursor: pointer;
      font: inherit;
      text-align: left;
    }}
    button:hover {{ background: var(--surface-2); border-color: #3a3f58; }}
    .chat-form {{
      position: fixed;
      left: 356px;
      right: 0;
      bottom: 0;
      padding: 18px clamp(24px, 12vw, 250px) 24px;
      background: linear-gradient(180deg, rgba(15,17,23,0) 0%, rgba(15,17,23,0.92) 22%, rgba(15,17,23,1) 100%);
    }}
    .chat-box {{ display: grid; grid-template-columns: minmax(0, 1fr) 44px; gap: 8px; background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 8px; }}
    .chat-box textarea {{
      min-height: 42px;
      max-height: 120px;
      resize: vertical;
      border: 0;
      padding: 8px 10px;
      background: transparent;
    }}
    .send {{ display: grid; place-items: center; text-align: center; background: #3a3f58; }}
    .status, .answer-card, .chat-message {{
      border: 1px solid rgba(45,49,71,0.72);
      border-radius: 8px;
      background: rgba(26,29,39,0.58);
      padding: 16px 18px;
      margin-top: 18px;
    }}
    .chat-message.user {{ max-width: 720px; margin-left: auto; background: rgba(34,37,53,0.72); }}
    .answer-card {{ max-width: 760px; }}
    .answer-card pre {{
      white-space: pre-wrap;
      overflow-wrap: anywhere;
      font: inherit;
      margin: 0;
    }}
    .trust, .sources {{
      margin-top: 16px;
      padding: 10px 12px;
      border: 1px solid rgba(202,138,4,0.22);
      border-radius: 8px;
      background: rgba(202,138,4,0.08);
      color: #d6b56b;
      font-size: 13px;
    }}
    .source-row, .source-more {{ color: var(--muted); font-size: 13px; margin-top: 4px; }}
    .prov-badge {{
      display: inline-flex;
      align-items: center;
      padding: 2px 8px;
      border-radius: 4px;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 11px;
      white-space: nowrap;
      border: 1px solid transparent;
    }}
    .prov-quoted {{ color: #16a34a; background: rgba(22,163,74,0.12); border-color: rgba(22,163,74,0.25); }}
    .prov-supported {{ color: #ca8a04; background: rgba(202,138,4,0.12); border-color: rgba(202,138,4,0.25); }}
    .prov-inference {{ color: #6b7280; background: rgba(107,114,128,0.12); border-color: rgba(107,114,128,0.25); }}
    code {{
      color: var(--text);
      background: rgba(34,37,53,0.9);
      padding: 1px 6px;
      border-radius: 4px;
      border: 1px solid rgba(45,49,71,0.8);
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    }}
    @media (max-width: 860px) {{
      .app {{ grid-template-columns: 1fr; }}
      aside {{ border-right: 0; border-bottom: 1px solid var(--border); padding: 24px; }}
      main {{ padding: 28px 20px 140px; }}
      .chat-form {{ left: 0; padding: 18px 20px 22px; }}
      .examples {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
<div class="app">
  <aside>
    <div class="vault-panel">
      <div class="vault-kicker">Feline Research OS</div>
      <h1 style="font-size:20px">Ask the vault</h1>
      <p>Ask a natural question. Get evidence, uncertainty, and a next step.</p>
    </div>
    <div class="divider"></div>
    <div id="settings">
      <div class="vault-panel-label">Answer engine</div>
      <div class="field"><select name="backend" form="ask-form">{backend_select}</select></div>
      <div class="notice">{html.escape(engine_notice)}</div>
      <div class="vault-panel-label" style="margin-top:24px">Condition</div>
      <div class="field"><select name="disease" form="ask-form">{disease_select}</select></div>
      <details>
        <summary>Advanced settings</summary>
        <div class="details-body">
          <label class="vault-panel-label" for="max_hops">Depth</label>
          <input id="max_hops" name="max_hops" form="ask-form" type="number" min="1" max="5" value="{int(max_hops)}">
        </div>
      </details>
      <div class="divider"></div>
      <div class="vault-panel-label">Find by keyword</div>
      <div class="field"><input name="keyword" placeholder="Try phosphorus, SDMA, fibrosis..."></div>
      <div class="vault-panel vault-sidebar-meta">
        <div class="meta-row"><span>engine</span><strong>{html.escape(engine_label)}</strong></div>
        <div class="meta-row"><span>vault index</span><strong>{source_count} sources</strong></div>
        <div class="meta-row"><span>public mode</span><strong>HTTP form</strong></div>
      </div>
    </div>
  </aside>
  <main>
    <div class="main-header">
      <div class="vault-kicker">Research Chat</div>
      <h1>Ask the vault</h1>
      <div class="statline">{source_count} sources · {topic_count} topic pages · {disease_count} diseases</div>
    </div>
    <div class="vault-panel try-panel"><div class="vault-panel-label">Try asking</div></div>
    <form method="post" action="/ask" class="examples">
      <input type="hidden" name="backend" value="{html.escape(backend_choice, quote=True)}">
      <input type="hidden" name="disease" value="{html.escape(disease_choice, quote=True)}">
      <input type="hidden" name="max_hops" value="{int(max_hops)}">
      {examples}
    </form>
    {status_html}
    {answer_html}
  </main>
</div>
<form method="post" action="/ask" class="chat-form" id="ask-form">
  <div class="chat-box">
    <textarea name="question" placeholder="Ask a natural feline health question...">{escaped_question}</textarea>
    <button class="send" type="submit" aria-label="Ask">↑</button>
  </div>
</form>
</body>
</html>"""
    return body.encode("utf-8")


class PublicTestHandler(BaseHTTPRequestHandler):
    source_index = build_source_index(VAULT_ROOT)
    source_weights = build_source_weights(VAULT_ROOT)
    source_titles = build_source_titles(VAULT_ROOT)

    def log_message(self, fmt: str, *args) -> None:
        print(f"[public-test] {self.address_string()} - {fmt % args}", file=sys.stderr)

    def _send_html(self, body: bytes, status: int = 200) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            body = b"ok"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        self._send_html(render_page())

    def do_POST(self) -> None:
        if urllib.parse.urlparse(self.path).path != "/ask":
            self._send_html(render_page(status_html="<div class='status'>Not found.</div>"), 404)
            return

        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(min(length, 20_000)).decode("utf-8", errors="replace")
        fields = urllib.parse.parse_qs(raw)
        question = next(
            (
                value.strip()
                for value in fields.get("question", [])
                if isinstance(value, str) and value.strip()
            ),
            "",
        )
        disease_choice = fields.get("disease", ["auto"])[0]
        if disease_choice not in {"auto", "ckd", "hcm", "fip", "ibd", "diabetes", "fcv"}:
            disease_choice = "auto"
        backend_choice = fields.get("backend", ["local"])[0]
        if backend_choice not in {"local", "openrouter"}:
            backend_choice = "local"
        try:
            max_hops = int(fields.get("max_hops", ["3"])[0])
        except (TypeError, ValueError):
            max_hops = 3
        max_hops = max(1, min(5, max_hops))
        if not question:
            status = "<div class='status'>Please enter a question.</div>"
            self._send_html(
                render_page(
                    question=question,
                    status_html=status,
                    backend_choice=backend_choice,
                    disease_choice=disease_choice,
                    max_hops=max_hops,
                ),
                400,
            )
            return

        statuses: list[str] = []
        started = time.time()
        try:
            disease_hint = None if disease_choice == "auto" else disease_choice
            if backend_choice == "local":
                statuses.append("Checking deterministic local surfaces...")
                result = build_local_surface_answer(
                    question=question,
                    vault_root=VAULT_ROOT,
                    disease_hint=disease_hint,
                )
                if result is None:
                    result = run_local_query_core(
                        question=question,
                        vault_root=VAULT_ROOT,
                        source_index=self.source_index,
                        source_weights=self.source_weights,
                        disease_hint=disease_hint,
                        search_limit=max(6, max_hops * 2),
                        on_status=statuses.append,
                    )
            else:
                client = make_client("openrouter")
                result = run_query_core(
                    client=client,
                    question=question,
                    vault_root=VAULT_ROOT,
                    source_index=self.source_index,
                    source_weights=self.source_weights,
                    disease_hint=disease_hint,
                    max_hops=max_hops,
                    model=OPENROUTER_MODEL,
                    on_status=statuses.append,
                )
            answer = str(result.get("answer", "")).strip()
            source_ids = list(result.get("loaded_source_ids") or parse_source_ids_from_answer(answer))
            confidence = confidence_for_answer(answer)
            counts = provenance_counts(answer)
            sourced_claims = counts["quoted"] + counts["supported"]
            engine_meta = "local" if backend_choice == "local" else OPENROUTER_MODEL
            meta = (
                f"<div class='statline'><code>{html.escape(str(result.get('disease', 'unknown')))}</code> "
                f"<code>{html.escape(str(result.get('question_type', 'unknown')))}</code> "
                f"<code>{html.escape(engine_meta)}</code> "
                f"<code>{len(source_ids)} sources</code> "
                f"<code>{time.time() - started:.1f}s</code></div>"
            )
            trust = (
                "<div class='trust'>"
                f"Confidence: {confidence}. {sourced_claims} sourced claim tags and "
                f"{counts['inference']} inference tags. Readings loaded: {len(source_ids)}."
                "</div>"
            )
            sources = ""
            if source_ids:
                sources = (
                    "<div class='sources'><div class='vault-panel-label'>Sources</div>"
                    f"{render_source_titles(source_ids)}</div>"
                )
            answer_html = (
                f"<section class='chat-message user'>{html.escape(question)}</section>"
                "<section class='answer-card'>"
                f"{meta}<pre>{render_provenance(answer)}</pre>{trust}{sources}</section>"
            )
            status_html = ""
            if statuses:
                status_html = (
                    "<div class='status'><div class='vault-panel-label'>Read path</div>"
                    + "<br>".join(html.escape(s) for s in statuses[-6:])
                    + "</div>"
                )
            self._send_html(
                render_page(
                    answer_html=answer_html,
                    question=question,
                    status_html=status_html,
                    backend_choice=backend_choice,
                    disease_choice=disease_choice,
                    max_hops=max_hops,
                )
            )
        except Exception as exc:
            status = (
                "<div class='status'><strong>Request failed.</strong><br>"
                f"<pre>{html.escape(type(exc).__name__ + ': ' + str(exc))}</pre></div>"
            )
            self._send_html(
                render_page(
                    question=question,
                    status_html=status,
                    backend_choice=backend_choice,
                    disease_choice=disease_choice,
                    max_hops=max_hops,
                ),
                500,
            )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the public HTTP test page.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8510")))
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), PublicTestHandler)
    print(f"Public test HTTP page: http://{args.host}:{args.port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
