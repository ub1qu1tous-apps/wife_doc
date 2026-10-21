"""Crop each 'Resource N ...' block of an Insert PDF into its own PNG.
usage: crop_resources.py <insert.pdf> <outdir> [dpi]"""
import re, sys, os
import pdfplumber, pypdfium2 as pdfium

pdf_path, outdir = sys.argv[1], sys.argv[2]
dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 170
os.makedirs(outdir, exist_ok=True)
HEAD = re.compile(r'^\s*(Resource|Figure|Fig\.?|Table)\s+([0-9]+[A-Za-z]?)\b', re.I)

def lines_of(page):
    words = page.extract_words(keep_blank_chars=False, use_text_flow=True)
    rows = {}
    for w in words:
        key = round(w['top'] / 3)
        rows.setdefault(key, []).append(w)
    out = []
    for k in sorted(rows):
        ws = sorted(rows[k], key=lambda w: w['x0'])
        out.append((min(w['top'] for w in ws), max(w['bottom'] for w in ws), ' '.join(w['text'] for w in ws)))
    return out

doc = pdfium.PdfDocument(pdf_path)
with pdfplumber.open(pdf_path) as pdf:
    blocks = []  # (page_idx, top, label)
    footers, tops, stop_pages = {}, {}, set()
    for i, page in enumerate(pdf.pages):
        ls = lines_of(page)
        # content bottom = last line that isn't a page number / footer
        body = [l for l in ls if not re.fullmatch(r'\s*(\d+|\[?Turn over\]?|©.*|.*\bPrelim.*\d{4}.*|\[?\d+\]?)\s*', l[2], re.I)]
        bots = [l[1] for l in body]
        for obj in list(page.images) + list(page.rects) + list(page.curves) + list(page.lines):
            if obj['top'] > page.height * 0.9:
                continue   # logos/rules in the page footer
            if obj['bottom'] < page.height - 30 and (obj['bottom'] - obj['top']) < page.height * 0.9:
                bots.append(obj['bottom'])
        footers[i] = (max(bots) + 6) if bots else page.height
        tops[i] = min([l[0] for l in body] + [im['top'] for im in page.images]) if (body or page.images) else None
        txt = ' '.join(l[2] for l in ls).lower()
        if 'acknowledg' in txt or 'blank page' in txt or ('copyright' in txt and 'permission' in txt):
            stop_pages.add(i)
        short = [l for l in ls if len(l[2].replace(' ', '')) <= 3]
        if len(ls) > 15 and len(short) > 0.5 * len(ls):
            stop_pages.add(i)   # landscape (rotated) page: text reads as vertical letters, its heading isn't found
        for top, bot, text in ls:
            m = HEAD.match(text)
            if m and re.search(r'https?:|www\.|adapted from|source:|\.com|\.org', text, re.I):
                continue   # source/acknowledgement line, not a resource heading
            if m and re.match(r'\s*\S+\s+\S+\s+(?!for\b)[a-z]', text):
                continue   # a sentence such as "Resource 1 shows ..." (question paper text), not a heading
            if m and m.group(1).lower() == 'resource':
                blocks.append((i, top, 'R' + m.group(2).upper(), text.strip()))
    crops = []
    for n, (pi, top, label, text) in enumerate(blocks):
        nxt = blocks[n + 1] if n + 1 < len(blocks) else None
        page = pdf.pages[pi]
        bottom = nxt[1] - 4 if nxt and nxt[0] == pi else footers[pi]
        scale = dpi / 72
        img = doc[pi].render(scale=scale).to_pil()
        crop = img.crop((0, max(0, int((top - 6) * scale)), img.width, int(bottom * scale)))
        # trim white margins
        from PIL import ImageOps
        bbox = ImageOps.invert(crop.convert('L')).getbbox()
        if bbox:
            crop = crop.crop((max(0, bbox[0] - 10), 0, min(crop.width, bbox[2] + 10), crop.height))
        # resources spanning to next page with no new heading: append continuation
        parts = [crop]
        if nxt is None or nxt[0] > pi:
            last = nxt[0] if nxt else len(pdf.pages) - 1
            for cp in range(pi + 1, last + 1):
                if cp in stop_pages or tops.get(cp) is None:
                    break
                if nxt and nxt[0] == cp and sum(p.height for p in parts) > 250 and footers[cp - 1] < 0.8 * pdf.pages[cp - 1].height:
                    break   # previous page wasn't full, so nothing overflowed: content above the next heading isn't ours
                bot_c = (nxt[1] - 4) if (nxt and nxt[0] == cp) else footers[cp]
                if bot_c - tops[cp] < 12:
                    continue
                cimg = doc[cp].render(scale=scale).to_pil()
                c = cimg.crop((0, int((tops[cp] - 6) * scale), cimg.width, int(bot_c * scale)))
                b = ImageOps.invert(c.convert('L')).getbbox()
                if b and (b[3] - b[1]) > 60:
                    parts.append(c.crop((max(0, b[0] - 10), 0, min(c.width, b[2] + 10), c.height)))
        if len(parts) > 1:
            from PIL import Image
            W = max(p.width for p in parts); H = sum(p.height for p in parts)
            canvas = Image.new('RGB', (W, H), 'white'); y = 0
            for p in parts:
                canvas.paste(p, (0, y)); y += p.height
            crop = canvas
        crops.append([label, crop, text])
    from PIL import Image
    merged = []
    for i, (label, crop, text) in enumerate(crops):
        nxt = crops[i + 1] if i + 1 < len(crops) else None
        if crop.height < 150 and nxt and re.fullmatch(re.escape(label) + '[A-Z]', nxt[0]):
            W = max(crop.width, nxt[1].width)
            canvas = Image.new('RGB', (W, crop.height + nxt[1].height), 'white')
            canvas.paste(crop, (0, 0)); canvas.paste(nxt[1], (0, crop.height))
            nxt[1] = canvas
            continue
        merged.append((label, crop, text))
    seen = set()
    for label, crop, text in merged:
        if label in seen:
            print('DUPLICATE', label, '|', text[:70])
            continue
        seen.add(label)
        fn = os.path.join(outdir, f'{label}.png')
        crop.save(fn)
        print(fn, crop.size, '|', text[:70])
