"""
Research Record UI for Streamlit.

Displays research records with harness loop visualization,
verification status, and evidence grounding details.
"""

import html
import sys
from pathlib import Path
from typing import Optional

import streamlit as st

# Add parent directory for core imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import (
    RecordStore,
    TaskEvaluator,
    GapChecker,
    Verifier,
    ValidatedClaimStore,
    ResearchRecord,
    TaskType,
    SearchDepth,
    VerifierStatus,
)


def get_record_store(vault_root: Path) -> RecordStore:
    """Get or create the record store."""
    records_path = vault_root / "system" / "research-records"
    return RecordStore(records_path)


def render_task_type_badge(task_type: TaskType) -> str:
    """Render a colored badge for task type."""
    colors = {
        TaskType.PROTOCOL_DESIGN: ("#8b5cf6", "Protocol"),
        TaskType.ENDPOINT_SELECTION: ("#06b6d4", "Endpoint"),
        TaskType.LITERATURE_REVIEW: ("#10b981", "Literature"),
        TaskType.EVIDENCE_CHECK: ("#f59e0b", "Evidence"),
        TaskType.BIOMARKER_MAPPING: ("#ec4899", "Biomarker"),
        TaskType.MODEL_EVALUATION: ("#6366f1", "Model"),
        TaskType.PK_DESIGN: ("#14b8a6", "PK"),
        TaskType.QUICK_EXPLANATION: ("#94a3b8", "Quick"),
        TaskType.OTHER: ("#64748b", "Other"),
    }
    color, label = colors.get(task_type, ("#64748b", task_type.value))
    return f'<span style="background:{color}22;color:{color};padding:2px 8px;border-radius:4px;font-size:0.75em">{label}</span>'


def render_search_depth_badge(depth: SearchDepth) -> str:
    """Render a badge for search depth."""
    colors = {
        SearchDepth.QUICK: ("#94a3b8", "Quick"),
        SearchDepth.STANDARD: ("#10b981", "Standard"),
        SearchDepth.DEEP: ("#f59e0b", "Deep"),
        SearchDepth.EVIDENCE_AUDIT: ("#ef4444", "Audit"),
    }
    color, label = colors.get(depth, ("#64748b", depth.value))
    return f'<span style="background:{color}22;color:{color};padding:2px 8px;border-radius:4px;font-size:0.75em">{label}</span>'


def render_verifier_status_badge(status: VerifierStatus) -> str:
    """Render a badge for verification status."""
    colors = {
        VerifierStatus.PASSED: ("#10b981", "Passed"),
        VerifierStatus.FAILED: ("#ef4444", "Failed"),
        VerifierStatus.NEEDS_HUMAN_REVIEW: ("#f59e0b", "Review"),
        VerifierStatus.PENDING: ("#94a3b8", "Pending"),
    }
    color, label = colors.get(status, ("#64748b", status.value))
    return f'<span style="background:{color}22;color:{color};padding:2px 8px;border-radius:4px;font-size:0.75em">{label}</span>'


def render_harness_loop_diagram(record: ResearchRecord) -> str:
    """Render an ASCII-style harness loop progress diagram."""
    stages = [
        ("Evaluate", record.task_type != TaskType.OTHER),
        ("Draft", record.draft_versions > 0),
        ("Gap Check", record.gap_checks_performed > 0),
        ("Revise", record.revisions_made > 0),
        ("Verify", len(record.verification_results) > 0),
        ("Final", record.verifier_status == VerifierStatus.PASSED),
    ]

    parts = []
    for name, completed in stages:
        if completed:
            parts.append(f'<span style="color:#10b981">✓ {name}</span>')
        else:
            parts.append(f'<span style="color:#64748b">○ {name}</span>')

    return ' → '.join(parts)


def render_record_card(record: ResearchRecord) -> None:
    """Render a single research record as an expandable card."""
    # Header with badges
    task_badge = render_task_type_badge(record.task_type)
    depth_badge = render_search_depth_badge(record.search_depth)
    status_badge = render_verifier_status_badge(record.verifier_status)

    timestamp = record.timestamp.strftime("%Y-%m-%d %H:%M")
    disease = html.escape(record.disease.upper()) if record.disease else "General"
    request_preview = html.escape(record.user_request[:80])
    if len(record.user_request) > 80:
        request_preview += "..."

    st.markdown(
        f"""
        <div class="vault-panel" style="margin-bottom:12px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
            <span style="font-size:12px;color:#8b90a0">{timestamp}</span>
            <span style="font-size:12px;color:#8b90a0">{disease}</span>
          </div>
          <div style="font-size:14px;color:#e8eaf0;margin-bottom:8px">{request_preview}</div>
          <div style="display:flex;gap:8px;flex-wrap:wrap">
            {task_badge}
            {depth_badge}
            {status_badge}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander(f"Details: {record.record_id}", expanded=False):
        # Full request
        st.markdown("**Request:**")
        st.text(record.user_request)

        # Harness loop progress
        st.markdown("**Harness Loop:**")
        st.markdown(render_harness_loop_diagram(record), unsafe_allow_html=True)

        # Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Drafts", record.draft_versions)
        with col2:
            st.metric("Gap Checks", record.gap_checks_performed)
        with col3:
            st.metric("Revisions", record.revisions_made)

        # Key decisions
        if record.key_decisions:
            st.markdown("**Key Decisions:**")
            for decision in record.key_decisions:
                st.markdown(f"- {decision}")

        # Uncertainties
        if record.uncertainties:
            st.markdown("**Uncertainties:**")
            for uncertainty in record.uncertainties:
                st.markdown(f"- {uncertainty}")

        # Verification results
        if record.verification_results:
            st.markdown("**Verification Results:**")
            for result in record.verification_results:
                icon = "✓" if result.passed else "✗"
                color = "#10b981" if result.passed else "#ef4444"
                st.markdown(
                    f'<span style="color:{color}">{icon}</span> **{result.check_name}** ({result.severity}): {result.message}',
                    unsafe_allow_html=True,
                )

        # Evidence used
        if record.selected_evidence:
            st.markdown("**Evidence Used:**")
            st.text(", ".join(record.selected_evidence))

        # Final answer preview
        if record.final_answer:
            st.markdown("**Answer Preview:**")
            preview = record.final_answer[:500]
            if len(record.final_answer) > 500:
                preview += "..."
            st.text(preview)

        # Next steps
        if record.next_steps:
            st.markdown("**Next Steps:**")
            for step in record.next_steps:
                st.markdown(f"- {step}")


def render_task_evaluator_demo(vault_root: Path) -> None:
    """Interactive demo of the task evaluator."""
    st.markdown("### Query Evaluator Demo")
    st.caption("Test how queries are classified and routed")

    evaluator = TaskEvaluator()

    demo_query = st.text_input(
        "Test query",
        placeholder="e.g., 猫CKD的终点指标有哪些？",
        key="evaluator-demo-query",
    )

    if demo_query:
        evaluation = evaluator.evaluate(demo_query)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Task Type:** {render_task_type_badge(evaluation.task_type)}", unsafe_allow_html=True)
            st.markdown(f"**Disease:** `{evaluation.disease or 'undetected'}`")
            st.markdown(f"**Search Depth:** {render_search_depth_badge(evaluation.search_depth)}", unsafe_allow_html=True)

        with col2:
            st.markdown(f"**Freshness Required:** {'Yes' if evaluation.requires_freshness else 'No'}")
            st.markdown(f"**Plurality Required:** {'Yes' if evaluation.requires_plurality else 'No'}")
            st.markdown(f"**Species Strict:** {'Yes' if evaluation.species_strict else 'No'}")

        if evaluation.subqueries:
            st.markdown("**Generated Subqueries:**")
            for sq in evaluation.subqueries:
                st.markdown(f"- {sq}")

        if evaluation.suggested_sources:
            st.markdown(f"**Suggested Sources:** `{', '.join(evaluation.suggested_sources)}`")


def render_research_records(vault_root: Path) -> None:
    """Main render function for the Research Records workspace."""
    st.markdown(
        """
        <style>
        .vault-panel {
            background: #1a1d2e;
            border: 1px solid #2d3147;
            border-radius: 8px;
            padding: 16px;
        }
        .vault-panel-label {
            font-size: 11px;
            font-weight: 600;
            color: #8b90a0;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="vault-panel" style="margin-bottom:24px">
          <div class="vault-panel-label">Research OS</div>
          <div style="font-size:20px;font-weight:600;color:#e8eaf0">Research Records</div>
          <div style="font-size:13px;color:#8b90a0;margin-top:8px">
            View research task history with harness loop progress, verification status, and evidence grounding.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Tabs for different views
    tab1, tab2, tab3 = st.tabs(["Records", "Evaluator Demo", "Statistics"])

    with tab1:
        store = get_record_store(vault_root)

        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            disease_filter = st.selectbox(
                "Disease",
                ["All", "CKD", "FIP", "HCM", "IBD", "FCV", "Diabetes", "Obesity", "Cancer"],
                key="record-disease-filter",
            )
        with col2:
            status_filter = st.selectbox(
                "Status",
                ["All", "Passed", "Failed", "Needs Review", "Pending"],
                key="record-status-filter",
            )
        with col3:
            limit = st.number_input("Limit", min_value=5, max_value=100, value=20, key="record-limit")

        # Convert filters
        disease_arg = None if disease_filter == "All" else disease_filter.lower()
        status_map = {
            "Passed": VerifierStatus.PASSED,
            "Failed": VerifierStatus.FAILED,
            "Needs Review": VerifierStatus.NEEDS_HUMAN_REVIEW,
            "Pending": VerifierStatus.PENDING,
        }
        status_arg = status_map.get(status_filter)

        # Fetch and display records
        records = store.list_records(disease=disease_arg, status=status_arg, limit=limit)

        if not records:
            st.info("No research records found. Records are created only after you explicitly save a research run.")
        else:
            st.markdown(f"**{len(records)} records found**")
            for record in records:
                render_record_card(record)

    with tab2:
        render_task_evaluator_demo(vault_root)

    with tab3:
        store = get_record_store(vault_root)
        validated_store = ValidatedClaimStore(vault_root / "system" / "validated-claims")

        st.markdown("### Record Statistics")

        # Count by disease
        diseases = ["ckd", "fip", "hcm", "ibd", "fcv", "diabetes", "obesity", "cancer"]
        disease_counts = {d: store.count(disease=d) for d in diseases}
        total = store.count()

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Records", total)
        with col2:
            st.metric("Diseases Covered", sum(1 for c in disease_counts.values() if c > 0))

        current_validated = validated_store.query_validated_claims(vault_root)
        st.metric("Validated Claims", len(current_validated))

        st.markdown("**Records by Disease:**")
        for disease, count in sorted(disease_counts.items(), key=lambda x: -x[1]):
            if count > 0:
                st.markdown(f"- **{disease.upper()}**: {count}")

        # Recent activity
        recent = store.get_recent(days=7, limit=5)
        if recent:
            st.markdown("**Recent Activity (7 days):**")
            for record in recent:
                timestamp = record.timestamp.strftime("%Y-%m-%d")
                st.markdown(f"- {timestamp}: {record.user_request[:50]}...")
