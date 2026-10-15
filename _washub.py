# -*- coding: utf-8 -*-
"""Add a lesson card to the Wasitiyyah hub grid.

Usage: python _washub.py <n> <file.html> <arabic title> <english title> <blurb>

Replaces the one-off _was49_hub.py pattern: the card markup is identical every
time, so the only thing that should live in a script is the five fields.
"""
import io, sys
sys.stdout.reconfigure(encoding='utf-8')

n, href, t_ar, t_en, blurb = sys.argv[1:6]
F = 'pages/aqeedah/wasitiyyah-index.html'
h = io.open(F, encoding='utf-8').read()

if href in h:
    print('hub: %s already present, nothing to do' % href)
    sys.exit(0)

CARD = (
    '          <a href="%s" style="text-decoration:none" data-lesson-id="ws-l%s">\n'
    '            <div style="background:white;border:1px solid var(--ivory-dark);'
    'border-radius:var(--radius-lg);padding:var(--space-lg);height:100%%;'
    'transition:all .2s" onmouseover="this.style.boxShadow=\'var(--shadow-md)\';'
    'this.style.transform=\'translateY(-2px)\'" onmouseout="this.style.boxShadow=\'\';'
    'this.style.transform=\'\'">\n'
    '              <p style="font-size:.7rem;letter-spacing:.08em;'
    'text-transform:uppercase;color:var(--ink-faint);margin-bottom:6px">Lesson %s</p>\n'
    '              <p style="font-family:var(--font-arabic);font-size:1.1rem;'
    'color:var(--teal-deep);direction:rtl;font-weight:700;margin-bottom:4px">%s</p>\n'
    '              <p style="font-size:.86rem;font-weight:600;color:var(--ink-mid);'
    'margin-bottom:var(--space-sm)">%s</p>\n'
    '              <p style="font-size:.78rem;color:var(--ink-light);line-height:1.7">'
    '%s</p>\n'
    '            </div>\n'
    '          </a>\n' % (href, n, n, t_ar, t_en, blurb))

MARK = '          <!-- WAS-GRID-END -->'
assert h.count(MARK) == 1, 'grid-end marker'
io.open(F, 'w', encoding='utf-8', newline='\n').write(h.replace(MARK, CARD + MARK))
print('hub: Lesson %s card added' % n)
