"""Checks that make Word 2007 refuse a docx: invalid link URLs, unresolved r:ids, run properties out of schema order.

usage: check_docx.py <file.docx> [...]
"""
import re, sys, zipfile
from lxml import etree

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
RPR = ['rStyle', 'rFonts', 'b', 'bCs', 'i', 'iCs', 'caps', 'smallCaps', 'strike', 'dstrike', 'outline', 'shadow', 'emboss',
       'imprint', 'noProof', 'snapToGrid', 'vanish', 'webHidden', 'color', 'spacing', 'w', 'kern', 'position', 'sz', 'szCs',
       'highlight', 'u', 'effect', 'bdr', 'shd', 'fitText', 'vertAlign', 'rtl', 'cs', 'em', 'lang', 'eastAsianLayout']

for path in sys.argv[1:]:
    z = zipfile.ZipFile(path)
    rels = z.read('word/_rels/document.xml.rels').decode('utf8')
    doc = z.read('word/document.xml')
    bad_urls = [t for t in re.findall(r'Target="([^"]+)"[^>]*TargetMode="External"', rels)
                if re.search(r"[^A-Za-z0-9\-._~:/?#\[\]@!$&'()*+,;=%]", t)]
    ids = set(re.findall(r'Id="([^"]+)"', rels))
    unresolved = set(re.findall(rb'r:(?:id|embed)="([^"]+)"', doc)) - {i.encode() for i in ids}
    bad_order = 0
    for el in etree.fromstring(doc).iter(W + 'rPr'):
        idx = [RPR.index(etree.QName(c).localname) if etree.QName(c).localname in RPR else 99 for c in el]
        bad_order += idx != sorted(idx)
    ok = not (bad_urls or unresolved or bad_order)
    print(('OK  ' if ok else 'FAIL'), path.split('/')[-1], f'| bad URLs {len(bad_urls)} | unresolved rIds {len(unresolved)} | rPr order {bad_order}')
