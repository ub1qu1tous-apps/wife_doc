import json, os, hashlib, sys
sys.path.insert(0,'tools')
import importlib, extract_questions; importlib.reload(extract_questions)
from extract_questions import extract
S=os.environ.get('SCRATCH', '/tmp/wife_doc_scratch')
def pdf(f):
    if f.endswith('.pdf'): return 'sources/'+f
    k=hashlib.md5(f.encode()).hexdigest()[:10]
    return f'{S}/pdfcache/{k}/'+os.path.splitext(os.path.basename(f))[0]+'.pdf'
out={}
only=sys.argv[1:]
for s,y,q,i in json.load(open('tools/h1_manifest.json')):
    if only and f'{s}_{y}' not in only: continue
    try:
        r=extract(pdf(q),1,'A')
        tot=sum(m or 0 for _,_,m in r['parts'])
        labels=''.join(l[1] for l,_,_ in r['parts'])
        ok= tot==30 and labels=='abcdefgh'[:len(labels)] and all(m for _,_,m in r['parts'])
        if not ok or only:
            print(f"{s} {y}: parts={labels} marks={[m for *_,m in r['parts']]} {'' if ok else '<<<'}")
        out[f'{s}_{y}']=r
    except Exception as e:
        print(f'{s} {y}: ERROR {e!r}')
if not only: json.dump(out,open(f'{S}/h1_q1.json','w'),indent=1,ensure_ascii=False)
