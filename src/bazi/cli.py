import argparse
import json
import sys
from .engine import calculate, compare, places, BaziError

def markdown(r):
    if 'profiles' in r:
        return '\n\n'.join('## '+k+'\n\n'+markdown(v) for k,v in r['profiles'].items())
    lines=['# 八字静态排盘','', '规则：'+json.dumps(r['rules'],ensure_ascii=False),'', '|柱|干支|十神|藏干（十神）|纳音|旬空|十二长生|','|---|---|---|---|---|---|---|']
    for k,p in r['natal'].items():
        lines.append('|'+ '|'.join([k,p['ganzhi'],p['stem_ten_god'],'、'.join(h['stem']+'（'+h['ten_god']+'）' for h in p['hidden']),p['nayin'],p['void'],p['growth_stage']])+'|')
    lines+=['','## 时间与节令','', '```json',json.dumps({'time':r['time'],'season':r['season']},ensure_ascii=False,indent=2),'```','','## 大运','', '起运：'+r['luck']['start']+'；折算年龄：'+str(r['luck']['starting_age']),'']
    lines+=['- '+v['start']+'：'+v['pillar']['ganzhi'] for v in r['luck']['periods']]
    for title,key in [('干支关系','relations'),('辅助表','auxiliary'),('流年','annual'),('流月','monthly'),('提示','warnings')]:
        lines+=['','## '+title,'','```json',json.dumps(r[key],ensure_ascii=False,indent=2),'```']
    return '\n'.join(lines)+'\n'
def main():
    p=argparse.ArgumentParser(); s=p.add_subparsers(dest='command',required=True)
    for name in ['chart','compare']:
        q=s.add_parser(name); q.add_argument('--input',required=True); q.add_argument('--format',choices=['json','markdown'],default='json')
    s.add_parser('places').add_argument('query',nargs='?',default='')
    a=p.parse_args()
    try:
        if a.command=='places': result=places(a.query)
        else:
            with open(a.input) as f: data=json.load(f)
            birth=data.get('birth',data)
            result=calculate(birth,data.get('rules'),data.get('options')) if a.command=='chart' else compare(birth,data.get('profiles'))
        print(markdown(result) if getattr(a,'format','json')=='markdown' else json.dumps(result,ensure_ascii=False,indent=2))
    except (BaziError,ValueError,OSError) as e:
        print(json.dumps({'error':e.as_dict() if isinstance(e,BaziError) else {'code':'INPUT','message':str(e)}},ensure_ascii=False),file=sys.stderr); sys.exit(2)
if __name__=='__main__': main()
