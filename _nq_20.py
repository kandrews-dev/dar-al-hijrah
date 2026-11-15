# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 20 — مَانِعُ الخَطَأ + مَانِعُ التَّأْوِيل + خَاتِمَةُ المَتْن.

The last of the capstone, and the close of the whole book. Printed folios
272–280 (PDF indices 269–277, offset +3).

Two barriers remain after coercion and ignorance:
  • مَانِعُ الخَطَأ — the honest slip: a Muslim may utter a word of kufr from
    overwhelming joy or anger «فلا يكفر بها؛ لعدم القصد». The man who, from the
    intensity of joy at his found mount, said «اللهم أنت عبدي وأنا ربك». Daleel:
    al-Baqarah 2:286, with Ibn Taymiyyah that the scholars of the Muslims are
    not takfīr'd by mere محض خطأ.
  • مَانِعُ التَّأْوِيل — the barrier most easily abused, so the sharḥ cuts it
    both ways: a CORRUPT taʾwīl of a CLEAR text is no excuse (Imām Muḥammad:
    «التأويل الفاسد... ليس عذرًا؛ بل زيادة في الكفر»; Iblīs's shubhah; the
    Khawārij «بالإجماع ... باجتهاد وتقرب إلى الله» yet مرقوا) — but a taʾwīl in
    a genuine place of ikhtilāf and shubhah DOES excuse (the woman's face: «ليس
    بجيد... مسألة خلاف وفيها شبهة؛ لكنها عاصية»; denying the siḥr ḥadīth: «له
    شبهة... مخطئ»), while denial of a PLAIN established matter after bayān and
    persistence is kufr (the Dajjāl, nuzūl ʿĪsā).

Then the khātimah: the matn's closing words and Ibn Bāz on «خير خلقه»; and the
lesson lands the whole section — the ruling on the act and the ruling on the
man are two rulings.

Rule 8: the Khawārij ḥadīth «شر قتلى تحت أديم السماء...» is quoted as the sharḥ
gives it, from the Prophet ﷺ, without adding a grading of our own; 2:286's
«قد فعلت» is named «في الصحيح» as the sharḥ's footnote names it.
"""
from _nq_15_lib import B, p, ar, box, qa
from _nq_20_q import QS

b = B.objectives([
    'State <strong>مَانِعُ الخَطَأ</strong> — the slip of the tongue from joy '
    'or anger — with the sharḥ’s own example, and why the absence of intent '
    'removes the ruling.',
    'Give the daleel of honest error (al-Baqarah 2:286) and Ibn Taymiyyah’s '
    'principle that the scholars of the Muslims are not declared disbelievers '
    'for «%s».' % ar('مُجَرَّدِ الخَطَأِ المَحْض'),
    'State Imām Muḥammad ibn ʿAbd al-Wahhāb’s ruling on '
    '<strong>التَّأْوِيلُ الفَاسِد</strong> of a clear text, with the case of '
    'Iblīs.',
    'Use the <strong>Khawārij</strong> to show that sincere interpretation '
    'does not shield from مُرُوق when the text is clear.',
    'Draw the line the other way — where taʾwīl <em>does</em> excuse (a place '
    'of ikhtilāf and shubhah) — with the sharḥ’s two worked cases.',
    'Give the <strong>khātimah</strong> of the matn and Ibn Bāz’s gloss of '
    '«%s».' % ar('خَيْرِ خَلْقِه'),
    'State, over all four barriers, the one principle the whole section was '
    'built to establish — the ruling on the <em>act</em> versus the ruling on '
    'the <em>man</em>.',
])

b += B.provenance(272, 280)

# ----------------------------------------------- مانع الخطأ
b += B.heading('مَانِعُ الخَطَأ', 'The Barrier of Honest Error')
b += B.prose(
    '<strong>The third barrier is the gentlest, and the easiest to picture.</strong> '
    'A word of kufr may leave a Muslim’s tongue with no will behind it at all '
    '— carried out by a surge of joy or grief or rage. He did not mean it, and '
    'he is not touched by it.')
b += B.sharh(
    p('<strong>Ibn Bāz states it on the absence of intent:</strong> «قَدْ '
      'يَنْطِقُ المُسْلِمُ بِكَلِمَةِ الكُفْرِ لِغَلَبَةِ فَرَحٍ أَوْ غَضَبٍ '
      'أَوْ نَحْوِهِمَا، فَلَا يَكْفُرُ بِهَا؛ <strong>لِعَدَمِ '
      'القَصْد</strong>.»') +
    box('<p style="margin:0;font-size:.95rem"><strong>The example is the man '
        'of the lost mount.</strong> <em>He had despaired of it in the desert, '
        'then found it — and, «أَخْطَأَ مِنْ شِدَّةِ الفَرَح», meaning to say '
        '«O Allah, You are my Lord and I am Your servant», his tongue '
        'stumbled into:</em> «اللَّهُمَّ أَنْتَ عَبْدِي وَأَنَا رَبُّك». '
        '<em>The gravest inversion of words — and no kufr, because the heart '
        'behind them never moved toward it.</em></p>'))
b += B.ayah(
    'رَبَّنَا لَا تُؤَاخِذْنَا إِن نَّسِينَا أَوْ أَخْطَأْنَا',
    'Our Lord, do not take us to task if we forget or err.',
    'سُورَةُ البَقَرَة · 2:286')
b += B.sharh(
    p('<strong>The footnote raises the barrier from a man to a '
      'principle.</strong> <em>Ibn Taymiyyah:</em> «اتَّفَقَ أَهْلُ '
      'السُّنَّةِ وَالجَمَاعَةِ عَلَى أَنَّ عُلَمَاءَ المُسْلِمِينَ لَا '
      'يَجُوزُ تَكْفِيرُهُمْ <strong>بِمُجَرَّدِ الخَطَأِ المَحْض</strong>؛ '
      'بَلْ كُلُّ أَحَدٍ يُؤْخَذُ مِنْ قَوْلِهِ وَيُتْرَك، إِلَّا رَسُولَ '
      'اللهِ ﷺ.» <em>Over this verse, the sharḥ notes, the Prophet ﷺ reported '
      'that Allah said «قَدْ فَعَلْت» — I have done it. The error of a heart '
      'that sought the truth, he adds in </em>Minhāj al-Sunnah<em>, is nearer '
      'to Allah’s pardon than the deliberate sin of one who knew.</em>'))

# ----------------------------------------------- مانع التأويل
b += B.heading('مَانِعُ التَّأْوِيل', 'The Barrier of Interpretation — Cut Both Ways')
b += B.prose(
    '<strong>This is the barrier most often turned into a skeleton key, so the '
    'sharḥ is careful to cut it on both edges.</strong> Not every '
    'interpretation excuses; and not every interpretation condemns. The whole '
    'skill is the line between them.')
b += B.sharh(
    box('<p style="margin:0;font-size:.95rem"><strong>One edge — a corrupt '
        'taʾwīl of a <em>clear</em> text is no excuse.</strong> <em>Imām '
        'Muḥammad ibn ʿAbd al-Wahhāb:</em> «التَّأْوِيلُ الفَاسِدُ فِي '
        'النُّصُوصِ لَيْسَ عُذْرًا لِصَاحِبِه؛ كَمَا أَنَّهُ سُبْحَانَهُ '
        '<strong>لَمْ يَعْذِرْ إِبْلِيسَ فِي شُبْهَتِهِ</strong> الَّتِي '
        'أَبْدَاهَا؛ بَلْ كَانَ ذَلِكَ التَّأْوِيلُ زِيَادَةً فِي الكُفْر»؛ '
        'وَ«الشُّبْهَةُ إِذَا كَانَتْ وَاضِحَةَ البُطْلَانِ لَا عُذْرَ '
        'لِصَاحِبِهَا».</p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<em>Iblīs is the first case of «I had my reasoning»: he read his being '
      'made of fire against the plain command to prostrate — and the reading '
      'did not excuse him; it deepened the sin.</em> «وَلَا يُقَاسُ الخَطَأُ '
      'فِي أَصْلِ الدِّينِ وَشَهَادَةِ أَنْ لَا إِلَهَ إِلَّا اللهُ '
      'بِالخَطَأِ فِي غَيْرِه.»'))
b += B.sharh(
    p('<strong>The decisive case is the Khawārij — because no one ever doubted '
      'their sincerity.</strong> <em>They «تَأَوَّلُوا النُّصُوصَ عَلَى '
      'غَيْرِ تَأْوِيلِهَا، فَقَاتَلُوا أَهْلَ الإِسْلَامِ وَتَرَكُوا أَهْلَ '
      'الأَوْثَان، وَكَفَّرُوا عَلِيًّا» — and the footnote says it plainly:</em> '
      '«وَهُمْ بِالإِجْمَاعِ لَمْ يَفْعَلُوا مَا فَعَلُوا إِلَّا '
      'بِاجْتِهَادٍ وَتَقَرُّبٍ إِلَى اللهِ؛ <strong>فَلَمْ يَكُنِ '
      'التَّأْوِيلُ هُنَا مَانِعًا لَهُمْ مِنَ المُرُوق</strong>.»') +
    p('<em>And the Prophet ﷺ placed them, for all their worship, outside:</em> '
      '«إِنَّهُمْ شَرُّ قَتْلَى تَحْتَ أَدِيمِ السَّمَاء، وَأَنَّهُمْ '
      'يَمْرُقُونَ مِنَ الإِسْلَامِ ثُمَّ لَا يَعُودُونَ إِلَيْه». <strong>So '
      'a sincere interpretation of a clear text is not a shield — it can be '
      'the very thing that carries a man through the religion and out the '
      'other side.</strong>'))
b += B.heading('حَيْثُ يَكُونُ التَّأْوِيلُ عُذْرًا', 'Where Interpretation Does Excuse')
b += B.prose(
    '<strong>Now the other edge, so the barrier is not read as a hammer.</strong> '
    'Where the matter is a genuine place of scholarly difference, carrying a '
    'real doubt, the one who errs in it is <em>not</em> declared a disbeliever '
    '— though he may be mistaken, or sinning.')
b += B.sharh(
    qa('شَيْخٌ أَفْتَى بِأَنَّ المَرْأَةَ الَّتِي تَسْتَحِلُّ كَشْفَ وَجْهِهَا '
       '— مَعَ عِلْمِهَا بِمَا وَرَدَ — تَكْفُر؟',
       '«الحُكْمُ بِكُفْرِهَا <strong>لَيْسَ بِجَيِّد</strong>؛ لِأَنَّهَا '
       'مَسْأَلَةُ خِلَافٍ بَيْنَ العُلَمَاءِ وَفِيهَا شُبْهَة؛ لَكِنَّهَا '
       'عَلَى كُلِّ حَالٍ تَكُونُ عَاصِيَةً بِذَلِك.» <em>A disputed matter '
       'with a live doubt is a place of sin, not of takfīr.</em>') +
    qa('مَنْ أَنْكَرَ حَدِيثَ عَائِشَةَ فِي سِحْرِ النَّبِيِّ ﷺ؟',
       '«لَا يَصِيرُ حُكْمُهُ حُكْمَ الكَفَرَة؛ <strong>لَهُ شُبْهَة؛ لَكِنْ '
       'يُعْلَمُ أَنَّهُ مُخْطِئ</strong>.» Mistaken, and told so — not '
       'cast out.') +
    p('<strong>But the line holds firm where the matter is plain.</strong> '
      '<em>One who denies the Dajjāl, or the descent of ʿĪsā, or Yaʾjūj and '
      'Maʾjūj — after the people of knowledge have made it clear to him and he '
      'persists — «فَيَكُونُ كَافِرًا... لَا شَكَّ فِي كُفْرِهِ وَلَا '
      'تَوَقُّف», only denial of al-Mahdī alone admitting تَوَقُّفًا. The doubt '
      'excuses where a doubt can honestly stand; it does not manufacture one '
      'over a matter known by necessity.</em>'))

# ----------------------------------------------- khātimah
b += B.heading('خَاتِمَةُ المَتْن', 'The Seal of the Book')
b += B.prose(
    '<strong>Imām Muḥammad ibn ʿAbd al-Wahhāb ends the whole matn not on a '
    'ruling but on fear and on ṣalāh upon the Messenger ﷺ.</strong>')
b += B.matn(
    'وَكُلُّهَا مِنْ أَعْظَمِ مَا يَكُونُ خَطَرًا، وَمِنْ أَكْثَرِ مَا '
    'يَكُونُ وُقُوعًا، فَيَنْبَغِي لِلْمُسْلِمِ أَنْ يَحْذَرَهَا '
    'وَيَخَافَ مِنْهَا عَلَى نَفْسِه. نَعُوذُ بِاللهِ مِنْ مُوجِبَاتِ '
    'غَضَبِهِ وَأَلِيمِ عِقَابِه، وَصَلَّى اللهُ عَلَى خَيْرِ خَلْقِهِ '
    'مُحَمَّد.',
    'And all of them are among the gravest of dangers and the most frequent in '
    'occurrence — so it befits the Muslim to beware of them and to fear them '
    'for himself. We seek refuge in Allah from the causes of His anger and the '
    'pain of His punishment; and may Allah send blessings upon the best of His '
    'creation, Muḥammad.')
b += B.sharh(
    p('<strong>Ibn Bāz pauses on the last two words of the book — «خَيْرِ '
      'خَلْقِه».</strong> «هُوَ أَفْضَلُ الكَوْن، هُوَ أَفْضَلُ '
      'المَخْلُوقَات ﷺ، سَيِّدُ وَلَدِ آدَم، وَأَفْضَلُ الخَلْق، وَخَيْرُ '
      'البَرِيَّة ﷺ.»') +
    p('<em>There is a fitness in it. A book that walked, clause by clause, '
      'through the ten ways a heart can leave Islām, and then through the '
      'barriers that guard a man from being wrongly cast out, closes by '
      'turning the reader’s face to the one whose way is the opposite of every '
      'nullifier — and asking blessings upon him.</em>'))
b += B.prose(
    '<strong>And this is the whole section in one line.</strong> <em>Across '
    'four barriers — coercion, ignorance, honest error, interpretation — the '
    'book has taught a single discipline: the ruling on an </em>act<em> and '
    'the ruling on a </em>man<em> are two rulings. A deed may be a nullifier '
    'in its very type, and the person who did it may yet not be a disbeliever '
    '— because he was compelled, or ignorant of a hidden matter, or slipped, '
    'or held a doubt a doubt could honestly hold. The barriers are real. They '
    'are also only barriers: lift them, with a cause of takfīr established, and '
    'the ruling falls. </em><strong>To name a deed kufr is one thing; to pass '
    'judgement on a soul is another — and the book that was most willing to do '
    'the first spends its final pages teaching caution in the second.</strong>')

# ----------------------------------------------- vocab, quiz, memorize
b += B.vocab([
    ('مَانِعُ الخَطَأ', 'māniʿ al-khaṭaʾ', 'the barrier of honest error',
     'A word of kufr uttered from overwhelming joy or anger, with no intent — '
     '«فَلَا يَكْفُرُ بِهَا؛ لِعَدَمِ القَصْد».'),
    ('عَدَمُ القَصْد', 'ʿadam al-qaṣd', 'absence of intent',
     'Why the slip does not disbelieve: the tongue moved, the will did not. '
     'The man of the lost mount who inverted his own words from joy.'),
    ('الخَطَأُ المَحْض', 'al-khaṭaʾ al-maḥḍ', 'pure, honest error',
     'Ibn Taymiyyah: the scholars of the Muslims are not declared disbelievers '
     'by it; «كُلُّ أَحَدٍ يُؤْخَذُ مِنْ قَوْلِهِ وَيُتْرَك، إِلَّا رَسُولَ '
     'اللهِ ﷺ».'),
    ('مَانِعُ التَّأْوِيل', 'māniʿ al-taʾwīl', 'the barrier of interpretation',
     'Cut both ways: a corrupt taʾwīl of a clear text is no excuse; a taʾwīl '
     'in a genuine place of ikhtilāf and shubhah excuses.'),
    ('التَّأْوِيلُ الفَاسِد', 'al-taʾwīl al-fāsid', 'corrupt interpretation',
     'Imām Muḥammad: «لَيْسَ عُذْرًا... بَلْ زِيَادَةٌ فِي الكُفْر» — as '
     'Iblīs’s shubhah did not excuse him but deepened his sin.'),
    ('المُرُوق', 'al-murūq', 'shooting clean through [and out of] the religion',
     'The Prophet’s ﷺ word for the Khawārij: for all their worship and '
     'sincerity, «يَمْرُقُونَ مِنَ الإِسْلَامِ ثُمَّ لَا يَعُودُون».'),
    ('شُبْهَة', 'shubhah', 'a doubt / specious argument',
     'Where one can honestly stand, taʾwīl excuses (the face, the siḥr '
     'ḥadīth); where its falsehood is plain, «لَا عُذْرَ لِصَاحِبِهَا».'),
    ('خَيْرُ خَلْقِه', 'khayru khalqih', 'the best of His creation',
     'The last words of the matn. Ibn Bāz: «أَفْضَلُ المَخْلُوقَات، سَيِّدُ '
     'وَلَدِ آدَم» ﷺ — the book seals on blessings upon him.'),
])

b += B.mcq('nq-l20-mcq', QS)

b += B.tf('nq-l20-tf', [
    ('مَنْ نَطَقَ بِكَلِمَةِ الكُفْرِ لِغَلَبَةِ فَرَحٍ أَوْ غَضَبٍ بِلَا '
     'قَصْدٍ لَا يَكْفُرُ بِهَا.',
     'One who utters a word of kufr through overwhelming joy or anger, without '
     'intent, does not disbelieve by it.', True),
    ('التَّأْوِيلُ الفَاسِدُ لِلنَّصِّ الوَاضِحِ عُذْرٌ لِصَاحِبِهِ عِنْدَ '
     'أَهْلِ السُّنَّة.',
     'A corrupt interpretation of a clear text is an excuse for its holder, in '
     'the view of ahl al-sunnah.', False),
    ('الخَوَارِجُ تَأَوَّلُوا النُّصُوصَ وَتَقَرَّبُوا بِاجْتِهَادِهِم، '
     'وَمَعَ ذَلِكَ مَرَقُوا مِنَ الإِسْلَام.',
     'The Khawārij interpreted the texts and drew near [to Allah] by their '
     'striving, and yet shot clean out of Islām.', True),
    ('المَرْأَةُ الَّتِي تَسْتَحِلُّ كَشْفَ وَجْهِهَا يُحْكَمُ بِكُفْرِهَا '
     'عِنْدَ ابْنِ بَاز.',
     'Ibn Bāz ruled that a woman who deems uncovering her face permissible '
     'disbelieves.', False),
    ('مَنْ أَنْكَرَ الدَّجَّالَ وَنُزُولَ عِيسَى بَعْدَ البَيَانِ وَأَصَرَّ '
     'فَلَا شَكَّ فِي كُفْرِه.',
     'One who denies the Dajjāl and the descent of ʿĪsā after clarification '
     'and persists — there is no doubt about his disbelief.', True),
    ('عُلَمَاءُ المُسْلِمِينَ يُكَفَّرُونَ بِمُجَرَّدِ الخَطَأِ المَحْض.',
     'The scholars of the Muslims are declared disbelievers for mere honest '
     'error.', False),
    ('خَتَمَ ابْنُ بَازٍ بِأَنَّ النَّبِيَّ ﷺ خَيْرُ خَلْقِ اللهِ، سَيِّدُ '
     'وَلَدِ آدَمَ وَأَفْضَلُ الخَلْق.',
     'Ibn Bāz sealed with: the Prophet ﷺ is the best of Allah’s creation, the '
     'master of the children of Ādam and the most excellent of creation.',
     True),
])

b += B.memorize(
    'التَّأْوِيلُ الفَاسِدُ فِي النُّصُوصِ لَيْسَ عُذْرًا لِصَاحِبِه؛ كَمَا '
    'أَنَّهُ سُبْحَانَهُ لَمْ يَعْذِرْ إِبْلِيسَ فِي شُبْهَتِهِ الَّتِي '
    'أَبْدَاهَا، بَلْ كَانَ ذَلِكَ التَّأْوِيلُ زِيَادَةً فِي الكُفْر',
    'Imām Muḥammad ibn ʿAbd al-Wahhāb, on the last of the four barriers — and '
    'the close of the whole book. <strong>Hold it beside its other edge.</strong> '
    '<em>Interpretation excuses where a doubt can honestly stand — a real '
    'place of scholarly difference. It does not excuse a corrupt reading of a '
    'text that is clear; there, as with Iblīs reasoning against the plain '
    'command, the «interpretation» only deepens the sin. This is the whole '
    'discipline of the capstone: the barriers of coercion, ignorance, error '
    'and taʾwīl are real and they shield the man — but they are barriers, not '
    'a wall, and the ruling on an act was never the same as the ruling on a '
    'soul.</em>')

b += B.nav('nq-l19-mani-al-jahl.html',
           'مَانِعُ الجَهْل',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l20')

B.write('nq-l20-mani-al-khata-wa-al-tawil.html',
        'مَوَانِعُ التَّكْفِير · الخَطَأ وَالتَّأْوِيل وَالخَاتِمَة',
        'The Barriers to Takfīr — Error, Interpretation, and the Seal',
        'The close of the Nawāqiḍ, from the words of Shaykh Ibn Bāz: the last '
        'two barriers to takfīr of a particular person and the seal of the '
        'matn. Honest error — a word of kufr uttered from overwhelming joy or '
        'anger with no intent, as the man who from joy at his found mount '
        'inverted his own words; on al-Baqarah 2:286, with Ibn Taymiyyah that '
        'the scholars of the Muslims are not declared disbelievers for mere '
        'honest error. Interpretation, cut both ways: a corrupt taʾwīl of a '
        'clear text is no excuse — Imām Muḥammad ibn ʿAbd al-Wahhāb on Iblīs, '
        'and the Khawārij who interpreted sincerely and yet shot out of Islām; '
        'but a taʾwīl in a genuine place of ikhtilāf and doubt does excuse — '
        'the woman’s face, denying the ḥadīth of the bewitchment — while '
        'denying a plain established matter after clarification and persisting '
        'is kufr. The khātimah: the matn’s closing words and Ibn Bāz on «the '
        'best of His creation»; and the principle the whole section was built '
        'to establish — the ruling on an act and the ruling on a particular '
        'person are two rulings.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ العِشْرُون', '6', b)
print('wrote nq-l20-mani-al-khata-wa-al-tawil.html')
