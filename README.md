# 大模型高效化：阶段性证据与可复现研究框架（POC）

> 研究结论的「可复现证据」与「实验方法」快照，非维护中的产品级项目。

**声明**：证据驱动、主张即代码、报告即发布；门禁与结论可由本框架内脚本与证据复现。「这是我如何得到这些数据的方法，你可以按此复现和审查。」不承诺长期维护。用途：求职作品集 / 技术展示；内容已脱敏。

---

## 版本与当前最优指标（与主仓库 V37–V43 对齐）

本 POC 为证据与 Schema 快照，与主仓库 **HoloForge-CE / ThomasLab Evidence Suite（V37–V43 阶段）** 口径一致。以下为可对外表述的当前最优历史指标。

| 版本 | 角色 | 本阶段最优（可对外表述） |
|------|------|---------------------------|
| **V80** | 运行时显存 | **PASS**（Peak RSS &lt;1024MB，可复现「&lt;1GB 推理」） |
| **V38** | 静态压缩（Static+Align） | **out_cos ≈0.991**（对齐达标），**ratio ≈4.69x**（policy 20x 未达） |
| **V39** | 跨层 Pareto | **~9.6x @ cos_min~0.94** 或 **~5.65x @ cos_min≥0.99**（帕累托已摸清） |
| **V42** | FFN 功能对齐（Holo-Hessian） | TinyLlama **5.88x 且 PPL 下降**（项目内强信号） |
| **V43** | 权重层代理（Seed×CrossBlock×ColdDust） | **cos_min≈0.9999**，ratio≈4.0；证据闭环（S1/S2/S3、Field、PPL 接入） |
| **TNSEC Breakthrough** | 战略突破证据（Field/熵增益） | **go=true**，determinism_delta=0，entropy_gain_ok=true |
| **FFN_SOTA** | FFN 16x@cosine≥0.99 门禁 | 目标 16x@0.99；当前证据攻关进行中 |
| **V36** | Indra-Lite PQ 阶段最优 | 约 **8x @ cosine≈0.958**（证据落盘后可作 hard fact） |

- **V37 门禁总判**：当前为 **NO-GO**（v37 policy 下 FFN_SOTA required 且 fail；v38 policy 下 V38 倍率未达 20x）。
- **未达成**：V38 倍率 20x、FFN_SOTA 16x@cosine≥0.99 仍在攻关；本 POC 不做「已达成」宣称。

---

## 仓库结构

| 路径 | 说明 |
|------|------|
| `README.md` | 本文件 |
| `REPRODUCTION.md` | 复现指南（最小指令集） |
| `LICENSE` | MIT |
| `docs/` | 阶段复盘与收尾说明（脱敏） |
| `evidence/` | 证据示例（脱敏） |
| `schemas/` | 证据 JSON Schema（v43 + breakthrough） |
| `scripts/` | 自检脚本 `validate_evidence.py`；主代码库复现见 `scripts/README.md` |
| `requirements.txt` | 自检依赖（jsonschema） |

---

## 复现与验证

| 方式 | 条件 | 说明 |
|------|------|------|
| **本仓库自检** | 无需主代码库 | `pip install -r requirements.txt` → `python scripts/validate_evidence.py`；校验 evidence 与 schemas 一致（见 REPRODUCTION.md §0） |
| **轻量验证** | 需主代码库 | `run_light_regression.py`，约 30 秒（REPRODUCTION.md §1） |
| **全量证据** | 需主代码库 + 本地 safetensors | 按 REPRODUCTION.md §2 执行证据脚本与门禁 |

`evidence/` 为示例；真实证据由主代码库脚本产出，格式与示例一致。Schema 见 `schemas/`。

---

## 主仓库与复现

- **主仓库**（HoloForge-CE / ThomasLab Evidence Suite，V37–V43）：完整门禁与证据管线（V37 Evidence Suite、run_v43_evidence、run_tnsec_breakthrough_evidence、run_light_regression、Field 预处理、PPL/前向对齐等）；证据刷新与轻量回归见主仓库 `V43_CLOSING_NOTE_CN.md` 与 `run_light_regression.py`。
- **本仓库**：仅提供 Schema、示例证据、复现指南与自检脚本；完整复现需主代码库。

---

## 引用与联系

基于本证据或方法开展研究或衍生工作时，建议注明 **Evidence-Driven LLM Compression Research Framework (POC)**。本仓库为阶段性研究快照，不提供维护承诺。
