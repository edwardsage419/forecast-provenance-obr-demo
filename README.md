# Forecast Provenance | OBR Forecast Audit Demo

English | [中文说明](#中文说明)

## English

### Overview

This is a small, **offline and independently rerunnable research demonstration** using selected public forecasts from the UK's Office for Budget Responsibility (OBR). It recalculates forecast errors and compares a supplied selection against a **researcher-curated four-entry catalog**.

The demo is separate from Forecast Provenance Trust Core. It does **not** establish a complete mandatory forecast history, authenticate original publication timestamps, or qualify any production protocol.

### What you can check

All four selected releases forecast **UK calendar-year 2025 real GDP growth**. The comparison uses the **1.4% observation vintage from March 2026**, which may be revised later.

| OBR forecast edition | Forecast | Signed error | Absolute error |
| --- | ---: | ---: | ---: |
| March 2024 | 1.9% | +0.5 pp | 0.5 pp |
| October 2024 | 2.0% | +0.6 pp | 0.6 pp |
| March 2025 | 1.0% | −0.4 pp | 0.4 pp |
| November 2025 | 1.5% | +0.1 pp | 0.1 pp |

The mean absolute error (MAE) for **these four selected forecasts** is **0.4 percentage points**. These are successive forecasts of the same target year, so this mean is an arithmetic illustration, **not** an independent-sample performance benchmark.

The deliberately incomplete `input_v01_original.json` contains only the first three editions. When compared with `catalog.json`, the demo reports the November 2025 entry as missing **from the supplied selection**. This is **not** evidence that OBR omitted a required publication. The catalog itself is not independently proven complete.

### Quick start

**Requirements:** Python 3.10 or later. No third-party packages, credentials, network requests, or external services are needed **after the files have been downloaded**.

1. Download and extract the repository using GitHub's **Code → Download ZIP**, or clone it with Git. Open a terminal in the folder containing `audit.py` and `catalog.json`.
2. Run the self-checks, then reproduce the full selected input:

   ```sh
   python3 selftest.py
   python3 audit.py --input input_v02.json --catalog catalog.json --output replayed_v02.json
   ```

3. Reproduce the deliberately incomplete input:

   ```sh
   python3 audit.py --input input_v01_original.json --catalog catalog.json --output replayed_old.json
   ```

On systems where `python3` is unavailable, use the installed Python 3 command (for example, `py -3` on Windows).

### Expected results

| Run | Expected exit code | Expected finding |
| --- | ---: | --- |
| `selftest.py` | `0` | 12 assertions across 4 direct audit invocations pass |
| Revised input (`input_v02.json`) | `0` | `MATCHED_CURATED_REGISTER`; `ARITHMETIC=PASS`; `MANDATORY_UNIVERSE=UNKNOWN`; selected MAE `0.4` pp |
| Earlier input (`input_v01_original.json`) | `2` | `FAIL` for membership against this curated catalog; one selected entry missing; selected MAE `0.5` pp; mandatory universe still `UNKNOWN` |

Exit code `2` for the earlier input is **expected**, because it deliberately omits one catalog entry. It is a local catalog-membership result, not a claim of historical wrongdoing. `selftest.py` writes `test_results.json` and refreshes the archived earlier-input example. The `replayed_*.json` files are locally generated outputs. The two `result_*.json` files shipped with the repository are reference outputs.

### How to interpret the results

* `ARITHMETIC=PASS` validates calculations for the input rows only.
* `MATCHED_CURATED_REGISTER` means that the selected records agree with the provided catalog. If both input and catalog are reduced, a local match is still possible.
* Independent mandatory issuance universe, original source authenticity and revisions, independent pre-deadline existence, and pre-outcome durability remain `UNKNOWN`.
* The program performs no external Roughtime requests, signing, ManifestAcceptance, qualification, Genesis, or production verification.

See [sources and limitations](SOURCE_AND_LIMITATIONS.md) for official OBR report links, the correction notice, and the exact evidence boundary.

### License and attribution

Only the original Python code in `audit.py` and `selftest.py` is licensed under MIT. See [code license](LICENSE_CODE_MIT.txt) and [license scope](LICENSE_SCOPE.md). The researcher-transcribed OBR information has separate reuse terms; see [OBR attribution](OBR_DATA_ATTRIBUTION.md). No OBR endorsement is implied. Forecast Provenance Trust Core is excluded from this license.

---

## 中文说明

### 项目简介

这是一个使用英国预算责任办公室（OBR）部分公开经济预测资料的**离线、可独立重复运行的研究演示**。程序能够重新计算预测误差，并将提交的预测记录与一份**研究人员整理的四条记录目录**比较。

本演示与 Forecast Provenance Trust Core 分离。它**尚不能**证明所有强制预测发布记录的完整性，不能独立认证原始发布时间，也不代表任何生产协议获得资格。

### 演示验证什么

四次选定的公开报告都预测**英国 2025 日历年度实际 GDP 增长率**。比较基准使用 **2026 年 3 月版本中记录的 1.4% 实际值**；该实际值可能在未来修订。

| OBR 预测版本 | 预测值 | 有符号误差 | 绝对误差 |
| --- | ---: | ---: | ---: |
| 2024 年 3 月 | 1.9% | +0.5 个百分点 | 0.5 个百分点 |
| 2024 年 10 月 | 2.0% | +0.6 个百分点 | 0.6 个百分点 |
| 2025 年 3 月 | 1.0% | −0.4 个百分点 | 0.4 个百分点 |
| 2025 年 11 月 | 1.5% | +0.1 个百分点 | 0.1 个百分点 |

**这四条选定记录**的平均绝对误差为 **0.4 个百分点**。它们针对同一年度目标，是不同时间形成的预测版本，因此该平均值只说明计算过程，**不能**视为独立样本的模型表现指标。

`input_v01_original.json` 故意只包含前三期。与 `catalog.json` 比较时，程序会指出**这份选样**缺少 2025 年 11 月记录。这个结果**不代表** OBR 未履行发布义务。该目录自身的历史全集完整性尚未获得独立证明。

### 运行方法

**环境要求：** Python 3.10 或更新版本。下载文件后，运行过程无需第三方 Python 依赖、账户、密钥、网络请求或外部服务。

1. 在 GitHub 页面选择 **Code → Download ZIP** 下载并解压，也可以通过 Git 克隆。进入包含 `audit.py` 和 `catalog.json` 的文件夹。
2. 运行自测并重算四条记录：

   ```sh
   python3 selftest.py
   python3 audit.py --input input_v02.json --catalog catalog.json --output replayed_v02.json
   ```

3. 运行故意缺少一条记录的旧版输入：

   ```sh
   python3 audit.py --input input_v01_original.json --catalog catalog.json --output replayed_old.json
   ```

如果系统没有 `python3` 命令，请使用已安装的 Python 3 启动方式，例如 Windows 的 `py -3`。

### 预期输出

| 操作 | 退出码 | 关键结果 |
| --- | ---: | --- |
| `selftest.py` | `0` | 12 条断言通过，覆盖 4 次直接审计函数调用 |
| 修订版输入 `input_v02.json` | `0` | `MATCHED_CURATED_REGISTER`，`ARITHMETIC=PASS`，`MANDATORY_UNIVERSE=UNKNOWN`，选样平均绝对误差为 `0.4` 个百分点 |
| 旧版输入 `input_v01_original.json` | `2` | 相对于当前选定目录的覆盖检查为 `FAIL`，少一条记录，选样平均绝对误差为 `0.5` 个百分点；强制发布全集仍为 `UNKNOWN` |

旧版输入的退出码 `2` 是预期行为，表示它故意遗漏了所选目录中的一项，**不说明**历史发布违规。`selftest.py` 会写入 `test_results.json` 并刷新旧版的归档示例；`replayed_*.json` 是运行时新生成的文件。仓库提供的两个 `result_*.json` 是对照结果。

### 结果解释与限制

* `ARITHMETIC=PASS` 只说明所提交记录的算术计算通过。
* `MATCHED_CURATED_REGISTER` 只说明记录与当前人工整理的目录一致。若同时缩减记录和目录，仍有可能显示局部匹配。
* 强制预测发布全集、原始文件来源与修订历史、截止前独立存在证明和结果发生前的耐久性，均为 `UNKNOWN`。
* 程序不会发起外部 Roughtime 请求，不执行签名、ManifestAcceptance、资格确认、Genesis 或任何生产验证。

有关官方 OBR 资料链接、更正公告及证据限制，请查看[来源与局限说明](SOURCE_AND_LIMITATIONS.md)。

### 许可与署名

只有原创 Python 程序 `audit.py` 和 `selftest.py` 采用 MIT 许可，具体参见[许可证原文](LICENSE_CODE_MIT.txt)及[许可范围](LICENSE_SCOPE.md)。研究人员转录的 OBR 资料受独立的复用条件约束，详见[OBR 数据署名](OBR_DATA_ATTRIBUTION.md)。本演示不代表获得 OBR 官方认可，也不改变 Forecast Provenance Trust Core 的许可状态。
