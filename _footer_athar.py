# -*- coding: utf-8 -*-
"""Add a verified, subject-fitting ayah to each tab hub footer (the 'guiding
light' line). Fiqh already carries an athar of Yahya ibn Abi Kathir and is left
alone. Each Qur'anic line is wrapped as <span dir="rtl" lang="ar">...</span>
followed by a (Name n:m) citation so _verifyayat.py checks it against the mushaf.

Idempotent: a footer that already has class="footer-athar" is skipped.
"""
import io, sys
sys.stdout.reconfigure(encoding='utf-8')

# relpath -> (arabic ayah, english gloss, citation shown in parens)
TABS = {
    'pages/islam101/index.html': (
        'وَمَا خَلَقْتُ الْجِنَّ وَالْإِنْسَ إِلَّا لِيَعْبُدُونِ',
        'I did not create jinn and mankind except to worship Me.',
        'al-Dhāriyāt 51:56'),
    'pages/aqeedah/index.html': (
        'فَاعْلَمْ أَنَّهُ لَا إِلَٰهَ إِلَّا اللَّهُ',
        'So know that there is no god but Allah.',
        'Muḥammad 47:19'),
    'pages/hadeeth/index.html': (
        'وَمَا يَنطِقُ عَنِ الْهَوَىٰ ۝ إِنْ هُوَ إِلَّا وَحْيٌ يُوحَىٰ',
        'Nor does he speak from desire; it is but a revelation revealed.',
        'al-Najm 53:3-4'),
    'pages/seerah/index.html': (
        'لَقَدْ كَانَ لَكُمْ فِي رَسُولِ اللَّهِ أُسْوَةٌ حَسَنَةٌ',
        'In the Messenger of Allah you have an excellent example.',
        'al-Aḥzāb 33:21'),
    'pages/quran/index.html': (
        'كِتَابٌ أَنزَلْنَاهُ إِلَيْكَ مُبَارَكٌ لِّيَدَّبَّرُوا آيَاتِهِ',
        'A blessed Book We have revealed to you, that they may ponder its verses.',
        'Ṣād 38:29'),
    'pages/arabic/index.html': (
        'إِنَّا أَنزَلْنَاهُ قُرْآنًا عَرَبِيًّا لَّعَلَّكُمْ تَعْقِلُونَ',
        'We have sent it down as an Arabic Qurʾān, that you may understand.',
        'Yūsuf 12:2'),
    'pages/grammar/index.html': (
        'وَقُل رَّبِّ زِدْنِي عِلْمًا',
        'And say: My Lord, increase me in knowledge.',
        'Ṭā Hā 20:114'),
    'pages/resources/index.html': (
        'يَرْفَعِ اللَّهُ الَّذِينَ آمَنُوا مِنكُمْ وَالَّذِينَ أُوتُوا الْعِلْمَ دَرَجَاتٍ',
        'Allah raises those who believe among you, and those given knowledge, by degrees.',
        'al-Mujādilah 58:11'),
}

ANCHOR = '<footer class="site-footer">'

for rel, (ar, en, cite) in TABS.items():
    h = io.open(rel, encoding='utf-8').read()
    if 'footer-athar' in h:
        print('%-34s already has an athar — skipped' % rel)
        continue
    assert h.count(ANCHOR) == 1, '%s: expected exactly one footer' % rel
    block = (ANCHOR
             + '\n  <p class="footer-athar" style="font-family:var(--font-arabic);'
               'font-size:1.3rem;color:#fff;font-weight:600;direction:rtl;'
               'line-height:1.7;margin-bottom:4px">'
               '<span dir="rtl" lang="ar">' + ar + '</span></p>'
             + '\n  <p style="color:rgba(255,255,255,0.72);max-width:560px;'
               'margin:0 auto var(--space-lg)">“' + en + '” ('
             + cite + ')</p>')
    io.open(rel, 'w', encoding='utf-8', newline='\n').write(h.replace(ANCHOR, block, 1))
    print('%-34s + %s' % (rel, cite))

print('\ndone')
