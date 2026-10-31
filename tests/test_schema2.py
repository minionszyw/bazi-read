from datetime import datetime
import pytest
from bazi_read import calculate, compare, BaziError
from bazi_read.engine import _incremental

B = dict(sex='male', year=1990, month=5, day=17, hour=14, minute=30,
         longitude=116.405285, timezone='Asia/Shanghai')


def test_core_and_unchanged_calendar():
    previous = {'natal': {'year': {'ganzhi': '庚午',
                        'stem_element': '金',
                        'stem_polarity': '阳',
                        'stem_ten_god': '偏印',
                        'hidden': [{'stem': '丁', 'ten_god': '正财'}, {'stem': '己', 'ten_god': '正官'}],
                        'nayin': '路旁土',
                        'void': '戌亥',
                        'growth_stage': '沐浴'},
               'month': {'ganzhi': '辛巳',
                         'stem_element': '金',
                         'stem_polarity': '阴',
                         'stem_ten_god': '正印',
                         'hidden': [{'stem': '丙', 'ten_god': '偏财'},
                                    {'stem': '戊', 'ten_god': '七杀'},
                                    {'stem': '庚', 'ten_god': '偏印'}],
                         'nayin': '白蜡金',
                         'void': '申酉',
                         'growth_stage': '死'},
               'day': {'ganzhi': '壬午',
                       'stem_element': '水',
                       'stem_polarity': '阳',
                       'stem_ten_god': '日主',
                       'hidden': [{'stem': '丁', 'ten_god': '正财'}, {'stem': '己', 'ten_god': '正官'}],
                       'nayin': '杨柳木',
                       'void': '申酉',
                       'growth_stage': '胎'},
               'hour': {'ganzhi': '丁未',
                        'stem_element': '火',
                        'stem_polarity': '阴',
                        'stem_ten_god': '正财',
                        'hidden': [{'stem': '己', 'ten_god': '正官'},
                                   {'stem': '丁', 'ten_god': '正财'},
                                   {'stem': '乙', 'ten_god': '伤官'}],
                        'nayin': '天河水',
                        'void': '寅卯',
                        'growth_stage': '冠带'}},
     'luck': {'start': '1996-12-13T23:05:20.800800+08:00',
              'periods': [{'pillar': {'ganzhi': '壬午'}},
                          {'pillar': {'ganzhi': '癸未'}},
                          {'pillar': {'ganzhi': '甲申'}},
                          {'pillar': {'ganzhi': '乙酉'}},
                          {'pillar': {'ganzhi': '丙戌'}},
                          {'pillar': {'ganzhi': '丁亥'}},
                          {'pillar': {'ganzhi': '戊子'}},
                          {'pillar': {'ganzhi': '己丑'}},
                          {'pillar': {'ganzhi': '庚寅'}},
                          {'pillar': {'ganzhi': '辛卯'}}]},
     'relations': [{'type': '天干同类', 'positions': ['year', 'month'], 'rule_id': 'REL-01'},
                   {'type': '自刑', 'positions': ['year', 'day'], 'rule_id': 'REL-01'},
                   {'type': '天干前生后', 'positions': ['year', 'day'], 'rule_id': 'REL-01'},
                   {'type': '六合', 'positions': ['year', 'hour'], 'rule_id': 'REL-01'},
                   {'type': '天干后克前', 'positions': ['year', 'hour'], 'rule_id': 'REL-01'},
                   {'type': '天干前生后', 'positions': ['month', 'day'], 'rule_id': 'REL-01'},
                   {'type': '天干后克前', 'positions': ['month', 'hour'], 'rule_id': 'REL-01'},
                   {'type': '天干五合', 'positions': ['day', 'hour'], 'rule_id': 'REL-01'},
                   {'type': '六合', 'positions': ['day', 'hour'], 'rule_id': 'REL-01'},
                   {'type': '天干前克后', 'positions': ['day', 'hour'], 'rule_id': 'REL-01'},
                   {'type': '三会', 'positions': ['year', 'month', 'hour'], 'rule_id': 'REL-01'},
                   {'type': '三会', 'positions': ['month', 'day', 'hour'], 'rule_id': 'REL-01'}]}
    result = calculate(B)
    assert result['schema_version'] == '2.0'
    assert set(result) == {'schema_version', 'engine_version', 'input', 'rules', 'time',
                           'natal', 'season', 'relations', 'luck', 'warnings'}
    for key, p in result['natal'].items():
        for field in ('ganzhi', 'hidden', 'stem_ten_god'):
            assert p[field] == previous['natal'][key][field]
    assert result['luck']['start'] == previous['luck']['start']
    assert result['relations'] == previous['relations']
    assert [p['ganzhi'] for p in result['luck']['periods']] == [p['pillar']['ganzhi'] for p in previous['luck']['periods']]
    assert result == calculate(B)


def test_year_and_month_context():
    r = calculate(B, options=dict(analysis_year=2026, include_monthly=True))
    a = r['analysis']
    assert a['annual']['ganzhi'] == '丙午'
    assert len(a['monthly']) == 12
    assert a['monthly'][0]['start'] == a['start']
    assert a['monthly'][-1]['end'] == a['end']
    for p in a['periods']:
        assert all(set(rel['positions']) & {'luck', 'annual'} for rel in p['relations'])
    for month in a['monthly']:
        for segment in month['periods']:
            assert all('monthly' in rel['positions'] for rel in segment['relations'])


def test_transition_and_pre_luck():
    initial = calculate(B)
    start = datetime.fromisoformat(initial['luck']['start'])
    r = calculate(B, options={'analysis_year': start.year, 'include_monthly': True})
    segments = r['analysis']['periods']
    assert len(segments) == 2
    assert segments[0]['luck'] is None
    assert segments[1]['luck']['index'] == 1
    assert datetime.fromisoformat(segments[0]['end']) == start
    assert segments[0]['end'] == segments[1]['start']
    assert sum(len(m['periods']) for m in r['analysis']['monthly']) == 13
    later = calculate(B, options={'analysis_year': start.year + 10, 'luck_count': 1})
    assert [p['luck']['index'] for p in later['analysis']['periods']] == [1, 2]


def test_beyond_overview():
    r = calculate(B, options={'analysis_year': 2220, 'luck_count': 1})
    assert r['analysis']['periods'][0]['luck']['index'] > 1


def test_auxiliary_and_trace():
    r = calculate(B, options={'include_auxiliary': True, 'include_trace': True})
    hour = r['auxiliary']['pillars']['hour']
    assert hour['day_master_growth']['stage'] == '养'
    assert hour['self_stem_growth']['stage'] == '冠带'
    assert hour['void']['reference'] == 'hour'
    assert r['trace']['time']['selected_clock'] == r['time']['selected_clock']
    assert 'growth_stage' not in r['natal']['hour']


@pytest.mark.parametrize('options', [dict(year_count=10), dict(unknown=True),
    dict(include_monthly=True), dict(include_trace=1), dict(luck_count=True),
    dict(analysis_year=None), dict(analysis_year=2221)])
def test_options_errors(options):
    with pytest.raises(BaziError) as e:
        calculate(B, options=options)
    assert e.value.code == 'OPTIONS'


def test_combination_with_luck_and_annual():
    rows = _incremental({'year': '甲申', 'luck': '丙子', 'annual': '戊辰'}, {'luck', 'annual'})
    assert any(r['type'] == '三合' and r['positions'] == ['year','luck','annual'] for r in rows)


def test_compare_options():
    r = compare(B, {'civil': {'time_basis': 'civil'}}, {'analysis_year': 2026})
    assert r['profiles']['civil']['analysis']['year'] == 2026
