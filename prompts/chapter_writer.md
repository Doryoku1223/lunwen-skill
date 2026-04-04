# Chapter Writer Prompt

用于按样文章节节奏写作。

要求：

- 先看样文对应章节字数
- 控制当前章节篇幅
- 语言风格贴近本科软件类论文
- 第 5 章默认按“说明 -> 流程图 -> 关键实现 -> 页面图”展开
- 写完立即统计字数，优先使用 `python tools/count_chapter_words.py <thesis.md>`
- 超出就压缩
- 不能残留 `**`、反引号、Markdown 链接等标记
- 如果正文缺少架构图、E-R 图、关键流程图、数据表、测试用例表或页面截图占位，必须执行
  `python tools/ensure_thesis_assets.py <thesis.md> --check-only`
  并在继续写作前补齐缺失项
- 如果正文存在截图占位，优先执行：
  `python tools/extract_screenshot_placeholders.py <thesis.md> --json-out labels.json`
  `python tools/build_screenshot_plan.py labels.json output/screenshot-plan.json --base-url <system-url>`
  `python tools/capture_thesis_screenshots.py output/screenshot-plan.json`
