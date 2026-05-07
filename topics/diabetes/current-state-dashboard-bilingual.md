---
id: topic-diabetes-current-state-dashboard-bilingual
type: topic
topic: diabetes
species: feline
disease: diabetes mellitus
question_type: overview
source_ids: [src-diabetes-001, src-diabetes-002, src-diabetes-003, src-diabetes-004, src-diabetes-005, src-diabetes-006, src-diabetes-007, src-diabetes-008, src-diabetes-009, src-diabetes-010, src-diabetes-011, src-diabetes-012, src-diabetes-013, src-diabetes-014, src-diabetes-015, src-diabetes-016, src-diabetes-017, src-diabetes-018, src-diabetes-019, src-diabetes-020, src-diabetes-021, src-diabetes-022, src-diabetes-023, src-diabetes-024, src-reg-010, src-reg-011, src-reg-012, src-reg-013]
language: bilingual
last_compiled_at: 2026-04-24
confidence: low
verification_status: compiled
decision_grade: no
language_qa_status: bilingual_checked
language_qa_notes: "Derived from current-state-dashboard.md as the first high-reuse bilingual Diabetes compiled page. Translation preserves the same compiled and non-decision-grade boundaries after the 2026-04-24 paper-card verification sync."
owner: codex
status: active
---

# Feline Diabetes Current State Dashboard, Bilingual

This page is a high-reuse bilingual derivative of [current state dashboard](current-state-dashboard.md). It does not add new source claims.

本页是 [current state dashboard](current-state-dashboard.md) 的高复用双语派生页，不新增 source claim。

## Quick Helpers / 快速入口

- if you want to trace a claim back down:
  [verify a claim](../../system/indexes/verify-a-claim.md)
- if you want the detailed one-language dashboard:
  [current state dashboard](current-state-dashboard.md)
- if you want the branch-level synthesis:
  [synthesis index](synthesis-index.md)
- if you want treatment routing:
  [treatment branch map](treatment-branch-map.md)
- if you want SGLT2 label boundaries:
  [SGLT2 label control](sglt2-label-control.md)

## Top Questions / 高频问题入口

If your real question is one of these, go straight there:

- `What is the current diabetes disease model? / 当前糖尿病 disease model 应该怎么读？`
  Open: [mechanism overview](mechanism-overview.md)
- `How should diagnosis, monitoring, and treatment candidacy be routed? / 诊断、监测和治疗候选门槛应该怎样路由？`
  Open: [diagnostic and monitoring workup](diagnostic-monitoring-workup.md)
- `Can remission claims be ranked by diet or insulin protocol? / remission 能不能按饮食或胰岛素方案排序？`
  Open: [remission boundaries](remission-boundaries.md)
- `How should SGLT2 products be bounded? / SGLT2 产品分支应该怎样设边界？`
  Open: [SGLT2 label control](sglt2-label-control.md)
- `Which Diabetes claims should I verify back in the papers? / 哪些 Diabetes 结论应该回原文核查？`
  Open: [verify a claim](../../system/indexes/verify-a-claim.md)

## Current Status / 当前状态

### Usable Now / 现在可用

**EN**
- Diabetes is now the fifth 24-source disease module in the vault.
- All 24 paper source cards are explicit `extraction_depth: full`.
- All 24 paper sources have round-1 worksheets.
- Four U.S. SGLT2 regulatory / label source cards exist for Bexacat and Senvelgo.
- The first briefing, dossier, and slides output sets exist across `working-en / en / zh`.
- Ten memo-derived topic pages now expose diagnostic/workup, diet, remission, treatment, obesity/body-condition, endocrine-secondary disease, pancreatitis, neuropathy, epidemiology/breed risk, and SGLT2 label-control branches.
- The first verified Diabetes image asset is linked from `src-diabetes-023`.

**ZH**
- Diabetes 现在已经是 vault 中第五个 24-source disease module。
- 24 张 paper source card 全部都有明确的 `extraction_depth: full`。
- 24 篇 paper source 都已有 round-1 worksheet。
- Bexacat 与 Senvelgo 现在已有 4 张美国 SGLT2 regulatory / label source card。
- 第一组 briefing、dossier 和 slides output 已经覆盖 `working-en / en / zh`。
- 10 个由 memo 派生的 topic page 已经覆盖 diagnostic/workup、diet、remission、treatment、obesity/body-condition、endocrine-secondary disease、pancreatitis、neuropathy、epidemiology/breed risk 和 SGLT2 label-control 分支。
- 第一张 verified Diabetes image asset 已经从 `src-diabetes-023` 链接进来。

### Evidence-Depth Boundary / 证据深度边界

**EN**
- The module is output-capable but not decision-grade or output-compression mature.
- All `24/24` Diabetes paper cards are now `verification_status: deep_extracted`.
- The remaining gap is not paper-card depth rescue, but stronger topic/output-level compression for treatment ranking, remission-rate tables, diet sequencing, insulin protocol comparison, and product recommendation boundaries.
- Strong treatment ranking, remission-rate tables, diet sequencing, insulin protocol comparison, and product recommendation still require tighter topic/output compression and, where necessary, official-label precision.

**ZH**
- 这个模块已经具备 output 能力，但还不是 decision-grade 或 output-compression mature。
- `24/24` Diabetes paper card 现在都已经是 `verification_status: deep_extracted`。
- 剩余缺口不再是 paper-card depth rescue，而是治疗排序、remission rate 表、diet sequencing、insulin protocol comparison 和产品推荐边界所需的更强 topic/output-level compression。
- 强治疗排序、remission rate 表、diet sequencing、insulin protocol comparison 和产品推荐仍需要更紧的 topic/output 压缩，并在必要时补 official-label precision。

## Strongest Branches / 当前最强分支

| Branch | EN read | ZH read | Lead sources |
|---|---|---|---|
| Pathogenesis | insulin resistance plus inadequate insulin secretion, with species-specific framing | 胰岛素抵抗加胰岛素分泌不足，并保留猫种属特异性 | `src-diabetes-001`, `src-diabetes-002`, `src-diabetes-019` |
| Obesity / diet | obesity, carbohydrate, fiber, protein, and body-condition state must stay separated | obesity、carbohydrate、fiber、protein 和 body-condition state 不能混成一个饮食结论 | `src-diabetes-005`, `src-diabetes-006`, `src-diabetes-015`, `src-diabetes-016`, `src-diabetes-022` |
| Remission | real endpoint, but no single predictor or protocol controls the branch | remission 是真实 endpoint，但不能由单一 predictor 或 protocol 控制 | `src-diabetes-007`, `src-diabetes-015`, `src-diabetes-024` |
| Secondary endocrine disease | type-2-like disease is the default frame, not the universal explanation | type-2-like 是默认框架，不是所有病例的唯一解释 | `src-diabetes-013`, `src-diabetes-020` |
| Pancreatitis / DKA complexity | bidirectional comorbidity and complexity gate | 双向 comorbidity 与复杂性门槛 | `src-diabetes-010`, `src-diabetes-023` |
| Treatment | branch map, not treatment leaderboard | 治疗分支图，不是治疗排行榜 | `src-diabetes-008`, `src-diabetes-011`, `src-diabetes-017`, `src-diabetes-024` |
| SGLT2 label control | U.S. primary-source branch with candidate and safety gates | 有美国 primary source 支撑，但受 candidate selection 与安全门槛控制 | `src-reg-010`, `src-reg-011`, `src-reg-012`, `src-reg-013` |
| Breed risk | Burmese risk signal is durable but denominator-bound | Burmese 风险信号稳定出现，但必须绑定 denominator | `src-diabetes-009`, `src-diabetes-012` |
| Complications | neuropathy and microvascular pathology are complication / endpoint branches | neuropathy 与 microvascular pathology 是 complication / endpoint 分支 | `src-diabetes-004`, `src-diabetes-018` |

## Boundary Tensions / 边界张力

Use [conflict register](../../system/indexes/conflict-register.md) for the full system owner.

详见 [conflict register](../../system/indexes/conflict-register.md)。

**EN**
- Do not flatten feline diabetes into only a type-2-like story; secondary endocrine disease and pancreatitis can change routing.
- Do not turn remission signals into a universal protocol promise.
- Do not treat SGLT2 oral route or FDA approval as superiority over insulin / diet branches.
- Do not turn obesity into immediate weight-loss instruction without current body-condition and stabilization context.
- Do not generalize Burmese risk magnitude outside the source population denominator.

**ZH**
- 不要把 feline diabetes 压成单一 type-2-like 故事；secondary endocrine disease 和 pancreatitis 可能改变路由。
- 不要把 remission 信号改写成通用 protocol 承诺。
- 不要把 SGLT2 口服路径或 FDA approval 直接当成优于 insulin / diet 分支。
- 不要在没有当前 body-condition 与 stabilization context 时，把 obesity 改写成即时减重指令。
- 不要脱离 source population denominator 泛化 Burmese 风险幅度。

## Best Entry Pages / 最佳入口页

| Area | Main Page | State | Notes |
|---|---|---|---|
| Dashboard | [current state dashboard](current-state-dashboard.md) | usable | fastest one-language overview |
| Dashboard bilingual | [current state dashboard bilingual](current-state-dashboard-bilingual.md) | usable | fastest cross-language overview |
| Synthesis | [synthesis index](synthesis-index.md) | usable | best branch-level compiled overview |
| Mechanism | [mechanism overview](mechanism-overview.md) | usable | disease model and mechanism spine |
| Workup | [diagnostic and monitoring workup](diagnostic-monitoring-workup.md) | usable | recognition, monitoring, and treatment-candidacy routing |
| Treatment map | [treatment branch map](treatment-branch-map.md) | usable | branch separation without treatment ranking |
| Remission | [remission boundaries](remission-boundaries.md) | usable | endpoint / evidence-quality boundary |
| Diet | [diet architecture](diet-architecture.md) | usable | carbohydrate, fiber, protein, stage, and endpoint separation |
| Obesity | [obesity and body condition](obesity-and-body-condition.md) | usable | mechanism, recognition, endpoint, and sequencing branch |
| Endocrine-secondary | [endocrine secondary diabetes](endocrine-secondary-diabetes.md) | usable | hypersomatotropism / acromegaly gate |
| SGLT2 label control | [SGLT2 label control](sglt2-label-control.md) | usable | U.S. label and safety boundaries |
| Output matrix | [Diabetes output language matrix](../../system/indexes/diabetes-output-language-matrix.md) | usable | fastest page for output and language state |

## Recommended Next Moves / 推荐下一步

**EN**
1. Keep bilingual rollout narrow: dashboard first, then synthesis only if reuse pressure stays real.
2. Use full-text review only where it changes remission, diet/obesity sequencing, insulin protocol, or SGLT2 safety boundaries.
3. Add non-U.S. regulatory checks only when jurisdiction comparison becomes necessary.
4. Keep treatment pages as branch maps, not product or protocol rankings.

**ZH**
1. 双语 rollout 继续保持窄范围：先做 dashboard；只有复用压力继续明确时再做 synthesis。
2. 只有当 full-text review 会改变 remission、diet/obesity sequencing、insulin protocol 或 SGLT2 safety boundary 时才继续加深。
3. 只有需要 jurisdiction comparison 时才补 non-U.S. regulatory check。
4. 治疗页继续保持 branch map，不做产品或 protocol 排名。

## Footer / 页脚

This bilingual derivative preserves the same source ids and evidence boundaries as [current state dashboard](current-state-dashboard.md). Translation does not imply stronger evidence than the original.

本双语派生页保留与 [current state dashboard](current-state-dashboard.md) 相同的 source ids 和证据边界。翻译不代表证据强度高于原页面。
