---
name: bazi
description: 接收出生资料，调用本地bazi引擎排原局和岁运，依古籍指南保存JSON分析报告，随后解盘并单独回答后续问题。
---

# AI Agent 命理分析

## 安装依赖

先从本文件所在目录向上两级定位项目根，检查项目环境，仅在缺少依赖时安装。要求Python 3.10+；在项目根运行 `.venv/bin/python -c "import bazi, sxtwl"` 检查，虚拟环境不存在时才创建：

```sh
python3 -m venv .venv
.venv/bin/pip install -e .
```

已有虚拟环境但缺少包时，只执行安装命令。

## 工作流

先读[分析指南](../../docs/analysis.md)，按[输出模板](../../examples/output.template.json)组织报告。以项目根为基准，古籍位于 `../子平古籍/`，完整报告直接保存到 `outputs/`，不为每份资料创建子目录。

1. **识别资料**：姓名去除首尾空白后填入name，未提供或为空时填“用户1”。首次用 `str(uuid.uuid4())` 生成case_id，复用时保持稳定；同名不自动合并，对象或更正意图不明时先补问。
2. **解析生辰**：整理birth/rules/options并保留来源，不将name/case_id传给排盘引擎。历法、同名闰月、生时、时区或地点有关键歧义时先补问；已明确的资料不重复确认。
3. **排盘**：用Python `calculate(birth, rules, options)`，或将补齐资料写入任务临时文件后调用 `.venv/bin/bazi chart --input case.json`。地点查询用 `.venv/bin/bazi places 查询词`。核对返回input/rules和warnings，按下述排盘约定处理边界。
4. **分析原局**：按指南第2节分析日干月令、力量、格局、寒暖燥湿、气势和喜忌，依模板记录判断及依据。
5. **分析岁运与分项**：按下述年份约定展开岁运，依指南第3—4节解释交运分段及六个默认主题；流月、辅助及溯源按需展开。
6. **保存报告**：按指南第5节审查后，首次完整报告默认保存至 `outputs/<case_id>.json`。显式更新时另存为 `<case_id>-002.json` 起的递增版本，数字后缀至少三位；只使用校验后的UUID，不覆盖已有文件。澄清不保存为完整报告，保存失败如实说明，成功后告知文件链接。
7. **解盘**：保存成功后在同一轮回复中，按[解盘方法](../../docs/analysis.md#保存后解盘)直接用自然语言讲解，不只返回文件链接或等待再次要求。
8. **回答追问**：单独用自然语言回答，不写入报告。修正生辰或规则时保留case_id、增加birth_revision并重排；新年份不增加该修订号。仅明确要求更新报告时另存递增文件版本。

跨会话复用时，按case_id定位文件，读取数字版本最大的完整报告（无后缀视为第1版）；对象不明或找不到报告时先说明，不假装记得旧分析。

### 排盘约定

|资料|字段与处理|
|---|---|
|性别|birth.sex为male/female，用于传统大运顺逆，不据称谓猜测|
|历法|birth.calendar为solar/lunar；年月日未注明历法时补问|
|生辰|year/month/day/hour/minute；当前引擎要求准确到分钟，不支持缺时或模糊时段，不能用12点占位|
|闰月|农历同名正常月和闰月并存时指定is_leap_month；引擎能查闰月，但不能猜出生记录指哪一个月；公历无须填写|
|地点|longitude或place；先用places查唯一完整路径，同名补问；经度明确时不重复查询|
|时区|timezone或utc_offset_minutes；地点表不含时区，历史记录不能一律假定UTC+8|
|重复钟点|fold=0/1选择夏令时前后分支；不存在的钟点须核实记录，不自动平移|

默认规则：time_basis=apparent（真太阳时）、year_boundary=lichun（立春）、day_boundary=midnight（00点）、late_zi=same_day（晚子时按当日日干起时）。
可选值依次为mean/civil、spring_festival、zi_start、next_day。月柱始终按十二节；太阳时需要经度，缺失不自动退回民用时间。用户指定的规则优先并在结果中展示。

需要规则对照时调用compare，不以已知经历暗中挑盘；临时输入文件不覆盖模板。

#### 年份和展开选项

首次默认十步大运及当前立春年；用户明确年份优先。当前立春年由执行时可信时刻与当年立春瞬间比较，立春前取上一年，不使用模型记忆或模板年份。

```python
from datetime import datetime, timezone, timedelta
import sxtwl
now = datetime.now(timezone.utc)
year = now.year
v = next(v for v in sxtwl.getJieQiByYear(year) if v.jqIndex == 3)
d = sxtwl.JD2DD(v.jd)
lichun = (datetime(d.Y, d.M, d.D, tzinfo=timezone(timedelta(hours=8)))
          + timedelta(hours=d.h, minutes=d.m, seconds=d.s))
analysis_year = year if now >= lichun else year - 1
```

报告记录年份选择方式、参考时刻及其来源。只有立春当天的日期而没有时刻时先取得可信时刻或保留未定。指定公历日期按实际所属立春年处理；整段公历年可能需要两个相邻立春年的结果，不能称一个analysis_year覆盖公历全年。

|options|默认与范围|
|---|---|
|luck_count|10，允许1—12步大运|
|analysis_year|引擎默认不展开；agent首报显式选择当前立春年，允许1900—2220|
|include_monthly|false；问题需要月份时开启，必须指定分析年|
|include_auxiliary|false；采用相关辅助论法时开启|
|include_trace|false；时间或规则复核需要时开启|

出生公历年支持1900—2100。输入错误抛BaziError，CLI以状态码2输出结构化错误；未解决的同名闰月、地点、重复时间按错误详情补问，不以相同输入反复重试。
BOUNDARY_SENSITIVE提示要检查实际是否跨交节、换日或时辰；普通整点也可能触发，并不等于排盘错误。


## 注意／限制

- 区分引擎事实与分析解释，不手填干支，不把未执行调用或未成功保存写成已完成。
- 古籍核验和论法边界遵循指南；目录不可用时说明无法核验，不编造出处或假称已读原文。
- 模板是报告骨架，不是有效生辰；不猜缺失生时，不以用户经历反向修改排盘规则。
