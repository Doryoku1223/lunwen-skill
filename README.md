# lunwen

面向中文毕业论文、毕业设计论文、技术报告和课程设计论文的写作与交付技能。

## 推荐使用方式

建议优先在 Codex 中使用本 skill。

原因：

- Codex 更适合一边读取项目代码、一边分析学校模板、一边生成和修正文档
- 本 skill 的完整流程依赖多轮文件检查、样式比对、脚本执行和成稿验证
- 当论文模板是“带完整示例内容的学校模板”时，Codex 更适合持续迭代修正编号、目录、图表、附录和后置章节样式

推荐工作顺序：

1. 在 Codex 中加载本 skill
2. 先提供学校模板、样文、开题报告或任务书路径
3. 等待模板分析与目录/样式确认
4. 再生成正文、图表和 `.docx` 成稿

## 推荐搭配使用 Skills

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
- `skill-creator`
  当你要继续迭代或发布这个 skill 时，用它来规范更新 `SKILL.md`、prompts、脚本和资源结构

如果论文工作流中还涉及以下任务，也建议按需搭配：

- `pdf`
  当学校只给 PDF 模板、PDF 样文或需要逐页视觉检查时使用
- `doc`
  当输入是 `.doc` 而不是 `.docx`，且需要先转换后再分析时使用
- `playwright`
  当需要抓真实系统截图替换论文占位图时使用

## 当前能力

- 基于真实项目代码与文档冻结论文事实底稿
- 优先分析学校模板和往届样文，而不是直接套默认样式
- 支持 `.doc -> .docx` 转换后再做模板/样文分析
- 提取封面、目录、正文起点、标题层级、图题表题、参考文献等样式
- 新建 Word 表格时优先按三线表处理，并支持从模板/样文克隆三线表结构
- 按样文章节体量控字写作
- 通过独立 prompt 控制语言风格、逻辑检查和整体 review
- 支持科研型论文的概念图、示意图、框架图规划
- 支持将 LaTeX 公式转换为 Word 公式对象插入文档
- 处理真实图片、截图、Mermaid 图和参考文献
- 输出可交付的 `.docx`

## 核心变化

当前版本已补充：

1. 模板优先工作流
2. `.doc` 自动转换入口
3. `docx` 模板样式分析脚本
4. `docx` 模板继承式生成脚本
5. 无模板时自动生成可刷新目录字段
6. 三线表默认生成
7. 语言风格 / 逻辑检查 / 整体 review / 图示规划 prompt
8. LaTeX 公式转 Word 公式对象
9. 模板三线表识别与克隆

## 常用脚本

### 转换 doc 为 docx

```bash
python tools/convert_word_to_docx.py template.doc
```

### 分析模板或样文样式

```bash
python tools/analyze_docx_styles.py template.docx template-style.json
```

### 生成 DOCX

无模板模式：

```bash
python tools/generate_thesis_docx.py thesis.md thesis.docx image-map.json --insert-toc
```

模板继承模式：

```bash
python tools/generate_thesis_docx.py thesis.md thesis.docx image-map.json \
  --template template.docx \
  --style-spec template-style.json \
  --replace-from 设计总说明
```
