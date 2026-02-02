# 收尾说明（脱敏版）

> 当前证据与门禁状态、复现入口、已知缺口。仅作研究快照说明，非产品路线图。

---

## 当前状态

- **证据链路**：权重层代理（S1/S2/S3）、Field 预处理、PPL/前向对齐接入、战略突破证据（Field/熵增益）均已闭环；产出 JSON 与 Schema 见 `evidence/`、`schemas/`。
- **门禁**：统一读证据、Policy JSON、GO/NO-GO；当前总判 **NO-GO**（静态倍率、FFN 对齐等目标未达）。
- **测试**：证据脚本出口、Field 口径、PPL/model-path-after、field_transform 单元测试、门禁回归；轻量回归约 30s 无模型。

---

## 复现入口

- **轻量回归**：`python tools/run_light_regression.py`（见 REPRODUCTION.md）。
- **全量证据**：见 REPRODUCTION.md 第二节（需本地 safetensors）。
- **门禁**：`python _suite/v37_evidence_suite.py --check-only --policy _suite/v37_evidence_policy.json`。

---

## 已知缺口（不宣称已达成）

- 静态倍率 20x 未达；FFN 16x@cosine≥0.99 未达。
- 门禁总判 NO-GO；本 POC 不做「已达成」对外宣称。

以上为阶段性收尾说明，与实验室叙事及未公开资产脱敏。
