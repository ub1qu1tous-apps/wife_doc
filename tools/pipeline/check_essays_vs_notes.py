"""Compare extracted essay wording with the notes' wording ('- Q4 <wording> [13] – answer notes').

usage: python3 tools/pipeline/check_essays_vs_notes.py <q_spec.json>   (prints essays whose wording differs)
"""
import difflib, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parse_notes import paper_of


def norm(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'[^a-z0-9]+', ' ', t.lower()).strip()


notes = {}
for p in glob.glob('notes/20*/*.md'):
    year, school = p.split('/')[1], os.path.splitext(os.path.basename(p))[0]
    level = prefix = None
    for line in open(p, encoding='utf8'):
        if line.startswith('## '):
            level, prefix = paper_of(line[3:].strip())
        m = re.match(r'\s*- \*{0,2}Q(\d)\*{0,2}\.?\s+(.*)', line)
        if level and m:
            text = re.split(r'\s\[\d{1,2}\]|\s[–—]\s', m.group(2))[0]
            notes[f'{school}_{year}_{prefix}Q{m.group(1)}'] = text
qs = json.load(open(sys.argv[1]))
low = 0
for k, r in qs.items():
    mine = ' '.join(r['stem'])
    theirs = notes.get(k)
    if theirs is None:
        print(f'{k}: not in notes'); low += 1; continue
    ratio = difflib.SequenceMatcher(None, norm(mine), norm(theirs)).ratio()
    if ratio < float(os.environ.get("MIN_RATIO", 0.85)):
        low += 1
        print(f'{k}: {ratio:.2f}\n   QP:    {mine[:200]}\n   notes: {theirs[:200]}')
print(f'{len(qs)} checked, {low} differ')
