# -*- coding: utf-8 -*-
"""Lesson 15, part B — the second and third excuses: fear, and nationality.

Printed folios 206-208 and 211-212. The sharḥ sets al-Māʾidah 5:51-52 against
the pan-Arab nationalism of his own day, and the footnote behind it — Ibn
Taymiyyah on the cause of revelation — isolates the MOTIVE of tawallī and
shows it is not love of their religion. Which is the point: the motive was
fear, and the verse came down anyway. Then the qāʿidah on istiḥlāl, with the
condition built into it, and the two verses that close the matter.
"""
from _nq_15_lib import B, p, ar, box, row, row3, thead3, table, qa

BODY = B.prose(
    '<strong>The second excuse is fear</strong> — and the sharḥ does not have '
    'to argue that it is no excuse, because the Qurʾān answers it in the verse '
    'immediately after the one the matn quotes. <em>Read the two together, in '
    'order, as the sharḥ reads them.</em>')
BODY += B.ayah(
    'يَا أَيُّهَا الَّذِينَ آمَنُوا لَا تَتَّخِذُوا الْيَهُودَ '
    'وَالنَّصَارَىٰ أَوْلِيَاءَ بَعْضُهُمْ أَوْلِيَاءُ بَعْضٍ وَمَن '
    'يَتَوَلَّهُم مِّنكُمْ فَإِنَّهُ مِنْهُمْ إِنَّ اللَّهَ لَا يَهْدِي '
    'الْقَوْمَ الظَّالِمِينَ',
    'O you who believe, do not take the Jews and the Christians as allies. '
    'They are allies of one another. And whoever among you allies with them — '
    'then he is one of them. Indeed, Allah does not guide the wrongdoing '
    'people.',
    'سُورَةُ المَائِدَة · 5:51')
BODY += B.ayah(
    'فَتَرَى الَّذِينَ فِي قُلُوبِهِم مَّرَضٌ يُسَارِعُونَ فِيهِمْ '
    'يَقُولُونَ نَخْشَىٰ أَن تُصِيبَنَا دَائِرَةٌ',
    'So you see those in whose hearts is disease hastening toward them, '
    'saying, “We fear that a turn of fortune may strike us.”',
    'سُورَةُ المَائِدَة · 5:52')
BODY += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><em>«<strong>سُبْحَانَ اللهِ! '
        'مَا أَصْدَقَ قَوْلَهُ وَأَوْضَحَ بَيَانَه.</strong> These '
        'nationalists call to a bloc around <strong>Arab '
        'nationalism</strong>, its Muslim and its disbeliever alike. They '
        'say: we fear a turn of fortune may strike us; we fear colonialism '
        'will return to our lands; we fear our wealth will be seized by the '
        'hands of our enemies — <strong>فَيُوَالُونَ لِأَجْلِ ذَلِك</strong> '
        'every Arab, of Jews and Christians and Magians and idolaters and '
        'atheists and others, under the banner of Arab nationalism. And they '
        'say: its system does not distinguish between one Arab and another, '
        'even if their religions differ.</em></p>'
        '<p style="margin:.5rem 0 0;font-size:.95rem"><em>«<strong>فَهَلْ '
        'هَذَا إِلَّا مُصَادَمَةٌ لِكِتَابِ اللهِ وَمُخَالَفَةٌ لِشَرْعِ '
        'اللهِ وَتَعَدٍّ لِحُدُودِ اللهِ وَمُوَالَاةٌ وَمُعَادَاةٌ وَحُبٌّ '
        'وَبُغْضٌ عَلَى غَيْرِ دِينِ الله؟ فَمَا أَعْظَمَ ذَلِكَ مِنْ '
        'بَاطِل!</strong>»</em></p>') +
    p('<strong>And now the footnote, which is the part to keep.</strong> '
      '<em>Ibn Taymiyyah, in</em> مَجْمُوعُ الفَتَاوَى <em>and</em> '
      'الإِيمَان: «وَالمُفَسِّرُونَ <strong>مُتَّفِقُونَ</strong> عَلَى '
      'أَنَّهَا نَزَلَتْ بِسَبَبِ قَوْمٍ مِمَّنْ كَانَ يُظْهِرُ الإِسْلَامَ '
      'وَفِي قَلْبِهِ مَرَضٌ خَافَ أَنْ يُغْلَبَ أَهْلُ الإِسْلَامِ '
      'فَيُوَالِي الكُفَّارَ مِنَ اليَهُودِ وَالنَّصَارَى وَغَيْرِهِمْ '
      '<strong>لِلْخَوْفِ الَّذِي فِي قُلُوبِهِم</strong>، <strong>لَا '
      'لِاعْتِقَادِهِمْ أَنَّ مُحَمَّدًا كَاذِبٌ وَاليَهُودَ وَالنَّصَارَى '
      'صَادِقُون</strong>.»') +
    p('<em>And the compiler draws out exactly what that is worth:</em> '
      '«فَقَوْلُه: <strong>لِلْخَوْفِ الَّذِي فِي قُلُوبِهِم</strong> — '
      'فِيهِ بَيَانٌ <strong>لِبَاعِثِ التَّوَلِّي</strong> وَأَنَّهُ '
      'لَيْسَ حُبًّا فِي دِينِ اليَهُودِ وَالنَّصَارَى.»'))
BODY += B.prose(
    '<strong>Sit with what that footnote has just conceded, because it is '
    'conceding the whole of the sympathetic case and then saying the verse '
    'came down anyway.</strong> The men it was revealed about '
    '<em>did not believe the Jews and the Christians were right</em>. They did '
    'not think Muḥammad ﷺ was a liar. <em>They were frightened, and they were '
    'frightened of something that could really have happened to them.</em> '
    'And the verse named them as having a disease in the heart. '
    '<strong>So the motive is not the measure.</strong> <em>Which is the same '
    'answer kinship got on the folio before: the clause asks what you '
    '<strong>did</strong>, and against whom.</em>')
BODY += B.prose(
    '<strong>And the third excuse is the one this passage is actually '
    'about — nationality as a basis for walāʾ.</strong> <em>Keep it in mind; '
    'the sharḥ will turn it over in a few folios and condemn the nationalism '
    'of the other direction in the same words.</em> '
    '<strong>«الجِنْسِيَّاتُ هَذِهِ لَا قِيمَةَ لَهَا»</strong> — and when he '
    'says it there, he is not defending Arabs against others. He is saying '
    '<em>a passport is not a religion, in either direction.</em>')

# ------------------------------------------------------------- the muḥkam
BODY += B.heading('آيَةٌ مُحْكَمَة', 'A Verse Not Open to Being Softened')
BODY += B.sharh(
    p('Ibn Taymiyyah again: <em>«وَقَدْ حَرَّمَ اللهُ مُوَالَاتَهُم، '
      'وَنَهَى عَنِ اتِّخَاذِهِمْ <strong>بِطَانَة</strong>، وَحَكَمَ عَلَى '
      'مَنْ تَوَلَّاهُمْ بِأَنَّهُ مِنْهُم، وَأَخْبَرَ أَنَّ الجَمِيعَ مِنَ '
      'الظَّالِمِين، كَمَا سَبَقَ ذَلِكَ فِي <strong>الآيَاتِ '
      'المُحْكَمَات</strong>.»</em> <em>The footnote notes that he states here, '
      'expressly, that</em> ﴿وَمَنْ يَتَوَلَّهُمْ مِنْكُمْ فَإِنَّهُ '
      'مِنْهُمْ﴾ <em>is</em> آيَةٌ مُحْكَمَة.') +
    p('<em>And then three sentences that between them close every remaining '
      'door:</em>') +
    table([
        row('<span dir="rtl" lang="ar">لَوْ أَحَبُّونَا</span>',
            '«وَلَوْ فُرِضَ أَنَّ النَّصَارَى أَحَبُّوا المُؤْمِنِينَ '
            'وَأَظْهَرُوا مَوَدَّتَهُمْ لَهُمْ <strong>لَمْ يَجُزْ</strong> '
            'لِأَهْلِ الإِيمَانِ أَنْ يُوَادُّوهُمْ وَيُوَالُوهُم.» '
            '<em>— reciprocity is not a ground.</em>'),
        row('<span dir="rtl" lang="ar">مَتَى يَزُولُ الحِقْد</span>',
            '«وَلَنْ يَزُولَ حِقْدُ الكُفَّارِ عَلَى المُسْلِمِينَ إِلَّا '
            'إِذَا تَرَكُوا دِينَهُمْ وَاتَّبَعُوا مِلَّةَ أَعْدَائِهِمْ '
            'وَصَارُوا فِي حِزْبِهِم؛ وَذَلِكَ هُوَ الضَّلَالُ البَعِيدُ '
            'وَالكُفْرُ الصَّرِيح.» <em>— so the price of the goodwill is the '
            'religion, which is why it is not a bargain.</em>'),
        row('<span dir="rtl" lang="ar">الدِّينُ وَاحِد؟</span>',
            '«أَمَّا إِذَا قَال: لَيْسَ بَيْنَنَا وَبَيْنَ اليَهُودِ '
            'شَيْء، بَلْ جَاءَ القُرْآنُ الكَرِيمُ بِدَعْوَى مَحَبَّتِهِمْ '
            '— فَهَذَا كُفْرٌ وَرِدَّة... <strong>وَمَنْ يَقُول: إِنَّ '
            'الدِّينَ وَاحِدٌ فَهَذَا ضَالٌّ مُضِلٌّ كَافِر</strong>.» '
            '<em>— and note what is being ruled on: not an alliance, but a '
            'claim about the Qurʾān.</em>'),
    ]))
BODY += B.ayah(
    'لَتَجِدَنَّ أَشَدَّ النَّاسِ عَدَاوَةً لِّلَّذِينَ آمَنُوا الْيَهُودَ '
    'وَالَّذِينَ أَشْرَكُوا',
    'You will surely find the most intense of people in animosity toward the '
    'believers to be the Jews and those who associate others with Allah.',
    'سُورَةُ المَائِدَة · 5:82')

# --------------------------------------------------------- qāʿidat al-istiḥlāl
BODY += B.heading('قَاعِدَةُ الاسْتِحْلَال', 'The Rule on Declaring It Lawful')
BODY += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><em>«Whoever declares '
        'lawful the affection… and states that it is legislated or permitted — '
        '<strong>this speech of his is apostasy</strong>.»</em></p>'
        '<p style="margin:0;font-size:.95rem"><span dir="rtl" lang="ar">'
        '«هَذِهِ قَاعِدَة: كُلُّ مَنِ اسْتَحَلَّ مَا حَرَّمَ اللهُ '
        '<strong>مِمَّا هُوَ مُجْمَعٌ عَلَيْه</strong>، أَوْ أَسْقَطَ مَا '
        'أَوْجَبَ اللهُ <strong>مِمَّا هُوَ مُجْمَعٌ عَلَيْه</strong> — '
        '<strong>مَا فِيهِ خِلَافٌ وَلَا شُبْهَة</strong> — يَكُونُ '
        'رِدَّة.»</span></p>') +
    p('<strong>The rule carries its own restraint, and the restraint is said '
      'twice and then said a third way.</strong> <em>Not whatever Allah '
      'forbade — what is</em> <strong>agreed upon</strong><em>. Not whatever a '
      'man denies — what has</em> <strong>no disagreement in it and no doubt '
      'in it</strong><em>.</em> Which means this qāʿidah, as the sharḥ states '
      'it, <strong>cannot be reached through a contested question</strong>, '
      'and a man who thinks he has reached it through one has not used the '
      'rule; he has dropped half of it.'))
BODY += B.ayah(
    'لَّا تَجِدُ قَوْمًا يُؤْمِنُونَ بِاللَّهِ وَالْيَوْمِ الْآخِرِ '
    'يُوَادُّونَ مَنْ حَادَّ اللَّهَ وَرَسُولَهُ وَلَوْ كَانُوا آبَاءَهُمْ '
    'أَوْ أَبْنَاءَهُمْ أَوْ إِخْوَانَهُمْ أَوْ عَشِيرَتَهُمْ',
    'You will not find a people who believe in Allah and the Last Day having '
    'affection for those who oppose Allah and His Messenger, even if they were '
    'their fathers, or their sons, or their brothers, or their kindred.',
    'سُورَةُ المُجَادَلَة · 58:22')
BODY += B.sharh(
    p('<em>And with that verse he gives the tier again, in the same breath, '
      'because he will not let the two merge:</em> '
      '«وَمَحَبَّةُ الكُفَّارِ وَإِعَانَتُهُمْ عَلَى بَاطِلِهِمْ '
      'وَاتِّخَاذُهُمْ أَصْحَابًا وَأَخْدَانًا وَنَحْوُ ذَلِكَ '
      '<strong>مِنْ كَبَائِرِ الذُّنُوبِ وَمِنْ وَسَائِلِ الكُفْرِ '
      'بِالله</strong>؛ فَإِنْ نَصَرَهُمْ عَلَى المُسْلِمِينَ وَسَاعَدَهُمْ '
      'ضِدَّ المُسْلِمِينَ <strong>فَهَذَا هُوَ التَّوَلِّي وَهُوَ مِنْ '
      'أَنْوَاعِ الرِّدَّةِ عَنِ الإِسْلَام</strong>.»') +
    p('<strong>Taking a disbeliever as an intimate friend: a major sin, and a '
      'means to disbelief. Aiding him against the Muslims: apostasy.</strong> '
      '<em>Two sentences, one breath, and the whole clause’s discipline is '
      'in the gap between them.</em>'))
