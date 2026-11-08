# Copyright (c) 2026 Forecast Provenance
# SPDX-License-Identifier: MIT
"""Simple deterministic demo checks; these do not test protocol acceptance."""
import copy, json
from pathlib import Path
from decimal import Decimal
from audit import examine

p=Path(__file__).parent
cat=json.loads((p/'catalog.json').read_text())
prior=json.loads((p/'input_v01_original.json').read_text())
updated=json.loads((p/'input_v02.json').read_text())
old=examine(prior,cat)
assert old['bounded_catalog_membership']=='FAIL'
assert old['missing_from_curated_selection']==['OBR-EFO-2025-11-26-UKGDP-2025']
assert old['selected_rows_mean_absolute_error_pp_not_benchmark']=='0.5'
new=examine(updated,cat)
assert new['bounded_catalog_membership']=='MATCHED_CURATED_REGISTER'
assert new['catalog_is_independently_complete']=='UNKNOWN'
assert new['mandatory_forecast_cycle_universe']=='UNKNOWN'
assert new['selected_rows_mean_absolute_error_pp_not_benchmark']=='0.4'
assert new['calculated_rows'][-1]['absolute_error_pp']=='0.1'
reduced=copy.deepcopy(cat)
reduced['releases']=reduced['releases'][:-1]
evasion=examine(prior,reduced)
assert evasion['bounded_catalog_membership']=='MATCHED_CURATED_REGISTER'
assert evasion['mandatory_forecast_cycle_universe']=='UNKNOWN'
assert evasion['catalog_is_independently_complete']=='UNKNOWN'
wrong=copy.deepcopy(updated)
wrong['forecast_rows'][0]['source_url']='https://example.org/wrong'
assert examine(wrong,cat)['bounded_catalog_membership']=='FAIL'
print('12 assertions across 4 audit invocations passed; mandatory universe still UNKNOWN')
(p/'test_results.json').write_text(json.dumps({
  'assertions':12,
  'audit_invocations':4,
  'scenario_groups':4,
  'status':'PASS_FOR_BOUNDED_DEMO_ONLY',
  'old_missing':old['missing_from_curated_selection'],
  'old_selected_mae_pp':old['selected_rows_mean_absolute_error_pp_not_benchmark'],
  'new_selected_mae_pp':new['selected_rows_mean_absolute_error_pp_not_benchmark'],
  'simultaneous_shrink_cannot_claim_universe_complete':'PASS',
  'normative_universe':'UNKNOWN'
},indent=2)+'\n')
(p/'result_v01_checked_against_v02_catalog.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
