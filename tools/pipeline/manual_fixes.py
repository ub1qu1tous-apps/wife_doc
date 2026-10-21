"""Crops that need a hand fix after crop_resources.py. Run after cropping; safe to re-run.

- EJC 2024 H1 R7A/7B: the two maps are a picture on a landscape page of the Word insert, and LibreOffice drops
  it when converting to PDF. Take the picture from the .docx itself and put it under the heading crop.
- SAJC 2026 H2 P2 R1: picture turned 90 degrees in the Word file (see ROTATE_BELOW_HEADING).
- CJC 2026 H2 P2 R4: table placed above its heading in the converted PDF (see HEAD_BELOW).
- TJC 2026 H1 R5 and R9: heading + picture are a group turned 270 degrees in Word; LibreOffice turns the picture
  but clips the heading. Rebuild the crop from the heading text and the upright picture in the .docx.
"""
import os, sys, zipfile, io
from PIL import Image, ImageDraw, ImageFont

S = os.environ.get('SCRATCH', '/tmp/wife_doc_scratch')
FIXES = [  # (crop file, source docx, media item)
    ('full/img/2024_EJC_H1/R7A.png',
     'sources/Other JC Prelims 2024/EJC (Ans)/EJC Geography Exam Paper (2024 Prelim) JC2 H1 (Insert_Final).docx',
     'word/media/image10.png'),
]
for crop, docx, media in FIXES:
    path = os.path.join(S, crop)
    if not os.path.exists(path):
        print('missing', path); continue
    head = Image.open(path).convert('RGB')
    if head.height > 300:
        print('already fixed', crop); continue
    pic = Image.open(io.BytesIO(zipfile.ZipFile(docx).read(media))).convert('RGB')
    pic = pic.resize((head.width, round(pic.height * head.width / pic.width)))
    out = Image.new('RGB', (head.width, head.height + pic.height), 'white')
    out.paste(head, (0, 0)); out.paste(pic, (0, head.height))
    out.save(path)
    print('fixed', crop, out.size)

TJC26 = 'sources/Other JC Prelims 2026/TJC/H1 Geog/2026 H1 JC2 TJC Prelim Insert Final.docx'
REBUILD = [  # (crop file, source docx, media item, heading lines)
    ('full/img/2026_TJC_H1/R5.png', TJC26, 'word/media/image7.png',
     ['Resource 5 for Question 2', 'Share of the urban population living in slums, 2024']),
    ('full/img/2026_TJC_H1/R9.png', TJC26, 'word/media/image12.png',
     ['Resource 9 for Question 3', 'Sources of greenhouse gas emissions in the United Kingdom (UK) and Ethiopia in 2023']),
]
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
for crop, docx, media, heading in REBUILD:
    pic = Image.open(io.BytesIO(zipfile.ZipFile(docx).read(media))).convert('RGB')
    W = max(pic.width, 1100)
    font = ImageFont.truetype(FONT, max(18, W // 55))
    head_h = 20 + len(heading) * (font.size + 12)
    out = Image.new('RGB', (W, head_h + pic.height + 10), 'white')
    d = ImageDraw.Draw(out)
    for i, line in enumerate(heading):
        w = d.textlength(line, font=font)
        d.text(((W - w) / 2, 12 + i * (font.size + 12)), line, fill='black', font=font)
    out.paste(pic, ((W - pic.width) // 2, head_h))
    out.save(os.path.join(S, crop))
    print('rebuilt', crop, out.size)

# CJC 2026 H2 P2 R4: in the PDF made from the Word file the floating table sits above its heading, so the normal crop
# (heading down to the footer) misses it. Crop the heading block and the table separately and stack heading first.
import hashlib, re, pdfplumber, pypdfium2 as pdfium
HEAD_BELOW = [  # (crop file, source Word file, page index, heading text)
    ('full/img/2026_CJC_H2P2/R4.png', 'Other JC Prelims 2026/CJC/H2/Paper 2/2026 H2 Geo Prelim P2 Insert.docx', 4, 'Resource 4 for Question 1'),
]
for crop, src, pi, head in HEAD_BELOW:
    pdf_path = f"{S}/pdfcache/{hashlib.md5(src.encode()).hexdigest()[:10]}/{os.path.splitext(os.path.basename(src))[0]}.pdf"
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[pi]
        words = page.extract_words()
        h = next(w for i, w in enumerate(words) if w['text'] == 'Resource' and ' '.join(x['text'] for x in words[i:i + len(head.split())]) == head)
        body = [w for w in words if not re.fullmatch(r'\d+', w['text']) or w['top'] < page.height * 0.9]
        above = [w['bottom'] for w in body if w['bottom'] < h['top'] - 2] + [r['bottom'] for r in page.rects if r['bottom'] < h['top']]
        below = [w['bottom'] for w in body if w['top'] >= h['top'] - 1 and w['bottom'] < page.height * 0.9]
        top0 = min([w['top'] for w in body] + [r['top'] for r in page.rects])
    scale = 170 / 72
    img = pdfium.PdfDocument(pdf_path)[pi].render(scale=scale).to_pil()
    table = img.crop((0, max(0, int((top0 - 6) * scale)), img.width, int((max(above) + 2) * scale)))
    heading = img.crop((0, int((h['top'] - 2) * scale), img.width, int((max(below) + 8) * scale)))
    from PIL import ImageOps
    parts = []
    for p in (heading, table):
        b = ImageOps.invert(p.convert('L')).getbbox()
        parts.append(p.crop((max(0, b[0] - 10), 0, min(p.width, b[2] + 10), p.height)) if b else p)
    W = max(p.width for p in parts)
    out = Image.new('RGB', (W, sum(p.height for p in parts)), 'white')
    y = 0
    for p in parts:
        out.paste(p, ((W - p.width) // 2, y)); y += p.height
    out.save(os.path.join(S, crop))
    print('rebuilt', crop, out.size)

# SAJC 2026 H2 P2 R1: the picture is turned 90 degrees in the Word file (reads top to bottom). Keep the heading lines
# (the first `lines` runs of ink) and turn the rest upright. Skipped if already done (crop wider than tall).
ROTATE_BELOW_HEADING = [  # (crop file, heading lines, angle for PIL rotate)
    ('full/img/2026_SAJC_H2P2/R1.png', 2, 90),
]
for crop, nlines, angle in ROTATE_BELOW_HEADING:
    path = os.path.join(S, crop)
    im = Image.open(path).convert('RGB')
    if im.width > im.height:
        print('already fixed', crop); continue
    g = im.convert('L')
    ink = [min(g.crop((0, y, g.width, y + 1)).getdata()) < 200 for y in range(g.height)]
    runs, y = 0, 0
    while y < g.height and runs < nlines:
        while y < g.height and not ink[y]:
            y += 1
        while y < g.height and ink[y]:
            y += 1
        runs += 1
    head, pic = im.crop((0, 0, im.width, y + 8)), im.crop((0, y + 8, im.width, im.height)).rotate(angle, expand=True)
    W = max(head.width, pic.width)
    out = Image.new('RGB', (W, head.height + pic.height), 'white')
    out.paste(head, ((W - head.width) // 2, 0)); out.paste(pic, ((W - pic.width) // 2, head.height))
    out.save(path)
    print('rotated', crop, out.size)
