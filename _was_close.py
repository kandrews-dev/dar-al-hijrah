# -*- coding: utf-8 -*-
"""Badge Part 7 complete on the Wasitiyyah hub -- the matn is finished."""
import io, sys
sys.stdout.reconfigure(encoding='utf-8')

F = 'pages/aqeedah/wasitiyyah-index.html'
h = io.open(F, encoding='utf-8').read()

P7 = ('<span style="font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;'
      'color:var(--ink-faint);white-space:nowrap">Part 7</span>')
BADGE = ('\n              <span style="font-size:.62rem;letter-spacing:.06em;'
         'text-transform:uppercase;font-weight:700;color:white;'
         'background:var(--teal-deep);border-radius:999px;padding:3px 9px;'
         'white-space:nowrap">✓ complete · 5 lessons</span>')
assert h.count(P7) == 1, 'Part 7 label'
h = h.replace(P7, P7 + BADGE)

# A banner above the plan: every part of the matn is now built.
ANCHOR = '        <div class="section-heading">\n          <span class="sh-ar">خِطَّةُ المَسَار</span>'
assert h.count(ANCHOR) == 1, 'plan heading'
BANNER = (
    '        <div style="background:var(--brand-wash);border:1px solid var(--brand);'
    'border-radius:var(--radius-lg);padding:var(--space-lg);margin-bottom:var(--space-lg)">\n'
    '          <p style="font-family:var(--font-arabic);font-size:1.18rem;'
    'color:var(--teal-deep);direction:rtl;font-weight:700;margin:0 0 .4rem;'
    'text-align:center">تَمَّ المَتْنُ بِحَمْدِ اللهِ</p>\n'
    '          <p style="font-size:.9rem;color:var(--ink-mid);line-height:1.8;margin:0;'
    'text-align:center"><strong>All seven parts of al-ʿAqīdah al-Wāsiṭiyyah are now '
    'built — 54 lessons</strong>, taken in Ibn Taymiyyah’s own order, with Shaykh Ṣāliḥ '
    'al-Fawzān’s <em>sharḥ</em> followed page by page from its opening to its last '
    'line. Nothing of the matn has been passed over.</p>\n'
    '        </div>\n')
h = h.replace(ANCHOR, BANNER + ANCHOR)

io.open(F, 'w', encoding='utf-8', newline='\n').write(h)
print('hub: Part 7 badged complete; matn-complete banner added')
