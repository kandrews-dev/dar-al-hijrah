# -*- coding: utf-8 -*-
"""Wire ḥadīth 18 into the track: a card on the hub, and h17's forward link."""
import io, sys
sys.stdout.reconfigure(encoding='utf-8')

HUB = 'pages/hadeeth/index.html'
h = io.open(HUB, encoding='utf-8').read()

if 'h18-ittaqi-allah.html' in h:
    print('hub: already wired')
else:
    CARD = '''<a href="h18-ittaqi-allah.html" style="text-decoration:none;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;display:flex;flex-direction:column;transition:all .2s" onmouseover="this.style.boxShadow='var(--shadow-md)';this.style.transform='translateY(-2px)'" onmouseout="this.style.boxShadow='';this.style.transform=''">
          <div style="height:4px;background:var(--tab-hadeeth)"></div>
          <div style="padding:var(--space-lg);flex:1;display:flex;flex-direction:column">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:var(--space-sm)">
              <span style="font-size:.68rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-faint)">Ḥadīth 18</span>
              <span class="lesson-status current" data-lesson-id="hd-h18"></span>
            </div>
            <p style="font-family:var(--font-arabic);font-size:1.3rem;color:var(--brand-deep);direction:rtl;font-weight:700;margin-bottom:2px">اتَّقِ اللهَ حَيْثُمَا كُنْت</p>
            <p style="font-size:.92rem;font-weight:600;color:var(--ink);margin-bottom:var(--space-sm)">Fear Allah Wherever You Are</p>
            <p style="font-size:.82rem;color:var(--ink-faint);line-height:1.6;flex:1">Three commands for the three relationships of a life — with your Lord, your own sins, and other people.</p>
            <div style="display:flex;gap:6px;margin-top:var(--space-md);flex-wrap:wrap">
              <span style="background:var(--surface-2);border:1px solid var(--line);border-radius:20px;padding:2px 9px;font-size:.7rem;color:var(--ink-light)">Sharḥ</span>
              <span style="background:var(--surface-2);border:1px solid var(--line);border-radius:20px;padding:2px 9px;font-size:.7rem;color:var(--ink-light)">Vocab</span>
              <span style="background:var(--surface-2);border:1px solid var(--line);border-radius:20px;padding:2px 9px;font-size:.7rem;color:var(--ink-light)">Quiz</span>
            </div>
          </div>
        </a>'''

    i = h.find('<a href="h17-ihsan.html"')
    assert i > 0, 'h17 card not found on the hub'
    j = h.index('</a>', i) + 4
    io.open(HUB, 'w', encoding='utf-8', newline='\n').write(
        h[:j] + '\n        ' + CARD + h[j:])
    print('hub: ḥadīth 18 card added after ḥadīth 17')

L17 = 'pages/hadeeth/h17-ihsan.html'
g = io.open(L17, encoding='utf-8').read()
OLD = ('<a href="index.html" class="btn-primary" onclick="markLessonComplete(\'hd-h17\')">'
       'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub →</a>')
NEW = ('<a href="h18-ittaqi-allah.html" class="btn-primary" '
       'onclick="markLessonComplete(\'hd-h17\')">'
       'Ḥadīth 18 · اتَّقِ الله →</a>')
if NEW in g:
    print('h17: already points to h18')
else:
    assert g.count(OLD) == 1, 'h17 nav target not found exactly once'
    io.open(L17, 'w', encoding='utf-8', newline='\n').write(g.replace(OLD, NEW))
    print('h17: forward link now goes to ḥadīth 18')
