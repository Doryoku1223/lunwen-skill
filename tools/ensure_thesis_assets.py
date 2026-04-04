from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_ITEMS = [
    {
        "id": "architecture",
        "label": "系统总体架构图",
        "kind": "figure",
        "keywords": ["架构图", "总体架构", "系统架构"],
        "template": """```mermaid
flowchart LR
    U[用户] --> W[Web/桌面前端]
    W --> S[业务服务层]
    S --> D[(数据库)]
    S --> F[文件存储/缓存]
```
图 {number} {label}""",
    },
    {
        "id": "er",
        "label": "数据库 E-R 图",
        "kind": "figure",
        "keywords": ["E-R 图", "ER图", "实体关系"],
        "template": """```mermaid
erDiagram
    USER ||--o{{ NOTE : creates
    NOTE ||--o{{ TAG : tagged_with
    USER {{
        int id
        string name
    }}
    NOTE {{
        int id
        string title
    }}
    TAG {{
        int id
        string name
    }}
```
图 {number} {label}""",
    },
    {
        "id": "flow",
        "label": "关键业务流程图",
        "kind": "figure",
        "keywords": ["流程图", "业务流程", "关键流程"],
        "template": """```mermaid
flowchart TD
    A[进入系统] --> B[输入业务参数]
    B --> C[执行核心处理]
    C --> D[保存结果]
    D --> E[反馈执行状态]
```
图 {number} {label}""",
    },
    {
        "id": "data_table",
        "label": "核心数据表设计",
        "kind": "table",
        "keywords": ["数据表", "表结构", "数据库设计"],
        "template": """表 {number} {label}
| 表名 | 说明 | 关键字段 |
| --- | --- | --- |
| user | 用户信息表 | id, username, password |
| note | 业务主表 | id, title, content |
| tag | 分类标签表 | id, name |""",
    },
    {
        "id": "test_table",
        "label": "系统测试用例表",
        "kind": "table",
        "keywords": ["测试用例", "测试表", "功能测试"],
        "template": """表 {number} {label}
| 用例编号 | 测试目标 | 输入/操作 | 预期结果 |
| --- | --- | --- | --- |
| TC-01 | 正常流程 | 输入合法数据并提交 | 系统提示成功 |
| TC-02 | 异常流程 | 输入缺失字段 | 系统给出校验提示 |""",
    },
    {
        "id": "screenshot",
        "label": "核心功能页面截图",
        "kind": "screenshot",
        "keywords": ["此处插入截图", "页面截图", "系统截图"],
        "template": "[此处插入截图：系统首页]\n[此处插入截图：核心功能页面]",
    },
]


FIGURE_RE = re.compile(r"^图\s*(\d+(?:\.\d+)?)", flags=re.M)
TABLE_RE = re.compile(r"^表\s*(\d+(?:\.\d+)?)", flags=re.M)


def next_number(text: str, pattern: re.Pattern[str]) -> str:
    matches = pattern.findall(text)
    if not matches:
        return "1.1"
    last = matches[-1]
    if "." in last:
        major, minor = last.split(".", 1)
        if minor.isdigit():
            return f"{major}.{int(minor) + 1}"
    if last.isdigit():
        return str(int(last) + 1)
    return "1.1"


def analyze_missing_items(text: str) -> list[dict]:
    missing = []
    for item in REQUIRED_ITEMS:
        if any(keyword in text for keyword in item["keywords"]):
            continue
        missing.append(item)
    return missing


def append_templates(text: str, missing: list[dict]) -> str:
    if not missing:
        return text

    figure_number = next_number(text, FIGURE_RE)
    table_number = next_number(text, TABLE_RE)
    blocks = ["", "## 图表与截图补全草稿", ""]

    for item in missing:
        if item["kind"] == "figure":
            blocks.append(item["template"].format(number=figure_number, label=item["label"]))
            major, minor = figure_number.split(".") if "." in figure_number else (figure_number, "0")
            figure_number = f"{major}.{int(minor) + 1}"
        elif item["kind"] == "table":
            blocks.append(item["template"].format(number=table_number, label=item["label"]))
            major, minor = table_number.split(".") if "." in table_number else (table_number, "0")
            table_number = f"{major}.{int(minor) + 1}"
        else:
            blocks.append(item["template"])
        blocks.append("")

    return text.rstrip() + "\n" + "\n".join(blocks)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ensure mandatory figures, tables and screenshots exist in thesis markdown.")
    parser.add_argument("markdown_file", type=Path)
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--in-place", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    text = args.markdown_file.read_text(encoding="utf-8")
    missing = analyze_missing_items(text)

    print(f"MISSING_COUNT\t{len(missing)}")
    for item in missing:
        print(f"MISSING\t{item['id']}\t{item['label']}")

    if args.check_only or not args.in_place or not missing:
        return 2 if missing else 0

    updated = append_templates(text, missing)
    args.markdown_file.write_text(updated, encoding="utf-8")
    print(f"UPDATED\t{args.markdown_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
