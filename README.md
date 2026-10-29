# 本地子平排盘引擎

Python 3.10+；本地计算，出生数据不会上传。

## 安装

在项目目录下创建虚拟环境并安装：

```sh
python3 -m venv .venv
.venv/bin/pip install -e .
```

## 使用

以下命令均在项目目录下执行。

```sh
# 排盘，输出 JSON
.venv/bin/bazi chart --input examples/birth.json

# 对照不同时间与换日规则
.venv/bin/bazi compare --input examples/birth.json

# 查询出生地
.venv/bin/bazi places 朝阳
```

Python 调用：

```python
from bazi import calculate

result = calculate({
    'sex': 'male', 'calendar': 'solar',
    'year': 1990, 'month': 5, 'day': 17, 'hour': 14, 'minute': 30,
    'longitude': 116.405285, 'timezone': 'Asia/Shanghai',
})
```

## 输入

可直接传入出生资料，或使用 `birth`、`rules`、`options` 外层结构，见[输入示例](examples/birth.json)。

- 历法：公历用 `calendar=solar`；农历用 `calendar=lunar`，以 `is_leap_month=true/false` 区分闰月与正常月。若该年该月无闰月，标识可省略。
- 时间：准确到分钟；指定 `timezone` 或 `utc_offset_minutes`。夏令时导致钟点重复时，用 `fold=0/1` 选择前后分支。
- 出生地：指定 `longitude`，或通过 `place` 提供地点完整路径或唯一查询串；地点表保留原有旧地名。

查询某年闰几月，不能确定出生记录指的是正常月还是同名闰月；有歧义时仍须明确指定。

## 排盘规则

通过 `rules` 指定，省略时使用默认值。

| 参数 | 含义 | 默认值 | 其他可选值 |
|---|---|---|---|
| `time_basis` | 时间基准 | `apparent`：真太阳时 | `mean`：平太阳时；`civil`：民用时间 |
| `year_boundary` | 换年 | `lichun`：立春 | `spring_festival`：春节 |
| `day_boundary` | 换日 | `midnight`：00点 | `zi_start`：23点 |
| `late_zi` | 00点换日时，晚子时起时所用日干 | `same_day`：当日 | `next_day`：次日 |

太阳时需要经度，缺失时不会自动退回民用时间。

## 输出选项

通过 `options` 指定。

| 参数 | 含义 | 默认值 | 范围 |
|---|---|---|---|
| `luck_count` | 大运步数 | 10 | 1—12 |
| `year_count` | 从出生年起输出的流年数 | 100 | 1—120 |
| `analysis_year` | 展开流月的年份 | 出生年 | 1900—2220 |

流月指指定立春年起的十二节月；流年年份标签指立春年。辅助神煞仅标匹配位置，不作吉凶解释。

JSON 包含输入、规则、时间换算、四柱、节气、关系、岁运与辅助表。
输入错误时，Python 抛出 `BaziError`，命令行输出结构化错误并以状态码 2 退出。

`compare` 返回各规则的结果，以及相对首盘有变化的原局字段；可通过 `profiles` 字典指定对照规则。

## 开发与测试

```sh
.venv/bin/pip install -e '.[dev]'
.venv/bin/pytest -q
```

## 依据与限制

古籍规则存在版本分歧。当前已有篇章定位，本地扫描逐条页码校勘尚未完成，神煞表带待校勘状态。
精确交节与时区采用现代计算约定；不自动判断身强弱、格局、喜用神或人生事件。

参见[规则依据](docs/rules.md)及[人工分析指南](docs/analysis.md)。

历法依赖 sxtwl（BSD-3-Clause），感谢寿星天文历原作者许剑伟及 sxtwl 维护者；时区数据由 tzdata 提供。
地点数据为用户已有文件，未确认其再分发许可，对外发布前应确认该许可。
