# -*- coding: utf-8 -*-
"""Link the Nawāqiḍ depth track from the overview page.

u6-nawaqid.html stays exactly where it is — six pages link to it — and gains a
banner pointing to the lessons that take each nullifier at the depth of the
sharḥ. The banner lists the lessons that exist, so it grows as they are built.
"""
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

F = 'pages/aqeedah/u6-nawaqid.html'
h = io.open(F, encoding='utf-8').read()

LESSONS = [
    ('nq-l01-shirk-al-ibadah.html', '١',
     'الشِّرْكُ فِي العِبَادَة', 'Shirk in Worship'),
    ('nq-l02-dhabh-wa-tarik-al-salah.html', '١',
     'الذَّبْحُ وَتَارِكُ الصَّلَاة',
     'Slaughter, and the One Who Leaves the Prayer'),
    ('nq-l03-al-wasait.html', '٢',
     'اتِّخَاذُ الوَسَائِط', 'Taking Intermediaries'),
    ('nq-l04-takfir-al-mushrikin.html', '٣',
     'عَدَمُ تَكْفِيرِ المُشْرِكِين',
     'Not Declaring the Mushrikīn Disbelievers'),
]

MARK = '<!-- NQ-DEPTH-TRACK -->'
h = re.sub(re.escape(MARK) + r'.*?' + re.escape(MARK) + r'\s*', '', h, flags=re.S)

rows = ''.join(
    '<a href="%s" style="display:flex;align-items:baseline;gap:.6rem;'
    'text-decoration:none;padding:.5rem .7rem;border-radius:var(--radius-sm);'
    'background:white;border:1px solid var(--ivory-dark)">'
    '<span style="font-family:var(--font-arabic);color:var(--teal-deep);'
    'font-weight:700">%s</span>'
    '<span style="font-family:var(--font-arabic);direction:rtl;'
    'color:var(--teal-deep);font-weight:600;font-size:.95rem">%s</span>'
    '<span style="font-size:.8rem;color:var(--ink-mid)">%s →</span></a>'
    % (href, num, tar, ten) for href, num, tar, ten in LESSONS)

BANNER = (
    MARK + '\n'
    '        <div style="background:var(--brand-wash);border:1px solid var(--brand);'
    'border-radius:var(--radius-lg);padding:var(--space-lg);'
    'margin:0 0 var(--space-lg)">\n'
    '          <p style="font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;'
    'color:var(--brand-deep);font-weight:700;margin:0 0 .4rem">'
    'الشَّرْحُ المُفَصَّل · the lessons in depth</p>\n'
    '          <p style="font-size:.9rem;color:var(--ink-mid);line-height:1.85;'
    'margin:0 0 .7rem">This page is the overview — the ten nullifiers in one '
    'sitting. Each one is also taken at the depth of the sharḥ, explained '
    'throughout from the words of <strong>Shaykh Ibn Bāz</strong>.</p>\n'
    '          <div style="display:flex;flex-direction:column;gap:6px">%s</div>\n'
    '        </div>\n        ' % rows) + MARK + '\n'

ANCHOR = '        <div class="objectives-box">'
assert h.count(ANCHOR) == 1, 'objectives box anchor'
i = h.index(ANCHOR)
j = h.index('</div>', h.index('</ul>', i)) + len('</div>') + 1

io.open(F, 'w', encoding='utf-8', newline='\n').write(h[:j] + '\n' + BANNER + h[j:])
print('overview: depth-track banner with %d lesson(s)' % len(LESSONS))
