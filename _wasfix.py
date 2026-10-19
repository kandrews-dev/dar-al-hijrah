# -*- coding: utf-8 -*-
"""Pre-existing defects in older Wasitiyyah lessons, surfaced by the audit that
ran after the provenance pass. Two classes:

  1. Rule 1a misses -- Arabic words left unvowelled, mostly in places the
     harakat pass does not reach: objective bullets, flashcard data- attributes,
     MCQ option text and section headings.
  2. One real structural fault -- L34 opens a <strong> and never closes it
     before opening a nested one, so everything after it inherited bold. Found
     with an HTML parser; the regex counter that first flagged it also reported
     two phantom <em> faults in L14 and L18 which the parser cleared.
"""
import io, re, sys
sys.stdout.reconfigure(encoding='utf-8')

EDITS = [
    # ------------------------------------------------------- rule 1a misses
    ('was-l01-basmalah.html',
     u'derivation of the name <span dir="rtl" lang="ar">الله</span>',
     u'derivation of the name <span dir="rtl" lang="ar">اللهُ</span>'),

    ('was-l06-nafy-ithbat.html',
     u'A verbal noun of تسبيح',
     u'A verbal noun of تَسْبِيح'),

    # The disconnected letters of al-Sajdah. Written with the maddah, which is
    # how the mushaf marks them and what tells the student they are spelled out
    # alif-lam-mim rather than read as a word.
    ('was-l16-istiwa-uluww.html',
     u'وَقَالَ فِي سُورَةِ الم السَّجْدَةِ',
     u'وَقَالَ فِي سُورَةِ «الٓمٓ» السَّجْدَةِ'),

    ('was-l19-quran-kalam-allah.html',
     u'<span class="sh-ar">٥ · القُرْآنُ كَلَامُ الله</span>',
     u'<span class="sh-ar">٥ · القُرْآنُ كَلَامُ اللهِ</span>'),

    ('was-l20-tanzil-quran.html',
     u'واللهُ أعلم.',
     u'وَاللهُ أَعْلَم.'),

    ('was-l25-qadam-nida-sawt.html',
     u'That جهنم is a proper name',
     u'That جَهَنَّم is a proper name'),

    ('was-l26-uluww-sunnah.html',
     u'<span dir="rtl" lang="ar">رَحْمَةُ الله</span>',
     u'<span dir="rtl" lang="ar">رَحْمَةُ اللهِ</span>'),

    ('was-l34-quran-kalam-haqiqatan.html',
     u'data-definition="أزلي أبدي — beginningless and endless"',
     u'data-definition="أَزَلِيٌّ أَبَدِيٌّ — beginningless and endless"'),

    # ------------------------------------------------------ structural fault
    # The <strong> opened at "returns to Allah" ran on past a nested one and
    # was never closed. It belongs to the clause about the Qur'an being raised
    # up; close it where that clause ends.
    ('was-l34-quran-kalam-haqiqatan.html',
     u'neither in the breasts nor in the copies — <strong>and that is among '
     u'the signs of the Hour</strong>',
     u'neither in the breasts nor in the copies</strong> — <strong>and that is '
     u'among the signs of the Hour</strong>'),
]

for base, old, new in EDITS:
    f = 'pages/aqeedah/' + base
    h = io.open(f, encoding='utf-8').read()
    n = h.count(old)
    assert n == 1, '%s: %d matches for %r' % (base, n, old[:60])
    io.open(f, 'w', encoding='utf-8', newline='\n').write(h.replace(old, new))
    print('  fixed  %-42s %s' % (base[:42], old[:46].replace('\n', ' ')))
print('%d edits' % len(EDITS))
