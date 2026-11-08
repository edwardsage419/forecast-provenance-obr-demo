# OBR Forecast Audit Demo v0.1.0

## English

This standalone, offline research demo recalculates selected OBR UK GDP growth forecast errors and detects a deliberately missing forecast entry relative to a researcher-curated four-release catalog. It uses only the Python standard library.

**Run:** After extracting the repository, open a terminal in its root folder and execute:

```sh
python3 selftest.py
python3 audit.py --input input_v02.json --catalog catalog.json --output replayed_v02.json
python3 audit.py --input input_v01_original.json --catalog catalog.json --output replayed_old.json
```

The self-checks pass 12 assertions. The revised four-row input returns code `0` and selected-row MAE `0.4` percentage points. The intentionally incomplete earlier input returns code `2` and selected-row MAE `0.5` percentage points. This only tests the supplied catalog, **not** the independently complete mandatory history.

Original source authenticity, historical revisions, pre-outcome durability, independent mandatory issuance universe and all production protocol claims remain **UNKNOWN** or **NOT ESTABLISHED**, as applicable. No Genesis or production activity occurs. See `SOURCE_AND_LIMITATIONS.md`, `LICENSE_SCOPE.md`, and `OBR_DATA_ATTRIBUTION.md` for the evidence and license boundaries.

## 中文说明

这是一个独立、离线运行的公开研究演示。程序使用 Python 标准库，对选定的 OBR 英国 GDP 增长预测重新计算误差，并相对于研究人员整理的四期目录，检测故意缺少的一条预测记录。

**运行方法：** 解压仓库文件后，在包含 `audit.py` 的目录执行：

```sh
python3 selftest.py
python3 audit.py --input input_v02.json --catalog catalog.json --output replayed_v02.json
python3 audit.py --input input_v01_original.json --catalog catalog.json --output replayed_old.json
```

自测包含 12 条断言。四条记录的修订版输入返回退出码 `0`，选样平均绝对误差为 `0.4` 个百分点。故意缺少一条记录的旧版输入返回退出码 `2`，选样平均绝对误差为 `0.5` 个百分点。上述检查只针对给定目录，**不证明**全部强制历史发布义务完整。

原始来源认证、历史修订、结果发生前的耐久性、独立强制发布全集及生产协议资格仍为 **`UNKNOWN`** 或 **`NOT ESTABLISHED`**。演示不执行 Genesis 或生产操作。证据与许可范围见 `SOURCE_AND_LIMITATIONS.md`、`LICENSE_SCOPE.md` 和 `OBR_DATA_ATTRIBUTION.md`。
