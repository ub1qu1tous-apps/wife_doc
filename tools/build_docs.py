"""Build the consolidated Word docs from questions.json.

Doc 1: topic grid (H1 table, H2 table): rows = school + year, columns = question slots,
       cells = syllabus topic(s) of each question.
Doc 2: questions listed by syllabus topic, split into 4 docs
       (H1 structured, H1 essay, H2 structured, H2 essay); each entry = school + year,
       full question text, then the resources (diagrams) it uses.

usage: build_docs.py <questions.json> <outdir> <version> [--preview]
"""
import json, os, sys
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = json.load(open(os.path.join(HERE, 'syllabus_topics.json')))
GREY = RGBColor(0x59, 0x59, 0x59)

H1_SLOTS = [('Q1', 'Sec A', 'Fieldwork'), ('Q2', 'Sec B', 'Structured'), ('Q3', 'Sec B', 'Structured'),
            ('Q4', 'Sec C', 'Essay'), ('Q5', 'Sec C', 'Essay'), ('Q6', 'Sec C', 'Essay')]
H2_SLOTS = [('P1 Q1', 'Cluster 1', 'Structured'), ('P1 Q2', 'Cluster 2', 'Structured'),
            ('P1 Q3', 'Cluster 1', 'Essay'), ('P1 Q4', 'Cluster 1', 'Essay'),
            ('P1 Q5', 'Cluster 2', 'Essay'), ('P1 Q6', 'Cluster 2', 'Essay'),
            ('P2 Q1', 'Fieldwork', 'Structured'), ('P2 Q2', 'Cluster 3', 'Structured'),
            ('P2 Q3', 'Cluster 3', 'Essay'), ('P2 Q4', 'Cluster 3', 'Essay')]


def topic_label(level, code):
    """'1.2.2' -> '1.2.2 Possible Effects of Climate Change'."""
    return f"{code} {TOPICS[level]['subtopics'].get(code) or TOPICS[level]['topics'].get(code) or code}"


def short_label(level, code):
    """'1.2.2' -> '1.2.2 Effects of CC' (grid cells)."""
    return f"{code} {TOPICS[level]['short'].get(code) or TOPICS[level]['topics'].get(code) or code}"


def base_doc(title, version, landscape=False, preview=False):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    if landscape:
        sec.orientation = WD_ORIENT.LANDSCAPE
        sec.page_width, sec.page_height = sec.page_height, sec.page_width
    for side in ('left_margin', 'right_margin', 'top_margin', 'bottom_margin'):
        setattr(sec, side, Cm(1.5))
    st = doc.styles['Normal']
    st.font.name, st.font.size = 'Arial', Pt(10)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')
    for name, size in (('Title', 18), ('Heading 1', 14), ('Heading 2', 12), ('Heading 3', 11)):
        s = doc.styles[name]
        s.font.name, s.font.size = 'Arial', Pt(size)
        s.element.rPr.rFonts.set(qn('w:asciiTheme'), 'Arial') if False else None
    doc.add_heading(f"{title} — {version}" + (" (PREVIEW)" if preview else ''), level=0)
    p = doc.add_paragraph()
    r = p.add_run("Topics follow the SEAB syllabus: H1 Geography 8834 (2026) and H2 Geography 9173 (2026).")
    r.italic, r.font.color.rgb, r.font.size = True, GREY, Pt(9)
    return doc


def shade(cell, hex_fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hex_fill)
    tcPr.append(shd)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement('w:tblHeader'); el.set(qn('w:val'), 'true'); trPr.append(el)


def cell_text(cell, lines, size=8):
    cell.text = ''
    first = True
    for text, bold, grey in lines:
        p = cell.paragraphs[0] if first else cell.add_paragraph()
        first = False
        p.paragraph_format.space_after = Pt(1)
        r = p.add_run(text)
        r.bold, r.font.size = bold, Pt(size)
        if grey:
            r.italic, r.font.color.rgb = True, GREY


def grid_table(doc, level, slots, qs, schools_years, title):
    doc.add_heading(title, level=1)
    t = doc.add_table(rows=2, cols=len(slots) + 1)
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr, sub = t.rows[0], t.rows[1]
    cell_text(hdr.cells[0], [('School & Year', True, False)])
    cell_text(sub.cells[0], [('', False, False)])
    for i, (slot, sec, kind) in enumerate(slots, 1):
        cell_text(hdr.cells[i], [(slot, True, False)])
        cell_text(sub.cells[i], [(f'{sec} · {kind}', False, True)], size=7)
    for row in (hdr, sub):
        repeat_header(row)
        for c in row.cells:
            shade(c, 'D9E2F3')
    for school, year in schools_years:
        cells = t.add_row().cells
        cell_text(cells[0], [(f'{school} {year}', True, False)])
        for i, (slot, _, _) in enumerate(slots, 1):
            q = qs.get((school, year, slot))
            if not q:
                cell_text(cells[i], [('—', False, True)])
                continue
            lines = [(short_label(level, c), True, False) for c in q['topics']]
            if q.get('fieldwork_area'):
                lines = [(f"Fieldwork – {q['fieldwork_area']}", True, False)]
            if q.get('focus'):
                lines.append((q['focus'], False, True))
            cell_text(cells[i], lines)
    widths = [Cm(2.2)] + [Cm((doc.sections[0].page_width.cm - 3.0 - 2.2) / len(slots))] * len(slots)
    for row in t.rows:
        for w, c in zip(widths, row.cells):
            c.width = w


def build_grid(questions, outdir, version, preview):
    doc = base_doc('Other JC Prelims – Topics by School (H1 & H2)', version, landscape=True, preview=preview)
    for level, slots, title in (('H1', H1_SLOTS, 'H1 Geography (8834) – Paper 1'),
                                ('H2', H2_SLOTS, 'H2 Geography (9173) – Papers 1 & 2')):
        qs = {(q['school'], q['year'], q['slot']): q for q in questions if q['level'] == level}
        rows = sorted({(s, y) for s, y, _ in qs})
        grid_table(doc, level, slots, qs, rows, title)
    name = '1 Topic Grid by School (H1 & H2)'
    path = os.path.join(outdir, f"{name} {version}{' PREVIEW' if preview else ''}.docx")
    doc.save(path)
    return path


def add_question(doc, q, img_root):
    level = q['level']
    doc.add_heading(f"{q['school']} {q['year']} — {q['paper']}, {q['qno']}  [{q['marks']} marks]", level=3)
    p = doc.add_paragraph()
    r = p.add_run('Syllabus: ' + '; '.join(topic_label(level, c) for c in q['topics'])
                  + (f"   |   Fieldwork area: {q['fieldwork_area']}" if q.get('fieldwork_area') else ''))
    r.italic, r.font.size, r.font.color.rgb = True, Pt(8.5), GREY
    section, *stem = q['stem']
    r = doc.add_paragraph().add_run(section)
    r.font.size, r.font.color.rgb, r.bold = Pt(8.5), GREY, True
    for para in stem:
        doc.add_paragraph(para).paragraph_format.space_after = Pt(4)
    right = doc.sections[0].page_width - doc.sections[0].left_margin - doc.sections[0].right_margin
    for label, text, marks in q.get('parts', []):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.left_indent, pf.first_line_indent, pf.space_after = Cm(1.0), Cm(-1.0), Pt(4)
        pf.tab_stops.add_tab_stop(Cm(1.0))
        pf.tab_stops.add_tab_stop(right, WD_TAB_ALIGNMENT.RIGHT)
        p.add_run(f'{label}\t{text}\t[{marks}]')
    for res in q.get('resources', []):
        doc.add_paragraph()
        doc.add_picture(os.path.join(img_root, res), width=Cm(15.5))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph()


def build_by_topic(questions, outdir, version, preview, img_root):
    docs = [('H1', 'structured', '2a H1 Structured Questions by Topic', 'H1 Structured Questions by Topic (8834 Sec A & B)'),
            ('H1', 'essay', '2b H1 Essay Questions by Topic', 'H1 Essay Questions by Topic (8834 Sec C)'),
            ('H2', 'structured', '2c H2 Structured Questions by Topic', 'H2 Structured Questions by Topic (9173 P1 & P2)'),
            ('H2', 'essay', '2d H2 Essay Questions by Topic', 'H2 Essay Questions by Topic (9173 P1 & P2)')]
    paths = []
    for level, kind, fname, title in docs:
        doc = base_doc(title, version, preview=preview)
        sel = [q for q in questions if q['level'] == level and q['kind'] == kind and q.get('stem')]
        tops = TOPICS[level]
        # group under primary topic (structured) or primary sub-topic (essay)
        key = (lambda q: q['primary']) if kind == 'essay' else (lambda q: q['primary'])
        for cluster, cl_name in tops['clusters'].items():
            in_cluster = [q for q in sel if key(q).startswith(cluster + '.') or key(q) == cluster]
            if not in_cluster:
                continue
            doc.add_heading(f'Cluster {cluster}: {cl_name}', level=1)
            groups = sorted({key(q) for q in in_cluster}, key=lambda c: [x if not x.isdigit() else int(x) for x in c.replace('-', '.').split('.')])
            for g in groups:
                doc.add_heading(topic_label(level, g) if g in tops['subtopics'] or g in tops['topics'] else g, level=2)
                for q in sorted((q for q in in_cluster if key(q) == g), key=lambda q: (q['school'], q['year'])):
                    add_question(doc, q, img_root)
        path = os.path.join(outdir, f"{fname} {version}{' PREVIEW' if preview else ''}.docx")
        doc.save(path)
        paths.append(path)
    return paths


if __name__ == '__main__':
    qfile, outdir, version = sys.argv[1:4]
    preview = '--preview' in sys.argv
    questions = json.load(open(qfile))
    os.makedirs(outdir, exist_ok=True)
    img_root = os.path.dirname(os.path.abspath(qfile))
    print(build_grid(questions, outdir, version, preview))
    for p in build_by_topic(questions, outdir, version, preview, img_root):
        print(p)
