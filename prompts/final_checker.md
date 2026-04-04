# Final Checker Prompt

交付前必须逐项检查：

1. 章节完整
2. 字数接近样文目标，优先核对 `python tools/count_chapter_words.py <thesis.md>` 的 `APPROX_WORDS`
3. 参考文献比例符合要求
4. 图表编号连续
5. 是否残留占位符
6. `.docx` 是否真实存在
7. 摘要 / Abstract / 参考文献 / 致谢样式是否正确
8. 英文字体是否正确
9. 图表是否真实插入
10. 最终正文是否还残留 `**`、反引号或 Markdown 链接

最终检查时，必须至少执行：

- `python tools/count_chapter_words.py <thesis.md>`
- `python tools/ensure_thesis_assets.py <thesis.md> --check-only`
- 如果存在截图占位，还必须确认 `image-map.json` 已由 `python tools/capture_thesis_screenshots.py <plan.json>` 生成
