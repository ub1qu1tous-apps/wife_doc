"""Compare extracted questions with the reading notes: part labels and marks per question.

usage: python3 tools/pipeline/check_vs_notes.py <q_spec.json>
Notes list each part as '- (a) ... [n]' under a '**Qn ...' line inside '## H1 ...' / '## H2 Paper 1 ...' sections.
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parse_notes import paper_of


def note_parts():
    out = {}
    for p in glob.glob('notes/20*/*.md'):
        year, school = p.split('/')[1], os.path.splitext(os.path.basename(p))[0]
        level = prefix = q = None
        for line in open(p, encoding='utf8'):
            if line.startswith('## '):
                level, prefix = paper_of(line[3:].strip())
                q = None
            m = re.match(r'\s*(?:\*\*|- )?(?:Sec [A-D] )?Q(\d)\b', line)
            if level and m:
                q = f'{school}_{year}_{prefix}Q{m.group(1)}'
                out.setdefault(q, [])
                mk = re.search(r'\[(\d{1,2})\]', line)
                if not line.lstrip().startswith('**') and mk:   # one-line essay entry
                    out[q].append(('', int(mk.group(1))))
                continue
            m = re.match(r'\s*- \(([a-h])\)(?:\s*\(?([ivx]+)\)?)?.*?\[(\d{1,2})\]', line)
            if level and q and m:
                out[q].append((m.group(1), int(m.group(3))))
    return out


if __name__ == '__main__':
    qs = json.load(open(sys.argv[1]))
    notes = note_parts()
    bad = 0
    for k, r in qs.items():
        mine = [(l[1], m) for l, _, m in r['parts']]
        theirs = notes.get(k)
        if theirs is None:
            print(f'{k}: not in notes'); bad += 1; continue
        if [x for x in theirs if x[0]] != mine and not (not mine and len(theirs) <= 1):
            print(f'{k}: QP {mine}  notes {theirs}'); bad += 1
    print(f'{len(qs)} checked, {bad} differ')
