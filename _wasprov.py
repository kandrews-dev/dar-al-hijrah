# -*- coding: utf-8 -*-
"""Put a reference line on every Wasitiyyah lesson naming where in al-Fawzan's
sharh the lesson's material comes from.

Where the page numbers come from
--------------------------------
Two sources, both evidence-based:

  1. For the 41 lessons whose builder script records the pages it was written
     from, that record is used. Each one was VALIDATED independently: the
     lesson's own Arabic was scored against every OCR page, and the
     best-matching page falls inside the recorded range for 40 of the 41. The
     exception (L27) is listed in EXCEPTIONS below with what was done about it.

  2. For the 13 lessons whose builder is no longer on disk, the range is
     derived from the text: the lesson's best-matching page is its start, and
     the next lesson's best-matching page less one is its end. The sharh runs
     in the matn's order and the lessons follow it, so consecutive lessons tile
     the book -- and the derived peaks do come out strictly increasing, which
     is what tiling looks like. Two were then checked against the rendered
     page: L07 is derived to start on folio 27, which is where the sharh opens
     section 1 with Surat al-Ikhlas; L12 to folio 47, which opens section 8 on
     Allah's pleasure and anger. Both are exactly what those lessons teach.

Folio offset
------------
OCR markers are 0-based PDF page indices; the printed folio is one higher.
Checked six ways, by rendering the page and reading the folio rather than
trusting OCR of the digits: indices 5, 26, 46, 187 and 201 carry folios 6, 27,
47, 188 and 202; and the book's own fihris puts karamat al-awliya' at 188,
the fasl on the qualities at 191 and the fasl on the completers at 196,
against derived indices 187, 190 and 195.

Usage:  python _wasprov.py            audit only
        python _wasprov.py --write    inject the line
"""
import io, os, re, sys, glob

sys.stdout.reconfigure(encoding='utf-8')

WRITE = '--write' in sys.argv
PRINT_OFFSET = 1
NGRAM = 12
FIHRIS_FROM = 203          # pages from here on are the index; never a source
AQ = 'pages/aqeedah'
OCR = 'assets/md/sharh-wasitiyyah-fawzan.md'

# L27's text peaks on index 98, inside L26's range, because it recaps L26's
# material before adding its own. The builder's own note (100-101) is what was
# actually read and is kept; recorded here so the discrepancy is not silent.
EXCEPTIONS = {'was-l27-arsh-jariyah.html':
              'peak 98 sits in L26 (recap); builder note 100-101 kept'}

# Lessons whose derived START page was confirmed by rendering the page and
# reading it, which is stronger evidence than the n-gram score. L12's score is
# low because most of its length is quoted ayat, which cannot match; folio 47
# nevertheless opens section 8, on Allah's pleasure and anger, which is the
# lesson's subject exactly.
VERIFIED = {'was-l07-ikhlas.html': 'folio 27 opens section 1 with Surat al-Ikhlas',
            'was-l12-rahmah-ghadab-maji.html':
                "folio 47 opens section 8 on Allah's pleasure and anger"}

MARKS = u'[ً-ْٰـۖ-ۭ]'
PRES = {u'ﻻ': u'لا', u'ﻷ': u'لا', u'ﻹ': u'لا',
        u'ﻵ': u'لا', u'ﷺ': u'', u'﷽': u''}


def norm(t):
    for a, b in PRES.items():
        t = t.replace(a, b)
    t = re.sub(MARKS, '', t)
    t = re.sub(u'[آأإٱ]', u'ا', t)
    t = t.replace(u'ى', u'ي').replace(u'ة', u'ه')
    return re.sub(u'[^ء-ي]', '', t)


def grams(s, n=NGRAM):
    return {s[i:i + n] for i in range(0, max(0, len(s) - n + 1))}


def lesson_arabic(h):
    """All the lesson's Arabic EXCEPT quoted ayat -- the sharh prints Qur'anic
    text in a decorative face that OCRs to noise, so ayat can never match and
    only dilute the score. Dropping them is what let L19, whose matn is
    entirely ayat, be located at all."""
    b = re.sub(r'<script.*?</script>|<style.*?</style>|<head>.*?</head>', '',
               h, flags=re.S | re.I)
    b = re.sub(r'<div class="ayah-block".*?</div>', '', b, flags=re.S)
    return norm(re.sub(r'<[^>]+>', ' ', b))


# ------------------------------------------------------------------- sources
pages = {}
parts = re.split(r'^## page (\d+)\s*$', io.open(OCR, encoding='utf-8').read(), flags=re.M)
for i in range(1, len(parts), 2):
    n = int(parts[i])
    if n < FIHRIS_FROM:
        pages[n] = grams(norm(parts[i + 1]))

recorded = {}
for bf in glob.glob('_was_*.py'):
    src = io.open(bf, encoding='utf-8').read()
    doc = src.split('"""')[1] if '"""' in src else ''
    mo = re.search(r"io\.open\(os\.path\.join\(B\.AQ,\s*'(was-l\d+[^']*\.html)'", src)
    mr = re.search(r'[Ss]harh\s*pp?\.\s*(\d+)\s*[-–]\s*(\d+)', doc)
    if mo and mr:
        recorded[mo.group(1)] = (int(mr.group(1)), int(mr.group(2)))

# ------------------------------------------------- peak page for every lesson
files = sorted(glob.glob(os.path.join(AQ, 'was-l*.html')))
peak = {}
for f in files:
    g = grams(lesson_arabic(io.open(f, encoding='utf-8').read()))
    sc = {p: len(g & pg) for p, pg in pages.items()}
    best = max(sc, key=lambda p: sc[p])
    peak[os.path.basename(f)] = (best, sc[best])

# ------------------------------------------------------- settle every range
order = [os.path.basename(f) for f in files]
final, how, flags = {}, {}, []
for i, b in enumerate(order):
    pk, strength = peak[b]
    if b in recorded:
        final[b] = recorded[b]
        how[b] = 'builder note'
        lo, hi = recorded[b]
        if not (lo <= pk <= hi):
            flags.append((b, 'peak %d outside noted %d-%d -- %s'
                          % (pk, lo, hi, EXCEPTIONS.get(b, 'UNEXPLAINED'))))
    else:
        nxt = None
        for b2 in order[i + 1:]:
            cand = recorded[b2][0] if b2 in recorded else peak[b2][0]
            if cand > pk:
                nxt = cand
                break
        final[b] = (pk, (nxt - 1) if nxt else pk)
        how[b] = 'derived'
        if strength < 20 and b not in VERIFIED:
            flags.append((b, 'weak text match (peak score %d) -- not published'
                          % strength))
            del final[b]
        elif b in VERIFIED:
            how[b] = 'derived+seen'

# ------------------------------------------------------------------- report
print('%-46s %-10s %-13s %-13s %s' % ('LESSON', 'INDEX', 'PRINTED', 'SOURCE', 'pk'))
print('-' * 96)
for b in order:
    if b not in final:
        print('%-46s %-10s %-13s %-13s %d  (omitted)' % (b[:46], '--', '--', '--', peak[b][1]))
        continue
    lo, hi = final[b]
    print('%-46s %-10s %-13s %-13s %d' % (
        b[:46], '%d-%d' % (lo, hi),
        u'ص %d-%d' % (lo + PRINT_OFFSET, hi + PRINT_OFFSET), how[b], peak[b][1]))

print('\n%d lessons · %d cited (%d from builder notes, %d derived) · %d omitted'
      % (len(order), len(final),
         sum(1 for b in final if how[b] == 'builder note'),
         sum(1 for b in final if how[b] == 'derived'),
         len(order) - len(final)))
for b, why in flags:
    print('   !! %-42s %s' % (b, why))

if not WRITE:
    print('\n(audit only -- pass --write to inject the reference line)')
    sys.exit(0)

# -------------------------------------------------------------------- write
AR_D = u'٠١٢٣٤٥٦٧٨٩'
MARK = '<!-- SHARH-PROVENANCE -->'
written = 0
for b in order:
    if b not in final:
        continue
    f = os.path.join(AQ, b)
    h = io.open(f, encoding='utf-8').read()
    h = re.sub(re.escape(MARK) + r'.*?' + re.escape(MARK) + r'\s*', '', h, flags=re.S)
    a, z = final[b][0] + PRINT_OFFSET, final[b][1] + PRINT_OFFSET
    arn = lambda n: ''.join(AR_D[int(c)] for c in str(n))
    ar_pp = (u'ص %s' % arn(a)) if a == z else (u'ص %s–%s' % (arn(a), arn(z)))
    en_pp = ('p. %d' % a) if a == z else ('pp. %d–%d' % (a, z))
    line = (
        MARK + '\n'
        '        <p style="font-size:.73rem;color:var(--ink-faint);line-height:1.8;'
        'margin:0 0 var(--space-lg);padding-bottom:var(--space-sm);'
        'border-bottom:1px solid var(--line)">\n'
        '          <span dir="rtl" lang="ar">شَرْحُ الشَّيْخِ صَالِحٍ الفَوْزَان · '
        '%s</span><br>\n'
        '          <em>Sharḥ al-ʿAqīdah al-Wāsiṭiyyah</em>, Ṣāliḥ al-Fawzān — %s.\n'
        '        </p>\n' % (ar_pp, en_pp)) + '        ' + MARK + '\n        '
    m = re.search(r'<div class="objectives-box"', h)
    if not m:
        print('   ?? %s: no objectives box to anchor to' % b)
        continue
    io.open(f, 'w', encoding='utf-8', newline='\n').write(h[:m.start()] + line + h[m.start():])
    written += 1
print('\nreference line written into %d lessons' % written)
