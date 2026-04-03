---
name: lunwen
description: 用于撰写、补写、压缩、仿写、规范化交付中文毕业论文、毕业设计论文、技术报告和课程设计论文。用户提到论文、样文、学校模板、参考文献、摘要、图表、截图、Word 成稿、查重口吻优化，或需要基于真实项目代码生成论文正文时必须使用。本技能内置样文结构学习、样式提取、章节控字、参考文献筛选、Mermaid/PlantUML 图表处理、Chrome MCP 页面截图工作流，以及 doc/docx Word 成稿交付工作流。
---

# Lunwen

## Overview

这个技能用于把“真实项目事实 + 样文/模板 + 文献约束 + 图表截图 + Word 成稿要求”稳定转化为一篇可交付的中文论文。目标不是把论文写厚，而是按样文体量、真实项目能力和版式规则，输出结构完整、字数可控、图表齐全的 `.docx` 成稿。

## Core Flow

### 1. 锁定输入

先确认以下输入并确定优先级：

1. 学校模板
2. 用户上传的往届样文
3. 用户口头要求
4. 技能默认规则

如果模板、样文和默认规则冲突，必须列出冲突项并让用户选择。样式冲突细则见：

- `prompts/intake.md`
- `prompts/style_extractor.md`
- `references/default-style.md`

### 2. 冻结项目事实

先读项目代码和文档，再提炼固定的项目事实底稿。后续各章只能基于这份底稿扩写。

事实提取细则见：

- `prompts/fact_extractor.md`

### 3. 学样文，不只学目录

如果用户提供样文或模板，必须同时分析：

- 结构：目录、页数、字数、图表节奏
- 样式：标题、正文、摘要、关键词、图题表题、参考文献、致谢

对应资源：

- `prompts/sample_analyzer.md`
- `prompts/style_extractor.md`
- `tools/analyze_sample_pdf.py`

### 4. 先定字数，再写作

写正文前必须生成目标章节字数表。默认优先贴近样文体量，不默认写厚。写完一章就统计一次，超出就压缩。

对应资源：

- `prompts/chapter_writer.md`
- `tools/count_chapter_words.py`
- `references/chapter-patterns.md`

### 5. 图表与截图闭环

图表默认要求：

- 系统架构图
- E-R 图
- 关键流程图
- 数据表
- 测试用例表

如果存在 `mermaid` / `plantuml`，优先渲染为真实图片；若无法渲染，再退回源码或占位。

如果存在 Chrome MCP、Playwright 或等效浏览器自动化能力，优先抓真实系统截图替换占位符。

对应资源：

- `tools/render_mermaid.py`
- `tools/extract_screenshot_placeholders.py`

### 6. 参考文献先建池再回填

默认约束：

- 2020 年及以后
- 中文 10-12 篇
- 英文 3-5 篇
- 总数约 15 篇

必须优先真实可核验文献，不确定就不用。

对应资源：

- `prompts/reference_selector.md`
- `tools/build_reference_pool.py`

### 7. DOCX 成稿交付

如果环境具备 `doc` / `docx` 能力，必须生成 `.docx` 成稿，而不是只停留在 Markdown。

默认样式规则：

- 摘要、Abstract、参考文献、致谢标题居中
- 摘要与 Abstract 独立分页
- 一级章节分页开始
- 中文正文宋体
- 英文正文 Times New Roman
- 关键词单独成段，顶格，标签加粗
- 参考文献悬挂缩进

对应资源：

- `prompts/docx_formatter.md`
- `tools/generate_thesis_docx.py`
- `references/default-style.md`

### 8. 最终检查

交付前必须检查：

- 章节完整
- 字数接近样文目标
- 参考文献比例正确
- 图表编号连续
- 是否残留占位符
- `.docx` 是否真实存在

最终检查细则见：

- `prompts/final_checker.md`

## Resource Map

- 项目输入与冲突决策：`prompts/intake.md`
- 样文结构分析：`prompts/sample_analyzer.md`
- 样式提取：`prompts/style_extractor.md`
- 项目事实提取：`prompts/fact_extractor.md`
- 章节写作与控字：`prompts/chapter_writer.md`
- 参考文献筛选：`prompts/reference_selector.md`
- Word 格式化：`prompts/docx_formatter.md`
- 最终检查：`prompts/final_checker.md`

- 默认版式：`references/default-style.md`
- 章节模式：`references/chapter-patterns.md`

- 统计章节字数：`tools/count_chapter_words.py`
- 分析样文 PDF：`tools/analyze_sample_pdf.py`
- 检查参考文献池：`tools/build_reference_pool.py`
- 提取截图占位符：`tools/extract_screenshot_placeholders.py`
- 渲染 Mermaid：`tools/render_mermaid.py`
- 生成 DOCX：`tools/generate_thesis_docx.py`
