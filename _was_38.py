# -*- coding: utf-8 -*-
"""Wasitiyyah L38 -- Part 4: the registers of deeds spread open, and the
Reckoning -- of the believer and of the disbelievers. Sharh pp.133-135."""
import io, os, importlib.util

spec = importlib.util.spec_from_file_location('qb', os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '_mutunbuild.py'))
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
B.set_source(os.path.join(B.AQ, 'was-l01-basmalah.html'))
B.FOOT = ('al-ʿAqīdah al-Wāsiṭiyyah of Shaykh al-Islām Ibn Taymiyyah '
          '· sharḥ of Shaykh Ṣāliḥ al-Fawzān · in our own words')
B.READING = [
    'Shaykh <strong>صَالِحٌ الفَوْزَان</strong>, <em>شَرْحُ العَقِيدَةِ الوَاسِطِيَّة</em> '
    '(Riyadh, Presidency of Scholarly Research &amp; Iftāʾ) — the sharḥ this track follows.',
    'The aḥādīth of the private reckoning and of the ʿarḍ are <strong>فِي الصَّحِيحَيْن</strong> '
    '— from <strong>ابْنِ عُمَر</strong> and <strong>عَائِشَة</strong> رضي الله عنهم.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Say why the registers are described as being <em>spread open</em>, and when.',
    'Reconcile the two descriptions of how the disbeliever takes his record.',
    'Define %s as al-Fawzān defines it, and distinguish %s from %s.'
    % (ar('الحِسَاب'), ar('العَرْض'), ar('المُنَاقَشَة')),
    'Explain in what sense the disbelievers are reckoned with, given that they have no good deeds.',
])

b += B.heading('٤ · وَتُنْشَرُ الدَّوَاوِين', 'Fourth — And the Registers Are Spread Open')
b += B.matn(
    'وَتُنْشَرُ الدَّوَاوِينُ — وَهِيَ صَحَائِفُ الأَعْمَالِ — فَآخِذٌ كِتَابَهُ '
    'بِيَمِينِهِ، وَآخِذٌ كِتَابَهُ بِشِمَالِهِ أَوْ مِنْ وَرَاءِ ظَهْرِهِ، كَمَا قَالَ '
    'سُبْحَانَهُ وَتَعَالَى: ﴿وَكُلَّ إِنْسَانٍ أَلْزَمْنَاهُ طَائِرَهُ فِي عُنُقِهِ '
    'وَنُخْرِجُ لَهُ يَوْمَ الْقِيَامَةِ كِتَابًا يَلْقَاهُ مَنْشُورًا ۝ اقْرَأْ '
    'كِتَابَكَ كَفَى بِنَفْسِكَ الْيَوْمَ عَلَيْكَ حَسِيبًا﴾.')
b += B.sharh(
    p('<strong>%s</strong> — <em>that is: <strong>the pages in which the deeds of the servants '
      'were written — the deeds they did in this world, which the recording angels wrote against '
      'them</strong>.</em>' % ar('الدَّوَاوِين')) +
    p('And al-Fawzān explains the verb, which is doing real work: '
      '<em><strong>because they are folded up at death, and spread open</strong> — that is, '
      '<strong>at the Reckoning — so that every human being may stand upon his own page and know '
      'what is in it.</strong></em>') +
    p('So the word <em>nashr</em> carries a whole sequence: <strong>written during the life, '
      'closed at the death, opened at the Reckoning.</strong> Nothing is being compiled on the '
      'Day; <strong>the record was complete before the man was buried.</strong>'))
b += B.ayah(
    'وَكُلَّ إِنْسَانٍ أَلْزَمْنَاهُ طَائِرَهُ فِي عُنُقِهِ وَنُخْرِجُ لَهُ يَوْمَ '
    'الْقِيَامَةِ كِتَابًا يَلْقَاهُ مَنْشُورًا اقْرَأْ كِتَابَكَ كَفَى بِنَفْسِكَ '
    'الْيَوْمَ عَلَيْكَ حَسِيبًا',
    '"And every man — We have fastened his record to his neck; and We shall bring out for him, on '
    'the Day of Rising, a book which he will find spread open. Read your book! You suffice today '
    'as a reckoner against yourself."',
    'Sūrat al-Isrāʾ 17:13–14 · سُورَةُ الإِسْرَاء')
b += B.sharh(
    p('<strong>%s</strong> — <em>is <strong>what flew off from him of his deed, of good and of '
      'evil</strong></em>. <strong>%s</strong> — <em>that is: <strong>he is bound to it and '
      'recompensed by it; there is no turning away from it for him</strong> — '
      '<strong>so it clings to him as a necklace clings to the neck.</strong></em>'
      % (ar('طَائِرَه'), ar('فِي عُنُقِهِ'))) +
    p('<strong>%s</strong> — <em>that is: <strong>we gather for him his whole deed in a book he is '
      'given on the Day of Rising</strong> — either in his right hand if he is of the happy, or '
      'in his left if he is of the wretched.</em> <strong>%s</strong> — <em>that is: '
      '<strong>opened</strong>; <strong>he reads it and so does someone else.</strong></em>'
      % (ar('وَنُخْرِجُ لَهُ يَوْمَ الْقِيَامَةِ كِتَابًا'), ar('مَنْشُورًا'))) +
    p('And why <em>spread open</em> rather than merely handed over? al-Fawzān: <em>and He said '
      '%s only <strong>to intensify the glad tidings at the good deed, and the rebuke at the evil '
      'one.</strong></em> <strong>A sealed record would spare its owner the worst part of '
      'it.</strong>' % ar('يَلْقَاهُ مَنْشُورًا')) +
    p('<strong>%s</strong> — <em>that is: <strong>we say that to him</strong></em>; and note '
      'whom it is said to: <em><strong>before he reads that book — both the one who was a reader '
      'and the one who was not.</strong></em> <strong>The illiterate man reads his own record on '
      'that Day.</strong>' % ar('اقْرَأْ كِتَابَكَ')) +
    p('<strong>%s</strong> — <em>that is: <strong>as a reckoner</strong>; and it is manṣūb as '
      '%s</em>. <em>And <strong>this is the utmost of justice</strong>, in that '
      '<strong>He made him the reckoner of his own self, so that he might see all of his '
      'deeds</strong></em> — <strong>and the shāhid of the āyah is that every human being is given '
      'the page of his deed on the Day of Rising, which he reads himself and comes to know '
      'himself, not by means of anyone else.</strong>'
      % (ar('حَسِيبًا'), ar('التَّمْيِيز'))))
b += B.sharh(
    p('And on the two ways of taking the record, al-Fawzān resolves what looks like a conflict '
      'between the āyāt: <em>this explains <strong>the manner of the people\'s taking of their '
      'pages</strong>, and it is <strong>of two kinds</strong>: '
      '<strong>one who takes his book in his right hand — and he is the believer</strong>; and '
      '<strong>one who takes his book in his left hand, or from behind his back — and he is the '
      'disbeliever.</strong></em>') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.94rem"><em>— <strong>and there is no conflict between the '
    'two</strong>, because <strong>the disbeliever’s right hand is shackled to his neck and '
    'his left is put behind his back, so he takes his book with it</strong> — by his left '
    'hand being twisted round from behind his back and his book given to him in it, '
    '<strong>as the āyāt came with this and with that.</strong></em></p></div>' +
    p('One posture, described from two angles. <strong>The two sets of āyāt were reporting the '
      'same thing and there was nothing to choose between them</strong> — the resolution being, '
      'again, that the texts were never in competition.'))

b += B.heading('٥ · وَيُحَاسِبُ اللهُ الخَلَائِق', 'Fifth — And Allah Reckons with the Creation')
b += B.matn(
    'وَيُحَاسِبُ اللهُ الخَلَائِقَ، وَيَخْلُو بِعَبْدِهِ المُؤْمِنِ فَيُقَرِّرُهُ '
    'بِذُنُوبِهِ، كَمَا وُصِفَ ذَلِكَ فِي الكِتَابِ وَالسُّنَّةِ. وَأَمَّا الكُفَّارُ '
    'فَلَا يُحَاسَبُونَ مُحَاسَبَةَ مَنْ تُوزَنُ حَسَنَاتُهُ وَسَيِّئَاتُهُ، فَإِنَّهُ لَا '
    'حَسَنَاتِ لَهُمْ؛ وَلَكِنْ تُعَدُّ أَعْمَالُهُمْ فَتُحْصَى، فَيُوقَفُونَ عَلَيْهَا '
    'وَيُقَرَّرُونَ بِهَا وَيُجْزَوْنَ بِهَا.')
b += B.sharh(
    p('<strong>%s</strong> — and al-Fawzān gives the definition twice, which is worth having both '
      'times: <em>al-ḥisāb is <strong>Allah\'s acquainting the creation with the measures of the '
      'recompense for their deeds, and His reminding them of what they had forgotten of '
      'that</strong>; or in another expression: <strong>Allah\'s halting His servants, before '
      'their departure from the place of gathering, upon their deeds — whether they were good or '
      'evil.</strong></em>' % ar('الحِسَاب')) +
    p('Note what the first definition says about the purpose. <strong>It is not an investigation; '
      'it is an informing.</strong> Allah is not finding out what was done — '
      '<em>He is acquainting the servant with it,</em> and reminding him of what he had himself '
      'forgotten. Which is why the record must be read by its owner.') +
    p('<em>Then the Shaykh mentioned that <strong>the Reckoning is of two kinds.</strong></em>'))
b += B.heading('النَّوْعُ الأَوَّل · حِسَابُ المُؤْمِن',
               'The First Kind — the Reckoning of the Believer')
b += B.sharh(
    p('The author\'s words: <strong>%s</strong> — '
      '<em>as Allah تعالى said:</em>'
      % ar('وَيَخْلُو بِعَبْدِهِ المُؤْمِنِ فَيُقَرِّرُهُ بِذُنُوبِهِ')))
b += B.ayah(
    'فَأَمَّا مَنْ أُوتِيَ كِتَابَهُ بِيَمِينِهِ فَسَوْفَ يُحَاسَبُ حِسَابًا يَسِيرًا',
    '"So as for him who is given his record in his right hand, he will be reckoned with an easy '
    'reckoning."',
    'Sūrat al-Inshiqāq 84:7–8 · سُورَةُ الانْشِقَاق')
b += B.hadith(
    'إِنَّ اللهَ يُدْنِي المُؤْمِنَ فَيَضَعُ عَلَيْهِ كَنَفَهُ وَيَسْتُرُهُ مِنَ النَّاسِ، '
    'وَيُقَرِّرُهُ بِذُنُوبِهِ فَيَقُولُ لَهُ: أَتَعْرِفُ ذَنْبَ كَذَا؟ أَتَعْرِفُ ذَنْبَ '
    'كَذَا؟ حَتَّى إِذَا قَرَّرَهُ بِذُنُوبِهِ وَرَأَى فِي نَفْسِهِ أَنْ قَدْ هَلَكَ، '
    'قَالَ: فَإِنِّي قَدْ سَتَرْتُهَا عَلَيْكَ فِي الدُّنْيَا، وَأَنَا أَغْفِرُهَا لَكَ '
    'اليَوْمَ. ثُمَّ يُعْطَى كِتَابَ حَسَنَاتِهِ',
    '"Allah brings the believer near and places His covering over him and screens him from the '
    'people, and makes him acknowledge his sins, saying: do you know of such a sin? Do you know '
    'of such a sin? Until, when He has made him acknowledge his sins and he sees within himself '
    'that he is ruined, He says: I concealed them for you in the world, and I forgive them for '
    'you today. Then he is given the record of his good deeds."',
    'فِي الصَّحِيحَيْنِ — al-Bukhārī and Muslim, from Ibn ʿUmar رضي الله عنهما')
b += B.sharh(
    p('<em>And the meaning of <strong>%s</strong> is <strong>that He makes him '
      'acknowledge them</strong> — that is, <strong>confess them</strong></em>, as in this '
      'ḥadīth.' % ar('يُقَرِّرُهُ بِذُنُوبِهِ')) +
    p('Read the shape of it, because the whole mercy of the ḥadīth is in the <em>order</em>. '
      '<strong>The screening comes first</strong> — before a single sin is named, he is brought '
      'near and covered from the people. <strong>Then he is made to see the full account</strong>, '
      'to the point of believing himself destroyed. <strong>And only then is he forgiven.</strong>') +
    p('He is not spared the knowledge of what he did; <strong>he is spared the exposure of '
      'it</strong>, and then the consequence. And the reason given is the thing to carry out of '
      'the lesson: <em>I concealed them for you <strong>in the world</strong></em> — '
      '<strong>the covering on that Day is the continuation of a covering that was already '
      'happening, unnoticed, for a lifetime.</strong>') +
    p('<em>And <strong>of the believers there are those who enter the Garden without a '
      'reckoning</strong> — as is authentic in the ḥadīth of <strong>the seventy '
      'thousand</strong> who enter the Garden <strong>without reckoning and without '
      'punishment.</strong></em>'))
b += B.heading('العَرْضُ وَالمُنَاقَشَة', 'The Presentation, and the Interrogation')
b += B.sharh(
    p('<em>And <strong>the Reckoning differs</strong>: <strong>of it is the easy, and that is '
      '%s — the presentation; and of it is %s — the interrogation.</strong></em> And the '
      'distinction is not al-Fawzān\'s own — it is ʿĀʾishah\'s question and the Prophet\'s '
      '&#65018; answer:' % (ar('العَرْض'), ar('المُنَاقَشَة'))) +
    p('<em>In the two Ṣaḥīḥs, from ʿĀʾishah رضي الله عنها, that the Messenger of Allah &#65018; '
      'said: <strong>«no one is reckoned with on the Day of Rising but he is ruined»</strong>. '
      'She said: O Messenger of Allah, <strong>did Allah تعالى not say %s?</strong> So the '
      'Messenger of Allah &#65018; said:</em>'
      % ar('فَأَمَّا مَنْ أُوتِيَ كِتَابَهُ بِيَمِينِهِ فَسَوْفَ يُحَاسَبُ حِسَابًا يَسِيرًا')) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.96rem" dir="rtl" lang="ar"><strong>إِنَّمَا ذَلِكَ '
    'العَرْضُ؛ وَلَيْسَ أَحَدٌ يُنَاقَشُ الحِسَابَ يَوْمَ القِيَامَةِ إِلَّا '
    'عُذِّبَ</strong></p>'
    '<p style="margin:.55rem 0 0;font-size:.9rem"><em>— <strong>that is only the '
    'presentation. And no one is interrogated in the Reckoning on the Day of Rising but he is '
    'punished.</strong></em> — فِي '
    'الصَّحِيحَيْنِ</p></div>' +
    p('That exchange is a model of how an apparent conflict between two texts is settled, and the '
      'student should notice who settles it. <strong>ʿĀʾishah heard a ḥadīth, found an āyah that '
      'seemed to contradict it, and asked.</strong> The answer distinguishes two things the one '
      'word <em>ḥisāb</em> was covering — <strong>the <em>easy</em> reckoning of the āyah is a '
      'presentation, and the ruinous reckoning of the ḥadīth is an interrogation.</strong> '
      '<em>Al-ḥaqqu lā yatanāqaḍ</em>, demonstrated in a conversation.'))
b += B.heading('النَّوْعُ الثَّانِي · حِسَابُ الكُفَّار',
               'The Second Kind — the Reckoning of the Disbelievers')
b += B.sharh(
    p('<em>The author explained it with his words: <strong>%s</strong> — '
      'that is: <strong>they have no good deeds to be weighed against their evil deeds, '
      '<em>because their deeds were nullified by the disbelief</em>, so there remains for them in '
      'the Hereafter nothing but evil deeds.</strong></em>'
      % ar('وَأَمَّا الكُفَّارُ فَلَا يُحَاسَبُونَ مُحَاسَبَةَ مَنْ تُوزَنُ حَسَنَاتُهُ وَسَيِّئَاتُهُ، فَإِنَّهُ لَا حَسَنَاتِ لَهُمْ')) +
    p('<em>So <strong>their reckoning means</strong> that <strong>%s</strong> — that is: '
      '<strong>they are informed of their deeds of disbelief, and they acknowledge them, and then '
      'they are recompensed for them.</strong></em>'
      % ar('تُعَدُّ أَعْمَالُهُمْ فَتُحْصَى، فَيُوقَفُونَ عَلَيْهَا وَيُقَرَّرُونَ بِهَا وَيُجْزَوْنَ بِهَا')) +
    p('So the word <em>reckoning</em> is being used in two senses, and the author is careful to '
      'say so. <strong>For the believer it is a weighing, with an outcome in doubt.</strong> '
      '<strong>For the disbeliever there is nothing to weigh</strong> — only an enumeration, an '
      'acknowledgement and a recompense. <strong>The scales are not used where there is nothing '
      'in one pan.</strong>') +
    p('And al-Fawzān brings three āyāt for the enumeration and the acknowledgement:'))
b += B.ayah(
    'فَلَنُنَبِّئَنَّ الَّذِينَ كَفَرُوا بِمَا عَمِلُوا وَلَنُذِيقَنَّهُمْ مِنْ عَذَابٍ '
    'غَلِيظٍ',
    '"We shall surely inform those who disbelieved of what they did, and We shall surely make '
    'them taste a harsh punishment."',
    'Sūrat Fuṣṣilat 41:50 · سُورَةُ فُصِّلَت')
b += B.ayah(
    'وَشَهِدُوا عَلَى أَنْفُسِهِمْ أَنَّهُمْ كَانُوا كَافِرِينَ',
    '"And they will bear witness against themselves that they were disbelievers."',
    'Sūrat al-Aʿrāf 7:37 · سُورَةُ الأَعْرَاف')
b += B.ayah(
    'فَاعْتَرَفُوا بِذَنْبِهِمْ فَسُحْقًا لِأَصْحَابِ السَّعِيرِ',
    '"So they will acknowledge their sin — then away with the companions of the Blaze!"',
    'Sūrat al-Mulk 67:11 · سُورَةُ المُلْك')
b += B.prose(
    'Notice that in all three the disbelievers <strong>testify against themselves</strong>. '
    'Nobody needs to be convinced of anything; the record is read, and they confirm it. '
    '<strong>Which is the same justice as %s in the āyah of al-Isrāʾ above</strong> — the man is '
    'made the witness in his own case, and in neither case does he dispute the evidence.'
    % ar('كَفَى بِنَفْسِكَ الْيَوْمَ عَلَيْكَ حَسِيبًا'))

b += B.vocab([
    ('الدَّوَاوِين', 'al-dawāwīn', 'the registers',
     'The pages of deeds — folded at death, spread open at the Reckoning'),
    ('طَائِرَه', 'ṭāʾirah', 'his record',
     'What flew off from him of his deed, good and evil — clinging like a necklace'),
    ('مَنْشُورًا', 'manshūran', 'spread open',
     'To intensify the glad tidings at the good and the rebuke at the evil'),
    ('حَسِيبًا', 'ḥasīban', 'a reckoner',
     'Manṣūb as tamyīz — and the utmost of justice: he reckons with himself'),
    ('الحِسَاب', 'al-ḥisāb', 'the Reckoning',
     'Allah’s acquainting them with the measures of the recompense, and reminding them of '
     'what they forgot'),
    ('العَرْض', 'al-ʿarḍ', 'the presentation',
     'The easy reckoning of al-Inshiqāq 84:8 — per the Prophet ط himself'),
    ('المُنَاقَشَة', 'al-munāqashah', 'the interrogation',
     'And no one is interrogated in the Reckoning but he is punished'),
    ('يُقَرِّرُهُ بِذُنُوبِه', 'yuqarriruhu bi-dhunūbih',
     'makes him acknowledge his sins',
     'That is: makes him confess them'),
])
b += B.mcq('ws-l38', [
    ('What does the word %s convey about the registers?' % ar('تُنْشَر'),
     ['That they are written on the Day itself',
      'That they were folded at death and are opened at the Reckoning — so the record was '
      'complete before burial',
      'That they are published to all creation',
      'That they are read aloud by the angels'], 1),
    ('Why does the āyah say the book is found %s?' % ar('مَنْشُورًا'),
     ['Because the angels cannot fold it',
      'To intensify the glad tidings at the good deed and the rebuke at the evil one — a sealed '
      'record would spare its owner the worst of it',
      'Because it is too long to fold',
      'To show that others may not read it'], 1),
    ('Who is told %s?' % ar('اقْرَأْ كِتَابَكَ'),
     ['Only those who were literate in this world',
      'Both the one who was a reader and the one who was not — the illiterate man reads his own '
      'record that Day',
      'Only the believers', 'The angels, on his behalf'], 1),
    ('How is the apparent conflict over the left hand and behind the back resolved?',
     ['One describes the believer and the other the hypocrite',
      'The disbeliever’s right hand is shackled to his neck and his left put behind his '
      'back, so he takes it with that — one posture described from two angles',
      'The narrations differ and one is preferred',
      'It refers to two different groups of disbelievers'], 1),
    ('What is al-Fawzān’s first definition of %s?' % ar('الحِسَاب'),
     ['Allah’s investigation of what the servant did',
      'Allah’s acquainting the creation with the measures of the recompense for their deeds, '
      'and reminding them of what they had forgotten',
      'The weighing of deeds on the Scales',
      'The questioning of the two angels'], 1),
    ('What is the order of events in the believer’s private reckoning?',
     ['He is shown his good deeds, then his sins, then forgiven',
      'He is brought near and screened from the people FIRST, then made to acknowledge his sins '
      'until he believes himself ruined, and only then forgiven',
      'He confesses, then is punished, then forgiven',
      'He is forgiven first, then shown the record'], 1),
    ('How did the Prophet ﷺ settle ʿĀʾishah’s question?',
     ['By saying the āyah concerns the prophets only',
      'By distinguishing two things the one word ḥisāb covered — the easy reckoning of the āyah '
      'is the ʿarḍ, while no one interrogated in the Reckoning escapes punishment',
      'By saying the ḥadīth was abrogated',
      'By saying the reckoning differs by nation'], 1),
    ('In what sense are the disbelievers reckoned with?',
     ['Their good deeds are weighed but found light',
      'There is nothing to weigh, since their deeds were nullified by disbelief — so their deeds '
      'are enumerated, they are halted upon them, they acknowledge them and are recompensed',
      'They are not reckoned with at all',
      'They are reckoned with by their nations rather than individually'], 1),
])
b += B.tf('ws-l38-tf', [
    ('صَحَائِفُ الأَعْمَالِ تُطْوَى عِنْدَ المَوْتِ وَتُنْشَرُ عِنْدَ الحِسَابِ.',
     'The pages of deeds are folded at death and spread open at the Reckoning.', True),
    ('يَقْرَأُ كِتَابَهُ مَنْ كَانَ قَارِئًا فِي الدُّنْيَا فَقَطْ.',
     'Only one who was literate in this world reads his record.', False),
    ('الحِسَابُ اليَسِيرُ هُوَ العَرْضُ.', 'The easy reckoning is the ʿarḍ.', True),
    ('لِلْكُفَّارِ حَسَنَاتٌ تُوزَنُ مَعَ سَيِّئَاتِهِمْ.',
     'The disbelievers have good deeds that are weighed against their evil deeds.', False),
])
b += B.memorize(
    'فَإِنِّي قَدْ سَتَرْتُهَا عَلَيْكَ فِي الدُّنْيَا، وَأَنَا أَغْفِرُهَا لَكَ اليَوْمَ',
    'The end of the believer\'s private reckoning, after he has seen the whole account and given '
    'himself up for lost. Note the reason He gives: <em>I concealed them for you in the world.</em> '
    'The covering on that Day is the continuation of a covering that has been going on, unnoticed, '
    'for your whole life.')
b += B.aiquiz('The registers and the Reckoning in al-Aqidah al-Wasitiyyah: why tunshar implies '
              'the record was complete before burial, tairah as what flew off from his deed '
              'clinging like a necklace, why the book is found manshuran, that the illiterate man '
              'reads his own record, how the left hand and behind the back are one posture, '
              'al-hisab as an acquainting rather than an investigation, the ORDER of the '
              'believers private reckoning with the screening first, Aishahs question settled by '
              'distinguishing the ard from the munaqashah, and why there is nothing to weigh for '
              'the disbelievers')
b += B.further()
b += B.nav('was-l37-qiyamah-kubra.html', 'The Greater Resurrection and the Scales',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l38')

io.open(os.path.join(B.AQ, 'was-l38-dawawin-hisab.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'نَشْرُ الدَّوَاوِينِ وَالحِسَاب',
    'The Registers Spread Open, and the Reckoning',
    'Lesson 38 of al-ʿAqīdah al-Wāsiṭiyyah: the record written in '
    'life, folded at death and opened at the Reckoning; why it is found spread open; the order of '
    'the believer’s private reckoning, in which the screening comes first; and '
    'ʿĀʾishah’s question settled by distinguishing the presentation from the '
    'interrogation.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الثَّامِنُ وَالثَّلَاثُون', '4',
           'نَشْرُ الدَّوَاوِينِ وَالحِسَاب',
           'The Registers Spread Open, and the Reckoning', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l38-dawawin-hisab.html')
