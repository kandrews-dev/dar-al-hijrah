# -*- coding: utf-8 -*-
"""Lesson 15, part D — the book's second printed heading on these folios:
وُجُوبُ التَّنَاصُرِ وَالتَّعَاضُدِ بَيْنَ المُؤْمِنِين.

Printed folios 208-214, under a heading the book sets in type itself. The
eighth nullifier is read everywhere as a list of what a Muslim may not do with
disbelievers. The sharḥ turns it over and spends six folios on what he OWES
believers — and makes the nationalism condemned a few folios earlier
worthless in the other direction too.
"""
from _nq_15_lib import B, p, ar, box, row, row3, thead3, table, qa

BODY = B.heading('وُجُوبُ التَّنَاصُرِ وَالتَّعَاضُدِ بَيْنَ المُؤْمِنِين',
                 'The Obligation of Mutual Support Between the Believers')
BODY += B.prose(
    '<strong>This heading is the book’s own, printed on the folio, and '
    'its placement is the argument.</strong> <em>Walāʾ has two faces, and a '
    'reader who has learned only the prohibition has learned one of them. '
    'The sharḥ sets the two verses side by side the way the sūrah does.</em>')
BODY += B.ayah(
    'الْمُنَافِقُونَ وَالْمُنَافِقَاتُ بَعْضُهُم مِّن بَعْضٍ يَأْمُرُونَ '
    'بِالْمُنكَرِ وَيَنْهَوْنَ عَنِ الْمَعْرُوفِ وَيَقْبِضُونَ '
    'أَيْدِيَهُمْ نَسُوا اللَّهَ فَنَسِيَهُمْ',
    'The hypocrite men and the hypocrite women are of one another. They enjoin '
    'what is wrong and forbid what is right, and they close their hands. They '
    'have forgotten Allah, so He has forgotten them.',
    'سُورَةُ التَّوْبَة · 9:67')
BODY += B.ayah(
    'وَالْمُؤْمِنُونَ وَالْمُؤْمِنَاتُ بَعْضُهُمْ أَوْلِيَاءُ بَعْضٍ '
    'يَأْمُرُونَ بِالْمَعْرُوفِ وَيَنْهَوْنَ عَنِ الْمُنكَرِ',
    'And the believing men and the believing women are allies of one another. '
    'They enjoin what is right and forbid what is wrong.',
    'سُورَةُ التَّوْبَة · 9:71')
BODY += B.sharh(
    p('«وَمِنَ الآيَاتِ الجَامِعَةِ قَوْلُهُ سُبْحَانَه: '
      '﴿وَالمُؤْمِنُونَ وَالمُؤْمِنَاتُ بَعْضُهُمْ أَوْلِيَاءُ بَعْضٍ﴾ — '
      '<strong>هَذِهِ آيَةٌ جَامِعَة</strong>… '
      '<strong>ضِدَّ المُنَافِقِين</strong>؛ المُنَافِقُونَ ذَكَرَهُمْ '
      'قَبْلَ ذَلِك… أَمَّا المُؤْمِنُونَ فَهُمْ ضِدَّ المُنَافِقِين: '
      '<strong>إِخْلَاصٌ لِلهِ وَإِيمَانٌ بِاللهِ وَصِدْقٌ فِي '
      'المُعَامَلَةِ وَتَعَاوُنٌ عَلَى البِرِّ وَالتَّقْوَى</strong>.»') +
    p('<em>Then he puts the verse in the second person, which is where it '
      'stops being a description:</em> «فَإِذَا كُنْتَ وَلِيَّ أَخِيكَ '
      'وَأُخْتِكَ فِي الله، وَهُوَ وَلِيُّكَ وَهِيَ وَلِيَّتُكَ أَيْضًا — '
      '<strong>وَجَبَ أَدَاءُ حَقِّ هَذِهِ الوِلَايَة</strong>.»') +
    box('<p style="margin:0 0 .4rem;font-size:.95rem"><em>«And this walāyah '
        '<strong>requires</strong>: sincere counsel, direction, help toward '
        'good, and the absence of envy, of deceit, of betrayal, of '
        'wrong-doing.»</em></p>'
        '<p style="margin:0 0 .4rem;font-size:1rem"><span dir="rtl" lang="ar">'
        '«<strong>فَكَيْفَ تَظْلِمُهُ؟ كَيْفَ تَغُشُّهُ؟ وَكَيْفَ '
        'تَخُونُهُ؟ كَيْفَ تَكْذِبُ عَلَيْهِ وَهُوَ '
        'أَخُوك؟</strong>»</span></p>'
        '<p style="margin:0;font-size:.93rem"><em>«So if any of that occurs, '
        'that is a <strong>deficiency in faith</strong> and a '
        '<strong>weakness in this walāyah</strong>; and the duty is to make '
        'it good again» — </em><span dir="rtl" lang="ar">«فَالوَاجِبُ '
        'الاسْتِدْرَاك… حَتَّى يَجْبُرَ إِيمَانَهُ وَحَتَّى يَجْبُرَ '
        'نَقْصَ الوِلَايَةِ الَّذِي حَصَل»</span>.</p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>Read that against the clause it sits inside.</strong> '
      '<em>A man can spend his life policing the walāʾ he owes the '
      'disbelievers — which is none — and be, by this folio, in '
      '</em>نَقْصٌ فِي الوِلَايَة<em> every day, because he lies to his '
      'brother.</em> <strong>The sharḥ puts cheating a Muslim and betraying a '
      'Muslim inside the same chapter as the nullifier, as a defect in the '
      'very thing the nullifier is about.</strong>'))

BODY += B.prose(
    '<strong>And then the sentence that makes the nationalism passage cut '
    'both ways.</strong>')
BODY += B.sharh(
    p('«<strong>المُسْلِمُونَ شَيْءٌ وَاحِدٌ وَجَسَدٌ وَاحِدٌ أَيْنَمَا '
      'كَانُوا</strong>، لَا فَرْقَ بَيْنَ جَنُوبِيِّهِمْ '
      'وَشَمَالِيِّهِمْ وَشَرْقِيِّهِمْ وَغَرْبِيِّهِمْ أَيْنَمَا '
      'كَانُوا؛ <strong>الجِنْسِيَّاتُ هَذِهِ لَا قِيمَةَ لَهَا، '
      'الجِنْسِيَّةُ العَامَّةُ هِيَ الإِسْلَام</strong> تَعُمُّ '
      'الجَمِيعَ أَيْنَمَا كَانُوا» — and on '
      '﴿وَالمُؤْمِنُونَ وَالمُؤْمِنَاتُ بَعْضُهُمْ أَوْلِيَاءُ بَعْضٍ﴾: '
      '«<strong>هَذِهِ عَامَّةٌ فِي أَمْرِيكَا، فِي كُلِّ '
      'مَكَان</strong>، بَعْضُهُمْ أَوْلِيَاءُ بَعْض.»') +
    p('<em>The compiler flags the text here rather than smoothing it:</em> '
      'the word read as <span dir="rtl" lang="ar">«جَسَد»</span> is '
      '«<span dir="rtl" lang="ar">لَيْسَ بِوَاضِحٍ فِي الأَصْل، وَهَذَا '
      'الأَقْرَب</span>» — <em>not clear in the original, and this is the '
      'nearest reading. A note worth keeping, because it shows what the '
      'footnotes of this book are for.</em>'))
BODY += B.prose(
    '<strong>Set that beside the pan-nationalism he condemned a few folios '
    'back and the principle is one principle, not two.</strong> '
    '<em>There, Arabness was refused as a ground for </em>walāʾ<em> with '
    'disbelievers. Here, nationality is refused as a ground for '
    '</em>withholding walāʾ<em> from believers.</em> '
    '<strong>«الجِنْسِيَّاتُ هَذِهِ لَا قِيمَةَ لَهَا» cuts in whichever '
    'direction you were about to use it.</strong>')
BODY += B.hadith(
    'المُؤْمِنُ لِلْمُؤْمِنِ كَالْبِنْيَانِ يَشُدُّ بَعْضُهُ بَعْضًا',
    'The believer to the believer is like a building: one part of it braces '
    'the other.',
    'رَوَاهُ البُخَارِيُّ وَمُسْلِمٌ عَنْ أَبِي مُوسَى مَرْفُوعًا — '
    'as the sharḥ cites it; it names the two Shaykhayn and adds no grading of '
    'its own, so none is supplied here.')
BODY += B.sharh(
    p('<em>His gloss turns the image into a load-bearing one, and the '
      'sentence in the middle is the one to keep:</em> '
      '«البِنْيَانُ هَذَا فَوْقَ هَذَا، <strong>يُمْسِكُ بَعْضُهُ '
      'بَعْضًا</strong>؛ أَمْسَكَ أَسْفَلُهَا أَعْلَاهَا، '
      '<strong>وَإِنْ سَقَطَ أَسْفَلُهَا سَقَطَت</strong>؛ فَهَكَذَا '
      'المُؤْمِنُون، <strong>يَشُدُّ بَعْضُهُمْ أَزْرَ بَعْض</strong>، '
      'وَيُقَوِّي بَعْضُهُمْ بَعْضًا، <strong>وَهُمْ يَدٌ عَلَى مَنْ '
      'سِوَاهُم</strong>.»') +
    p('<em>And what the brotherhood is actually made of, in his own list:</em> '
      '«لِأَنَّ حَقِيقَتَهَا <strong>تَكَاتُفٌ وَتَعَاوُنٌ عَلَى البِرِّ '
      'وَالتَّقْوَى</strong>؛ حَقِيقَتُهَا إِصْلَاحُ الشَّأْنِ '
      'وَتَوْجِيهُ النَّاسِ إِلَى الخَيْرِ <strong>وَالأَخْذُ عَلَى يَدِ '
      'السَّفِيهِ وَرَدُّ الظَّالِمِ عَنْ ظُلْمِهِ</strong> وَالأَخْذُ '
      'بِيَدِ المَظْلُومِ وَالأَمْرُ بِالمَعْرُوفِ وَالنَّهْيُ عَنِ '
      'المُنْكَرِ وَإِفْشَاءُ أَمْرِ اللهِ فِي أَرْضِ اللهِ '
      'وَإِعْلَانُه.»') +
    p('<strong>Note what is inside his definition of brotherhood: restraining '
      'the fool, and turning the wrongdoer back from his wrong.</strong> '
      '<em>Brotherhood, on this folio, is not agreement. It includes being '
      'stopped by your brother.</em>'))
BODY += B.prose(
    '<strong>And the last application he draws from the one-body image is a '
    'hard one, and he states it as an absence of evidence.</strong>')
BODY += B.sharh(
    p('«<strong>لَمْ يَرِدْ فِي الكِتَابِ وَالسُّنَّةِ مَا يَدُلُّ عَلَى '
      'أَنَّ مَنْ وَقَعَ عَلَيْهِ العَدُوُّ يَكُونُ هُوَ المَسْؤُولَ '
      'عَنِ الجِهَادِ فَقَط</strong>؛ فَإِنَّ المُسْلِمِينَ شَيْءٌ '
      'وَاحِدٌ وَجَسَدٌ وَاحِد، يَجِبُ أَنْ يَتَعَاوَنُوا ضِدَّ '
      'أَعْدَائِهِمْ <strong>وَلَوْ تَبَاعَدَتِ الدِّيَار</strong>؛ '
      'فَلَيْسَ فِي الكِتَابِ وَالسُّنَّةِ مَا يَدُلُّ عَلَى أَنَّ مَنْ '
      'نَزَلَ بِهِمْ <strong>يُتْرَكُونَ وَعَدُوَّهُم</strong>؛ بَلْ فِي '
      'الكِتَابِ وَالسُّنَّةِ مَا يَدُلُّ عَلَى أَنَّهُمْ '
      '<strong>يُنْصَرُونَ وَيُعَانُون</strong>.»'))
BODY += B.ayah(
    'وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ وَلَا تَعَاوَنُوا عَلَى '
    'الْإِثْمِ وَالْعُدْوَانِ',
    'And cooperate in righteousness and piety, and do not cooperate in sin and '
    'aggression.',
    'سُورَةُ المَائِدَة · 5:2')
