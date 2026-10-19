# -*- coding: utf-8 -*-
"""Link the muraja'ah from the Wasitiyyah hub, directly under the
matn-complete banner -- which is where a student who has just finished the
text will be looking."""
import io, sys
sys.stdout.reconfigure(encoding='utf-8')

F = 'pages/aqeedah/wasitiyyah-index.html'
h = io.open(F, encoding='utf-8').read()

if 'wasitiyyah-murajaah.html' in h:
    sys.exit('already linked')

ANCHOR = ('          <p style="font-size:.9rem;color:var(--ink-mid);line-height:1.8;'
          'margin:0;text-align:center"><strong>All seven parts of al-ʿAqīdah '
          'al-Wāsiṭiyyah are now built')
assert h.count(ANCHOR) == 1, 'banner text'

CLOSE = '        </div>\n'
i = h.index(ANCHOR)
j = h.index(CLOSE, i) + len(CLOSE)

LINK = (
    '        <a href="wasitiyyah-murajaah.html" style="text-decoration:none;display:block;'
    'margin-bottom:var(--space-lg)">\n'
    '          <div style="background:white;border:1px solid var(--brand);'
    'border-radius:var(--radius-lg);padding:var(--space-lg);transition:all .2s" '
    'onmouseover="this.style.boxShadow=\'var(--shadow-md)\';'
    'this.style.transform=\'translateY(-2px)\'" onmouseout="this.style.boxShadow=\'\';'
    'this.style.transform=\'\'">\n'
    '            <p style="font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;'
    'color:var(--ink-faint);margin-bottom:6px">After the text</p>\n'
    '            <p style="font-family:var(--font-arabic);font-size:1.18rem;'
    'color:var(--teal-deep);direction:rtl;font-weight:700;margin-bottom:4px">'
    'مُرَاجَعَةُ المَتْن</p>\n'
    '            <p style="font-size:.88rem;font-weight:600;color:var(--ink-mid);'
    'margin-bottom:var(--space-sm)">What You Should Now Know</p>\n'
    '            <p style="font-size:.8rem;color:var(--ink-light);line-height:1.75">'
    'Thirty-six prompts walking the seven parts in order — the definitions you should '
    'now own, the proofs and where they sit, the positions of the opposing sects, and '
    'the places al-Fawzān qualified or corrected the matn. Each answer is hidden until '
    'you have tried it, and each one links back to its lesson. '
    '<strong>Not an exam; no timer and no score.</strong></p>\n'
    '          </div>\n        </a>\n')

io.open(F, 'w', encoding='utf-8', newline='\n').write(h[:j] + LINK + h[j:])
print('hub: murajaʿah linked under the completion banner')
