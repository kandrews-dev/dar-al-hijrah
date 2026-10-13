# -*- coding: utf-8 -*-
"""Regenerate the Wasitiyyah hub's live-lesson grid from the files on disk.

Scans pages/aqeedah/was-l*.html, reads each one's Arabic and English title and
its meta description for the blurb, and rewrites the grid between the markers.
Run after adding lessons instead of hand-editing the hub.
"""
import io, os, re, glob, sys, html as htmllib

sys.stdout.reconfigure(encoding='utf-8')
AQ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pages', 'aqeedah')
HUB = os.path.join(AQ, 'wasitiyyah-index.html')
START = '<!-- WAS-GRID-START -->'
END = '<!-- WAS-GRID-END -->'

CARD = """          <a href="%s" style="text-decoration:none" data-lesson-id="%s">
            <div style="background:white;border:1px solid var(--ivory-dark);border-radius:var(--radius-lg);padding:var(--space-lg);height:100%%;transition:all .2s" onmouseover="this.style.boxShadow='var(--shadow-md)';this.style.transform='translateY(-2px)'" onmouseout="this.style.boxShadow='';this.style.transform=''">
              <p style="font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-faint);margin-bottom:6px">Lesson %d</p>
              <p style="font-family:var(--font-arabic);font-size:1.1rem;color:var(--teal-deep);direction:rtl;font-weight:700;margin-bottom:4px">%s</p>
              <p style="font-size:.86rem;font-weight:600;color:var(--ink-mid);margin-bottom:var(--space-sm)">%s</p>
              <p style="font-size:.78rem;color:var(--ink-light);line-height:1.7">%s</p>
            </div>
          </a>
"""


def blurb(desc):
    """Trim the meta description down to the part after the colon."""
    d = htmllib.unescape(desc).strip()
    d = re.sub(r'^Lesson \d+ of al-.{0,40}?Wāsiṭiyyah:\s*', '', d)
    d = d[0].upper() + d[1:] if d else d
    return d


cards = []
for f in sorted(glob.glob(os.path.join(AQ, 'was-l*.html'))):
    h = io.open(f, encoding='utf-8').read()
    n = int(re.search(r'was-l(\d+)', os.path.basename(f)).group(1))
    tar = re.search(r'<p class="lesson-title-ar">(.*?)</p>', h)
    ten = re.search(r'<p class="lesson-title-en">(.*?)</p>', h)
    desc = re.search(r'<meta name="description" content="(.*?)">', h, re.S)
    lid = 'ws-l%02d' % n
    if not (tar and ten):
        print('  !! no title in %s' % os.path.basename(f)); continue
    cards.append(CARD % (os.path.basename(f), lid, n, tar.group(1).strip(),
                         ten.group(1).strip(),
                         blurb(desc.group(1)) if desc else ''))

h = io.open(HUB, encoding='utf-8').read()
if START not in h:
    # first run: wrap the existing grid contents in markers
    # Find the grid's opening div, then its MATCHING close by depth counting.
    # A non-greedy .*? stops at the first </div> inside a card, which leaves
    # half the old grid behind and duplicates every card. (Learned the hard way.)
    open_pat = ('<div style="display:grid;grid-template-columns:repeat(auto-fill,'
                'minmax(290px,1fr));gap:var(--space-md)">')
    i = h.find(open_pat)
    if i < 0:
        raise SystemExit('could not locate the live-lesson grid to mark up')
    j = i + len(open_pat)
    depth = 1
    while depth:
        o = h.find('<div', j)
        c = h.find('</div>', j)
        if c < 0:
            raise SystemExit('unbalanced grid')
        if 0 <= o < c:
            depth += 1
            j = o + 4
        else:
            depth -= 1
            j = c + 6
    inner_end = j - len('</div>')
    h = h[:i + len(open_pat)] + '\n' + START + '\n' + END + '\n        ' + h[inner_end:]
    print('  inserted grid markers')

new = START + '\n' + ''.join(cards) + '          ' + END
h = re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda _: new, h, count=1, flags=re.S)
io.open(HUB, 'w', encoding='utf-8', newline='\n').write(h)
print('hub grid synced: %d lessons' % len(cards))
