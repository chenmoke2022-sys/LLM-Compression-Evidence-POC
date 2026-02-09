# 复现指南

从零复现本作品集仓库结论的最小指令集。环境：Python 3.10+。

**说明**：本仓库只包含“证据样例 + Schema + 自检”。完整的实验脚本与门禁管线位于我的完整实验代码库（未在此公开）；下文用 `<REPO_ROOT>` 指代那份代码库的根目录（含 `tools/`、`tests/`、门禁脚本等）。如果你没有那份代码库，只需要执行第 0 节自检即可理解证据形态与口径。

---

## 0. 本仓库内自检（无需主代码库或模型）

确认本仓库内证据示例与 Schema 一致。

```bash
# 在本 POC 仓库根目录（LLM-Compression-Evidence-POC）执行
pip install -r requirements.txt
python scripts/validate_evidence.py
```

**预期**：两行 `PASS` 及「全部证据校验通过。」（或 `All evidence validated.`），退出码 0。

建议直接打开 `README.md`，里面我把可复核的关键数字（ratio/cosine/determinism_delta/bytes_*）对应到样例文件与字段了。

---

## 1. 轻量验证（无模型，约 30 秒）

用于确认证据脚本与门禁逻辑可正常退出并产出合法 JSON。

```bash
# 进入完整代码库根目录（含 tests/、tools/）
cd <REPO_ROOT>

# 轻量回归：证据脚本出口 + 可逆预处理口径 + model-path-after 透传 + 关键单元测试
python tools/run_light_regression.py
```

预期：全部用例通过，退出码 0。

---

## 2. 全量证据与门禁（需本地 safetensors）

需准备本地模型目录 `<MODEL_DIR>`（如 7B 级 safetensors）。

```bash
cd <REPO_ROOT>

# 2.1 分阶段代理评估证据（权重层/压缩代理指标）
python tools/run_v43_evidence.py --model-path <MODEL_DIR> --phase all --output _evidence/WEIGHT_PROXY_EVIDENCE.json

# 2.2 稳定性/可复现性证据（预处理 + 熵/字节口径 + determinism）
python tools/run_tnsec_breakthrough_evidence.py --model-path <MODEL_DIR> --output assets/REPRODUCIBILITY_EVIDENCE.json

# 2.3 门禁（读取证据并输出 GO/NO-GO 报告）
python _suite/v37_evidence_suite.py --check-only --policy _suite/v37_evidence_policy.json
```

报告落盘：`_evidence/V37_EVIDENCE_SUITE_REPORT.json` 与 `.md`。

---

## 3. 证据含义速查

| 产出 | 含义 |
|------|------|
| **WEIGHT_PROXY_EVIDENCE.json** | 分阶段代理评估；关注 `summary.go`、`ratio_fp16_effective_min`、`cos_min`、`bytes_*` |
| **REPRODUCIBILITY_EVIDENCE.json** | 可复现性/口径；关注 `summary.go`、`determinism_delta`、`entropy_gain_ok`、`bytes_*` |
| **EVIDENCE_SUITE_REPORT** | 各项检查 pass/fail 与门禁总判 NO-GO/GO |

Schema 见 `schemas/`；示例见 `evidence/`。
