#!/usr/bin/env python3
"""
本仓库内自检：用 schemas/ 校验 evidence/ 下 JSON，无需主代码库或模型。
用法：在仓库根目录执行  python scripts/validate_evidence.py
"""
from pathlib import Path
import json
import sys

try:
    import jsonschema
except ImportError:
    print("请先安装依赖: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = REPO_ROOT / "evidence"
SCHEMAS_DIR = REPO_ROOT / "schemas"

# 证据文件 -> Schema 文件
EVIDENCE_SCHEMA_MAP = {
    "v43_evidence_sample.json": "v43_evidence.schema.json",
    "breakthrough_evidence_sample.json": "breakthrough_evidence.schema.json",
}


def main():
    if not EVIDENCE_DIR.is_dir() or not SCHEMAS_DIR.is_dir():
        print("未找到 evidence/ 或 schemas/ 目录，请在仓库根目录执行本脚本。", file=sys.stderr)
        sys.exit(2)

    failed = []
    for evidence_file, schema_file in EVIDENCE_SCHEMA_MAP.items():
        evidence_path = EVIDENCE_DIR / evidence_file
        schema_path = SCHEMAS_DIR / schema_file
        if not evidence_path.exists():
            print(f"跳过（证据文件不存在）: {evidence_file}")
            continue
        if not schema_path.exists():
            print(f"FAIL: 缺少 Schema {schema_file}", file=sys.stderr)
            failed.append(evidence_file)
            continue
        try:
            with open(evidence_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            with open(schema_path, "r", encoding="utf-8") as f:
                schema = json.load(f)
            jsonschema.validate(instance=data, schema=schema)
            print(f"PASS: {evidence_file} <- {schema_file}")
        except jsonschema.ValidationError as e:
            print(f"FAIL: {evidence_file} <- {schema_file}: {e}", file=sys.stderr)
            failed.append(evidence_file)
        except Exception as e:
            print(f"FAIL: {evidence_file} - {e}", file=sys.stderr)
            failed.append(evidence_file)

    if failed:
        sys.exit(1)
    print("全部证据校验通过。")
    print("All evidence validated.")  # 终端编码非 UTF-8 时仍可读
    sys.exit(0)


if __name__ == "__main__":
    main()
