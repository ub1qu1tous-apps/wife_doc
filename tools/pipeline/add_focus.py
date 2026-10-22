"""Merge focus lines (lines 'KEY | text' on stdin) into tools/data/focus_lines.json; keys must be real grid cells.

usage: python3 tools/pipeline/add_focus.py <questions.json> < lines.txt
"""
import json, sys
cells = {f"{q['school']}_{q['year']}_{q['level']}_{q['slot']}" for q in json.load(open(sys.argv[1]))}
path = 'tools/data/focus_lines.json'
d = json.load(open(path, encoding='utf8'))
n = 0
for line in sys.stdin:
    if not line.strip():
        continue
    k, v = (x.strip() for x in line.split('|', 1))
    if k not in cells:
        sys.exit(f'unknown cell: {k}')
    if len(v) > 48:
        print(f'long ({len(v)}): {k} | {v}')
    d[k] = v
    n += 1
json.dump(d, open(path, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
print(n, 'added;', len(d) - 1, 'of', len(cells), 'cells have a focus line')
