# -*- coding: utf-8 -*-
"""Lesson 15, part E — the spy, and the case of Ḥāṭib ibn Abī Baltaʿah.

Printed folios 217-222, and the longest single topic in the eighth nullifier's
second half. It is also where the clause stops being abstract: a Companion did
the thing the nullifier names, and was neither killed nor declared a
disbeliever. The sharḥ therefore has to say WHY — and in saying why it names
the two مَوَانِع that the last section of this book is devoted to.

Two things on these folios must not be flattened:

  * **Ibn Bāz and al-Rājiḥī disagree, on the same page.** Al-Rājiḥī: the two
    preventers cannot combine for anyone after Ḥāṭib — «مَا يَجْتَمِعَان».
    Ibn Bāz: «الأَظْهَر» that a man with great prior service may be treated as
    Ḥāṭib was, and the walī al-amr may see it so. The compiler's own قلت sides
    with the second. The page keeps both, named.
  * **Ibn Bāz's two sittings pull in different directions.** In one he says a
    later man may be treated as Ḥāṭib was; in another, «فَغَيْرُ حَاطِبٍ لَا
    يُلْحَقُ بِهِ وَلَا يُسَاوِيه». The page says so, and gives the
    reconciliation the folios themselves support: الأَصْل is the killing, and
    the exception is not a plea anyone may enter for himself.

Rule 8: every report here carries a grading from a NAMED authority — Ibn Bāz
on «اعْمَلُوا مَا شِئْتُم» («الحَدِيثُ الصَّحِيح»), the compiler's «بِسَنَدٍ
صَحِيح» with Ibn Kathīr's «عَلَى شَرْطِ مُسْلِم», and «بِسَنَدٍ حَسَن» with
al-Ḥākim, al-Dhahabī's agreement, al-Ḍiyāʾ, and Ibn Kathīr's «إِسْنَادٌ
جَيِّد».
"""
from _nq_15_lib import B, p, ar, box, row, row3, thead3, table, qa

BODY = B.heading('الجَاسُوس', 'The Spy')
BODY += B.prose(
    '<strong>The clause now meets a fact that will not go away: a Companion '
    'who had fought at Badr wrote to Quraysh.</strong> <em>He was not killed, '
    'and he was not declared a disbeliever. Any account of this nullifier has '
    'to explain that, and the explanation is where the whole of Islamic '
    'takfīr-restraint comes from.</em>')
BODY += B.sharh(
    p('«<strong>الجَاسُوسُ شَرُّهُ عَظِيمٌ وَبَلَاؤُهُ عَظِيم</strong>؛ '
      'وَلِهَذَا يَسْتَحِقُّ [حَاطِبٌ] القَتْلَ <strong>لَوْلَا أَنَّهُ '
      'شَهِدَ بَدْرًا وَصَدَّقَهُ النَّبِيُّ ﷺ</strong>؛ صَارَ شُبْهَةً '
      'فِي كِتَابَتِهِ لَهُمْ أَنْ يَحْفَظُوا أَهْلَهُ وَمَالَه… '
      '<strong>أَمَّا مَنْ بَعْدَهُ فَمَا لَهُ إِلَّا الخِيَانَةُ لِلهِ '
      'وَرَسُولِهِ وَالمُؤْمِنِين</strong>.»'))
BODY += B.hadith(
    'إِنَّ اللهَ قَالَ لِأَهْلِ بَدْر: اعْمَلُوا مَا شِئْتُمْ فَقَدْ '
    'غَفَرْتُ لَكُم',
    'Allah has said to the people of Badr: do as you wish, for I have already '
    'forgiven you.',
    'الشَّيْخُ ابْنُ بَاز يُسَمِّيهِ «الحَدِيثَ الصَّحِيح» — he names it the '
    'ṣaḥīḥ ḥadīth himself in the course of the answer.')
BODY += B.sharh(
    qa('وَإِنْ تَابَ ذَلِكَ الجَاسُوس؟',
       '«<strong>هَذَا مَحَلُّ نَظَر</strong>؛ المَقْصُود: أَنَّهُ إِذَا '
       'ثَبَتَ أَنَّهُ جَاسُوسٌ يُقْتَل؛ أَمَّا مَسْأَلَةُ النَّظَرِ فِي '
       'تَوْبَتِهِ أَوْ عَدَمِ تَوْبَتِهِ <strong>فَشَيْءٌ '
       'آخَر</strong>.» <em>— the fourth time in this book he is handed a '
       'question and declines to rule on it.</em>') +
    qa('يُقْتَلُ حَدًّا أَوْ كُفْرًا؟',
       '«<strong>عَلَى حَسَبِ حَالِه</strong>: إِنْ كَانَ يَتَجَسَّسُ '
       'لِلْكُفَّارِ فَهُوَ يُقْتَلُ <strong>كَافِرًا</strong>؛ لِأَنَّهُ '
       'مِنْ أَنْصَارِهِم. وَإِنْ كَانَ <strong>لِلْبُغَاة</strong> '
       'فَيُقْتَلُ مِثْلَ قَتْلِ البُغَاة.»') +
    p('<strong>«عَلَى حَسَبِ حَالِه» is the same move this book has made in '
      'every hard clause</strong>, and it is worth naming as a pattern: '
      '<em>«فِيهِ التَّفْصِيل» on the magician; «الفَرْدُ وَالفَرْدَانِ '
      'فِسْق» on reviling the Companions; «عَلَى حَسَبِ التَّوْلِيَة» on '
      '5:51 in the first half of this nullifier; and now this.</em> '
      '<strong>The same act, two rulings, decided by a fact about the '
      'case.</strong>'))

# ----------------------------------------------------------- the two mawāniʿ
BODY += B.heading('المَانِعَان', 'The Two Preventers')
BODY += B.sharh(
    qa('قَوْلُ بَعْضِ أَهْلِ العِلْم: إِنَّ فِعْلَ حَاطِبٍ فِعْلُ كُفْر، '
       'لَكِنَّ حَاطِبًا مَنَعَهُ مِنَ الكُفْرِ أَنَّهُ مِنْ أَهْلِ '
       'بَدْر — هَلْ هُوَ وَجِيه؟',
       '«الظَّاهِر: <strong>الشُّبْهَةُ مَنَعَتْ مِنْ تَكْفِيرِهِ '
       'وَقَتْلِه</strong> — شُبْهَةُ كَوْنِهِ مِنْ أَهْلِ بَدْر، '
       '<strong>وَكَوْنِهِ تَأَوَّل</strong>؛ فَاجْتَمَعَ لَهُ '
       '<strong>التَّأْوِيلُ</strong> وَالحَدِيثُ الصَّحِيحُ (اعْمَلُوا '
       'مَا شِئْتُمْ فَقَدْ غَفَرْتُ لَكُم) <strong>فَصَارَ شُبْهَةً فِي '
       'قَتْلِهِ وَكُفْرِهِ جَمِيعًا</strong>. وَلَا شَكَّ أَنَّ '
       'التَّجَسُّسَ <strong>تَوَلٍّ لِلْمُشْرِكِين، رِدَّةٌ تُوجِبُ '
       'القَتْل</strong>.»') +
    p('<strong>Hold both halves of that answer at once, because a reader will '
      'want to drop one of them.</strong> <em>The act is named</em> '
      'تَوَلٍّ <em>and</em> رِدَّةٌ تُوجِبُ القَتْل<em>, without '
      'softening. And the man who did it was neither killed nor declared a '
      'disbeliever.</em> <strong>That is not an inconsistency; it is the '
      'distinction between the ruling on an act and the ruling on a '
      'man.</strong> <em>Which is precisely the subject of the section this '
      'book closes with —</em> مَوَانِعُ تَكْفِيرِ المُعَيَّن.'))
BODY += B.prose(
    '<strong>And a Muslim killed as a disbeliever is not buried as a '
    'Muslim.</strong> Asked whether such a spy is washed and prayed over, his '
    'answer is one word: «<span dir="rtl" lang="ar">نَعَم</span>» — <em>that '
    'is, he is not.</em> <em>The same consequence the seventh nullifier drew '
    'for the magician killed as a disbeliever rather than by a ḥadd.</em>')

# ------------------------------------------------- where the scholars differ
BODY += B.heading('مَوْضِعُ الخِلَاف', 'Where the Scholars on These Folios Differ')
BODY += B.prose(
    '<strong>Three contemporary scholars are quoted in the footnote, and they '
    'do not all say the same thing. The disagreement is about one question: '
    'can the two preventers ever combine again?</strong>')
BODY += B.sharh(table([
    thead3('who', 'on Ḥāṭib', 'on anyone after him'),
    row3('<strong>الشَّيْخُ عَبْدُ العَزِيزِ الرَّاجِحِي</strong>',
         '«فَالَّذِي فَعَلَهُ حَاطِبٌ رَضِيَ اللهُ عَنْهُ هَذَا مِنْ '
         'بَابِ <strong>التَّوَلِّي لِلْكُفَّار</strong>، وَتَوَلِّي '
         'الكُفَّارِ رِدَّة؛ وَالمَانِعُ مِنْ رِدَّةِ حَاطِبٍ وَقَتْلِهِ '
         '<strong>مَجْمُوعُ الأَمْرَيْن</strong>: الشُّبْهَةُ الَّتِي '
         'عَرَضَتْ لَه… وَكَوْنُهُ شَهِدَ بَدْرًا.»',
         '«<strong>فَهَلْ يُمْكِنُ أَنْ يَجْتَمِعَ الأَمْرَانِ فِيمَنْ '
         'بَعْدَه؟! مَا يَجْتَمِعَان</strong>؛ فَمَنْ تَجَسَّسَ عَلَى '
         'المُسْلِمِينَ يُقْتَل؛ لِأَنَّهُ لَا يَجْتَمِعُ فِيهِ '
         'الأَمْرَان.» <em>— the door is shut.</em>'),
    row3('<strong>الشَّيْخُ أَحْمَدُ بْنُ يَحْيَى النَّجْمِي</strong>',
         '«مُظَاهَرَةُ المُشْرِكِينَ وَالكُفَّارِ عَلَى المُسْلِمِينَ '
         '<strong>بِأَيِّ نَوْعٍ مِنْ أَنْوَاعِ المُظَاهَرَة</strong> — '
         'سَوَاءٌ كَانَ <strong>بِإِفْشَاءِ أَسْرَارِ '
         'المُسْلِمِين</strong> أَوْ بِإِعْطَائِهِمُ السِّلَاحَ أَوْ '
         'بِإِعَانَتِهِمْ فِي القِتَال — كُلُّ ذَلِكَ يُعَدُّ '
         'رِدَّة.»',
         '«فَإِذَا فَعَلَ ذَلِكَ مَنْ لَيْسَ لَهُ ظُرُوفٌ مِثْلُ '
         'ظُرُوفِ ذَلِكَ الرَّجُل… فَإِنَّهُ <strong>يُعْتَبَرُ فِي '
         'حَقِّهِ كُفْرًا</strong>.»'),
    row3('<strong>الشَّيْخُ صَالِحٌ الفَوْزَان</strong><br>'
         '<em>سِلْسِلَةُ شَرْحِ الرَّسَائِل</em>',
         '«فَعَلَ حَاطِبٌ مَا فَعَلَ <strong>لِأَنَّهُ تَأَوَّلَ '
         'لِنَفْسِهِ وَظَنَّ أَنَّ هَذَا مَا يَضُرُّ '
         'المُسْلِمِين</strong>؛ وَلِذَلِكَ الرَّسُولُ ﷺ <strong>لَمْ '
         'يُكَفِّرْه</strong>؛ لِأَنَّهُ حَصَلَ مِنْهُ خَطَأٌ عَنْ '
         'تَأْوِيلٍ وَلَهُ سَابِقَةٌ كَفَّرَتْ عَنْهُ مَا حَصَل.»',
         '<em>— he states the cause without closing the door either '
         'way.</em>'),
    row3('<strong>المُؤَلِّف</strong>, in his own «قُلْت»',
         '<em>— he accepts that the act is what the others say it is.</em>',
         '«<strong>لَوْ قُدِّرَ أَنَّ رَجُلًا فَعَلَ كَمَا فَعَلَ '
         'حَاطِبٌ وَظَنَّ أَنَّهُ لَا ضَرَرَ مِنْ فِعْلِهِ فَلَا رَيْبَ '
         'فِي عَدَمِ كُفْرِهِ فِيمَا بَيْنَهُ وَبَيْنَ الله</strong>، '
         'وَكَذَا إِذَا عَلِمْنَا مِنْهُ ذَلِك.» <em>— he does not shut '
         'the door al-Rājiḥī shut.</em>'),
]))
BODY += B.prose(
    '<strong>And Ibn Bāz himself, asked the question directly, gives the '
    'answer that sides against the closed door — and he gives it with the '
    'اَصْل still in place.</strong>')
BODY += B.sharh(
    qa('لَوْ تَجَسَّسَ غَيْرُ حَاطِبٍ مُتَأَوِّلًا؟',
       '«<strong>يَخْتَلِف</strong>؛ الأَظْهَرُ [أَنَّهُ] إِذَا كَانَ '
       'لَهُ مِنَ السَّوَابِقِ وَالأَعْمَالِ الصَّالِحَةِ الَّتِي '
       'تُبْعِدُهُ عَنْ ظَنِّ السُّوءِ وَعَنِ الرِّدَّةِ '
       '<strong>فَمَا فِيهِ مَانِعٌ أَنْ يُعَامَلَ مِثْلَ مَا عَامَلَ '
       'النَّبِيُّ ﷺ حَاطِبًا</strong>؛ <strong>لَكِنَّ الأَصْلَ أَنَّ '
       'الجَاسُوسَ يُقْتَل، هَذَا هُوَ الأَصْل</strong>… وَهَذِهِ '
       'الخَصْلَةُ قَدْ يُشَارِكُهُ فِيهَا مَنْ سَبَقَتْ لَهُ '
       'أَعْمَالٌ صَالِحَةٌ وَمَشَاهِدُ كَبِيرَةٌ وَأَعْمَالٌ '
       'جَلِيلَةٌ فِي نَصْرِ الإِسْلَامِ وَالمُسْلِمِين… ثُمَّ زَلَّ '
       'وَهَفَا هَفْوَةً تُوجِبُ لَه [القَتْل]، لَكِنَّ هَذِهِ '
       'المَشَاهِدَ وَهَذِهِ الأَعْمَالَ الصَّالِحَةَ '
       '<strong>قَدْ يَرَى فِيهَا وَلِيُّ الأَمْرِ أَنَّهَا تَشْفَعُ '
       'لَهُ فِي قَبُولِ عُذْرِهِ وَدَفْعِ هَذِهِ الزَّلَّة</strong>.»') +
    box('<p style="margin:0 0 .4rem;font-size:.8rem;letter-spacing:.06em;'
        'text-transform:uppercase;color:var(--ink-light)">and in another '
        'sitting he says this</p>'
        '<p style="margin:0;font-size:.94rem"><span dir="rtl" lang="ar">'
        '«فَالأَمْرُ عَظِيمٌ وَالخَطَرُ كَبِيرٌ فِي التَّجَسُّس؛ فَإِذَا '
        'انْدَفَعَ القَتْلُ فِي حَقِّ حَاطِبٍ <strong>فَغَيْرُ حَاطِبٍ '
        'لَا يُلْحَقُ بِهِ وَلَا يُسَاوِيه</strong>.»</span></p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>Those two answers are from two different sittings and they '
      'pull in different directions, and it would be dishonest to quote one '
      'and not the other.</strong> <em>What the folios themselves support is '
      'this:</em> <strong>الأَصْل is the killing</strong>, and the exception '
      'is <em>not a plea a man may enter for himself</em> — it is something '
      '«<span dir="rtl" lang="ar">قَدْ يَرَى فِيهَا وَلِيُّ '
      'الأَمْر</span>», which is to say it belongs to the one who carries the '
      'case, not to the one hoping to escape it. <em>Read that way, the '
      'second answer is a warning against the first being turned into a '
      'rule.</em>'))

# -------------------------------------------- that he was a mutaʾawwil
BODY += B.heading('أَنَّهُ كَانَ مُتَأَوِّلًا', 'That He Was Interpreting — and Who Said So')
BODY += B.prose(
    '<strong>The footnote then does something this book does when a point '
    'matters: it stops arguing and starts counting.</strong> <em>Fourteen '
    'imāms are named as having stated expressly that Ḥāṭib was a '
    '</em>مُتَأَوِّل<em>:</em> القَاضِي أَبُو يَعْلَى · ابْنُ الجَوْزِيّ · '
    'ابْنُ العَرَبِيّ · المُحِبُّ الطَّبَرِيّ · الزَّرْكَشِيّ · '
    'بَهَاءُ الدِّينِ بْنُ شَدَّاد · ابْنُ بَطَّال · ابْنُ الوَزِير · '
    'ابْنُ حَجَر · زَكَرِيَّا الأَنْصَارِيّ · السَّاعَاتِيّ · '
    'المُبَارَكْفُورِيّ · الكَانْدَهْلَوِيّ · ابْنُ عُثَيْمِين.')
BODY += B.prose(
    '<strong>And their evidence is not inference. It is what the man '
    'said.</strong>')
BODY += B.hadith(
    'يَا حَاطِبُ أَفَعَلْتَ؟ — قَال: أَمَا إِنِّي لَمْ أَفْعَلْهُ غِشًّا '
    'يَا رَسُولَ اللهِ وَلَا نِفَاقًا؛ قَدْ عَلِمْتُ أَنَّ اللهَ '
    'مُظْهِرٌ رَسُولَهُ وَمُتِمٌّ لَهُ أَمْرَهُ',
    '“Ḥāṭib — did you do it?” He said: I did not do it out of treachery, O '
    'Messenger of Allah, nor out of hypocrisy. I knew that Allah would make '
    'His Messenger prevail and would complete his affair for him.',
    'رَوَاهُ أَحْمَدُ فِي المُسْنَدِ وَابْنُ حِبَّانَ فِي صَحِيحِهِ عَنْ '
    'جَابِرٍ — «بِسَنَدٍ صَحِيح» عِنْدَ المُؤَلِّف، وَصَحَّحَهُ '
    'ابْنُ كَثِيرٍ فِي تَارِيخِهِ «عَلَى شَرْطِ مُسْلِم»')
BODY += B.hadith(
    'يَا حَاطِبُ مَا حَمَلَكَ عَلَى ذَلِك؟ — قَال: يَا رَسُولَ الله، '
    'أَمَا وَاللهِ إِنِّي لَنَاصِحٌ لِلهِ وَلِرَسُولِه؛ وَلَكِنْ كُنْتُ '
    'غَرِيبًا فِي أَهْلِ مَكَّة، وَكَانَ أَهْلِي بَيْنَ ظَهْرَانَيْهِم، '
    'وَخَشِيتُ عَلَيْهِم، فَكَتَبْتُ كِتَابًا لَا يَضُرُّ اللهَ '
    'وَرَسُولَه، وَعَسَى أَنْ يَكُونَ فِيهِ مَنْفَعَةٌ لِأَهْلِي',
    '“Ḥāṭib — what moved you to that?” He said: Messenger of Allah, by Allah '
    'I am sincere to Allah and to His Messenger; but I was a stranger among '
    'the people of Makkah, and my family were in their midst, and I feared for '
    'them. So I wrote a letter that would not harm Allah or His Messenger, and '
    'that might perhaps be of benefit to my family.',
    'رَوَاهُ الطَّحَاوِيُّ فِي المُشْكِلِ وَالحَاكِمُ — وَصَحَّحَهُ '
    'وَوَافَقَهُ الذَّهَبِيّ — وَالضِّيَاءُ فِي الأَحَادِيثِ '
    'المُخْتَارَةِ عَنِ ابْنِ عَبَّاس؛ «بِسَنَدٍ حَسَن» عِنْدَ '
    'المُؤَلِّف، وَقَالَ ابْنُ كَثِيرٍ فِي مُسْنَدِ الفَارُوق: '
    '«هَذَا إِسْنَادٌ جَيِّد»')
BODY += B.sharh(
    p('<em>And the compiler’s argument from the two reports is worth '
      'following, because it is an argument about what a man’s own words '
      'prove:</em> «<strong>وَهَذَا نَصٌّ صَرِيحٌ فِي '
      'تَأْوِيلِه</strong>؛ أَفَبَعْدَ هَذَا يُقَالُ إِنَّهُ تَعَمَّدَ '
      'مُظَاهَرَةَ الكُفَّارِ وَمُعَاوَنَتَهُمْ عَلَى الرَّسُولِ '
      'وَأَصْحَابِهِ لِأَجْلِ وَلَدِهِ وَمَالِه؟ '
      '<strong>فَهَذَا بَاطِلٌ مَرْدُودٌ بِنَصِّ الحَدِيثِ وَكَلَامِ '
      'أَهْلِ العِلْم</strong>؛ فَقَدْ نَفَى عَنْ نَفْسِهِ الغِشَّ '
      'وَأَثْبَتَ النُّصْحَ لِلهِ وَرَسُولِه، '
      '<strong>وَلَا يَقُولُ ذَلِكَ مَنْ يُظَاهِرُ الكُفَّارَ لِأَجْلِ '
      'الدُّنْيَا</strong>.»') +
    p('<em>And the sentence of his that al-Bukhārī preserves, which the '
      'compiler treats as the decisive one:</em> '
      '«<strong>وَاللهِ مَا كَفَرْتُ وَلَا ازْدَدْتُ لِلْإِسْلَامِ '
      'إِلَّا حُبًّا</strong>» — «فَهَلْ يَقُولُ هَذَا مَنْ آثَرَ '
      'حُبَّ مَالِهِ وَوَلَدِهِ عَلَى حُبِّ نَصْرَةِ الإِسْلَام؟»'))
BODY += B.prose(
    '<strong>Then an objection is raised against the whole line of argument, '
    'and the answer to it is the most precise thing on the folio.</strong> '
    '<em>If an excused interpreter does not sin, then Ḥāṭib had no need of a '
    'good deed to be pardoned — for pardon is only for a sin.</em>')
BODY += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><span dir="rtl" lang="ar">'
        '«هَذَا <strong>لَا يَمْنَعُ كَوْنَهُ تَأَوَّل</strong>؛ '
        'وَإِنَّمَا أَثِمَ وَاحْتَاجَ لِلْمَغْفِرَةِ '
        '<strong>لِعِلْمِهِ بِعِصْيَانِهِ أَمْرَ النَّبِيِّ ﷺ بِكَتْمِ '
        'الخَبَرِ عَنْ كُلِّ أَحَد</strong>، وَلِأَنَّهُ تَوَدَّدَ '
        'لِأُنَاسٍ مِنَ المُشْرِكِينَ لِمَصْلَحَةٍ رَجَاهَا مِنْهُم؛ '
        '<strong>وَإِنَّمَا التَّأْوِيلُ وَاقِعٌ فِي كَوْنِهِ '
        'اعْتَقَدَ أَنْ لَا ضَرَرَ عَلَى المُؤْمِنِينَ فِي '
        'إِخْبَارِهِ</strong>.»</span></p>') +
    p('<strong>So the taʾwīl is located to the inch.</strong> <em>It is not '
      'in the concealment — he knew he was disobeying a direct order, and '
      'that is the sin he needed pardon for. It is in his belief that the '
      'disclosure would do no harm.</em> <strong>A man can be sinning and '
      'interpreting at the same time, and the interpretation answers the '
      'takfīr while the sin still answers for itself.</strong>') +
    p('<em>And al-Qārī in</em> مِرْقَاةُ المَفَاتِيح <em>says the same from '
      'the other end:</em> «فَالصَّوَاب: <strong>أَنَّهُ لَمْ يَقْصِدْ '
      'أَذَى النَّبِيِّ ﷺ</strong>، بَلْ إِنَّمَا قَصَدَ دَفْعَ أَذَى '
      'الكُفَّارِ عَنْ قَرَابَتِه… وَقَدْ صَدَّقَهُ النَّبِيُّ ﷺ عَلَى '
      'ذَلِك. <strong>نَعَم، قَصَّرَ فِي اجْتِهَادِهِ حَيْثُ أَخْفَى '
      'أَمْرَهُ وَلَمْ يَسْتَأْذِنْ مِنْهُ ﷺ</strong>.»'))

# ------------------------------------------- Ṭaḥāwī on dhawū al-hayʾāt
BODY += B.heading('إِقَالَةُ ذَوِي الهَيْئَاتِ عَثَرَاتِهِم',
                  'Overlooking the Slips of People of Standing')
BODY += B.prose(
    '<strong>One question is still open: the taʾwīl explains why he was not '
    'declared a disbeliever — but why was he not even punished?</strong> '
    '<em>The compiler answers it from</em> al-Ṭaḥāwī <em>in</em> '
    'شَرْحُ مُشْكِلِ الآثَار<em>, and the principle he draws out is exact.</em>')
BODY += B.sharh(
    p('«أَنَّ مِنْ سُنَّةِ رَسُولِ اللهِ ﷺ <strong>أَمْرَهُ بِإِقَالَةِ '
      'ذَوِي الهَيْئَاتِ عَثَرَاتِهِم</strong> — <strong>إِلَّا فِي '
      'حَدٍّ مِنْ حُدُودِ اللهِ تَعَالَى</strong>؛ وَكَانَ حَاطِبٌ '
      'لِشُهُودِهِ بَدْرًا… <strong>مِنْ ذَوِي الهَيْئَة</strong>، '
      'وَلَمْ يَكُنِ الَّذِي أَتَى مِمَّا يُوجِبُ حَدًّا، '
      '<strong>وَإِنَّمَا يُوجِبُ عُقُوبَةً لَيْسَتْ بِحَدّ</strong>، '
      'فَرَفَعَهَا عَنْهُ رَسُولُ اللهِ ﷺ.»') +
    p('<em>And the control case, from the same passage:</em> '
      '«وَكَانَ الَّذِي كَانَ مِنْ <strong>قُدَامَة</strong> فِيهِ '
      'حَدٌّ لِلهِ <strong>فَلَمْ يَرْفَعْهُ عُمَرُ وَلَا عَلِيٌّ وَلَا '
      'مَنْ سِوَاهُمَا لِهَيْئَتِه</strong>؛ لِأَنَّ الهَيْئَةَ '
      'إِنَّمَا تَرْفَعُ العُقُوبَاتِ الَّتِي لَيْسَتْ حُدُودًا، '
      '<strong>وَلَا تَرْفَعُ العُقُوبَاتِ الَّتِي هِيَ حُدُود</strong>.»') +
    p('<strong>That is a principle with a fence built into it, and the fence '
      'is the half people forget.</strong> <em>Standing buys a man the '
      'overlooking of a slip. It does not buy him a ḥadd of Allah’s — '
      'and the proof is that it did not buy Qudāmah one, from ʿUmar, with '
      'ʿAlī present.</em>'))
BODY += B.ayah(
    'يَا أَيُّهَا الَّذِينَ آمَنُوا لَا تَتَّخِذُوا عَدُوِّي '
    'وَعَدُوَّكُمْ أَوْلِيَاءَ تُلْقُونَ إِلَيْهِم بِالْمَوَدَّةِ '
    'وَمَن يَفْعَلْهُ مِنكُمْ فَقَدْ ضَلَّ سَوَاءَ السَّبِيلِ',
    'O you who believe, do not take My enemies and your enemies as allies, '
    'extending to them affection… And whoever of you does it has strayed from '
    'the straight way.',
    'سُورَةُ المُمْتَحَنَة · 60:1')
BODY += B.sharh(
    p('<em>And the sharḥ ends the clause where the Qurʾān ended it — on the '
      'verse revealed about this very incident:</em> '
      '«وَلِهَذَا أَنْزَلَ اللهُ فِي ذَلِك ﴿لَا تَتَّخِذُوا عَدُوِّي '
      'وَعَدُوَّكُمْ أَوْلِيَاءَ﴾ حَتَّى قَالَ بَعْدَه '
      '﴿وَمَنْ يَفْعَلْهُ مِنْكُمْ فَقَدْ ضَلَّ سَوَاءَ '
      'السَّبِيلِ﴾.»') +
    p('<strong>Note what the verse does and does not say about him, because '
      'the sharḥ has been reading it carefully all along.</strong> '
      '<em>It says</em> ضَلَّ سَوَاءَ السَّبِيل<em> — he has strayed from '
      'the straight way.</em> <strong>It does not say he has left '
      'Islām.</strong> <em>And the man it was revealed about died a '
      'Muslim.</em>'))

# ------------------------------------------------------ forward to the mawāniʿ
BODY += B.heading('إِلَى أَيْنَ يَمْضِي الكِتَاب', 'Where the Book Goes Next')
BODY += B.prose(
    '<strong>The ninth and tenth nullifiers remain, and then this book closes '
    'with the section everything on this folio has been pointing at:</strong> '
    '<span dir="rtl" lang="ar">مَوَانِعُ تَكْفِيرِ '
    'المُعَيَّن</span> — <em>the barriers to declaring a particular '
    'person a disbeliever</em>, with <span dir="rtl" lang="ar">مَانِعُ '
    'الجَهْل</span> and <span dir="rtl" lang="ar">مَانِعُ '
    'التَّأْوِيل</span> each taken on its own. <em>It is not an appendix. It '
    'is the reason the ten clauses can be taught at all:</em> '
    '<strong>a man may hold a nullifier in his hands and still not be the one '
    'the ruling falls on — and Ḥāṭib ibn Abī Baltaʿah is the proof, with the '
    'Prophet ﷺ himself deciding the case.</strong>')
