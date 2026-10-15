# -*- coding: utf-8 -*-
"""Add the L49 card to the Wasitiyyah hub grid and badge Part 6 complete."""
import io, sys
sys.stdout.reconfigure(encoding='utf-8')

F = 'pages/aqeedah/wasitiyyah-index.html'
h = io.open(F, encoding='utf-8').read()
orig = h

CARD = (
    '          <a href="was-l49-ma-shajara-bayna-al-sahabah.html" '
    'style="text-decoration:none" data-lesson-id="ws-l49">\n'
    '            <div style="background:white;border:1px solid var(--ivory-dark);'
    'border-radius:var(--radius-lg);padding:var(--space-lg);height:100%;'
    'transition:all .2s" onmouseover="this.style.boxShadow=\'var(--shadow-md)\';'
    'this.style.transform=\'translateY(-2px)\'" onmouseout="this.style.boxShadow=\'\';'
    'this.style.transform=\'\'">\n'
    '              <p style="font-size:.7rem;letter-spacing:.08em;'
    'text-transform:uppercase;color:var(--ink-faint);margin-bottom:6px">Lesson 49</p>\n'
    '              <p style="font-family:var(--font-arabic);font-size:1.1rem;'
    'color:var(--teal-deep);direction:rtl;font-weight:700;margin-bottom:4px">'
    'الإِمْسَاكُ عَمَّا شَجَرَ بَيْنَ الصَّحَابَة</p>\n'
    '              <p style="font-size:.86rem;font-weight:600;color:var(--ink-mid);'
    'margin-bottom:var(--space-sm)">Refraining from What Occurred Between the '
    'Companions</p>\n'
    '              <p style="font-size:.78rem;color:var(--ink-light);line-height:1.7">'
    'Closing Part 6: disowning both the Rāfiḍah and the Nawāṣib; the two matters of '
    'refraining and answering; the four excuses in order, and the rule that a certainty '
    'is not surrendered to a doubt; the ḥadīth of the judge and the reward of the '
    'mistaken mujtahid; and the expiators that cover a Companion’s sin as they cover no '
    'later man’s.</p>\n'
    '            </div>\n'
    '          </a>\n')

MARK = '          <!-- WAS-GRID-END -->'
assert h.count(MARK) == 1, 'grid-end marker'
h = h.replace(MARK, CARD + MARK)

# Part 6 badge, inserted after the "Part 6" label span exactly as Parts 1-5 carry it
P6 = ('<span style="font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;'
      'color:var(--ink-faint);white-space:nowrap">Part 6</span>')
BADGE = ('\n              <span style="font-size:.62rem;letter-spacing:.06em;'
         'text-transform:uppercase;font-weight:700;color:white;'
         'background:var(--teal-deep);border-radius:999px;padding:3px 9px;'
         'white-space:nowrap">✓ complete · 5 lessons</span>')
assert h.count(P6) == 1, 'Part 6 label'
h = h.replace(P6, P6 + BADGE)

assert h != orig
io.open(F, 'w', encoding='utf-8', newline='\n').write(h)
print('hub: L49 card added, Part 6 badged complete (5 lessons)')
