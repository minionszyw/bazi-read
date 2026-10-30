# bazi · AI Agent 命理分析

接收出生资料，由本地排盘引擎计算原局与岁运，再由AI agent依据古籍论法完成原局、岁运、分项分析及持续问答。

## 使用入口

- [技能文档](.agents/skills/SKILL.md)：安装依赖、执行工作流与注意事项。
- [分析指南](docs/analysis.md)：资料解析、分析方法、引擎字段、输出约定和古籍依据。
- [输出模板](examples/output.template.json)：统一JSON骨架，不含预设生辰或命理结论。

在支持agent skill的环境中加载技能文档，提供性别、历法、出生年月日时分及出生地/经度、记录时区；必要信息有歧义时由agent补问。
需要具体年份或月份时直接提出问题，agent按需调用引擎。

## 排盘引擎

Python 3.10+；引擎本地计算，提供 `calculate`、`compare` 和 `bazi` 命令行，返回schema 2.0 JSON。
安装与调用方法见技能和指南。引擎不自动生成命理结论，本项目也未实现持久化会话服务。
agent使用的模型及其数据处理方式由实际运行环境决定。

## 开发

```sh
.venv/bin/pip install -e '.[dev]'
.venv/bin/pytest -q
```

历法依赖sxtwl（BSD-3-Clause），感谢寿星天文历原作者许剑伟及sxtwl维护者；时区数据由tzdata提供。
地点数据的来源与再分发许可尚未确认；古籍扫描逐条校勘及解释限制见分析指南。
