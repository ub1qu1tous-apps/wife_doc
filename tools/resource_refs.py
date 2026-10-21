"""Find which resources a question's wording refers to, e.g. 'Resources 1 and 2', 'Resources 2A to 2D'."""
import re


def refs(text):
    out = []
    for m in re.finditer(r'Resources?\s+((?:\d+[A-Z]?(?:\s*(?:,|and|&|to|-|–)\s*)?)+)', text):
        toks = re.findall(r'\d+[A-Z]?|to|–|-', m.group(1))
        i = 0
        while i < len(toks):
            t = toks[i]
            if t in ('to', '–', '-'):
                i += 1
                continue
            if i + 2 < len(toks) and toks[i + 1] in ('to', '–', '-'):
                a, b = t, toks[i + 2]
                if a[:-1].isdigit() and a[-1].isalpha() and b[-1].isalpha():   # 2A to 2D
                    out += [f'{a[:-1]}{chr(c)}' for c in range(ord(a[-1]), ord(b[-1]) + 1)]
                elif a.isdigit() and b.isdigit():                              # 1 to 3
                    out += [str(n) for n in range(int(a), int(b) + 1)]
                else:
                    out += [a, b]
                i += 3
                continue
            out.append(t)
            i += 1
    return list(dict.fromkeys(out))
