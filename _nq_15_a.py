# -*- coding: utf-8 -*-
"""Lesson 15, part A — the book's own heading: الاسْتِعَانَةُ بِالكُفَّارِ عَلَى الكُفَّار.

Printed folios 205-208 of this part. The eighth nullifier's second half opens
not with a new prohibition but with a **permission**, and Ibn Bāz applies it to
a named contemporary case in his own words. Then the ijmāʿ on the thing that
IS the nullifier, with its transmitters named; then the first of the three
excuses the sharḥ refuses — kinship.
"""
from _nq_15_lib import B, p, ar, box, row, row3, thead3, table, qa

BODY = B.objectives([
    'State the permission the sharḥ opens this half with — %s — and the one '
    'thing it says is <strong>not</strong> permitted, in his own words.'
    % ar('الاسْتِعَانَةُ بِالكُفَّارِ عَلَى الكُفَّار'),
    'Give the <strong>ijmāʿ</strong> on backing the disbelievers against the '
    'Muslims, and <strong>name</strong> the scholars the sharḥ cites as having '
    'transmitted it.',
    'State the three excuses the sharḥ refuses one after another — '
    '<strong>kinship</strong>, <strong>fear</strong>, and '
    '<strong>nationality</strong> — and the reason each is refused.',
    'Give the <strong>three categories of people</strong> he divides mankind '
    'into, and say what is owed to the third.',
    'Say why residence among the mushrikīn is treated in this clause at all, '
    'and what al-Nisāʾ 4:97–99 was revealed about.',
    'State what %s obliges a Muslim to <em>give</em> another Muslim — the '
    'clause read forwards, not only backwards.' % ar('الوِلَايَة'),
    'Give the ruling on the <strong>spy</strong>, and the <em>two</em> things '
    'the sharḥ says prevented it in the case of Ḥāṭib.',
    'Say where the scholars named on these folios <strong>disagree</strong> '
    'about whether anyone after Ḥāṭib can be treated as Ḥāṭib was.',
])

BODY += B.provenance(205, 222)

BODY += B.prose(
    '<strong>This is the second half of the eighth nullifier.</strong> The '
    'first half settled the distinction the whole clause turns on — '
    '«<span dir="rtl" lang="ar">المُوَالَاةُ مَعْصِيَة، وَالتَّوَلِّي '
    'كُفْر</span>» — and the sharḥ now spends eighteen folios on what sits on '
    'either side of the line. <em>It does not begin where a reader braced for '
    'the harshest clause in the book would expect it to begin.</em> '
    '<strong>It begins with a permission</strong>, under a heading the book '
    'prints itself.')

# ------------------------------------------------- al-istiʿānah bi-l-kuffār
BODY += B.heading('الاسْتِعَانَةُ بِالكُفَّارِ عَلَى الكُفَّار',
                  'Seeking the Help of Disbelievers Against Disbelievers')
BODY += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><em>«And what is '
        '<strong>not</strong> permitted is that he give the disbelievers '
        'victory over the Muslims.»</em></p>'
        '<p style="margin:0;font-size:.93rem"><span dir="rtl" lang="ar">'
        '«وَالَّذِي لَا يَجُوزُ هُوَ أَنْ يَنْصُرَ الكُفَّارَ عَلَى '
        'المُسْلِمِين.»</span></p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>Then he applies it to a case of his own lifetime, by name.</strong> '
      '<em>«As for what took place of seeking the help of some of the '
      'disbelievers <strong>against Ṣaddām</strong> — that is of what protects '
      'the Muslims and their lands from the criminals and the aggressors and '
      'the disbelievers. <strong>وَفَرْقٌ بَيْنَ الاثْنَيْن</strong> — and '
      'there is a difference between the two: between this, and a man who gives '
      'the disbelievers victory over the Muslims and aids them against the '
      'Muslims — <strong>وَهَذِهِ هِيَ الرِّدَّةُ عَنِ الإِسْلَام</strong>, '
      'and this is the apostasy from Islām.»</em>') +
    p('And again, plainly: <em>«<strong>لَا بَأْسَ</strong> أَنْ يَسْتَعِينَ '
      'المُسْلِمُونَ بِغَيْرِهِمْ لِلدِّفَاعِ عَنْ بِلَادِ المُسْلِمِينَ '
      'وَحِمَايَتِهِمْ ضِدَّ العُدْوَانِ عَنْهُم؛ وَلَيْسَ هَذَا مِنْ نَصْرِ '
      'الكُفَّارِ عَلَى المُسْلِمِينَ الَّذِي ذَكَرَهُ العُلَمَاءُ فِي بَابِ '
      'حُكْمِ المُرْتَدّ؛ <strong>فَذَاكَ أَنْ يَنْصُرَ المُسْلِمُ الكَافِرَ '
      'عَلَى إِخْوَانِهِ المُسْلِمِين</strong>، فَهَذَا هُوَ الَّذِي لَا '
      'يَجُوز.»</em>'))
BODY += B.prose(
    '<strong>Read what he has just done, because it is the method of the whole '
    'clause.</strong> The books of fiqh have a chapter called '
    '«<span dir="rtl" lang="ar">بَابُ حُكْمِ المُرْتَدّ</span>» in which '
    '«aiding the disbelievers» appears as a nullifier. He is asked about a '
    'live case that <em>looks</em> like it, and instead of reasoning from the '
    'resemblance he goes back to <strong>what the chapter was about</strong>: '
    '<em>a Muslim giving a disbeliever victory over his Muslim brothers.</em> '
    '<strong>The direction the harm runs in is the whole ruling.</strong> '
    'Turn it the other way and the same act is defence of Muslim land.')

# --------------------------------------------------------------- the ijmāʿ
BODY += B.heading('الإِجْمَاعُ عَلَى النَّاقِض', 'The Ijmāʿ on What the Nullifier Is')
BODY += B.prose(
    '<strong>Having fenced what the clause is not, the sharḥ states what it '
    'is — and states it as ijmāʿ.</strong>')
BODY += B.sharh(
    box('<p style="margin:0;font-size:.96rem"><span dir="rtl" lang="ar">'
        '«وَقَدْ أَجْمَعَ عُلَمَاءُ الإِسْلَامِ عَلَى أَنَّ مَنْ ظَاهَرَ '
        'الكُفَّارَ عَلَى المُسْلِمِينَ وَسَاعَدَهُمْ عَلَيْهِمْ '
        '<strong>بِأَيِّ نَوْعٍ مِنَ المُسَاعَدَة</strong> فَهُوَ كَافِرٌ '
        'مِثْلُهُم.»</span></p>') +
    p('<em>A claim of ijmāʿ is worth exactly as much as the transmitters behind '
      'it, so the sharḥ names them:</em>') +
    table([
        thead3('who', 'where', 'what he says'),
        row3('<strong>ابْنُ حَزْم</strong>',
             '<em>المُحَلَّى</em>',
             '«وَصَحَّ أَنَّ قَوْلَ اللهِ تَعَالَى ﴿وَمَنْ يَتَوَلَّهُمْ '
             'مِنْكُمْ فَإِنَّهُ مِنْهُمْ﴾ إِنَّمَا هُوَ عَلَى ظَاهِرِهِ '
             'بِأَنَّهُ كَافِرٌ مِنْ جُمْلَةِ الكُفَّارِ فَقَط؛ '
             '<strong>وَهَذَا حَقٌّ لَا يَخْتَلِفُ فِيهِ اثْنَانِ مِنَ '
             'المُسْلِمِين</strong>.»'),
        row3('<strong>ابْنُ بَاز</strong>, on Ibn Ḥazm',
             '<em>أَسْئِلَةُ الجَامِعِ الكَبِير</em>',
             '«أَبُو مُحَمَّدِ بْنُ حَزْمٍ هُوَ <strong>مِنْ أَعْلَمِ '
             'النَّاسِ بِالإِجْمَاعِ وَالخِلَاف</strong>.» <em>— which is why '
             'his transmission is cited first.</em>'),
        row3('<strong>الإِمَامُ مُحَمَّدُ بْنُ عَبْدِ الوَهَّاب</strong>',
             '<em>الدُّرَرُ السَّنِيَّة</em> · '
             '<em>مَجْمُوعَةُ الرَّسَائِلِ وَالمَسَائِلِ النَّجْدِيَّة</em>',
             '«وَاعْلَمْ أَنَّ الأَدِلَّةَ عَلَى تَكْفِيرِ المُسْلِمِ '
             'الصَّالِحِ إِذَا أَشْرَكَ بِاللهِ أَوْ صَارَ مَعَ '
             'المُشْرِكِينَ عَلَى المُوَحِّدِينَ — <strong>وَلَوْ لَمْ '
             'يُشْرِك</strong> — أَكْثَرُ مِنْ أَنْ تُحْصَرَ مِنْ كَلَامِ '
             'اللهِ وَكَلَامِ رَسُولِهِ وَكَلَامِ أَهْلِ العِلْمِ '
             'كُلِّهِم.» <em>— the author of the matn, on his own clause.</em>'),
    ]) +
    p('<em>Note the four words inside the Imām’s sentence that are easy to '
      'read past:</em> <strong>«وَلَوْ لَمْ يُشْرِك»</strong>. <em>He is not '
      'saying the man committed shirk. He is saying this is a separate '
      'nullifier with its own door, and a man may walk through it while his '
      'tawḥīd is intact.</em>'))

# ------------------------------------------------------- excuse 1: kinship
BODY += B.heading('الأَعْذَارُ الَّتِي يَرُدُّهَا الشَّرْح',
                  'The Excuses the Sharḥ Refuses')
BODY += B.prose(
    '<strong>Three excuses are raised on these folios and refused one after '
    'another.</strong> <em>Take them in the order the sharḥ takes them, '
    'because they run from the most sympathetic to the most organised.</em> '
    '<strong>The first is kinship</strong> — and it is the most sympathetic '
    'excuse there is, because the man is not claiming to love their religion. '
    'He is claiming to be afraid for his children.')
BODY += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><em>«Whoever gives the '
        'disbelievers victory over the Muslims — <strong>even if he claims it '
        'is for the sake of looking after relatives of his and children of '
        'his</strong> — this does not benefit him; because backing the '
        'disbelievers against the Muslims and aiding them against the Muslims '
        'is <strong>tawallī</strong> of them and apostasy '
        '<strong>عِنْدَ جَمِيعِ أَهْلِ العِلْم</strong>.»</em></p>') +
    p('<em>And the footnote sends the reader to a verse, which is the better '
      'half of the answer.</em> Al-ʿAllāmah <strong>عَبْدُ اللَّطِيفِ بْنُ '
      'عَبْدِ الرَّحْمَنِ بْنِ حَسَن</strong>, in <em>مِصْبَاحُ '
      'الظَّلَام</em>, on al-Nisāʾ 4:91 — <em>«the verse’s indication of '
      'this question is plain:</em> «فَإِنَّ مَنْ تَكَلَّمَ بِالإِسْلَامِ '
      'وَلَمْ يَعْتَزِلْ أَهْلَ الكُفْرِ بَلْ صَارَ مَعَهُمْ وَقَاتَلَ '
      'أَهْلَ التَّوْحِيدِ <strong>لِغَرَضٍ مِنْ أَغْرَاضِهِ '
      'الدُّنْيَوِيَّة</strong> تَنَاوَلَتْهُ الآيَةُ وَشَمِلَهُ ذَمُّهَا '
      'الصَّرِيح؛ وَقَدْ جَعَلَ اللهُ لِحَقْنِ دَمِهِ <strong>حَدًّا '
      'وَفِعْلًا يَتَمَيَّزُ بِهِ إِسْلَامُه</strong>، وَهُوَ '
      '<strong>اعْتِزَالُ قِتَالِ المُسْلِمِين</strong>.»'))
BODY += B.ayah(
    'سَتَجِدُونَ آخَرِينَ يُرِيدُونَ أَن يَأْمَنُوكُمْ وَيَأْمَنُوا '
    'قَوْمَهُمْ كُلَّمَا رُدُّوا إِلَى الْفِتْنَةِ أُرْكِسُوا فِيهَا',
    'You will find others who wish to be secure from you and secure from their '
    'own people. Every time they are returned to temptation, they plunge into '
    'it.',
    'سُورَةُ النِّسَاء · 4:91')
BODY += B.prose(
    '<strong>That is the sharpest sentence in the footnote, and it is a mercy, '
    'not a threat.</strong> A man in a land at war with the Muslims, under '
    'pressure, with his family in reach of people who will hurt them, wants to '
    'know what keeps him a Muslim. He is not told to prove his heart. He is '
    'given <strong>one act</strong> — «<span dir="rtl" lang="ar">اعْتِزَالُ '
    'قِتَالِ المُسْلِمِين</span>», <em>withdrawing from fighting the '
    'Muslims</em> — and told that this is the <em>line drawn for the '
    'protection of his own blood</em>. <strong>Do that, and whatever else is '
    'true of you, you are not in this clause.</strong>')
