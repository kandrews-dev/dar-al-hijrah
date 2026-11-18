# -*- coding: utf-8 -*-
"""Wire ḥadīth 21 into the track: a card on the hub, and h20's forward link."""
import io, sys
sys.stdout.reconfigure(encoding='utf-8')

HUB = 'pages/hadeeth/index.html'
h = io.open(HUB, encoding='utf-8').read()

if 'h21-qul-amantu.html' in h:
    print('hub: already wired')
else:
    CARD = '''<a href="h21-qul-amantu.html" style="text-decoration:none;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;display:flex;flex-direction:column;transition:all .2s" onmouseover="this.style.boxShadow='var(--shadow-md)';this.style.transform='translateY(-2px)'" onmouseout="this.style.boxShadow='';this.style.transform=''">
          <div style="height:4px;background:var(--tab-hadeeth)"></div>
          <div style="padding:var(--space-lg);flex:1;display:flex;flex-direction:column">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:var(--space-sm)">
              <span style="font-size:.68rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-faint)">Ḥadīth 21</span>
              <span class="lesson-status current" data-lesson-id="hd-h21"></span>
            </div>
            <p style="font-family:var(--font-arabic);font-size:1.3rem;color:var(--brand-deep);direction:rtl;font-weight:700;margin-bottom:2px">قُلْ آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ</p>
            <p style="font-size:.92rem;font-weight:600;color:var(--ink);margin-bottom:var(--space-sm)">Say “I Believe in Allah,” Then Be Steadfast</p>
            <p style="font-size:.82rem;color:var(--ink-faint);line-height:1.6;flex:1">The whole religion in two words — the heart’s affirmation of tawḥīd and going straight on the sharīʿah; the two conditions of worship; istiqāmah, not iltizām.</p>
            <div style="display:flex;gap:6px;margin-top:var(--space-md);flex-wrap:wrap">
              <span style="background:var(--surface-2);border:1px solid var(--line);border-radius:20px;padding:2px 9px;font-size:.7rem;color:var(--ink-light)">Sharḥ</span>
              <span style="background:var(--surface-2);border:1px solid var(--line);border-radius:20px;padding:2px 9px;font-size:.7rem;color:var(--ink-light)">Vocab</span>
              <span style="background:var(--surface-2);border:1px solid var(--line);border-radius:20px;padding:2px 9px;font-size:.7rem;color:var(--ink-light)">Quiz</span>
            </div>
          </div>
        </a>'''

    i = h.find('<a href="h20-idha-lam-tastahi.html"')
    assert i > 0, 'h20 card not found on the hub'
    j = h.index('</a>', i) + 4
    io.open(HUB, 'w', encoding='utf-8', newline='\n').write(
        h[:j] + '\n        ' + CARD + h[j:])
    print('hub: ḥadīth 21 card added after ḥadīth 20')

L20 = 'pages/hadeeth/h20-idha-lam-tastahi.html'
g = io.open(L20, encoding='utf-8').read()
OLD = ('<a href="index.html" class="btn-primary" onclick="markLessonComplete(\'hd-h20\')">'
       'Mark complete · أَتْمَمْتَ الدَّرْس · Hadeeth Hub →</a>')
NEW = ('<a href="h21-qul-amantu.html" class="btn-primary" '
       'onclick="markLessonComplete(\'hd-h20\')">'
       'Ḥadīth 21 · قُلْ آمَنْتُ بِالله →</a>')
if NEW in g:
    print('h20: already points to h21')
else:
    assert g.count(OLD) == 1, 'h20 nav target not found exactly once'
    io.open(L20, 'w', encoding='utf-8', newline='\n').write(g.replace(OLD, NEW))
    print('h20: forward link now goes to ḥadīth 21')
