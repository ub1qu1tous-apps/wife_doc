"""Crops that need a hand fix after crop_resources.py. Run after cropping; safe to re-run.

- EJC 2024 H1 R7A/7B: the two maps are a picture on a landscape page of the Word insert, and LibreOffice drops
  it when converting to PDF. Take the picture from the .docx itself and put it under the heading crop.
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
