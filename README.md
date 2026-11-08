# Forecast Provenance: OBR GDP forecast audit demonstration

An offline, independently rerunnable example of **bounded arithmetic and curated catalog comparison**, using researcher-transcribed UK Office for Budget Responsibility (OBR) forecasts. This demonstration is separate from the Forecast Provenance Trust Core and cannot substantiate a complete, production-ready historical verification claim.

## What the example shows

Four selected OBR Economic and fiscal outlook editions contain different projections for **UK calendar-year 2025 real GDP growth**. Their forecast values are 1.9% (March 2024), 2.0% (October 2024), 1.0% (March 2025) and 1.5% (November 2025). The fixed comparison value is the **March 2026 observation vintage of 1.4%**. The absolute errors are 0.5, 0.6, 0.4 and 0.1 percentage points, respectively, giving a mean of **0.4 percentage points for the selected four rows**.

The earlier three-row selection in `input_v01_original.json` deliberately excludes November 2025. It is detected as a missing entry relative to the **separately saved, researcher-curated, four-entry catalog**. This does not show OBR failed to release anything, and does not prove the catalog is a complete mandatory issuance schedule. The dates and numbers were transcribed from public OBR web reports and have not been independently authenticated to their original publication dates.

## Run it

Requires Python 3.10 or newer. No package installation, network requests, account, external service or secret material is required.

```sh
python3 selftest.py
python3 audit.py --input input_v02.json --catalog catalog.json --output replayed_v02.json
python3 audit.py --input input_v01_original.json --catalog catalog.json --output replayed_old.json
```

Expected behavior:

| Command | Exit | Key findings |
| --- | ---: | --- |
| `selftest.py` | 0 | 12 assertions over 4 direct audit invocations |
| `audit.py` with `input_v02.json` | 0 | curated catalog matched; selected-row MAE 0.4 percentage points; mandatory universe UNKNOWN |
| `audit.py` with `input_v01_original.json` | 2 | one missing row relative to this curated catalog; selected-row MAE 0.5 percentage points; mandatory universe UNKNOWN |

Exit code 2 is expected for the intentionally incomplete older input. The two `result_*.json` files are archived expected result examples; `selftest.py` writes `test_results.json` during execution.

## Verification limits

* `ARITHMETIC=PASS` is restricted to the supplied rows.
* `MATCHED_CURATED_REGISTER` is agreement with this selected register only.
* Independent mandatory cycle universe, source authenticity, original publication-time existence, pre-outcome durability, and complete historical revision tracking remain **UNKNOWN**.
* The four forecasts target the same year and are correlated. Their mean absolute error is illustrative arithmetic, not a sample-independent forecasting performance estimate.
* No external Roughtime request, signer, acceptance, qualification, Genesis, or production protocol operation is performed by this program.

See [source locations and limitations](SOURCE_AND_LIMITATIONS.md) for links and assumptions.

## Rights and attribution

**Only the original source code** in `audit.py` and `selftest.py` is provided under the MIT License text in [LICENSE_CODE_MIT.txt](LICENSE_CODE_MIT.txt), with `Copyright (c) 2026 Forecast Provenance`. Other content has separate conditions as described in [LICENSE_SCOPE.md](LICENSE_SCOPE.md).

Selected OBR-origin information is reused subject to the applicable Open Government Licence terms. See [OBR_DATA_ATTRIBUTION.md](OBR_DATA_ATTRIBUTION.md). No OBR endorsement is implied. Nothing here grants rights to or changes the license or governance state of Forecast Trust Core.
