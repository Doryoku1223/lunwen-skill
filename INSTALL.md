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
- `.trae/commands/lunwen.md`
- `.trae/agents/lunwen-writer.md`

如果你在 Trae 或其他只读取入口 prompt 的环境中使用，建议优先保证宿主至少能读取：

- `agents/openai.yaml`
- `tools/analyze_docx.py`
- `tools/build_screenshot_plan.py`
- `tools/capture_thesis_screenshots.py`
- `tools/ensure_thesis_assets.py`
- `tools/generate_thesis_docx.py`

否则容易出现“读到技能名字，但没执行完整工作流”的情况。

因此有两种接入方式：

1. 作为技能目录放入 `.claude/skills/lunwen/`
2. 作为项目仓库放在根目录，直接让 Claude Code 读取其中 `.claude/commands/` 和 `.claude/agents/`

## 依赖建议

论文文字与 Word 交付建议具备以下能力：

- `python-docx`
- `pdfplumber`
- `pypdf`
- `Node.js` 与 `npm`（用于仓库内置 Playwright 自举）

如果需要将 `mermaid` / `plantuml` 渲染为真实图片，建议环境额外具备：

- `@mermaid-js/mermaid-cli`
- `plantuml.jar` 或等效渲染方案

如果需要对 `.docx` 做逐页渲染检查，建议环境具备：

- `soffice`
- `pdftoppm`

## 浏览器截图自举

仓库内置了 Playwright 执行链路，首次运行：

```powershell
python tools/capture_thesis_screenshots.py output/screenshot-plan.json
```

会自动在仓库目录执行：

```powershell
npm install
npm run install:browsers
```

然后再开始截图。用户不需要额外安装浏览器 skill。

## 编码规则

- 所有 Markdown、YAML、Prompt、脚本文件统一使用 `UTF-8`
- 不要依赖系统默认编码
- 校验脚本应显式使用 `utf-8` 读取文件
