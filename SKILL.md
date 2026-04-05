---
name: lunwen
description: 用于撰写、补写、压缩、仿写、规范化交付中文毕业论文、毕业设计论文、技术报告和课程设计论文。用户提到论文、样文、学校模板、参考文献、摘要、图表、截图、Word 成稿、查重口吻优化，或需要基于真实项目代码生成论文正文时必须使用。本技能内置样文结构学习、样式提取、章节控字、参考文献筛选、Mermaid/PlantUML 图表处理、Chrome MCP 页面截图工作流，以及 doc/docx Word 成稿交付工作流。
---

# Lunwen

## Overview

这个技能用于把“真实项目事实 + 样文/模板 + 文献约束 + 图表截图 + Word 成稿要求”稳定转化为一篇可交付的中文论文。目标不是把论文写厚，而是按样文体量、真实项目能力和版式规则，输出结构完整、字数可控、图表齐全的 `.docx` 成稿。

## Hard Gates

以下规则是硬约束：

1. 用户第一次说“为项目生成论文”时，必须先索要辅助资料，至少包括：
   - 学校模板
   - 往届样文
   - 开题报告 / 任务书
   - 封面字段要求
   - 字数要求
2. 在用户明确表示“没有更多资料”或已经给出可分析资料之前，禁止直接生成论文初稿。
3. 如果用户给了样文或模板，必须先分析样文与样式，先回传“建议目录 + 目标字数 + 样式摘要 + 冲突项”，等待用户确认后才能开写正文。
4. 输出文件名必须使用论文标题，不得使用 `smart-lab-thesis`、`final`、`draft` 这类通用名。
5. 除主论文 `.docx` 外，必须额外交付一个“附件 `.docx`”，用于收录正文中的 Mermaid / PlantUML 图源码、数据库 E-R 图源码、关键流程图源码等不渲染版本。
6. 第 4 章“系统详细设计与实现”必须是全文最长章节；每个一级功能模块默认都要包含：
   - 模块说明
   - 页面截图
   - 简要核心代码或关键实现片段
7. 如果正文数据库设计部分缺少 E-R 图，则视为未完成。
8. 如果用户给了任务书 / 开题报告 / 学校模板 / 样文，必须先分析这些材料，禁止绕过分析直接生成正文。
9. 如果任务书、样文、README、旧说明文档和源码之间出现冲突，默认以“学校模板 > 任务书/开题报告 > 用户明确要求 > 样文 > 项目源码 > README > 旧说明文档”为优先级。
10. 旧部署说明、历史项目介绍、演示文档默认视为低可信来源；除非用户明确要求，否则不能作为论文事实主依据。

## Execution States

本技能默认按以下状态机执行：

1. `intake_only`
   只收资料，不写正文。
2. `sample_analysis_done`
   已完成样文 / 模板 / 任务书分析，但未开写。
3. `outline_confirmed`
   用户已确认目录、字数和样式方案。
4. `writing_allowed`
   允许开始正文写作。
5. `delivery_done`
   已生成主论文、附件和校验产物。

状态约束：

- 未进入 `outline_confirmed` 前，禁止写正文。
- 若用户中途补交新模板、新样文、新任务书，状态必须退回 `sample_analysis_done`。
- 只有进入 `writing_allowed` 后，才允许生成主论文 `.md` / `.docx`。

## Core Flow

### 1. 锁定输入

先确认以下输入并确定优先级：

1. 学校模板
2. 任务书 / 开题报告
3. 用户上传的往届样文
4. 用户口头要求
5. 项目源码
6. README
7. 旧项目说明文档
8. 技能默认规则

首次响应论文请求时，必须主动告诉用户可以直接提供模板、历届样文、开题报告、任务书或封面要求的本地路径，示例格式如：

- `D:\论文模板.docx`
- `D:\论文样文1.docx`
- `D:\开题报告.pdf`

并且必须明确说明：

- 如果用户还没提供样文、模板或任务书，当前阶段只收集资料和分析，不直接开写初稿。
- 如果用户确认“没有更多资料”，才能按项目源码和默认规则继续。

如果模板、样文和默认规则冲突，必须列出冲突项并让用户选择。样式冲突细则见：

- `prompts/intake.md`
- `prompts/style_extractor.md`
- `references/default-style.md`

### 2. 冻结项目事实

先读项目代码和文档，再提炼固定的项目事实底稿。后续各章只能基于这份底稿扩写。

冻结事实时，必须明确区分：

1. 任务书要求
2. 源码实际实现
3. 论文最终采用口径

如果三者不一致，必须在设计回传阶段提前告诉用户，不得等正文写完后再修正。

事实提取细则见：

- `prompts/fact_extractor.md`

### 3. 学样文，不只学目录

如果用户提供样文或模板，必须同时分析：

- 结构：目录、页数、字数、图表节奏
- 样式：标题、正文、摘要、关键词、图题表题、参考文献、致谢
- 细节：中英文正文的字体字号、段前段后、行距、首行缩进
- 标题：一级、二级、三级标题的字体字号、加粗、对齐、分页方式
- 表图代码：图题、表题、表格内容、代码块或代码截图的插入位置与样式

对应资源：

- `prompts/sample_analyzer.md`
- `prompts/style_extractor.md`
- `tools/analyze_sample_pdf.py`
- `tools/analyze_docx.py`

### 3.5 先回传设计，再开写

模板和样文分析结束后，必须先把以下内容回传给用户确认：

1. 当前论文建议目录
2. 各章目标字数
3. 正文、标题、摘要、关键词、图题、表题、表格内容等版式样式
4. 与默认规则的冲突项

回传时，默认必须结构化为 4 张表：

1. 输入资料表
2. 建议目录表
3. 字数预算表
4. 样式与冲突表

必须明确等待用户确认目录和样式；若用户提出新的修改意见，以用户最后确认的版本为准，再进入正文写作。

如果用户后续又补充了新样文、模板或任务书，必须中断正文写作流程，回到本步骤重新分析，不得沿用旧设计继续写。

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

E-R 图规则：

- 如果数据库总表 E-R 图过大，必须拆分为至少两张：
  1. 总表设计图
  2. 核心表设计图
- 若业务复杂，可继续拆成“权限与用户域”“预约与改派域”“设备与报修域”“耗材域”等多张图
- 正文中至少保留“总表设计图 + 核心表设计图”两张 E-R 图

截图默认要求：

- 第 4 章每个主要模块至少 1 张页面截图
- 如果模块跨“管理端 / 用户端”，优先两端都给截图
- 截图标题必须与正文模块对应，不得只放“系统页面图”这类空泛标题

代码默认要求：

- 第 4 章每个主要模块至少给出 1 段简要核心代码、SQL 片段或关键实现片段
- 代码以“解释业务规则”为目的，不堆大段源码
- 大段源码放附录，不直接塞正文

第 3 章设计图最低要求：

- 系统总体架构图
- 功能模块结构图
- 权限控制流程图
- 关键业务流程图
- E-R 图

第 4 章截图最低要求：

- 每个主模块至少 1 张截图
- 主模块跨多角色时，优先补多角色截图
- 截图总数不足 6 张时，默认视为实现章节不充分

如果存在 `mermaid` / `plantuml`，优先渲染为真实图片；若无法渲染，再退回源码或占位。

仓库内置 Playwright 截图链路。默认先用本仓库脚本自动抓取系统页面，不再要求用户额外安装浏览器 skill。

如果宿主环境提供 Chrome CDP / Chrome MCP 连接地址，可以作为增强路径复用当前浏览器会话；否则默认由仓库自举 Playwright Chromium。

对应资源：

- `tools/render_mermaid.py`
- `tools/ensure_thesis_assets.py`
- `tools/extract_screenshot_placeholders.py`
- `tools/build_screenshot_plan.py`
- `tools/capture_thesis_screenshots.py`

### 6. 参考文献先建池再回填

默认约束：

- 2020 年及以后
- 中文 10-12 篇
- 英文 3-5 篇
- 总数约 15 篇

必须优先真实可核验文献，不确定就不用。

文献工作流必须分 5 步执行：

1. 建候选池
2. 做真实性核验
3. 做相关性筛选
4. 格式化参考文献
5. 生成文献核验清单

默认文献质量规则：

- 中文优先使用 CNKI / 万方 / 维普中可核验的北大核心、CSCD 等来源
- 英文优先使用 IEEE、Elsevier、Springer、ACM、MDPI 等可核验 DOI 来源
- 优先近五年文献
- 优先被引较高文献
- 不确定真实性的条目直接丢弃，不写“猜测型引用”

文献交付产物默认至少包括：

- 正文参考文献列表
- `references-verified.json` 文献核验清单

文献核验清单默认字段：

- title
- authors
- year
- source
- doi_or_url
- citation_count_if_available
- relevance_note
- status

对应资源：

- `prompts/reference_selector.md`
- `tools/build_reference_pool.py`

### 7. DOCX 成稿交付

如果环境具备 `doc` / `docx` 能力，必须生成 `.docx` 成稿，而不是只停留在 Markdown。

交付物必须至少包括：

1. 主论文 `.md`
2. 主论文 `.docx`
3. 图像映射文件
4. 附件 `.docx`

文件名规则：

- 主论文文件名必须使用论文标题，如 `智慧实验室管理系统的设计与实现.docx`
- 附件文件名必须使用论文标题加“附件”，如 `智慧实验室管理系统的设计与实现-附件.docx`
- 禁止使用 `smart-lab-thesis`、`paper-final`、`doc1` 等通用名

派生文件也应统一命名：

- `论文标题.md`
- `论文标题.docx`
- `论文标题-附件.docx`
- `论文标题-image-map.json`
- `论文标题-文献核验清单.json`

附件 `.docx` 默认内容：

- 正文中的 Mermaid / PlantUML 源码
- 数据库 E-R 图源码
- 关键流程图源码
- 必要时补充核心 SQL / 接口结构说明

默认样式规则：

- 摘要、Abstract、参考文献、致谢标题居中
- 摘要与 Abstract 独立分页
- 一级章节分页开始
- 中文正文宋体
- 英文正文 Times New Roman
- 中文关键词单独成段，顶格，“关键词：”标签使用黑体小四加粗，内容使用宋体小四
- 中英文摘要正文除关键词行外，默认首行缩进 2 字符
- 英文摘要正文使用 Times New Roman 小四
- 英文关键词单独成段，顶格，不首行缩进，使用 Times New Roman 小四
- 参考文献悬挂缩进

对应资源：

- `prompts/docx_formatter.md`
- `tools/generate_thesis_docx.py`
- `tools/analyze_docx.py`
- `references/default-style.md`

### 8. 最终检查

交付前必须检查：

- 章节完整
- 字数接近样文目标
- 参考文献比例正确
- 图表编号连续
- 是否残留占位符
- `.docx` 是否真实存在
- 主论文文件名是否为论文标题
- 附件 `.docx` 是否真实存在
- 第 4 章是否为全文最长章节或接近最长章节
- 第 4 章每个主要模块是否包含截图
- 第 4 章每个主要模块是否包含简要核心代码
- 第 3 章设计图数量是否达标
- E-R 图是否按需要拆分为总表图和核心表图
- 文献是否全部在目标时间范围内
- 是否还混入低可信旧说明文档中的事实

## Style Guardrails

正文语言默认遵循以下风格约束：

1. 模仿样文的章节推进节奏，不机械模仿原句。
2. 优先写项目事实，不先写空泛结论。
3. 避免连续堆砌“具有重要意义”“实现了良好效果”“具有较高价值”这类空话。
4. 避免过密排比句、模板化总分总和明显 AI 套话。
5. 每章至少应有一部分直接对应源码中的真实模块、真实规则或真实数据结构。
6. 致谢可适度更自然、更有人情味，但正文不能过度口语化。

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
- 分析样文 DOCX：`tools/analyze_docx.py`
- 检查参考文献池：`tools/build_reference_pool.py`
- 生成文献核验清单模板：`tools/write_reference_verification_template.py`
- 图表与截图补全检查：`tools/ensure_thesis_assets.py`
- 提取截图占位符：`tools/extract_screenshot_placeholders.py`
- 生成图源码附件 DOCX：`tools/generate_diagram_appendix_docx.py`
- 生成截图计划：`tools/build_screenshot_plan.py`
- 自动抓取页面截图：`tools/capture_thesis_screenshots.py`
- 渲染 Mermaid：`tools/render_mermaid.py`
- 生成 DOCX：`tools/generate_thesis_docx.py`
