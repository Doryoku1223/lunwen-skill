# 安装说明

## 本地技能目录

推荐安装到：

`C:\Users\Administrator\.codex\skills\lunwen`

或其他 `$CODEX_HOME/skills` 可发现路径。

## Claude Code 兼容

Claude Code 官方支持 `SKILL.md` 技能目录，也兼容 `.claude/commands/` 与 `.claude/agents/`。

本仓库已经内置：

- `.claude/commands/lunwen.md`
- `.claude/agents/lunwen-writer.md`

因此有两种接入方式：

1. 作为技能目录放入 `.claude/skills/lunwen/`
2. 作为项目仓库放在根目录，直接让 Claude Code 读取其中 `.claude/commands/` 和 `.claude/agents/`

## 依赖建议

论文文字与 Word 交付建议具备以下能力：

- `python-docx`
- `pdfplumber`
- `pypdf`
- Chrome MCP 或等效浏览器自动化能力

如果需要将 `mermaid` / `plantuml` 渲染为真实图片，建议环境额外具备：

- `@mermaid-js/mermaid-cli`
- `plantuml.jar` 或等效渲染方案

如果需要对 `.docx` 做逐页渲染检查，建议环境具备：

- `soffice`
- `pdftoppm`

## 编码规则

- 所有 Markdown、YAML、Prompt、脚本文件统一使用 `UTF-8`
- 不要依赖系统默认编码
- 校验脚本应显式使用 `utf-8` 读取文件
