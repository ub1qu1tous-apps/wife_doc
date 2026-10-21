import os,re,sys,collections
SP=os.environ.get('SCRATCH', '/tmp/wife_doc_scratch')
T=SP+'/text/'
files=[l.rstrip('\n') for l in open(SP+'/src.txt')]
groups=collections.defaultdict(list)
for f in files:
    p=f.split('/')
    year=p[0][-4:]
    if p[0].endswith('2024') and len(p)==2: school='_USER'
    elif year=='2025': school=p[2]
    else: school=p[1]
    school=school.replace(' (Ans)','')
    groups[(year,school)].append(f)
def norm(f):
    b=os.path.basename(f).lower()
    b=re.sub(r'\.(pdf|docx|doc)$','',b)
    b=re.sub(r'\(?\s*(for )?sharing\s*\)?','',b)
    b=re.sub(r'[^a-z0-9]','',b)
    return b
os.makedirs(SP+'/bundles',exist_ok=True)
rep=[]
for (y,s),fs in sorted(groups.items()):
    seen={}
    keep=[];skip=[]
    for f in sorted(fs, key=lambda f:(0 if f.endswith('.docx') else 1 if f.endswith('.pdf') else 2, f)):
        k=norm(f)
        if k in seen: skip.append(f); continue
        seen[k]=f; keep.append(f)
    out=[]
    for f in sorted(keep):
        tp=T+f+'.txt'
        if not os.path.exists(tp): out.append(f'\n===== FILE: {f} =====\n[NO TEXT EXTRACTED]\n'); continue
        t=open(tp,errors='replace').read()
        t=re.sub(r'[ \t]{3,}','  ',t); t=re.sub(r'\n\s*\n+','\n\n',t)
        out.append(f'\n===== FILE: {f} =====\n'+t)
    txt=''.join(out)
    open(f'{SP}/bundles/{y}_{s}.txt','w').write(txt)
    rep.append(f'{y} {s}: keep {len(keep)} skip {len(skip)} words {len(txt.split())}' + (' SKIPPED: '+'; '.join(os.path.basename(x) for x in skip) if skip else ''))
print('\n'.join(rep))
