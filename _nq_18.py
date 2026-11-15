# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 18 — مَوَانِعُ تَكْفِيرِ المُعَيَّن: the capstone opens.

The ten nullifiers are done. The book does not end on the tenth; it ends on
the question every reader of a book of takfīr must be made to face before he
closes it: granting that an ACT is a nullifier, when may you rule that THIS
MAN has left Islām? The matn’s own closing sentence turns the key —
«وَلَا فَرْقَ فِي جَمِيعِ هَذِهِ النَّوَاقِضِ بَيْنَ الهَازِلِ وَالجَادِّ
وَالخَائِفِ إِلَّا المُكْرَه» — and the compiler gathers Ibn Bāz’s words on the
barriers (موانع) that stand between the ruling on the act and the ruling on the
person: الإكراه، الجهل، الخطأ، التأويل.

This lesson: the مدخل (the النوع/المعين distinction that the whole section is
for) and the first barrier, مَانِعُ الإِكْرَاه. Printed folios 236–242
(PDF indices 233–239, offset +3).

The daleel is al-Naḥl 16:106. The structure follows the sharḥ:
  1. The matn’s closing sentence and what موانع التكفير means — the ruling on
     the act vs the ruling on the particular man. This is the exact thing
     nullifier 8 (the spy) ended pointing toward.
  2. The ijmāʿ: coercion to SAY kufr is excused; the ṣaḥīḥ view that coercion
     to DO an act of kufr is the same, «القول والعمل شيء واحد من جهة التكفير».
  3. Ibn Bāz’s definition of the مكره and his two conditions (الإكراه +
     الطمأنينة بالإيمان); and that leaving without coercion, or content with
     them, is «باء بإثم ذلك».
  4. الغضب — the three levels, Mūsā and the Tablets, and Ibn Bāz’s own fatwā
     that the one whose reason is overtaken is like the madman.
  5. What is NOT coercion: doing kufr for a job, position or wealth.
  6. The footnote on coercion to KILL — not lawful by ijmāʿ.

Rule 8: «مَنْ يُرِدِ اللهُ...» is not here; the one marfūʿ text used (al-ʿAbbās
report «أَمَّا ظَاهِرُك...») is carried from the sharḥ’s own footnote without a
grading of our own.
"""
from _nq_15_lib import B, p, ar, box, qa
from _nq_18_q import QS

b = B.objectives([
    'Explain what <strong>مَوَانِعُ تَكْفِيرِ المُعَيَّن</strong> means, and '
    'the one distinction the whole section exists to draw — the ruling on the '
    '<em>act</em> versus the ruling on a <em>particular person</em>.',
    'Give the matn’s own closing sentence and how its exception «%s» opens the '
    'barriers.' % ar('إِلَّا المُكْرَه'),
    'State the daleel of the barrier of coercion (al-Naḥl 16:106) and the '
    'ijmāʿ on coercion to <em>say</em> kufr.',
    'Give the ṣaḥīḥ position on coercion to <em>do</em> an act of kufr, and the '
    'reasoning «%s».' % ar('القَوْلُ وَالعَمَلُ شَيْءٌ وَاحِد'),
    'State Ibn Bāz’s <strong>two conditions</strong> for the excuse of the '
    'coerced, and the standing of one who acts with no coercion or is content.',
    'Give the three levels of <strong>الغَضَب</strong> and the ruling on one '
    'whose reason is overtaken, with the precedent the scholars cited.',
    'Name what is <strong>not</strong> coercion (acting for a post or wealth), '
    'and the ijmāʿ that coercion never makes lawful the killing of a '
    'maʿṣūm.',
])

b += B.provenance(236, 242)

# ----------------------------------------------- the مدخل
b += B.matn(
    'وَلَا فَرْقَ فِي جَمِيعِ هَذِهِ النَّوَاقِضِ بَيْنَ الهَازِلِ '
    'وَالجَادِّ وَالخَائِفِ إِلَّا المُكْرَه. '
    'نَعُوذُ بِاللهِ مِنْ مُوجِبَاتِ غَضَبِه، وَأَلِيمِ عِقَابِه، وَصَلَّى '
    'اللهُ عَلَى خَيْرِ خَلْقِهِ مُحَمَّد.',
    'The author seals the ten with a single sentence: in none of these '
    'nullifiers is there a difference between the one who jests, the one in '
    'earnest, and the one afraid — <em>except the one coerced</em>. '
    '<strong>That lone exception is the door to the last section of the '
    'book.</strong> The jester is not excused by his jest, nor the frightened '
    'by his fear — those were refused, one by one, in the clauses before. Only '
    '<em>al-mukrah</em>, the coerced, is set apart. And naming one barrier '
    'opens the question of the rest.')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:1rem"><strong>This is where the '
        'book turns from the act to the man.</strong></p>'
        '<p style="margin:0;font-size:.95rem">Everything before this named '
        '<em>what</em> nullifies Islām — the <strong>النَّوْع</strong>, the '
        'type of deed. This closing section asks the harder question: granting '
        'that an act is a nullifier, when may you rule that <em>this '
        'particular person</em> — <strong>المُعَيَّن</strong> — has left the '
        'religion by it? The two are not the same ruling, and the whole '
        'section is built to keep them apart.</p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<em>This is exactly the distinction the eighth nullifier ended '
      'pointing toward.</em> There, the spy Ḥāṭib ؓ did an act that in its '
      'type is betrayal — and he was <strong>not</strong> declared a '
      'disbeliever, because a barrier stood in the way of applying the ruling '
      'to <em>him</em>. «الحُكْمُ عَلَى الفِعْلِ شَيْء، وَالحُكْمُ عَلَى '
      'المُعَيَّنِ شَيْءٌ آخَر.» <strong>A thing may be kufr, and the man who '
      'did it may yet not be a kāfir</strong> — because takfīr of a named '
      'person requires that its conditions be met <em>and its barriers '
      'absent</em>.'))
b += B.prose(
    'Imām Ibn ʿAbd al-Wahhāb named one barrier in the matn — <em>coercion</em> '
    '— and the compiler gathers Ibn Bāz’s words on the four the scholars '
    'count: <strong>الإِكْرَاه</strong> (coercion), <strong>الجَهْل</strong> '
    '(ignorance), <strong>الخَطَأ</strong> (honest error) and '
    '<strong>التَّأْوِيل</strong> (misinterpretation). This lesson takes the '
    'first; the two after it take the rest. <em>Read them as the discipline '
    'the entire book has been teaching: the same scholars most willing to name '
    'a deed a nullifier are the most careful about pinning it on a man.</em>')

# ----------------------------------------------- مانع الإكراه
b += B.heading('مَانِعُ الإِكْرَاه', 'The Barrier of Coercion')
b += B.prose(
    '<strong>The matn’s one stated exception.</strong> A man forced, under '
    'threat he cannot escape, to utter or do kufr — while his heart holds '
    'firm — is not touched by it. The daleel is the verse revealed about '
    '%s ؓ (ʿAmmār ibn Yāsir), made to speak a word of disbelief under '
    'torture:' % ar('عَمَّارِ بْنِ يَاسِر'))
b += B.ayah(
    'مَن كَفَرَ بِاللَّهِ مِن بَعْدِ إِيمَانِهِ إِلَّا مَنْ أُكْرِهَ '
    'وَقَلْبُهُ مُطْمَئِنٌّ بِالْإِيمَانِ',
    'Whoever disbelieves in Allah after his belief — except one who is coerced '
    'while his heart is at rest upon faith…',
    'سُورَةُ النَّحْل · 16:106')
b += B.sharh(
    p('<strong>Ibn Bāz reads the coerced man as one <em>driven</em>, not one '
      'who chose.</strong> «المُكْرَهُ الَّذِي أُكْرِهَ بِالضَّرْبِ أَوْ '
      'بِالتَّهْدِيدِ بِالقَتْلِ مِمَّنْ يَظُنُّ إِيقَاعَهُ بِه... كَمَا أَنَّ '
      'مَنْ أُكْرِهَ عَلَى الكُفْرِ لَا يَكْفُرُ بِنُطْقِهِ بِالكُفْرِ بِسَبَبِ '
      'الإِكْرَاهِ عَلَيْه؛ لِأَنَّهُ مُلْجَأٌ إِلَى ذَلِك.» <em>His tongue '
      'moved; his will did not. The word is spoken to push away the whip or '
      'the sword, and the heart behind it never left.</em>'))
b += B.sharh(
    box('<p style="margin:0;font-size:.93rem"><strong>The footnote fixes the '
        'reach of the excuse.</strong> The scholars <em>agreed</em> that one '
        'coerced into <strong>saying</strong> kufr is excused. They differed '
        'over coercion into an <strong>act</strong> — and the ṣaḥīḥ view is '
        'that it too is excused: <em>«لِعُمُومِ الآيَة ﴿إِلَّا مَنْ '
        'أُكْرِه﴾ فَلَمْ تُقَيَّدْ بِقَوْلٍ أَوْ عَمَل... وَلِأَنَّ القَوْلَ '
        'وَالعَمَلَ شَيْءٌ وَاحِدٌ مِنْ جِهَةِ التَّكْفِير؛ وَإِذَا عُذِرَ '
        'بِقَوْلِ كَلِمَةِ الكُفْرِ عُذِرَ بِالعَمَل»</em>. The verse says «one '
        'coerced» without limiting it to speech.</p>') +
    p('<strong>Then the two conditions, named plainly:</strong>') +
    box('<p style="margin:0;font-size:.95rem"><span dir="rtl" lang="ar">'
        '«المُكْرَهُ... لَهُ شَرْطَانِ: '
        '<strong>١ ‑ الإِكْرَاه</strong>، وَهُوَ كَوْنُهُ يَعْجِزُ عَنِ '
        'التَّخَلُّص. '
        '<strong>٢ ‑ وَالطُّمَأْنِينَةُ بِالإِيمَان</strong>. فَإِذَا '
        'أُكْرِهَ وَقَلْبُهُ مُطْمَئِنٌّ بِالإِيمَانِ فَلَا شَيْءَ عَلَيْه؛ '
        'وَالإِثْمُ عَلَى مَنْ أَكْرَهَه.»</span></p>') +
    p('<strong>And the limit on the other side, which keeps the excuse '
      'honest:</strong> <em>«فَأَمَّا إِذَا خَرَجَ مِنْ غَيْرِ إِكْرَاه، أَوْ '
      'خَرَجَ مُكْرَهًا وَلَكِنِ اطْمَأَنَّ إِلَيْهِم — فَلَيْسَ بِمُكْرَه؛ '
      '<strong>بَاءَ بِإِثْمِ ذَلِك</strong>.»</em> Compulsion he cannot '
      'escape, and a heart that did not go over: remove either, and the '
      'barrier is gone.'))

# ----------------------------------------------- الغضب
b += B.heading('الغَضَبُ وَمَرَاتِبُه', 'Overwhelming Anger, and Its Three Levels')
b += B.prose(
    '<strong>Ibn Bāz places intense anger beside coercion, because both can '
    'take a man’s intent out of his own hands.</strong> He gives the people of '
    'knowledge’s three levels — and the ruling turns, as it did with coercion, '
    'on whether any choice remained.')
b += B.sharh(
    qa('المَرْتَبَةُ الأُولَى — أَنْ يَشْتَدَّ غَضَبُهُ حَتَّى يَفْقِدَ '
       'عَقْلَه؟',
       '«حُكْمُهُ حُكْمُ المَجَانِينِ وَالمَعَاتِيه؛ <strong>لَا يَتَرَتَّبُ '
       'عَلَى كَلَامِهِ حُكْم</strong> — لَا طَلَاقُه، وَلَا سَبُّه، وَلَا '
       'غَيْرُ ذَلِك.» A man whose reason is gone carries no ruling at all.') +
    qa('المَرْتَبَةُ الثَّانِيَة — دُونَ ذَلِك، يَغْلِبُ عَلَيْهِ الغَضَبُ '
       'حَتَّى يَصِيرَ كَالمَدْفُوعِ الَّذِي لَا يَسْتَطِيعُ التَّخَلُّص؟',
       'The scholars differed; and Ibn Bāz gives <em>his own</em> verdict: '
       '«هَذَا القَوْلُ أَرْجَحُ عِنْدِي، وَهُوَ الَّذِي أُفْتِي بِه» — he is '
       '«أَقْرَبُ إِلَى المَجْنُونِ... مِنْهُ إِلَى العَاقِلِ السَّلِيم», so '
       'no ṭalāq falls and no ridda is recorded, «لَكِنْ لَا مَانِعَ مِنْ '
       'كَوْنِهِ يُؤَدَّبُ بَعْضَ الأَدَب» by way of caution — <strong>but he '
       'is not judged with the ruling of the apostates</strong>.') +
    qa('المَرْتَبَةُ الثَّالِثَة — الغَضَبُ العَادِيُّ الَّذِي لَا يَزُولُ '
       'مَعَهُ العَقْل؟',
       '«تَقَعُ تَصَرُّفَاتُه... لِأَنَّ غَضَبَهُ خَفِيفٌ لَا يُغَيِّرُ '
       'عَلَيْهِ قَصْدَهُ وَلَا قَلْبَه.» Ordinary anger changes nothing; the '
       'man is sound of mind and his words stand.') +
    p('<strong>The precedent the scholars cited is Mūsā ﷺ.</strong> <em>When '
      'he found his people at the calf, «اشْتَدَّ غَضَبُهُ عَلَيْهِم», he '
      'threw down the Tablets and seized his brother’s head, dragging Hārūn '
      '— a Prophet like himself — toward him. «فَلَمْ يُؤَاخِذْهُ اللهُ لَا '
      'بِإِلْقَاءِ الأَلْوَاحِ وَلَا بِجَرِّ أَخِيه.» Had he done either in '
      'contempt, while composed, it would have been grave; but overtaking '
      'anger for Allah’s sake lifted the reckoning.</em> Ibn Taymiyyah and '
      'Ibn al-Qayyim, the sharḥ notes, chose this view and «بَسَطَا» its '
      'proofs.'))

# ----------------------------------------------- what is NOT coercion
b += B.heading('مَا لَيْسَ بِإِكْرَاه', 'What Is Not Coercion')
b += B.prose(
    '<strong>The barrier is for the one truly compelled — not for the one who '
    'bargains.</strong> Ibn Bāz draws the line at the motive.')
b += B.sharh(
    p('<em>He divides the man faced with a command into two:</em> '
      '«حَالٌ يُطِيعُهُ مُخْتَارًا — فَإِذَا قِيلَ لَه: اشْرَبِ الخَمْرَ '
      'شَرِبَ، وَإِذَا قِيلَ لَه: سُبَّ الدِّينَ سَبّ — <strong>فَهَذَا لَا '
      'عُذْرَ لَهُ فِي اخْتِيَارِه</strong>. وَالحَالُ الثَّانِي: يَكُونُ '
      'مُكْرَهًا» — threatened with a beating or death he believes will fall, '
      'or wine poured into his mouth by force. <em>The first obeys; the second '
      'is overpowered.</em>') +
    box('<p style="margin:0;font-size:.95rem"><strong>And the motive that '
        'voids the excuse outright:</strong> <em>«أَمَّا لِقَصْدِ الدُّنْيَا '
        'وَالطَّمَعِ وَالتَّوَسُّعِ فِي المَال، أَوْ لِأَجْلِ حَظِّ '
        'الرِّيَاسَة، أَوْ لِأَجْلِ الوَظِيفَة — <strong>فَهَذَا كُلُّهُ '
        'مُنْكَرٌ وَلَيْسَ بِعُذْر</strong>، نَعُوذُ بِاللهِ.»</em> A post, a '
        'rank, an income — none of these is the sword at the throat the verse '
        'is speaking of.</p>',
        wash='var(--accent-wash)', edge='var(--accent)'))
b += B.sharh(
    p('<strong>And the one place coercion stops even for the truly '
      'compelled:</strong> <em>killing a maʿṣūm.</em> The footnote gathers it '
      '— Ibn Taymiyyah: «لَوْ أُكْرِهَ رَجُلٌ رَجُلًا عَلَى قَتْلِ مُسْلِمٍ '
      'مَعْصُوم، فَإِنَّهُ لَا يَجُوزُ لَهُ قَتْلُهُ <strong>بِاتِّفَاقِ '
      'المُسْلِمِين</strong>... فَلَيْسَ حِفْظُ نَفْسِهِ بِقَتْلِ ذَلِكَ '
      'المَعْصُومِ أَوْلَى مِنَ العَكْس»; Ibn Rajab and al-Nawawī report the '
      'same ijmāʿ. <em>You may speak a word to save your life; you may not '
      'take a protected life to save it.</em>'))
b += B.prose(
    '<strong>So the first barrier, read whole, teaches the shape of all '
    'four.</strong> <em>It does not say the act was no kufr — it says the '
    'ruling is withheld from <em>this</em> man because something stood between '
    'him and his own will. The act keeps its name; the person is spared it. '
    'That is </em>māniʿ<em> — a barrier — and it is the generosity the book '
    'builds into its own gravest rulings.</em>')

# ----------------------------------------------- vocab, quiz, memorize
b += B.vocab([
    ('مَوَانِعُ تَكْفِيرِ المُعَيَّن', 'mawāniʿ takfīr al-muʿayyan',
     'the barriers to declaring a particular person a disbeliever',
     'The book’s closing section: the causes that withhold the ruling of kufr '
     'from a <em>named</em> man even when his act is a nullifier.'),
    ('النَّوْعُ وَالمُعَيَّن', 'al-nawʿ wa-l-muʿayyan',
     'the type and the particular',
     'The ruling on the <em>act</em> (that it is kufr) versus the ruling on '
     '<em>this man</em> (that he is a kāfir). Not the same ruling.'),
    ('المَانِع', 'al-māniʿ', 'the barrier / preventer',
     'A cause whose presence stops a ruling from falling — here, one of four: '
     'coercion, ignorance, honest error, misinterpretation.'),
    ('الإِكْرَاه', 'al-ikrāh', 'coercion',
     'The one barrier named in the matn itself. Its daleel is al-Naḥl 16:106, '
     'revealed about ʿAmmār ibn Yāsir ؓ.'),
    ('مُلْجَأ', 'muljaʾ', 'driven / compelled against one’s will',
     'Ibn Bāz’s word for the coerced man — moved to the act like one forced, '
     'his will overridden, not exercised.'),
    ('الطُّمَأْنِينَةُ بِالإِيمَان', 'al-ṭumaʾnīnah bi-l-īmān',
     'the heart’s rest upon faith',
     'The second condition of the excuse: the heart never went over. Without '
     'it, «بَاءَ بِإِثْمِ ذَلِك».'),
    ('مَعْصُوم', 'maʿṣūm', 'one whose life is inviolable',
     'Coercion excuses a word; it does not make lawful the killing of a '
     'maʿṣūm — by the agreement of the Muslims.'),
    ('بَاءَ بِإِثْمِه', 'bāʾa bi-ithmih', 'he bore its sin',
     'The standing of one who acts with no coercion, or goes over to them '
     'content: the barrier does not reach him.'),
])

b += B.mcq('nq-l18-mcq', QS)

b += B.tf('nq-l18-tf', [
    ('مَوَانِعُ تَكْفِيرِ المُعَيَّنِ مَعْنَاهَا: أَنَّ الفِعْلَ قَدْ يَكُونُ '
     'كُفْرًا وَلَا يُحْكَمُ عَلَى فَاعِلِهِ المُعَيَّنِ بِالكُفْرِ حَتَّى '
     'تَنْتَفِيَ المَوَانِع.',
     'The barriers to takfīr of a particular person mean: an act may be kufr '
     'while its named doer is not ruled a disbeliever until the barriers are '
     'absent.', True),
    ('مَنْ أُكْرِهَ عَلَى قَوْلِ الكُفْرِ لَا يُعْذَر، وَإِنَّمَا يُعْذَرُ '
     'المُكْرَهُ عَلَى الفِعْلِ فَقَط.',
     'One coerced into saying kufr is not excused; only coercion into an act '
     'is excused.', False),
    ('لِلْمُكْرَهِ شَرْطَانِ: العَجْزُ عَنِ التَّخَلُّص، وَالطُّمَأْنِينَةُ '
     'بِالإِيمَان.',
     'The coerced has two conditions: inability to escape, and the heart’s '
     'rest upon faith.', True),
    ('مَنْ فَعَلَ الكُفْرَ لِأَجْلِ الوَظِيفَةِ أَوِ المَالِ فَهُوَ مَعْذُورٌ '
     'كَالمُكْرَه.',
     'One who does kufr for the sake of a job or wealth is excused like the '
     'coerced.', False),
    ('مَنِ اشْتَدَّ بِهِ الغَضَبُ حَتَّى فَقَدَ عَقْلَهُ فَحُكْمُهُ حُكْمُ '
     'المَجْنُون، لَا يَتَرَتَّبُ عَلَى كَلَامِهِ حُكْم.',
     'One whose reason is lost through intense anger carries the ruling of the '
     'insane; no ruling attaches to his words.', True),
    ('الإِكْرَاهُ يُبِيحُ قَتْلَ المَعْصُومِ لِحِفْظِ النَّفْس.',
     'Coercion makes lawful the killing of an inviolable person to preserve '
     'one’s own life.', False),
    ('خَتَمَ المُؤَلِّفُ النَّوَاقِضَ بِقَوْلِهِ: لَا فَرْقَ بَيْنَ الهَازِلِ '
     'وَالجَادِّ وَالخَائِفِ إِلَّا المُكْرَه.',
     'The author sealed the nullifiers by saying: no difference between the '
     'jester, the earnest and the fearful — except the coerced.', True),
])

b += B.memorize(
    'المُكْرَهُ لَهُ شَرْطَانِ: الإِكْرَاهُ وَهُوَ كَوْنُهُ يَعْجِزُ عَنِ '
    'التَّخَلُّص، وَالطُّمَأْنِينَةُ بِالإِيمَان؛ فَإِذَا أُكْرِهَ وَقَلْبُهُ '
    'مُطْمَئِنٌّ بِالإِيمَانِ فَلَا شَيْءَ عَلَيْه، وَالإِثْمُ عَلَى مَنْ '
    'أَكْرَهَه',
    'Ibn Bāz on the first of the four barriers. <strong>This is the shape of '
    'every barrier in miniature.</strong> <em>A deed can be kufr in its type '
    'and still not fall upon the man who did it — here because he was '
    'overpowered, his will overridden and his heart unmoved. The act keeps its '
    'name; the person is shielded by a </em>māniʿ<em>. It is the same care the '
    'eighth nullifier showed with the spy, now made a principle: the ruling on '
    'an act and the ruling on a particular man are two rulings.</em>')

b += B.nav('nq-l17-al-irad-an-al-din.html',
           'النَّاقِضُ العَاشِر',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l18')

B.write('nq-l18-mawani-al-ikrah.html',
        'مَوَانِعُ التَّكْفِير · مَانِعُ الإِكْرَاه',
        'The Barriers to Takfīr — Coercion',
        'The capstone of the Nawāqiḍ, from the words of Shaykh Ibn Bāz: the '
        'barriers to declaring a particular person a disbeliever (mawāniʿ '
        'takfīr al-muʿayyan). The matn’s own closing sentence — no difference '
        'between the jester, the earnest and the fearful except the coerced — '
        'opens the distinction between the ruling on an act and the ruling on a '
        'named person. The first barrier, coercion, on al-Naḥl 16:106: the '
        'ijmāʿ that coercion to say kufr is excused and the ṣaḥīḥ view that '
        'coercion to an act is the same; Ibn Bāz’s two conditions — inability '
        'to escape and the heart’s rest upon faith; the three levels of '
        'overwhelming anger with the precedent of Mūsā and the Tablets; that '
        'acting for a job, rank or wealth is not coercion; and the ijmāʿ that '
        'coercion never makes lawful the killing of an inviolable person.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ الثَّامِنَ عَشَر', '6', b)
print('wrote nq-l18-mawani-al-ikrah.html')
