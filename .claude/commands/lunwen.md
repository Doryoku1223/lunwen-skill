---
description: 写作、压缩、仿写、交付中文毕业论文或毕业设计论文
argument-hint: "[论文需求或任务说明]"
---

使用仓库中的 `lunwen` 技能完成论文任务。

执行要求：

1. 先读取 `SKILL.md`
2. 按其中的主流程执行
3. 需要细则时按 `prompts/`、`references/`、`tools/` 中的资源展开
4. 默认输出中文
5. 如果存在样文、模板、项目代码、参考文献约束、截图需求或 `.docx` 要求，全部纳入同一工作流
6. 如果样文是 `.docx`，先运行 `tools/analyze_docx.py` 生成样式配置，再开始正文
7. 写作期间必须用 `tools/count_chapter_words.py` 控字，并用 `tools/ensure_thesis_assets.py` 检查图表/截图闭环
8. 如果存在截图占位，优先用 `tools/build_screenshot_plan.py` + `tools/capture_thesis_screenshots.py` 生成 `image-map.json`

ARGUMENTS: $ARGUMENTS
