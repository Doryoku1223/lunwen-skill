<div align="center">

# 论文.skill

> “论文不是把字堆满，而是把项目事实、样文规范、图表截图和 Word 交付一次性闭环。”

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-F7C948)
![Codex](https://img.shields.io/badge/Codex-Skill-111111)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-6B7280)
![Chinese Thesis](https://img.shields.io/badge/Chinese-Thesis%20Workflow-0A7EFA)

面向本科计科学生推出的一键论文初稿 Skill。

不会写毕业论文初稿，开题报告和项目代码不知道怎么落成正文？  
历届样文、学校模板、格式要求很多，但拼不出完整结构？  
流程图、用例图、E-R 图、系统截图和测试内容总是缺一块？  
最后要交 `.docx`，却还停留在零散材料和碎片化笔记里？

把零散材料快速整理成论文初稿的 Skill。  
可以结合历届样文、开题报告、学校模板和真实项目内容生成初稿，  
自动补充流程图、用例图、E-R 图等论文图表，并补齐项目截图与常见配图位，形成一套可继续精修的论文初稿工作流。

[安装](#安装) · [快速使用方式](#快速使用方式) · [使用流程](#推荐工作流) · [当前能力](#当前能力) · [常用脚本](#常用脚本) · [详细安装说明](./INSTALL.md) · [GitHub](https://github.com/Doryoku1223/lunwen-skill)

</div>

## 安装

### 方式 1：使用 Codex skill-installer 直接安装

```powershell
python "${HOME}\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo Doryoku1223/lunwen-skill --path . --name lunwen
```

### 方式 2：手动克隆到本地 skills 目录

```powershell
git clone https://github.com/Doryoku1223/lunwen-skill.git "${HOME}\.codex\skills\lunwen"
```

安装后重启 Codex，即可让它发现这个 skill。

如果你使用 Claude Code，也可以把仓库放到项目中直接复用其中的 `.claude/commands/` 和 `.claude/agents/` 兼容层，详细说明见 [INSTALL.md](./INSTALL.md)。

仓库同时补充了 `.trae/commands/` 与 `.trae/agents/` 兼容包装，方便在 Trae 这类只读取入口命令/代理定义的环境里尽量完整传递工作流。

## 快速使用方式

推荐优先在 Codex 中使用本 skill。

最简单的使用方法：

1. 把本项目 GitHub 链接复制给 Codex，让它帮你安装这个 skill。
2. 安装成功后，在 Codex 中打开你的项目文件夹。
3. 直接对 Codex 说：`为这个项目写一篇论文`
4. 然后按提示继续提供学校模板、历届样文、开题报告或任务书路径。

建议你在第一次使用时优先提供：

- 学校论文模板
- 历届样文
- 开题报告或任务书
- 项目源码目录

这样 Codex 才能按“先分析模板，再确认目录样式，最后生成 `.docx` 成稿”的正确流程工作。

## 推荐搭配 Skills

以下是这次实战迭代中证明有价值的搭配：

- `lunwen`
  论文主流程，负责模板优先分析、目录设计、正文写作、图表与成稿交付
- `docx`
  用于读取、分析和校验 `.docx` 模板与成稿，尤其适合处理样式、结构和文档对象
- `planning-with-files`
  用于长流程任务管理，适合论文这类多阶段任务，避免在模板分析、写作、成稿之间丢状态
- `systematic-debugging`
  当成稿出现目录重复、标题编号叠加、图片覆盖正文、附录样式错误等问题时，用它来定位根因，而不是盲改
- `verification-before-completion`
  在声称“论文已经生成好”之前，强制执行字数、引用、目录、图片和 `.docx` 存在性检查

如果论文工作流中还涉及以下任务，也建议按需搭配：

- `pdf`
  当学校只给 PDF 模板、PDF 样文或需要逐页视觉检查时使用
- `doc`
  当输入是 `.doc` 而不是 `.docx`，且需要先转换后再分析时使用
- `playwright`
  当需要抓真实系统截图替换论文占位图时使用

## 当前能力

- 样文目录与字数分析
- 样文 DOCX 样式提取与结构化样式配置
- 模板/样文样式提取
- 项目事实底稿抽取
- 按样文章节节奏控字写作
- 中文/英文参考文献比例控制
- Mermaid / PlantUML 图表策略
- 内置 Playwright / Chrome CDP 浏览器自动截图策略
- doc / docx Word 成稿交付策略

## 推荐目录结构

```text
lunwen/
├── SKILL.md
├── README.md
├── INSTALL.md
├── agents/
│   └── openai.yaml
├── prompts/
├── references/
├── tools/
├── docs/
└── examples/
```

## 设计原则

1. 项目事实优先，不凭空补模块。
2. 样文章节体量优先，不默认写厚。
3. 学样文不只学内容，也学样式。
4. 图表、截图、参考文献和 Word 交付都要闭环。
5. 最终对用户展现过程与结果默认使用中文。

## 推荐工作流

建议按下面顺序使用本 skill：

1. 读取项目代码与文档，冻结项目事实底稿。
2. 分析样文或模板，提取章节体量和版式样式。
3. 生成目标章节字数表。
4. 分章写作并持续控字。
5. 构建参考文献池并检查中英文比例。
6. 处理 Mermaid / PlantUML 图表。
7. 抓取真实系统截图替换占位。
8. 生成 `.docx`。
9. 做最终检查。

## 常用脚本

### 1. 统计论文各章字数

```bash
python tools/count_chapter_words.py thesis.md
```

### 2. 分析样文 PDF

```bash
python tools/analyze_sample_pdf.py sample.pdf
```

### 3. 检查参考文献池

```bash
python tools/build_reference_pool.py thesis.md
```

### 4. 分析样文 DOCX 并生成样式配置

```bash
python tools/analyze_docx_styles.py sample.docx output/style-profile.json
```

### 5. 提取截图占位并生成截图计划

```bash
python tools/extract_screenshot_placeholders.py thesis.md --json-out labels.json
python tools/build_image_map.py labels.json output/doc image-map.json
```

### 6. 提取 Mermaid 图块

```bash
python tools/extract_mermaid_blocks.py thesis.md tmp/mermaid --manifest tmp/mermaid/manifest.json
```

### 7. 渲染 Mermaid

```bash
python tools/render_mermaid.py tmp/mermaid/diagram-01.mmd tmp/mermaid/diagram-01.png
```

### 8. 生成 DOCX

```bash
python tools/generate_thesis_docx.py thesis.md thesis.docx --style-spec output/style-profile.json --image-map image-map.json
```

## 当前限制

- 如果环境没有 LibreOffice / Poppler，无法做逐页渲染检查。
- 如果环境没有 Mermaid 渲染能力，流程图可能只能保留源码或占位。
- 浏览器截图与真实系统抓图能力依赖额外环境支持。

## 兼容性

- Codex：原生适配。
- Claude Code：已补 `.claude/commands/` 与 `.claude/agents/` 兼容层。
