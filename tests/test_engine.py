import pytest
import sxtwl
from datetime import datetime,timedelta
from bazi import calculate,compare,BaziError
from bazi.engine import ten, G, terms, equation
B=dict(sex='male',year=2000,month=2,day=29,hour=12,minute=30,longitude=120,utc_offset_minutes=480)
def chart(**kw): return calculate(B|kw,options={})
def test_basic():
    r=chart(); assert 'analysis' not in r; assert len(r['luck']['periods'])==10
    assert r['natal']['day']['stem_ten_god']=='日主'
    assert r==chart()
def test_gregorian():
    with pytest.raises(BaziError): chart(year=1900)
def test_lunar():
    with pytest.raises(BaziError,match='同名'): chart(calendar='lunar',year=2020,month=4,day=1)
    for leap in [True,False]:
        r=chart(calendar='lunar',year=2020,month=4,day=1,is_leap_month=leap)
        assert r['time']['lunar']['is_leap_month']==leap
    with pytest.raises(BaziError): chart(calendar='lunar',year=2021,month=4,day=1,is_leap_month=True)
def test_ten():
    assert ten('甲','乙')=='劫财'; assert ten('甲','庚')=='七杀'; assert ten('甲','癸')=='正印'
    for g in G: assert len({ten(g,h) for h in G})==10
def test_rollover():
    b=B|dict(hour=23,minute=30)
    a=calculate(b,{'time_basis':'civil'}); c=calculate(b,{'time_basis':'civil','day_boundary':'zi_start'})
    assert a['natal']['day']['ganzhi']!=c['natal']['day']['ganzhi']
    assert calculate(b,{'time_basis':'civil','late_zi':'next_day'})['natal']['hour']['ganzhi']==c['natal']['hour']['ganzhi']
def test_term_boundary():
    for term in [x for x in terms(2000) if x['utc'].year==2000 and x['index']%2]:
        outputs=[]
        for dt in [-1,1]:
            t=term['utc']+timedelta(seconds=dt)
            outputs.append(chart(year=t.year,month=t.month,day=t.day,hour=t.hour,minute=t.minute,second=t.second,utc_offset_minutes=0))
        assert outputs[0]['natal']['month']['ganzhi']!=outputs[1]['natal']['month']['ganzhi']
def test_dst():
    b={k:v for k,v in B.items() if k!='utc_offset_minutes'}
    with pytest.raises(BaziError,match='不存在'): calculate(b|dict(year=2021,month=3,day=14,hour=2,minute=30,timezone='America/New_York'))
    with pytest.raises(BaziError,match='重复'): calculate(b|dict(year=2021,month=11,day=7,hour=1,minute=30,timezone='America/New_York'))
def test_eot():
    from datetime import timezone
    assert -15<equation(datetime(2020,2,11,tzinfo=timezone.utc))<-13
    assert 15<equation(datetime(2020,11,3,tzinfo=timezone.utc))<18
@pytest.mark.parametrize('year',[1900,1950,2000,2100])
def test_calendar_roundtrip(year):
    for month in range(1,13):
        d=sxtwl.fromSolar(year,month,15)
        x=sxtwl.fromLunar(d.getLunarYear(),d.getLunarMonth(),d.getLunarDay(),d.isLunarLeap())
        assert (x.getSolarYear(),x.getSolarMonth(),x.getSolarDay())==(year,month,15)
@pytest.mark.parametrize('date,expected',[
 ((1900,1,15),['己亥','丁丑','戊子','戊午']),
 ((1950,7,15),['庚寅','癸未','辛亥','甲午']),
 ((2000,2,29),['庚辰','戊寅','丁巳','丙午']),
 ((2024,2,10),['甲辰','丙寅','甲辰','庚午']),
 ((2100,12,15),['庚申','戊子','辛卯','甲午'])])
def test_cross_checked_pillars(date,expected):
    # Fixtures captured from independent lunar-python comparison.
    y,m,d=date
    r=calculate(B|dict(year=y,month=m,day=d,hour=12),{'time_basis':'civil'}, {})
    assert [p['ganzhi'] for p in r['natal'].values()]==expected

def test_luck_directions_and_month_ends():
    for year in [1999,2000]:
        for sex in ['male','female']:
            r=chart(year=year,month=1,day=31,sex=sex)
            yi=G.index(r['natal']['year']['ganzhi'][0])
            assert r['luck']['forward']==((yi%2==0)==(sex=='male'))
            assert 'analysis' not in r

def test_unknown_rule_and_longitude():
    with pytest.raises(BaziError): calculate(B,{'unknown':True})
    with pytest.raises(BaziError): chart(longitude=181)
