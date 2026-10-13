# -*- coding: utf-8 -*-
"""Wasitiyyah L21 -- section 23: the believers will see their Lord on the Day of
Rising. The four ayat, the three objections of the deniers with al-Fawzan's
answers, and the author's closing words that seal Part 1, the Qur'anic
evidence. Sharh pp.87-89."""
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
    '<strong>صَحِيحُ مُسْلِم</strong> — where the Prophet’s ﷺ own tafsīr of '
    '<span dir="rtl" lang="ar">وَزِيَادَةٌ</span> as the looking at the Face of Allah is '
    'established.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Distinguish %s from %s in al-Qiyāmah 75:22–23, and say what each contributes.'
    % (ar('نَاضِرَة'), ar('نَاظِرَة')),
    'Show how the veiling of the disbelievers in al-Muṭaffifīn is a proof for the believers’ seeing.',
    'Give the Prophet’s ﷺ own tafsīr of %s, and where it is established.' % ar('وَزِيَادَةٌ'),
    'Answer all three objections of those who deny the ruʾyah.',
])

b += B.heading('٢٣ · إِثْبَاتُ رُؤْيَةِ المُؤْمِنِينَ لِرَبِّهِمْ يَوْمَ القِيَامَة',
               'Section 23 — The Believers Will See Their Lord on the Day of Rising')
b += B.matn(
    'وَقَوْلُهُ: ﴿وُجُوهٌ يَوْمَئِذٍ نَاضِرَةٌ ۝ إِلَى رَبِّهَا نَاظِرَةٌ﴾، ﴿عَلَى '
    'الْأَرَائِكِ يَنْظُرُونَ﴾، ﴿لِلَّذِينَ أَحْسَنُوا الْحُسْنَى وَزِيَادَةٌ﴾، ﴿لَهُمْ '
    'مَا يَشَاءُونَ فِيهَا وَلَدَيْنَا مَزِيدٌ﴾. وَهَذَا البَابُ فِي كِتَابِ اللهِ '
    'كَثِيرٌ. وَمَنْ تَدَبَّرَ القُرْآنَ طَالِبًا لِلْهُدَى تَبَيَّنَ لَهُ طَرِيقُ الحَقِّ.')
b += B.ayah(
    'وُجُوهٌ يَوْمَئِذٍ نَاضِرَةٌ إِلَى رَبِّهَا نَاظِرَةٌ',
    '"Faces, on that Day, radiant — looking at their Lord."',
    'Sūrat al-Qiyāmah 75:22–23 · سورة القيامة')
b += B.sharh(
    p('<strong>%s</strong> — <em>the faces of <strong>the believers</strong></em>; '
      '<strong>%s</strong> — <em>the Day of Rising</em>.' % (ar('وُجُوهٌ'), ar('يَوْمَئِذٍ'))) +
    p('And now the point al-Fawzān is careful to flag, because the whole āyah turns on two '
      'letters. <strong>%s — with the ض</strong> — <em>is from %s, which is splendour and '
      'beauty</em>: <em>that is, soft, fresh, beautiful, luminous, shining.</em> And '
      '<strong>%s — with the ظ</strong> — is from looking.'
      % (ar('نَاضِرَة'), ar('النَّضَارَة'), ar('نَاظِرَة'))) +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.92rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.55rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>نَاضِرَة</strong> — بالضَّاد</td>'
    '<td style="padding:.55rem .8rem;border:1px solid var(--line)">from '
    '<span dir="rtl" lang="ar">النَّضَارَة</span>: radiant, fresh, shining — '
    '<strong>what the faces ARE</strong></td></tr>'
    '<tr><td style="padding:.55rem .8rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>نَاظِرَة</strong> — بالظَّاء</td>'
    '<td style="padding:.55rem .8rem;border:1px solid var(--line)">from looking — '
    '<strong>what the faces DO</strong></td></tr>'
    '</table></div>' +
    p('Two words a careless reader would run together, and the āyah uses both — in that order. '
      '<strong>The radiance comes first and the looking second, and the second is the cause of '
      'the first.</strong> This is also a lesson in why the ḥarakāt and the exact letters are '
      'not decoration: swap the ض for the ظ and you have lost half the āyah.') +
    p('<strong>%s</strong> — <em>their Creator</em> — <strong>%s</strong> — '
      '<em>they look at Him <strong>with their eyes</strong>.</em> And then the attestation, '
      'which al-Fawzān states in four stacked layers: <em>as the authentic aḥādīth have come '
      '<strong>mutawātir</strong> with it; and <strong>the Ṣaḥābah and the Tābiʿūn and the '
      'predecessors of this Ummah were agreed upon it</strong>; and <strong>the imāms of Islam '
      'concurred upon it</strong>.</em>' % (ar('إِلَى رَبِّهَا'), ar('نَاظِرَةٌ'))) +
    p('<strong>So the shāhid from the noble āyah: the affirming of the believers\' seeing of '
      'their Lord on the Day of Rising.</strong>'))
b += B.ayah(
    'عَلَى الْأَرَائِكِ يَنْظُرُونَ',
    '"Upon couches, looking."',
    'Sūrat al-Muṭaffifīn 83:23 · سورة المطففين')
b += B.sharh(
    p('<strong>%s</strong> is <em>the plural of %s, and it is the couches</em>; and '
      '<strong>%s</strong> — <em>at Allah عز وجل</em>.'
      % (ar('الْأَرَائِكِ'), ar('أَرِيكَة'), ar('يَنْظُرُونَ'))) +
    p('And al-Fawzān draws in the context, which is where the argument lies: <em>and as for the '
      'disbelievers, it has already come in the āyāt <strong>before this āyah</strong> that '
      'they are %s</em> — <strong>«veiled from their Lord on that Day»</strong> '
      '(al-Muṭaffifīn 83:15).'
      % ar('عَنْ رَبِّهِمْ يَوْمَئِذٍ لَمَحْجُوبُونَ')) +
    p('Sit with the structure of the sūrah for a moment, because it argues by contrast. A few '
      'āyāt apart, Allah describes <strong>the disbelievers as veiled from Him</strong> and '
      '<strong>the righteous as looking</strong>. Now: <em>being veiled is named as part of their '
      'punishment.</em> A veil is only a deprivation if there is something behind it to be seen — '
      '<strong>and the punishment of one party establishes the reward of the other.</strong> If '
      'nobody can see Him, then the disbelievers have been threatened with nothing.') +
    p('<strong>And the shāhid from the āyah: the affirming of the believers\' seeing of their '
      'Lord عز وجل.</strong>'))
b += B.ayah(
    'لِلَّذِينَ أَحْسَنُوا الْحُسْنَى وَزِيَادَةٌ',
    '"For those who did good is the best — and more."',
    'Sūrat Yūnus 10:26 · سورة يونس')
b += B.sharh(
    p('<strong>%s</strong> — <em>by undertaking what Allah obliged upon them of deeds, and '
      'holding back from what He forbade them of acts of disobedience.</em> Again the two halves: '
      '<em>doing and refraining.</em>' % ar('لِلَّذِينَ أَحْسَنُوا')) +
    p('<strong>%s</strong> — <em>the goodly recompense; and it has been said: the Garden.</em>'
      % ar('الْحُسْنَى')) +
    p('<strong>%s</strong> — and here is the decisive point: <em>it is '
      '<strong>the looking at the Noble Face of Allah</strong> — <strong>as its being explained '
      'with that is established from the Messenger of Allah &#65018; in '
      '«صَحِيحُ مُسْلِم» and elsewhere</strong>, and as the predecessors of this Ummah explained '
      'it with that.</em>' % ar('وَزِيَادَةٌ')) +
    p('Note the form of the proof. The āyah by itself says only «and more» — it does not say what '
      'the increase is. <strong>The content comes from the Prophet &#65018; himself, in a named '
      'collection.</strong> This is the standard the whole track works to: nobody is guessing at '
      '%s, and nobody needs to.' % ar('زِيَادَة')))
b += B.ayah(
    'لَهُمْ مَا يَشَاءُونَ فِيهَا وَلَدَيْنَا مَزِيدٌ',
    '"They will have whatever they wish for therein — and with Us is more."',
    'Sūrat Qāf 50:35 · سورة ق')
b += B.sharh(
    p('<strong>%s</strong> — <em>for the believers in the Garden is whatever their souls desire '
      'and their eyes delight in, of the varieties of bliss and the kinds of good.</em>'
      % ar('لَهُمْ مَا يَشَاءُونَ فِيهَا')) +
    p('<strong>%s</strong> — <em>an increase beyond that, and it is '
      '<strong>the looking at the Noble Face of Allah</strong>.</em>' % ar('وَلَدَيْنَا مَزِيدٌ')) +
    p('Read the two halves against each other and the whole doctrine of the section is in them. '
      'The first half is <em>everything they could wish for</em> — the ceiling of what a desire '
      'can reach. And then the āyah says: <strong>and there is more.</strong> Whatever that is, '
      'it is by definition something the soul would not have known to ask for.'))

b += B.heading('مَا يُسْتَفَادُ · وَأَعْظَمُ النَّعِيم', 'What the Āyāt Yield — the Greatest Bliss')
b += B.prose(
    '<em>What is derived from them is the affirming of the believers\' seeing of their Lord on the '
    'Day of Rising, and <strong>that it is the greatest of the bliss which they attain</strong>. '
    'And this is the statement of the Ṣaḥābah, the Tābiʿūn and the imāms of the Muslims — '
    '<strong>contrary to the Rāfiḍah, the Jahmiyyah and the Muʿtazilah</strong>, who negate the '
    'seeing and thereby oppose the Book, the Sunnah and the consensus of the predecessors of '
    'this Ummah and its imāms, <strong>relying upon flimsy objections and false '
    'reasonings</strong> — among them:</em>')

b += B.heading('الشُّبْهَةُ الأُولَى · لَوْ رُئِيَ لَكَانَ فِي جِهَة',
               'First Objection — To Be Seen Is to Be in a Direction')
b += B.sharh(
    p('<strong>Their statement:</strong> <em>affirming the seeing necessitates affirming that '
      'Allah is <strong>in a direction</strong>; and were He in a direction, '
      '<strong>He would be a body</strong> — and Allah is free of that.</em>') +
    p('<strong>The answer:</strong> <em>we say: <strong>the word %s is '
      'ambiguous</strong></em> — and the whole reply is in that single observation. '
      'al-Fawzān then splits it:' % ar('الجِهَة')) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .6rem">— <em>If what is intended by “direction” is that '
    '<strong>He is indwelling in something of His creation</strong>, then '
    '<strong>this is false</strong>, and the proofs reject it — <strong>and it does not '
    'follow from affirming the seeing.</strong></em></p>'
    '<p style="margin:0">— <em>And if what is intended by “direction” is that '
    'He سبحانه is <strong>above His creation</strong>, then '
    '<strong>this is established for Allah</strong> سبحانه and '
    '<strong>its negation is false</strong> — and it is <strong>not in conflict with His '
    'being seen</strong>.</em></p></div>' +
    p('This is the method of Lesson 6 applied to a word rather than to a text. The objection '
      'works only while %s is left vague enough to carry both a false meaning and a true one at '
      'once. <strong>Separate the two meanings and the argument has nothing left to stand '
      'on</strong>: the false sense was never entailed, and the true sense was never a problem.'
      % ar('الجِهَة')))

b += B.heading('الشُّبْهَةُ الثَّانِيَة · ﴿لَنْ تَرَانِي﴾', 'Second Objection — "You Shall Not See Me"')
b += B.sharh(
    p('<strong>They argued with His saying to Mūsā:</strong> <strong>%s</strong> — '
      '<em>you shall not see Me</em> (al-Aʿrāf 7:143).' % ar('لَنْ تَرَانِي')) +
    p('<strong>The answer:</strong> <em>the noble āyah has come regarding '
      '<strong>the negation of the seeing in this world</strong>, and '
      '<strong>it does not negate its being established in the Hereafter</strong>, as is '
      'established in the other proofs. <strong>And the state of people in the Hereafter differs '
      'from their state in this world.</strong></em>') +
    p('The distinction is not a convenience invented for the occasion; the āyah itself supplies '
      'it. Mūsā asked while <em>alive in the dunyā</em>, and the refusal came with a '
      'demonstration — the mountain was levelled by the mere unveiling. '
      '<strong>What the āyah proves is that this world cannot bear it</strong>, which is a '
      'statement about the asker\'s condition, not about Allah\'s being visible.'))

b += B.heading('الشُّبْهَةُ الثَّالِثَة · ﴿لَا تُدْرِكُهُ الْأَبْصَارُ﴾',
               'Third Objection — "The Eyes Do Not Grasp Him"')
b += B.sharh(
    p('<strong>They argued with His saying:</strong> <strong>%s</strong> '
      '(al-Anʿām 6:103).' % ar('لَا تُدْرِكُهُ الْأَبْصَارُ')) +
    p('<strong>The answer:</strong> <em>that the āyah contains only '
      '<strong>the negation of %s</strong>, and <strong>there is no negation of %s in it</strong>. '
      'And the meaning of al-idrāk is <strong>%s — encompassing</strong>. So Allah سبحانه وتعالى '
      '<strong>is seen by the believers, and they do not encompass Him.</strong></em>'
      % (ar('الإِدْرَاك'), ar('الرُّؤْيَة'), ar('الإِحَاطَة'))) +
    p('And then al-Fawzān turns the objection completely around, which is the most instructive '
      'move in the section: <em>rather, <strong>the negation of al-idrāk necessitates the '
      'existence of the seeing</strong> — <strong>so the āyah is from the proofs affirming the '
      'ruʾyah.</strong></em>') +
    p('Follow why. To say that eyes <em>do not encompass</em> something is to speak about how '
      'that thing is seen, not whether it is. One does not say of the invisible that it is not '
      'fully taken in by the eye. <strong>The denial of a limit on the seeing presupposes the '
      'seeing.</strong> The verse the deniers lean on hardest is counted among the proofs '
      'against them.') +
    p('And the distinction it leaves behind is the one to carry: <strong>the believers '
      '<em>see</em> Him and do not <em>encompass</em> Him.</strong> Which is the same shape as '
      'every attribute in this book — real, and not comprehended.'))

b += B.heading('خَاتِمَةُ القِسْمِ الأَوَّل · وَمَنْ تَدَبَّرَ القُرْآن',
               'The Close of Part One — Whoever Ponders the Qurʾān')
b += B.prose(
    'With this section the author closes the first part of his book: the evidence from the Book of '
    'Allah. He does not claim to have exhausted it, and says so.')
b += B.sharh(
    p('<strong>%s</strong> — al-Fawzān: <em>that is, '
      '<strong>the chapter of affirming the names of Allah and His attributes in the Qurʾān is '
      'abundant</strong>, and <strong>the author mentioned only some of it</strong>; for the '
      'affirming of Allah\'s names and attributes, in the manner that befits Him, has come in '
      '<strong>many āyāt</strong> of the Book of Allah.</em>'
      % ar('وَهَذَا البَابُ فِي كِتَابِ اللهِ كَثِيرٌ')) +
    p('Twenty-three sections and more than two hundred āyāt, and the author\'s own verdict is '
      'that this is a <em>selection</em>. That is worth registering before Part 2 begins: '
      '<strong>the case was never short of material.</strong>') +
    p('<strong>%s</strong> — <em>that is: pondered over it and reflected upon what it indicates '
      'of guidance</em> — <strong>%s</strong> — <em>that is: '
      '<strong>the way of correctness became clear to him</strong>.</em>'
      % (ar('وَمَنْ تَدَبَّرَ القُرْآنَ'), ar('تَبَيَّنَ لَهُ طَرِيقُ الحَقِّ'))) +
    p('And note the condition the author attaches: <strong>%s</strong> — '
      '<em>seeking guidance</em>. The promise is not made to whoever reads, nor to whoever '
      'studies hardest. It is made to whoever comes <em>looking for guidance</em> — which is why '
      'two people can read the same āyāt and only one of them is addressed by this sentence.'
      % ar('طَالِبًا لِلْهُدَى')) +
    p('<em>And the pondering of the Qurʾān is <strong>what is demanded by its recitation</strong>.</em> '
      'al-Fawzān closes the part with three āyāt, and they are worth reading in sequence:'))
b += B.ayah(
    'كِتَابٌ أَنْزَلْنَاهُ إِلَيْكَ مُبَارَكٌ لِيَدَّبَّرُوا آيَاتِهِ وَلِيَتَذَكَّرَ أُولُو '
    'الْأَلْبَابِ',
    '"A Book We have sent down to you, blessed, so that they may ponder its āyāt and that those '
    'of understanding may take heed."',
    'Sūrat Ṣād 38:29 · سورة ص')
b += B.ayah(
    'أَفَلَا يَتَدَبَّرُونَ الْقُرْآنَ أَمْ عَلَى قُلُوبٍ أَقْفَالُهَا',
    '"Will they not ponder the Qurʾān? Or are there locks upon their hearts?"',
    'Sūrat Muḥammad 47:24 · سورة محمد')
b += B.ayah(
    'أَفَلَمْ يَدَّبَّرُوا الْقَوْلَ',
    '"Have they then not pondered the speech?"',
    'Sūrat al-Muʾminūn 23:68 · سورة المؤمنون')
b += B.prose(
    'Three āyāt, and the middle one names the alternative to pondering. Not ignorance, and not '
    'lack of access — <strong>locks.</strong> Part 1 has spent twenty-three sections showing that '
    'the Qurʾān states these attributes plainly and repeatedly. '
    '<strong>So where someone has read all of it and arrived at the opposite, the Qurʾān\'s own '
    'diagnosis is not that the evidence was unclear.</strong>')

b += B.vocab([
    ('نَاضِرَة', 'nāḍirah', 'radiant',
     'With the ض — from النَّضَارَة: splendour, freshness, beauty'),
    ('نَاظِرَة', 'nāẓirah', 'looking',
     'With the ظ — they look at Him with their eyes'),
    ('الأَرَائِك', 'al-arāʾik', 'the couches',
     'Plural of أَرِيكَة'),
    ('مَحْجُوبُون', 'maḥjūbūn', 'veiled',
     'The disbelievers’ punishment — which proves there is a seeing to be veiled from'),
    ('الزِّيَادَة', 'al-ziyādah', 'the increase',
     'The looking at the Noble Face of Allah — per the Prophet ﷺ in Ṣaḥīḥ Muslim'),
    ('الجِهَة', 'al-jihah', 'direction',
     'An ambiguous word: indwelling in creation (false) vs above creation (true)'),
    ('الإِدْرَاك', 'al-idrāk', 'grasping, encompassing',
     'الإِحَاطَة — negated of Him; the seeing is not'),
    ('التَّدَبُّر', 'al-tadabbur', 'pondering',
     'What is demanded by the recitation — on condition of seeking guidance'),
])
b += B.mcq('ws-l21', [
    ('What is the difference between %s and %s?' % (ar('نَاضِرَة'), ar('نَاظِرَة')),
     ['They are two spellings of one word',
      'نَاضِرَة with the ض is from النَّضَارَة — radiance, what the faces ARE; نَاظِرَة with the '
      'ظ is from looking — what they DO',
      'One describes the believers, the other the angels',
      'One is in this world, the other in the Hereafter'], 1),
    ('How does al-Muṭaffifīn 83:15 support the believers’ seeing?',
     ['It does not; it concerns only the disbelievers',
      'Because being veiled is named as the disbelievers’ punishment — and a veil is only a '
      'deprivation if there is something behind it to be seen',
      'Because it mentions the couches',
      'Because the veil will be lifted for them later'], 1),
    ('What is %s in Yūnus 10:26, and on what authority?' % ar('وَزِيَادَةٌ'),
     ['Extra provision in the Garden, by consensus',
      'The looking at the Noble Face of Allah — established from the Prophet ﷺ in Ṣaḥīḥ Muslim '
      'and elsewhere, and so explained by the predecessors',
      'Forgiveness of what remained of their sins, by ijtihād',
      'An unspecified increase whose meaning is unknown'], 1),
    ('How does al-Fawzān answer the objection from %s?' % ar('الجِهَة'),
     ['By denying that Allah is above His creation',
      'By showing the word is ambiguous: indwelling in creation is false and does not follow from '
      'the seeing; being above creation is true and does not conflict with it',
      'By affirming that Allah is a body in a direction',
      'By refusing to discuss the word at all'], 1),
    ('How is %s answered?' % ar('لَنْ تَرَانِي'),
     ['By declaring the āyah abrogated',
      'It negates the seeing in this world and does not negate its occurring in the Hereafter — '
      'and people’s state there differs from their state here',
      'By reading it as a question rather than a negation',
      'By restricting it to Mūsā alone among all creation'], 1),
    ('Why is al-Anʿām 6:103 counted among the proofs FOR the seeing?',
     ['Because it mentions eyes',
      'Because it negates idrāk — encompassing — not ruʾyah; and to deny that eyes encompass a '
      'thing presupposes that it is seen',
      'Because it was revealed before the other āyāt',
      'Because الأَبْصَار here means the disbelievers’ eyes only'], 1),
    ('What condition does the author attach to %s?' % ar('وَمَنْ تَدَبَّرَ القُرْآنَ'),
     ['That he knows Arabic',
      'That he comes %s — seeking guidance' % ar('طَالِبًا لِلْهُدَى'),
      'That he has studied the sciences of hadith',
      'That he recites it in full'], 1),
])
b += B.tf('ws-l21-tf', [
    ('رُؤْيَةُ المُؤْمِنِينَ لِرَبِّهِمْ أَعْظَمُ النَّعِيمِ الَّذِي يَنَالُونَهُ.',
     'The believers’ seeing of their Lord is the greatest bliss they attain.', True),
    ('آيَةُ ﴿لَا تُدْرِكُهُ الْأَبْصَارُ﴾ فِيهَا نَفْيُ الرُّؤْيَةِ.',
     'The āyah "the eyes do not grasp Him" contains a negation of the seeing.', False),
    ('الأَحَادِيثُ فِي الرُّؤْيَةِ مُتَوَاتِرَةٌ.',
     'The aḥādīth on the seeing are mutawātir.', True),
    ('المُؤْمِنُونَ يَرَوْنَ اللهَ وَيُحِيطُونَ بِهِ.',
     'The believers see Allah and encompass Him.', False),
])
b += B.memorize(
    'وُجُوهٌ يَوْمَئِذٍ نَاضِرَةٌ إِلَى رَبِّهَا نَاظِرَةٌ',
    'Memorize it with the two letters distinct — the ض of radiance and the ظ of looking. The '
    'order is the argument: the faces are radiant <em>because</em> of what they are looking at.')
b += B.aiquiz('The believers seeing their Lord on the Day of Rising in al-Aqidah al-Wasitiyyah: '
              'nadirah with the dad against nazirah with the zaa, how the veiling of the '
              'disbelievers in al-Mutaffifin proves the seeing, the Prophets own tafsir of '
              'wa-ziyadah in Sahih Muslim, and the three objections of the deniers answered -- '
              'the ambiguity of jihah, lan tarani as about this world, and why la tudrikuhu '
              'al-absar is itself a proof for the seeing')
b += B.further()
b += B.nav('was-l20-tanzil-quran.html', 'The Sending Down of the Qurʾān',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l21')

io.open(os.path.join(B.AQ, 'was-l21-ruyah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'رُؤْيَةُ المُؤْمِنِينَ لِرَبِّهِمْ — وَخَاتِمَةُ القِسْمِ الأَوَّل',
    'The Believers Seeing Their Lord — and the Close of Part One',
    'Lesson 21 of al-ʿAqīdah al-Wāsiṭiyyah: nāḍirah '
    'against nāẓirah, how the veiling of the disbelievers proves the seeing, the '
    'Prophet’s ط own tafsīr of “and more,” the three objections of the '
    'deniers answered — and the author’s closing words sealing the evidence from the '
    'Book of Allah.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الحَادِي وَالعِشْرُون', '3',
           'رُؤْيَةُ المُؤْمِنِينَ لِرَبِّهِمْ — وَخَاتِمَةُ القِسْمِ الأَوَّل',
           'The Believers Seeing Their Lord — and the Close of Part One', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l21-ruyah.html')
