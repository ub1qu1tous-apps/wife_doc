"""Extract the wording of one question from a question-paper PDF.

extract(pdf, qno, section) -> {'section': str, 'stem': [paragraphs], 'parts': [(label, text, marks)]}
Works on `pdftotext -layout` output: the question starts at the line numbered `qno` after the
section heading and ends at the next section heading or question number.
"""
import re, subprocess

FOOTER = re.compile(r'(©|geography prelim|\b20\d\d\s+JC\d\b|\[?\s*turn over|8834|9173|preliminary exam|prelim(inary)? examination|'
                    r'^\s*\d{1,2}\s*$|^\s*page \d+|this document consists|blank page|^\s*cluster \d\b[^.]{0,70}$)', re.I)
PART = re.compile(r'^(?:\(([a-h])\)?|([a-h])\))(?:\s+(.*))?$')  # (a) / a) / '(b' with ')' wrapped to next line
END = re.compile(r'^\s*(\*+\s*)?(end of (the )?(question )?paper\.?|end of section [a-d]|- ?end ?-|end\.?|_{8,}.*|'
                 r'\[?\s*total\s*:?\s*\d*\s*(marks?)?\s*\]?|blank page|copyright acknowledg.*|acknowledge?ments?\s*:?|'
                 r'resource \d+[a-z]? for question.*|this insert.*|insert)\s*$', re.I)   # end of the last question in a paper
MARKS = re.compile(r'\[\s*(\d{1,2})\s*(?:marks?)?\s*\]\s*$', re.I)


def pdf_lines(pdf):
    txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    lines = txt.replace('\f', '\n').split('\n')
    # labels and marks printed down a narrow column over three lines ('(' / 'a' / ')' and '[' / '4' / ']'; SAJC Word files)
    for i in range(len(lines) - 2):
        a, b, c = lines[i], lines[i + 1], lines[i + 2]
        ma, mb, mc = re.match(r'^(\s*)\((\s+.*|)$', a), re.match(r'^(\s*)([a-h])(\s+.*|)$', b), re.match(r'^(\s*)\)(\s+.*|)$', c)
        if ma and mb and mc and abs(len(ma.group(1)) - len(mb.group(1))) <= 1:
            lines[i] = f'{ma.group(1)}({mb.group(2)})  ' + ma.group(2).strip()
            lines[i + 1] = ' ' * (len(mb.group(1)) + 5) + mb.group(3).strip() if mb.group(3).strip() else ''
            lines[i + 2] = ' ' * (len(mc.group(1)) + 5) + mc.group(2).strip() if mc.group(2).strip() else ''
    for i in range(len(lines) - 2):
        if re.search(r'\s\[\s*$', lines[i]) and re.search(r'\s(\d{1,2})\s*$', lines[i + 1]) and re.match(r'^\s*.*\]\s*$', lines[i + 2]) \
                and '[' not in lines[i + 2]:
            n = re.search(r'\s(\d{1,2})\s*$', lines[i + 1]).group(1)
            lines[i] = re.sub(r'\s\[\s*$', '', lines[i])
            lines[i + 1] = re.sub(r'\s\d{1,2}\s*$', '', lines[i + 1])
            lines[i + 2] = re.sub(r'\]\s*$', '', lines[i + 2]).rstrip()
            last = i + 2 if lines[i + 2].strip() else i + 1 if lines[i + 1].strip() else i
            lines[last] = lines[last].rstrip() + f'   [{n}]'
    # a mark split over two lines ('... [6' / ']' or '... [' / '3]'): move the whole mark to the second line
    for i in range(len(lines) - 1):
        a = re.search(r'\s\[\s*(\d*)\s*$', lines[i])
        b = re.match(r'^(.*?)\s*(\d*)\]\s*$', lines[i + 1])
        if a and b and (a.group(1) + b.group(2)).isdigit() and not re.search(r'\[', b.group(1)):
            lines[i] = lines[i][:a.start()]
            lines[i + 1] = f'{b.group(1)}   [{a.group(1) + b.group(2)}]'
    return lines


def extract(pdf, qno, section_name):
    lines = pdf_lines(pdf)
    # locate the section heading ("Section A" on its own line)
    qstart = re.compile(rf'^\s{{0,12}}{qno}[.)]?\s+\S')
    any_sec = re.compile(r'\s*section [a-d]\b.*', re.I)

    def leads_to_q(i):   # the heading is followed by question qno before any other section heading (skips cover pages)
        for j in range(i + 1, len(lines)):
            if qstart.match(lines[j]):
                return True
            if any_sec.fullmatch(lines[j]) and 'answer' not in lines[j].lower():
                return False
        return False
    cands = [i for i, l in enumerate(lines) if l.strip().lower() == f'section {section_name.lower()}'] or \
            [i for i, l in enumerate(lines) if re.fullmatch(rf'\s*section {section_name}\b.*', l, re.I) and 'answer' not in l.lower()]
    sec_i = next((i for i in reversed(cands) if leads_to_q(i)), None)   # the last one: cover pages list sections too
    if sec_i is None:   # some papers letter their sections differently (e.g. H2 P2 with only Sections A and B)
        heads = [i for i, l in enumerate(lines) if any_sec.fullmatch(l) and 'answer' not in l.lower()]
        sec_i = next((i for i in reversed(heads) if leads_to_q(i)), (cands or heads)[0])
    # the question number sits furthest left: a wrapped stem line can also start with the number ('Resource' / '2 is a map')
    starts = [i for i in range(sec_i + 1, len(lines)) if qstart.match(lines[i])]
    sec_end = next((j for j in range(sec_i + 1, len(lines)) if any_sec.fullmatch(lines[j]) and 'answer' not in lines[j].lower()), len(lines))
    starts = [i for i in starts if i < sec_end] or starts
    indent0 = min(len(lines[i]) - len(lines[i].lstrip()) for i in starts)
    start = next(i for i in starts if len(lines[i]) - len(lines[i].lstrip()) <= indent0 + 1)
    heading = [lines[sec_i].strip()] + [l.strip() for l in lines[sec_i + 1:start] if l.strip() and not FOOTER.search(l)]
    # end: next section heading, or the next question number at the same indent right after a mark
    indent = len(lines[start]) - len(lines[start].lstrip())
    nxt = re.compile(rf'^\s{{{max(0, indent - 3)},{indent + 3}}}{qno + 1}[.)]?\s+\S')
    mark_re = re.compile(r'\[\s*\d{1,2}\s*(?:marks?)?\s*\]', re.I)
    marked = bool(mark_re.search(lines[start]))   # a mark has been seen (so a line starting 'qno+1' is not a stem line)
    end = len(lines)
    part_seen = False   # an essay (no parts) ends at its mark, or the blank line after it if words follow the mark

    def essay_end(i):
        j = i + 1
        while j < len(lines) and lines[j].strip() and not (FOOTER.search(lines[j]) or nxt.match(lines[j]) or END.match(lines[j])
                                                         or re.fullmatch(r'\s*section [b-d]\s*', lines[j], re.I)):
            j += 1
        return j
    if marked:
        end = essay_end(start)
    for i in range(start + 1, end):
        if re.fullmatch(r'\s*section [b-d]\s*', lines[i], re.I) or (nxt.match(lines[i]) and marked) or END.match(lines[i]):
            end = i
            break
        part_seen = part_seen or bool(PART.match(re.sub(rf'^{qno}[.)]?\s+(?=\(?[a-h]\)\s)', '', lines[i].strip())))
        if lines[i].strip() and not FOOTER.search(lines[i]) and mark_re.search(lines[i]):
            marked = True
            if not part_seen:
                end = essay_end(i)
                break
    body = [l for l in lines[start:end] if not FOOTER.search(l) or l.strip().startswith('(')]
    body[0] = re.sub(rf'^\s*{qno}[.)]?\s+', '', body[0])

    stem, parts, buf, cur, stem_marks = [], [], [], None, []

    def flush():
        if buf:
            text = ' '.join(x.strip() for x in buf)
            # a word broken over two lines at its hyphen ('problem-' / 'solving'), but not 'low- and high-income'
            text = re.sub(r'(?<=[A-Za-z])- (?!(?:and|or|to|on|in|at|the|nor)\b)(?=[a-z])', '-', text)
            text = re.sub(r'\s+', ' ', text).strip()
            if cur is None:
                stem.append(text)
            else:
                cur[1] = (cur[1] + ' ' + text).strip()
        buf.clear()

    for raw in body:
        s = re.sub(r'^\)\s+', '', raw.strip())
        s = re.sub(rf'^{qno}[.)]?\s+(?=\(?[a-h]\)\s)', '', s)   # question number repeated before (a) on a new page
        if not s:
            flush()
            continue
        m = PART.match(s)
        if m and not (cur is None and not stem and not buf and False):
            flush()
            if cur:
                parts.append(cur)
            cur = [f'({m.group(1) or m.group(2)})', m.group(3) or '', None]
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
            else:
                stem_marks.append(int(mk.group(1)))   # essay: mark printed after the question
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
    out = {'section': ' — '.join(heading), 'stem': [clean(p) for p in stem if p], 'parts': out_parts}
    if not out_parts:
        found = stem_marks or [int(x) for x in inline.findall(' '.join(stem))]
        out['marks'] = found[-1] if found else None
        out['stem'] = [clean(inline.sub(' ', p)) for p in out['stem']]
        out['stem'] = [p for p in out['stem'] if p]
    return out


if __name__ == '__main__':
    import json, sys
    print(json.dumps(extract(sys.argv[1], int(sys.argv[2]), sys.argv[3]), indent=1, ensure_ascii=False))
