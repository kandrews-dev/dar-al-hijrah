# -*- coding: utf-8 -*-
"""Page builders for the Ḥadīth track (al-Arbaʿūn al-Nawawiyyah).

Wraps _mutunbuild for everything the two tracks share — objectives, headings,
prose, āyah blocks, MCQ, T/F, memorize, nav — and overrides the handful of
things the Ḥadīth pages do differently:

  * the chrome is inherited from an existing ḥadīth page, not an ʿaqīdah one
  * <title> reads «الحديث», not «العقيدة»
  * the lesson card backs out to the ḥadīth index
  * hadith_block() — the matn with its translation and takhrīj, which is this
    track's equivalent of the ʿaqīdah track's matn() block
  * vocab() carries data-root and data-example, which the existing ḥadīth pages
    use and the ʿaqīdah ones do not

The track targets **42** ḥadīth, not 40: an-Nawawī left 42, and the last two
are the ones Ibn Rajab carried into Jāmiʿ al-ʿUlūm wa-l-Ḥikam. The existing
pages already read "of 42", so new pages keep that count.
"""
import io, os, re, importlib.util

BASE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('mb', os.path.join(BASE, '_mutunbuild.py'))
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)

HD = os.path.join(BASE, 'pages', 'hadeeth')

# Shared, unchanged
objectives = M.objectives
heading = M.heading
prose = M.prose
ayah = M.ayah
mcq = M.mcq
tf = M.tf
memorize = M.memorize
nav = M.nav

TOTAL = 42

FOOT = ('al-Arbaʿūn al-Nawawiyyah · sharḥ of Shaykh Muḥammad ibn Ṣāliḥ '
        'al-ʿUthaymīn · in our own words')

READING = [
    'Shaykh <strong>مُحَمَّدُ بْنُ صَالِحٍ العُثَيْمِين</strong>, '
    '<em>شَرْحُ الأَرْبَعِينَ النَّوَوِيَّة</em> — the sharḥ this track follows.',
    'al-Ḥāfiẓ <strong>ابْنُ رَجَبٍ الحَنْبَلِيّ</strong>, '
    '<em>جَامِعُ العُلُومِ وَالحِكَم</em> — consulted where the sharḥ is brief.',
]


def init():
    """Point the chrome at an existing ḥadīth page so nav and footer match."""
    M.set_source(os.path.join(HD, 'h15-qul-khayran.html'))
    M.FOOT = FOOT
    M.READING = READING


init()


def shell(title_ar, title_en, desc, body):
    """As M.shell, but with the ḥadīth section name in <title>."""
    pre = re.sub(r'<title>.*?</title>',
                 u'<title>%s — %s | الحديث | دار الهجرة</title>' % (title_ar, title_en),
                 M.PRE, flags=re.S)
    pre = re.sub(r'(<meta name="description" content=")(.*?)(">)',
                 lambda m: m.group(1) + desc + m.group(3), pre, count=1, flags=re.S)
    post = re.sub(r'(<footer class="site-footer">.*?<p>)(.*?)(</p>)',
                  lambda m: m.group(1) + FOOT + m.group(3), M.POST, count=1, flags=re.S)
    return pre + u'<main>\n' + body + u'\n' + post


def card(num, grading, year, tar, ten, inner):
    """num = ḥadīth number; grading = e.g. 'Agreed upon' or 'Muslim'."""
    return M.card(u'Ḥadīth %d of %d · %s' % (num, TOTAL, grading),
                  year, tar, ten, inner,
                  back=u'index.html', back_label=u'الحَدِيث · Hadeeth')


def hadith_block(ar, en, src):
    """The matn, its translation, and the takhrīj line. Rule 8 lives here:
    `src` must name the collection AND, where the grading is not carried by
    inclusion in the Ṣaḥīḥayn, the scholar who graded it."""
    return (u'\n        <div class="hadith-block">\n'
            u'          <p class="hadith-arabic">%s</p>\n'
            u'          <p class="hadith-translation">%s</p>\n'
            u'          <p class="hadith-source">%s</p>\n'
            u'        </div>\n') % (ar, en, src)


def vocab(cards):
    """cards = [(arabic, translit, english, root, definition, example), ...]"""
    out = []
    for arw, tr, en, root, df, ex in cards:
        out.append(u'          <div class="vocab-card" data-ar="%s" data-translit="%s" '
                   u'data-en="%s" data-root="%s" data-definition="%s" data-example="%s">\n'
                   u'            <span class="vocab-ar">%s</span>'
                   u'<span class="vocab-transliteration">%s</span>'
                   u'<span class="vocab-en">%s</span>\n'
                   u'          </div>' % (arw, tr, en, root, df, ex, arw, tr, en))
    return (heading(u'المُفْرَدَات', u'Key Vocabulary — tap to flip')
            + u'        <div class="vocab-grid">\n' + u'\n'.join(out)
            + u'\n        </div>\n')


MARK = '<!-- SHARH-PROVENANCE -->'
AR_D = u'٠١٢٣٤٥٦٧٨٩'


def provenance(first, last=None):
    """The reference line, per the citation standard.

    `first`/`last` are PRINTED folios of the Arabic ʿUthaymīn sharḥ, NOT PDF
    indices — that file's offset is -1 (PDF index 40 carries folio 39, index 41
    carries 40), verified by rendering the pages. Convert before calling.
    """
    last = first if last is None else last
    arn = lambda n: ''.join(AR_D[int(c)] for c in str(n))
    ar_pp = (u'ص %s' % arn(first)) if first == last else (
        u'ص %s–%s' % (arn(first), arn(last)))
    en_pp = ('p. %d' % first) if first == last else ('pp. %d–%d' % (first, last))
    return (MARK + '\n'
            '        <p style="font-size:.73rem;color:var(--ink-faint);line-height:1.8;'
            'margin:0 0 var(--space-lg);padding-bottom:var(--space-sm);'
            'border-bottom:1px solid var(--line)">\n'
            '          <span dir="rtl" lang="ar">شَرْحُ الشَّيْخِ ابْنِ عُثَيْمِين · '
            '%s</span><br>\n'
            '          <em>Sharḥ al-Arbaʿīn al-Nawawiyyah</em>, Ibn ʿUthaymīn — %s.\n'
            '        </p>\n        ' % (ar_pp, en_pp)) + MARK + '\n'


def write(filename, title_ar, title_en, desc, num, grading, year, body):
    path = os.path.join(HD, filename)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(
        shell(title_ar, title_en, desc, card(num, grading, year, title_ar, title_en, body)))
    return path
