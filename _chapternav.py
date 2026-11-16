# -*- coding: utf-8 -*-
"""Add an in-page chapter dropdown to every Arabic vocab book page.

The 40 vocab lessons + 5 vocab exams only let you move chapter-by-chapter via
the bottom 'next' button. This injects a <select> jump-menu — all chapters
grouped by Book (and the exams) — into the existing 'Jump to:' bar at the top
of each page, with the current chapter preselected. Chapter labels are pulled
from the hub menu so nothing is transcribed by hand.

Idempotent: a page already carrying data-chapnav is skipped.
"""
import re, io, sys, glob
sys.stdout.reconfigure(encoding='utf-8')

HUB = 'pages/arabic/index.html'
hub = io.open(HUB, encoding='utf-8').read()
pairs = re.findall(
    r'<li><a href="(vocab-\d\d-[^"]+\.html)"><span class="dd-ch">([^<]+)</span></a></li>', hub)
assert len(pairs) == 40, 'expected 40 vocab chapters, got %d' % len(pairs)

BOOKS = [('الكِتَابُ الأَوَّل · Book 1', pairs[0:9]),
         ('الكِتَابُ الثَّانِي · Book 2', pairs[9:24]),
         ('الكِتَابُ الثَّالِث · Book 3', pairs[24:40])]
EXAMS = [('vocab-exam-1.html', '★ اختبار ١ · (١–١٣)'),
         ('vocab-exam-2.html', '★ اختبار ٢ · (١٤–١٨)'),
         ('vocab-exam-3.html', '★ اختبار ٣ · (١٩–٢٤)'),
         ('vocab-exam-4.html', '★ اختبار ٤ · (٢٥–٣٠)'),
         ('vocab-exam-5.html', '★ اختبار ٥ · (٣١–٣٦)')]


def select_html(current):
    o = ['<select data-chapnav dir="rtl" onchange="if(this.value)location.href=this.value" '
         'aria-label="اذهب إلى درس · Jump to a chapter" '
         'style="font-family:var(--font-arabic);font-size:.82rem;font-weight:600;'
         'color:var(--ink-mid);background:var(--surface-2);border:1px solid var(--line);'
         'border-radius:999px;padding:5px 12px;cursor:pointer;max-width:280px">']
    o.append('<option value="">اذهب إلى درس · Jump to chapter…</option>')
    for label, items in BOOKS:
        o.append('<optgroup label="%s">' % label)
        for href, lab in items:
            sel = ' selected' if href == current else ''
            o.append('<option value="%s"%s>%s</option>' % (href, sel, lab))
        o.append('</optgroup>')
    o.append('<optgroup label="الاختبارات · Exams">')
    for href, lab in EXAMS:
        sel = ' selected' if href == current else ''
        o.append('<option value="%s"%s>%s</option>' % (href, sel, lab))
    o.append('</optgroup>')
    o.append('</select>')
    return ''.join(o)


ANCHOR = '>Jump to:</span>'
targets = sorted(glob.glob('pages/arabic/vocab-[0-9][0-9]-*.html')) + \
          sorted(glob.glob('pages/arabic/vocab-exam-*.html'))
n = 0
for f in targets:
    h = io.open(f, encoding='utf-8').read()
    if 'data-chapnav' in h:
        print('%-44s already has chapter nav — skipped' % f); continue
    if ANCHOR not in h:
        print('%-44s NO jump bar — skipped' % f); continue
    cur = f.replace('\\', '/').split('/')[-1]
    sel = select_html(cur)
    h = h.replace(ANCHOR, ANCHOR + sel, 1)
    io.open(f, 'w', encoding='utf-8', newline='\n').write(h)
    n += 1
    print('%-44s + chapter nav (current: %s)' % (f, cur))

print('\n%d pages given a chapter dropdown' % n)
