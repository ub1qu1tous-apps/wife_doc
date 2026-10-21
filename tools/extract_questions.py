"""Extract the wording of one question from a question-paper PDF.

extract(pdf, qno, section) -> {'section': str, 'stem': [paragraphs], 'parts': [(label, text, marks)]}
Works on `pdftotext -layout` output: the question starts at the line numbered `qno` after the
section heading and ends at the next section heading or question number.
"""
import re, subprocess

FOOTER = re.compile(r'(©|geography prelim|\b20\d\d\s+JC\d\b|\[?\s*turn over|8834|9173|preliminary exam|prelim(inary)? examination|'
                    r'^\s*\d{1,2}\s*$|^\s*page \d+|this document consists|blank page)', re.I)
PART = re.compile(r'^(?:\(([a-h])\)?|([a-h])\))\s+(.*)$')  # (a) / a) / '(b' with ')' wrapped to next line
MARKS = re.compile(r'\[\s*(\d{1,2})\s*(?:marks?)?\s*\]\s*$', re.I)


def pdf_lines(pdf):
    txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    return txt.replace('\f', '\n').split('\n')


def extract(pdf, qno, section_name):
    lines = pdf_lines(pdf)
    # locate the section heading ("Section A" on its own line)
    sec_i = next((i for i, l in enumerate(lines) if l.strip().lower() == f'section {section_name.lower()}'), None)
    if sec_i is None:
        sec_i = next(i for i, l in enumerate(lines) if re.fullmatch(rf'\s*section {section_name}\b.*', l, re.I)
                     and 'answer' not in l.lower())
    qstart = re.compile(rf'^\s{{0,12}}{qno}[.)]?\s+\S')
    start = next(i for i in range(sec_i + 1, len(lines)) if qstart.match(lines[i]))
    heading = [lines[sec_i].strip()] + [l.strip() for l in lines[sec_i + 1:start] if l.strip() and not FOOTER.search(l)]
    # end: next section heading, or the next question number at the same indent right after a mark
    indent = len(lines[start]) - len(lines[start].lstrip())
    nxt = re.compile(rf'^\s{{{indent}}}{qno + 1}[.)]?\s+\S')
    prev = ''
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.fullmatch(r'\s*section [b-d]\s*', lines[i], re.I) or (nxt.match(lines[i]) and MARKS.search(prev)):
            end = i
            break
        if lines[i].strip() and not FOOTER.search(lines[i]):
            prev = lines[i]
    body = [l for l in lines[start:end] if not FOOTER.search(l) or l.strip().startswith('(')]
    body[0] = re.sub(rf'^\s*{qno}[.)]?\s+', '', body[0])

    stem, parts, buf, cur = [], [], [], None

    def flush():
        if buf:
            text = ' '.join(x.strip() for x in buf)
            text = re.sub(r'\s+', ' ', text).strip()
            if cur is None:
                stem.append(text)
            else:
                cur[1] = (cur[1] + ' ' + text).strip()
        buf.clear()

    for raw in body:
        s = re.sub(r'^\)\s+', '', raw.strip())
        if not s:
            flush()
            continue
        m = PART.match(s)
        if m and not (cur is None and not stem and not buf and False):
            flush()
            if cur:
                parts.append(cur)
            cur = [f'({m.group(1) or m.group(2)})', m.group(3), None]
            s = ''
        if s.startswith(('•', '−', '–', '- ')) and cur is None:
            flush()
        mk = MARKS.search(raw)
        if mk:
            s = MARKS.sub('', s).strip()
            if s:
                buf.append(s)
            flush()
            if cur is not None:
                cur[2] = int(mk.group(1))
            continue
        if s:
            buf.append(s)
    flush()
    if cur:
        parts.append(cur)
    clean = lambda t: re.sub(r'\s+([,.;:?])', r'\1', re.sub(r'\s+', ' ', t)).strip()
    inline = re.compile(r'\s*\[\s*(\d{1,2})\s*(?:marks?)?\s*\]\s*', re.I)
    out_parts = []
    for l, t, m in parts:
        found = inline.findall(t)      # mark printed inside the text (one-line part, or wrapped layout)
        if m is None and found:
            m = int(found[-1])
        out_parts.append((l, clean(inline.sub(' ', t)), m))
    return {'section': ' — '.join(heading),
            'stem': [clean(p) for p in stem if p],
            'parts': out_parts}


if __name__ == '__main__':
    import json, sys
    print(json.dumps(extract(sys.argv[1], int(sys.argv[2]), sys.argv[3]), indent=1, ensure_ascii=False))
