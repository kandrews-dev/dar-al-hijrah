# -*- coding: utf-8 -*-
"""Shared pieces for the Nawāqiḍ al-Islām depth track.

The matn is Imām Muḥammad ibn ʿAbd al-Wahhāb's ten nullifiers. The sharḥ is
«سُبُلُ السَّلَام شَرْحُ نَوَاقِضِ الإِسْلَام», which is not a lecture but a
COMPILATION of Shaykh Ibn Bāz's own words on each clause, footnoted to
Majmūʿ al-Fatāwā by volume and page. Attribution on the pages says exactly
that, because calling it "Ibn Bāz's sharḥ" would overstate what the book is.

Folio offset for this file is **+3** — PDF index 16 carries printed folio 19,
verified by rendering the page. That is a fourth distinct offset across four
source books, which is why the citation standard verifies per file.

Lessons live in pages/aqeedah/ beside the existing u6-nawaqid.html overview,
which stays where it is: six pages link to it.
"""
import io, os, re, importlib.util

BASE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('mb', os.path.join(BASE, '_mutunbuild.py'))
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)

AQ = M.AQ
PRINT_OFFSET = 3

objectives = M.objectives
heading = M.heading
prose = M.prose
ayah = M.ayah
hadith = M.hadith
matn = M.matn
sharh = M.sharh
vocab = M.vocab
mcq = M.mcq
tf = M.tf
memorize = M.memorize
nav = M.nav

FOOT = ('نَوَاقِضُ الإِسْلَام of Imām Muḥammad ibn ʿAbd al-Wahhāb · explained from '
        'the words of Shaykh Ibn Bāz · in our own words')

READING = [
    '<em>سُبُلُ السَّلَام شَرْحُ نَوَاقِضِ الإِسْلَام</em> — the ten nullifiers '
    'explained throughout from the words of Shaykh '
    '<strong>عَبْدُ العَزِيزِ بْنُ بَاز</strong>, footnoted to '
    '<em>مَجْمُوعُ الفَتَاوَى</em>.',
]


def init():
    M.set_source(os.path.join(AQ, 'u6-nawaqid.html'))
    M.FOOT = FOOT
    M.READING = READING


init()


def shell(title_ar, title_en, desc, body):
    pre = re.sub(r'<title>.*?</title>',
                 u'<title>%s — %s | العقيدة | دار الهجرة</title>' % (title_ar, title_en),
                 M.PRE, flags=re.S)
    pre = re.sub(r'(<meta name="description" content=")(.*?)(">)',
                 lambda m: m.group(1) + desc + m.group(3), pre, count=1, flags=re.S)
    post = re.sub(r'(<footer class="site-footer">.*?<p>)(.*?)(</p>)',
                  lambda m: m.group(1) + FOOT + m.group(3), M.POST, count=1, flags=re.S)
    return pre + u'<main>\n' + body + u'\n' + post


def card(label, year, tar, ten, inner):
    return M.card(label, year, tar, ten, inner,
                  back=u'u6-nawaqid.html', back_label=u'نَوَاقِضُ الإِسْلَام')


MARK = '<!-- SHARH-PROVENANCE -->'
AR_D = u'٠١٢٣٤٥٦٧٨٩'


def provenance(first, last=None):
    """first/last are PRINTED folios (index + 3), not PDF indices."""
    last = first if last is None else last
    arn = lambda n: ''.join(AR_D[int(c)] for c in str(n))
    ar_pp = (u'ص %s' % arn(first)) if first == last else (
        u'ص %s–%s' % (arn(first), arn(last)))
    en_pp = ('p. %d' % first) if first == last else ('pp. %d–%d' % (first, last))
    return (MARK + '\n'
            '        <p style="font-size:.73rem;color:var(--ink-faint);line-height:1.8;'
            'margin:0 0 var(--space-lg);padding-bottom:var(--space-sm);'
            'border-bottom:1px solid var(--line)">\n'
            '          <span dir="rtl" lang="ar">مِنْ كَلَامِ الشَّيْخِ ابْنِ بَاز · '
            '%s</span><br>\n'
            '          <em>Subul al-Salām Sharḥ Nawāqiḍ al-Islām</em> — %s, '
            'gathering Ibn Bāz’s words on this clause.\n'
            '        </p>\n        ' % (ar_pp, en_pp)) + MARK + '\n'


def write(filename, title_ar, title_en, desc, label, year, body):
    path = os.path.join(AQ, filename)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(
        shell(title_ar, title_en, desc, card(label, year, title_ar, title_en, body)))
    return path
