"""Deterministic calendar facts; no automated fortune interpretation."""
import math
from functools import lru_cache
import json
from importlib.resources import files
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from calendar import monthrange
from importlib.metadata import version
import sxtwl

G='甲乙丙丁戊己庚辛壬癸'; Z='子丑寅卯辰巳午未申酉戌亥'; W='木火土金水'
H=['癸','己癸辛','甲丙戊','乙','戊乙癸','丙戊庚','丁己','己丁乙','庚壬戊','辛','戊辛丁','壬甲']
N='海中金 炉中火 大林木 路旁土 剑锋金 山头火 涧下水 城头土 白蜡金 杨柳木 泉中水 屋上土 霹雳火 松柏木 长流水 沙中金 山下火 平地木 壁上土 金箔金 覆灯火 天河水 大驿土 钗钏金 桑柘木 大溪水 沙中土 天上火 石榴木 大海水'.split()
J='冬至 小寒 大寒 立春 雨水 惊蛰 春分 清明 谷雨 立夏 小满 芒种 夏至 小暑 大暑 立秋 处暑 白露 秋分 寒露 霜降 立冬 小雪 大雪'.split()
DEFAULT={'time_basis':'apparent','year_boundary':'lichun','day_boundary':'midnight','late_zi':'same_day'}
class BaziError(ValueError):
    def __init__(self, code, message, details=None):
        super().__init__(message); self.code=code; self.details=details
    def as_dict(self): return {'code':self.code,'message':str(self),'details':self.details}
def fail(code,msg,details=None): raise BaziError(code,msg,details)
def places(query=''):
    data=json.loads(files('bazi_read').joinpath('data', 'latlng.json').read_text(encoding='utf-8'))
    out=[]
    def walk(n,path):
        p=path+[n['name']]
        if 'lng' in n and (not query or query in '/'.join(p)):
            out.append({'path':'/'.join(p),'longitude':float(n['lng']),'latitude':float(n['lat'])})
        for c in n.get('children',[]): walk(c,p)
    walk(data,[]); return out
def ten(a,b):
    i,j=G.index(a),G.index(b); d=(j//2-i//2)%5; same=i%2==j%2
    return [('比肩','劫财'),('食神','伤官'),('偏财','正财'),('七杀','正官'),('偏印','正印')][d][not same]
def gz(i): return G[i%10]+Z[i%12]
def idx(p): return next(i for i in range(60) if gz(i)==p)
def pillar(p,day):
    i=idx(p); g,z=G.index(p[0]),Z.index(p[1]); start=[11,6,2,9,2,9,5,0,8,3][g]
    stage=(z-start)*(1 if g%2==0 else -1)%12
    return {'ganzhi':p,'stem_element':W[g//2],'stem_polarity':'阳' if g%2==0 else '阴',
      'stem_ten_god':ten(day,p[0]),'hidden':[{'stem':h,'ten_god':ten(day,h)} for h in H[z]],
      'nayin':N[i//2],'void':Z[(10+(i//10)*10)%12]+Z[(11+(i//10)*10)%12],
      'growth_stage':'长生 沐浴 冠带 临官 帝旺 衰 病 死 墓 绝 胎 养'.split()[stage]}
def equation(t):
    jd=(t-datetime(2000,1,1,12,tzinfo=timezone.utc)).total_seconds()/86400+2451545
    c=(jd-2451545)/36525
    l=math.radians((280.46646+c*(36000.76983+0.0003032*c))%360)
    m=math.radians(357.52911+c*(35999.05029-0.0001537*c))
    e=0.016708634-c*(0.000042037+0.0000001267*c)
    eps=math.radians(23+(26+(21.448-c*(46.815+c*(0.00059-c*0.001813)))/60)/60+0.00256*math.cos(math.radians(125.04-1934.136*c)))
    y=math.tan(eps/2)**2
    return 4*math.degrees(y*math.sin(2*l)-2*e*math.sin(m)+4*e*y*math.sin(m)*math.cos(2*l)-0.5*y*y*math.sin(4*l)-1.25*e*e*math.sin(2*m))
@lru_cache(maxsize=512)
def terms(year):
    out={}
    for y in (year-1,year,year+1):
        for v in sxtwl.getJieQiByYear(y):
            d=sxtwl.JD2DD(v.jd)
            t=datetime(d.Y,d.M,d.D,tzinfo=timezone(timedelta(hours=8)))+timedelta(hours=d.h,minutes=d.m,seconds=d.s)
            out[t]= {'name':J[v.jqIndex],'index':v.jqIndex,'utc':t.astimezone(timezone.utc)}
    return sorted(out.values(),key=lambda x:x['utc'])
def normalize(b,r):
    try:
        y,m,d=(int(b[k]) for k in ('year','month','day'))
        if b.get('calendar','solar') not in ('solar','lunar'): fail('CALENDAR','calendar须为solar或lunar')
        if not 1<=m<=12: fail('DATE','月份必须为1—12')
        if b.get('calendar','solar')=='lunar':
            leap=b.get('is_leap_month')
            if leap is not None and not isinstance(leap,bool): fail('LEAP','闰月标识必须为布尔值')
            if leap is None and sxtwl.getRunMonth(y)==m: fail('AMBIGUOUS_LUNAR','同名正常月及闰月并存，请指定is_leap_month')
            if leap and sxtwl.getRunMonth(y)!=m: fail('LEAP','该年不存在所指定闰月')
            if not 1<=m<=12 or not 1<=d<=sxtwl.getLunarMonthNum(y,m,bool(leap)): fail('DATE','农历日期无效')
            v=sxtwl.fromLunar(y,m,d,bool(leap)); y,m,d=v.getSolarYear(),v.getSolarMonth(),v.getSolarDay()
        naive=datetime(y,m,d,int(b['hour']),int(b['minute']),int(b.get('second',0)))
        if not 1900<=y<=2100: fail('RANGE','出生公历年须在1900—2100')
        if 'utc_offset_minutes' in b:
            tz=timezone(timedelta(minutes=float(b['utc_offset_minutes'])))
        else: tz=ZoneInfo(b['timezone'])
        t=naive.replace(tzinfo=tz,fold=int(b.get('fold',0)))
        if t.astimezone(timezone.utc).astimezone(tz).replace(tzinfo=None)!=naive: fail('NONEXISTENT_TIME','该民用时间因夏令时跳变不存在')
        if 'utc_offset_minutes' not in b and 'fold' not in b and naive.replace(tzinfo=tz,fold=0).utcoffset()!=naive.replace(tzinfo=tz,fold=1).utcoffset(): fail('AMBIGUOUS_TIME','重复民用时间，请指定fold')
        lon=b.get('longitude'); source='explicit'
        if lon is None and b.get('place'):
            found=places(b['place']); exact=[p for p in found if p['path']==b['place']]
            if exact: found=exact
            if len(found)!=1: fail('PLACE','地点需要唯一匹配或完整路径',found)
            lon=found[0]['longitude']; source=found[0]['path']
        if lon is None and r['time_basis']!='civil': fail('LONGITUDE','太阳时需要经度或唯一出生地')
        if lon is not None and not -180<=float(lon)<=180: fail('LONGITUDE','经度须在-180至180')
        return t, float(lon) if lon is not None else None,source
    except BaziError: raise
    except (ValueError,KeyError,TypeError) as e: fail('INPUT',str(e))
def relations(ps):
    out=[]; items=list(ps.items())
    for n,(a,p) in enumerate(items):
        for b,q in items[n+1:]:
            x,y=Z.index(p[1]),Z.index(q[1]); pair=''.join(sorted([p[1],q[1]]))
            hits=[]
            if abs(G.index(p[0])-G.index(q[0]))==5: hits.append('天干五合')
            if (x-y)%12==6: hits.append('六冲')
            for label, pairs in [('六合',['子丑','寅亥','卯戌','辰酉','巳申','午未']),('六害',['子未','丑午','寅巳','卯辰','申亥','酉戌']),('六破',['子酉','卯午','辰丑','未戌','寅亥','巳申']),('刑',['子卯','寅巳','巳申','申寅','丑戌','戌未','未丑'])]:
                if pair in [''.join(sorted(v)) for v in pairs]: hits.append(label)
            if x==y and p[1] in '辰午酉亥': hits.append('自刑')
            ai,bi=G.index(p[0])//2,G.index(q[0])//2
            hits.append('天干'+('同类' if ai==bi else '前生后' if (bi-ai)%5==1 else '后生前' if (ai-bi)%5==1 else '前克后' if (bi-ai)%5==2 else '后克前'))
            out.extend({'type':h,'positions':[a,b],'rule_id':'REL-01'} for h in hits)
    from itertools import combinations
    for combo in combinations(items,3):
        zs={p[1] for _,p in combo}
        for typ,groups in [('三合',['申子辰','亥卯未','寅午戌','巳酉丑']),('三会',['寅卯辰','巳午未','申酉戌','亥子丑'])]:
            if zs in [set(g) for g in groups]: out.append({'type':typ,'positions':[k for k,_ in combo],'rule_id':'REL-01'})
    return out

def _facts(birth,rules=None,options=None):
    r=DEFAULT| (rules or {}); o=options or {}
    for k,allowed in {'time_basis':['apparent','mean','civil'],'year_boundary':['lichun','spring_festival'],'day_boundary':['midnight','zi_start'],'late_zi':['same_day','next_day']}.items():
        if r[k] not in allowed: fail('RULE',f'{k}无效')
    if set(r)-set(DEFAULT): fail('RULE','存在未知规则')
    t,lon,ls=normalize(birth,r); utc=t.astimezone(timezone.utc); eot=equation(utc)
    mean=utc.replace(tzinfo=None)+timedelta(minutes=4*(lon or 0)); apparent=mean+timedelta(minutes=eot)
    clock={'civil':t.replace(tzinfo=None),'mean':mean,'apparent':apparent}[r['time_basis']]
    ts=terms(utc.year); before=[v for v in ts if v['utc']<=utc]; after=[v for v in ts if v['utc']>utc]
    jie_before=[v for v in before if v['index']%2==1][-1]; jie_after=[v for v in after if v['index']%2==1][0]
    lichun=[v for v in before if v['index']==3][-1]; yy=lichun['utc'].astimezone(timezone(timedelta(hours=8))).year
    solar_yi=(yy-4)%60
    if r['year_boundary']=='spring_festival':
        c=utc.astimezone(timezone(timedelta(hours=8))); yy=sxtwl.fromSolar(c.year,c.month,c.day).getLunarYear()
    yi=(yy-4)%60; mi=((jie_before['index']-3)//2)%12
    month=G[((solar_yi%10)%5*2+2+mi)%10]+Z[(mi+2)%12]
    date=clock+timedelta(days=int(r['day_boundary']=='zi_start' and clock.hour>=23))
    dg=sxtwl.fromSolar(date.year,date.month,date.day).getDayGZ(); day=G[dg.tg]+Z[dg.dz]
    hg=(dg.tg+int(r['day_boundary']=='midnight' and clock.hour==23 and r['late_zi']=='next_day'))%10
    hz=((clock.hour+1)//2)%12; hour=G[(hg%5*2+hz)%10]+Z[hz]
    ps=dict(zip(['year','month','day','hour'],[gz(yi),month,day,hour])); natal={k:pillar(p,day[0]) for k,p in ps.items()}; natal['day']['stem_ten_god']='日主'
    gender=birth.get('sex')
    if gender not in ('male','female'): fail('SEX','sex须为male或female（用于传统顺逆规则）')
    forward=(yi%2==0)==(gender=='male'); edge=jie_after if forward else jie_before
    delta=abs((edge['utc']-utc).total_seconds()); age_seconds=delta*120
    years,rem=divmod(age_seconds,360*86400); months,rem=divmod(rem,30*86400); days,rem=divmod(rem,86400)
    month_abs=t.year*12+t.month-1+int(years)*12+int(months); sy,sm=divmod(month_abs,12); sm+=1
    start=t.replace(year=sy,month=sm,day=min(t.day,monthrange(sy,sm)[1]))+timedelta(days=days,seconds=rem)
    count=34  # Covers analysis years through 2220, independently of overview size.
    luck=[]
    for i in range(count):
        p=gz(idx(month)+(i+1)*(1 if forward else -1)); year=start.year+10*i
        luck.append({'index':i+1,'start':start.replace(year=year,day=min(start.day,monthrange(year,start.month)[1])).isoformat(),'end':start.replace(year=year+10,day=min(start.day,monthrange(year+10,start.month)[1])).isoformat(),'pillar':pillar(p,day[0])})
    cday=sxtwl.fromSolar(t.year,t.month,t.day)
    aux={'fetal_month_formula':gz(0), 'fetal_300_days':None,'life_palace':None}
    fg=G[(G.index(month[0])+1)%10]+Z[(Z.index(month[1])+3)%12]; aux['fetal_month_formula']={'ganzhi':fg,'rule_id':'AUX-01'}
    prior=clock-timedelta(days=300); pg=sxtwl.fromSolar(prior.year,prior.month,prior.day).getDayGZ()
    aux['fetal_300_days']={'date':prior.date().isoformat(),'ganzhi':G[pg.tg]+Z[pg.dz],'rule_id':'AUX-02'}
    lm=cday.getLunarMonth(); palace=(4-lm-hz)%12
    aux['life_palace']={'ganzhi':G[(yi%10%5*2+2+(palace-2)%12)%10]+Z[palace],'month_basis':'civil_date_chinese_lunar_month','rule_id':'AUX-03'}
    aux['stars']=stars(ps)
    warnings=[]
    distance=min(abs((v['utc']-utc).total_seconds()) for v in ts)
    if distance<60 or min(clock.minute*60+clock.second,3600-clock.minute*60-clock.second)<60: warnings.append('BOUNDARY_SENSITIVE：靠近节气或整点，请核对记录及计算精度')
    def event(v): return {'name':v['name'],'utc':v['utc'].isoformat(),'distance_seconds':(v['utc']-utc).total_seconds()}
    return {'dependencies':{k:version(k) for k in ['sxtwl','tzdata']},'input':birth,'rules':r,
      'time':{'civil':t.isoformat(),'utc':utc.isoformat(),'mean_solar':mean.isoformat() if lon is not None else None,'apparent_solar':apparent.isoformat() if lon is not None else None,'selected_clock':clock.isoformat(),'longitude':lon,'longitude_source':ls,'equation_minutes':eot,'longitude_from_utc_minutes':4*lon if lon is not None else None,'lunar':{'year':cday.getLunarYear(),'month':lm,'day':cday.getLunarDay(),'is_leap_month':cday.isLunarLeap()}},
      'natal':natal,'season':{'previous_term':event(before[-1]),'next_term':event(after[0]),'previous_jie':event(jie_before),'next_jie':event(jie_after),'elapsed_since_jie_seconds':(utc-jie_before['utc']).total_seconds()},
      'relations':relations(ps),'luck':{'forward':forward,'reference_jie':event(edge),'conversion_convention':'3 elapsed days = 1 symbolic year (360 days); Gregorian calendar addition','interval_seconds':delta,'starting_age':{'years':int(years),'months':int(months),'days':int(days),'seconds':rem},'start':start.isoformat(),'periods':luck},
      'auxiliary':aux,'warnings':warnings}
def monthly(year,day):
    # Twelve solar months of the lichun year, including next January.
    tt=[v for v in terms(year) if v['index']%2]
    lc=next(i for i,v in enumerate(tt) if v['index']==3 and v['utc'].year==year)
    out=[]
    for n in range(12):
        v,w=tt[lc+n:lc+n+2]
        p=G[((year-4)%10%5*2+2+n)%10]+Z[(n+2)%12]
        out.append({'start':v['utc'].isoformat(),'end':w['utc'].isoformat(),'pillar':pillar(p,day)})
    return out

def stars(ps):
    out=[]
    def add(name,targets,reference,scope='branch'):
        for k,p in ps.items():
            if p[1 if scope=='branch' else 0] in targets:
                out.append({'name':name,'position':k,'reference':reference,'targets':targets,'rule_id':'STAR-'+name,'status':'traditional_table_pending_scan_collation'})
    g=G.index(ps['day'][0]); m=Z.index(ps['month'][1])
    add('天乙贵人',['丑未','子申','亥酉','亥酉','丑未','子申','丑未','寅午','卯巳','卯巳'][g],'day.stem')
    add('禄','寅卯巳午巳午申酉亥子'[g],'day.stem')
    # Only yang-stem blades in this profile; yin-stem variants require a separate source.
    if g%2==0: add('羊刃','卯午午酉子'[g//2],'day.stem')
    add('文昌','巳午申酉申酉亥子寅卯'[g],'day.stem')
    add('月德','壬庚丙甲'[m%4],'month.branch','stem')
    td=['巳','庚','丁','申','壬','辛','亥','甲','癸','寅','丙','乙'][m]
    add('天德',td,'month.branch','branch' if td in Z else 'stem')
    for ref in ['year','day']:
        group=Z.index(ps[ref][1])%4
        for name,table in [('驿马','寅亥申巳'),('桃花','酉午卯子'),('华盖','辰丑戌未'),('将星','子酉午卯')]:
            add(name,table[group],ref+'.branch')
    return out


def _core_pillar(p):
    z = Z.index(p['ganzhi'][1])
    return {k: v for k, v in p.items() if k not in ('nayin', 'void', 'growth_stage')} | {
        'branch_element': '水土木木土火火土金金土水'[z],
        'branch_polarity': '阳' if z % 2 == 0 else '阴',
    }


def _growth(stem, branch):
    g, z = G.index(stem), Z.index(branch)
    start = [11, 6, 2, 9, 2, 9, 5, 0, 8, 3][g]
    return '长生 沐浴 冠带 临官 帝旺 衰 病 死 墓 绝 胎 养'.split()[((z-start)*(1 if g%2==0 else -1))%12]


def _incremental(ps, added):
    return [v for v in relations(ps) if any(k in added for k in v['positions'])]


def _intervals(start, end, periods):
    # All intervals are half-open and compared as absolute instants.
    cuts = {start, end}
    for p in periods:
        for key in ('start', 'end'):
            t = datetime.fromisoformat(p[key])
            if start < t < end:
                cuts.add(t)
    cuts = sorted(cuts)
    for a, b in zip(cuts, cuts[1:]):
        active = next((p for p in periods if datetime.fromisoformat(p['start']) <= a < datetime.fromisoformat(p['end'])), None)
        yield a, b, active


def calculate(birth, rules=None, options=None):
    if options is not None and not isinstance(options, dict):
        fail('OPTIONS', 'options必须为对象')
    o = options or {}
    allowed = {'luck_count', 'analysis_year', 'include_monthly', 'include_auxiliary', 'include_trace'}
    if not isinstance(o, dict) or set(o)-allowed:
        fail('OPTIONS', '未知或已移除的输出选项（year_count已移除）')
    for key in ('include_monthly', 'include_auxiliary', 'include_trace'):
        if key in o and not isinstance(o[key], bool):
            fail('OPTIONS', key+'必须为布尔值')
    count = o.get('luck_count', 10)
    target = o.get('analysis_year')
    if isinstance(count, bool) or not isinstance(count, int) or not 1 <= count <= 12:
        fail('OPTIONS', 'luck_count须为1—12的整数')
    if 'analysis_year' in o and (isinstance(target, bool) or not isinstance(target, int) or not 1900 <= target <= 2220):
        fail('OPTIONS', 'analysis_year须为1900—2220的整数')
    if o.get('include_monthly') and target is None:
        fail('OPTIONS', '展开流月需要analysis_year')
    raw = _facts(birth, rules, o)
    ps = {k: p['ganzhi'] for k, p in raw['natal'].items()}
    day = ps['day'][0]
    periods = raw['luck']['periods']
    compact_periods = [{k: p[k] for k in ('index', 'start', 'end')} | {
        'ganzhi': p['pillar']['ganzhi'], 'stem_ten_god': p['pillar']['stem_ten_god']
    } for p in periods]
    result = {
        'schema_version': '2.0', 'engine_version': '0.2.0',
        'input': raw['input'], 'rules': raw['rules'],
        'time': {k: raw['time'][k] for k in ('civil', 'selected_clock', 'longitude', 'lunar')},
        'natal': {k: _core_pillar(p) for k, p in raw['natal'].items()},
        'season': {k: raw['season'][k] for k in ('previous_jie', 'next_jie', 'elapsed_since_jie_seconds')},
        'relations': raw['relations'],
        'luck': {k: raw['luck'][k] for k in ('forward', 'starting_age', 'start')} | {'periods': compact_periods[:count]},
        'warnings': raw['warnings'],
    }
    if target is not None:
        tt = terms(target)
        start = next(v['utc'] for v in tt if v['index']==3 and v['utc'].year==target)
        end = next(v['utc'] for v in tt if v['index']==3 and v['utc'].year==target+1)
        annual = gz(target-4)
        def segments(a, b, month=None):
            out = []
            for left, right, active in _intervals(a, b, compact_periods):
                context = ps | {'annual': annual}
                if active:
                    context['luck'] = active['ganzhi']
                if month:
                    context['monthly'] = month
                added = {'monthly'} if month else {'luck', 'annual'}
                out.append({'start': left.isoformat(), 'end': right.isoformat(),
                            'luck': active, 'relations': _incremental(context, added)})
            return out
        analysis = {'year': target, 'year_boundary': 'lichun', 'start': start.isoformat(),
                    'end': end.isoformat(), 'annual': _core_pillar(pillar(annual, day)),
                    'periods': segments(start, end)}
        if o.get('include_monthly'):
            months = monthly(target, day)
            analysis['monthly'] = [
                {'start': m['start'], 'end': m['end'], 'pillar': _core_pillar(m['pillar']),
                 'periods': segments(datetime.fromisoformat(m['start']), datetime.fromisoformat(m['end']), m['pillar']['ganzhi'])}
                for m in months
            ]
        result['analysis'] = analysis
    if o.get('include_auxiliary'):
        result['auxiliary'] = raw['auxiliary'] | {
            'pillars': {k: {'nayin': p['nayin'],
                'void': {'reference': k, 'branches': p['void']},
                'day_master_growth': {'reference': 'day.stem', 'stage': _growth(day, p['ganzhi'][1])},
                'self_stem_growth': {'reference': k+'.stem', 'stage': p['growth_stage']}}
                for k, p in raw['natal'].items()}}
    if o.get('include_trace'):
        result['trace'] = {'dependencies': raw['dependencies'], 'time': raw['time'],
                           'season': raw['season'],
                           'luck': {k: raw['luck'][k] for k in ('reference_jie', 'conversion_convention', 'interval_seconds')}}
    return result


def compare(birth, profiles=None, options=None):
    profiles = profiles or {f'{basis}/{boundary}': {'time_basis': basis, 'day_boundary': boundary}
                           for basis in ['apparent', 'mean', 'civil'] for boundary in ['midnight', 'zi_start']}
    result = {name: calculate(birth, r, options) for name, r in profiles.items()}
    first = next(iter(result.values()))
    return {'profiles': result, 'differences': {name: [k for k in first['natal'] if first['natal'][k]!=v['natal'][k]] for name, v in result.items()}}
