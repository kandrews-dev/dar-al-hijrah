# -*- coding: utf-8 -*-
"""Nawāqiḍ lesson 16 — النَّاقِضُ التَّاسِع: being outside the sharīʿah.

Printed folios 223-227 (PDF indices 220-224, offset +3); index 225 opens the
tenth nullifier, which fixes the end of the range. Five folios, one lesson.

The clause: «مَنِ اعْتَقَدَ أَنَّ بَعْضَ النَّاسِ يَسَعُهُ الخُرُوجُ عَنْ
شَرِيعَةِ مُحَمَّدٍ ﷺ كَمَا وَسِعَ الخَضِرَ الخُرُوجُ عَنْ شَرِيعَةِ مُوسَى».

What makes this clause teachable — and why a shaykh loves it — is that the
deviant's own proof-text refutes him. The Sufi who claims to stand ABOVE the
sharīʿah cites al-Khiḍr; and al-Khiḍr was an independent prophet acting on his
own revelation, with no relation to Mūsā's sharīʿah whatsoever. The very story
he leans on is the answer to him.

Structure, following the sharḥ's own weighting:
  1. The clause, and the two readings of the al-Khiḍr story.
  2. The hinge — the universality of the Prophet's ﷺ message (7:158, 34:28),
     and al-Khiḍr as nabī mustaqill.
  3. Awliyāʾ never above anbiyāʾ — walāyah is BY following, never by bypassing.
  4. No station lifts the sharīʿah — isqāṭ al-taklīf is kufr (15:99), and the
     Rusul, the most knowledgeable, were themselves mukallaf.
  5. «حَدَّثَنِي قَلْبِي عَنْ رَبِّي» — the heart is not maʿṣūm; only the Book
     and the authentic Sunnah are.
  6. The ruling, and praying behind such a person.
  7. The footnote's live application: those who hold the People of the Book
     need not follow Muḥammad ﷺ because jizyah exempts them.

Rule 8: the one marfūʿ text on these folios is al-Khiḍr's words to Mūsā, which
the sharḥ quotes from the well-known story without a grading of its own; the
page names its home in the Ṣaḥīḥayn (muttafaq ʿalayh) and adds nothing beyond
that.
"""
from _nq_15_lib import B, p, ar, box, row, row3, thead3, table, qa
from _nq_16_q import QS

b = B.objectives([
    'State the ninth nullifier in the matn’s own words, and the ruling on one '
    'who falls into it.',
    'Explain <strong>why the al-Khiḍr story is no precedent</strong> for '
    'standing outside the sharīʿah — what al-Khiḍr was, and what he was not.',
    'Give the two verses that establish the Prophet’s ﷺ message is '
    '<strong>universal</strong>, and why that closes the door this clause '
    'guards.',
    'State the rule on the <strong>awliyāʾ and the anbiyāʾ</strong> — who is '
    'above whom, and in what walāyah actually consists.',
    'Refute <strong>إِسْقَاطُ التَّكْلِيف</strong> — the claim that gnosis '
    'lifts worship — from al-Ḥijr 15:99 and from the state of the Messengers '
    'themselves.',
    'Answer «%s»: is the heart an authority, and what is?'
    % ar('حَدَّثَنِي قَلْبِي عَنْ رَبِّي'),
    'Give the footnote’s contemporary application — who holds that the People '
    'of the Book need not follow Muḥammad ﷺ, and why it is «%s».'
    % ar('ضَلَالٌ مُبِين'),
])

b += B.provenance(223, 227)

b += B.matn(
    'التَّاسِع: مَنِ اعْتَقَدَ أَنَّ بَعْضَ النَّاسِ يَسَعُهُ الخُرُوجُ '
    'عَنْ شَرِيعَةِ مُحَمَّدٍ ﷺ كَمَا وَسِعَ الخَضِرَ الخُرُوجُ عَنْ '
    'شَرِيعَةِ مُوسَى عَلَيْهِ السَّلَام.',
    'Read what the clause actually says before the explanation: it is not '
    'about disobeying the sharīʿah — it is about <strong>believing one is '
    'entitled to stand outside it</strong>, and it reaches for the one story '
    'in the Qurʾān that looks, to a careless eye, like a precedent.')
b += B.sharh(
    box('<p style="margin:0 0 .5rem;font-size:.95rem"><em>«Whoever holds that '
        'it is permissible for him to exit the sharīʿah of Muḥammad ﷺ, as '
        'al-Khiḍr was permitted to exit the sharīʿah of Mūsā — '
        '<strong>فَهُوَ كَافِرٌ بِإِجْمَاعِ أَهْلِ العِلْم</strong>: he is a '
        'disbeliever by the consensus of the people of knowledge. He is asked '
        'to repent and the evidences are made clear to him; if he repents, '
        'else he is killed.»</em></p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>The clause names a claim, not a lapse.</strong> <em>A man who '
      'sins against the sharīʿah while holding it binding over him is a '
      'sinner. A man who holds that the sharīʿah does not reach him at all — '
      'that he has climbed above it — has stepped outside the religion, '
      'because he has denied the one thing that makes him a Muslim: that '
      'Muḥammad ﷺ was sent to him.</em>'))

# ----------------------------------------------- the misread story
b += B.heading('قِصَّةُ الخَضِرِ لَا تَنْفَعُهُ', 'The al-Khiḍr Story Is No Refuge for Him')
b += B.prose(
    '<strong>This is the heart of the clause, and it is the kind of answer a '
    'teacher savours: the deviant’s own proof-text is the refutation of '
    'him.</strong> The claim — made, Ibn Bāz says, by «%s», the deviant '
    'zanādiqah of the Sufis — is that a man may receive knowledge directly '
    'from Allah «%s», be told and commanded and forbidden by his Lord in his '
    'heart, and so <em>dispense with following the Messenger ﷺ</em>, just as '
    'al-Khiḍr acted on a knowledge Mūsā did not have.'
    % (ar('كَثِيرٌ مِنَ الصُّوفِيَّةِ الضَّالِّينَ الزَّنَادِقَة'),
       ar('مِنْ طَرِيقِ التَّحْدِيثِ الَّذِي يَقَعُ فِي القَلْب')))
b += B.sharh(
    p('<strong>Ibn Bāz dismantles the analogy at its root:</strong> '
      '<em>«فَإِنَّ الخَضِرَ لَيْسَ مِنْ بَنِي إِسْرَائِيل، وَلَيْسَ مُوسَى '
      'مَبْعُوثًا إِلَيْه؛ <strong>فَالخَضِرُ نَبِيٌّ مُسْتَقِلٌّ لَيْسَ '
      'لَهُ تَعَلُّقٌ بِمُوسَى</strong>، وَمُوسَى إِنَّمَا بُعِثَ إِلَى '
      'بَنِي إِسْرَائِيل.»</em>') +
    p('<strong>So al-Khiḍr never was «outside Mūsā’s sharīʿah» in the sense '
      'the Sufi needs.</strong> <em>He was never under it to begin with. He '
      'was an independent prophet with his own revelation from Allah — '
      '«وَلَهُ نُبُوَّة، وَلَهُ وَحْيٌ مِنْ جِهَةِ اللهِ غَيْرُ مَا جَاءَ '
      'بِهِ مُوسَى». The story is not a man bypassing a sharīʿah by way of '
      'his heart; it is two prophets, each carrying revelation.</em>'))
b += B.hadith(
    'إِنَّكَ عَلَى عِلْمٍ مِنْ عِلْمِ اللهِ عَلَّمَكَهُ اللهُ لَا أَعْلَمُهُ '
    'أَنَا، وَأَنَا عَلَى عِلْمٍ مِنْ عِلْمِ اللهِ عَلَّمَنِيهِ لَا '
    'تَعْلَمُهُ أَنْتَ',
    'You are upon a knowledge from Allah’s knowledge which He taught you that '
    'I do not know; and I am upon a knowledge from Allah’s knowledge which He '
    'taught me that you do not know.',
    'قَوْلُ الخَضِرِ لِمُوسَى، مِنْ حَدِيثِهِمَا المَشْهُورِ — مُتَّفَقٌ '
    'عَلَيْهِ؛ the sharḥ quotes it from the well-known story and grades it no '
    'further, so the page names only its home in the Ṣaḥīḥayn.')
b += B.prose(
    '<strong>Notice what al-Khiḍr’s own sentence does to the argument.</strong> '
    'Each of the two had <em>a knowledge from Allah</em> — by revelation, by '
    'prophethood. Neither was leaning on a whisper in the breast. <strong>The '
    'man who cites this story to justify «حَدَّثَنِي قَلْبِي عَنْ رَبِّي» is '
    'quoting the very proof that sinks him</strong>: al-Khiḍr had waḥy; he has '
    'a feeling.')

# ----------------------------------------------- the hinge: universality
b += B.heading('رِسَالَةٌ عَامَّة', 'A Message Sent to All')
b += B.prose(
    '<strong>Behind the correction sits the doctrine the whole clause '
    'guards.</strong> Every prophet before our Prophet ﷺ was sent '
    '<em>to his own people specifically</em> — «وَكُلُّ نَبِيٍّ قَبْلَ '
    'نَبِيِّنَا يُبْعَثُ إِلَى قَوْمِهِ خَاصَّة». Muḥammad ﷺ was not.')
b += B.ayah(
    'قُلْ يَا أَيُّهَا النَّاسُ إِنِّي رَسُولُ اللَّهِ إِلَيْكُمْ جَمِيعًا',
    'Say: O mankind, I am the Messenger of Allah to you all.',
    'سُورَةُ الأَعْرَاف · 7:158')
b += B.ayah(
    'وَمَا أَرْسَلْنَاكَ إِلَّا كَافَّةً لِّلنَّاسِ بَشِيرًا وَنَذِيرًا',
    'And We have not sent you except to all of mankind, as a bringer of good '
    'tidings and a warner.',
    'سُورَةُ سَبَأ · 34:28')
b += B.sharh(
    p('<em>«أَمَّا مُحَمَّدٌ ﷺ فَقَدْ بَعَثَهُ اللهُ لِلنَّاسِ عَامَّة: '
      'مِنَ الجِنِّ وَالإِنْس، وَالعَرَبِ وَالعَجَم، وَالذُّكُورِ '
      'وَالإِنَاث، وَالأَغْنِيَاءِ وَالفُقَرَاء، وَالحُكَّامِ '
      'وَالمَحْكُومِين؛ كُلُّهُمْ مَأْمُورُونَ بِاتِّبَاعِ مُحَمَّدٍ ﷺ، '
      'وَكُلُّهُمْ مَأْمُورُونَ بِإِخْلَاصِ العِبَادَةِ لِلهِ '
      'وَحْدَه.»</em>') +
    p('<strong>So there is no one left over the edge of this message to whom a '
      'private path could run.</strong> <em>The universality is exactly what '
      'forecloses the claim: if the Messenger ﷺ was sent to «all mankind», '
      'then «some people are outside his sharīʿah» is not a lesser error — it '
      'is a denial of the verse.</em> «فَمَنْ خَرَجَ عَنْ طَرِيقَةِ مُحَمَّدٍ '
      'وَعَنْ شَرِيعَتِهِ فَقَدْ كَفَرَ بِاللهِ وَضَلَّ عَنْ سَوَاءِ '
      'السَّبِيل.»'))

# ----------------------------------------------- awliyāʾ vs anbiyāʾ
b += B.heading('الأَوْلِيَاءُ دُونَ الأَنْبِيَاء', 'The Saints Are Below the Prophets, Never Above')
b += B.sharh(
    p('<em>«وَالأَوْلِيَاءُ لَيْسُوا أَفْضَلَ مِنَ الأَنْبِيَاء، بَلِ '
      'الأَنْبِيَاءُ هُمْ أَفْضَلُ النَّاسِ وَهُمْ خَيْرُ النَّاس، ثُمَّ '
      'بَعْدَ ذَلِكَ طَبَقَاتُ المُؤْمِنِينَ عَلَى تَفَاوُتِهِم؛ فَمَنْ '
      'زَعَمَ أَنَّ الوَلِيَّ يَكُونُ أَفْضَلَ مِنَ النَّبِيِّ فَقَدْ '
      'ضَلَّ وَزَعَمَ قَوْلًا بَاطِلًا.»</em>') +
    box('<p style="margin:0;font-size:.95rem"><strong>And here is the sentence '
        'that turns the whole thing right-side up:</strong> the saints «إِنَّمَا '
        'كَانُوا مَحْمُودِينَ وَلَهُمُ الثَّوَابُ العَظِيمُ '
        '<strong>إِذَا كَانُوا مِنْ أَتْبَاعِ الأَنْبِيَاء</strong>؛ '
        'فَكَيْفَ يَكُونُونَ فَوْقَ الأَنْبِيَاء؟!»</p>',
        wash='var(--accent-wash)', edge='var(--accent)') +
    p('<strong>Read the logic, because it inverts the Sufi’s picture '
      'exactly.</strong> <em>Walāyah is not a ladder that rises past '
      'prophethood and out the top. It is constituted</em> by following — '
      '«فَإِنَّ فَضْلَهُمْ وَكَمَالَ إِيمَانِهِمْ أَنْ يَكُونُوا مُتَّبِعِينَ '
      'لِلْأَنْبِيَاء، سَائِرِينَ خَلْفَ الأَنْبِيَاء، لَيْسُوا خَارِجِينَ '
      'عَنِ الأَنْبِيَاء». <strong>The closer a believer’s following, the '
      'stronger his walāyah — so a «saint» who steps outside the sharīʿah has '
      'not risen above walāyah; he has destroyed the only thing it was ever '
      'made of.</strong>'))

# ----------------------------------------------- isqāṭ al-taklīf
b += B.heading('لَا يَسْقُطُ التَّكْلِيف', 'No Station Lifts the Obligation')
b += B.prose(
    '<strong>From the same root grows the claim the sharḥ spends its last '
    'folios on:</strong> that when a man reaches «المَعْرِفَةُ الكَامِلَة», '
    'complete gnosis, <em>taklīf drops from him</em> — he no longer prays, '
    'nor fasts, «وَلَا وَلَا وَلَا». Ibn Bāz: «هَذَا مِنَ الضَّلَالِ '
    'البَعِيد، وَالكُفْرِ الوَاضِح».')
b += B.sharh(
    p('<strong>His refutation is one clean line of reasoning, and it needs no '
      'ijmāʿ to carry it:</strong> <em>«بَلْ هُوَ لَا يَزَالُ مُكَلَّفًا '
      'مَأْمُورًا مَنْهِيًّا وَإِنْ كَانَ أَعْلَمَ النَّاس؛ '
      '<strong>فَالرُّسُلُ أَعْلَمُ النَّاسِ وَهُمْ مُكَلَّفُون، فَمَنْ '
      'دُونَهُمْ مِنْ بَابِ أَوْلَى</strong>.»</em>') +
    p('<em>If the highest knowledge there has ever been — the knowledge of the '
      'Messengers — did not lift the prayer from them, then no lesser '
      'knowledge lifts it from anyone.</em> The ʿabd «مَأْمُورٌ '
      'بِالاسْتِمْرَارِ فِي طَاعَةِ اللهِ حَتَّى يَجِيئَهُ المَوْتُ أَوْ '
      'يَذْهَبَ عَقْلُه» — <strong>there is no threshold of knowledge at which '
      'obligation ends.</strong>'))
b += B.ayah(
    'وَاعْبُدْ رَبَّكَ حَتَّىٰ يَأْتِيَكَ الْيَقِينُ',
    'And worship your Lord until there comes to you the certainty [i.e. '
    'death].',
    'سُورَةُ الحِجْر · 15:99')
b += B.prose(
    '<strong>«الْيَقِين» here is death</strong> — «يَعْنِي: حَتَّى يَأْتِيَ '
    'المَوْت». <em>Allah said it to His Prophet ﷺ himself, the most knowing '
    'and most honoured of creation. If worship ran «until certainty» for '
    'him, no servant reaches a certainty that excuses him from it.</em>')

# ----------------------------------------------- the heart is not maʿṣūm
b += B.heading('القَلْبُ غَيْرُ مَعْصُوم', 'The Heart Is Not Infallible')
b += B.sharh(
    qa('قَالَ بَعْضُهُم: حَدَّثَنِي قَلْبِي عَنْ رَبِّي، وَالمُتَّبِعُ '
       'يَقُول: عَنْ رَسُولِ اللهِ — فَمَا الفَرْق؟',
       '«هَذَا هُوَ الهَلَاك، وَهَذَا هُوَ الإِلْحَادُ وَالفَسَاد! '
       '<strong>وَهَلْ قَلْبُهُ مَعْصُوم؟!</strong> أَذْوَاقُهُ '
       'وَآرَاؤُهُ وَخَوَاطِرُه — يَخْطُرُ فِي قَلْبِهِ الشَّرُّ '
       'وَالخَيْر، وَيَخْطُرُ فِيهِ الفَسَادُ وَغَيْرُ الفَسَاد؛ '
       '<strong>فَالقَلْبُ غَيْرُ مَعْصُوم، وَإِنَّمَا المَعْصُومُ مَا '
       'ثَبَتَ عَنِ الرَّسُولِ ﷺ أَوْ جَاءَ بِهِ الكِتَاب</strong>.»') +
    p('<strong>That is the exact line the whole nullifier defends, and it is '
      'worth memorising as the answer to every «my heart told me» there will '
      'ever be.</strong> <em>The breast is not a protected source. Good and '
      'evil both pass through it. What is protected — maʿṣūm — is the Book and '
      'what is authentically established from the Messenger ﷺ, and nothing '
      'else.</em> «فَمَنْ جَعَلَ الطَّرِيقَ هَذَا: حَدَّثَنِي قَلْبِي عَنْ '
      'رَبِّي، أَوْ قَالَ شَيْخِي كَذَا — فَهَذَا قَدْ سَلَكَ طَرِيقَ '
      'الشَّيْطَان، وَلَمْ يَسْلُكْ طَرِيقَ الرَّحْمَن.»'))
b += B.sharh(
    qa('هَلْ يُصَلَّى خَلْفَهُم؟',
       '«مَنْ كَانَ بِهَذِهِ المَثَابَةِ <strong>لَا يُصَلَّى '
       'خَلْفَه؛ لَيْسَ بِمُسْلِم</strong>. مَنِ اسْتَغْنَى عَنِ '
       'الرَّسُولِ لَيْسَ بِمُسْلِم؛ مَنْ قَالَ: إِنَّهُ يَسْتَغْنِي عَنِ '
       'الرَّسُولِ بِأَذْوَاقِهِ وَآرَائِهِ وَمَا يَقَعُ فِي قَلْبِهِ '
       'فَهُوَ خَارِجٌ مِنَ الشَّرِيعَة، غَيْرُ مُسْلِم.»'))

# ----------------------------------------------- the footnote's application
b += B.heading('تَطْبِيقٌ مُعَاصِر', 'A Living Application')
b += B.prose(
    '<strong>The compiler closes the clause by pointing it at his own '
    'day — and not at the Sufis this time.</strong>')
b += B.sharh(
    box('<p style="margin:0;font-size:.94rem"><em>«This nullifier is fallen '
        'into by <strong>some writers who claim the People of the Book are '
        'not obliged to follow the sharīʿah of Muḥammad ﷺ</strong>, taking as '
        'their pretext that their acknowledgement of paying the jizyah and '
        'their submission exempts them from the obligation of entering '
        'Islām — <strong>وَهَذَا ضَلَالٌ مُبِين</strong>; their being left '
        'upon the jizyah is no evidence that they are upon the '
        'truth.»</em></p>') +
    p('<strong>See how the clause has turned.</strong> <em>It opened on a man '
      'claiming to stand </em>above<em> the sharīʿah by a secret knowledge; '
      'it closes on men leaving a whole community </em>outside<em> it by a '
      'legal excuse. Both are the same nullifier, because both deny the one '
      'thing it exists to protect: that the sharīʿah of Muḥammad ﷺ reaches '
      '</em>everyone<em>, with no one standing over it and no one left out '
      'from under it.</em>'))

# ----------------------------------------------- vocab, quiz, memorize
b += B.vocab([
    ('شَرِيعَة', 'sharīʿah', 'the revealed law',
     'The whole of what Allah legislated through His Messenger ﷺ. The clause '
     'is about claiming entitlement to stand outside it.'),
    ('الخَضِر', 'al-Khiḍr', 'al-Khiḍr',
     'The figure of Sūrat al-Kahf. Ibn Bāz: «نَبِيٌّ مُسْتَقِلّ» — an '
     'independent prophet, never under Mūsā’s sharīʿah, so no precedent here '
     'at all.'),
    ('كَافَّة', 'kāffah', 'to all, without exception',
     'Sabaʾ 34:28. The word that forecloses the clause: the Messenger ﷺ was '
     'sent to all mankind, so none stands outside his message.'),
    ('العِلْمُ اللَّدُنِّيّ', 'al-ʿilm al-ladunnī', 'knowledge direct from Allah',
     'The deviant claim: a knowledge received «مِنْ طَرِيقِ القَلْب», '
     'bypassing the prophets. «حَدَّثَنِي قَلْبِي عَنْ رَبِّي».'),
    ('مَعْصُوم', 'maʿṣūm', 'protected from error',
     'Ibn Bāz: the heart is NOT this. Only the Book and the authentic Sunnah '
     'are «المَعْصُوم».'),
    ('إِسْقَاطُ التَّكْلِيف', 'isqāṭ al-taklīf', 'dropping of obligation',
     'The claim that gnosis lifts worship. Kufr — the Messengers were the '
     'most knowing of people and remained mukallaf.'),
    ('الزَّنْدَقَة', 'al-zandaqah', 'heresy / crypto-disbelief',
     'What Ibn Bāz names the claim of independence from the Messenger ﷺ: '
     '«ضَلَالٌ وَزَنْدَقَةٌ وَكُفْرٌ وَإِلْحَاد».'),
    ('الاسْتِغْنَاءُ عَنِ الرَّسُول', 'al-istighnāʾ ʿan al-rasūl',
     'dispensing with the Messenger',
     'The core of the nullifier. «مَنِ اسْتَغْنَى عَنِ الرَّسُولِ لَيْسَ '
     'بِمُسْلِم».'),
    ('نَبِيٌّ مُسْتَقِلّ', 'nabī mustaqill', 'an independent prophet',
     'What al-Khiḍr was — with his own revelation, unconnected to Mūsā. The '
     'fact that undoes the analogy at its root.'),
])

b += B.mcq('nq-l16-mcq', QS)

b += B.tf('nq-l16-tf', [
    ('مَنِ اعْتَقَدَ أَنَّهُ يَسَعُهُ الخُرُوجُ عَنْ شَرِيعَةِ مُحَمَّدٍ ﷺ '
     'فَهُوَ كَافِرٌ بِإِجْمَاعِ أَهْلِ العِلْم.',
     'Whoever believes he may stand outside the sharīʿah of Muḥammad ﷺ is a '
     'disbeliever by the consensus of the people of knowledge.', True),
    ('كَانَ الخَضِرُ مِنْ بَنِي إِسْرَائِيلَ وَتَحْتَ شَرِيعَةِ مُوسَى.',
     'al-Khiḍr was of Banū Isrāʾīl and under the sharīʿah of Mūsā.', False),
    ('بُعِثَ مُحَمَّدٌ ﷺ إِلَى النَّاسِ كَافَّة: جِنِّهِمْ وَإِنْسِهِمْ، '
     'عَرَبِهِمْ وَعَجَمِهِم.',
     'Muḥammad ﷺ was sent to all people — their jinn and mankind, Arab and '
     'non-Arab.', True),
    ('قَدْ يَكُونُ الوَلِيُّ أَفْضَلَ مِنَ النَّبِيِّ إِذَا كَمُلَتْ '
     'مَعْرِفَتُه.',
     'A saint may be superior to a prophet once his gnosis is complete.',
     False),
    ('إِذَا بَلَغَ العَبْدُ المَعْرِفَةَ الكَامِلَةَ سَقَطَ عَنْهُ '
     'التَّكْلِيف.',
     'When a servant attains complete gnosis, obligation drops from him.',
     False),
    ('القَلْبُ غَيْرُ مَعْصُوم، وَإِنَّمَا المَعْصُومُ الكِتَابُ وَمَا '
     'ثَبَتَ عَنِ الرَّسُولِ ﷺ.',
     'The heart is not infallible; only the Book and what is established from '
     'the Messenger ﷺ are protected.', True),
    ('مَنِ اسْتَغْنَى عَنِ الرَّسُولِ ﷺ بِأَذْوَاقِهِ وَآرَائِهِ يُصَلَّى '
     'خَلْفَه.',
     'Prayer is prayed behind one who dispenses with the Messenger ﷺ by his '
     'tastes and opinions.', False),
])

b += B.memorize(
    'فَالقَلْبُ غَيْرُ مَعْصُوم، وَإِنَّمَا المَعْصُومُ مَا ثَبَتَ عَنِ '
    'الرَّسُولِ ﷺ أَوْ جَاءَ بِهِ الكِتَاب',
    'Ibn Bāz. <strong>This one sentence is the answer to every «my heart told '
    'me» and every «my shaykh said» there will ever be.</strong> <em>The '
    'breast is not a protected source — «يَخْطُرُ فِي قَلْبِهِ الشَّرُّ '
    'وَالخَيْر». What is protected is the Book and the authentic Sunnah, and '
    'nothing besides.</em> <strong>And keep beside it why the whole clause '
    'stands: the Messenger ﷺ was sent «كَافَّةً لِلنَّاس» — so no one rises '
    'above his sharīʿah, and no one is left outside it.</strong> <em>The very '
    'story the deviant cites, al-Khiḍr’s, refutes him: al-Khiḍr had waḥy; the '
    'claimant has a feeling.</em>')

b += B.nav('nq-l15-al-istianah-wa-al-jasus.html',
           'النَّاقِضُ الثَّامِن · part 2',
           'u6-nawaqid.html', 'Back to the Nawāqiḍ overview', 'nq-l16')

B.write('nq-l16-al-khuruj-an-al-shariah.html',
        'النَّاقِضُ التَّاسِع · الخُرُوجُ عَنِ الشَّرِيعَة',
        'The Ninth Nullifier — Claiming to Stand Outside the Sharīʿah',
        'The ninth nullifier, from the words of Shaykh Ibn Bāz: believing one '
        'may stand outside the sharīʿah of Muḥammad ﷺ as al-Khiḍr stood '
        'outside that of Mūsā — and why the al-Khiḍr story is no precedent, '
        'al-Khiḍr being an independent prophet with his own revelation; the '
        'universality of the Prophet’s ﷺ message on al-Aʿrāf 7:158 and Sabaʾ '
        '34:28; that the saints are never above the prophets and that walāyah '
        'consists in following them; the refutation of isqāṭ al-taklīf from '
        'al-Ḥijr 15:99 and the state of the Messengers; that the heart is not '
        'maʿṣūm but only the Book and the authentic Sunnah; the ruling on '
        'praying behind such a person; and the footnote’s application to those '
        'who hold the People of the Book need not follow Muḥammad ﷺ.',
        'نَوَاقِضُ الإِسْلَام · الدَّرْسُ السَّادِسَ عَشَر', '6', b)
print('wrote nq-l16-al-khuruj-an-al-shariah.html')
