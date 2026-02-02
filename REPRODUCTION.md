# 复现指南

以下为从零复现本 POC 结论的最小指令集。环境：Python 3.10+。

**说明**：完整验证脚本与门禁入口位于主代码库；此处 `<REPO_ROOT>` 指代该代码库根目录（含 `tools/`、`tests/`、门禁脚本等）。若仅阅读本 POC 包，可只查看 `evidence/` 与 `schemas/` 理解证据形态。

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

- **V43_EVIDENCE_LATEST.json**：Seed / CrossBlock / ColdDust 三阶段指标；`summary.go`、`summary.ratio_fp16_effective_min`、`summary.cos_min`。
- **TNSEC_BREAKTHROUGH_EVIDENCE.json**：Field、熵增益、determinism；`summary.go`、`summary.determinism_delta`、`summary.entropy_gain_ok`。
- **V37_EVIDENCE_SUITE_REPORT**：各 Claim 的 pass/fail 与门禁总判 NO-GO/GO。

Schema 见 `schemas/`；示例见 `evidence/`。
