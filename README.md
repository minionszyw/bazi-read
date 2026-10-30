# bazi · AI Agent 命理分析

## 简介

本地排盘引擎计算原局与岁运，AI agent依据古籍论法完成分析，并接续用户追问。

- [技能文档](.agents/skills/SKILL.md)：环境检查与工作流。
- [分析指南](docs/analysis.md)：原局、岁运和分项分析方法，以及报告组织方式。
- [输出模板](examples/output.template.json)：完整报告骨架。

## 安装

要求Python 3.10+，在项目根目录执行：

```sh
python3 -m venv .venv
.venv/bin/pip install -e .
```

已有虚拟环境时先检查依赖，仅在缺少包时执行安装命令。

## 使用

### CLI 使用

将以下排盘输入保存为自建的 `case.json`，在项目根目录执行命令：

```json
{
  "birth": {
    "sex": "male",
    "calendar": "solar",
    "year": 1990,
    "month": 5,
    "day": 17,
    "hour": 14,
    "minute": 30,
    "longitude": 116.405285,
    "timezone": "Asia/Shanghai"
  },
  "rules": {
    "time_basis": "apparent"
  },
  "options": {
    "analysis_year": 2026
  }
}
```

```sh
# 原局与指定年份的岁运排盘
.venv/bin/bazi chart --input case.json

# 对照时间和换日规则
.venv/bin/bazi compare --input case.json

# 查询出生地
.venv/bin/bazi places 东城区
```

CLI返回排盘、规则对照或地点查询JSON，不生成命理分析，也不自动建立档案或保存完整报告。
`case.json`是排盘输入，与完整报告模板不同；字段及可选规则见[排盘约定](.agents/skills/SKILL.md#排盘约定)。

### Agent 使用

直接在对话中提供姓名（可选）、性别、历法、出生年月日时分、出生地/经度和出生记录时区，例如：

> 我叫小林，男，公历1990年5月17日14:30，出生地北京，时间记录为当时当地钟表时间。请分析原局和今年的岁运。

信息有关键歧义时先补问。首次完整报告默认保存为 `outputs/<case_id>.json`，返回文件链接后直接解盘，讲清原局主线、当前岁运及分项重点，再接续追问。

随后可直接追问，或明确要求更新报告：

> 刚才为什么这样判断事业？
>
> 请看看小林明年的情况。
>
> 请把小林明年的分析更新到报告，保留旧版。

追问用自然语言回答，不写入完整报告。资料复用和报告更新按[技能工作流](.agents/skills/SKILL.md#工作流)执行。

历法依赖sxtwl（BSD-3-Clause），时区数据由tzdata提供，感谢寿星天文历原作者许剑伟及sxtwl维护者。
古籍核验、地点数据许可及解释限制见分析指南；模型和数据处理方式由实际运行环境决定。
