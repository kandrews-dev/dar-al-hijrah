# -*- coding: utf-8 -*-
"""Lesson 15, part C — the tiers restated, the three categories of people,
the household, residence among the mushrikīn, and the state-level case.

Printed folios 204-212. This is the half of the clause that most readers need
and least expect: page after page of Ibn Bāz being asked whether some ordinary
act of civility is the nullifier, and answering that it is not. Then the
sentence that makes the whole clause teachable — the third category of people,
who are loved and disliked at once, by measure.
"""
from _nq_15_lib import B, p, ar, box, row, row3, thead3, table, qa

BODY = B.heading('المُجَامَلَاتُ لَيْسَتْ مِنَ المُوَالَاة',
                 'Ordinary Civility Is Not the Nullifier')
BODY += B.prose(
    '<strong>He is asked outright what the ruling on allying with the '
    'mushrikīn is, and his first word is the tier.</strong>')
BODY += B.sharh(
    qa('مَا حُكْمُ مُوَالَاةِ المُشْرِكِين؟',
       '«<strong>المُوَالَاةُ أَقْسَام</strong>: إِذَا تَوَلَّاهُمْ '
       'وَنَصَرَهُمْ عَلَى المُسْلِمِينَ صَارَ <strong>رِدَّة</strong>؛ '
       'أَمَّا مُوَالَاتُهُمْ بِمُجَرَّدِ الجُلُوسِ مَعَهُمْ لِلْأَكْلِ '
       'وَالشُّرْبِ وَالمُضَاحَكَةِ فَهَذِهِ <strong>مَعْصِيَةٌ '
       'بِخِلَافِ التَّوَلِّي</strong>.»') +
    qa('مَحَبَّتُهُمْ مَا تَكُونُ تَوَلِّيًا؟',
       '«<strong>المَحَبَّةُ الطَّبِيعِيَّةُ مِنَ المُوَالَاةِ مَا هِيَ '
       'مِنَ التَّوَلِّي</strong>؛ أَمَّا مَحَبَّةُ دِينِهِمْ '
       'فَكُفْر؛ لَكِنَّ المَحَبَّةَ الطَّبِيعِيَّةَ — لِأَنَّهُ أَبٌ أَوْ '
       'قَرِيبٌ أَوْ نَحْوُ ذَلِكَ — <strong>لَا تَجُوز</strong>؛ '
       'لِأَنَّهَا <strong>وَسِيلَةٌ إِلَى مَا هُوَ أَكْبَر</strong>.»') +
    p('<strong>Three tiers in one answer, and none of them collapsed into '
      'another.</strong> <em>Love of their religion: kufr. Natural love, '
      'because the man is your father: not tawallī — and still not '
      'permitted, because of where it leads. And sitting, eating, laughing: a '
      'sin, and expressly</em> <strong>«بِخِلَافِ التَّوَلِّي»</strong>.') +
    p('<em>And he gives the same structure from the other side:</em> '
      '«وَالمُوَالَاةُ لَهُمْ <strong>مُصَادَقَتُهُمْ وَمَحَبَّتُهُمْ '
      'وَالأُنْسُ بِهِم</strong> وَنَحْوُ ذَلِكَ فَهَذِهِ مُوَالَاتُهُم؛ '
      'فَإِذَا جُعِلُوا عَلَى المُسْلِمِينَ وَفَوْقَ المُسْلِمِينَ صَارَ '
      'هَذَا <strong>مِنْ أَشَدِّ المُوَالَاةِ وَمِنْ أَعْظَمِ '
      'الخَطَر</strong>؛ أَمَّا تَوَلِّيهِمْ فَهُوَ <strong>مُنَاصَرَتُهُمْ '
      'وَمُسَاعَدَتُهُمْ عَلَى المُسْلِمِين</strong> فَهَذَا يَكُونُ '
      'كُفْرًا وَرِدَّة.»'))
BODY += B.prose(
    '<strong>Now the particulars, and they are worth laying out as a list, '
    'because the list is what a reader of this clause actually comes looking '
    'for.</strong> <em>Every row below is him being asked about a specific '
    'act. Note how many are forbidden, how many are permitted — and how many '
    'are the nullifier.</em>')
BODY += B.sharh(table([
    thead3('the act', 'his answer', 'what it is'),
    row3('Calling a disbeliever or an open sinner <strong>«سَيِّد»</strong>',
         '«لَا يُقَالُ لِلْكَافِرِ: سَيِّد، وَلَا لِلْفَاسِقِ: سَيِّد… '
         'لِأَنَّ هَذَا <strong>وَصْفٌ عَظِيمٌ لَا يَلِيقُ</strong> '
         'بِالكَافِرِ وَالفَاسِق؛ بَلْ يُدْعَى بِاسْمِهِ المَعْرُوف: '
         'فُلَانٌ أَوْ أَبُو فُلَان» — <em>as the Prophet ﷺ said of '
         '</em>عَبْدِ اللهِ بْنِ أُبَيّ<em>: (مَا فَعَلَ أَبُو '
         'الحُبَاب؟). The sharḥ gives this phrase without naming a source '
         'for it or a grading, so none is supplied here.</em>',
         '<strong>Forbidden</strong>'),
    row3('Beginning the greeting of peace',
         '«لَا يُسَلَّمُ إِلَّا عَلَى المُسْلِمِين؛ وَأَمَّا الكَافِرُ '
         'فَلَا يُسَلَّمُ عَلَيْهِ لَا حَيًّا وَلَا مَيِّتًا، '
         '<strong>لَا يُبْدَأُ بِالسَّلَام</strong>.»',
         '<strong>Forbidden</strong>'),
    row3('<strong>Returning</strong> their greeting; asking after them and '
         'their children; answering their question',
         '«<strong>لَا يُسَمَّى مِثْلُ هَذَا</strong> الَّذِي يَقَعُ مِنْ '
         'بَعْضِ <strong>المُجَامَلَات</strong> فِي رَدِّ السَّلَامِ '
         'عَلَيْهِمْ إِذَا سَلَّمُوا أَوْ سُؤَالِهِمْ أَوْ إِجَابَتِهِمْ '
         'عَنْ سُؤَالِهِمْ… أَوْ كَيْفَ حَالُ أَوْلَادِكَ أَوْ كَيْفَ '
         'حَالُك — <strong>لَيْسَ هَذَا مِنَ المُوَالَاة</strong>.»',
         '<strong>Permitted</strong> — <em>and not even the lesser '
         'tier</em>'),
    row3('Eating with him; accepting his invitation',
         '«وَلَا مَانِعَ أَنْ يَسْأَلَهُ عَنْ أَوْلَادِهِ وَعَنْ '
         'حَالِه… <strong>وَلَا بَأْسَ أَنْ يَأْكُلَ مَعَهُ إِذَا دَعَتِ '
         'الحَاجَةُ</strong> إِلَى ذَلِك؛ وَلَا بَأْسَ أَنْ يُجِيبَ '
         'دَعْوَتَه، <strong>كَمَا أَجَابَ النَّبِيُّ ﷺ دَعْوَةَ '
         'اليَهُودِ وَأَكَلَ مِنْ طَعَامِهِم</strong> إِذَا رَأَى '
         'المَصْلَحَةَ الشَّرْعِيَّةَ فِي ذَلِك.»',
         '<strong>Permitted</strong> at need, with a lawful benefit in '
         'view'),
    row3('Reciting ruqyah over a disbeliever',
         '«الرُّقْيَةُ عَلَى الكَافِرِ إِذَا مَا كَانَ بَيْنَنَا '
         'وَبَيْنَهُمْ حَرْبٌ <strong>فَلَا بَأْس</strong>» — on '
         'al-Mumtaḥanah 60:8. <em>His fatwā within</em> فَتَاوَى '
         'اللَّجْنَةِ الدَّائِمَة<em>, with</em> الغُدَيَّان '
         '<em>and</em> الفَوْزَان <em>and</em> بَكْر أَبُو زَيْد '
         '<em>and</em> عَبْدُ العَزِيزِ آلُ الشَّيْخ <em>named with '
         'him.</em>',
         '<strong>Permitted</strong> — outside a state of war'),
    row3('Gladness at a calamity that befalls them',
         '«المُصِيبَةُ الَّتِي <strong>تَنْفَعُ المُسْلِمِين</strong> '
         'يُفْرَحُ بِهَا إِذَا كَانَ فِيهَا نَفْعٌ لِلْمُسْلِمِين» — '
         '<em>and asked about an earthquake in Japan:</em> '
         '«<strong>يُفْرَحُ بِه؛ لِأَنَّهُ قَدْ يَكُونُ مَوْعِظَةً '
         'لَهُم، قَدْ يَكُونُ فِيهِ هِدَايَة</strong>.»',
         'Permitted — <em>and look at the reason he gives</em>'),
]))
BODY += B.ayah(
    'لَّا يَنْهَاكُمُ اللَّهُ عَنِ الَّذِينَ لَمْ يُقَاتِلُوكُمْ فِي '
    'الدِّينِ وَلَمْ يُخْرِجُوكُم مِّن دِيَارِكُمْ أَن تَبَرُّوهُمْ '
    'وَتُقْسِطُوا إِلَيْهِمْ',
    'Allah does not forbid you from those who did not fight you over religion '
    'and did not drive you from your homes — that you should be kind to them '
    'and deal justly with them.',
    'سُورَةُ المُمْتَحَنَة · 60:8')
BODY += B.ayah(
    'قُلْ بِفَضْلِ اللَّهِ وَبِرَحْمَتِهِ فَبِذَٰلِكَ فَلْيَفْرَحُوا',
    'Say: in the bounty of Allah and in His mercy — in that let them rejoice.',
    'سُورَةُ يُونُس · 10:58')
BODY += B.prose(
    '<strong>Do not hurry past the reason attached to the earthquake, because '
    'it is the most revealing sentence on the folio.</strong> He is handed a '
    'natural disaster in a disbelieving country and asked whether a Muslim may '
    'be glad. He does not say <em>yes, they are enemies</em>. He says it may '
    'be an admonition for them — <strong>«قَدْ يَكُونُ فِيهِ '
    'هِدَايَة»</strong>. <em>The gladness he permits is aimed at their '
    'guidance.</em> The footnote’s own evidence runs the same way: the '
    'report of <strong>سَعْدُ بْنُ أَبِي وَقَّاص</strong> in '
    '<em>Muslim</em>, where the Prophet ﷺ laughed, and <strong>al-Nawawī</strong> '
    'glosses the laughter — «(فَضَحِكَ) أَيْ: <strong>فَرَحًا بِقَتْلِهِ '
    'عَدُوًّا</strong>، لَا لِانْكِشَافِه». <em>Muslim is named; the sharḥ '
    'adds no grading of its own, so none is supplied here.</em>')

# ------------------------------------------------- the three kinds of people
BODY += B.heading('النَّاسُ ثَلَاثَةُ أَقْسَام', 'Mankind in Three Categories')
BODY += B.prose(
    '<strong>And here the clause stops being a list of prohibitions and '
    'becomes a way of looking at every person you will ever meet.</strong> '
    '<em>He sets it out himself.</em>')
BODY += B.sharh(table([
    thead3('', 'who', 'what is owed'),
    row3('<strong>الأَوَّل</strong>',
         '«<strong>مُؤْمِنُونَ خُلَّصٌ مَعْرُوفُون</strong>»',
         '«فَحَقُّهُمُ <strong>المَحَبَّةُ وَالوِلَايَةُ وَالنَّصْرَةُ '
         'وَالتَّأْيِيدُ وَالتَّعَاوُنُ مَعَهُمْ فِي كُلِّ خَيْر</strong>؛ '
         'وَهَذَا هُوَ وَاجِبُ المُسْلِمِينَ مَعَ جَمِيعِ المُؤْمِنِينَ فِي '
         'عَهْدِهِ ﷺ وَبَعْدَ ذَلِك» — <em>and the footnote glosses «and '
         'after that»:</em> «أَيْ: فِي جَمِيعِ الأَزْمِنَة.»'),
    row3('<strong>الثَّانِي</strong>',
         '«<strong>الكَفَرَة</strong> مِنْ سَائِرِ الكُفَّارِ مِنَ '
         'اليَهُودِ وَالنَّصَارَى وَالمَجُوسِ وَالوَثَنِيِّينَ '
         'وَالشُّيُوعِيِّينَ وَالمَلَاحِدَةِ وَالإِبَاحِيِّينَ '
         'وَغَيْرِهِم»',
         '«يَجِبُ <strong>بُغْضُهُمْ فِي اللهِ وَمُعَادَاتُهُمْ فِي '
         'الله</strong> أَيْنَمَا كَانُوا فِي أَيِّ مَكَانٍ وَفِي أَيِّ '
         'زَمَان… وَمَنْ نَاصَرَهُمْ عَلَى المُسْلِمِينَ وَأَعَانَهُمْ '
         'عَلَى المُسْلِمِينَ ضِدَّ المُسْلِمِينَ <strong>فَهُوَ '
         'مِنْهُم</strong>.»'),
    row3('<strong>الثَّالِث</strong>',
         '«<strong>المُسْلِمُ الَّذِي عِنْدَهُ شَيْءٌ مِنَ المَعَاصِي '
         'وَالتَّقْصِير</strong>»',
         '«فَهَذَا <strong>لَهُ حَقُّ الوِلَايَةِ وَالمَحَبَّةِ مِنْ '
         'جَانِب</strong>؛ وَعَلَى المُؤْمِنِ حَقٌّ مِنْ جِهَتِهِ مِنْ '
         'جِهَةِ البَغْضَاءِ وَالتَّوْجِيهِ وَالإِرْشَادِ وَالأَمْرِ '
         'بِالمَعْرُوفِ وَالنَّهْيِ عَنِ المُنْكَرِ <strong>مِنْ جَانِبٍ '
         'آخَر</strong>؛ <strong>فَيُحَبُّ لِإِسْلَامِهِ وَإِيمَانِهِ '
         'الَّذِي مَعَه، وَيُبْغَضُ عَلَى قَدْرِ مَعَاصِيهِ الَّتِي '
         'مَعَهُ وَبِدْعَتِه</strong>؛ وَلَكِنْ يُؤْخَذُ عَلَى يَدَيْهِ '
         'وَيُعَلَّمُ وَيُوَجَّهُ وَيُؤْمَرُ بِالمَعْرُوفِ وَيُنْهَى '
         'عَنِ المُنْكَرِ وَتُقَامُ عَلَيْهِ الحُدُودُ وَيُدْعَى لَهُ '
         'بِالهِدَايَةِ وَالتَّوْفِيق — <strong>وَلَا '
         'يُهْمَل</strong>.»'),
]))
BODY += B.prose(
    '<strong>The third category is the one to learn by heart, and it is the '
    'answer to the way this clause is most often abused.</strong> A single '
    'man, loved and disliked <em>at the same time</em>, each <strong>by '
    'measure</strong> — «عَلَى قَدْرِ مَعَاصِيه» — and the measure of the '
    'love is his Islām and the measure of the dislike is his sins. '
    '<em>Walāʾ is therefore not a switch with two positions.</em> '
    '<strong>And the clause ends on a duty, not a verdict: وَلَا '
    'يُهْمَل — he is not to be abandoned.</strong> <em>A man who has learned '
    'only to classify people has not learned this page; the page ends by '
    'handing him a list of things to do for the man he has just '
    'classified.</em>')

# ------------------------------------------------------------- ahl al-bayt
BODY += B.heading('أَهْلُ البَيْت', 'The Household, by the Same Criterion')
BODY += B.sharh(
    p('«وَيُحِبُّ المُسْلِمُ أَهْلَ بَيْتِ رَسُولِ اللهِ '
      '<strong>المُؤْمِنِين</strong>؛ أَمَّا مَنْ كَانَ كَافِرًا مِنْهُمْ '
      'فَهُوَ يُبْغِضُهُ فِي الله؛ <strong>أَبُو لَهَبٍ</strong> مِنْ '
      'أَهْلِ البَيْتِ يَجِبُ إِبْغَاضُهُ فِي الله، '
      '<strong>وَأَبُو طَالِبٍ</strong> مِنْ أَهْلِ البَيْتِ يَجِبُ '
      'إِبْغَاضُهُ فِي الله.»') +
    p('«وَيُحِبُّ أَهْلَ البَيْتِ المُؤْمِنِين، كَعَلِيٍّ وَالحَسَنِ '
      'وَالحُسَيْنِ وَفَاطِمَةَ وَغَيْرِهِمْ… كُلُّ مَنْ كَانَ مِنْهُمْ '
      'مِنْ أَهْلِ الإِيمَانِ مِنْ بَنِي هَاشِمٍ <strong>يُحِبُّهُ فِي '
      'اللهِ كَمَا يُحِبُّ غَيْرَهُمْ مِنْ تَمِيمٍ وَقَحْطَان</strong>… '
      '<strong>حَتَّى العَبْدُ المَمْلُوكُ يُحَبُّ فِي اللهِ إِذَا كَانَ '
      'مُطِيعًا لِله</strong>؛ وَمَنْ كَانَ كَافِرًا بِاللهِ يُبْغَضُ فِي '
      'اللهِ <strong>وَلَوْ كَانَ مِنْ أَوْلَادِ الأَنْبِيَاء</strong>.»') +
    p('<strong>From the Prophet’s own uncle to an owned slave in one '
      'passage, and the criterion never moves once.</strong> <em>This is the '
      'nationalism passage again in a different key: lineage is not a '
      'religion either, and the highest lineage there has ever been is the '
      'one he uses to prove it.</em>'))
BODY += B.prose(
    '<strong>And then a question arrives that puts this page against the '
    'last one, and the sharḥ does not flinch.</strong> A man watched a serial '
    'drama about the Prophet’s ﷺ grandfather, and came away loving '
    '<strong>عَبْدَ المُطَّلِبِ</strong> and <strong>أَبَا طَالِب</strong> '
    'for what they did for him — is there sin on him for that?')
BODY += B.sharh(
    qa('فَأَحْبَبْتُ عَبْدَ المُطَّلِبِ وَأَبَا طَالِبٍ لِذَلِك… فَهَلْ '
       'عَلَيَّ إِثْمٌ فِي هَذَا؟',
       '«<strong>رِعَايَةُ عَبْدِ المُطَّلِبِ وَحِمَايَةُ أَبِي طَالِبٍ '
       'لِلنَّبِيِّ ﷺ لَا تُوجِبُ مَحَبَّةً لَهُمَا</strong>؛ لِأَنَّ '
       'عَبْدَ المُطَّلِبِ مَاتَ عَلَى دِينِ الجَاهِلِيَّةِ وَهُوَ '
       'الشِّرْكُ بِالله؛ وَأَبَا طَالِبٍ <strong>عَلِمَ الحَقَّ وَلَمْ '
       'يَعْمَلْ بِه</strong>، وَقَدِ امْتَنَعَ عَنِ النُّطْقِ '
       'بِالشَّهَادَةِ عِنْدَ احْتِضَارِهِ لَمَّا طَلَبَ مِنْهُ '
       'النَّبِيُّ ﷺ قَوْلَهَا، وَقَال: (هُوَ عَلَى مِلَّةِ عَبْدِ '
       'المُطَّلِب).»') +
    p('<strong>Put this beside part one and the pair of them teach something '
      'neither says alone.</strong> <em>In the first half of this nullifier, '
      'Abū Ṭālib’s protection of the Prophet ﷺ was cited as '
      '<strong>proof</strong> that the third division — accepting a '
      'disbeliever’s help — is permitted. Here, the same protection is '
      'said <strong>not to oblige love of him</strong>.</em> '
      '<strong>So a Muslim may lawfully accept a disbeliever’s shelter '
      'and still owe him barāʾah.</strong> <em>The two are not in tension, '
      'and the fact that they are not is the whole architecture of this '
      'clause: what you may </em>do<em> with a man and what you may '
      '</em>give him in your heart<em> are two different questions.</em>'))

# -------------------------------------------------- residence among them
BODY += B.heading('الإِقَامَةُ بَيْنَ المُشْرِكِين',
                  'Residence Among Them, and Why It Is in This Clause')
BODY += B.prose(
    '<strong>The sharḥ now turns to something that is not, in itself, the '
    'nullifier at all — and spends two folios on it because of what it leads '
    'to.</strong>')
BODY += B.ayah(
    'إِنَّ الَّذِينَ تَوَفَّاهُمُ الْمَلَائِكَةُ ظَالِمِي أَنفُسِهِمْ '
    'قَالُوا فِيمَ كُنتُمْ قَالُوا كُنَّا مُسْتَضْعَفِينَ فِي الْأَرْضِ '
    'قَالُوا أَلَمْ تَكُنْ أَرْضُ اللَّهِ وَاسِعَةً فَتُهَاجِرُوا فِيهَا '
    'فَأُولَٰئِكَ مَأْوَاهُمْ جَهَنَّمُ وَسَاءَتْ مَصِيرًا',
    'Indeed, those whom the angels take in death while they are wronging '
    'themselves — they will say, “In what condition were you?” They will say, '
    '“We were oppressed in the land.” They will say, “Was not the earth of '
    'Allah spacious, that you might emigrate in it?” Those — their refuge is '
    'Hell, and an evil destination it is.',
    'سُورَةُ النِّسَاء · 4:97')
BODY += B.sharh(
    p('<em>His gloss on the three words the verse hangs on:</em> '
      '«<strong>ظَالِمِي أَنْفُسِهِم</strong> يَعْنِي: '
      '<strong>بِالإِقَامَةِ بَيْنَ المُشْرِكِين</strong>.»') +
    p('«وَهَذِهِ نَزَلَتْ فِي قَوْمٍ مِنَ المُسْلِمِينَ كَانُوا بِمَكَّةَ '
      'فَخَرَجُوا مَعَ أَعْدَاءِ اللهِ فِي <strong>بَدْر</strong> '
      'وَقُتِلَ مِنْهُمْ مَنْ قُتِلَ مَعَ المُشْرِكِين؛ '
      '<strong>وَالمَشْهُورُ أَنَّهُمْ كَانُوا مُكْرَهِين</strong>، '
      'وَلَوْ خَرَجُوا مُقَاتِلِينَ طَائِعِينَ كَانُوا '
      '<strong>مُرْتَدِّين</strong>؛ وَلَكِنْ بِسَبَبِ إِقَامَتِهِمْ '
      'بَيْنَ المُشْرِكِينَ <strong>اجْتَرَؤُوا عَلَيْهِم</strong> '
      'وَسَاقُوهُمْ إِلَى مَا سَاقُوهُمْ إِلَيْهِ مِنَ المُشَارَكَةِ فِي '
      'قِتَالِ المُسْلِمِين.»') +
    p('<em>And he reports the harder view without adopting it:</em> '
      '«<strong>وَقَالَ بَعْضُ السَّلَف: إِنَّهُمْ كَفَرُوا '
      'بِذَلِك</strong>؛ لِأَنَّهُمْ ظَاهَرُوا المُشْرِكِينَ '
      'وَسَاعَدُوهُمْ فَصَارُوا بِذَلِكَ مِثْلَهُم.»') +
    box('<p style="margin:0 0 .45rem;font-size:.8rem;letter-spacing:.06em;'
        'text-transform:uppercase;color:var(--ink-light)">'
        '<span dir="rtl" lang="ar">فَهُمْ بَيْنَ أَمْرَيْن</span> · the two '
        'cases he divides them into</p>'
        '<p style="margin:0 0 .4rem;font-size:.93rem"><strong>١ —</strong> '
        '<span dir="rtl" lang="ar">«مَنْ كَانَ مُوَالِيًا لَهُمْ '
        'مُسَاعِدًا لَهُمْ مُوَافِقًا لَهُمْ عَلَى قِتَالِ أَوْلِيَاءِ '
        'اللهِ <strong>كَفَر</strong>.»</span></p>'
        '<p style="margin:0;font-size:.93rem"><strong>٢ —</strong> '
        '<span dir="rtl" lang="ar">«وَمَنْ كَانَ <strong>مُكْرَهًا</strong> '
        'لَمْ يَرْضَ بِذَلِكَ وَإِنَّمَا أُكْرِهَ عَلَيْهِ '
        '<strong>فَقَدْ أَسَاءَ بِإِقَامَتِهِ بَيْنَهُمْ وَعَدَمِ '
        'بِدَارِهِ بِالهِجْرَة</strong>؛ فَكَانَتْ إِقَامَتُهُ '
        '<strong>وَسِيلَةً وَذَرِيعَة</strong> إِلَى أَنْ خَرَجَ '
        'مُقَاتِلًا وَمُسَاعِدًا لِأَعْدَاءِ الله.»</span></p>') +
    p('<em>And the general lesson he draws from the pair:</em> '
      '«وَإِنْ سَلِمَ مِنْ ذَلِكَ صَارَتْ إِقَامَتُهُ وَسِيلَةً إِلَى أَنْ '
      'يُوَافِقَهُمْ فِي بَعْضِ البَاطِلِ أَوْ عَلَى تَرْكِ بَعْضِ '
      'الحَقّ؛ وَرُبَّمَا خَرَجَ عَنْ دِينِهِ <strong>بِتَشْكِيكِهِمْ '
      'لَه</strong> وَدَعْوَتِهِمْ لَهُ إِلَى البَاطِلِ وَأَنْوَاعِ '
      'الكُفْر.»'))
BODY += B.ayah(
    'إِلَّا الْمُسْتَضْعَفِينَ مِنَ الرِّجَالِ وَالنِّسَاءِ وَالْوِلْدَانِ '
    'لَا يَسْتَطِيعُونَ حِيلَةً وَلَا يَهْتَدُونَ سَبِيلًا '
    'فَأُولَٰئِكَ عَسَى اللَّهُ أَن يَعْفُوَ عَنْهُمْ وَكَانَ اللَّهُ '
    'عَفُوًّا غَفُورًا',
    'Except for the oppressed among men, women and children who cannot devise '
    'a plan nor are they able to find a way — for those, Allah may well pardon '
    'them, and Allah is ever Pardoning and Forgiving.',
    'سُورَةُ النِّسَاء · 4:98–99')
BODY += B.prose(
    '<strong>Notice that the verse itself is the second case, and the sharḥ '
    'reads the passage as a whole.</strong> The one who truly '
    '<em>cannot</em> — no plan, no way — is not the one being addressed; '
    'Allah holds out pardon to him by name. <em>And this is the reason the '
    'remedy the sharḥ names is a remedy and not a punishment:</em> '
    '«<span dir="rtl" lang="ar">وَعَدَمِ بِدَارِهِ '
    '<strong>بِالهِجْرَة</strong></span>». <strong>The nullifier’s '
    'preventative, on this folio, is hijrah</strong> — <em>moving, before the '
    'situation does the choosing for you.</em>')

# --------------------------------------------------- the state-level case
BODY += B.heading('إِعَانَةُ دَوْلَةٍ كَافِرَة', 'When a Muslim State Aids a Disbelieving One')
BODY += B.sharh(
    p('«الحُكُومَةُ المُسْلِمَةُ عَلَيْهَا أَنْ تَنْظُرَ فِي المَصَالِحِ '
      'لِلْمُسْلِمِين، <strong>وَتُعِينَ بَعْضَ الدُّوَلِ الكَافِرَةِ '
      'إِذَا كَانَ فِيهِ مَصْلَحَةٌ لِلْمُسْلِمِينَ وَدَفْعٌ لِعَدُوٍّ '
      'أَكْثَرَ وَشَرٍّ أَكْثَر</strong>؛ فَعَلَى وَلِيِّ الأَمْرِ أَنْ '
      'يَتَّقِيَ اللهَ وَأَنْ يَجْتَهِدَ فِي صَرْفِ المَالِ فِي '
      'وَجْهِه… وَلَا مَانِعَ مِنْ أَنْ يَدْفَعَ الضَّرَرَ الأَكْبَرَ '
      'وَالشَّرَّ الَّذِي يُخْشَى مِنْهُ بِمَالٍ يَدْفَعُهُ لِأَعْدَاءِ '
      'اللهِ يَتَّقِي بِهِ شَرَّهُم… <strong>إِذَا كَانَ صَادِرًا عَنْ '
      'نِيَّةٍ صَالِحَةٍ وَعَنْ قَصْدٍ صَالِحٍ وَعَنْ نَظَرٍ فِي '
      'المَصَالِح</strong>.»') +
    box('<p style="margin:0 0 .35rem;font-size:.8rem;letter-spacing:.06em;'
        'text-transform:uppercase;color:var(--ink-light)">the footnote fences '
        'it, in one sentence</p>'
        '<p style="margin:0;font-size:.94rem"><span dir="rtl" lang="ar">'
        '«أَيْ: <strong>فِي غَيْرِ حَرْبٍ وَلَا مُظَاهَرَةٍ لَهُمْ عَلَى '
        'المُسْلِمِين</strong>، بَلِ الإِعَانَةُ لِمَصْلَحَةِ '
        'المُسْلِمِينَ عَامَّةً <strong>كَفَكِّ الأَسْرَى</strong> أَوْ '
        'دَفْعِ شَرِّ عَدُوٍّ أَكْبَرَ مِنْ دُوَلٍ كَافِرَةٍ '
        'أُخْرَى.»</span></p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<em>This is the same discipline the first half of the nullifier used on '
      'Khaybar, and it is worth naming as a habit:</em> '
      '<strong>a permission is given, and then immediately bounded in '
      'writing.</strong> <em>No war; no backing them against Muslims; a '
      'general Muslim benefit, with ransoming captives given as the example; '
      'and the whole of it resting on</em> نَظَرٍ فِي المَصَالِح <em>by the '
      'one who actually carries the responsibility.</em>'))
