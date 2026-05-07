---
id: system-hcm-image-ingest-pilot-20260417
type: system
topic: operating-system
question_type: pilot
language: zh
last_compiled_at: 2026-04-17
verification_status: compiled
decision_grade: provisional
language_qa_status: light_checked
owner: codex
status: active
---

# HCM Image Ingest Pilot, 2026-04-17

这页只回答一个小问题：

`如果先做一轮最小 image ingest pilot，HCM 应该先抓哪几张 source？`

## 类型判断

这件事属于：

`P0 pilot`

不是全量 rollout。

## 最短结论

先抓 5 张：

1. `src-hcm-001`
2. `src-hcm-009`
3. `src-hcm-010`
4. `src-hcm-012`
5. `src-hcm-020`

这 5 张覆盖了：

- 综述 backbone（mechanism overview + clinical staging）
- echo phenotype anchor（echocardiographic criteria）
- biomarker screening boundary（NT-proBNP threshold）
- genotype-severity bridge（MYBPC3 penetrance）
- remodeling / fibrosis mechanism depth（macrophage-driven histopathology）

## Why These Five

### src-hcm-001

[src-hcm-001.md](../../raw/papers/src-hcm-001.md)

为什么先抓：

- broad HCM review backbone（2021）
- mechanism overview schematic 很可能已经把 fibrosis / diastolic dysfunction 逻辑压成稳定图
- 这张 review 是 HCM module 的 framing anchor，对应 CKD 里的 src-ckd-001

### src-hcm-009

[src-hcm-009.md](../../raw/papers/src-hcm-009.md)

为什么先抓：

- echo phenotype anchor（1995，AHA Circulation）
- 46 cats，两维超声特征化 HCM：diffuse vs segmental hypertrophy
- echo 这类图像在 prose 里几乎无法完整表达，图表优先型 source

### src-hcm-010

[src-hcm-010.md](../../raw/papers/src-hcm-010.md)

为什么先抓：

- NT-proBNP screening boundary（2009）
- 44 pmol/L threshold 是一个数值边界
- ROC curve / scatter plot 是这类 biomarker 论文最核心的视觉证据
- 阈值图比 prose 更直接支持后续 query 里的 staging 判断

### src-hcm-012

[src-hcm-012.md](../../raw/papers/src-hcm-012.md)

为什么先抓：

- genotype-severity bridge（2024，MDPI）
- homozygous vs heterozygous MYBPC3 p.A31P 的 penetrance curve 和 survival 数据
- age-related penetrance（no disease up to 1y，highest proportion at 7y+）
  这种时间序列数据非常适合图表压缩

### src-hcm-020

[src-hcm-020.md](../../raw/papers/src-hcm-020.md)

为什么先抓：

- remodeling / fibrosis mechanism depth（2019，Vet Pathology）
- 18 HCM + 18 controls，histopathology panel + macrophage infiltration figure
- Iba1-positive macrophage density 图是当前 HCM module 里最薄的部分

## Pilot Rule

第一轮先不要追求每篇都抓完。

每篇只做：

- `1-3` 张最关键图片
- 回链到 `local_assets`
- 保证命名稳定

可直接照着落盘的目标文件名见：

- [HCM image ingest manifest](hcm-image-ingest-manifest-20260417.md)

## One-Line Summary

这轮 pilot 的目标不是让 HCM 图片层"全部完成"。

而是证明：

`图片可以从外部上下文，进入 source-card 可引用资产层。`

和 CKD / FIP / IBD 相同的结构，相同的 candidate 命名规则，相同的 manifest + checklist 搭配。
