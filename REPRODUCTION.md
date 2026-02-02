# 复现指南

从零复现本 POC 结论的最小指令集。环境：Python 3.10+。

**说明**：完整验证与门禁位于主代码库（HoloForge-CE / ThomasLab）；`<REPO_ROOT>` 指主代码库根目录（含 `tools/`、`tests/`、门禁脚本等）。第 1、2 节依赖主代码库；若无法获取，仅能执行第 0 节自检。阅读证据形态可只看 `evidence/` 与 `schemas/`。

---

## 0. 本仓库内自检（无需主代码库或模型）

确认本仓库内证据示例与 Schema 一致。

```bash
# 在本 POC 仓库根目录（LLM-Compression-Evidence-POC）执行
pip install -r requirements.txt
python scripts/validate_evidence.py
```

**预期**：两行 `PASS` 及「全部证据校验通过。」（或 `All evidence validated.`），退出码 0。

---

## 1. 轻量验证（无模型，约 30 秒）

用于确认证据脚本与门禁逻辑可正常退出并产出合法 JSON。

```bash
# 进入完整代码库根目录（含 tests/、tools/）
cd <REPO_ROOT>

# 轻量回归：V43 证据脚本出口 + Field 口径 + model-path-after + field_transform 单元测试
python tools/run_light_regression.py
```

预期：全部用例通过，退出码 0。

---

## 2. 全量证据与门禁（需本地 safetensors）

需准备本地模型目录 `<MODEL_DIR>`（如 7B 级 safetensors）。

```bash
cd <REPO_ROOT>

# 2.1 权重层代理证据（V43）
python tools/run_v43_evidence.py --model-path <MODEL_DIR> --phase all --output _evidence/V43_EVIDENCE_LATEST.json

# 2.2 战略突破证据（Field / 熵增益）
python tools/run_tnsec_breakthrough_evidence.py --model-path <MODEL_DIR> --output assets/TNSEC_BREAKTHROUGH_EVIDENCE.json

# 2.3 门禁（读上述证据，输出 GO/NO-GO 报告）
python _suite/v37_evidence_suite.py --check-only --policy _suite/v37_evidence_policy.json
```

报告落盘：`_evidence/V37_EVIDENCE_SUITE_REPORT.json` 与 `.md`。

---

## 3. 证据含义速查

| 产出 | 含义 |
|------|------|
| **V43_EVIDENCE_LATEST.json** | Seed / CrossBlock / ColdDust；`summary.go`、`ratio_fp16_effective_min`、`cos_min` |
| **TNSEC_BREAKTHROUGH_EVIDENCE.json** | Field、熵增益、determinism；`summary.go`、`determinism_delta`、`entropy_gain_ok` |
| **V37_EVIDENCE_SUITE_REPORT** | 各 Claim pass/fail，门禁总判 NO-GO/GO |

Schema 见 `schemas/`；示例见 `evidence/`。
