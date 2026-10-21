"""Contact sheets of the crops a doc uses, for checking by eye.

usage: SCRATCH=... python3 tools/pipeline/contact_sheets.py <res.json> <outprefix> [per_sheet=20]
"""
import json, os, sys
from PIL import Image, ImageDraw

S = os.environ.get('SCRATCH', '/tmp/wife_doc_scratch')
res, prefix = json.load(open(sys.argv[1])), sys.argv[2]
per = int(sys.argv[3]) if len(sys.argv) > 3 else 20
items = list(dict.fromkeys((k.rsplit('_', 1)[0] if '_Q' in k else k, p) for k, ps in res.items() for p in ps))
cols, tw, th = 5, 300, 330
for n in range(0, len(items), per):
    chunk = items[n:n + per]
    rows = (len(chunk) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * tw, rows * th), 'white')
    d = ImageDraw.Draw(sheet)
    for i, (k, p) in enumerate(chunk):
        im = Image.open(os.path.join(S, 'full', p)).convert('RGB')
        lab = f"{p.split('/')[1]} {os.path.basename(p)[:-4]} {im.size[0]}x{im.size[1]}"
        im.thumbnail((tw - 10, th - 30))
        x, y = (i % cols) * tw, (i // cols) * th
        sheet.paste(im, (x + 5, y + 22))
        d.rectangle([x + 4, y + 21, x + 6 + im.width, y + 23 + im.height], outline='red')
        d.text((x + 5, y + 5), lab, fill='black')
    sheet.save(f'{prefix}_{n // per + 1:02d}.png')
print((len(items) + per - 1) // per, 'sheets,', len(items), 'crops')
