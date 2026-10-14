# -*- coding: utf-8 -*-
"""Wasitiyyah L34 -- Part 3: the obligation of believing that the Qur'an is the
speech of Allah in reality, uncreated, its letters and its meanings -- against
the Jahmiyyah, the Kullabiyyah, the Ashaira and the Mu'tazilah.
Sharh pp.120-123."""
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
    'Lesson 19 of this track covered the attribute of speech itself; this lesson is the '
    '<em>Qurʾān</em> specifically, and the four positions opposed to it.',
]


def p(x):
    return '<p style="margin:0 0 .7rem">%s</p>' % x


def ar(x):
    return '<span dir="rtl" lang="ar">%s</span>' % x


b = B.objectives([
    'Explain the distinction between %s and %s in Allah’s speech.'
    % (ar('نَوْعُ الكَلَام'), ar('مُفْرَدَاتُه')),
    'Give both meanings al-Fawzān offers for %s.' % ar('وَإِلَيْهِ يَعُودُ'),
    'State the position of the Jahmiyyah, the Kullābiyyah, the Ashāʿirah and the Muʿtazilah, and '
    'what each one costs.',
    'Give the author’s own proof that the Qurʾān remains Allah’s speech when a man recites it.',
])

b += B.heading('وُجُوبُ الإِيمَانِ بِأَنَّ القُرْآنَ كَلَامُ اللهِ حَقِيقَة',
               'The Obligation of Believing That the Qurʾān Is the Speech of Allah in Reality')
b += B.matn(
    'فَصْلٌ — وَمِنَ الإِيمَانِ بِاللهِ وَكُتُبِهِ: الإِيمَانُ بِأَنَّ القُرْآنَ كَلَامُ '
    'اللهِ مُنَزَّلٌ غَيْرُ مَخْلُوقٍ، مِنْهُ بَدَأَ وَإِلَيْهِ يَعُودُ، وَأَنَّ اللهَ '
    'تَكَلَّمَ بِهِ حَقِيقَةً، وَأَنَّ هَذَا القُرْآنَ الَّذِي أَنْزَلَهُ عَلَى '
    'مُحَمَّدٍ ﷺ هُوَ كَلَامُ اللهِ حَقِيقَةً لَا كَلَامُ غَيْرِهِ، وَلَا يَجُوزُ '
    'إِطْلَاقُ القَوْلِ بِأَنَّهُ حِكَايَةٌ عَنْ كَلَامِ اللهِ أَوْ عِبَارَةٌ، بَلْ '
    'إِذَا قَرَأَهُ النَّاسُ أَوْ كَتَبُوهُ فِي المَصَاحِفِ لَمْ يَخْرُجْ بِذَلِكَ '
    'عَنْ أَنْ يَكُونَ كَلَامَ اللهِ تَعَالَى حَقِيقَةً؛ فَإِنَّ الكَلَامَ إِنَّمَا '
    'يُضَافُ حَقِيقَةً إِلَى مَنْ قَالَهُ مُبْتَدِئًا، لَا إِلَى مَنْ قَالَهُ '
    'مُبَلِّغًا مُؤَدِّيًا. وَهُوَ كَلَامُ اللهِ حُرُوفُهُ وَمَعَانِيهِ، لَيْسَ '
    'كَلَامُ اللهِ الحُرُوفَ دُونَ المَعَانِي، وَلَا المَعَانِي دُونَ الحُرُوفِ.')
b += B.sharh(
    p('al-Fawzān first shows why this belongs under <em>two</em> of the six pillars at once: '
      '<em>of the foundations of faith are <strong>belief in Allah</strong> and '
      '<strong>belief in His Books</strong> — and <strong>belief that the Qurʾān is the speech of '
      'Allah enters into both of these foundations.</strong> For belief in Allah عز وجل '
      '<strong>comprises belief in His attributes, and His speech is one of His '
      'attributes</strong>; and of His speech is the Mighty Qurʾān, which is the greatest of His '
      'Books — <strong>so it enters into belief in His Books by the foremost kind of '
      'entry.</strong></em>') +
    p('Then the formula for the attribute, which gathers Lesson 19 into one line: '
      '<em>Allah تعالى is described as <strong>speaking with what He wills, when He wills; He has '
      'never ceased and will never cease speaking; and His speech does not run out.</strong></em>'))
b += B.sharh(
    p('And now a distinction that is the most precise thing in the section, and which resolves an '
      'old difficulty in one stroke:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>نَوْعُ الكَلَام</strong><br>'
    '<span style="font-size:.82rem">the KIND</span></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<strong><span dir="rtl" lang="ar">أَزَلِيٌّ أَبَدِيٌّ</span></strong> — '
    'beginningless and endless. He was never not a Speaker.</td></tr>'
    '<tr><td style="padding:.65rem .8rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>مُفْرَدَاتُه</strong><br>'
    '<span style="font-size:.82rem">the individual instances</span></td>'
    '<td style="padding:.65rem .8rem;border:1px solid var(--line)">'
    '<em><strong>do not cease occurring one after another</strong>, '
    '<span dir="rtl" lang="ar">شَيْئًا فَشَيْئًا</span>, '
    '<strong>according to His wisdom</strong></em> تعالى.</td></tr>'
    '</table></div>' +
    p('This is how Ahl al-Sunnah can say both halves of Lesson 19 without strain. '
      '<strong>Speech is an attribute of the Essence</strong> — because the <em>kind</em> never '
      'began. <strong>And it is an attribute of the Actions</strong> — because each '
      '<em>instance</em> occurs by His will, at a time. So He addressed Mūsā at an appointed hour, '
      'and will address ʿĪsā on the Day of Rising, <strong>without His having become a Speaker at '
      'some point</strong>. The two parties of Lesson 19 each had to deny one of these; the '
      'distinction between the kind and its instances lets you keep both.') +
    p('And from this the conclusion the whole section is built on: <em>and <strong>His attributes '
      'are not created, so His speech is not created.</strong></em> Not a separate claim, but a '
      'consequence — <strong>if the speech is an attribute, then whoever says it is created has '
      'said that an attribute of Allah is created.</strong>'))

b += B.heading('١ · مَقَالَةُ الجَهْمِيَّة', 'First — the Position of the Jahmiyyah')
b += B.sharh(
    p('<em>And <strong>parties opposed this</strong>, and the Shaykh رحمه الله mentioned the '
      'statement of some of them here.</em> The first: <em>the Jahmiyyah, who say '
      '<strong>that Allah does not speak at all</strong>; rather <strong>He created a speech in '
      'something other than Himself and made it express Him</strong>. So the ascribing of the '
      'speech to Allah with them is <strong>figurative, not real</strong> — because He created '
      'the speech, so He is «a speaker» <strong>in the sense of being the creator of speech in '
      'another</strong>.</em>') +
    p('<em>And <strong>this statement is false</strong>, contradicting the transmitted and the '
      'rational proofs, and contradicting the statement of the Salaf and the imāms of the '
      'Muslims.</em> And then al-Fawzān\'s refutation, which is two questions and needs no '
      'apparatus at all:') +
    '<div style="background:var(--brand-wash);border-right:4px solid var(--brand);'
    'border-radius:var(--radius-sm);padding:var(--space-md);margin:0 0 .7rem;font-size:.94rem">'
    '<p style="margin:0 0 .6rem"><em>For <strong>it is not intelligible that anyone be called a '
    'speaker except one in whom the speech really subsists.</strong></em></p>'
    '<p style="margin:0"><em>— <strong>So how is it said: «Allah said», while the sayer is '
    'someone else?! And how is it said: «the speech of Allah», while it is the speech of someone '
    'else?!</strong></em></p></div>' +
    p('That is the whole matter. <strong>A created speech placed in a creature is that '
      'creature\'s speech</strong>, however it got there — and calling its maker the speaker is '
      'like calling a carpenter the author of the book printed on his paper.'))
b += B.sharh(
    p('And this is what the author\'s clause <strong>%s</strong> was written against. al-Fawzān: '
      '<em>his intent by this is <strong>the refutation of the Jahmiyyah, who say that the Qurʾān '
      'began from someone other than Him, and that Allah did not speak it in reality but '
      'figuratively, and that it is the speech of another ascribed to Him because He created '
      'it.</strong></em>' % ar('مِنْهُ بَدَأَ وَإِلَيْهِ يَعُودُ')) +
    p('<strong>%s</strong> — <em>that the Qurʾān <strong>began and came forth from Allah تعالى, '
      'and He spoke it</strong>; and the %s is <strong>for the starting-point</strong></em> '
      '(%s). The preposition is the argument: <em>from</em> Him, not <em>through</em> Him.'
      % (ar('مِنْهُ بَدَأَ'), ar('مِنْ'), ar('لِابْتِدَاءِ الغَايَة'))) +
    p('<strong>%s</strong> — and here al-Fawzān gives two possible meanings, and the first is '
      'striking: <em>that the Qurʾān <strong>returns to Allah تعالى, because '
      '<span style="white-space:nowrap">it will be raised up at the end of time</span>, so that '
      'nothing of it remains — neither in the breasts nor in the copies — '
      '<strong>and that is among the signs of the Hour</strong>; or the meaning is '
      '<strong>that it is ascribed to Him.</strong></em>'
      % ar('وَإِلَيْهِ يَعُودُ')))

b += B.heading('٢ وَ٣ · الكُلَّابِيَّةُ وَالأَشَاعِرَة',
               'Second and Third — the Kullābiyyah and the Ashāʿirah')
b += B.sharh(
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.89rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>الكُلَّابِيَّة</strong><br>'
    '<span style="font-size:.8rem">عَبْدُ اللهِ بْنُ سَعِيدِ بْنِ كُلَّابٍ</span></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">the Qurʾān is '
    '<strong><span dir="rtl" lang="ar">حِكَايَةٌ</span> — a RECOUNTING</strong> of Allah’s '
    'speech. <em>For Allah’s speech with them is <strong>a meaning subsisting in '
    'Himself</strong>, <strong>necessary to His Essence as life and knowledge are</strong>, '
    '<strong>not connected to His will and volition</strong>. That meaning is uncreated; but '
    'these utterances, made of letters and sounds, are <strong>created</strong>, and are a '
    'recounting of His speech — <strong>not His speech.</strong></em></td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'vertical-align:top" dir="rtl" lang="ar"><strong>الأَشَاعِرَة</strong><br>'
    '<span style="font-size:.8rem">أَبُو الحَسَنِ الأَشْعَرِيّ</span></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">the Qurʾān is '
    '<strong><span dir="rtl" lang="ar">عِبَارَةٌ</span> — an EXPRESSION</strong> of '
    'Allah’s speech. <em>For His speech with them is a meaning subsisting in Himself, and '
    'that meaning is uncreated; but <strong>these recited utterances are an expression of that '
    'inner meaning, and they are created</strong> — <strong>and it is not said that they are '
    'a recounting of it.</strong></em></td></tr>'
    '</table></div>' +
    p('<em>And <strong>some of the scholars say that the difference between the Kullābiyyah and '
      'the Ashāʿirah is a verbal difference with nothing under it</strong></em> '
      '(%s). <em>For both say: <strong>the Qurʾān is of two kinds — utterances and meanings; the '
      'utterances are created, and these are the ones in existence; and the meanings are '
      'pre-eternal, subsisting in the Self, <strong>a single meaning admitting of no division and '
      'no multiplicity.</strong></strong></em>'
      % ar('خِلَافٌ لَفْظِيٌّ لَا طَائِلَ تَحْتَه')) +
    p('Follow what that last clause costs. If Allah\'s speech is <strong>one single undivided '
      'meaning</strong>, then the Torah and the Qurʾān are the same thing; the command and the '
      'prohibition are the same thing; <em>«do not approach prayer while intoxicated»</em> and '
      '<em>«and Allah created you and what you do»</em> are the same thing. '
      '<strong>And nothing you have ever recited is any of it.</strong>') +
    p('<em>And the Shaykh رحمه الله pointed to <strong>the invalidity of both of these '
      'statements</strong> by saying <strong>%s</strong> — that is, <em>as the Kullābiyyah say</em> '
      '— <strong>%s</strong>, as the Ashāʿirah say.</em>'
      % (ar('وَلَا يَجُوزُ إِطْلَاقُ القَوْلِ بِأَنَّهُ حِكَايَةٌ عَنْ كَلَامِ اللهِ'),
         ar('أَوْ عِبَارَةٌ عَنْه'))) +
    p('<em>And <strong>%s</strong> — that is: <strong>the Mighty Qurʾān is the speech of Allah, '
      'its utterances and its meanings, <em>wherever it is found</em>: whether it is preserved in '
      'the breasts, or recited by the tongues, or written in the copies — it does not thereby '
      'cease to be the speech of Allah تعالى in reality.</strong></em>'
      % ar('بَلْ إِذَا قَرَأَهُ النَّاسُ أَوْ كَتَبُوهُ فِي المَصَاحِفِ لَمْ يَخْرُجْ بِذَلِكَ عَنْ أَنْ يَكُونَ كَلَامَ اللهِ حَقِيقَةً')))

b += B.heading('دَلِيلُ المُصَنِّف · المُبْتَدِئُ لَا المُبَلِّغ',
               'The Author’s Proof — the Originator, Not the Conveyer')
b += B.sharh(
    p('<em>Then the Shaykh رحمه الله mentioned the proof of that, saying: <strong>%s</strong> — '
      'for <strong>the conveying transmitter is only called <em>%s</em> — a means</strong>, and '
      'nothing more.</em>'
      % (ar('فَإِنَّ الكَلَامَ إِنَّمَا يُضَافُ حَقِيقَةً إِلَى مَنْ قَالَهُ مُبْتَدِئًا، لَا إِلَى مَنْ قَالَهُ مُبَلِّغًا مُؤَدِّيًا'),
         ar('وَاسِطَة'))) +
    p('This is a rule everyone already uses. <strong>When a messenger reads out a king\'s letter, '
      'the words are the king\'s</strong> — nobody says the herald wrote them, and nobody says '
      'that the letter stopped being the king\'s when it was read aloud. '
      '<strong>Speech is ascribed to whoever first said it.</strong>') +
    p('And then the proof from the Qurʾān, which the student has already met once:'))
b += B.ayah(
    'وَإِنْ أَحَدٌ مِنَ الْمُشْرِكِينَ اسْتَجَارَكَ فَأَجِرْهُ حَتَّى يَسْمَعَ كَلَامَ اللَّهِ',
    '"And if any one of the mushrikūn seeks your protection, then grant him protection until he '
    'hears the speech of Allah."',
    'Sūrat al-Tawbah 9:6 · سُورَةُ التَّوْبَة')
b += B.sharh(
    p('<em>And <strong>the hearing mentioned in this āyah can only be by means of a conveying '
      'transmitter</strong> — <strong>and what is heard is called «the speech of Allah»</strong>. '
      '<strong>So it indicates that speech is ascribed only to the one who said it as the '
      'originator.</strong></em>') +
    p('Notice how exactly this āyah is being used, and that it is a <em>second</em> job for it. In '
      'Lesson 19 it proved that <strong>the recited Qurʾān is Allah\'s speech</strong>. Here it '
      'proves <strong>why that stays true through a human reciter</strong> — because the mushrik '
      'in the āyah hears it from the Prophet\'s &#65018; mouth or a Companion\'s, with his ears, '
      'in Arabic, <strong>and the Qurʾān still calls what reached his ears «the speech of '
      'Allah».</strong>') +
    p('<strong>Which is precisely what the Kullābiyyah and the Ashāʿirah must deny.</strong> On '
      'their account, what that man heard was a created recounting or expression, and the speech '
      'of Allah never reached him at all. <strong>The āyah says it did.</strong>'))

b += B.heading('٤ · مَقَالَةُ المُعْتَزِلَة · وَالمَذْهَبُ الحَقّ',
               'Fourth — the Muʿtazilah; and the True Position')
b += B.sharh(
    p('<em>Then the Shaykh mentioned <strong>the statement of the Muʿtazilah</strong>, who say: '
      '<strong>the speech of Allah is the letters without the meanings</strong>. So they say: '
      '<strong>what is named by «saying» and «speech», unrestrictedly, is a name for the '
      'utterance alone</strong>; and <strong>the meaning is not a part of what it names, but '
      'rather what the name points to.</strong></em>') +
    p('<em>Then he mentioned <strong>the opposing madhhab</strong>, saying <strong>%s</strong> — '
      '<em>as is the madhhab of the Kullābiyyah and the Ashāʿirah, as was explained above.</em></em>'
      % ar('وَلَا المَعَانِي دُونَ الحُرُوفِ')) +
    p('So the author closes the <em>fasl</em> by placing two errors against each other, and the '
      'symmetry is worth seeing laid out:') +
    '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;'
    'font-size:.91rem;margin:0 0 .7rem">'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>المُعْتَزِلَة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">the letters '
    '<strong>without</strong> the meanings</td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap"'
    ' dir="rtl" lang="ar"><strong>الكُلَّابِيَّةُ وَالأَشَاعِرَة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line)">the meanings '
    '<strong>without</strong> the letters</td></tr>'
    '<tr><td style="padding:.6rem .78rem;border:1px solid var(--line);white-space:nowrap;'
    'background:var(--brand-wash)" dir="rtl" lang="ar">'
    '<strong>أَهْلُ السُّنَّةِ وَالجَمَاعَة</strong></td>'
    '<td style="padding:.6rem .78rem;border:1px solid var(--line);'
    'background:var(--brand-wash)"><strong>the Qurʾān is the speech of Allah, '
    'its letters AND its meanings</strong></td></tr>'
    '</table></div>' +
    p('<em>And <strong>%s</strong> — <strong>the true madhhab is that the Qurʾān is the speech of '
      'Allah, its letters and its meanings</strong>, as is the statement of Ahl al-Sunnah '
      'wa-l-Jamāʿah, <strong>and it is that upon which the proofs from the Book and the Sunnah '
      'have stood.</strong> وَالحَمْدُ لِلَّهِ رَبِّ العَالَمِينَ.</em>'
      % ar('المَذْهَبُ الحَقّ')) +
    p('And there is the pattern of Lesson 30 again, in a fifth place. '
      '<strong>Two parties each hold one half of a thing that was never two things.</strong> The '
      'Muʿtazilah kept the words you can hear and emptied them of a Speaker\'s meaning; the '
      'Ashāʿirah kept an inner meaning and cut it off from every word you can hear. '
      '<strong>And Ahl al-Sunnah, holding both, are the only ones for whom the Qurʾān in your '
      'hands is what the Qurʾān says it is.</strong>'))

b += B.vocab([
    ('نَوْعُ الكَلَام', 'nawʿ al-kalām', 'the kind of the speech',
     'أزلي أبدي — beginningless and endless'),
    ('مُفْرَدَاتُه', 'mufradātuh', 'its individual instances',
     'Occurring one after another, by His wisdom — which is how speech is both dhātī '
     'and fiʿlī'),
    ('مِنْهُ بَدَأ', 'minhu badaʺ', 'from Him it began',
     'The مِنْ is لِابْتِدَاءِ الغَايَة — FROM Him, not through Him'),
    ('حِكَايَة', 'ḥikāyah', 'a recounting',
     'The Kullābiyyah’s word for the recited Qurʾān — rejected'),
    ('عِبَارَة', 'ʿibārah', 'an expression',
     'The Ashāʿirah’s word for it — also rejected'),
    ('مُبْتَدِئ', 'mubtadiʾ', 'the originator',
     'Speech is ascribed in reality to him — not to the conveyer'),
    ('مُبَلِّغٌ مُؤَدٍّ', 'muballighun muʾaddin', 'a conveying transmitter',
     'Called a وَاسِطَة, a means, and nothing more'),
    ('خِلَافٌ لَفْظِيّ', 'khilāf lafẓī', 'a merely verbal difference',
     'What some scholars judged the Kullābiyyah/Ashāʿirah dispute to be'),
])
b += B.mcq('ws-l34', [
    ('Why does this belief fall under two pillars of faith at once?',
     ['Because the Qurʾān mentions both',
      'Belief in Allah comprises belief in His attributes, and speech is one; and the Qurʾān is '
      'the greatest of His Books',
      'Because it was revealed to a messenger',
      'Because the angels brought it'], 1),
    ('How does the distinction between %s and %s resolve Lesson 19’s difficulty?'
     % (ar('نَوْعُ الكَلَام'), ar('مُفْرَدَاتُه')),
     ['By making speech an attribute of the Essence only',
      'The kind never began, so speech is dhātī; each instance occurs by His will at a time, so '
      'it is also fiʿlī — He addressed Mūsā at an hour without having become a Speaker',
      'By leaving the question unanswered',
      'By making the Qurʾān pre-eternal in its letters'], 1),
    ('What exactly do the Jahmiyyah say?',
     ['That the Qurʾān is a recounting of Allah’s speech',
      'That Allah does not speak at all — He created a speech in another and made it express Him, '
      'so "speaker" means "creator of speech in another"',
      'That the letters are created and the meanings are not',
      'That the Qurʾān is the letters without the meanings'], 1),
    ('What is al-Fawzān’s refutation of them?',
     ['That the Companions rejected it',
      'That no one is intelligibly called a speaker except one in whom the speech really subsists '
      '— so how is it said "Allah said" while the sayer is someone else?',
      'That it contradicts the consensus only',
      'That it makes the Qurʾān eternal'], 1),
    ('What are the two meanings al-Fawzān gives for %s?' % ar('وَإِلَيْهِ يَعُودُ'),
     ['That it returns to the Preserved Tablet, or to Jibrīl',
      'That it will be raised up at the end of time so that nothing of it remains in the breasts '
      'or the copies — among the signs of the Hour; or that it is ascribed to Him',
      'That it returns to the Arabs, or to the Prophet ﷺ',
      'That its rulings are abrogated, or its recitation ceases'], 1),
    ('What does the Kullābiyyah/Ashʿarī "single undivided meaning" cost?',
     ['Nothing; it is a merely verbal matter',
      'It makes the Torah and the Qurʾān the same thing, the command and the prohibition the same '
      'thing — and nothing you have recited any of it',
      'It makes the Qurʾān created',
      'It denies that Allah has knowledge'], 1),
    ('What is the author’s proof that the recited Qurʾān remains Allah’s speech?',
     ['That the Companions recited it as such',
      'That speech is ascribed in reality to the one who said it as originator, not to the '
      'conveyer — and al-Tawbah 9:6 calls what the mushrik hears, by means of a transmitter, "the '
      'speech of Allah"',
      'That the muṣḥaf is not to be touched without purity',
      'That the Qurʾān is inimitable'], 1),
    ('What is the symmetry between the Muʿtazilah and the Ashāʿirah here?',
     ['Both say the Qurʾān is created',
      'The Muʿtazilah say the letters without the meanings; the Kullābiyyah and Ashāʿirah say the '
      'meanings without the letters',
      'Both deny that Allah speaks at all',
      'Both affirm the letters and deny the Speaker'], 1),
])
b += B.tf('ws-l34-tf', [
    ('كَلَامُ اللهِ غَيْرُ مَخْلُوقٍ لِأَنَّ صِفَاتِهِ غَيْرُ مَخْلُوقَةٍ.',
     'Allah’s speech is uncreated because His attributes are uncreated.', True),
    ('إِذَا كَتَبَ النَّاسُ القُرْآنَ فِي المَصَاحِفِ خَرَجَ عَنْ كَوْنِهِ كَلَامَ اللهِ.',
     'When people write the Qurʾān in copies it ceases to be the speech of Allah.', False),
    ('الكَلَامُ يُضَافُ حَقِيقَةً إِلَى المُبَلِّغِ المُؤَدِّي.',
     'Speech is ascribed in reality to the conveying transmitter.', False),
    ('المَذْهَبُ الحَقُّ أَنَّ القُرْآنَ كَلَامُ اللهِ حُرُوفُهُ وَمَعَانِيهِ.',
     'The true position is that the Qurʾān is Allah’s speech, its letters and its meanings.',
     True),
])
b += B.memorize(
    'وَهُوَ كَلَامُ اللهِ حُرُوفُهُ وَمَعَانِيهِ، لَيْسَ كَلَامُ اللهِ الحُرُوفَ دُونَ '
    'المَعَانِي، وَلَا المَعَانِي دُونَ الحُرُوفِ',
    'The author states the creed and both errors in one sentence, which is why it is worth having '
    'word for word. And notice what it secures: that the Book in your hands, in the letters you '
    'can see, is the speech of Allah — not a report of it.')
b += B.aiquiz('That the Quran is the speech of Allah in reality in al-Aqidah al-Wasitiyyah: why '
              'it falls under two pillars at once, the distinction between the KIND of the speech '
              'which is azali abadi and its individual instances which occur successively, minhu '
              'badaa wa-ilayhi yaud with both meanings, the Jahmiyyah that He created a speech in '
              'another, the Kullabiyyah hikayah and the Ashaira ibarah with the single undivided '
              'meaning, the Mutazilah letters without meanings, and the proof from al-Tawbah 9:6 '
              'that speech is ascribed to the originator and not the conveyer')
b += B.further()
b += B.nav('was-l33-qurb.html', 'The Obligation of Believing in His Nearness',
           'wasitiyyah-index.html', 'Back to the track overview', 'ws-l34')

io.open(os.path.join(B.AQ, 'was-l34-quran-kalam-haqiqatan.html'), 'w', encoding='utf-8',
        newline='\n').write(B.shell(
    'القُرْآنُ كَلَامُ اللهِ حَقِيقَةً · حُرُوفُهُ وَمَعَانِيه',
    'The Qurʾān Is Allah’s Speech in Reality — Its Letters and Its Meanings',
    'Lesson 34 of al-ʿAqīdah al-Wāsiṭiyyah: the distinction '
    'between the kind of Allah’s speech and its instances, which lets Ahl al-Sunnah hold '
    'both halves at once; the four opposing positions and what each one costs; and the '
    'author’s proof that speech is ascribed to the one who originated it, not to the one who '
    'conveys it.',
    B.card('الوَاسِطِيَّة · الدَّرْسُ الرَّابِعُ وَالثَّلَاثُون', '3',
           'القُرْآنُ كَلَامُ اللهِ حَقِيقَةً · حُرُوفُهُ وَمَعَانِيه',
           'The Qurʾān Is Allah’s Speech in Reality — Its Letters and Its Meanings', b,
           back='wasitiyyah-index.html', back_label='العَقِيدَةُ الوَاسِطِيَّة')))
print('wrote was-l34-quran-kalam-haqiqatan.html')
