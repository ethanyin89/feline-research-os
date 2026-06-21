#!/usr/bin/env python3
"""
Statically check Streamlit widget keys in render contexts and loops
using AST analysis.
"""

import ast
import sys
from pathlib import Path

PATHS_TO_SCAN = [
    "scripts/app.py",
    "scripts/research_case_ui.py",
    "scripts/research_record_ui.py",
]

class StreamlitKeyLinter(ast.NodeVisitor):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.violations = []
        self.scope_stack = []

    def visit_FunctionDef(self, node):
        self.scope_stack.append(node)
        self.generic_visit(node)
        self.scope_stack.pop()

    def visit_AsyncFunctionDef(self, node):
        self.scope_stack.append(node)
        self.generic_visit(node)
        self.scope_stack.pop()

    def visit_For(self, node):
        self.scope_stack.append(node)
        self.generic_visit(node)
        self.scope_stack.pop()

    def visit_While(self, node):
        self.scope_stack.append(node)
        self.generic_visit(node)
        self.scope_stack.pop()

    def visit_ListComp(self, node):
        self.scope_stack.append(node)
        self.generic_visit(node)
        self.scope_stack.pop()

    def visit_Call(self, node):
        # Check if it is st.<widget>
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == 'st':
            widget_type = node.func.attr
            if widget_type in {'button', 'selectbox', 'checkbox', 'text_input', 'text_area', 'multiselect', 'slider', 'radio', 'number_input'}:
                self.check_widget(node, widget_type)
        self.generic_visit(node)

    def check_widget(self, node, widget_type):
        in_loop = False
        in_render = False
        context_desc = ""
        
        for parent in reversed(self.scope_stack):
            if isinstance(parent, (ast.For, ast.While, ast.ListComp)):
                in_loop = True
                context_desc = "loop"
                break
            if isinstance(parent, ast.FunctionDef) and (parent.name.startswith("render_") or parent.name.startswith("_render_")):
                in_render = True
                context_desc = f"render function `{parent.name}`"
                break

        if not (in_loop or in_render):
            return

        # Find key keyword argument
        key_arg = None
        for kw in node.keywords:
            if kw.arg == 'key':
                key_arg = kw.value
                break

        if key_arg is None:
            # If it's inside st.form, we can check if it is within a form context (ignoring warning if inside a simple form),
            # but inside dynamic messages / loop contexts, a key is mandatory.
            # Let's see if the parent scopes indicate form usage.
            self.violations.append(
                f"L{node.lineno}: Widget `st.{widget_type}` in {context_desc} has no `key=` parameter."
            )
            return

        # Check if key is static
        is_static = False
        key_repr = "expression"
        try:
            key_repr = ast.unparse(key_arg)
        except Exception:
            pass
            
        if isinstance(key_arg, ast.Constant) and isinstance(key_arg.value, str):
            is_static = True
        elif isinstance(key_arg, ast.JoinedStr):
            # Check if there are no formatted values (i.e. no {var})
            if not any(isinstance(val, ast.FormattedValue) for val in key_arg.values):
                is_static = True

        if is_static:
            self.violations.append(
                f"L{node.lineno}: Widget `st.{widget_type}` in {context_desc} uses a static key: {key_repr}"
            )
            return

        # Verify dynamic variables are referenced in name or string attributes
        referenced_names = []
        for child in ast.walk(key_arg):
            if isinstance(child, ast.Name):
                referenced_names.append(child.id)
            elif isinstance(child, ast.Constant) and isinstance(child.value, str):
                for term in ['key_prefix', 'prefix', 'record_id', 'card_id', 'cache_key', 'i', 'idx', 'uuid', 'id']:
                    if term in child.value:
                        referenced_names.append(term)
                        
        has_dynamic_var = any(
            any(term in name for term in ['key_prefix', 'prefix', 'record_id', 'card_id', 'cache_key', 'i', 'idx', 'uuid', 'id', 'case_id', 'mode_id'])
            for name in referenced_names
        )
        if not has_dynamic_var:
            self.violations.append(
                f"L{node.lineno}: Widget `st.{widget_type}` in {context_desc} uses key `{key_repr}` but doesn't seem to incorporate a key prefix or iteration index."
            )

def main():
    workspace_root = Path(__file__).parent.parent.parent.parent.parent
    has_violations = False
    
    print("--- Streamlit Key AST Checker ---")
    for rel_path in PATHS_TO_SCAN:
        file_path = workspace_root / rel_path
        if not file_path.exists():
            print(f"Skipping {rel_path} (does not exist)")
            continue
            
        print(f"Scanning {rel_path}...")
        try:
            tree = ast.parse(file_path.read_text(encoding="utf-8"), filename=str(file_path))
            visitor = StreamlitKeyLinter(str(file_path))
            visitor.visit(tree)
            if visitor.violations:
                has_violations = True
                for v in visitor.violations:
                    print(f"  [VIOLATION] {v}")
            else:
                print("  Clean!")
        except Exception as e:
            print(f"  Failed to parse {rel_path}: {e}")
            has_violations = True
            
    if has_violations:
        print("\nResult: Hazards identified.")
        sys.exit(1)
    else:
        print("\nResult: All files clean of static key hazards!")
        sys.exit(0)

if __name__ == "__main__":
    main()
