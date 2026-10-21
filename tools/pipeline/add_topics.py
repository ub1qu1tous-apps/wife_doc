"""Append 'Syllabus topics:' lines to 2024 notes. usage: add_topics.py <labels.json>
labels.json: {"SCHOOL": {"H1": "...", "H2P1": "...", "H2P2": "..."}}"""
import json, re, sys
L = json.load(open(sys.argv[1]))
for school, papers in L.items():
    p = f'/home/user/wife_doc/notes/2024/{school}.md'
    lines = open(p, encoding='utf8').read().split('\n')
    lines = [l for l in lines if not l.startswith('Syllabus topics:')]
    starts = [i for i, l in enumerate(lines) if l.startswith('## ')] + [len(lines)]
    out, done = lines[:starts[0]], set()
    for a, b in zip(starts, starts[1:]):
        sec = lines[a:b]
        h = sec[0][3:].lower()
        key = 'H1' if h.startswith('h1') else 'H2P1' if re.match(r'h2 (paper|p) ?1', h) else 'H2P2' if re.match(r'h2 (paper|p) ?2', h) else None
        while sec and sec[-1].strip() == '':
            sec.pop()
        if key in papers:
            sec.append('Syllabus topics: ' + papers[key])
            done.add(key)
        out += sec + ['']
    missing = set(papers) - done
    if missing:
        print('MISSING', school, missing)
    open(p, 'w', encoding='utf8').write('\n'.join(out).rstrip('\n') + '\n')
print('ok')
