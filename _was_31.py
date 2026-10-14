# -*- coding: utf-8 -*-
"""Wasitiyyah L31 -- Part 3: the obligation of believing in the istiwa', the
'uluww and the ma'iyyah together, and al-Fawzan's four answers to the claim that
they conflict. Sharh pp.113-115."""
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
    'For the terminology of <span dir="rtl" lang="ar">المُتَوَاتِر</span> defined on this page, '
    'see also the <strong>Hadeeth</strong> track’s مُصْطَلَحُ الحَدِيث lessons.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'State the objection the author is forestalling, in its own words.',
    'Give all four of al-Fawzān’s answers to it.',
    'Define %s as al-Fawzān defines it.' % ar('المُتَوَاتِر'),
    'Say what %s and %s each add to the question of nearness.'
    % (ar('الرَّقِيب'), ar('المُهَيْمِن')),
])

b += B.heading('وُجُوبُ الإِيمَانِ بِاسْتِوَاءِ اللهِ عَلَى عَرْشِهِ وَعُلُوِّهِ وَمَعِيَّتِهِ '
               'وَأَنَّهُ لَا تَنَافِي بَيْنَهُمَا',
               'The Obligation of Believing in the Istiwāʾ, the ʿUluww and the Maʿiyyah — and That '
               'They Do Not Conflict')
b += B.matn(
    'وَقَدْ دَخَلَ فِيمَا ذَكَرْنَاهُ مِنَ الإِيمَانِ بِاللهِ الإِيمَانُ بِمَا أَخْبَرَ '
    'اللهُ بِهِ فِي كِتَابِهِ وَتَوَاتَرَ عَنْ رَسُولِهِ ﷺ وَأَجْمَعَ عَلَيْهِ سَلَفُ '
    'الأُمَّةِ: مِنْ أَنَّهُ سُبْحَانَهُ فَوْقَ سَمَاوَاتِهِ عَلَى عَرْشِهِ، عَلِيٌّ '
    'عَلَى خَلْقِهِ، وَهُوَ سُبْحَانَهُ مَعَهُمْ أَيْنَمَا كَانُوا، يَعْلَمُ مَا هُمْ '
    'عَامِلُونَ… وَلَيْسَ مَعْنَى قَوْلِهِ ﴿وَهُوَ مَعَكُمْ﴾ أَنَّهُ مُخْتَلِطٌ '
    'بِالخَلْقِ، فَإِنَّ هَذَا لَا تُوجِبُهُ اللُّغَةُ، وَهُوَ خِلَافُ مَا أَجْمَعَ '
    'عَلَيْهِ سَلَفُ الأُمَّةِ، وَخِلَافُ مَا فَطَرَ اللهُ عَلَيْهِ الخَلْقَ؛ بَلِ '
    'القَمَرُ آيَةٌ مِنْ آيَاتِ اللهِ مِنْ أَصْغَرِ مَخْلُوقَاتِهِ، وَهُوَ مَوْضُوعٌ '
    'فِي السَّمَاءِ، وَهُوَ مَعَ المُسَافِرِ وَغَيْرِ المُسَافِرِ أَيْنَمَا كَانَ. '
    'وَهُوَ سُبْحَانَهُ فَوْقَ عَرْشِهِ رَقِيبٌ عَلَى خَلْقِهِ، مُهَيْمِنٌ عَلَيْهِمْ، '
    'مُطَّلِعٌ عَلَيْهِمْ… إِلَى غَيْرِ ذَلِكَ مِنْ مَعَانِي رُبُوبِيَّتِهِ.')
b += B.prose(
    'al-Fawzān explains the author\'s motive for singling these two out: <em>the author رحمه الله '
    '<strong>specified these two matters — the istiwāʾ upon the Throne, and His maʿiyyah with the '
    'creation — for a warning, in order to remove the difficulty</strong>, for one might imagine '
    'that there is a conflict between them.</em> Parts 1 and 2 brought the texts; '
    '<strong>this section is about the student\'s own objection.</strong>')
b += B.ayah(
    'هُوَ الَّذِي خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ فِي سِتَّةِ أَيَّامٍ ثُمَّ اسْتَوَى عَلَى '
    'الْعَرْشِ يَعْلَمُ مَا يَلِجُ فِي الْأَرْضِ وَمَا يَخْرُجُ مِنْهَا وَمَا يَنْزِلُ مِنَ '
    'السَّمَاءِ وَمَا يَعْرُجُ فِيهَا وَهُوَ مَعَكُمْ أَيْنَ مَا كُنْتُمْ وَاللَّهُ بِمَا '
    'تَعْمَلُونَ بَصِيرٌ',
    '"He it is who created the heavens and the earth in six days, then rose over the Throne. He '
    'knows what penetrates into the earth and what comes out of it, and what descends from the '
    'heaven and what ascends into it; and He is with you wherever you are — and Allah is Seeing '
    'of what you do."',
    'Sūrat al-Ḥadīd 57:4 · سُورَةُ الحَدِيد')
b += B.prose(
    'Notice why the author chose this āyah above all others for the purpose. '
    '<strong>It states both in one breath</strong> — the istiwāʾ upon the Throne, and «He is with '
    'you wherever you are» — <em>as He gathered the two together in His saying…</em> '
    '<strong>So whoever holds that the two conflict is holding that a single āyah contradicts '
    'itself.</strong>')
b += B.sharh(
    p('And here is the objection stated at full strength, as al-Fawzān puts it: '
      '<em>one might suppose that this is <strong>like the attributes of the created</strong>, and '
      'that <strong>He is mixed with them</strong> — </em>') +
    '<div style="background:#fff8e6;border-right:4px solid #d4a017;'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .9rem">'
    '<p style="margin:0;font-size:.95rem"><em>— so <strong>how can He be above His creation, '
    'established upon His Throne, and be with His creation, near to them, without '
    'mixing?!</strong></em></p></div>' +
    p('That is a fair question, and the author does not dismiss it. He answers it — and al-Fawzān '
      'lays the answer out in <strong>four distinct grounds</strong>, which are worth taking one '
      'at a time, because they come from four different places: '
      '<strong>the language · the consensus · the fiṭrah · and the transmitted texts.</strong>'))

b += B.heading('الوَجْهُ الأَوَّل · اللُّغَةُ لَا تُوجِبُه',
               'First Ground — The Language Does Not Require It')
b += B.sharh(
    p('<em>That <strong>this is not required by the language of the Arabs in which the Noble '
      'Qurʾān was sent down</strong>: for the word <strong>%s</strong> in the language is for '
      '<strong>%s — unrestricted accompaniment</strong>. '
      '<strong>It does not convey mixing or blending, nor adjacency, nor contact.</strong></em>'
      % (ar('مَعَ'), ar('مُطْلَقِ المُصَاحَبَة'))) +
    p('And al-Fawzān gives two examples from ordinary speech, the first of which is new here:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.93rem">'
    '<p style="margin:0 0 .6rem">— <em>for you say <strong>'
    '«<span dir="rtl" lang="ar">زَوْجَتِي مَعِي</span>», my wife is with me</strong> '
    '— <strong>while you are in one place and she is in another.</strong></em></p>'
    '<p style="margin:0">— <em>and you say <strong>'
    '«<span dir="rtl" lang="ar">مَا زِلْنَا نَسِيرُ وَالقَمَرُ مَعَنَا</span>», we kept '
    'travelling and the moon was with us</strong> — <strong>and it is in the heaven</strong>; '
    'and it is with the traveller and the non-traveller, wherever he is.</em></p></div>' +
    p('The first example is the more telling of the two, because it is not even about distance in '
      'the sky. <strong>A man says «my wife is with me» while she is at home and he is at '
      'work</strong>, and no listener is confused. <em>With</em> is a word about relation, not '
      'about position — and the one who insists that %s must mean <em>mixed in among</em> is '
      'making a claim about Arabic that no speaker of Arabic makes.' % ar('مَعَ')) +
    p('And then the argument from the lesser to the greater, which is al-Fawzān\'s habitual move: '
      '<em>and <strong>if it is correct to say this concerning the moon — and it is a small '
      'created thing — then how should it not be said concerning the Creator, who is greater than '
      'everything?</strong></em>'))

b += B.heading('الوَجْهُ الثَّانِي · خِلَافُ إِجْمَاعِ السَّلَف',
               'Second Ground — It Contradicts the Consensus of the Salaf')
b += B.sharh(
    p('<em>That <strong>this statement contradicts what the predecessors of the Ummah were agreed '
      'upon</strong> — of <strong>the Ṣaḥābah, the Tābiʿūn and those who followed them</strong> '
      '(<strong>%s — and they are the most excellent generations</strong>), '
      '<strong>who are the examples to be followed</strong>.</em>'
      % ar('القُرُونُ المُفَضَّلَة')) +
    p('And al-Fawzān states what exactly they agreed on, in two clauses:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line)">'
    '<em>they were agreed that Allah is <strong>established upon His Throne, high above His '
    'creation</strong>, <strong><span dir="rtl" lang="ar">بَائِنٌ مِنْهُمْ</span> — '
    'separate from them</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .75rem;border:1px solid var(--line)">'
    '<em>and they were agreed that He is <strong>with His creation '
    '<span dir="rtl" lang="ar">بِعِلْمِهِ</span> — by His knowledge</strong> '
    'سبحانه وتعالى — '
    '<strong>as they explained His saying <span dir="rtl" lang="ar">وَهُوَ مَعَكُمْ</span> with '
    'exactly that</strong></em></td></tr>'
    '</table></div>' +
    p('<strong>%s</strong> is the word to keep from this ground. The Salaf did not merely affirm '
      'the height; they stated the separateness — which is the precise denial of the '
      '<em>ḥulūliyyah</em> position that Allah is indwelling in His creation. '
      '<strong>And they did not leave %s without a reading: they read it as His knowledge</strong>, '
      'which is what Lesson 17 found the two āyāt of the general maʿiyyah doing themselves.'
      % (ar('بَائِنٌ مِنْهُمْ'), ar('وَهُوَ مَعَكُمْ'))))

b += B.heading('الوَجْهُ الثَّالِث · خِلَافُ الفِطْرَة',
               'Third Ground — It Contradicts the Fiṭrah')
b += B.sharh(
    p('<em>That <strong>this contradicts what Allah created the creation upon</strong> — '
      'that is, <strong>what He implanted in their very natures</strong>: for '
      '<strong>the creation were created upon the acknowledgement of Allah\'s highness above His '
      'creation.</strong></em>') +
    p('And the evidence he gives for it is not a text at all. It is an observation about what '
      'people do:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem"><em>For <strong>the creation turn toward Allah, at '
    'hardships and calamities, in the direction of HEIGHT</strong> — '
    '<strong>they do not turn to the right or to the left</strong> — '
    '<strong>without anyone having guided them to that.</strong> '
    'That is only by the requirement of the fiṭrah upon which Allah created '
    'people.</em></p></div>' +
    p('This is an argument anyone can test, and it does not require literacy. '
      '<strong>Watch where a person\'s hands and eyes go when something terrible happens.</strong> '
      'Not sideways, and not down. And the ones who do it have mostly never read a line of this '
      'book — which is the point: a doctrine that has to be taught against the grain of every '
      'instinct is a doctrine with a case to answer.'))

b += B.heading('الوَجْهُ الرَّابِع · خِلَافُ الكِتَابِ وَالمُتَوَاتِرِ مِنَ السُّنَّة',
               'Fourth Ground — It Contradicts the Book and the Mutawātir Sunnah')
b += B.sharh(
    p('<em>That <strong>this contradicts what Allah informed of in His Book and what was '
      'transmitted <span dir="rtl" lang="ar">مُتَوَاتِرًا</span> from His Messenger</strong> '
      '&#65018; — that He سبحانه وتعالى is upon His Throne, high above His creation, '
      '<strong>and He is with them wherever they are.</strong></em>') +
    p('And since the author rested the matn on the word %s, al-Fawzān defines it — and this is a '
      'definition from %s worth learning here, where it is being used, rather than in the '
      'abstract:' % (ar('وَتَوَاتَرَ'), ar('مُصْطَلَحِ الحَدِيث'))) +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem">'
    '<p style="margin:0;font-size:.95rem" dir="rtl" lang="ar"><strong>المُتَوَاتِرُ مِنَ '
    'النُّصُوصِ: هُوَ مَا رَوَاهُ جَمَاعَةٌ تُحِيلُ العَادَةُ تَوَاطُؤَهُمْ عَلَى '
    'الكَذِبِ، عَنْ مِثْلِهِمْ، مِنَ الابْتِدَاءِ إِلَى الانْتِهَاءِ.</strong></p>'
    '<p style="margin:.5rem 0 0;font-size:.9rem">— <em>the mutawātir among the texts is '
    '<strong>what a group transmitted whose colluding upon a lie is ruled out by ordinary '
    'experience</strong>, <strong>from a group like themselves</strong>, '
    '<strong>from the beginning of the chain to its end.</strong></em></p></div>' +
    p('Read the three parts of it. <strong>A group large enough that collusion is not '
      'credible</strong> — not a count of narrators but a judgement about what human beings '
      'plausibly do. <strong>From a group like themselves</strong> — the breadth has to hold at '
      'every link. <strong>From beginning to end</strong> — a chain that is broad at one layer '
      'and narrows to one man at another is not mutawātir.') +
    p('That is why it outranks even the ṣaḥīḥ report of Lesson 22: a ṣaḥīḥ ḥadīth asks you to '
      'trust the uprightness and precision of particular men, while '
      '<strong>a mutawātir text asks you to believe only that a crowd does not conspire.</strong>') +
    p('<em>And <strong>the āyāt and the aḥādīth on this are many</strong> — among them the āyah '
      'the author mentioned. وَاللهُ أَعْلَم.</em>'))

b += B.heading('الرَّقِيبُ وَالمُهَيْمِن', 'al-Raqīb and al-Muhaymin')
b += B.sharh(
    p('The author closes the passage with <strong>%s</strong>, and al-Fawzān reads this as '
      '<em>a confirming and an emphasising of what preceded</em> — the height and the withness — '
      '<em>by mentioning <strong>two of His names</strong></em>.'
      % ar('وَهُوَ سُبْحَانَهُ فَوْقَ عَرْشِهِ رَقِيبٌ عَلَى خَلْقِهِ مُهَيْمِنٌ عَلَيْهِمْ مُطَّلِعٌ عَلَيْهِمْ')))
b += B.ayah(
    'إِنَّ اللَّهَ كَانَ عَلَيْكُمْ رَقِيبًا',
    '"Indeed Allah is ever Watchful over you."',
    'Sūrat al-Nisāʾ 4:1 · سُورَةُ النِّسَاء')
b += B.sharh(
    p('<strong>%s</strong> — <em>is <strong>the One who watches over the states of His '
      'servants</strong>; <strong>and in that is an indication of His nearness to them.</strong></em>'
      % ar('الرَّقِيب')))
b += B.ayah(
    'هُوَ اللَّهُ الَّذِي لَا إِلَهَ إِلَّا هُوَ الْمَلِكُ الْقُدُّوسُ السَّلَامُ '
    'الْمُؤْمِنُ الْمُهَيْمِنُ',
    '"He is Allah, beside whom there is no god — the Sovereign, the Most Holy, the Author of '
    'Peace, the Granter of Security, the Overseer."',
    'Sūrat al-Ḥashr 59:23 · سُورَةُ الحَشْر')
b += B.sharh(
    p('<strong>%s</strong> — <em>is <strong>the Witness over His creation, the One acquainted with '
      'their deeds, the Watcher over them</strong>.</em>' % ar('المُهَيْمِن')) +
    p('Both names do the same work for the argument, and it is worth seeing how. '
      '<strong>A watchman is not the thing he watches.</strong> The very meaning of <em>raqīb</em> '
      'and <em>muhaymin</em> requires <em>someone over something</em> — so these two names '
      'affirm the nearness (He is attending to each of them) <strong>in language that '
      'presupposes He is not one of them.</strong> The author did not choose them at random.') +
    p('<strong>%s</strong> — al-Fawzān: <em>that is, '
      '<strong>the requirement of His lordship سبحانه is that He be above His creation '
      '<span dir="rtl" lang="ar">بِذَاتِهِ</span> — by His very Self — and be acquainted with '
      'their deeds, and be near to them by His knowledge and His encompassing; disposing of their '
      'affairs, recording their deeds, and recompensing them for them.</strong></em>'
      % ar('إِلَى غَيْرِ ذَلِكَ مِنْ مَعَانِي رُبُوبِيَّتِه')) +
    p('So the whole difficulty dissolves into a distinction the student has now met in four '
      'different places: <strong>above them by His Self, with them by His knowledge.</strong> Not '
      'two halves of a compromise, but two true statements about different things.'))

b += B.vocab([
    ('مُطْلَقُ المُصَاحَبَة', 'muṭlaq al-muṣāḥabah',
     'unrestricted accompaniment',
     'What مَعَ means in Arabic — not mixing, blending, adjacency or contact'),
    ('بَائِنٌ مِنْهُم', 'bāʿinun minhum', 'separate from them',
     'The Salaf’s own word — the denial of indwelling'),
    ('القُرُونُ المُفَضَّلَة', 'al-qurūn al-mufāḍalah',
     'the most excellent generations',
     'The Ṣaḥābah, the Tābiʿūn and those after them'),
    ('الفِطْرَة', 'al-fiṭrah', 'the innate nature',
     'At calamity people turn upward — not sideways — untaught'),
    ('المُتَوَاتِر', 'al-mutawātir', 'mass-transmitted',
     'A group whose collusion on a lie is ruled out, from a like group, at every link'),
    ('الرَّقِيب', 'al-Raqīb', 'the Watchful',
     'The One who watches over the states of His servants — indicating His nearness'),
    ('المُهَيْمِن', 'al-Muhaymin', 'the Overseer',
     'The Witness over His creation, acquainted with their deeds'),
    ('بِذَاتِه', 'bi-dhātih', 'by His very Self',
     'How He is above them — as against بِعِلْمِهِ, how He is with them'),
])
b += B.mcq('ws-l31', [
    ('Why did the author single out the istiwāʾ and the maʿiyyah for a warning?',
     ['Because they are the hardest attributes to pronounce',
      'To remove the difficulty, since one might imagine a conflict between them',
      'Because the Jahmiyyah denied only these two',
      'Because they are mentioned least often'], 1),
    ('Why is al-Ḥadīd 57:4 the right āyah for this purpose?',
     ['Because it is the longest āyah on the attributes',
      'Because it states both in one breath — so whoever holds they conflict holds that one āyah '
      'contradicts itself',
      'Because it was the last revealed on the subject',
      'Because it mentions the six days'], 1),
    ('What does %s convey in Arabic, per al-Fawzān?' % ar('مَعَ'),
     ['Adjacency and contact',
      'Unrestricted accompaniment — not mixing, blending, adjacency or contact',
      'Being inside something', 'Being on the same level'], 1),
    ('Which everyday example does al-Fawzān give alongside the moon?',
     ['"The shade is with the walker"',
      '"My wife is with me" — said while you are in one place and she is in another',
      '"The road is with the traveller"', '"The sun is with the farmer"'], 1),
    ('What two things did the Salaf agree upon, in al-Fawzān’s words?',
     ['That He is above and that the question is not to be asked',
      'That He is established on His Throne, high above His creation and <em>separate from '
      'them</em>; and that He is with His creation <em>by His knowledge</em>',
      'That the istiwāʾ is known and the maʿiyyah unknown',
      'That both are to be left unexplained'], 1),
    ('What is the evidence from the fiṭrah?',
     ['A ḥadīth about the newborn',
      'That at hardships people turn toward Allah in the direction of height — not to the right '
      'or left — without anyone having guided them to it',
      'The consensus of the philosophers',
      'That children are taught it from infancy'], 1),
    ('How does al-Fawzān define %s?' % ar('المُتَوَاتِر'),
     ['A ḥadīth narrated by at least ten Companions',
      'What a group transmitted whose colluding upon a lie is ruled out by experience, from a '
      'group like themselves, from the beginning of the chain to its end',
      'A ḥadīth agreed upon by al-Bukhārī and Muslim',
      'A ḥadīth whose narrators are all upright and precise'], 1),
    ('How do %s and %s support the argument?' % (ar('الرَّقِيب'), ar('المُهَيْمِن')),
     ['They affirm His knowledge and deny His nearness',
      'Their very meaning requires someone over something — so they affirm nearness in language '
      'that presupposes He is not one of them',
      'They are names of the Essence, not of action',
      'They refer only to the Day of Rising'], 1),
])
b += B.tf('ws-l31-tf', [
    ('كَلِمَةُ «مَعَ» فِي اللُّغَةِ تُفِيدُ الاخْتِلَاطَ وَالمُمَاسَّةَ.',
     'The word maʿa in Arabic conveys mixing and contact.', False),
    ('أَجْمَعَ السَّلَفُ عَلَى أَنَّ اللهَ بَائِنٌ مِنْ خَلْقِهِ.',
     'The Salaf agreed that Allah is separate from His creation.', True),
    ('الخَلْقُ يَتَّجِهُونَ عِنْدَ الشَّدَائِدِ نَحْوَ العُلُوِّ بِمُوجَبِ الفِطْرَةِ.',
     'At calamities people turn upward by the requirement of the fiṭrah.', True),
    ('هُوَ سُبْحَانَهُ فَوْقَ خَلْقِهِ بِعِلْمِهِ، وَمَعَهُمْ بِذَاتِهِ.',
     'He is above His creation by His knowledge, and with them by His Self.', False),
])
b += B.memorize(
    'عَالٍ عَلَى خَلْقِهِ بَائِنٌ مِنْهُمْ، وَهُوَ مَعَهُمْ بِعِلْمِهِ',
    'The consensus of the Salaf in one line, and the whole answer to the difficulty: '
    '<strong>above them by His Self, with them by His knowledge.</strong> Two true statements '
    'about different things — which is why there was never a contradiction to resolve.')
b += B.aiquiz('The obligation of believing in the istiwa, the uluww and the maiyyah together in '
              'al-Aqidah al-Wasitiyyah, and al-Fawzan four answers to the claim that they '
              'conflict: that maa means unrestricted accompaniment with the examples of the wife '
              'and the moon, the consensus of the Salaf that He is bainun minhum and with them '
              'bi-ilmih, the argument from the fitrah that people turn upward untaught, and the '
              'definition of al-mutawatir -- plus how al-Raqib and al-Muhaymin affirm nearness in '
              'language presupposing He is not one of them')
b += B.further()
b += B.nav('was-l30-makanah-wasat.html', 'The Standing of Ahl al-Sunnah',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l31')

io.open(os.path.join(B.AQ, 'was-l31-wujub-istiwa-maiyyah.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'وُجُوبُ الإِيمَانِ بِالعُلُوِّ وَالمَعِيَّةِ مَعًا',
    'The Obligation of Believing in the Highness and the Withness Together',
    'Lesson 31 of al-ʿAqīdah al-Wāsiṭiyyah: the objection '
    'stated at full strength, and al-Fawzān’s four answers from the language, the '
    'consensus, the fiṭrah and the mutawātir texts — with the definition of '
    'al-mutawātir, and why al-Raqīb and al-Muhaymin were not chosen at random.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الحَادِي وَالثَّلَاثُون', '3',
           'وُجُوبُ الإِيمَانِ بِالعُلُوِّ وَالمَعِيَّةِ مَعًا',
           'The Obligation of Believing in the Highness and the Withness Together', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l31-wujub-istiwa-maiyyah.html')
