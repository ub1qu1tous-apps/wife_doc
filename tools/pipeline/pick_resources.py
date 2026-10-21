"""Pick each question's resources from its wording and check the crops exist.

usage: SCRATCH=... python3 tools/pipeline/pick_resources.py <q_spec.json> <level-tag e.g. H1 | H2P1 | H2P2>
Prints questions whose referenced resources have no crop; writes <q_spec>_res.json {key: [img paths]}.
"""
import json, os, sys
sys.path.insert(0, 'tools')
from resource_refs import refs

S = os.environ.get('SCRATCH', '/tmp/wife_doc_scratch')
qfile, tag = sys.argv[1], sys.argv[2]
qs = json.load(open(qfile))
out, missing = {}, 0
for k, r in qs.items():
    school, year = k.split('_')[:2]
    d = f'{S}/full/img/{year}_{school}_{tag}'
    files = os.listdir(d) if os.path.isdir(d) else []
    have = sorted(f[1:-4] for f in files if f.endswith('.png'))
    alias = {f[1:-6]: open(f'{d}/{f}').read()[1:] for f in files if f.endswith('.alias')}   # 'Resources 7A and 7B' = one crop
    text = ' '.join(r['stem'] + [t for _, t, _ in r['parts']])
    want = []
    for x in refs(text):
        if x in have or x in alias:
            want.append(alias.get(x, x))
        elif x.isdigit() and any(h.startswith(x) and h[len(x):].isalpha() for h in have):   # 'Resource 4' -> 4A, 4B
            want += [h for h in have if h.startswith(x) and h[len(x):].isalpha()]
        elif x[-1].isalpha() and x[:-1] in have:   # question says 2A/2B, Insert has one 'Resource 2' with both parts
            want.append(x[:-1])
        else:
            print(f'{k}: no crop for R{x} (have {have})'); missing += 1
    out[k] = [f'img/{year}_{school}_{tag}/R{x}.png' for x in dict.fromkeys(want)]
json.dump(out, open(qfile.replace('.json', '_res.json'), 'w'), indent=1)
print(len(out), 'questions,', sum(map(len, out.values())), 'resources,', missing, 'missing')
