import json, os, hashlib, subprocess, re, sys
from PIL import Image
S=os.environ.get('SCRATCH', '/tmp/wife_doc_scratch')
def pdf(f):
    if f.endswith('.pdf'): return 'sources/'+f
    k=hashlib.md5(f.encode()).hexdigest()[:10]
    return f'{S}/pdfcache/{k}/'+os.path.splitext(os.path.basename(f))[0]+'.pdf'
res={}
for s,y,q,i in json.load(open('tools/h1_manifest.json')):
    out=f'{S}/full/img/{y}_{s}_H1'
    r=subprocess.run(['python3','-I','tools/crop_resources.py',pdf(i),out],capture_output=True,text=True)
    items=[]
    for line in r.stdout.splitlines():
        m=re.match(r'(\S+\.png) \((\d+), (\d+)\) \| (.*)',line.replace(out+'/',''))
        if m: items.append([m.group(1),int(m.group(2)),int(m.group(3)),m.group(4)])
    res[f'{s}_{y}']=items
    if r.returncode: print(s,y,'ERR',r.stderr[-300:])
    small=[(it[0],it[2]) for it in items if it[2]<200]
    tall=[(it[0],it[2]) for it in items if it[2]>3000]
    if small or tall: print(s,y,'small',small,'tall',tall)
json.dump(res,open(f'{S}/full/h1_resources.json','w'),indent=1)
