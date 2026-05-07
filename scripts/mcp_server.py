#!/usr/bin/env python3
"""
scripts/mcp_server.py — MCP (Model Context Protocol) server for the feline research OS.

Exposes vault tools to external LLM agents via stdin/stdout JSON-RPC.

Tools exposed:
  - vault_search: Full-text search across vault .md files
  - vault_query: Route + hop + synthesize a research question (requires API key)
  - compile_check: Find downstream files needing recompilation after source changes
  - source_list: List all indexed source cards with metadata

Usage:
    # Start the MCP server (reads JSON-RPC from stdin, writes to stdout)
    python scripts/mcp_server.py

    # In Claude Code settings or MCP client config:
    {
      "mcpServers": {
        "feline-vault": {
          "command": "python3",
          "args": ["scripts/mcp_server.py"],
          "cwd": "/path/to/feline-research-os"
        }
      }
    }

Protocol: MCP over stdio (JSON-RPC 2.0)
"""

import json
import sys
from pathlib import Path

# Ensure scripts/ is importable
sys.path.insert(0, str(Path(__file__).parent))

from search import vault_search, format_results_for_llm
from compile_trigger import find_downstream_files, build_recompile_queue
from query import build_source_index, VAULT_ROOT

# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------

TOOLS = [
    {
        "name": "vault_search",
        "description": (
            "Full-text search across the feline research OS vault. "
            "Searches .md files for a query string (plain text or regex). "
            "Returns matching files with source IDs, match counts, and context snippets."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query (plain text or regex pattern)",
                },
                "scope": {
                    "type": "string",
                    "enum": ["raw", "topics", "system", "entities", "all"],
                    "description": "Limit search to a directory scope (default: all)",
                    "default": "all",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of results (default: 10)",
                    "default": 10,
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "compile_check",
        "description": (
            "Check which downstream files need recompilation after source card changes. "
            "Given a list of source IDs, finds all topic pages, indexes, and outputs "
            "that reference them."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "source_ids": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of source IDs to check (e.g. ['src-ckd-001', 'src-ckd-004'])",
                },
            },
            "required": ["source_ids"],
        },
    },
    {
        "name": "source_list",
        "description": (
            "List all indexed source cards in the vault with their IDs and file paths. "
            "Useful for discovering what sources are available before querying."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "disease_filter": {
                    "type": "string",
                    "description": "Filter by disease prefix (e.g. 'ckd', 'fip', 'hcm', 'ibd')",
                },
            },
        },
    },
]

# ---------------------------------------------------------------------------
# Tool handlers
# ---------------------------------------------------------------------------

def handle_vault_search(args: dict) -> str:
    query = args["query"]
    scope = args.get("scope", "all")
    limit = args.get("limit", 10)
    results = vault_search(query, VAULT_ROOT, scope=scope, limit=limit)
    return format_results_for_llm(results)


def handle_compile_check(args: dict) -> str:
    source_ids = args["source_ids"]
    downstream = find_downstream_files(source_ids, VAULT_ROOT)
    queue = build_recompile_queue(downstream)
    if not queue:
        return f"No downstream files reference {source_ids}."
    lines = [f"RECOMPILE QUEUE ({len(queue)} files):\n"]
    for item in queue:
        sources = ", ".join(item["affected_by"])
        lines.append(f"  {item['file']} (affected by: {sources})")
    return "\n".join(lines)


def handle_source_list(args: dict) -> str:
    index = build_source_index(VAULT_ROOT)
    disease_filter = args.get("disease_filter")
    entries = []
    for sid, path in sorted(index.items()):
        if disease_filter and not sid.startswith(f"src-{disease_filter}-"):
            continue
        rel = str(path.relative_to(VAULT_ROOT))
        entries.append(f"  {sid} → {rel}")
    if not entries:
        return "No source cards found."
    return f"SOURCE CARDS ({len(entries)}):\n" + "\n".join(entries)


HANDLERS = {
    "vault_search": handle_vault_search,
    "compile_check": handle_compile_check,
    "source_list": handle_source_list,
}

# ---------------------------------------------------------------------------
# MCP protocol (JSON-RPC 2.0 over stdio)
# ---------------------------------------------------------------------------

SERVER_INFO = {
    "name": "feline-vault",
    "version": "1.0.0",
}

CAPABILITIES = {
    "tools": {},
}


def make_response(id, result):
    return {"jsonrpc": "2.0", "id": id, "result": result}


def make_error(id, code, message):
    return {"jsonrpc": "2.0", "id": id, "error": {"code": code, "message": message}}


def handle_request(request: dict) -> dict | None:
    method = request.get("method", "")
    id = request.get("id")
    params = request.get("params", {})

    if method == "initialize":
        return make_response(id, {
            "protocolVersion": "2024-11-05",
            "serverInfo": SERVER_INFO,
            "capabilities": CAPABILITIES,
        })

    if method == "notifications/initialized":
        return None  # notification, no response

    if method == "tools/list":
        return make_response(id, {"tools": TOOLS})

    if method == "tools/call":
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})
        handler = HANDLERS.get(tool_name)
        if not handler:
            return make_error(id, -32602, f"Unknown tool: {tool_name}")
        try:
            result_text = handler(arguments)
            return make_response(id, {
                "content": [{"type": "text", "text": result_text}],
            })
        except Exception as e:
            return make_response(id, {
                "content": [{"type": "text", "text": f"Error: {e}"}],
                "isError": True,
            })

    if method == "ping":
        return make_response(id, {})

    # Unknown method
    if id is not None:
        return make_error(id, -32601, f"Method not found: {method}")
    return None


def main():
    """Run MCP server over stdio."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            response = make_error(None, -32700, "Parse error")
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
            continue

        response = handle_request(request)
        if response is not None:
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
