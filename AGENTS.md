# 仓库协作指南

## 项目结构与模块组织

- `src/bazi/engine.py` 实现历法计算、规则对照和结构化结果；`cli.py` 提供命令行入口。
- `src/bazi/data/latlng.json` 是唯一随包分发的地点数据。通过 `importlib.resources` 加载，避免依赖当前工作目录。
- `tests/` 包含历法规则和数据结构行为的 pytest 测试。
- `docs/analysis.md` 保持为唯一分析指南，`examples/output.template.json` 保持为唯一报告模板。
- `.agents/skills/SKILL.md` 定义咨询工作流；生成报告放入已被 Git 忽略的 `outputs/`。

## 构建、测试与开发命令

使用 Python 3.10+，在仓库根目录执行：

```sh
python3 -m venv .venv
.venv/bin/pip install -e '.[dev]'
.venv/bin/pytest -q
.venv/bin/pip wheel --no-deps --wheel-dir dist .
```

以上命令依次创建虚拟环境、安装开发依赖、运行测试和构建 wheel。
地点查询使用 `.venv/bin/bazi places 东城区`；排盘使用 `.venv/bin/bazi chart --input /path/to/case.json`。
输入包含 `birth`，以及可选的 `rules`、`options` 对象。

## 代码风格与命名

使用四空格缩进，函数和变量采用 `snake_case`，类采用 `PascalCase`。
改动应聚焦任务，避免格式化无关代码。目前未配置格式化工具或代码检查工具。
中文资源使用 UTF-8 编码，保留既有 JSON 字段名称。

## 测试要求

使用 pytest，测试文件命名为 `test_*.py`，测试函数以 `test_` 开头。
修改计算或接口时补充回归用例，重点覆盖交节边界、00点与23点换日、闰月、夏令时及交运分段。
目前未设置最低覆盖率。修改打包方式时，应安装 wheel，并在仓库目录之外验证包内数据可读取。

## 提交与拉取请求

沿用 Git 历史中的简洁 Conventional Commit 前缀：`feat:`、`refactor:`、`docs:`，描述改动后的行为。
拉取请求说明应包含问题、改动、验证结果及数据结构不兼容变化；有相关议题时附上链接。
提交前运行 `git diff --check`，避免纳入无关改动。

## 架构与报告约束

引擎输出确定性 JSON，agent 的命理解释单独处理。
区分项目版本、引擎结构版本和报告模板版本。保留来源核验限制，不编造古籍引文。
不提交个人生辰资料、生成报告、虚拟环境或构建产物。
