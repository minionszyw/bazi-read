import argparse
import json
import sys
from .engine import calculate, compare, places, BaziError

def main():
    p=argparse.ArgumentParser(); s=p.add_subparsers(dest='command',required=True)
    for name in ['chart','compare']:
        q=s.add_parser(name); q.add_argument('--input',required=True)
    s.add_parser('places').add_argument('query',nargs='?',default='')
    a=p.parse_args()
    try:
        if a.command=='places': result=places(a.query)
        else:
            with open(a.input) as f: data=json.load(f)
            birth=data.get('birth',data)
            result=calculate(birth,data.get('rules'),data.get('options')) if a.command=='chart' else compare(birth,data.get('profiles'),data.get('options'))
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (BaziError,ValueError,OSError) as e:
        print(json.dumps({'error':e.as_dict() if isinstance(e,BaziError) else {'code':'INPUT','message':str(e)}},ensure_ascii=False),file=sys.stderr); sys.exit(2)
if __name__=='__main__': main()
