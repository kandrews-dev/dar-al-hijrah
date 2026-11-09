# -*- coding: utf-8 -*-
"""Rule 1a debt on the Nawāqiḍ overview page: eleven bare Arabic words.

These are the overview page's own muṣṭalaḥāt cards, its breadcrumb and its
memorize label — chrome that the 2026-10-11 ḥarakāt pass left for a reading
pass because the grammar/term vocabulary needed deciding word by word. The
replacements below are whole-token, so the data-ar attribute and the visible
span are both corrected by the same substitution.

One of them is not only bare but duplicated in the original: the memorize
label read «اِحْفَظْ واحفظ نفسك», which is the vowelled word followed by an
unvowelled repetition of itself. Corrected to «اِحْفَظْ وَاحْفَظْ نَفْسَك».
"""
import io

F = 'pages/aqeedah/u6-nawaqid.html'
h = io.open(F, encoding='utf-8').read()

PAIRS = [
    ('اِحْفَظْ واحفظ نفسك', 'اِحْفَظْ وَاحْفَظْ نَفْسَك'),
    ('قاعدة مهمة', 'قَاعِدَةٌ مُهِمَّة'),
    ('"ناقض"', '"نَاقِض"'),
    ('>ناقض<', '>نَاقِض<'),
    ('"التكفير"', '"التَّكْفِير"'),
    ('>التكفير<', '>التَّكْفِير<'),
    ('"الواسطة"', '"الوَاسِطَة"'),
    ('>الواسطة<', '>الوَاسِطَة<'),
    ('"الاستهزاء"', '"الاسْتِهْزَاء"'),
    ('>الاستهزاء<', '>الاسْتِهْزَاء<'),
    ('"السحر"', '"السِّحْر"'),
    ('>السحر<', '>السِّحْر<'),
    ('"الإكراه"', '"الإِكْرَاه"'),
    ('>الإكراه<', '>الإِكْرَاه<'),
    ('← العقيدة · Aqeedah', '← العَقِيدَة · Aqeedah'),
]

for old, new in PAIRS:
    n = h.count(old)
    if not n:
        raise SystemExit('anchor not found: %r' % old)
    h = h.replace(old, new)
    print('%-28s x%d' % (old, n))

io.open(F, 'w', encoding='utf-8', newline='\n').write(h)
print('patched', F)
