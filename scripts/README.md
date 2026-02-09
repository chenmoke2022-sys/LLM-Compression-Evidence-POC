# 脚本说明

我把这个公开仓库定位为“证据与格式契约快照”：只保留证据样例、Schema 和最小自检脚本。

## 本仓库内自检（无需主代码库）

- **validate_evidence.py**：用 `schemas/` 校验 `evidence/` 下 JSON；依赖 `pip install -r requirements.txt`（在仓库根目录执行）。
- **用法**：在**本仓库根目录**执行 `python scripts/validate_evidence.py`。
- **复现指南**：根目录 **REPRODUCTION.md** §0。

## 主代码库复现脚本（需完整代码库）

以下脚本位于我的完整实验代码库根目录 `<REPO_ROOT>`（本公开仓库不包含其代码）：

- 轻量回归：`<REPO_ROOT>/tools/run_light_regression.py`
- 分阶段代理评估证据：`<REPO_ROOT>/tools/run_v43_evidence.py`
- 可复现性/口径证据：`<REPO_ROOT>/tools/run_tnsec_breakthrough_evidence.py`
- 门禁套件：`<REPO_ROOT>/_suite/v37_evidence_suite.py`

具体命令与顺序见根目录 **REPRODUCTION.md** 第 1、2 节。
