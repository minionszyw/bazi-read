# 本地子平排盘引擎

Python 3.10+；本地计算，出生数据不会上传。

```sh
cd /Users/m/new/bazi
python3 -m venv .venv
.venv/bin/pip install -e '.[dev]'
.venv/bin/bazi chart --input examples/birth.json
.venv/bin/bazi chart --input examples/birth.json --format markdown
.venv/bin/bazi compare --input examples/birth.json
.venv/bin/bazi places 朝阳
.venv/bin/pytest -q
```

```python
from bazi import calculate, compare
result = calculate({
    'sex': 'male', 'calendar': 'solar',
    'year': 1990, 'month': 5, 'day': 17, 'hour': 14, 'minute': 30,
    'longitude': 116.405285, 'timezone': 'Asia/Shanghai',
})
```

输入可使用`birth/rules/options`外层结构，见examples。农历用`calendar=lunar`、`is_leap_month=true/false`；若该年该月无闰月，标识可省略。查询闰月不能消除同名两个月的出生记录歧义。日期必须准确到分钟。时区必填或提供`utc_offset_minutes`；`fold`指定重复钟点的前后分支。`place`为地点完整路径或唯一查询串，可替代经度；表内旧地名保持原样。

默认规则：`time_basis=apparent`、`year_boundary=lichun`、`day_boundary=midnight`、`late_zi=same_day`。可选值依次为`mean/civil`、`spring_festival`、`zi_start`、`next_day`。没有经度时不自动退回民用时间。

options：`luck_count`默认10（1—12）；`year_count`默认100（1—120）；`analysis_year`默认出生年（1900—2220）。流月指指定立春年起的十二节月。流年年份标签指立春年。辅助神煞仅标匹配位置，不作吉凶解释。

JSON包含输入、规则、时间换算、四柱、节气、关系、岁运与辅助表；Python抛出`BaziError`，CLI输出结构化错误并退出2。`compare`返回各规则结果与相对首盘有变化的原局字段；可通过`profiles`字典指定规则，不自动筛选“正确命盘”。

重要限制：古籍规则有版本分歧。当前已有篇章定位，但本地扫描逐条页码校勘尚未完成，神煞表显式带待校勘状态。精确交节与时区是现代计算约定。参见[规则依据](docs/rules.md)及[人工分析指南](docs/analysis.md)。不输出自动身强弱、格局、喜用神或事件预测。

历法依赖sxtwl（BSD-3-Clause），感谢寿星天文历原作者许剑伟及sxtwl维护者；时区数据由tzdata提供。地点数据为用户已有文件，未确认其再分发许可。对外发布前应确认该数据许可。
