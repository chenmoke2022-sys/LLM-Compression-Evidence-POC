# 脚本说明

本仓库 = **LLM-Compression-Evidence-POC**（证据与 Schema 快照）。

## 本仓库内自检（无需主代码库）

- **validate_evidence.py**：用 `schemas/` 校验 `evidence/` 下 JSON；依赖 `pip install -r requirements.txt`（在仓库根目录执行）。
- **用法**：在**本仓库根目录**执行 `python scripts/validate_evidence.py`。
- **复现指南**：根目录 **REPRODUCTION.md** §0。

## 主代码库复现脚本（需完整代码库）

以下脚本位于主代码库根目录 `<REPO_ROOT>`，本仓库不包含其代码：

- 轻量回归：`<REPO_ROOT>/tools/run_light_regression.py`
- V43 证据：`<REPO_ROOT>/tools/run_v43_evidence.py`
- 战略突破证据：`<REPO_ROOT>/tools/run_tnsec_breakthrough_evidence.py`
- 门禁套件：`<REPO_ROOT>/_suite/v37_evidence_suite.py`

具体命令与顺序见根目录 **REPRODUCTION.md** 第 1、2 节。
