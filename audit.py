#!/usr/bin/env python3
# Copyright (c) 2026 Forecast Provenance
# SPDX-License-Identifier: MIT
"""Reproduce a bounded, public-source OBR forecast sample audit.

Scope: arithmetic and comparison to a researcher-curated public archive register.
This is demonstration software only, never production or FP protocol verification.
Even simultaneous changes to register and observations cannot confer authority.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path


def _ids(rows):
    return [r['id'] for r in rows]


def examine(observed: dict, catalog: dict) -> dict:
    if observed.get('artifact_scope') != 'PUBLIC_SOURCE_CURATED_OFFLINE_EVALUATION_DEMO_ONLY':
        raise ValueError('unexpected demonstration scope')
    if catalog.get('scope') != 'PUBLIC_OBR_EFO_ARCHIVE_BOUNDED_CATALOG_OBSERVATION_ONLY':
        raise ValueError('unexpected catalog scope')
    if catalog.get('normative_forecast_issuance_obligation') != 'NOT_ESTABLISHED':
        raise ValueError('bounded catalog cannot assert normative obligation')
    if catalog.get('independently_authenticated_complete_public_archive') != 'UNKNOWN':
        raise ValueError('unverified public catalog cannot assert historical completeness')
    if observed.get('limits',{}).get('independently_complete_mandatory_forecast_universe') != 'UNKNOWN':
        raise ValueError('mandatory universe must remain UNKNOWN')
    rows=observed['forecast_rows']
    releases=catalog['releases']
    if not rows or not releases:
        raise ValueError('empty rows or archive register')
    row_ids, register_ids=_ids(rows),_ids(releases)
    if len(set(row_ids)) != len(row_ids) or len(set(register_ids)) != len(register_ids):
        raise ValueError('duplicate ids')
    expected={r['id']:r for r in releases}
    actual={r['id']:r for r in rows}
    missing=sorted(set(expected)-set(actual))
    unexpected=sorted(set(actual)-set(expected))
    mismatched=sorted(k for k in set(actual)&set(expected) if
        actual[k].get('reported_publication_date') != expected[k]['date'] or
        actual[k].get('source_url') != expected[k]['url'])
    try:
        outturn=Decimal(observed['reference_outturn']['observation_percent'])
        if not outturn.is_finite():raise ValueError('nonfinite outturn')
        calculated=[]
        for r in rows:
            if r.get('externally_authenticated_pre_deadline_existence')!='UNKNOWN':
                raise ValueError('historical existence not established')
            if r.get('source_raw_bytes_preserved') is not False:
                raise ValueError('source bytes not preserved')
            forecast=Decimal(r['forecast_percent'])
            if not forecast.is_finite():raise ValueError('nonfinite forecast')
            signed=forecast-outturn
            calculated.append({'id':r['id'],
               'date':r['reported_publication_date'],
               'forecast_percent':str(forecast),
               'outturn_percent_march_2026_vintage':str(outturn),
               'signed_error_pp':str(signed),
               'absolute_error_pp':str(abs(signed)),
               'squared_error_pp2':str(signed*signed)})
    except (InvalidOperation,KeyError,TypeError) as e:
        raise ValueError('malformed numeric or historical fields') from e
    mean=sum((Decimal(r['absolute_error_pp']) for r in calculated),Decimal(0))/len(calculated)
    return {
      'scope':'PUBLIC_ARCHIVE_BOUNDED_CURATED_OBSERVATION_DEMO_ONLY',
      'bounded_catalog_membership':'FAIL' if missing or unexpected or mismatched else 'MATCHED_CURATED_REGISTER',
      'missing_from_curated_selection':missing,
      'unexpected_curated_selection':unexpected,
      'wrong_curated_release_locator':mismatched,
      'catalog_is_independently_complete':'UNKNOWN',
      'mandatory_forecast_cycle_universe':'UNKNOWN',
      'original_source_bytes_authenticated':'UNKNOWN',
      'corrected_source_version_authenticated':'UNKNOWN',
      'pre_publication_durability':'UNKNOWN',
      'real_genesis_readiness':'NOT_ESTABLISHED',
      'arithmetic_of_supplied_rows':'PASS',
      'observed_count':len(rows),
      'catalog_count':len(releases),
      'calculated_rows':calculated,
      'selected_rows_mean_absolute_error_pp_not_benchmark':str(mean),
      'interpretation':'A match to a user-curated catalog does not establish an independent mandatory universe, historical source authenticity or a valid protocol claim.'
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input', default='input_v02.json')
    p.add_argument('--catalog', default='catalog.json')
    p.add_argument('--output', default='result_v02.json')
    opt=p.parse_args()
    observation=json.loads(Path(opt.input).read_text(encoding='utf-8'))
    catalog=json.loads(Path(opt.catalog).read_text(encoding='utf-8'))
    result=examine(observation,catalog)
    Path(opt.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('CURATED_CATALOG_MEMBERSHIP='+result['bounded_catalog_membership'])
    print('ARITHMETIC='+result['arithmetic_of_supplied_rows'])
    print('MANDATORY_UNIVERSE='+result['mandatory_forecast_cycle_universe'])
    print('SELECTED_ROWS='+str(result['observed_count']))
    print('SELECTED_ROWS_MAE_PP='+result['selected_rows_mean_absolute_error_pp_not_benchmark'])
    if result['missing_from_curated_selection']:
        print('MISSING_FROM_CURATED_SELECTION='+','.join(result['missing_from_curated_selection']))
    return 0 if result['bounded_catalog_membership']=='MATCHED_CURATED_REGISTER' else 2


if __name__=='__main__':
    raise SystemExit(main())
