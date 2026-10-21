"""Collect the per-question syllabus topics from notes/<year>/<SCHOOL>.md.

Each paper section ("## H1 Paper 1 ...", "## H2 Paper 1 ...", "## H2 Paper 2 ...") ends with
"Syllabus topics: Q1 <label> | Q2 <label> | ...". Prints JSON: one record per question.
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AREAS = [('other', 'Others'), ('elderly', 'Elderly needs'), ('flood', 'Fluvial flood risk'),
         ('cc response', 'Community response to CC'), ('climate', 'Community response to CC')]


def paper_of(heading):
    h = heading.lower()
    if h.startswith('h1'):
        return 'H1', ''
    if re.match(r'h2 paper 1|h2 p1', h):
        return 'H2', 'P1 '
    if re.match(r'h2 paper 2|h2 p2', h):
        return 'H2', 'P2 '
    return None, None


def parse(path):
    year = int(os.path.basename(os.path.dirname(path)))
    school = os.path.splitext(os.path.basename(path))[0]
    out, level, prefix = [], None, None
    for line in open(path, encoding='utf8'):
        if line.startswith('## '):
            level, prefix = paper_of(line[3:].strip())
        elif line.startswith('Syllabus topics:') and level:
            for slot in line.split(':', 1)[1].strip().rstrip('.').split(' | '):
                m = re.match(r'\s*Q(\d)\s+(.*)', slot)
                if not m:
                    print(f'?? {path}: {slot!r}', file=sys.stderr)
                    continue
                qn, label = m.groups()
                rec = dict(school=school, year=year, level=level, slot=f'{prefix}Q{qn}')
                if label.lower().startswith('fieldwork'):
                    area = (label.split('–', 1)[-1] if '–' in label else label).split('(')[0].lower()
                    rec['fieldwork_area'] = next(name for key, name in AREAS if key in area) \
                        if any(k in area for k, _ in AREAS) else '??' + label
                    rec['topics'] = ['2' if level == 'H1' else '4']
                else:
                    rec['topics'] = list(dict.fromkeys(re.findall(r'\b\d\.\d\.\d\b', label)))
                    if not rec['topics']:
                        print(f'?? no code {path}: {slot!r}', file=sys.stderr)
                out.append(rec)
    return out


if __name__ == '__main__':
    recs = [r for p in sorted(glob.glob(os.path.join(ROOT, 'notes', '20*', '*.md'))) for r in parse(p)]
    json.dump(recs, sys.stdout, indent=1, ensure_ascii=False)
