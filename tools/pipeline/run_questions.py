"""Extract question wording for a set of slots from every QP in a manifest, and check it.

usage: SCRATCH=... python3 tools/pipeline/run_questions.py <spec> [SCHOOL_YEAR ...]
spec = h1b (H1 Q2-Q3, Sec B), h1c (H1 Q4-Q6, Sec C), h2p1a, h2p1b, h2p2a, h2p2b, h2p2c
Writes $SCRATCH/q_<spec>.json: {"SCHOOL_YEAR_SLOT": extract() result}.
"""
import hashlib, json, os, sys
sys.path.insert(0, 'tools')
from extract_questions import extract

S = os.environ.get('SCRATCH', '/tmp/wife_doc_scratch')
SPECS = {  # manifest, QP column, section, question numbers, slot prefix, expected marks per question
    'h1b': ('h1', 2, 'B', (2, 3), '', 22),
    'h1c': ('h1', 2, 'C', (4, 5, 6), '', None),
    'h2p1a': ('h2', 2, 'A', (1, 2), 'P1 ', 30),
    'h2p1b': ('h2', 2, 'B', (3, 4, 5, 6), 'P1 ', None),
    'h2p2a': ('h2', 4, 'A', (1,), 'P2 ', 30),
    'h2p2b': ('h2', 4, 'B', (2,), 'P2 ', 30),
    'h2p2c': ('h2', 4, 'C', (3, 4), 'P2 ', None),
}


def pdf(f):
    if f.endswith('.pdf'):
        return 'sources/' + f
    k = hashlib.md5(f.encode()).hexdigest()[:10]
    return f'{S}/pdfcache/{k}/' + os.path.splitext(os.path.basename(f))[0] + '.pdf'


if __name__ == '__main__':
    spec, only = sys.argv[1], sys.argv[2:]
    man, col, sec, qnos, prefix, total = SPECS[spec]
    out = {}
    for row in json.load(open(f'tools/{man}_manifest.json')):
        s, y = row[0], row[1]
        if only and f'{s}_{y}' not in only:
            continue
        for qno in qnos:
            key = f'{s}_{y}_{prefix}Q{qno}'
            try:
                r = extract(pdf(row[col]), qno, sec)
            except Exception as e:
                print(f'{key}: ERROR {e!r}')
                continue
            marks = [m for *_, m in r['parts']]
            labels = ''.join(l[1] for l, _, _ in r['parts'])
            text = ' '.join(r['stem'] + [t for _, t, _ in r['parts']])
            probs = []
            if labels != 'abcdefgh'[:len(labels)]:
                probs.append(f'labels={labels}')
            if r['parts'] and not all(marks):
                probs.append(f'marks={marks}')
            if total and sum(m or 0 for m in marks) != total:
                probs.append(f'sum={sum(m or 0 for m in marks)}')
            if '[' in text:
                probs.append('[ in text')
            if probs or only:
                print(f'{key}: {" ".join(probs)} | {text[:90]!r} ... {text[-60:]!r}')
            out[key] = r
    if not only:
        json.dump(out, open(f'{S}/q_{spec}.json', 'w'), indent=1, ensure_ascii=False)
        print(len(out), 'questions')
