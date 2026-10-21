"""Build the companion "Review Notes" doc for a consolidated doc.

Every doc in docs/ gets one: what it is and how it was built, the assumptions made, items for the
user to review (tables with a 'Your decision' column), and things to consider.
Spec: tools/review/<doc id>.json  {"title", "doc", "version", "sections": [{"title", "note"?, "bullets"? , "table"?: {"columns", "rows"}}]}

usage: review_docs.py <spec.json> <outdir>
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_docs import base_doc, cell_text, shade, repeat_header, GREY
from docx.shared import Pt


def build(spec, outdir):
    doc = base_doc(f"{spec['title']} – Review Notes", spec['version'])
    p = doc.add_paragraph()
    r = p.add_run(f"Companion to: {spec['doc']}")
    r.italic, r.font.size, r.font.color.rgb = True, Pt(9), GREY
    for sec in spec['sections']:
        doc.add_heading(sec['title'], level=1)
        if sec.get('note'):
            r = doc.add_paragraph().add_run(sec['note'])
            r.italic, r.font.size, r.font.color.rgb = True, Pt(9), GREY
        for b in sec.get('bullets', []):
            doc.add_paragraph(b, style='List Bullet')
        if sec.get('table'):
            cols, rows = sec['table']['columns'], sec['table']['rows']
            t = doc.add_table(rows=1, cols=len(cols))
            t.style = 'Table Grid'
            for c, h in zip(t.rows[0].cells, cols):
                cell_text(c, [(h, True, False)], size=9)
                shade(c, 'D9E2F3')
            repeat_header(t.rows[0])
            for row in rows:
                for c, v in zip(t.add_row().cells, row + [''] * (len(cols) - len(row))):
                    cell_text(c, [(str(v), False, False)], size=9)
    path = os.path.join(outdir, f"{spec['file']} – Review Notes {spec['version']}.docx")
    doc.save(path)
    return path


if __name__ == '__main__':
    print(build(json.load(open(sys.argv[1], encoding='utf8')), sys.argv[2]))
