"""Print, for each doc 1 grid cell still without a focus line, its key and the question's title line from the notes.

usage: python3 tools/pipeline/focus_sources.py <year> [width]
Keys match tools/data/focus_lines.json: SCHOOL_YEAR_LEVEL_SLOT (slot 'Q2' for H1, 'P1 Q2' for H2).
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parse_notes import paper_of

year, width = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 230
have = json.load(open('tools/data/focus_lines.json'))
for p in sorted(glob.glob(f'notes/{year}/*.md')):
    school = os.path.splitext(os.path.basename(p))[0]
    level = prefix = None
    for line in open(p, encoding='utf8'):
        if line.startswith('## '):
            level, prefix = paper_of(line[3:].strip())
            continue
        m = re.match(r'\s*(?:\*\*|- \*{0,2})(?:Sec [A-D] )?Q(\d)\b\*{0,2}\.?\s*(.*)', line)
        if level and m:
            key = f'{school}_{year}_{level}_{prefix}Q{m.group(1)}'
            if key not in have:
                text = re.sub(r'\*\*', '', m.group(2)).strip()
                print(f'{key} | {text[:width]}')
