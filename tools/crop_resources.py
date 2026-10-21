"""Crop each 'Resource N ...' block of an Insert PDF into its own PNG.
usage: crop_resources.py <insert.pdf> <outdir> [dpi]"""
import re, sys, os, subprocess
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

def trim_bands(im):
    """Cut plain bands at the left/right edge (e.g. the grey comment margin of a PDF printed with Word markup)."""
    from PIL import ImageStat
    g = im.convert('L')
    def plain(x):
        col = g.crop((x, 0, x + 1, g.height))
        lo, hi = col.getextrema()
        return hi - lo < 8 and lo > 190
    r = g.width
    while r > 50 and plain(r - 1):
        r -= 1
    l = 0
    while l < r - 50 and plain(l):
        l += 1
    if r < g.width - 20 or l > 20:
        return im.crop((max(0, l - 8), 0, min(g.width, r + 8), im.height))
    return im


doc = pdfium.PdfDocument(pdf_path)
with pdfplumber.open(pdf_path) as pdf:
    blocks = []  # (page_idx, top, label)
    footers, tops, stop_pages, stops = {}, {}, set(), {}
    for i, page in enumerate(pdf.pages):
        ls = lines_of(page)
        # content bottom = last line that isn't a page number / footer
        body = [l for l in ls if not re.fullmatch(r'\s*(\d+|\[?Turn over\]?|©.*|.*\bPrelim.*\d{4}.*|\[?\d+\]?|end( of insert)?|'
                                                  r'.*\b(8834|9173)\b.*|.*\bH[12] Geography\b.*|higher [12] geography.*)\s*', l[2], re.I)]
        bots = [l[1] for l in body]
        for obj in list(page.images) + list(page.rects) + list(page.curves) + list(page.lines):
            if obj['top'] > page.height * 0.87:
                continue   # logos/rules in the page footer
            if obj['bottom'] < page.height - 30 and (obj['bottom'] - obj['top']) < page.height * 0.9:
                bots.append(obj['bottom'])
        footers[i] = (max(bots) + 6) if bots else page.height
        stop = [l[0] for l in ls if l[0] > page.height * 0.4 and re.fullmatch(r'\s*(end( of (insert|paper))?|(re)?sources?|(copyright )?acknowledge?ments?)\s*:?\s*', l[2], re.I)]
        if stop:   # 'End' / 'Sources' list below the last resource on the page
            stops[i] = stop[0]
        tops[i] = min([l[0] for l in body] + [im['top'] for im in page.images]) if (body or page.images) else None
        txt = ' '.join(l[2] for l in ls).lower()
        if 'acknowledg' in txt or 'blank page' in txt or ('copyright' in txt and 'permission' in txt):
            stop_pages.add(i)
        short = [l for l in ls if len(l[2].replace(' ', '')) <= 3]
        side = sum(1 for c in page.chars if abs(c['matrix'][1]) > 0.5)
        if (len(ls) > 15 and len(short) > 0.5 * len(ls)) or (side > 20 and side > 0.5 * len(page.chars)):
            stop_pages.add(i)   # landscape (rotated) page: text reads as vertical letters, its heading isn't found
        for top, bot, text in ls:
            m = HEAD.match(text)
            if m and re.search(r'https?:|www\.|adapted from|source:|\.com|\.org', text, re.I):
                continue   # source/acknowledgement line, not a resource heading
            if m and re.match(r'\s*\S+\s+\S+\s+(?!for\b)[a-z]', text):
                continue   # a sentence such as "Resource 1 shows ..." (question paper text), not a heading
            if m and m.group(1).lower() == 'resource':
                covered = any(im['top'] < top and bot < im['bottom'] and im['bottom'] - im['top'] < page.height * 0.85 for im in page.images)
                blocks.append((i, top, 'R' + m.group(2).upper(), text.strip(), covered))
    # a label that sits under a picture and also appears elsewhere is a stray hidden label (NJC 2026 H1 'Resource 10' under R9)
    labels = [b[2] for b in blocks]
    blocks = [b[:4] for b in blocks if not (b[4] and labels.count(b[2]) > 1)]
    crops = []
    for n, (pi, top, label, text) in enumerate(blocks):
        nxt = blocks[n + 1] if n + 1 < len(blocks) else None
        page = pdf.pages[pi]
        bottom = nxt[1] - 4 if nxt and nxt[0] == pi else footers[pi]
        if stops.get(pi, 0) > top + 20:
            bottom = min(bottom, stops[pi] - 4)
        scale = dpi / 72
        img = doc[pi].render(scale=scale).to_pil()
        crop = img.crop((0, max(0, int((top - 6) * scale)), img.width, int(bottom * scale)))
        # trim white margins
        from PIL import ImageOps
        bbox = ImageOps.invert(crop.convert('L')).getbbox()
        if bbox:   # trim white margins left, right and below
            crop = crop.crop((max(0, bbox[0] - 10), 0, min(crop.width, bbox[2] + 10), min(crop.height, bbox[3] + 12)))
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
        crops.append([label, trim_bands(crop), text])
    # landscape pages (content turned sideways): heading from the rotated text, whole content area turned upright
    from PIL import Image
    for pi in sorted(stop_pages):
        page = pdf.pages[pi]
        side = [c for c in page.chars if abs(c['matrix'][1]) > 0.5]   # text turned 90 degrees
        words = subprocess.run(['pdftotext', '-raw', '-f', str(pi + 1), '-l', str(pi + 1), pdf_path, '-'],
                               capture_output=True, text=True).stdout
        words = ' '.join(words.split())
        if len(side) < 10 or 'acknowledg' in words.lower() or any(b[0] == pi for b in blocks):
            continue
        heads = re.findall(r'Resources?\s+(\d+[A-Z]?)((?:\s*(?:,|and|&)\s*\d+[A-Z]?)*)\s+for\b', words)
        if not heads:
            continue
        labels = []
        for first, rest in heads:
            labels += ['R' + first.upper()] + ['R' + x.upper() for x in re.findall(r'\d+[A-Z]?', rest)]
        boxes = [(c['x0'], c['top'], c['x1'], c['bottom']) for c in side]
        for obj in list(page.images) + list(page.rects) + list(page.curves) + list(page.lines):
            if page.height * 0.06 < obj['top'] and obj['bottom'] < page.height * 0.93:
                boxes.append((obj['x0'], obj['top'], obj['x1'], obj['bottom']))
        x0, t0 = max(0, min(b[0] for b in boxes) - 6), max(0, min(b[1] for b in boxes) - 6)
        x1, t1 = min(page.width, max(b[2] for b in boxes) + 6), min(page.height, max(b[3] for b in boxes) + 6)
        scale = dpi / 72
        img = doc[pi].render(scale=scale).to_pil().crop((int(x0 * scale), int(t0 * scale), int(x1 * scale), int(t1 * scale)))
        m = side[0]['matrix']
        img = img.rotate(-90 if m[1] > 0 else 90, expand=True)   # text running upwards -> turn clockwise
        crops.append([labels[0], img, f'(landscape page {pi + 1}) ' + ', '.join(labels)])
        for extra in labels[1:]:
            open(os.path.join(outdir, f'{extra}.alias'), 'w').write(labels[0])
    crops.sort(key=lambda c: [int(re.match(r'R(\d+)', c[0]).group(1)), c[0]])
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
    final = {}
    for label, crop, text in merged:
        if label in final:
            if re.search(r'for questions?\s+\d', text, re.I) and crop.height > 150:   # heading repeated on a continuation page
                prev, ptext = final[label]
                W = max(prev.width, crop.width)
                canvas = Image.new('RGB', (W, prev.height + crop.height), 'white')
                canvas.paste(prev, (0, 0)); canvas.paste(crop, (0, prev.height))
                final[label] = (canvas, ptext)
                print('CONTINUED', label, '|', text[:70])
            else:
                print('DUPLICATE', label, '|', text[:70])
            continue
        final[label] = (crop, text)
    for label, (crop, text) in final.items():
        fn = os.path.join(outdir, f'{label}.png')
        crop.save(fn)
        print(fn, crop.size, '|', text[:70])
