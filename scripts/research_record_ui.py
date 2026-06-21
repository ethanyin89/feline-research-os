"""
Research Record UI for Streamlit.

Displays research records with harness loop visualization,
verification status, and evidence grounding details.
"""

import html
import json
import re
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
    PromotionManifest,
    build_promotion_draft,
    extract_claim_candidates,
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


def is_zh_session() -> bool:
    """Check if the current session leans towards Chinese."""
    try:
        if st.session_state.get("pending_question") and bool(re.search(r"[\u3400-\u9fff]", st.session_state.pending_question)):
            return True
        messages = st.session_state.get("messages", [])
        for msg in reversed(messages):
            if msg.get("role") == "user" and bool(re.search(r"[\u3400-\u9fff]", msg.get("content", ""))):
                return True
    except Exception:
        pass
    return False


def render_claim_promotion_panel(record: ResearchRecord, vault_root: Path) -> None:
    """Render claim selection, validation and promotion panel (Gate 6B & 6C)."""
    is_zh = is_zh_session()
    
    # 1. Existing Promotions for this record
    validated_store = ValidatedClaimStore(vault_root / "system" / "validated-claims")
    existing_manifests = []
    if validated_store.manifest_path.exists():
        for path in validated_store.manifest_path.glob("*.json"):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                if data.get("record_id") == record.record_id:
                    existing_manifests.append(data)
            except Exception:
                continue
                
    if existing_manifests:
        header_text = "### Existing Promotions / 已存在晋升" if is_zh else "### Existing Promotions"
        st.markdown(header_text)
        for manifest in existing_manifests:
            claims_count = len(manifest.get("claim_ids", []))
            target = manifest.get("target_page")
            manifest_id = manifest.get("manifest_id")
            validated_at = manifest.get("validated_at", "")[:16].replace("T", " ")
            
            st.markdown(
                f"""
                <div style="background:#10b98111; border:1px solid #10b98133; border-radius:6px; padding:10px; margin-bottom:12px; font-size:13px">
                  <div style="font-weight:bold; color:#10b981">✓ Promoted to {target}</div>
                  <div style="color:#8b90a0; margin-top:4px">
                    Manifest: <code>{manifest_id}</code> | Time: {validated_at} | Claims: {claims_count}
                  </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    # 2. Extract Candidate Claims
    candidates = extract_claim_candidates(record)
    if not candidates:
        msg = (
            "No candidate claims found in this record. Ensure the final answer contains tags like `[quoted_fact: ...]` or `[source_supported_conclusion: ...]`. / "
            "此记录中未找到候选 claim。请确保最终回答包含 `[quoted_fact: ...]` 或 `[source_supported_conclusion: ...]` 等标签。"
        )
        st.info(msg)
        return
        
    st.markdown("---")
    title_text = "### Claim Selection & Promotion / 声明选择与晋升" if is_zh else "### Claim Selection & Promotion"
    st.markdown(title_text)
    
    # 3. Target Page Configuration
    disease_name = record.disease if record.disease else "general"
    default_target = f"topics/{disease_name}/validated-claims.md"
    
    target_lbl = "Target Page / 目标页面" if is_zh else "Target Page"
    target_help = "Vault-relative path, e.g. topics/ckd/validated-claims.md or topics/ckd/model-map-bilingual.md" if is_zh else "Vault-relative path, e.g. topics/ckd/validated-claims.md"
    
    # We allow the user to select from suggestions or type custom path
    st.caption("Common Targets / 常见目标页面:")
    
    col_a, col_b, col_c = st.columns(3)
    record_id = record.record_id
    tgt_key_record_id = f"target_page_{record_id}"
    if tgt_key_record_id not in st.session_state:
        st.session_state[tgt_key_record_id] = default_target
        
    with col_a:
        if st.button("Validated Claims", key=f"btn_tgt_vc_{record_id}", use_container_width=True):
            st.session_state[tgt_key_record_id] = f"topics/{disease_name}/validated-claims.md"
            st.rerun()
    with col_b:
        if st.button("Model Map (Bilingual)", key=f"btn_tgt_mm_{record_id}", use_container_width=True):
            st.session_state[tgt_key_record_id] = f"topics/{disease_name}/model-map-bilingual.md"
            st.rerun()
    with col_c:
        if st.button("Early Detection", key=f"btn_tgt_ed_{record_id}", use_container_width=True):
            st.session_state[tgt_key_record_id] = f"topics/{disease_name}/early-detection-bilingual.md"
            st.rerun()
            
    target_page = st.text_input(
        target_lbl,
        value=st.session_state[tgt_key_record_id],
        key=tgt_key_record_id,
        help=target_help
    )
    
    # 4. Checkbox lists for claim candidate selection
    selected_claim_ids = []
    select_lbl = "Select claims to promote / 选择要晋升的声明:" if is_zh else "Select claims to promote:"
    st.markdown(f"**{select_lbl}**")
    
    for claim in candidates:
        cols = st.columns([0.05, 0.95])
        with cols[0]:
            # By default, check quoted_fact or source_supported_conclusion
            chk_default = (claim.provenance != "llm_inference")
            is_selected = st.checkbox(
                "",
                value=chk_default,
                key=f"chk_{record.record_id}_{claim.claim_id}"
            )
        with cols[1]:
            if claim.provenance == "quoted_fact":
                claim_color = "#10b981"
                claim_label = "Quoted Fact / 引用事实"
            elif claim.provenance == "source_supported_conclusion":
                claim_color = "#3b82f6"
                claim_label = "Source Supported Conclusion / 来源支持的结论"
            else:
                claim_color = "#ef4444"
                claim_label = "LLM Inference / LLM 推论 (Blocked)"
                
            sources_str = ", ".join(claim.source_ids) if claim.source_ids else ("None" if not is_zh else "无")
            badge_html = f'<span style="background:{claim_color}22;color:{claim_color};padding:2px 6px;border-radius:4px;font-size:11px;font-weight:bold;margin-right:8px">{claim_label}</span>'
            sources_html = f'<span style="color:#8b90a0;font-size:12px;margin-left:8px">(Sources: {sources_str})</span>'
            st.markdown(f"{badge_html} <code>{claim.claim_id}</code> {sources_html}", unsafe_allow_html=True)
            st.markdown(f'<div style="color:#e8eaf0;font-size:14px;margin-top:4px;margin-bottom:12px;padding-left:4px;line-height:1.4">{claim.text}</div>', unsafe_allow_html=True)
            
        if is_selected:
            selected_claim_ids.append(claim.claim_id)
            
    # 5. On-the-fly Promotion Validation
    draft = build_promotion_draft(
        record=record,
        selected_claim_ids=selected_claim_ids,
        target_page=target_page,
    )
    
    # 6. Display Validation results
    val_header = "#### Validation Results / 验证结果" if is_zh else "#### Validation Results"
    st.markdown(val_header)
    
    for result in draft.validation_results:
        if result.passed:
            icon = "🟢"
            color = "#10b981"
        else:
            if result.severity in ("critical", "high"):
                icon = "🔴"
                color = "#ef4444"
            else:
                icon = "🟡"
                color = "#f59e0b"
                
        st.markdown(
            f'<div style="display:flex;align-items:flex-start;gap:8px;margin-bottom:6px;font-size:13px">'
            f'<span>{icon}</span>'
            f'<div style="flex:1">'
            f'<b style="color:{color};margin-right:8px">{result.check_name}</b>'
            f'<span style="color:#e8eaf0">{result.message}</span>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )
        
    # 7. Action Button
    st.markdown("<div style='margin-top:16px'></div>", unsafe_allow_html=True)
    if draft.ready_for_patch:
        success_msg = "Draft is validated and ready for promotion. / 草案已通过验证，可以晋升。" if is_zh else "Draft is validated and ready for promotion."
        st.success(success_msg)
        
        btn_label = "Confirm Promotion & Write to Vault / 确认晋升并写入库" if is_zh else "Confirm Promotion & Write to Vault"
        record_id = record.record_id
        if st.button(btn_label, key=f"btn_promote_{record_id}", type="primary", use_container_width=True):
            try:
                res = validated_store.promote_draft(draft, vault_root)
                manifest_id = res['manifest'].manifest_id
                claims_count = len(res['claims'])
                
                success_toast = f"Successfully promoted {claims_count} claims! / 成功晋升 {claims_count} 条声明！" if is_zh else f"Successfully promoted {claims_count} claims!"
                st.success(success_toast)
                st.toast(success_toast)
                st.rerun()
            except Exception as e:
                err_msg = f"Promotion failed: {str(e)} / 晋升失败: {str(e)}" if is_zh else f"Promotion failed: {str(e)}"
                st.error(err_msg)
    else:
        blocked_msg = "Promotion blocked. Resolve FAILED (🔴) validations to enable. / 晋升已阻止。请解决上述所有失败（🔴）验证。" if is_zh else "Promotion blocked. Resolve FAILED validations to enable."
        st.warning(blocked_msg)


def render_record_card(record: ResearchRecord, vault_root: Path) -> None:
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

        # Claim selection and promotion panel
        render_claim_promotion_panel(record, vault_root)


def render_task_evaluator_demo(vault_root: Path) -> None:
    """Interactive demo of the task evaluator."""
    st.markdown("### Query Evaluator Demo")
    st.caption("Test how queries are classified and routed")

    evaluator = TaskEvaluator()

    record_id_demo = "evaluator"
    demo_query = st.text_input(
        "Test query",
        placeholder="e.g., 猫CKD的终点指标有哪些？",
        key=f"evaluator-demo-query-{record_id_demo}",
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
            record_id_filter = "filter"
            disease_filter = st.selectbox(
                "Disease",
                ["All", "CKD", "FIP", "HCM", "IBD", "FCV", "Diabetes", "Obesity", "Cancer"],
                key=f"record-disease-filter-{record_id_filter}",
            )
        with col2:
            status_filter = st.selectbox(
                "Status",
                ["All", "Passed", "Failed", "Needs Review", "Pending"],
                key=f"record-status-filter-{record_id_filter}",
            )
        with col3:
            limit = st.number_input("Limit", min_value=5, max_value=100, value=20, key=f"record-limit-{record_id_filter}")

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
                render_record_card(record, vault_root)

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
